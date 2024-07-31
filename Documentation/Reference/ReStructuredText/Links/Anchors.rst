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

In the following example, the link target :rst:`columns-inline` is assigned
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
