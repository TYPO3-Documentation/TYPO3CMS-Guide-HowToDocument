.. include:: /Includes.rst.txt
.. highlight:: rst

.. _rest-lists:

============
Bullet Lists
============

This section contains information on bullet lists and numbered lists.
A text block which begins with a "\*", "+", "-", "•", "‣", or "⁃",
followed by whitespace, is a bullet list item.

*  Each item of a list should start with a `*` or `-` and 2 spaces after it
*  Lists should have an empty line before and after
*  Sublists should also have an empty line before and after
*  Indent sublists with 3 spaces

Bullet lists:

*  Each item of a list should start with a `*` or `-` and 2 spaces after it

Numbered lists:

*  Start each item with a `#.` and 1 space after it for automatic numbering


**See also:**

*  `Docutils cheat-sheet for reStructuredText: Bullet list
   <http://docutils.sourceforge.net/docs/user/rst/quickref.html#bullet-lists>`__

*  `Docutils cheat-sheet for reStructuredText: Enumerated lists
   <http://docutils.sourceforge.net/docs/user/rst/quickref.html#enumerated-lists>`__

*  `Docutils reference: bullet-lists
   <http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#bullet-lists>`__


Example 1: List with Sublist Items
==================================

.. code-block:: rest

   *  item 1
   *  item 2 is a longer text with line breaks. We can format and
      indent like this
   *  item 3

      *  subitem 3.1
      *  subitem 3.2

   *  item 4


**How it looks:**


*  item 1
*  item 2 is a longer text with line breaks. We can format and
   indent like this
*  item 3

   *  subitem 3.1
   *  subitem 3.2

*  item 4


Example 2: List with Sublist and Error
======================================

.. important::

   This example will not work as expected, because the extra lines
   for the sublist are missing.

.. code-block:: rest

   *  item 1
   *  item 2
   *  item 3
      *  subitem 3.1
      *  subitem 3.2
   *  item 4

**How it looks:**

*  item 1
*  item 2
*  item 3
   *  subitem 3.1
   *  subitem 3.2
*  item 4

For more information on common errors, see :ref:`rest-common-pitfalls`.
