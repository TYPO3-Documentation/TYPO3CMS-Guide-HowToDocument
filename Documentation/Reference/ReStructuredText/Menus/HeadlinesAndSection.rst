
..  include:: /Includes.rst.txt
..  index::
    pair: reST; Headlines
    pair: reST; Titles
    pair: reST; Sections
..  _Headlines-and-sections:

======================
Headlines and sections
======================

reStructuredText (reST) does not exactly have the notion of "headlines". Text
is split into "sections" instead. Those sections are identified by titles which
- in the end - appear as headlines as we know them.

**TYPO3** uses these conventions.

1. Use underlining plus overlining with `===` for the first section title of a
    file. The first section title is the "document title" (**doctitle**) of that
    file and will appear in the menu. Every .rst file should have a title, each
    title should have a link anchor. In :ref:`link-anchor` we describe 
    our recommended best way how to build a link anchor in the official 
    TYPO3 documentation. Here you see a title and a link anchor in
    action:

..  code-block:: rst

        ..  _doc-title:

        ==============
        Document Title
        ==============

2. Then use underlining only:

..  code-block:: rst

        1.  ==========  for the first  level
        2.  ----------  for the second level
        3.  ~~~~~~~~~~  for the third  level
        4.  """"""""""  for the fourth level

3. More levels will be rarely used. For sake of completeness here is the whole
    hierarchy the automatic conversion tools uses. Stick to this order if more
    levels are needed:

..  code-block:: rst

        5.  ''''''''''
        6.  ^^^^^^^^^^
        7.  ##########
        8.  **********
        9.  $$$$$$$$$$
        10. ``````````
        plus:  +;.,_/%&!  in that order

Example
=======

..  code-block:: rst


    ..  _document-title:

    ==============
    Document Title
    ==============

    About this document ...

    ..  _topic-1:

    Topic 1
    =======

    Here we go.

    ..  _subtopic-1-1:

    Subtopic 1.1
    ------------

    Here we dive deeper


    ..  _subsubtopic-1-1-1:

    Subsubtopic 1.1.1
    ~~~~~~~~~~~~~~~~~

    And this is even more specific.

    ..  _topic-2:

    Topic 2
    =======
    ...


Syntax
======

Length of Underlines
--------------------

The length of the underlines **should** at have the length of the text. It
**should not** be longer or shorter.

Example 1: This Works
~~~~~~~~~~~~~~~~~~~~~

..  code-block:: rst

    ..  _example-1:

    =========
    Example 1
    =========

Example 2: These headlines work but do not abide to the coding guidelines
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

..  code-block:: rst

    ..  _example-2:

    ==============
    Example 2
    ==============

    ..  _example-3:

    =======
    Example 3
    =======
