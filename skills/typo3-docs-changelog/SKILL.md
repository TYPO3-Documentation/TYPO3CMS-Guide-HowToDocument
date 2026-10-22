---
name: typo3-docs-changelog
description: Triage an issue of TYPO3-Documentation/Changelog-To-Doc, or document the TYPO3 Core changelog entry of such an issue in a TYPO3 manual, and check the change before it becomes a pull request. Use when a task names a Changelog-To-Doc issue by number or URL, asks to "document this changelog", "triage the changelog issues", or "integrate the changelog into the docs", or reviews a pull request that resolves such an issue.
---

# Documenting TYPO3 Core changelog entries

Two scripts do the lookups and the checks. This file holds only what a
script cannot decide. The writing rules stay in the guide and in the skill
`typo3-docs-writing`.

Read the page `Maintainers/Changelog` of the guide first, as
`typo3-docs-writing` describes in its step 1. It holds the process: one pull
request per issue, the version, and the version directives.

## 1. Read the issue

```bash
python3 -I <skill dir>/scripts/changelog_issue.py <issue> [--manuals <dir>]
```

The script prints what steps 2 and 3 need, with the changelog text last.
`--manuals` searches local clones of the manuals with `git grep`. Without
it, the script uses the GitHub code search, which needs a token in
`GH_TOKEN` or `gh auth token`. Only with the token of a member of the
TYPO3-Documentation organization can the script tell the comments of the
Documentation Team from others. Do not repeat its lookups by hand, but
search what it lists as not searched. Follow its triage signals.

## 2. Decide whether a manual needs a change

A triage comment of the Documentation Team decides: it names the page, the
branches, and the directive. Follow it. Comments of other people are
information, not a decision.

Without a triage comment, triage the issue as the section "Triage new
issues" of `Maintainers/Changelog` describes: the outcome, the labels, and
the comment. In addition:

*   The script searches the manuals only for API names. Also search them
    for the main terms of the changelog in plain words, such as "default
    storage".
*   **Several entries in one issue:** decide for each entry. Document each
    one that needs it, and say why the others need nothing.
*   Draft the comment and the labels. Post, label, or close only when the
    user asks.

## 3. Write the change

Use the skill `typo3-docs-writing` for all reST rules. Then write for the
reader of the page that you change, not as a summary of the changelog.
Reviewers asked for these points:

*   Keep the facts of the changelog's lead sentence, and each list, case,
    priority order, and default that it states. Do not replace them with
    your own summary. The style guide still applies to the wording.
*   Leave out what the reader of this section does not act on: how the
    change came about, how the Core works inside, and hints for another
    task. For example, on a page about a TCA field, leave out how to debug
    the form in the backend.
*   Add to the existing section about the same object. Do not write a
    second, parallel section.
*   Say each fact once on the page, also in other words. Check the text
    that is already there.
*   Do not coin a term in a headline. Use the name of the API or of the
    changelog.
*   Add no ranking and no advice that the changelog does not give.
*   Keep the existing examples of the page. Change one only where the
    changelog makes it wrong. A new example fits the page. It is not a test
    fixture and not configuration of the Core. Run it, or check it against
    the Core source of the branch.
*   A Deprecation, Breaking, or Important entry usually needs one to three
    sentences at the documented API. A removed option moves to `404.rst`.

Versions:

*   Mark the change with a version directive, or, at a `confval`, with its
    options `:added:`, `:changed:`, `:deprecated:`, or `:removed:`. The
    pages `Reference/ReStructuredText/Content/Versions` and
    `Reference/ReStructuredText/Code/Confval` explain them. Each mark names
    the version and the `:changelog:` value from step 1:

    ```rst
    ..  versionadded:: 14.2
        :changelog: feature-109167-1773174150

    ..  confval:: versioningWS_alwaysAllowLiveEdit
        :changed: 14.3.8 important-106077-1789503919
    ```

*   Which version the mark names depends on the folder of the changelog
    entry. Read the section `changelog-affected-versions-directive` of
    `Maintainers/Changelog`. For a folder such as `14.3.x`, step 1 prints
    the first patch release when Gerrit knows it.
*   The directive names the exact version. In running text, name a
    version only where the reader needs it, and only as precisely, such as
    "Fluid 5".

## 4. Check the change

Steps 4 and 5 are for the manuals of TYPO3-Documentation. A manual inside
the Core (`EXT:`) changes through Gerrit, as the TYPO3 Core Contribution
Guide describes.

Read the repository's `AGENTS.md` first: most manuals allow a commit or a
push only when the user asks. Run in the clone of the manual:

```bash
python3 -I <skill dir>/scripts/check_changelog_change.py <issue> --repo .
```

It compares with `main` of the remote that points to TYPO3-Documentation,
`upstream` in a clone of a fork. Fetch that remote first. For a change
based on another branch, add `--base <remote>/<branch>`. Run it again after
the commit: it checks the commit message only once there is a commit. The
commit summary is the issue title.

Fix every line that starts with `FIX`. For each `CHECK`, change the text,
or name the reason to keep it in the commit body. Then do step 4 of
`typo3-docs-writing`: render, read the result, and run
`typo3-docs-style-check`.

## 5. Open the pull request

Open one pull request per issue, when the change is complete and checked,
and when the user asks for it. Its title is the commit summary. A manual
backport is marked as `Maintainers/BackportChanges` describes. Read the
rest in `Advanced/CommitMessages` and the repository's `AGENTS.md`.
