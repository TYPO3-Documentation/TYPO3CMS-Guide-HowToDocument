"""Tests of the scripts of the skill typo3-docs-changelog.

They run offline: the issues are saved copies in fixtures/, the manual is a
small git repository built for each test, and the Gerrit lookup is
replaced. Run them from the root of the repository:

    python3 -m unittest discover -s skills/typo3-docs-changelog/tests
"""

import contextlib
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), 'scripts'))
import changelog_issue as ci  # noqa: E402
import check_changelog_change as cc  # noqa: E402

GIT_ENV = dict(os.environ, GIT_AUTHOR_NAME='Test', GIT_AUTHOR_EMAIL='t@e.st',
               GIT_COMMITTER_NAME='Test', GIT_COMMITTER_EMAIL='t@e.st',
               GIT_CONFIG_GLOBAL=os.devnull, GIT_CONFIG_NOSYSTEM='1')

PAGE = """\
..  include:: /Includes.rst.txt

..  _ctrl:

====
ctrl
====

The ctrl section of a table holds the properties that apply to the whole
table, such as its title and the fields that the backend lists first.
"""

ISSUE_1903 = 'https://github.com/TYPO3-Documentation/Changelog-To-Doc/issues/1903'


def fixture(number):
    with open(os.path.join(HERE, 'fixtures', 'issue-%d.json' % number),
              encoding='utf-8') as fh:
        return json.load(fh)


class Manual:
    """A clone of a manual: main and 14.3 at a base commit, and a change."""

    def __init__(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.dir = self.tmp.name
        self.git('init', '-q', '-b', 'main')
        self.write('Documentation/Includes.rst.txt', '')
        self.write('Documentation/Ctrl.rst', PAGE)
        self.commit('Base')
        self.git('update-ref', 'refs/remotes/origin/14.3', 'HEAD')
        # A snippet that exists on main only, as in the review of
        # TYPO3CMS-Reference-CoreApi pull request 7230.
        self.write('Documentation/_Includes/Snippet.rst.txt', 'Snippet.\n')
        self.commit('Add snippet on main')
        self.git('update-ref', 'refs/remotes/origin/main', 'HEAD')

    def git(self, *args):
        return subprocess.run(['git', '-C', self.dir] + list(args),
                              check=True, capture_output=True, text=True,
                              env=GIT_ENV).stdout

    def write(self, path, text):
        full = os.path.join(self.dir, path)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, 'w', encoding='utf-8') as fh:
            fh.write(text)

    def commit(self, message):
        self.git('add', '-A')
        self.git('commit', '-q', '--no-gpg-sign', '-m', message)

    def change(self, added, message):
        self.write('Documentation/Ctrl.rst', PAGE + '\n' + added)
        self.commit(message)


def message(title, url=ISSUE_1903, releases='main, 14.3'):
    out = title + '\n\nBody.\n\nResolves: ' + url
    return out + ('\nReleases: ' + releases if releases else '')


DIRECTIVE_1903 = """\
..  versionchanged:: 14.3.8
    :changelog: important-106077-1789503919

    The option :php:`versioningWS_alwaysAllowLiveEdit` has no effect on
    tables with :php:`versioningWS`.
"""


class CheckChangeTest(unittest.TestCase):

    def setUp(self):
        self.manual = Manual()
        self.addCleanup(self.manual.tmp.cleanup)
        self._releases = ci.first_releases
        ci.first_releases = lambda body: {'14.3': 'v14.3.8', 'main': None}
        self.addCleanup(setattr, ci, 'first_releases', self._releases)
        self._next = ci.next_patch
        ci.next_patch = lambda branch: branch + '.10'
        self.addCleanup(setattr, ci, 'next_patch', self._next)

    def check(self, number=1903, added=DIRECTIVE_1903, msg=None,
              branches=None, versioned=True, issue=None):
        issue = issue or fixture(number)
        info = ci.parse_issue(issue)
        self.manual.change(added, msg or message(info['title'], info['url']))
        findings, _count, _files = cc.check(info, issue, self.manual.dir,
                                            'origin/main', branches,
                                            versioned)
        return findings

    def assertFinding(self, findings, start, text):
        hits = [f for f in findings if f.startswith(start) and text in f]
        self.assertTrue(hits, 'no %s line with "%s" in %s'
                        % (start, text, findings))

    def test_accepted_change_has_no_findings(self):
        self.assertEqual(self.check(branches=['main', '14.3']), [])

    def test_commit_summary_must_be_the_issue_title(self):
        findings = self.check(msg=message(
            '[TASK] Restrict live editing in workspaces'))
        self.assertFinding(findings, 'FIX', 'commit summary')

    def test_trailers_are_required(self):
        title = fixture(1903)['title']
        findings = self.check(msg=title + '\n\nBody.')
        self.assertFinding(findings, 'FIX', 'does not name the issue')
        self.assertFinding(findings, 'FIX', 'Releases:')

    def test_releases_trailer_only_for_versioned_manuals(self):
        title = fixture(1903)['title']
        msg = message(title, releases=None)
        self.assertEqual(self.check(msg=msg, versioned=False), [])

    def test_releases_trailer_unknown_branches(self):
        title = fixture(1903)['title']
        findings = self.check(msg=message(title, releases=None),
                              versioned=None)
        self.assertFinding(findings, 'CHECK', 'No "Releases:" trailer')

    def test_sentence_copied_from_the_page(self):
        findings = self.check(added=DIRECTIVE_1903 + (
            '\nThe ctrl section of a table holds the properties that apply '
            'to the whole\ntable, such as its title and the fields that the '
            'backend lists first.\n'))
        self.assertFinding(findings, 'CHECK', 'says the same thing twice')

    def test_directive_added_to_an_existing_confval(self):
        self.manual.write('Documentation/Ctrl.rst', PAGE + (
            '\n..  confval:: versioningWS_alwaysAllowLiveEdit\n'
            '    :name: ctrl-live-edit\n\n'
            '    If set, the table can be edited live.\n'))
        self.manual.commit('Confval on main')
        self.manual.git('update-ref', 'refs/remotes/origin/main', 'HEAD')
        self.manual.write('Documentation/Ctrl.rst', PAGE + (
            '\n..  confval:: versioningWS_alwaysAllowLiveEdit\n'
            '    :name: ctrl-live-edit\n\n'
            '    If set, the table can be edited live.\n\n'
            '    ' + DIRECTIVE_1903.replace('\n', '\n    ').rstrip() + '\n'))
        info = ci.parse_issue(fixture(1903))
        self.manual.commit(message(info['title']))
        findings, _c, _f = cc.check(info, fixture(1903), self.manual.dir,
                                    'origin/main', None, True)
        self.assertFinding(findings, 'CHECK', 'inside a confval')

    def test_release_lookup_failed(self):
        ci.first_releases = lambda body: None
        findings = self.check(added=DIRECTIVE_1903.replace('14.3.8', '14.3'))
        self.assertFinding(findings, 'CHECK', 'Gerrit gave no release')

    def test_gerrit_lists_no_change(self):
        ci.first_releases = lambda body: {}
        findings = self.check(added=DIRECTIVE_1903.replace('14.3.8', '14.3'))
        self.assertFinding(findings, 'CHECK', 'Gerrit gave no release')

    def test_include_of_an_untracked_file(self):
        info = ci.parse_issue(fixture(1903))
        self.manual.change(DIRECTIVE_1903 + (
            '\n..  include:: /_Includes/LiveEdit.rst.txt\n'),
            message(info['title']))
        self.manual.write('Documentation/_Includes/LiveEdit.rst.txt', 'x\n')
        findings, _c, _f = cc.check(info, fixture(1903), self.manual.dir,
                                    'origin/main', None, True)
        self.assertFinding(findings, 'FIX', 'not added to git')
        self.assertFalse([f for f in findings if f.endswith('on 14.3.')],
                         findings)

    def test_wrong_version_before_the_release(self):
        ci.first_releases = lambda body: {'14.3': None, 'main': None}
        findings = self.check(added=DIRECTIVE_1903.replace('14.3.8', '14.3.9'))
        self.assertFinding(findings, 'CHECK', 'the next release of branch '
                           '14.3, 14.3.10; no release contains it yet')

    def test_patch_version_for_a_minor_release_folder(self):
        findings = self.check(1634, added=(
            '..  versionadded:: 14.2.3\n'
            '    :changelog: feature-109167-1773174150\n'))
        self.assertFinding(findings, 'CHECK', 'the folder 14.2 names 14.2')
        self.assertEqual(self.check(1634, added=(
            '..  versionadded:: 14.2\n'
            '    :changelog: feature-109167-1773174150\n')), [])

    def test_backport_not_in_gerrit_yet(self):
        ci.first_releases = lambda body: {'main': None}
        findings = self.check(added=DIRECTIVE_1903.replace('14.3.8', '14.3'))
        self.assertFinding(findings, 'CHECK', 'no change on branch 14.3 yet')
        self.assertFinding(findings, 'CHECK', '14.3.10')

    def test_change_on_no_branch_of_the_folder(self):
        ci.first_releases = lambda body: {'main': None}
        issue = fixture(1903)
        issue['body'] = issue['body'].replace('Releases: main, 14.3',
                                              'Releases: main')
        findings = self.check(added=DIRECTIVE_1903.replace('14.3.8', '14.3'),
                              issue=issue)
        self.assertFinding(findings, 'CHECK', 'on no branch 14.3')

    def test_text_moved_out_of_a_deleted_page_is_not_new(self):
        moved = '\n\n'.join(' '.join('word%d_%d' % (p, i) for i in range(20))
                            for p in range(30))
        self.manual.write('Documentation/404.rst', 'Removed pages.\n')
        self.manual.write('Documentation/Old.rst', moved + '\n')
        self.manual.commit('Old page on main')
        self.manual.git('update-ref', 'refs/remotes/origin/main', 'HEAD')
        os.remove(os.path.join(self.manual.dir, 'Documentation/Old.rst'))
        self.manual.write('Documentation/404.rst', 'Removed pages.\n\n'
                          + moved + '\n')
        self.manual.git('config', 'diff.renames', 'false')
        findings = self.check(added=DIRECTIVE_1903)
        self.assertFalse([f for f in findings if 'lines of new text' in f],
                         findings)

    def test_text_moved_to_404_is_not_new(self):
        moved = ' '.join('word%d' % i for i in range(300))
        self.manual.write('Documentation/Ctrl.rst', PAGE + '\n' + moved + '\n')
        self.manual.commit('Long text on main')
        self.manual.git('update-ref', 'refs/remotes/origin/main', 'HEAD')
        self.manual.write('Documentation/404.rst', moved + '\n')
        findings = self.check(added=DIRECTIVE_1903)
        self.assertFalse([f for f in findings if 'lines of new text' in f],
                         findings)

    def test_git_config_without_diff_prefixes(self):
        self.manual.git('config', 'diff.noprefix', 'true')
        self.assertEqual(self.check(branches=['main', '14.3']), [])

    def test_wrong_patch_version(self):
        findings = self.check(added=DIRECTIVE_1903.replace('14.3.8', '14.3.1'))
        self.assertFinding(findings, 'CHECK', 'first release that contains '
                           'it, 14.3.8')

    def test_earlier_version_in_a_version_directive_body(self):
        findings = self.check(added=DIRECTIVE_1903 + (
            '\n    TYPO3 v14.3.7 and below allowed live editing here.\n'))
        self.assertEqual(findings, [])

    def test_version_in_a_list_item(self):
        findings = self.check(added=DIRECTIVE_1903 + (
            '\n*   Since Fluid 5.3.2, the exception names the template '
            'file.\n'))
        self.assertFinding(findings, 'CHECK', 'The version 5.3.2')

    def test_sentence_repeated_with_one_more_word(self):
        findings = self.check(added=DIRECTIVE_1903 + (
            '\nThe option :php:`versioningWS_alwaysAllowLiveEdit` has no '
            'effect on tables with :php:`versioningWS` anymore.\n'))
        self.assertFinding(findings, 'CHECK', 'says the same thing twice')

    def test_top_level_directive_like_one_in_a_confval(self):
        confval = ('\n..  confval:: other\n    :name: ctrl-other\n\n'
                   '    ..  versionchanged:: 14.3.8\n'
                   '        :changelog: important-106077-1789503919\n\n'
                   '        Other text about this option.\n')
        self.manual.write('Documentation/Ctrl.rst', PAGE + confval)
        self.manual.commit('Confval on main')
        self.manual.git('update-ref', 'refs/remotes/origin/main', 'HEAD')
        self.manual.write('Documentation/Ctrl.rst', PAGE + confval + '\n'
                          + DIRECTIVE_1903)
        info = ci.parse_issue(fixture(1903))
        self.manual.commit(message(info['title']))
        findings, _c, _f = cc.check(info, fixture(1903), self.manual.dir,
                                    'origin/main', None, True)
        self.assertFalse([f for f in findings if 'inside a confval' in f],
                         findings)

    def test_upstream_remote_of_a_fork(self):
        self.manual.git('remote', 'add', 'origin',
                        'https://github.com/someone/TYPO3CMS-Reference-TCA.git')
        self.manual.git('remote', 'add', 'upstream', 'git@github.com:'
                        'TYPO3-Documentation/TYPO3CMS-Reference-TCA.git')
        self.assertEqual(ci.upstream_remote(self.manual.dir),
                         ('upstream', 'TYPO3CMS-Reference-TCA'))

    def test_include_missing_on_backport_branch_of_upstream(self):
        # A clone of a fork: origin is the fork, which has no branch 14.3.
        head = self.manual.git('rev-parse', 'origin/main').strip()
        old = self.manual.git('rev-parse', 'origin/14.3').strip()
        self.manual.git('update-ref', 'refs/remotes/upstream/main', head)
        self.manual.git('update-ref', 'refs/remotes/upstream/14.3', old)
        self.manual.git('update-ref', '-d', 'refs/remotes/origin/14.3')
        info = ci.parse_issue(fixture(1903))
        self.manual.change(DIRECTIVE_1903 + (
            '\n..  include:: /_Includes/Snippet.rst.txt\n'),
            message(info['title']))
        findings, _c, _f = cc.check(info, fixture(1903), self.manual.dir,
                                    'upstream/main', None, True)
        self.assertFinding(findings, 'FIX', 'does not exist on 14.3')
        # An include that exists on upstream/14.3 is fine.
        self.manual.change(DIRECTIVE_1903 + (
            '\n..  include:: /Includes.rst.txt\n'), message(info['title']))
        findings, _c, _f = cc.check(info, fixture(1903), self.manual.dir,
                                    'upstream/main', None, True)
        self.assertEqual(findings, [])

    def test_backport_branch_not_fetched(self):
        self.manual.git('update-ref', '-d', 'refs/remotes/origin/14.3')
        findings = self.check()
        self.assertFinding(findings, 'CHECK', 'origin/14.3 not found')

    @unittest.skipUnless(shutil.which('ssh-keygen'), 'needs ssh-keygen')
    def test_git_config_that_shows_signatures(self):
        key = os.path.join(self.manual.dir, '.key')
        subprocess.run(['ssh-keygen', '-q', '-t', 'ed25519', '-N', '', '-f',
                        key], check=True)
        for name, value in (('gpg.format', 'ssh'), ('user.signingkey', key),
                            ('log.showSignature', 'true')):
            self.manual.git('config', name, value)
        info = ci.parse_issue(fixture(1903))
        self.manual.write('Documentation/Ctrl.rst', PAGE + '\n'
                          + DIRECTIVE_1903)
        self.manual.git('add', 'Documentation')
        self.manual.git('commit', '-q', '-S', '-m', message(info['title']))
        findings, _c, _f = cc.check(info, fixture(1903), self.manual.dir,
                                    'origin/main', None, True)
        self.assertEqual(findings, [])

    def test_sentence_added_to_an_existing_version_directive(self):
        self.manual.write('Documentation/Ctrl.rst', PAGE + '\n'
                          + DIRECTIVE_1903)
        self.manual.commit('Directive on main')
        self.manual.git('update-ref', 'refs/remotes/origin/main', 'HEAD')
        findings = self.check(added=DIRECTIVE_1903 + (
            '\n    TYPO3 v14.3.7 and below allowed live editing here.\n'))
        self.assertFalse([f for f in findings if '14.3.7' in f], findings)

    def test_references_trailer_is_accepted(self):
        info = ci.parse_issue(fixture(1903))
        msg = message(info['title']).replace('Resolves:', 'References:')
        self.assertEqual(self.check(msg=msg, branches=['main', '14.3']), [])

    def test_related_trailer_is_accepted(self):
        info = ci.parse_issue(fixture(1903))
        msg = message(info['title']).replace('Resolves:', 'Related:')
        self.assertEqual(self.check(msg=msg, branches=['main', '14.3']), [])

    def test_untracked_page_is_named(self):
        info = ci.parse_issue(fixture(1903))
        self.manual.change(DIRECTIVE_1903, message(info['title']))
        self.manual.write('Documentation/New.rst', 'A new page.\n')
        findings, _c, _f = cc.check(info, fixture(1903), self.manual.dir,
                                    'origin/main', None, True)
        self.assertFinding(findings, 'CHECK', 'Documentation/New.rst')

    def test_manual_search_reads_main_of_the_remote(self):
        root = tempfile.TemporaryDirectory()
        self.addCleanup(root.cleanup)
        bare = os.path.join(root.name, 'TYPO3-Documentation',
                            'TYPO3CMS-Reference-TCA.git')
        subprocess.run(['git', 'clone', '-q', '--bare', self.manual.dir,
                        bare], check=True, capture_output=True, env=GIT_ENV)
        self.manual.git('remote', 'add', 'origin', bare)
        self.manual.write('Documentation/Local.rst', 'OnlyOnLocalBranch\n')
        self.manual.commit('Local work')
        clones = os.path.join(root.name, 'clones')
        os.makedirs(clones)
        os.symlink(self.manual.dir, os.path.join(clones, 'tca'))
        found, _missing = ci.mentions(['OnlyOnLocalBranch', 'ctrl section'],
                                      clones)
        self.assertEqual(found['OnlyOnLocalBranch'], [])
        self.assertEqual(found['ctrl section'],
                         ['TYPO3CMS-Reference-TCA:Documentation/Ctrl.rst'])

    def single_branch_clone(self):
        """(clones dir, bare repository) with a clone of branch 14.3 only."""
        root = tempfile.TemporaryDirectory()
        self.addCleanup(root.cleanup)
        self.manual.git('branch', '14.3', 'refs/remotes/origin/14.3')
        bare = os.path.join(root.name, 'TYPO3-Documentation',
                            'TYPO3CMS-Reference-TCA.git')
        subprocess.run(['git', 'clone', '-q', '--bare', self.manual.dir,
                        bare], check=True, capture_output=True, env=GIT_ENV)
        clones = os.path.join(root.name, 'clones')
        subprocess.run(['git', 'clone', '-q', '--single-branch', '--branch',
                        '14.3', bare, os.path.join(clones, 'tca')],
                       check=True, capture_output=True, env=GIT_ENV)
        return clones, bare

    def test_manual_search_in_a_single_branch_clone(self):
        clones, _bare = self.single_branch_clone()
        found, missing = ci.mentions(['ctrl section'], clones)
        self.assertEqual(found['ctrl section'],
                         ['TYPO3CMS-Reference-TCA:Documentation/Ctrl.rst'])
        self.assertFalse([m for m in missing if 'failed' in m], missing)

    def test_manual_search_without_main_is_not_searched(self):
        clones, bare = self.single_branch_clone()
        shutil.rmtree(bare)
        found, missing = ci.mentions(['ctrl section'], clones)
        self.assertTrue([m for m in missing if 'git grep failed' in m],
                        missing)

    def test_no_mention_line_needs_a_full_search(self):
        info = ci.parse_issue(fixture(1903))
        info['mentions'] = {}
        info['not_searched'] = ['the names X (GitHub code search rate limit)']
        args = type('Args', (), {'no_search': False})()
        text = ci.report(info, args)
        self.assertIn('Search them before you decide', text)
        self.assertNotIn('No page mentions these names', text)

    def test_code_search_names_the_names_over_the_limit(self):
        self.addCleanup(setattr, ci, 'get', ci.get)
        self.addCleanup(setattr, ci, 'TOKEN', ci.TOKEN)
        ci.get = lambda path, params=None: {'items': []}
        ci.TOKEN = 'x'
        names = ['Name%d' % i for i in range(ci.CODE_SEARCH_LIMIT + 2)]
        found, missing = ci.mentions(names, None)
        self.assertEqual(len(found), ci.CODE_SEARCH_LIMIT)
        self.assertIn(names[-1], missing[0])

    def test_tsconfig_label_points_to_the_typoscript_reference(self):
        self.assertEqual(ci.LABEL_REPOS['TSconfig Reference'],
                         'TYPO3CMS-Reference-Typoscript')

    def test_code_search_rate_limit_keeps_the_results(self):
        calls = []

        def get(path, params=None):
            calls.append(path)
            if len(calls) > 1:
                raise SystemExit('rate limit')
            return {'items': [{'repository': {'name': 'R'}, 'path': 'P'}]}
        self.addCleanup(setattr, ci, 'get', ci.get)
        self.addCleanup(setattr, ci, 'TOKEN', ci.TOKEN)
        ci.get, ci.TOKEN = get, 'x'
        found, missing = ci.mentions(['FirstName', 'SecondName'], None)
        self.assertEqual(found, {'FirstName': ['R:P']})
        self.assertIn('SecondName', missing[0])

    def test_code_search_waits_for_the_next_minute(self):
        answers = []

        class Response(io.BytesIO):
            def __enter__(self):
                return self

            def __exit__(self, *_args):
                return False

        def urlopen(*_args, **_kwargs):
            if not answers:
                answers.append(1)
                raise ci.urllib.error.HTTPError(
                    'u', 403, 'rate limit', {'X-RateLimit-Remaining': '0',
                                             'X-RateLimit-Reset': str(
                                                 int(ci.time.time()) + 30)},
                    None)
            return Response(b'{"items": []}')
        slept = []
        self.addCleanup(setattr, ci.urllib.request, 'urlopen',
                        ci.urllib.request.urlopen)
        self.addCleanup(setattr, ci.time, 'sleep', ci.time.sleep)
        ci.urllib.request.urlopen = urlopen
        ci.time.sleep = slept.append
        self.assertEqual(ci.get('/search/code', {'q': 'x'}), {'items': []})
        self.assertTrue(0 < slept[0] <= 65, slept)

    def test_untracked_names_with_spaces(self):
        info = ci.parse_issue(fixture(1903))
        self.manual.change(DIRECTIVE_1903, message(info['title']))
        self.manual.write('Documentation/Images/Screen shot.png', 'x')
        findings, _c, _f = cc.check(info, fixture(1903), self.manual.dir,
                                    'origin/main', None, True)
        self.assertFinding(findings, 'CHECK',
                           'Documentation/Images/Screen shot.png')

    def test_file_left_out_of_the_commit(self):
        info = ci.parse_issue(fixture(1903))
        self.manual.change(DIRECTIVE_1903, message(info['title']))
        self.manual.write('Documentation/Later.rst', 'Written later.\n')
        self.manual.git('add', '-N', 'Documentation/Later.rst')
        findings, _c, _f = cc.check(info, fixture(1903), self.manual.dir,
                                    'origin/main', None, True)
        self.assertFinding(findings, 'CHECK', 'Not committed: '
                           'Documentation/Later.rst')

    def test_renamed_include_is_backported_with_the_change(self):
        snippet = ''.join('Line %d of the snippet.\n' % i for i in range(12))
        self.manual.write('Documentation/_Includes/Old.rst.txt', snippet)
        self.manual.commit('Snippet on both branches')
        self.manual.git('update-ref', 'refs/remotes/origin/main', 'HEAD')
        self.manual.git('update-ref', 'refs/remotes/origin/14.3', 'HEAD')
        self.manual.git('mv', 'Documentation/_Includes/Old.rst.txt',
                        'Documentation/_Includes/New.rst.txt')
        findings = self.check(added=DIRECTIVE_1903 + (
            '\n..  include:: /_Includes/New.rst.txt\n'))
        self.assertEqual(findings, [])

    def test_renamed_file_after_the_commit(self):
        info = ci.parse_issue(fixture(1903))
        self.manual.change(DIRECTIVE_1903, message(info['title']))
        os.rename(os.path.join(self.manual.dir, 'Documentation/Ctrl.rst'),
                  os.path.join(self.manual.dir, 'Documentation/Moved.rst'))
        self.manual.git('add', '-N', 'Documentation/Moved.rst')
        findings, _c, _f = cc.check(info, fixture(1903), self.manual.dir,
                                    'origin/main', None, True)
        line = [f for f in findings if f.startswith('CHECK Not committed')]
        self.assertTrue(line, findings)
        self.assertIn('Documentation/Moved.rst', line[0])
        self.assertNotIn('umentation', line[0].replace('Documentation', ''))

    def test_rejected_token(self):
        def unauthorized(*_args, **_kwargs):
            raise ci.urllib.error.HTTPError('u', 401, 'Unauthorized', {}, None)
        original = ci.urllib.request.urlopen
        ci.urllib.request.urlopen = unauthorized
        self.addCleanup(setattr, ci.urllib.request, 'urlopen', original)
        with self.assertRaises(SystemExit) as raised:
            ci.get('/repos/x/y/issues/1')
        self.assertIn('rejected the token', str(raised.exception))

    def test_resolves_trailer_names_this_issue(self):
        info = ci.parse_issue(fixture(1903))
        msg = message(info['title'], info['url'] + '0')
        findings = self.check(msg=msg)
        self.assertFinding(findings, 'FIX', 'does not name the issue')

    def test_changelog_identifier_is_required(self):
        findings = self.check(added=DIRECTIVE_1903.replace(
            '    :changelog: important-106077-1789503919\n', ''))
        self.assertFinding(findings, 'CHECK', 'No version directive or '
                           'confval option names the :changelog: identifier '
                           'of an entry: important-106077-1789503919')

    def test_patch_release_folder_needs_the_patch_version(self):
        findings = self.check(added=DIRECTIVE_1903.replace('14.3.8', '14.3'))
        self.assertFinding(findings, 'CHECK', '14.3.8')

    def test_unreleased_patch_names_the_next_release(self):
        ci.first_releases = lambda body: {'14.3': None, 'main': None}
        findings = self.check(added=DIRECTIVE_1903.replace('14.3.8', '14.3'))
        self.assertFinding(findings, 'CHECK', 'no release contains it yet')
        self.assertFinding(findings, 'CHECK', '14.3.10')

    def test_releases_trailer_names_every_branch(self):
        title = fixture(1903)['title']
        findings = self.check(msg=message(title, releases='main'),
                              branches=['main', '14.3'])
        self.assertFinding(findings, 'CHECK', 'does not name 14.3')

    def test_ip_address_is_no_version(self):
        findings = self.check(added=DIRECTIVE_1903 + (
            '\nRequests from 127.0.0.1 are trusted by default.\n'))
        self.assertEqual(findings, [])

    def test_version_in_a_literal_is_no_finding(self):
        findings = self.check(added=DIRECTIVE_1903 + (
            '\nRun ``composer require typo3/cms-core:14.3.8`` first.\n'))
        self.assertEqual(findings, [])

    def test_word_deprecated_is_no_directive(self):
        findings = self.check(1913, added=(
            '..  versionadded:: 15.0\n'
            '    :changelog: deprecation-110966-1791471928\n\n'
            '    The methods basename() and dirname() are deprecated now.\n'))
        self.assertFinding(findings, 'CHECK', 'deprecated or :deprecated:')

    def test_parallel_sentences_with_paths(self):
        findings = self.check(added=DIRECTIVE_1903 + (
            '\nTo add resource definitions to an extension, create the file '
            ':file:`Configuration/Resources.php`.\n\n'
            'To add resource definitions to the project, create the file '
            ':file:`config/system/resources.php`.\n'))
        self.assertEqual(findings, [])

    def test_malformed_version_is_a_fix(self):
        findings = self.check(added=DIRECTIVE_1903.replace('14.3.8', 'v14'))
        self.assertFinding(findings, 'FIX', '"v14" is no version')

    def test_patch_version_in_running_text(self):
        # The review of TYPO3CMS-Reference-CoreApi pull request 7227 asked
        # to remove "Fluid 5.3.2" from the text.
        findings = self.check(added=DIRECTIVE_1903 + (
            '\nSince Fluid 5.3.2, the exception names the template file.\n'))
        self.assertFinding(findings, 'CHECK', 'The version 5.3.2')

    def test_include_missing_on_backport_branch(self):
        # The review of TYPO3CMS-Reference-CoreApi pull request 7230 found
        # an include that exists on main only.
        findings = self.check(added=DIRECTIVE_1903 + (
            '\n..  include:: /_Includes/Snippet.rst.txt\n'))
        self.assertFinding(findings, 'FIX', 'does not exist on 14.3')

    def test_include_is_fine_without_backport(self):
        title = fixture(1903)['title']
        findings = self.check(added=DIRECTIVE_1903 + (
            '\n..  include:: /_Includes/Snippet.rst.txt\n'),
            msg=message(title, releases='main'))
        self.assertEqual(findings, [])

    def test_sentence_said_twice(self):
        findings = self.check(added=DIRECTIVE_1903 + (
            '\nThe ctrl section of a table holds the properties that apply '
            'to the whole table, such as its title.\n'))
        self.assertFinding(findings, 'CHECK', 'says the same thing twice')

    def test_parallel_list_items_are_no_repetition(self):
        findings = self.check(added=DIRECTIVE_1903 + (
            '\n*   The template path of the backend module points to the '
            'folder Templates.\n'
            '*   The layout path of the backend module points to the '
            'folder Layouts.\n'))
        self.assertEqual(findings, [])

    def test_parallel_sentences_are_no_repetition(self):
        findings = self.check(added=DIRECTIVE_1903 + (
            '\nThe template path of the backend module points to the folder '
            'Templates of the extension.\n\n'
            'The layout path of the backend module points to the folder '
            'Layouts of the extension.\n'))
        self.assertEqual(findings, [])

    def test_include_added_by_the_change_is_backported_with_it(self):
        self.manual.write('Documentation/_Includes/New.rst.txt', 'New.\n')
        findings = self.check(added=DIRECTIVE_1903 + (
            '\n..  include:: /_Includes/New.rst.txt\n'))
        self.assertEqual(findings, [])

    def test_long_change_for_an_important_entry(self):
        filler = ' '.join('word%d' % i for i in range(300))
        findings = self.check(added=DIRECTIVE_1903 + '\n' + filler + '\n')
        self.assertFinding(findings, 'CHECK', 'lines of new text')

    def test_issue_role_and_changelog_link(self):
        findings = self.check(added=DIRECTIVE_1903 + (
            '\nSee :issue:`106077` and https://docs.typo3.org/c/typo3/'
            'cms-core/main/en-us/Changelog/14.3.x/Important.html.\n'))
        self.assertFinding(findings, 'CHECK', ':issue:')
        self.assertFinding(findings, 'CHECK', 'link to the changelog')

    def test_version_directive_inside_confval(self):
        added = ('..  confval:: versioningWS_alwaysAllowLiveEdit\n'
                 '    :name: ctrl-live-edit\n\n'
                 '    ' + DIRECTIVE_1903.replace('\n', '\n    ').rstrip()
                 + '\n')
        findings = self.check(added=added)
        self.assertFinding(findings, 'CHECK', 'inside a confval')

    def test_affected_installations_text_is_left_out(self):
        issue = fixture(1913)
        rst = cc.changelog_text(issue)
        breaking = [r for _t, _f, r in rst.values() if 'Breaking' in r][0]
        section = cc.section_texts(breaking)['Affected installations']
        prose = '\n'.join(section.splitlines()[2:])
        findings = self.check(1913, added=(
            '..  versionchanged:: 15.0\n'
            '    :changelog: breaking-110966-1791465024\n\n' + prose))
        self.assertFinding(findings, 'CHECK', 'Affected installations')

    def test_one_of_two_entries_documented_is_no_fix(self):
        findings = self.check(1913, added=(
            '..  versionchanged:: 15.0\n'
            '    :changelog: breaking-110966-1791465024\n\n'
            '    The setting is removed.\n'))
        self.assertFinding(findings, 'CHECK', 'deprecation-110966-1791471928')
        self.assertFalse([f for f in findings if f.startswith('FIX')],
                         findings)


class ReadIssueTest(unittest.TestCase):

    def test_patch_release_folder(self):
        info = ci.parse_issue(fixture(1903))
        entry = info['files'][0]
        self.assertEqual(entry['folder'], '14.3.x')
        self.assertEqual(entry['type'], 'Important')
        self.assertEqual(entry['changelog_option'],
                         'important-106077-1789503919')
        self.assertTrue(any('14.3.x' in f for f in ci.flags(info)))

    def test_workspaces_tag_points_to_the_core(self):
        manuals, notes = ci.suggested_manuals(ci.parse_issue(fixture(1903)))
        self.assertIn('EXT:workspaces', manuals)
        self.assertTrue(any('Gerrit' in n for n in notes))

    def test_fluid_tag_points_to_typo3_explained(self):
        manuals, notes = ci.suggested_manuals(ci.parse_issue(fixture(1634)))
        self.assertEqual(manuals, ['TYPO3 Explained'])
        self.assertTrue(any('generated' in n for n in notes))

    def test_api_names(self):
        terms = ci.parse_issue(fixture(1634))['files'][0]['terms']
        self.assertIn('UndeclaredArgumentException', terms)
        self.assertIn('getPrevious', terms)

    def test_example_values_are_no_api_names(self):
        info = ci.parse_issue(fixture(1913))
        terms = [t for f in info['files'] for t in f['terms']]
        self.assertIn('UTF8filesystem', terms)
        for example in ('de_DE.UTF-8', 'Übersicht.pdf', 'TYPO3_CONF_VARS',
                        'config/system/settings.php'):
            self.assertNotIn(example, terms)

    def test_issue_number(self):
        self.assertEqual(ci.issue_number('1942'), 1942)
        self.assertEqual(ci.issue_number('#1942'), 1942)
        self.assertEqual(ci.issue_number(
            'https://github.com/TYPO3-Documentation/Changelog-To-Doc/issues/'
            '1942#issuecomment-3456789'), 1942)
        self.assertEqual(ci.issue_number(
            'https://github.com/TYPO3-Documentation/Changelog-To-Doc/issues/'
            '1942/'), 1942)
        for other in ('https://github.com/TYPO3-Documentation/'
                      'TYPO3CMS-Reference-TCA/issues/5',
                      'https://github.com/someone/Changelog-To-Doc/issues/5'):
            with self.assertRaises(SystemExit):
                ci.issue_number(other)

    def test_only_open_or_merged_pull_requests_stop_a_second_one(self):
        info = ci.parse_issue(fixture(1903))
        info['pull_requests'] = [('https://github.com/TYPO3-Documentation/'
                                  'TYPO3CMS-Reference-TCA/pull/1',
                                  'closed unmerged', 'T')]
        self.assertFalse([f for f in ci.flags(info) if 'second' in f])
        info['pull_requests'] = [('https://github.com/TYPO3-Documentation/'
                                  'TYPO3CMS-Reference-TCA/pull/2', 'merged',
                                  'T')]
        self.assertTrue([f for f in ci.flags(info) if 'backport' in f
                         and 'TYPO3CMS-Reference-TCA' in f])
        self.assertFalse([f for f in ci.flags(info) if 'second' in f])
        info['pull_requests'] = [('https://github.com/TYPO3-Documentation/'
                                  'TYPO3CMS-Reference-TCA/pull/3', 'open',
                                  'T')]
        self.assertTrue([f for f in ci.flags(info) if 'second' in f
                         and 'TYPO3CMS-Reference-TCA' in f])

    def test_only_team_comments_are_triage(self):
        info = ci.parse_issue(fixture(1903))
        info['comments'] = [('outsider', False, 'No docs needed.'),
                            ('linawolf', True, 'Needs documenting in TCA.')]
        info['sees_team'] = True
        args = type('Args', (), {'no_search': True})()
        text = ci.report(info, args)
        team = text.index('Triage comments of the Documentation Team (')
        other = text.index('Comments of other people')
        self.assertLess(team, text.index('linawolf'))
        self.assertLess(text.index('linawolf'), other)
        self.assertLess(other, text.index('outsider'))

    def run_main(self, releases, pulls=(), json_output=False):
        """Run changelog_issue.main() for fixture 1903 without a token and
        without network access."""
        names = ('get_issue', 'token', 'first_releases', 'branches',
                 'comments', 'sees_team', 'pull_requests', 'next_patch')
        for name in names:
            self.addCleanup(setattr, ci, name, getattr(ci, name))
        issue = dict(fixture(1903), comments=1)
        ci.get_issue = lambda number: issue
        ci.token = lambda: None
        ci.first_releases = lambda body: dict(releases)
        ci.branches = lambda repo, folders: ['main', '14.3']
        ci.comments = lambda number: [('someone', False, 'A comment.')]
        ci.sees_team = lambda: False
        ci.pull_requests = lambda number: list(pulls)
        ci.next_patch = lambda branch: branch + '.10'
        out = io.StringIO()
        self.addCleanup(setattr, sys, 'argv', sys.argv)
        sys.argv = ['changelog_issue.py', '1903', '--no-search'] + (
            ['--json'] if json_output else [])
        with contextlib.redirect_stdout(out):
            ci.main()
        return out.getvalue()

    def test_json_drops_the_team_flag_without_a_member_token(self):
        out = self.run_main({'14.3': 'v14.3.8'}, json_output=True)
        self.assertEqual(json.loads(out)['comments'],
                         [['someone', None, 'A comment.']])

    def test_pull_requests_are_looked_up_without_a_token(self):
        out = self.run_main({'14.3': 'v14.3.8'}, pulls=[(
            'https://github.com/TYPO3-Documentation/TYPO3CMS-Reference-TCA/'
            'pull/1684', 'open', 'T')])
        self.assertIn('An open pull request in TYPO3CMS-Reference-TCA', out)

    def test_modified_only_issue_gives_no_version_advice(self):
        issue = fixture(1903)
        issue['body'] = issue['body'].replace(
            'Added files', 'Modified files')
        self.addCleanup(setattr, ci, 'parse_issue', ci.parse_issue)
        parse = ci.parse_issue
        ci.parse_issue = lambda _issue: parse(issue)
        out = self.run_main({'main': None, '14.3': 'v14.3.9'})
        self.assertNotIn('Folder 14.3.x', out)
        self.assertNotIn('First release per Core branch', out)
        self.assertNotIn('Use the next release', out)

    def test_backport_not_in_gerrit_names_the_next_release(self):
        out = self.run_main({'main': None})
        self.assertIn('the backport is not in Gerrit yet. Use the next '
                      'release of branch 14.3, 14.3.10.', out)
        self.assertIn('14.3 not released yet, next release 14.3.10', out)

    def test_comments_without_token_are_not_classified(self):
        info = ci.parse_issue(fixture(1903))
        info['comments'] = [('linawolf', False, 'Needs documenting in TCA.')]
        info['sees_team'] = False
        args = type('Args', (), {'no_search': True})()
        text = ci.report(info, args)
        self.assertIn('membership is unknown', text)
        self.assertNotIn('Comments of other people', text)

    def test_token_of_a_non_member(self):
        def not_found(*_args, **_kwargs):
            raise ci.urllib.error.HTTPError('u', 404, 'Not Found', {}, None)
        original, token = ci.urllib.request.urlopen, ci.TOKEN
        ci.urllib.request.urlopen, ci.TOKEN = not_found, 'x'
        self.addCleanup(setattr, ci.urllib.request, 'urlopen', original)
        self.addCleanup(setattr, ci, 'TOKEN', token)
        self.assertFalse(ci.sees_team())

    def test_token_of_an_invited_member(self):
        original, token = ci.get, ci.TOKEN
        ci.TOKEN = 'x'
        self.addCleanup(setattr, ci, 'get', original)
        self.addCleanup(setattr, ci, 'TOKEN', token)
        ci.get = lambda path, params=None: {'state': 'pending'}
        self.assertFalse(ci.sees_team())
        ci.get = lambda path, params=None: {'state': 'active'}
        self.assertTrue(ci.sees_team())

    def test_docs_flag_needs_modified_files_only(self):
        issue = dict(fixture(1903), title='[DOCS] Add missing entries')
        self.assertFalse([f for f in ci.flags(ci.parse_issue(issue))
                          if f.startswith('[DOCS]')])

    def test_gerrit_timeout_is_no_release(self):
        def timeout(*_args, **_kwargs):
            raise TimeoutError('The read operation timed out')
        original = ci.urllib.request.urlopen
        ci.urllib.request.urlopen = timeout
        self.addCleanup(setattr, ci.urllib.request, 'urlopen', original)
        self.assertIsNone(ci.first_releases(fixture(1903)['body']))

    def test_open_backport_counts_as_not_released(self):
        queries = []

        def gerrit(path):
            queries.append(path)
            if path.startswith('/changes/?'):
                return [{'_number': 1, 'branch': 'main', 'status': 'MERGED'},
                        {'_number': 2, 'branch': '14.3', 'status': 'NEW'}]
            return {'tags': []}
        original = ci.gerrit
        ci.gerrit = gerrit
        self.addCleanup(setattr, ci, 'gerrit', original)
        self.assertEqual(ci.first_releases(fixture(1903)['body']),
                         {'main': None, '14.3': None})
        # Open changes count too; only abandoned ones are left out.
        self.assertNotIn('status:merged', queries[0])
        self.assertIn('-status:abandoned', queries[0])

    def test_tag_lookup_timeout_is_no_release(self):
        def hang(*_args, **_kwargs):
            raise ci.subprocess.TimeoutExpired('git', 60)
        original = ci.subprocess.run
        ci.subprocess.run = hang
        self.addCleanup(setattr, ci.subprocess, 'run', original)
        self.assertIsNone(ci.next_patch('14.3'))

    def test_no_merged_change_is_reported(self):
        info = ci.parse_issue(fixture(1903))
        info['first_releases'] = {}
        args = type('Args', (), {'no_search': True})()
        self.assertIn('lists no merged change', ci.report(info, args))

    def test_unknown_release_is_reported(self):
        info = ci.parse_issue(fixture(1903))
        info['first_releases'] = None
        args = type('Args', (), {'no_search': True})()
        self.assertIn('unknown, Gerrit gave no answer',
                      ci.report(info, args))

    def test_removed_and_added_files_are_a_rename(self):
        issue = fixture(1903)
        issue = dict(issue, body=issue['body']
                     + '\n## :heavy_minus_sign: Removed files\n')
        flags = ci.flags(ci.parse_issue(issue))
        self.assertTrue([f for f in flags if 'probably a rename' in f])
        self.assertFalse([f for f in flags if 'roll back' in f])

    def test_earlier_issue_search_names_the_skipped_names(self):
        info = ci.parse_issue(fixture(1913))
        info['earlier'] = {'UTF8filesystem': []}
        info['earlier_skipped'] = ['PathUtility']
        args = type('Args', (), {'no_search': True})()
        self.assertIn('Not searched: PathUtility', ci.report(info, args))

    def test_earlier_issue_search_takes_a_name_of_each_entry(self):
        out, seen = io.StringIO(), []
        names = ('get_issue', 'token', 'first_releases', 'branches',
                 'comments', 'sees_team', 'pull_requests', 'mentions',
                 'earlier_issues')
        for name in names:
            self.addCleanup(setattr, ci, name, getattr(ci, name))
        ci.get_issue = lambda number: fixture(1913)
        ci.token = lambda: None
        ci.first_releases = lambda body: {}
        ci.branches = lambda repo, folders: ['main']
        ci.comments = lambda number: []
        ci.sees_team = lambda: False
        ci.pull_requests = lambda number: []
        ci.mentions = lambda terms, manuals: ({}, [])
        ci.earlier_issues = lambda terms, number: seen.extend(terms) or {}
        self.addCleanup(setattr, sys, 'argv', sys.argv)
        sys.argv = ['changelog_issue.py', '1913']
        with contextlib.redirect_stdout(out):
            ci.main()
        self.assertEqual(len(seen), 4)
        self.assertIn('PathUtility', seen)

    def test_removed_files(self):
        issue = fixture(1903)
        head = issue['body'].index('## :heavy_plus_sign: Added files')
        issue = dict(issue, body=issue['body'][:head]
                     + '## :heavy_minus_sign: Removed files\n')
        flags = ci.flags(ci.parse_issue(issue))
        self.assertTrue([f for f in flags if 'removes changelog files' in f])
        self.assertFalse([f for f in flags if 'not changelog related' in f])

    def test_modified_older_entry_does_not_widen_the_folders(self):
        info = ci.parse_issue(fixture(1903))
        info['files'].append({'path': '12.0/Feature-1-Old.rst',
                              'kind': 'modified', 'folder': '12.0',
                              'type': 'Feature', 'forge': '1',
                              'changed_lines': 2, 'terms': []})
        self.assertEqual(ci.change_folders(info), ['14.3.x'])
        self.assertFalse([f for f in ci.flags(info) if '12.0' in f])
        info['files'] = info['files'][1:]
        self.assertEqual(ci.change_folders(info), ['12.0'])

    def test_name_parts(self):
        self.assertEqual(ci.name_parts('\\Exception'), [])
        self.assertEqual(ci.name_parts('$e->getPrevious()'), ['getPrevious'])
        self.assertEqual(ci.name_parts(
            '\\TYPO3\\CMS\\Core\\Utility\\PathUtility::basename()'),
            ['PathUtility', 'basename'])
        self.assertEqual(ci.name_parts(
            "$GLOBALS['TYPO3_CONF_VARS']['SYS']['UTF8filesystem']"),
            ['UTF8filesystem'])
        self.assertTrue(ci.specific('@typo3/backend/wizard.js'))
        self.assertFalse(ci.specific('Übersicht'))
        self.assertFalse(ci.specific('Configuration/TCA/Overrides'))


if __name__ == '__main__':
    unittest.main()
