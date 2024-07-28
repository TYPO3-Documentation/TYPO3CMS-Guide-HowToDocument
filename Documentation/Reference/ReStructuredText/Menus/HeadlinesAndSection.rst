
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
    file and will appear in the menu. Every .rst file should have a doctitle:

..  code-block:: rst

        ========
        DocTitle
        ========

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

    ========
    DocTitle
    ========

    About this document ...

    Topic 1
    =======
    Here we go.

    Subtopic 1.1
    ------------
    Here we dive deeper

    Subsubtopic 1.1.1
    ~~~~~~~~~~~~~~~~~
    And this is even more specific.

    Topic 2
    =======
    ...


Syntax
======

Length of Underlines
--------------------

The length of the underlines must at least have the length of the text. It
may be longer, not shorter.

Example 1: This Works
~~~~~~~~~~~~~~~~~~~~~

..  code-block:: rst

    =========
    Example 1
    =========

Example 2: This Works Too
~~~~~~~~~~~~~~~~~~~~~~~~~

..  code-block:: rst

    ==============
    Example 1
    ==============

Example 3: This Does not Work
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

..  code-block:: rst

    =======
    Example 1
    =======



Additional Information
======================

*   **Docutils:** Read about `sections
    <http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#sections>`__
    in the Docutils documentation for the most fundamental description.

*   **Sphinx** is explaining `sections
    <http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#sections>`__
    as well.
