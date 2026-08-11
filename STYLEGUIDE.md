# Documentation Style Guide

General conventions for writing and editing `.rst` files across TYPO3's
official documentation repositories, distilled from real corrections made
during review. These are not enforced by tooling (except where noted), so
please follow them by hand and point reviewers here when in doubt.

This file lives in the `TYPO3CMS-Guide-HowToDocument` repo (the "how to
document" guide) since it's the natural shared home for cross-repo writing
conventions. Other repos should reference it — via their own `CLAUDE.md` or
similar — rather than duplicating it, adding only what is genuinely specific
to that repo (its own tooling, its own known problem areas, etc.).

## Inline roles

### `:php:` and `:php-short:`

Only use `:php:` / `:php-short:` for **real PHP identifiers** where a tooltip
is actually useful — classes, methods, constants, functions. The role renders
a tooltip identifying the text as PHP, and if the tooling recognizes the
pattern (a class, constant, etc.) it shows extra info about it.

- **Never use it for key names**: TCA keys, CType/type identifiers, array
  keys, YAML/config keys are not PHP code. Use a plain literal instead:

  ```rst
  Bad:  The :php:`enablecolumns` key ...
  Good: The `enablecolumns` key ...
  ```

- **When referencing a class, always pass the FQCN** (fully-qualified,
  leading backslash, full namespace), and prefer `:php-short:` over bare
  `:php:` — it still resolves/tooltips off the FQCN but displays just the
  short class name, which reads better inline:

  ```rst
  Bad:  :php:`Scope::backend()`
  Good: :php-short:`\TYPO3\CMS\Core\Security\ContentSecurityPolicy\Scope::backend()`
  ```

  A short/bare class name with no FQCN breaks tooltip resolution.

- Don't use `:php:` for a term used generically/conceptually rather than as a
  real resolvable identifier (e.g. referring to "a PreviewRenderer" as a
  concept, not a specific class) — plain literal text again.

- **Never use `:php:`/`:php-short:` (or any role) in a headline** — plain
  backticks only there, even for something that would get a role in body
  text. See "Headlines" below.

### `:composer:` for extension names

Reference an extension (system or third-party) by its Composer package
name, wrapped in `:composer:`, not by its extension key, EXT: notation, or
plain text:

```rst
Bad:  the system extension "lowlevel" is installed
Bad:  the `lowlevel` extension is installed
Good: the :composer:`typo3/cms-lowlevel` extension is installed
```

This applies to both system extensions (`typo3/cms-*`) and third-party ones
(`vendor/package`, e.g. `georgringer/news`). `EXT:extkey` notation is
still correct for actual filesystem paths (e.g. in `:caption:` on a code
block or `:file:`), just not as the way to name the extension itself in
prose.

### `..  literalinclude::` and `:language:`

Don't add an explicit `:language:` option when the included file's extension
already indicates the language (`.php`, `.yaml`, `.js`, ...). Sphinx
auto-detects it. Only set `:language:` when the extension is ambiguous or
absent.

## Code blocks

Prefer a real `..  code-block:: <language>` directive over a bare `::`
literal-block trigger (a line ending in `::` followed by an indented block).
The `::` shorthand renders as plain, unstyled text — no syntax highlighting —
even when the content is clearly code:

```rst
Bad:
Example::

    defined('TYPO3') or die();

Good:
Example:

..  code-block:: php

    defined('TYPO3') or die();
```

Code shown in a `..  code-block::` or `..  literalinclude::` must be
syntactically correct for the language it's tagged as — a reader should be
able to copy it out and have it actually parse.

- The opening `<?php` tag can be omitted from a PHP snippet if the point
  being made doesn't need it — `:language: php` (or the file extension for
  `literalinclude`) already conveys the language.
- Surrounding boilerplate — the enclosing class, method signature,
  namespace — can be omitted too, to show just the fragment that matters.
  Omit it cleanly (a real fragment), don't leave dangling/mismatched braces.
- If the snippet uses a class (by short name, a static call, a type-hint,
  ...), include a `use` statement for it, even if the rest of the
  surrounding boilerplate is omitted — it's how a reader finds the actual
  class (its namespace, its source, IDE navigation) instead of having to
  guess or search for it.
- If a snippet genuinely needs something that isn't valid syntax for the
  language — a placeholder like `<your value here>`, a bare `...` standing
  in for real code, prose mixed into what would otherwise be a statement —
  mark the block `:language: plaintext` (or drop the language entirely)
  instead of tagging it as PHP/JS/whatever when it isn't actually valid
  code in that language.
- Keep lines to 80 characters or less wherever possible. The rendered code
  block area is narrow enough that longer lines force horizontal scrolling,
  which is a poor reading experience — wrap arguments/chained calls/long
  strings the way you would in real code review, rather than one long line.
- Add a `:caption:` with an example path for where the file should go, e.g.
  `:caption: EXT:my_extension/Classes/EventListener/MyListener.php` — it
  orients a new reader on where this snippet belongs in their own
  extension, not just what it contains.

## Admonitions (`..  note::`, `..  attention::`, ...)

Reserve admonitions for genuine call-outs a skimming reader must not miss (a
real gotcha, a security-relevant warning, a breaking caveat) — not routine
explanatory detail. Admonitions are visually prominent, and long ones are
worse: overusing them, or writing long ones, dilutes their value and makes
the page harder to scan. Routine detail belongs in the normal paragraph flow.
If a note is running long, that's usually a sign it should be prose instead.

## Security implications of code examples

Before publishing a code example, think about whether the pattern it shows
could be misused to cause an injection vulnerability if someone adapts it
with their own (possibly user-controlled) values — SQL injection from
building queries with unbound values, XSS/JavaScript injection from
inserting unescaped HTML, and so on.

- If the danger is real for the pattern shown, say so explicitly using
  `..  warning::` (not `..  note::` — security issues warrant the stronger
  admonition) — don't just leave it implicit.
- Always pair the warning with what to actually do about it: use parameter
  binding (`createNamedParameter()`) instead of concatenating values into a
  query, escape/sanitize output, avoid `unsafeHTML()`-style directives with
  untrusted data, etc. A warning without a fix is not very useful.
- If the example as written is already safe (e.g. a value is strictly typed
  in a way that rules out injection), it can still be worth a short comment
  saying why, so a reader adapting the example understands the constraint
  they need to preserve.

## Version directives (`..  versionadded::`, `..  versionchanged::`, `..  deprecated::`)

Across TYPO3 documentation repos, `main` typically targets the next TYPO3
major version; all currently *supported* TYPO3 versions are the latest LTS
and the one before that. Check your repo's own supported-version floor (it
may differ from other repos, and changes over time) before applying this.

Do not add a version directive for anything that happened **at or before**
the oldest supported version. Every reader is already on a supported
version, so "this changed in 13.2" is noise, not useful information — for
them, current behavior is simply how it's always been. Write it as a plain
statement of current fact instead.

Only use version directives for changes in a version **newer than** the
oldest supported one — those are the ones a reader on the oldest supported
version actually needs to know about when upgrading. Pick the right one:

- **`..  versionadded::`** — a concept came from a Core feature and isn't
  available in all currently-supported versions yet. State the version it
  was added in and link to the changelog entry.
- **`..  versionchanged::`** — a concept has changed (behavior, signature,
  configuration, ...) in a way worth mentioning, in a version newer than
  the supported floor.
- **`..  deprecated::`** — a concept still works but shouldn't be used
  anymore. Deprecated features can be removed in the very next version
  without further notice — don't assume or document a guaranteed grace
  period.

When backporting a docs change to older release branches (the `Releases:`
commit trailer), only include branches where the described feature actually
existed — see "Commit messages" below.

**If the concept itself was removed:** follow the anchor-preservation rule in
"Anchors (permalinks)" below (move the anchor to the covering parent
heading, or to `404.rst`) — don't just delete it. As an exception, for a few
particularly important removed concepts, keep the content in place with a
`..  versionchanged::` noting the removal (with a changelog link) instead of
relegating it to `404.rst` — use judgment for how central/frequently-
referenced the concept was, this is the exception, not the default.

## Avoid temporal language in prose

Don't write "currently", "now", "as of now", "the latest version", etc. in
prose (as opposed to a dated `versionchanged::` directive, which is fine
because it's pinned to a specific point). Documentation is read for years;
a relative time reference either becomes meaningless or actively misleading
once "now" has moved on. State facts plainly. If a claim genuinely needs a
time anchor, use a real dated/versioned reference instead of a relative word.

## Headlines

Prefer headlines that can be understood standing alone, without their
surrounding content. Headlines rank highly in our Elasticsearch-based site
search and are what gets displayed for a search result, so a generic
headline like bare "Example" or "API" is actively unhelpful there, on top of
being unhelpful for a reader skimming the page or a table of contents.

This is an ongoing cleanup effort across the docs — many repos still have
older pages using exactly "Example" or "API" as a headline. Matching a
generic sibling convention is not, by itself, a reason to keep a new
headline generic — default to descriptive over consistent-with-bad.

**Sentence case.** Capitalize only the first word (and proper nouns/product
names): "Rendering HTML content in a modal", not "Rendering HTML Content In
A Modal".

**Code keys/identifiers in a headline** keep whatever case they need in the
actual code, wrapped in plain backticks — don't force them to lowercase to
fit sentence case, and don't use a role (`:php:`, `:php-short:`, etc.) in a
headline even where you'd normally use one in body text:

```rst
Bad:  Using The Scope Class
Bad:  Using the :php-short:`\...\Scope` class
Good: Using the `Scope` class
```

**Shorter menu label:** if a headline needs to be long/descriptive for the
reasons above but that makes the sidebar/navigation entry too cluttered, add
`:navigation-title: <short label>` as the very first line of the file (before
the `..  include::`) — it only affects the menu, not the page's actual
headline or its search-indexed text.

## `:ref:` links used inline in a sentence

A bare `:ref:`some-anchor`` renders using the *current* text of the target
heading. That's fine for a standalone "see also"-style link, but if the
reference is grammatically part of a sentence, give it an explicit title
instead: `:ref:`explicit title <some-anchor>``. Otherwise, renaming the
target heading later (which is expected and encouraged, see "Headlines"
above) can silently turn a grammatically correct sentence into a broken one
at the point of use — the two are unrelated to each other and nobody editing
the heading is likely to check every sentence that links to it.

```rst
Bad:  as described in :ref:`some-anchor`
Good: as described in the :ref:`extension-specific configuration
      <some-anchor>`
```

## Table of contents

A page with several headlines should have a `..  contents::` directive (near
the top, right after the intro text) so a reader can see and jump to it
without scrolling. Use `:local:` so it doesn't also list the page
title itself; add `:depth:` if the default nesting is too deep for the page.
A short custom title (e.g. `..  contents:: Table of contents`) is fine but
not required — a bare `..  contents::` is common too.

## Anchors (permalinks)

Every headline should have a `..  _some-anchor:` target directly above it.
Style:

- kebab-case, lowercase, hyphen-separated
- hierarchical: nest a heading's anchor under its nearest ancestor heading's
  anchor (e.g. `caching-clearing-flushing-warming-cache-warmup` under
  `caching-clearing-flushing-warming` under `caching`)
- short and "speaking" rather than a literal slug of the full heading text —
  pick the word(s) that actually distinguish this heading, not a mechanical
  transcription

Watch for malformed anchor lines too (wrong number of leading dots, missing
trailing colon) — they silently fail to work as a permalink and can render
as broken/stray text on the page instead.

### Never remove an anchor that has reached `main`

An anchor is a promise: once it has been on `main`, its permalink must keep
working forever, even after the heading it was on is gone. Never just delete
an anchor. Depending on why the content went away:

- **Restructuring, but the concept still exists somewhere** (a subchapter or
  example merged into — or moved under — a different heading): move the
  anchor to the heading that now covers that content, even if it's now less
  specific (e.g. the parent chapter).

- **The whole concept was removed** (a breaking change, or it's no longer
  the recommended approach): move the anchor into `Documentation/404.rst`
  instead, under the `TYPO3 v<version>` section for the version it was
  removed in (create that section if it doesn't exist yet), and add a short
  entry explaining what happened. Include a `..  deprecated::` or
  `..  versionchanged::` directive linking to the changelog entry that
  removed it, if one applies. Follow the existing entries in that file for
  the exact shape — anchor(s) directly above a heading, a short descriptive
  title, the version directive with a changelog permalink, then one or two
  sentences on what to do instead (if there is a replacement). Also add a
  `:ref:` link to the new `404.rst` entry from wherever a reader would
  naturally land looking for this concept today — the covering parent
  chapter, or a replacement feature's docs — so it's discoverable by
  browsing, not just by following an old permalink.

### Renaming or deleting a `.rst` file

Each `.rst` file is a page with its own URL. Unlike an anchor, there's no
in-repo mechanism to keep an old file's URL working — that has to be a
server-side redirect, added in a **separate PR** in a different repository:
[TYPO3GmbH/site-intercept](https://github.com/TYPO3GmbH/site-intercept),
editing `config/nginx/redirects.conf`. Whenever a page in a repo is renamed
or deleted (not just moved to a new anchor within another page — an actual
change to the file's path or removal of the file), open a PR there adding
an nginx `location` rule for it, using your repo's own package path in
place of `<repo-package>` below.

- **Renamed/moved to a different existing page** — redirect straight to the
  new path:

  ```nginx
  location ~ ^/m/typo3/<repo-package>/(main|14.3)/en-us/Old/Path/Index.html$ {
      return 303 /m/typo3/<repo-package>/$1/en-us/New/Path/Index.html;
  }
  ```

- **Deleted / the concept no longer exists** — redirect to that repo's own
  `404.rst` page (per "Never remove an anchor" above, that's where the
  explanation for the removal now lives), not to an unrelated page:

  ```nginx
  location ~ ^/m/typo3/<repo-package>/(main|14.3)/en-us/Old/Path/Index.html$ {
      return 303 /m/typo3/<repo-package>/$1/en-us/404.html#old-concept-anchor;
  }
  ```

Scope the version group (`(main|14.3)`, `(main|14.3|13.4)`, ...) to the
versions where the old path actually existed, same idea as the `Releases:`
commit trailer. Use `303` for a redirect to different content, `301` if it's
genuinely permanent/the same content moved. This file is a **shared,
directly-deployed production file** for all TYPO3 docs projects, not just
this repo — the file's own header warns that a syntax error there takes
down docs.typo3.org entirely, so this PR needs real care and review, not a
quick edit.

## Commit messages

If your repo tracks LTS release branches and backports docs changes to them
(not all do — check whether the repo has branches like `13.4`, `12.4`, ...
alongside `main`), include a `Releases:` trailer identifying which branches
the change applies to (usually `main` plus the supported LTS branches, e.g.
`Releases: main, 14.3, 13.4`) — but check whether the change actually applies
to older branches first. If it documents behavior that didn't exist yet on
an older supported branch, narrow the trailer accordingly (e.g.
`Releases: main, 14.3` if the described API only exists from 14.0 on).
