---
name: typo3-docs-style-check
description: Check TYPO3 documentation (.rst files) against the current rules of the TYPO3 "How to document" guide and report each violation with the rule and a fix. Use after writing or editing TYPO3 .rst files and before declaring a documentation task finished, or when asked to "check docs style", "review these docs", or "does this follow the style guide".
---

Check the target `.rst` files (the ones the user names, or the files changed
in the current git diff if none are named) against TYPO3-Documentation's
actual, current style rules.

**Do not rely on memory or any cached summary of these rules — they change,
and a stale rule is worse than no check at all.** Every time this skill
runs, read the current text of these pages from the `main` branch of
`TYPO3-Documentation/TYPO3CMS-Guide-HowToDocument`:

*   **A local checkout exists.** In the TYPO3 documentation workspace it is
    `guide-h2d`, beside the other manuals. Confirm it with
    `git -C <dir> remote get-url origin`. Run `git -C <dir> fetch -q origin`
    and read with `git -C <dir> show origin/main:<path>`. Do not download
    the pages as well.
*   **No checkout.** Fetch the raw file from
    `https://raw.githubusercontent.com/TYPO3-Documentation/TYPO3CMS-Guide-HowToDocument/main/<path>`.

A page that the `typo3-docs-writing` skill already read in this task, from
the same `origin/main` or the same download, does not need reading again.
Read only the pages below that are still missing:

*   `Documentation/Advanced/ContentStyleGuide.rst` — sentence case, spelling,
    capitalization, general prose rules. Always needed.
*   `Documentation/Advanced/CodingGuidelines.rst` — reST formatting:
    indentation, `..` marker spacing, line length. Always needed.
*   `Documentation/Reference/ReStructuredText/Code/InlineCode.rst` — single
    vs. double backticks, `:php:`/`:php-short:` usage. Read it when the
    target files contain any inline code or roles.
*   `Documentation/Reference/ReStructuredText/Links/Composer.rst` — prefer
    `:composer:` over extension key/`EXT:` notation. Read it when the target
    files name a TYPO3 extension.
*   `Documentation/Reference/ReStructuredText/Links/Anchors.rst` — anchor
    naming and the never-remove-an-anchor rule. Read it when the target files
    add, rename, or remove a headline.
*   `Documentation/Advanced/Redirects.rst` — required when a page is
    renamed or deleted. Read it when the diff includes a renamed/deleted
    `.rst` file.

If a page cannot be read, or the fetch fails, say so explicitly in the
report instead of silently skipping it — a rule you couldn't check is not
the same as a rule that passed.

Apply what you actually read to the target files. For each violation,
report the file, line, the rule it breaks (quote the relevant sentence
from the page you read), and the concrete fix. Group the report by file. If
nothing is wrong, say so plainly — don't invent findings to seem useful.

This skill only reports; it does not edit files unless the user asks it to
apply the fixes.
