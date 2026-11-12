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

This page explains the warnings and errors that the rendering writes to its
output. It also lists a problem that the rendering does not report.

..  contents::

..  _rendering-troubleshooting-exit-code:

The exit code does not show warnings
====================================

By default, the rendering writes the HTML and exits with code `0`, also when
it logs warnings or errors. Thus an unresolved reference or a missing image
does not stop a local render. A CI job that checks only the exit code does not
fail either.

These options change the exit code:

*   :bash:`--fail-on-log` exits with a non-zero code when the rendering logs a
    warning or an error.
*   :bash:`--fail-on-error` exits with a non-zero code when the rendering logs
    an error. Warnings do not change the exit code.
*   :bash:`--minimal-test` exits with a non-zero code when the rendering logs a
    warning or an error. The workflows in
    `Automatic testing for extension documentation <https://docs.typo3.org/permalink/h2document:test-documentation>`_
    use this option. A pipeline that you build from these examples fails on
    the messages on this page.

When one of these options sets a non-zero exit code, the last line of the
output starts with `Rendering failed: warnings or errors were logged, see above.`

..  tip::

    Read the output of a local render also when its last line is
    `Successfully placed ... files`. This line only tells you that the
    rendering wrote the HTML.

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

The rendering writes the page, but no menu links to it. Add the page to the
:rst:`..  toctree::` of the page above it. Usually this is the
:file:`Index.rst` file in the same directory. If readers must find the page
only through links, put :rst:`:orphan:` in the first line of the page.

..  _rendering-troubleshooting-menu-entry:

`Menu entry "..." was not found in the document tree`
-----------------------------------------------------

..  code-block:: text

    Menu entry "Installation" was not found in the document tree. Ignoring it.

A :rst:`..  toctree::` lists a document that does not exist. An entry is the
path of the file without the :file:`.rst` extension, relative to the current
file. A renamed page, a moved page, and a typo all cause this message. The
rendering removes the entry from the menu.

..  _rendering-troubleshooting-reference:

`Reference ... could not be resolved`
-------------------------------------

..  code-block:: text

    Reference installation-steps could not be resolved in Index

A :rst:`:ref:` names an anchor that no document defines. Make sure that the
spelling is correct. Make sure that the target file has
:rst:`..  _installation-steps:` directly above a headline, as
`Link anchors <https://docs.typo3.org/permalink/h2document:link-anchor>`_
describes. The rendering still writes the page. In place of a link, the page
shows the anchor name, marked as an invalid link.

..  _rendering-troubleshooting-duplicate-anchor:

`Duplicate anchor "..."`
------------------------

..  code-block:: text

    Duplicate anchor "installation". There is already another anchor of that
    name in document "Index"

Two files define the same :rst:`..  _label:` target. The rendering reports
this message for the second file. The message names the document that defines
the anchor first. References go to the first definition, so readers cannot
use this name to get to the section in the second file.

The same anchor twice in one file causes a different message:

..  code-block:: text

    The anchor "installation" is declared twice on this page (as
    "installation" and "installation"). Only the first one can be linked.
    Give the second section an anchor of its own.

An anchor names one section, see
`Link anchors <https://docs.typo3.org/permalink/h2document:link-anchor>`_.
Give the second section a new anchor. Do not delete one of the two anchors,
because other pages can link to an anchor that is already published.

..  _rendering-troubleshooting-unknown-directive:

`No template found for rendering directive "..."`
-------------------------------------------------

..  code-block:: text

    No template found for rendering directive "waring". Expected template
    "body/directive/waring.html.twig"

The rendering does not know the name of the directive. Usually the name has a
typo. If the name is correct, the directive comes from Sphinx, and the
rendering has no equivalent.
`The reST reference <https://docs.typo3.org/permalink/h2document:rest-reference>`_
lists the directives that you can use.

..  _rendering-troubleshooting-image:

`Image reference not found "..."`
---------------------------------

..  code-block:: text

    Image reference not found "/_Images/screenshot.png"

This message is an error. The other messages on this page are warnings.

The rendering finds an image path relative to the file that uses it. A path
that starts with a slash is relative to the :path:`Documentation` folder. Both
forms are correct, so the cause is usually a typo, an incorrect file
extension, or a file that is not committed. The message shows the full path from the
:path:`Documentation` folder. Compare this path with the location of the file.

..  _rendering-troubleshooting-empty-code-block:

`The code-block has no content`
-------------------------------

..  code-block:: text

    The code-block has no content. Did you properly indent the code?

The lines below :rst:`..  code-block::` have no indent, so they are not part
of the directive. The rendering shows them as normal paragraphs and shows no
code block. The same problem occurs with :rst:`..  math::` and
:rst:`..  list-table::`. Each of them writes its own version of this message.

..  _rendering-troubleshooting-inventory:

`Inventory with key ... not found` and `Inventory link ... not found`
---------------------------------------------------------------------

..  code-block:: text

    Inventory with key t3coreap not found.

    Inventory link with key "t3coreapi:sitehandlng" (sitehandlng) not found.

The first message tells you that the rendering does not know the key before
the colon. The rendering knows the official TYPO3 manuals, for example
`t3coreapi`, by default. You must declare all other manuals as an
:rst:`<inventory>` in your :file:`guides.xml` file, see
`Configuration of the rendering <https://docs.typo3.org/permalink/h2document:guides-xml>`_.
Usually the key has a typo.

The second message tells you that the rendering knows the manual, but the
manual has no anchor with this name. The anchor has a new name in that
manual, or the anchor has a typo.

For both messages, the page shows the reference as an invalid link.

..  _rendering-troubleshooting-interlink-shortcode:

`The manual declares no interlink shortcode`
--------------------------------------------

..  code-block:: text

    The manual declares no interlink shortcode, so it has no permalinks and
    other manuals cannot link to it. Add interlink-shortcode="..." to the
    <extension> element of guides.xml; for an extension it is the Composer
    name. See https://docs.typo3.org/permalink/h2document:guides-extension-interlink-shortcode

The rendering logs this warning for each render of a manual that has no
`interlink-shortcode` attribute in its :file:`guides.xml` file. Thus, with
:bash:`--minimal-test` or :bash:`--fail-on-log`, each render of this manual
fails. Add the attribute as the message tells you.

..  _rendering-troubleshooting-silent:

Problems that produce no message
================================

A directive must have a blank line between it and the paragraph above it. If
the blank line is missing, the directive becomes part of the paragraph. The
page then shows the source of the directive as plain text:

..  code-block:: rst
    :caption: Wrong: the page shows the note as plain text

    The installation is finished.
    ..  note::
        Clear the cache afterwards.

..  code-block:: rst
    :caption: Right

    The installation is finished.

    ..  note::
        Clear the cache afterwards.

The rendering logs nothing for the first example and exits with code `0`. You
can only see the problem on the rendered page.
