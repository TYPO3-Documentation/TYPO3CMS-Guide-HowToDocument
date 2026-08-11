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

A recommended recipe could be:

#.  Duplicate the headline
#.  Transform to lowercase
#.  Replace all blanks by a hyphens `-`
#.  Remove all non-alphanumeric characters or replace them by a hyphen `-`
#.  Add `.. _` at the beginning.
#.  Add `:` at the end.

We are currently trying to let `Fractor support <https://github.com/andreaswolf/fractor/issues/206>`
this and other transformations.

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
    :ref:`redirects` for the full pattern, including a real example.

This applies everywhere, not just to official TYPO3 documentation
repositories — anyone linking to your docs, from a bookmark, a search
result, or another page, is relying on the anchor still being there.

Also watch for malformed anchor lines (the wrong number of leading dots, a
missing trailing colon) — they silently fail to work as a permalink, and
can render as broken, stray text on the page instead of an invisible link
target.
