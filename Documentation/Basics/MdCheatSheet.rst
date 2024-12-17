:navigation-title: Markdown Cheat Sheet
..  include:: /Includes.rst.txt

..  _md-cheat-sheet:

====================
Markdown Cheat sheet
====================

See commonly used Commonmark Markdown Syntax in the
TYPO3 Documentation Theme:

..  contents:: Cheat Sheet

..  _md-cheat-sheet-headlines-anchors:

Headlines and Anchors
=====================

Each document must have a title of level 1. You can use headers of additional
levels, only use level 1 once per Markdown document

..  code-block:: md

    # Document header

    Some text.

    ## H2 Headline

    Lorem Ipsum

    ### H3 Headline

    Lorem Ipsum

..  _md-cheat-sheet-links:

References and linking
======================

References to documentation from the TYPO3 world should be copied from the wizard:

..  figure:: /_Images/link-headlines.png

    Hover over a headline to see if it is linkable, then click the link icon

They then look like this:

..  code-block:: md

    [Configuration of the rendering - guides.xml](https://docs.typo3.org/permalink/h2document:guides-xml)

External links can be copied into the document they will be auto detected. Or
the standard md Syntax can be used:

..  code-block:: md

    See also https://www.typo3.org or (the TER)[https://extensions.typo3.org].

..  _md-cheat-sheet-code-blocks:

Code blocks
===========

Use the standard Markdown syntax for code blocks:

..  code-block:: md

    ```php
    <?php
    defined('TYPO3') or die();
    ```

    Lorem Ipsum Dolor: `$dolor`...

    ``Use `code` in your Markdown file.``

..  _md-cheat-sheet-images:

Figures and Images
==================

..  code-block:: md

    ![Alternative Text](/_Images/a4.jpg "Some Caption")

*   :ref:`Guidelines for creating images <h2document:guidelines-for-images>`


..  _md-cheat-sheet-lists:

Lists, ordered and unordered
============================

..  code-block:: md

    - unordered
    - Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam
      nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat,
      sed diam voluptua.
    - list

    1.  ordered
    2.  Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam
        nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat,
        sed diam voluptua.
    10. list

..  _md-cheat-sheet-inline:

Inline text roles
=================

..  code-block:: md

    *italic text*, **bold text**, `$code = 'My Code'`

..  _md-cheat-sheet-comments:

Comments
========

Comments can be written like this:

..  code-block:: md

    <!-- this is a comment -->

..  _md-cheat-sheet-admonitions:

Admonitions
===========

We support the rendering of the following GitHub Markdown style admonitions
(Warning, Tip, etc):

..  code-block:: md

    > [!NOTE]
    > Useful information that users should know, even when skimming content.

    > [!TIP]
    > Helpful advice for doing things better or more easily.

    > [!IMPORTANT]
    > Key information users need to know to achieve their goal.

    > [!WARNING]
    > Urgent info that needs immediate user attention to avoid problems.

    > [!CAUTION]
    > Advises about risks or negative outcomes of certain actions.
