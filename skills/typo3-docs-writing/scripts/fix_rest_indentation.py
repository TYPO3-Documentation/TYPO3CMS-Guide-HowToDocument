#!/usr/bin/env python3
"""
Fix the indentation of reST files the way the coding guidelines ask for it
(anchor "cgl-indenting" and "rest-cgl-headline-underlines"):

*   two spaces after "..": "..  code-block:: php", "..  _some-anchor:"
*   4 spaces per reST level: directive bodies and options, definition
    bodies, and block quotes
*   list markers padded to 4 columns: "*   item", "#.  item", "1.  item"
*   headline over- and underlines exactly as long as the headline

The content of code blocks, literal blocks after "::", and comments keeps
its relative indentation, so code examples are not changed. The script does
not put headline levels into order, and it does not wrap long lines.

Usage:
    python3 fix_rest_indentation.py PATH [PATH ...] [--check]

A PATH is a .rst file or a directory, which is searched for .rst files.
The files are changed in place. With --check, nothing is written: the
script lists the files it would change and exits with 1 if there are any.

Files that contain merge conflict markers are skipped, because a "======="
marker looks like a headline underline.

The result renders the same as before, except where the old markup was
broken. Render the manual before and after and compare the HTML.
"""

import argparse
import os
import re
import sys

LITERAL_DIRECTIVES = ('code-block', 'code', 'sourcecode', 'parsed-literal', 'literalinclude', 'raw', 'math', 'csv-table')
ADORN = re.compile(r'^([=\-~"\'^#*+`:.])\1{2,}$')
LIST = re.compile(r'^([*\-+•]|#\.|\d+\.|[a-zA-Z]\.|\(\d+\))( +)(\S.*)$')
MARK = re.compile(r'^\.\.(?: +(.*))?$')
CONFLICT = re.compile(r'^(<{7}|>{7}|\|{7})( |$)', re.MULTILINE)


def ind(s):
    return len(s) - len(s.lstrip(' '))


def fix(lines):
    out = []
    # A frame is one indentation level: its column in the input ("old"),
    # its column in the output ("new"), whether its content is literal, and
    # the column of the list marker that opened it.
    stack = [dict(old=0, new=0, lit=False, list_x=None)]
    prev_blank = True
    pending_literal = False
    n = len(lines)
    i = 0

    def next_nonblank(k):
        while k < n and lines[k].strip() == '':
            k += 1
        return k

    while i < n:
        raw = lines[i]
        if raw.strip() == '':
            out.append('')
            prev_blank = True
            i += 1
            continue
        x = ind(raw)
        text = raw.lstrip(' ')
        popped_list_xs = set()
        while len(stack) > 1 and x < stack[-1]['old']:
            f = stack.pop()
            if f['list_x'] is not None:
                popped_list_xs.add(f['list_x'])
        top = stack[-1]
        if top['lit']:
            pad = ' ' * (top['new'] + x - top['old'])
            out.append(pad + (text if raw.endswith(' ') else text.rstrip(' ')))
            prev_blank = False
            i += 1
            continue
        if pending_literal and x > top['old'] and prev_blank:
            stack.append(dict(old=x, new=top['new'] + 4, lit=True, list_x=None))
            pending_literal = False
            continue
        pending_literal = False
        new_frame = False
        if x > top['old']:
            # Indented without a known opener: definition body, block quote,
            # or the continuation of an option.
            new_frame = True
            stack.append(dict(old=x, new=top['new'] + 4, lit=False, list_x=None))
            top = stack[-1]
        X = top['new'] if x != top['old'] else top['new'] + (x - top['old'])
        m = MARK.match(text.rstrip())
        if m and not (len(text) > 2 and text[2] != ' '):
            rest = m.group(1)
            if rest is None or rest.strip() == '':
                out.append(' ' * X + '..')
                # An empty comment: an indented block right below is its body.
                k = next_nonblank(i + 1)
                if k == i + 1 and k < n and ind(lines[k]) > x:
                    stack.append(dict(old=ind(lines[k]), new=X + 4, lit=True, list_x=None))
                prev_blank = False
                i += 1
                continue
            out.append(' ' * X + '..  ' + rest.rstrip())
            dm = re.match(r'^([\w:.-]+)::', rest)
            is_dir = bool(dm) or re.match(r'^\|[^|]+\|\s+[\w:.-]+::', rest)
            is_target = rest.startswith('_') or rest.startswith('[')
            name = dm.group(1) if dm else ''
            lit = (not is_dir and not is_target) or name in LITERAL_DIRECTIVES
            k = next_nonblank(i + 1)
            if k < n and ind(lines[k]) > x:
                stack.append(dict(old=ind(lines[k]), new=X + 4, lit=lit, list_x=None))
            prev_blank = False
            i += 1
            continue
        lm = LIST.match(text.rstrip())
        if lm and (prev_blank or new_frame or x in popped_list_xs or any(f['list_x'] == x for f in stack)):
            ox, nx, line_out = x, X, ''
            while lm:
                marker, sp, body = lm.groups()
                gap = ' ' if len(marker) >= 4 else ' ' * (4 - len(marker))
                line_out += marker + gap
                stack.append(dict(old=ox + len(marker) + len(sp), new=nx + len(marker) + len(gap), lit=False, list_x=ox))
                ox, nx = ox + len(marker) + len(sp), nx + len(marker) + len(gap)
                lm = LIST.match(body) if re.match(r'^([*\-+]|#\.)( +)\S', body) else None
            out.append(' ' * X + line_out + body)
            if text.rstrip().endswith('::'):
                pending_literal = True
            prev_blank = False
            i += 1
            continue
        if x == 0 and ADORN.match(text.rstrip()) and out:
            prevtext = out[-1]
            # Underline: the headline is the line above.
            if prevtext.strip() and not ADORN.match(prevtext.strip()) and not prev_blank:
                out.append(text.strip()[0] * len(prevtext.rstrip()))
                prev_blank = False
                i += 1
                continue
            # Overline: the headline is the line below, then the underline.
            if i + 2 < n and lines[i + 1].strip() and ADORN.match(lines[i + 2].strip() or 'x') and lines[i + 2].strip()[0] == text.strip()[0]:
                out.append(text.strip()[0] * len(lines[i + 1].rstrip()))
                prev_blank = False
                i += 1
                continue
        out.append(' ' * X + text.rstrip())
        if text.rstrip().endswith('::'):
            pending_literal = True
        prev_blank = False
        i += 1
    return out


def fix_text(src):
    endnl = src.endswith('\n')
    lines = src.split('\n')
    if endnl:
        lines = lines[:-1]
    return '\n'.join(fix(lines)) + ('\n' if endnl else '')


def rst_files(paths):
    for p in paths:
        if os.path.isdir(p):
            for root, dirs, files in os.walk(p):
                dirs[:] = sorted(d for d in dirs if not d.startswith('.') and d != 'Documentation-GENERATED-temp')
                for f in sorted(files):
                    if f.endswith('.rst'):
                        yield os.path.join(root, f)
        else:
            yield p


def main():
    parser = argparse.ArgumentParser(description='Fix the indentation of reST files.')
    parser.add_argument('paths', nargs='+', metavar='PATH', help='.rst file or directory')
    parser.add_argument('--check', action='store_true', help='list the files that would change, write nothing')
    args = parser.parse_args()

    changed = []
    for path in rst_files(args.paths):
        with open(path, encoding='utf-8') as fh:
            src = fh.read()
        if CONFLICT.search(src):
            print(f'skipped, has conflict markers: {path}', file=sys.stderr)
            continue
        new = fix_text(src)
        if new == src:
            continue
        changed.append(path)
        if not args.check:
            with open(path, 'w', encoding='utf-8') as fh:
                fh.write(new)

    for path in changed:
        print(path)
    print(f'{len(changed)} file(s) {"would change" if args.check else "changed"}', file=sys.stderr)
    return 1 if args.check and changed else 0


if __name__ == '__main__':
    sys.exit(main())
