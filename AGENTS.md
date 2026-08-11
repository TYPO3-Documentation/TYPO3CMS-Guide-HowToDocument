# Working in TYPO3 documentation repositories

This file collects conventions shared across TYPO3's official documentation
repositories (all repos under github.com/TYPO3-Documentation, rendered to
docs.typo3.org), for use by AI coding assistants of any kind. It lives in
`TYPO3CMS-Guide-HowToDocument` (the "how to document" guide) since that's
the natural shared home for cross-repo guidance. A repo-specific agent
instructions file should describe the repo's purpose and point back
here for the rest, adding only what is genuinely specific to it (its own
tooling, its own known problem areas, etc.) rather than duplicating this
file.

## Content style

See [STYLEGUIDE.md](STYLEGUIDE.md) for RST/writing conventions: `:php:` vs
`:php-short:` role usage, when to use admonitions, version directive scoping,
avoiding temporal language ("currently"/"now"), headline quality, and anchor
(permalink) conventions.

Before stating anything as a fact — a class name, a method signature, whether
something is deprecated, whether something has changed — verify it against the
current TYPO3 core source rather than relying on memory. Check whether your
repo has TYPO3 core sources available locally (e.g. composer-installed
packages under a vendor directory, often including their own
`Documentation/Changelog/`) — that's usually the fastest way to check. For
"when was X introduced/removed" questions, checking the real commit history
on `github.com/TYPO3/typo3` (via `gh` or the GitHub API) is better than guessing —
commit messages and changelog entries there are the actual source of truth.

## Git workflow — branch and push safety

First figure out which situation applies: run `git remote -v`. If `origin`
points at the repo itself, you (or whoever you're assisting) has direct push
access — most contributors don't, and instead have `origin` pointing at
their own fork, with `upstream` (or similar) pointing at the real repo.
Fork-based contributors should just follow GitHub's normal fork workflow:
branch, push to `origin` (your fork), open a PR from your fork branch
against `TYPO3-Documentation:main`.

The rest of this section is specifically for the case where `origin` **is**
the repo itself, i.e. you have write access to it directly — more than one
of these repos has had a real incident where a locally-tracked branch ended
up pushing straight to `main`. To make that impossible:

1. Always branch off a freshly-fetched `origin/main`, explicitly **without**
   setting upstream tracking:
   ```bash
   git fetch origin --quiet
   git checkout -b task/<description> origin/main --no-track
   ```
   Verify with `git branch -vv` — there must be no `[origin/...]` annotation
   next to the new branch. Without tracking, a bare `git push` is refused
   outright instead of silently going somewhere unintended.

2. When pushing, always use an explicit `<local>:<remote>` refspec that names
   the exact same branch on both sides — never a bare `git push`:
   ```bash
   git push -u origin task/<description>:task/<description>
   ```

3. If two changes touch overlapping lines but should be reviewable as
   separate PRs, build them as independent branches off `origin/main` rather
   than stacking one on the other. Expect a small rebase/conflict when one
   lands after the other — that's the normal cost of splitting for review,
   not a sign that something went wrong.

## Committing

Never commit or push without being asked, regardless of which workflow
above applies. Implement and verify a fix, then leave it uncommitted (or
commit only when explicitly told to) so it can be reviewed first.

Check whether your repo has pre-commit hooks configured (e.g. a
`.pre-commit-config.yaml`, commonly trailing-whitespace and
end-of-file-fixer). If so, run them on the changed files *before*
committing, rather than relying on the commit itself to trigger them:

```bash
pre-commit run --files <changed files>
```

If a hook modifies a file, `git add` it again before committing. Running
this upfront avoids the commit failing on the first attempt and needing a
second one after the hook's auto-fixes are staged.

If your repo has example PHP snippets and its own CGL/lint-fix tooling
(check its `Makefile`/`composer.json` scripts — a common pattern is
`Build/Scripts/runTests.sh -s cgl`), run it on any `.php` file you changed
or added and `git add` any files it touches before committing.

## Commit messages

```
[TASK|BUGFIX|FEATURE] Summary

Body explaining why, not just what.

Resolves: #<issue>
Assisted-by: <tool/model name> <contact, e.g. noreply@vendor.com>
Signed-off-by: <actual committer name>
Releases: main, 14.3
```

- If your repo tracks LTS release branches and backports docs changes to
  them (not all do — check whether the repo has branches like `13.4`,
  `12.4`, ... alongside `main`), include a `Releases:` trailer reflecting
  which branches the *described behavior* is actually true on — see
  STYLEGUIDE.md's version-directive section. Use `main` alone only when
  documenting a feature/behavior that's new to `main` and doesn't exist on
  the current stable branch yet — there is no branch for the *next* version
  to also list; a dedicated branch only gets cut once that version reaches
  its own LTS release, and until then all of its development lives on
  `main`. Only add an older branch when there's a specific reason to
  backport that far — e.g. a bugfix/security fix or correction that's
  broken there too; don't backport plain content/style improvements to
  old-stable by default.
- If your repo doesn't track release branches (nothing but `main`), omit
  `Releases:` and `Resolves:` entirely rather than including them as dead
  weight.
- Use the actual tool/model name you're running as (check your own
  identity, don't assume) in `Assisted-by:`.
