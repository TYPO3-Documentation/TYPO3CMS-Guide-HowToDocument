:navigation-title: ReST Cheat Sheet
..  include:: /Includes.rst.txt
..  _writing-rest-introduction:
..  _Formatting-with-reST:
..  _rest-quick-start:
..  _rest-cheat-sheet:

===============================================================
ReST Cheat sheet: Using reStructuredText in TYPO3 Documentation
===============================================================

..  contents:: Cheat Sheet

..  _rest-cheat-sheet-headlines-anchors:

Headlines and Anchors
=====================

Each reST document must have a title. It is overlined and underlined like this:

..  code-block:: rst

    ..  _rest-cheat-sheet:

    =============================
    Cheat sheet: reStructuredText
    =============================

    Some text.

    ..  _h2-headline:

    H2 Headline
    ===========

    Lorem Ipsum

    ..  _h3-headline:

    H3 Headline
    -----------

There are more :ref:`levels of headlines <headlines-and-sections>`

..  _rest-cheat-sheet-contents:

Contents menu
=============

If you use more then one headlines consider to provide a contents menu. It
also allows your users to collapse all sections and only open the one they are
reading:

..  code-block:: rst

    ..  contents::

Additional options are possible: :ref:`contents menu options <content-menu>`.

..  _rest-cheat-sheet-links:

References and linking
======================

References to documentation from the TYPO3 world should be copied from the wizard:

..  figure:: /_Images/link-headlines.png

    Hover over a headline to see if it is linkable, then click the link icon

They then look like this:

..  code-block:: rst

    :ref:`Cheat sheet: reStructuredText <h2document:rest-cheat-sheet>`

External links can be copied into the document they will be auto detected. Or
the standard reST Syntax can be used:

..  code-block:: rst

    See also https://www.typo3.org or `the TER <https://extensions.typo3.org>`.

There are special links for composer packages and PHP classes (linking to the API):

..  code-block:: rst

    Install :composer:`typo3/cms-seo` to listen to event
    :php:`\TYPO3\CMS\Seo\Event\ModifyUrlForCanonicalTagEvent`.

There is a dedicated chapter on links and references in reST: :ref:`links`.

..  _rest-cheat-sheet-code-blocks:

Code blocks
===========

Short code blocks can be inserted directly into a reST file:

..  code-block:: rst

    ..  code-block:: php
        :caption: EXT:my_extension/ext_localconf.php

        defined('TYPO3') or die();

Longer code blocks should be put into a file starting with an underscore and
included:

..  code-block:: rst

    ..  literalinclude:: /snippets/_HelloWorld.php
        :caption: EXT:my_extension/Classes/WorldDominance/HelloWorld.php

All :ref:`options of code blocks <codeblock-quick-reference>` can also be
applied to literal includes.

..  _rest-cheat-sheet-confvals:

Configuration values (confvals)
===============================

Configuration values can be defined like this:

..  code-block:: rst

    ..  confval:: label
        :name: some-unique-label
        :required: true
        :type: string or LLL reference
        :default: "abc"

        The name of the field as shown in the form.

Configuration values can have custom properties and displayed in special
confval menues: :ref:`rest-confval`.

..  _rest-cheat-sheet-images:

Figures and Images
==================

..  code-block:: rst

    ..  figure:: /_Images/a4.jpg
        :alt: some image

    The caption of the image

*   :ref:`Images in reST <h2document:images>`
*   :ref:`Guidelines for creating images <h2document:guidelines-for-images>`


..  _rest-cheat-sheet-lists:

Lists, ordered and unordered
============================

..  code-block:: rst

    *   unordered
    *   Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam
        nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat,
        sed diam voluptua.
    *   list

    #.  ordered
    #.  Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam
        nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat,
        sed diam voluptua.
    #.  list

More about :ref:`Lists <h2document:rest-lists>`.

..  _rest-cheat-sheet-inline:

Inline text roles
=================

..  code-block:: rst

    *italic text*, **bold text**, `general code` :typoscript:`page = PAGE`
    :php:`\TYPO3\CMS\Seo\Event\ModifyUrlForCanonicalTagEvent` :guilabel:`Web > Page`
    :composer:`typo3/cms-typo3`

Looks like this:

*italic text*, **bold text**, `general code` :typoscript:`page = PAGE`
:php:`\TYPO3\CMS\Seo\Event\ModifyUrlForCanonicalTagEvent` :guilabel:`Web > Page`
:composer:`typo3/cms-typo3`

More: :ref:`rest-bold-italic`.

..  _rest-cheat-sheet-comments:

Comments
========

Comments can be written like this:

..  code-block:: rst

    ..  this is a comment
    ..  with another line

Or like this:

..  code-block:: rst

    ..  this is a comment
        with another line

..  _rest-cheat-sheet-escape:

Escape characters
=================

If you want to use a character, which would create some special reST markup,
with its normal meaning, you must escape it with a prepended "\".

For example surrounding text with "*" signs normally makes it show up in italics. By
escaping the special characters "*" you make the stars normal text characters:

..  code-block:: rst

    \*non-italic\*
