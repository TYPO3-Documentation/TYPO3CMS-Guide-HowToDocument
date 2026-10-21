---
name: typo3-docs-changelog-triage
description: Triage new issues in the TYPO3-Documentation/Changelog-To-Doc repository - decide for each Core change whether a manual needs documentation, which pages change, and draft the labels and the comment for the user to approve. Use when asked to triage, label, sort, or close Changelog-To-Doc issues, to check "which changelog issues need docs", or to go through new changelog issues one by one.
---

# Triaging Changelog-To-Doc issues

Every Core change with a changelog entry opens an issue in
`TYPO3-Documentation/Changelog-To-Doc`. Triage gives each new issue one of
three outcomes: no docs needed, needs documenting in a named manual, or
already documented. The rules for the outcomes, the labels, and the comment
are in the "How to document" guide, page `Maintainers/Changelog`, section
`changelog-triage`. Read them there, as described in section 1 of the
skill `typo3-docs-writing`: the published Markdown
`https://docs.typo3.org/m/typo3/docs-how-to-document/main/en-us/Maintainers/Changelog.md`
first, the reST source as fallback. This skill does not copy the rules. It
describes how to apply them.

Triage writes to a public repository. Every label, comment, and closure is
visible at once and sends notifications. **Never label, comment on, or
close an issue without the user's approval of that exact issue.** Show the
draft for one issue, wait, apply it, then go on to the next one. An
approval covers only the text that the user saw: if you change the draft,
even by one link, show it again. You can research several issues ahead,
but show only the draft of the current issue, with no overview or count
of the others.

## 1. Find the issues to triage

An issue that still needs triage has only version labels, such as `15.0`,
`14.3.x`, or `13.4.x`:

```bash
gh issue list -R TYPO3-Documentation/Changelog-To-Doc -s open -L 100 \
    --json number,title,labels \
    --jq '.[] | select(all(.labels[].name; test("^[0-9]+\\.[0-9]+(\\.x)?$")))
          | "\(.number) \(.title)"'
```

Get the list of labels once with
`gh label list -R TYPO3-Documentation/Changelog-To-Doc -L 200`. Use only
labels that exist. Do not create labels.

## 2. Read the change

`gh issue view <n> -R TYPO3-Documentation/Changelog-To-Doc` shows the
commit message, the link to the commit on GitHub, the Gerrit review, and
the changelog entry in a `<details>` block.

*   Read the diff, not only the message:
    `gh api repos/TYPO3/typo3/commits/<sha> -H 'Accept: application/vnd.github.diff'`.
*   Take every name from the code: class, method, option key, TSconfig
    path, default value. Commit messages and changelog entries sometimes
    name an option differently from the code. Search a Core checkout of
    each affected version, or the GitHub repository `TYPO3/typo3` on the
    version branch, before you write a name into the comment.
*   Check whether the diff touches `typo3/sysext/*/Documentation/`. If so,
    the Core commit documented the change itself.
*   Find the versions from the path of the changelog entry, see the section
    `changelog-affected-versions` of the same guide page.

## 3. Search the manuals

Search every manual, not only the one that seems to fit:

*   A local clone of the manuals, if the user has one: `git grep` each name
    in `Documentation/` on the branch `main`, after `git fetch`.
*   Otherwise GitHub code search:
    `gh search code --owner TYPO3-Documentation '<name>'`. Search
    again with `--repo TYPO3/typo3` for the manuals of the system
    extensions, under `typo3/sysext/*/Documentation/`.
*   Search for the label text of the user interface too, for changes in the
    backend, and for the exception code, for changes to an exception. The
    Exceptions Reference has a page per code.

Read the page that you find. A match alone does not tell you whether the
page is now wrong.

## 4. Check the permalinks

Every page that the comment names gets a permalink. Get the anchor from the
published inventory of the manual, for example
`https://docs.typo3.org/m/typo3/reference-coreapi/main/en-us/objects.inv.json`
under `std:label`, or from the source file with `_` replaced by `-`. Then
check that it resolves:

```bash
curl -sL -o /dev/null -w '%{http_code} %{url_effective}\n' \
    'https://docs.typo3.org/permalink/<interlink>:<anchor>'
```

`200` with the right page at the end is correct. `404` means a wrong
interlink or anchor. The manuals of the system extensions use the package
name with hyphens as interlink, such as `typo3-cms-scheduler`.

## 5. Show the draft

Show the user, for one issue at a time:

*   The issue number as a full URL and its title.
*   The outcome: no docs needed, needs documenting, or already documented.
*   The labels to add, and whether the issue is closed.
*   The exact text of the comment.
*   Anything that you are not sure of, as a question. The user decides
    borderline cases. A change that no manual mentions can still belong in
    one.

Write the comment as described in the section `changelog-triage-comment`
of the guide. It follows the writing rules of the guide like any other text.
Link other issues and pull requests with their full URL, never with a bare
number.

## 6. Apply the decision

After the user approves, and only then:

```bash
R=TYPO3-Documentation/Changelog-To-Doc
gh issue edit <n> -R $R --add-label '<label>' --add-label '<label>'
gh issue comment <n> -R $R --body-file <draft file>
gh issue close <n> -R $R            # only for "no docs needed" and "already documented"
```

Comment first and close afterwards, as separate commands. Check the state
of the issue before you act: someone else may have triaged it since you
read it, and `gh issue close --comment` posts nothing on an issue that is
already closed. Check the result with
`gh issue view <n> -R $R --json state,labels,comments`.

Then show the next issue.
