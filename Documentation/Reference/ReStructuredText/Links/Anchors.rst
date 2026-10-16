:navigation-title: Anchors
..  include:: /Includes.rst.txt

..  index:: reST; Link targets
..  _link-anchor:
..  _link-targets-explanation:
..  _explicit-link-targets:

============
Link anchors
============

Link anchors assign a unique name to a headline and its section. These anchors
can be used in internal references and references between TYPO3 manuals.

As long as the anchor of a section stays the same the section can be moved to
another page or the headline can be renamed and references will still go to the
correct target.

You can define a link anchor with a label for a section.

In the following example, the link target :rst:`inline-columns` is assigned
to the section with the title "Inline columns".

Place the link anchor definition directly before the section header:

..  code-block:: rst

    ..  _inline-columns:

    Inline columns
    ==============

Link anchors should contain alphanumeric signs plus hyphen: (`[a-z][0-9][-]`).
All other signs are automatically transformed by the symfony
:php:`Symfony\Component\String\Slugger\AsciiSlugger`.

..  _link-anchor-new:

Naming a new anchor
-------------------

An anchor must be unique in the whole manual. Short anchors such as
`with-make` or `why-it-exists` belong to the first section that uses them,
and the next section with the same headline needs another name. Start a new
anchor with the anchor of the section that the headline is in. This makes the
anchor unique and shows where the section belongs.

#.  Take the anchor of the section that contains the headline, for example
    `migration`. The title of a page has no such section, so its anchor starts
    with the next step.
#.  Duplicate the headline.
#.  Transform it to lowercase.
#.  Replace all blanks with a hyphen `-`.
#.  Remove all non-alphanumeric characters or replace them by a hyphen `-`.
#.  Join both parts with a hyphen `-`.
#.  Add `..  _` at the beginning and `:` at the end.

..  code-block:: rst
    :caption: The anchor of a section starts with the anchor of its page

    ..  _migration:

    =========
    Migration
    =========

    ..  _migration-with-make:

    With make
    =========

A section further down takes the anchor of its direct parent section, so the
anchor grows with the nesting. If an anchor gets long, leave out words that
the prefix already says, or that add little to the name.

Existing anchors are not renamed to follow this rule, see
`Keeping anchors working <https://docs.typo3.org/permalink/h2document:anchor-persistence>`_.

..  _anchor-persistence:

Keeping anchors working
=======================

An anchor is a promise: once a page containing it has reached `main`, the
anchor **must** keep working, even after the heading it was on is gone.
Never just delete an anchor. What to do instead depends on why the content
went away:

*   **Restructured, but the concept still exists somewhere** — a subchapter
    or example merged into, or moved under, a different heading: move the
    anchor to the heading that now covers that content, even if it is now
    less specific (for example the parent chapter).

*   **The whole concept was removed** — a breaking change, or it is no
    longer the recommended approach: move the anchor into a
    :file:`Documentation/404.rst` page instead (create it if it does not
    exist yet), and add a short entry explaining what happened. See
    :ref:`redirecting renamed or deleted pages <redirects>` for the full pattern, including a real example.

This applies everywhere, not just to official TYPO3 documentation
repositories — anyone linking to your docs, from a bookmark, a search
result, or another page, is relying on the anchor still being there.

Also watch for malformed anchor lines (the wrong number of leading dots, a
missing trailing colon) — they silently fail to work as a permalink, and
can render as broken, stray text on the page instead of an invisible link
target.

..  _anchor-persistence-spelling:

Changing only the spelling of an anchor
---------------------------------------

The rendering normalizes every anchor: it changes all letters to lowercase,
and replaces every run of characters other than `a-z` and `0-9` with a
hyphen. Two spellings with the same normalized form are one anchor. For
example, `Setup_Docker` and `setup-docker` are the same anchor.

*   **The normalized form stays the same**, as in `Setup_Docker` changed to
    `setup-docker`: rewrite the anchor and do not keep the old spelling. Two
    labels that normalize to the same anchor are still one anchor. If a page
    declares both, the rendering warns about the second one.
*   **The normalized form changes**, as in `ClassIndexJson` changed to
    `class-index-json`: this is a new anchor. `ClassIndexJson` normalizes to
    `classindexjson`, without hyphens. Keep the old label above the heading,
    beside the new one.

To check, normalize both spellings. If the results are equal, it is one
anchor.
