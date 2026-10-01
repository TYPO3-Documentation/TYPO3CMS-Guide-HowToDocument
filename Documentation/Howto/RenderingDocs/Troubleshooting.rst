:navigation-title: Troubleshooting

..  include:: /Includes.rst.txt
..  index::
    pair: Documentation; Troubleshooting
    Rendering; Warnings
    Rendering; Errors
..  _rendering-troubleshooting:

=============================
Troubleshooting the rendering
=============================

This page explains the warnings and errors the rendering writes to its output,
and lists the problems it does not report at all.

..  contents::

..  _rendering-troubleshooting-exit-code:

A render that succeeds is not a render that is clean
====================================================

By default the rendering writes the HTML and exits with code `0` even when it
logged warnings and errors. An unresolved reference or a missing image
therefore does not stop a local render, and it does not fail a CI job that only
looks at the exit code.

Three options change that:

*   :bash:`--fail-on-log` exits with a non-zero code as soon as any warning or
    error was logged.
*   :bash:`--fail-on-error` exits with a non-zero code only for errors.
*   :bash:`--minimal-test` also exits with a non-zero code on a warning. The
    workflows shown in :ref:`test-documentation` use it, so a pipeline built
    from those examples already fails on the messages below.

..  tip::

    Read the output of a local render even when it ends with
    `Successfully placed ... files`. That line says the HTML was written, not
    that it is correct.

..  _rendering-troubleshooting-messages:

Messages and what to do about them
==================================

..  _rendering-troubleshooting-toctree-missing:

`Document "..." isn't included in any toctree`
----------------------------------------------

..  code-block:: text

    Document "Installation" isn't included in any toctree. Include it in a
    `.. toctree::` directive or add `:orphan:` in the first line of the rst
    document

The file is rendered, but no menu leads to it. Add it to the
:rst:`..  toctree::` of the page above it, usually the :file:`Index.rst` of the
same directory. If the page is meant to be reachable by link only, put
:rst:`:orphan:` in its first line.

..  _rendering-troubleshooting-menu-entry:

`Menu entry "..." was not found in the document tree`
-----------------------------------------------------

..  code-block:: text

    Menu entry "Installation" was not found in the document tree. Ignoring it.

A :rst:`..  toctree::` lists a document that does not exist. The entry is the
path of the file without the :file:`.rst` extension, relative to the current
file. A renamed or moved page and a typo both produce this message, and the
menu silently loses the entry.

..  _rendering-troubleshooting-reference:

`Reference ... could not be resolved`
-------------------------------------

..  code-block:: text

    Reference installation-steps could not be resolved in Index

A :rst:`:ref:` names an anchor that no document defines. Check the spelling and
make sure the target file contains :rst:`..  _installation-steps:` directly
above a headline, as described in :ref:`link-anchor`. The page is still
rendered: the reference becomes the bare anchor name, marked as an invalid
link, where the reader expected a link and its title.

..  _rendering-troubleshooting-duplicate-anchor:

`Duplicate anchor "..."`
------------------------

..  code-block:: text

    Duplicate anchor "installation". There is already another anchor of that
    name in document "Index"

Two files define the same :rst:`..  _label:` target. The message names the
document that already holds the anchor, and is reported for the file that
defines it a second time. References resolve to the first definition, so the
section in the second file can no longer be reached by that name.

The same anchor used twice within one file is not reported, and behaves the
same way. An anchor names one section, see :ref:`link-anchor`, so give the
second section an anchor of its own rather than deleting one — an anchor that
has already been published has to keep working.

..  _rendering-troubleshooting-unknown-directive:

`No template found for rendering directive "..."`
-------------------------------------------------

..  code-block:: text

    No template found for rendering directive "waring". Expected template
    "body/directive/waring.html.twig"

The directive name is not one the rendering knows. Most of the time it is a
typo. Otherwise the directive comes from Sphinx and has no equivalent here:
:ref:`the reST reference <rest-reference>` lists what is available.

..  _rendering-troubleshooting-image:

`Image reference not found "..."`
---------------------------------

..  code-block:: text

    Image reference not found "_Images/screenshot.png"

This one is logged as an error, not a warning. The path is resolved relative to
the file that uses it; a path starting with a slash is resolved relative to the
:path:`Documentation` folder. Both forms work, so the usual causes are a typo,
a wrong file extension or a file that was never committed.

..  _rendering-troubleshooting-empty-code-block:

`The code-block has no content`
-------------------------------

..  code-block:: text

    The code-block has no content. Did you properly indent the code?

The lines below :rst:`..  code-block::` are not indented, so they are not part
of the directive. They become ordinary paragraphs, and an empty code block is
rendered above them. The same applies to :rst:`..  math::` and
:rst:`..  list-table::`, which write their own version of this message.

..  _rendering-troubleshooting-inventory:

`Inventory with key ... not found` and `Inventory link ... not found`
---------------------------------------------------------------------

..  code-block:: text

    Inventory with key t3coreapi not found.

    Inventory link with key "t3coreapi:sitehandling" (sitehandling) not found.

The first message means the manual you link to is not declared as an
:rst:`<inventory>` in your :file:`guides.xml`, see :ref:`guides-xml`. The
second means the manual is declared but does not contain that anchor — it was
renamed upstream, or the identifier is misspelled. In both cases the reference
is rendered as an invalid link, as above.

..  _rendering-troubleshooting-silent:

Problems that produce no message
================================

A directive needs a blank line between it and the paragraph above it. Without
that blank line the rendering treats the directive as part of the paragraph and
prints its source as plain text:

..  code-block:: rst
    :caption: Wrong: the note is rendered as literal text

    The installation is finished.
    ..  note::
        Clear the cache afterwards.

..  code-block:: rst
    :caption: Right

    The installation is finished.

    ..  note::
        Clear the cache afterwards.

Nothing is logged in the first case, and the render exits successfully, so this
is only visible in the rendered page.
