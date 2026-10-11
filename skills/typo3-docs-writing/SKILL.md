---
name: typo3-docs-writing
description: Write or edit TYPO3 documentation in reStructuredText so that it follows every rule of the TYPO3 "How to document" guide. Use before writing or changing .rst or .rst.txt files of a TYPO3 manual or of an extension's Documentation/ folder, and before writing the commit message for such a change. Also use when a task edits files under Documentation/ in a TYPO3 documentation repository without mentioning the rules, or asks to "write the docs", "document this", "add a section", "update the manual", or "fix this page".
---

# Writing TYPO3 documentation

The rules live in the "How to document" guide,
`TYPO3-Documentation/TYPO3CMS-Guide-HowToDocument`. This skill does not
copy them. It tells you which page to read for the text you are about to
write, in which order, and how to check the result. Read the pages
themselves. A rule from memory or from a summary is often out of date.

## 1. Find the guide and the repository rules

Read the rules from the guide's `main` branch:

*   **A local checkout exists.** In the TYPO3 documentation workspace it is
    `guide-h2d`, beside the other manuals. Confirm it with
    `git -C <dir> remote get-url origin`. Run `git -C <dir> fetch -q origin`
    and read with `git -C <dir> show origin/main:<path>`, so that a stale
    local branch does not hide a newer rule.
*   **No checkout.** Fetch the raw file from
    `https://raw.githubusercontent.com/TYPO3-Documentation/TYPO3CMS-Guide-HowToDocument/main/<path>`.

To find a rule by its anchor, search for the target line, for example
`git -C <dir> grep -n '_content-styleguide-serial-comma:' origin/main -- Documentation`.

If a page cannot be read, say so. Do not write from memory instead.

Then read the `AGENTS.md` or `CLAUDE.md` of the repository you are writing
in. It names the commands, the branches, and the commit trailers of that
repository. Where it differs from the guide, the repository file wins for
that repository.

## 2. Read the rules before you write

Always read these, every time:

*   `Documentation/Advanced/ContentStyleGuide.rst`, at least the sections
    with the anchors `content-styleguide-serial-comma`,
    `content-styleguide-sentences` with all its subsections,
    `content-styleguide-difficulty`, and `spelling-ref-title`.
*   `Documentation/Advanced/CodingGuidelines.rst`, the sections
    `cgl-indenting`, `format-rest-cgl-basic-formatting-rules-line-length`,
    and `rest-cgl-headline-underlines`.
*   `Documentation/Reference/ReStructuredText/Links/Anchors.rst`, the whole
    page.
*   `Documentation/Reference/ReStructuredText/Links/Documentation.rst`, the
    sections `permalinks`, `permalinks-rules`, and `link-text`.
*   `Documentation/Advanced/Glossary.rst`, the whole page. Its sections
    `preferred-terms-spelling` and `preferred-terms-terms` define how to
    spell names and terms. Use the spelling from there, also in headlines.

Then read the pages for what the text contains. The table in
[references/rule-map.md](references/rule-map.md) maps each kind of content
to its page and anchor. Read the whole section, including its examples.

## 3. Write

Follow the pages you read. Then look at how the manual already handles the
same kind of content, such as console commands, GUI paths, code examples,
or links, and do it the same way. For example, a manual that shows each
command in a tab for DDEV and a tab for the server needs both tabs for a
new command, too.

These points are where written text breaks the rules most often. Each one
names the anchor that holds the rule:

*   Every headline has its own anchor directly above it, and its underline
    is as long as the headline (`link-anchor`, `rest-cgl-headline-underlines`).
*   A new anchor starts with the anchor of the section it is in, such as
    `migration-with-make` below `migration` (`link-anchor-new`). To add the
    missing anchors of a manual, run
    `python3 <this skill>/scripts/generate_anchors.py Documentation`. Check
    the plan it prints, shorten each name it warns about, then run it again
    with `--apply`. It never changes an existing anchor.
*   Never delete an anchor. Move it to the heading that now covers the
    content, or to `404.rst` (`anchor-persistence`).
*   Two labels that differ only in case, or in `_` and `-`, are the same
    anchor, such as `Building` and `building`. When you respell one, do not
    keep the old spelling beside it (`anchor-persistence-spelling`).
    `scripts/find_missing_anchors.py` reports such pairs, headlines without
    an anchor, and lines that look like a broken anchor.
*   A renamed or deleted page needs a redirect (`redirects`).
*   Link TYPO3 documentation with a permalink and a link text of its own,
    also inside the same manual. Do not replace an existing permalink with
    `:ref:` (`permalinks`, `permalinks-rules`, `link-text`).
*   Lines stay below 80 characters. Only a link that cannot be broken may be
    longer (`format-rest-cgl-basic-formatting-rules-line-length`).
*   reST indents 4 spaces, with 2 spaces after `..`. Code examples indent
    2 spaces, whatever their language (`cgl-indenting`).
*   Use single backticks. A backslash in a plain literal must be doubled. In
    `:php:`, `:php-short:`, `:php-namespace:`, and `:file:`, write it once,
    and never end the text with a backslash (`text-roles`).
*   Choose between a code role and a plain literal with
    `inline-code-when-to-use-a-role`.
*   Name extensions with `:composer:` (`linking-extensions`).
*   Examples use `my_extension`, `my_sitepackage`, `\MyVendor`, the main set
    `Configuration/Sets/Main/`, and the domain `example.org`
    (`codeblocks-example-names`, `preventing-links`).
*   A version directive holds only the change it announces
    (`rest-versions-what-belongs-in-directive`).
*   Serial comma, short sentences in the active voice, instructions in the
    imperative, and no word that calls a task easy
    (`content-styleguide-serial-comma`, `content-styleguide-sentences`,
    `content-styleguide-difficulty`).
*   Headlines use sentence case (`spelling-ref-title`).
*   Names and terms are spelled as the glossary spells them, for example
    "backend", "site package", and "TypoScript", never "back-end",
    "sitepackage", or "Typoscript" (`preferred-terms`).

Verify every technical fact against the source before you write it: class
names, method signatures, option names, defaults, and the version that
added or removed something. Always check against the TYPO3 version of the
branch you are writing on. On `main`, that is the Core `main` branch, the
version in development, also when the task names a released version. On a
branch such as `14.3`, it is that version. Look at an older version only to
decide whether the text needs a version directive. Name the version you
checked.

## 4. Check the result

1.  Run the repository's render check, usually `make test-docs`. It fails on
    every warning, such as a missing anchor, a missing link text, or a broken
    permalink. Fix every warning. Do not switch a check off to get it green.
2.  Read the rendered output of what you changed. The render does not catch
    everything. Look at inline code with backslashes, at roles that run on
    into the following text, and at code blocks that render as plain text.
    A minimal-test render writes `Documentation-GENERATED-temp/singlehtml/`.
    Do not trust an HTML file left over from an earlier full render.
3.  Run the `typo3-docs-style-check` skill on the changed files, if it is
    installed. The pages you read in step 2 count as read for that check, so
    it reads only the pages still missing. If the skill is not installed,
    check the diff against the pages from step 2 yourself. The render does
    not check line length, sentence case, the serial comma, or the wording.

## 5. Write the commit message

Read `Documentation/Advanced/CommitMessages.rst` and the repository's own
`AGENTS.md`. The commit message, the pull request description, and any
issue comment follow the writing rules of step 2 as well.
