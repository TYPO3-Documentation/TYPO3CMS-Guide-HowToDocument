..  include:: /Includes.rst.txt
..  highlight:: rst

..  index:: reST; Bullet lists
..  _rest-unordered-lists:

==============================
Bullet lists / unordered lists
==============================

This section contains information on bullet lists and numbered lists.
A text block which begins with a "\*", "+", "-", "•", "‣", or "⁃",
followed by whitespace, is a bullet list item.

*   Each item of a list should start with a `*` or `-` and 3 spaces after it
*   Lists should have an empty line before and after
*   Sublists should also have an empty line before and after
*   Indent sublists with 4 spaces

Bullet lists:

*   Each item of a list should start with a `*` or `-` and 3 spaces after it

Numbered lists:

*   Start each item with a `#.` and 1 space after it for automatic numbering


**See also:**

*   `Docutils cheat-sheet for reStructuredText: Bullet list
    <http://docutils.sourceforge.net/docs/user/rst/quickref.html#bullet-lists>`__

*   `Docutils cheat-sheet for reStructuredText: Enumerated lists
    <http://docutils.sourceforge.net/docs/user/rst/quickref.html#enumerated-lists>`__

*   `Docutils reference: bullet-lists
    <http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#bullet-lists>`__


.. index:: reST; Bullet list with sublist

Example 1: List with sublist items
==================================

.. code-block:: rst

    *   item 1
    *   item 2 is a longer text with line breaks. We can format and
        indent like this
    *   item 3

        *   subitem 3.1
        *   subitem 3.2

    *   item 4


**How it looks:**


*   item 1
*   item 2 is a longer text with line breaks. We can format and
    indent like this
*   item 3

    *   subitem 3.1
    *   subitem 3.2

*   item 4


Example 2: List with sublist and error
======================================

.. important::

    This example will not work as expected, because the extra lines
    for the sublist are missing.

.. code-block:: rst

    *   item 1
    *   item 2
    *   item 3
        *   subitem 3.1
        *   subitem 3.2
    *   item 4

**How it looks:**

*   item 1
*   item 2
*   item 3
    *   subitem 3.1
    *   subitem 3.2
*   item 4


Example 3: List with sublist and whitespace error
=================================================

.. important::

    Each asterix `*` has to be followed by three spaces.
    If you only use one the sublist is interpreted like
    a citation.

.. code-block:: rst

    * item 1
    * item 2
    * item 3

        * subitem 3.1
        * subitem 3.2

    * item 4

**How it looks:**

* item 1
* item 2
* item 3

    * subitem 3.1
    * subitem 3.2

* item 4


For more information on common errors, see :ref:`rest-common-pitfalls`.
