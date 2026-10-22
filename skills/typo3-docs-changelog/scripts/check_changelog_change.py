#!/usr/bin/env python3
"""
Check a documentation change for a Changelog-To-Doc issue against what the
documentation team accepted in earlier changes: the version directive and
its :changelog: identifier, the size of a Deprecation, Breaking, or
Important change compared with the changelog entry, sentences said twice,
includes missing on a backport branch, and the commit message.

Usage:
    python3 check_changelog_change.py ISSUE [--repo DIR] [--base REV]

ISSUE is the issue number or its URL. DIR is the clone of the manual,
default the current directory. REV is the branch the change is based on,
default main of the remote that points to the TYPO3-Documentation
repository, which is "upstream" in a clone of a fork. The script compares the working tree, committed or
not, with the merge base of REV and HEAD. It names untracked files but
does not check them. It reads the summary of the
oldest commit after the merge base and the trailers of all of them.

Each finding is a line that starts with FIX or CHECK. FIX breaks a rule of
the guide. CHECK is a deviation from what earlier accepted changes did;
keep it only for a reason that you can name. The exit code is 1 when a
FIX line was printed.
"""

import argparse
import difflib
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import changelog_issue as ci  # noqa: E402

# Median hand-written rst lines added per changelog line, measured on 40
# merged changes from 2023 to 2026 (human changes before 2025 for the
# non-Feature types, all changes for Feature).
TYPICAL_RATIO = {'Feature': 0.8, 'Deprecation': 0.2, 'Breaking': 0.2,
                 'Important': 0.25}
DIRECTIVE = {'Feature': ('versionadded', ':added:'),
             'Deprecation': ('deprecated', ':deprecated:'),
             'Breaking': ('versionchanged', ':changed:', ':removed:'),
             'Important': ('versionchanged', ':changed:')}
DROPPED_SECTION = 'Affected installations'


def git(repo, *args):
    r = subprocess.run(['git', '-C', repo] + list(args), capture_output=True,
                       text=True)
    if r.returncode != 0:
        sys.exit('git %s failed: %s' % (' '.join(args), r.stderr.strip()))
    return r.stdout


def changelog_text(issue):
    """{path: (type, folder, rst)} of the added changelog files."""
    body = issue.get('body') or ''
    out = {}
    for path, text in ci.split_files(body, 'Added files').items():
        name = ci.NAME_RE.search(path)
        if name:
            out[path] = (name.group('type'), path.split('/')[0], text)
    return out


def section_texts(rst):
    heads = [(m.start(), m.group(1).strip())
             for m in ci.HEADLINE_RE.finditer(rst)
             if m.group(2).startswith('=') and not m.group(1).startswith('=')]
    out = {}
    for i, (pos, name) in enumerate(heads):
        end = heads[i + 1][0] if i + 1 < len(heads) else len(rst)
        out[name] = rst[pos:end]
    return out


def marked_with(text, names):
    """Whether the text uses one of the directives or confval options, such
    as "versionadded" or ":added:". The word "deprecated" in a sentence is
    no directive."""
    for name in names:
        pattern = re.escape(name) + r'\s' if name.startswith(':') \
            else r'\.\.\s+' + name + '::'
        if re.search(pattern, text):
            return True
    return False


def words(text):
    text = re.sub(r':\w[\w-]*:`([^`]*)`', r'\1', text)
    return re.findall(r"[a-z0-9_]+", text.lower())


def shingles(text, n=6):
    w = words(text)
    return {tuple(w[i:i + n]) for i in range(len(w) - n + 1)}


def rst_diff(diff):
    """({file: [added lines]}, {file: [removed lines]}, {file: [line
    numbers of the added lines]}) of hand-written reST files in a unified
    diff."""
    added, removed, numbers, current, no = {}, {}, {}, None, 0
    old_path = None
    for line in diff.splitlines():
        if line.startswith('--- '):
            old_path = line[6:] if line.startswith('--- a/') else None
            continue
        if line.startswith('+++ '):
            # A deleted file has "+++ /dev/null"; its text counts as
            # removed, so that text moved out of it is not new.
            path = line[6:] if line.startswith('+++ b/') else old_path
            current = path if path and re.search(r'\.rst(\.txt)?$', path) \
                and '/CodeSnippets/' not in path else None
            if current:
                added.setdefault(current, [])
                removed.setdefault(current, [])
                numbers.setdefault(current, [])
        elif line.startswith('@@'):
            no = int(re.search(r'\+(\d+)', line).group(1))
        elif current and line.startswith('+'):
            added[current].append(line[1:])
            numbers[current].append(no)
            no += 1
        elif current and line.startswith('-'):
            removed[current].append(line[1:])
        elif not line.startswith('\\'):
            no += 1
    return added, removed, numbers


def new_lines(added, removed):
    """Added lines, not counting text that was only rewrapped or moved,
    also into another file such as 404.rst: the words that the change
    inserts, at 9 words per line of reST."""
    old = words('\n'.join(l for ls in removed.values() for l in ls))
    new = words('\n'.join(l for ls in added.values() for l in ls))
    ops = difflib.SequenceMatcher(None, old, new, autojunk=False)
    count = sum(j2 - j1 for tag, _i1, _i2, j1, j2 in ops.get_opcodes()
                if tag in ('insert', 'replace'))
    return round(count / 9)


def prose(lines, for_versions=False):
    """The running text of reST lines, without directives, their options,
    and the bodies of code blocks. The items of a list are parallel by
    design, so they are left out, unless for_versions is set: then list
    items stay, and the bodies of version directives, which may name the
    version before the change, are left out."""
    skipped = r'code-block|literalinclude'
    if for_versions:
        skipped += r'|versionadded|versionchanged|deprecated'
    out, skip_indent = [], None
    for line in lines:
        indent = len(line) - len(line.lstrip())
        if skip_indent is not None:
            if not line.strip() or indent > skip_indent:
                continue
            skip_indent = None
        if re.match(r'\s*\.\.\s+(%s)::' % skipped, line):
            skip_indent = indent
            continue
        if for_versions:
            line = re.sub(r'^\s*([*+-]|#\.|\d+\.)\s+', '', line)
        # Directives, their options, headline underlines, and list items.
        if re.match(r'\s*(\.\.\s|:[\w-]+:\s|[*+-]\s|#\.\s|\d+\.\s)', line) \
                or re.fullmatch(r'\s*([=\-~^"#*+])\1*\s*', line):
            out.append('')
            continue
        out.append(line.strip())
    return '\n'.join(out)


def sentences(text):
    text = re.sub(r'\n(?!\n)', ' ', text)
    out = []
    for part in re.split(r'(?<=[.!?])\s+|\n\n+', text):
        part = part.strip(' *-#')
        if len(part.split()) >= 8:
            out.append(part)
    return out


def norm(s):
    return ' '.join(words(s))


def tokens(text):
    """The words of a sentence, with each role or inline literal as one
    word: a path such as `config/system/resources.php` is one name."""
    text = re.sub(r'(:\w[\w-]*:)?``?[^`]+``?', ' code ', text)
    return [w for w in re.findall(r'[a-z0-9_]+', text.lower())]


def parallel(a, b):
    """Two sentences that differ in two words at most, not counting the
    names in roles and literals, describe parallel things, such as the
    template, layout, and partial paths."""
    ops = [op for op in difflib.SequenceMatcher(
        None, tokens(a), tokens(b)).get_opcodes() if op[0] != 'equal']
    # A word that is only added or left out is no parallel thing.
    return all(op[0] == 'replace' for op in ops) and \
        sum(op[2] - op[1] for op in ops) <= 2 and \
        sum(op[4] - op[3] for op in ops) <= 2


def repeated(repo, added):
    """Pairs of near-identical sentences: within the added text, and
    between the added text and the rest of the same file."""
    found = []
    for path, lines in added.items():
        new = sentences(prose(lines))
        try:
            with open(os.path.join(repo, path), encoding='utf-8') as fh:
                rest = fh.read().splitlines()
        except OSError:
            rest = []
        # The text that was there before: the file without the added lines.
        for line in lines:
            if line.strip() and line in rest:
                rest.remove(line)
        old = sentences(prose(rest))
        for i, a in enumerate(new):
            for b in new[i + 1:] + old:
                if norm(a) == norm(b) or difflib.SequenceMatcher(
                        None, norm(a), norm(b)).ratio() >= 0.8 and \
                        not parallel(a, b):
                    found.append((path, a, b))
                    break
    return found


def missing_includes(repo, added, branches, new_files, remote,
                     untracked=()):
    """(file, target, where) of included files that do not exist in the
    working tree, that are not added to git, or that do not exist on a
    version branch the change is backported to."""
    out = []
    for path, lines in added.items():
        for line in lines:
            m = re.match(r'\s*\.\.\s+(?:literal)?include::\s*(\S+)', line)
            if not m:
                continue
            target = m.group(1)
            if target.startswith('/'):
                rel = os.path.join('Documentation', target.lstrip('/'))
            else:
                rel = os.path.join(os.path.dirname(path), target)
            rel = os.path.normpath(rel)
            if not os.path.exists(os.path.join(repo, rel)):
                out.append((path, target, 'this branch'))
                continue
            if rel in untracked:
                out.append((path, target, 'any branch: it is not added to '
                            'git. Add and commit it'))
                continue
            if rel in new_files:
                continue
            for branch in branches:
                r = subprocess.run(['git', '-C', repo, 'cat-file', '-e',
                                    '%s/%s:%s' % (remote, branch, rel)],
                                   capture_output=True)
                if r.returncode != 0:
                    out.append((path, target, branch))
    return out


def backport_branches(repo, msg, remote):
    """([branches], [branches not fetched]): the version branches named in
    the Releases: trailer, split by whether <remote>/<branch> exists."""
    m = re.search(r'^Releases:\s*(.+)$', msg or '', re.M)
    if not m:
        return [], []
    found, missing = [], []
    for name in re.split(r'[,\s]+', m.group(1).strip()):
        if re.fullmatch(r'\d+\.\d+', name):
            exists = subprocess.run(
                ['git', '-C', repo, 'rev-parse', '-q', '--verify',
                 '%s/%s' % (remote, name)], capture_output=True).returncode
            (missing if exists else found).append(name)
    return found, missing


def version_bodies(repo, numbers):
    """{file: {line numbers}} of lines inside the body of a version
    directive in the working tree, also of a directive the change does not
    add."""
    out = {}
    for path in numbers:
        try:
            with open(os.path.join(repo, path), encoding='utf-8') as fh:
                whole = fh.read().splitlines()
        except OSError:
            continue
        inside, body_indent = set(), None
        for no, line in enumerate(whole, 1):
            indent = len(line) - len(line.lstrip())
            if body_indent is not None and line.strip() and \
                    indent <= body_indent:
                body_indent = None
            if body_indent is not None:
                inside.add(no)
            if re.match(r'\s*\.\.\s+(versionadded|versionchanged|'
                        r'deprecated)::', line):
                body_indent = indent
        out[path] = inside
    return out


def directives_in_confvals(repo, numbers):
    """Whether an added version directive is inside a confval, also in a
    confval that the change does not add. numbers: {file: [line numbers
    of the added lines]}."""
    for path, nos in numbers.items():
        try:
            with open(os.path.join(repo, path), encoding='utf-8') as fh:
                whole = fh.read().splitlines()
        except OSError:
            continue
        inside, conf_indent = set(), None
        for no, line in enumerate(whole, 1):
            indent = len(line) - len(line.lstrip())
            if conf_indent is not None and line.strip() and \
                    indent <= conf_indent:
                conf_indent = None
            if conf_indent is not None:
                inside.add(no)
            if re.match(r'\s*\.\.\s+confval::', line):
                conf_indent = indent
        for no in nos:
            if no in inside and re.match(
                    r'\s*\.\.\s+(versionadded|versionchanged|deprecated)::',
                    whole[no - 1]):
                return True
    return False


def check(info, issue, repo, base, branches=None, versioned=None):
    """branches: the docs branches of this change. versioned: whether the
    manual has version branches at all; None when unknown."""
    findings = []
    merge_base = git(repo, 'merge-base', base, 'HEAD').strip()
    # Fixed prefixes: the user's git config may change or drop them.
    diff = git(repo, 'diff', '--no-color', '--no-ext-diff', '--no-renames',
               '--src-prefix=a/', '--dst-prefix=b/', merge_base, '--',
               'Documentation')
    added, removed, numbers = rst_diff(diff)
    untracked = [p for p in git(repo, 'ls-files', '-z', '--others',
                                '--exclude-standard', '--',
                                'Documentation').split('\0') if p]
    if untracked:
        findings.append('CHECK Not added to git, so not checked: %s. Run '
                        '"git add -N" on them and run the check again.'
                        % ', '.join(untracked))
    lines = [l for ls in added.values() for l in ls]
    text = '\n'.join(lines)
    written = new_lines(added, removed)
    # An issue that only modifies changelog files has no new entry to mark.
    entries = changelog_text(issue)

    releases = ci.first_releases(issue.get('body') or '') if any(
        f.endswith('.x') for _t, f, _r in entries.values()) else None
    ids = {}
    for path, (ctype, folder, rst) in entries.items():
        anchor = ci.ANCHOR_RE.search(rst)
        ids[path] = anchor.group(1) if anchor else None
    used = {p for p, i in ids.items() if i and i in text}
    if entries and not used:
        findings.append('CHECK No version directive or confval option names '
                        'the :changelog: identifier of an entry: %s.'
                        % ', '.join(i for i in ids.values() if i))
    elif len(used) < len(entries):
        findings.append('CHECK The change does not name %s. Document that '
                        'entry too, or name in the commit body why it needs '
                        'no documentation.' % ', '.join(
                            ids[p] for p in entries if p not in used))

    # Only for these types do accepted AI-assisted changes run longer than
    # human ones; Feature changes of both are the same size.
    documented = [entries[p] for p in used] or list(entries.values())
    types = {ctype for ctype, _f, _r in documented}
    if documented and 'Feature' not in types:
        cl_lines = sum(len([l for l in rst.splitlines() if l.strip()])
                       for _t, _f, rst in documented)
        expected = sum(TYPICAL_RATIO.get(ctype, 0.25) * len(
            [l for l in rst.splitlines() if l.strip()])
            for ctype, _f, rst in documented)
        if written > 3 * expected and written > 15:
            findings.append(
                'CHECK About %d lines of new text for %d lines of %s '
                'entries. Accepted changes of this type add about %d. Remove '
                'what the reader of this page does not act on, such as '
                'how the change came about or how the Core works inside.' % (
                    written, cl_lines, '/'.join(sorted(types)),
                    round(expected)))

    for path, (ctype, folder, rst) in entries.items():
        cl_id = ids[path]
        if entries and used and path not in used:
            continue
        # Reviewers ask to keep the changelog's lead sentence, lists, cases,
        # and defaults, so copied text is no finding by itself. Only the
        # section about affected installations is left out of manuals.
        sec = section_texts(rst).get(DROPPED_SECTION, '')
        if len(shingles(sec) & shingles(text)) >= 8:
            findings.append(
                'CHECK Text from the changelog section "%s" is in the '
                'change. Accepted changes leave it out.' % DROPPED_SECTION)
        removed_to_404 = any(f.endswith('/404.rst') for f in added)
        if cl_id and not removed_to_404 and \
                not marked_with(text, DIRECTIVE.get(ctype, ())):
            findings.append('CHECK A %s entry is usually marked with %s.' % (
                ctype, ' or '.join(DIRECTIVE[ctype])))
        version = re.sub(r'\.x$', '', folder)
        # The patch release of a .x folder: shipped, next, or unknown.
        expected, shipped, released = None, None, False
        if not folder.endswith('.x'):
            pass
        elif not releases:  # None, or no change in Gerrit
            shipped = 'Gerrit gave no release for it. Find the first ' \
                'release that contains it under "Included In" in Gerrit'
        elif version not in releases and ci.trailer_names(info, version):
            expected = ci.next_patch(version)
            shipped = 'Gerrit shows no change on branch %s yet, although ' \
                'the Releases: trailer names it, so use the next release ' \
                'of branch %s, %s' % (version, version,
                                      expected or 'see Gerrit')
        elif version not in releases:
            shipped = 'Gerrit shows the change on no branch %s, so the ' \
                'commit may copy an entry of an earlier change. Take the ' \
                'release of that change' % version
        elif releases[version]:
            expected, released = releases[version].lstrip('v'), True
            shipped = 'the release %s shipped it' % expected
        else:
            expected = ci.next_patch(version)
            shipped = 'no release contains it yet, so use the next release ' \
                'of branch %s, %s' % (version, expected or 'see Gerrit')
        if shipped and not re.search(
                r'(::|:added:|:changed:|:deprecated:|:removed:)\s*'
                + re.escape(version) + r'\.\d+', text):
            findings.append('CHECK The entry is in the folder %s: %s. '
                            'Accepted changes name this patch version in the '
                            'directive.' % (folder, shipped))
        if not cl_id:
            continue
        # Only the directives and confval options of this entry.
        marks = re.findall(
            r'\.\.\s+(?:versionadded|versionchanged|deprecated)::\s*(\S+)'
            r'\s*\n\s*:changelog:\s*' + re.escape(cl_id), text) + \
            re.findall(r':(?:added|changed|deprecated|removed):\s*(\S+)\s+'
                       + re.escape(cl_id), text)
        for mark in marks:
            if not re.fullmatch(r'\d+\.\d+(\.\d+)?', mark):
                findings.append('FIX "%s" is no version. Write it as 14.3 or '
                                '14.3.7.' % mark)
            elif not mark.startswith(version):
                findings.append('CHECK The version %s of %s differs from the '
                                'changelog folder %s.'
                                % (mark, cl_id, folder))
            elif not folder.endswith('.x') and mark != version:
                findings.append('CHECK The version %s of %s: an entry of the '
                                'folder %s names %s.'
                                % (mark, cl_id, folder, version))
            elif expected and mark.count('.') == 2 and mark != expected:
                findings.append('CHECK The version %s of %s differs from %s.'
                                % (mark, cl_id, (
                                    'the first release that contains it, '
                                    + expected) if released else (
                                    'the next release of branch %s, %s; no '
                                    'release contains it yet'
                                    % (version, expected))))

    if re.search(r'docs\.typo3\.org/[^\s>]*changelog', text, re.I):
        findings.append('CHECK A link to the changelog in the text. The '
                        ':changelog: option links the entry already.')
    for path, a, b in repeated(repo, added):
        findings.append('CHECK %s says the same thing twice. Keep one of: '
                        '"%s" / "%s"' % (path, a[:90], b[:90]))
    log = git(repo, 'log', '--no-show-signature', '--format=%B',
              merge_base + '..HEAD')
    new_files = set(git(repo, 'diff', '--name-only', '-z', '--no-renames',
                        '--diff-filter=A', merge_base).split('\0'))
    remote = base.split('/', 1)[0] if '/' in base else 'origin'
    backports, not_fetched = backport_branches(repo, log, remote)
    if not_fetched:
        findings.append('CHECK %s not found, so the includes were not '
                        'checked there. Fetch the remote %s.' % (
                            ', '.join('%s/%s' % (remote, b)
                                      for b in not_fetched), remote))
    for path, target, branch in missing_includes(
            repo, added, backports, new_files, remote, untracked):
        findings.append('FIX %s includes %s, which does not exist on %s.'
                        % (path, target, branch))
    bodies = version_bodies(repo, numbers)
    running = '\n'.join(prose(
        [l for l, no in zip(added[p], numbers[p])
         if no not in bodies.get(p, ())], for_versions=True) for p in added)
    # Not an IP address such as 127.0.0.1, and not an inline literal.
    running = re.sub(r'``?[^`]*``?', '', running)
    for m in re.finditer(r'(?<![\d.])\d+\.\d+\.\d+(?![\d.]*\d)', running):
        findings.append('CHECK The version %s in the running text. The '
                        'version directive names the exact version. Leave it '
                        'out of the text, or name only as much of it as the '
                        'reader needs, such as "Fluid 5".' % m.group(0))
        break
    if ':issue:`' in text:
        findings.append('CHECK An :issue: role. Accepted changes link the '
                        'changelog entry with :changelog:, not the Forge '
                        'issue.')
    if directives_in_confvals(repo, numbers):
        findings.append('CHECK A version directive inside a confval. Mark '
                        'the version with the confval options :added:, '
                        ':changed:, :deprecated:, or :removed:. Keep the '
                        'directive only for text about the version change, '
                        'such as how to migrate.')

    commits = git(repo, 'rev-list', '--reverse', merge_base + '..HEAD').split()
    if commits:
        # The pull request holds only what is committed.
        pending, entries_z = [], git(repo, 'status', '--porcelain', '-z',
                                     '--', 'Documentation').split('\0')
        while entries_z:
            entry = entries_z.pop(0)
            if any(c in 'RC' for c in entry[:2]) and entries_z:
                entries_z.pop(0)  # the old path of a rename or copy
            if len(entry) > 3 and not entry.startswith('??'):
                pending.append(entry[3:])
        if pending:
            findings.append('CHECK Not committed: %s. The pull request holds '
                            'only committed files; the check above read the '
                            'working tree.' % ', '.join(pending))
        # The oldest commit carries the summary of the change; fixups that
        # follow it are squashed into it before the merge.
        first = git(repo, 'log', '--no-show-signature', '-1', '--format=%B',
                    commits[0])
        msg = git(repo, 'log', '--no-show-signature', '--format=%B',
                  merge_base + '..HEAD')
        subject = first.splitlines()[0] if first else ''
        # A squash merge on GitHub appends the pull request number.
        subject = re.sub(r'\s+\(#\d+\)$', '', subject.strip())
        if subject != info['title'].strip():
            findings.append('FIX The commit summary is not the issue title. '
                            'Use: %s' % info['title'])
        # Accepted changes name the issue in one of these trailers.
        if not re.search(r'^(Resolves|References|Related):\s*'
                         + re.escape(info['url']) + r'/?\s*$', msg, re.M):
            findings.append('FIX The commit message does not name the issue. '
                            'Add "Resolves: %s".' % info['url'])
        trailer = re.search(r'^Releases:\s*(.*)$', msg, re.M)
        if not trailer and versioned:
            findings.append('FIX No "Releases:" trailer. Name every branch '
                            'that changelog_issue.py printed.')
        elif not trailer and versioned is None:
            findings.append('CHECK No "Releases:" trailer. A manual with '
                            'version branches needs it.')
        elif branches:
            named = set(re.split(r'[,\s]+', trailer.group(1).strip()))
            missing = [b for b in branches if b not in named]
            if missing:
                findings.append('CHECK The "Releases:" trailer does not name '
                                '%s. The docs branches for this change are: '
                                '%s.' % (', '.join(missing),
                                         ', '.join(branches)))
    else:
        findings.append('CHECK Nothing committed yet; the commit message was '
                        'not checked.')
    return findings, written, sorted(added)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    ap.add_argument('issue')
    ap.add_argument('--repo', default='.')
    ap.add_argument('--base')
    args = ap.parse_args()
    ci.TOKEN = ci.token()
    issue = ci.get_issue(ci.issue_number(args.issue))
    info = ci.parse_issue(issue)
    # The docs branches of this manual, as changelog_issue.py prints them.
    remote, repo = ci.upstream_remote(args.repo)
    if not args.base and not remote:
        sys.exit('No remote points to a TYPO3-Documentation repository. The '
                 'check is for the manuals of TYPO3-Documentation; a manual '
                 'inside the Core changes through Gerrit. For a fork without '
                 'that remote, pass --base.')
    base = args.base or remote + '/main'
    names = ci.repo_branches(repo) if repo else None
    branches = ci.branches(repo, ci.change_folders(info)) \
        if repo else None
    versioned = any(re.fullmatch(r'\d+\.\d+', n) for n in names) \
        if names is not None else None
    findings, count, files = check(info, issue, args.repo, base,
                                   branches, versioned)
    print('#%d %s' % (info['number'], info['title']))
    print('About %d lines of new reST text in: %s'
          % (count, ', '.join(files) or 'none'))
    for f in findings:
        print(f)
    if not findings:
        print('No findings.')
    sys.exit(1 if any(f.startswith('FIX') for f in findings) else 0)


if __name__ == '__main__':
    main()
