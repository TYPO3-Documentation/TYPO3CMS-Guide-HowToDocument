.. include:: ../Includes.txt
.. highlight:: rst

.. _rest-lists:

============
Bullet Lists
============

This section contains information on bullet lists and numbered lists. 

* Each item of a list should start with a `*` or `-` and a space after it
* Lists should have an empty line before and after
* Sublists should also precede with an extra newline
* Indent sublists with 3 spaces

bullet lists:

* Each item of a list should start with a `*` or `-` and a space after it

numbered lists:

* Start each item with a `#.` and a space after it for automatic numbering


**See also:** 

* `Docutils cheat-sheet for reStructuredText: Bullet list <http://docutils.sourceforge.net/docs/user/rst/quickref.html#bullet-lists>`__
* `Docutils cheat-sheet for reStructuredText: Enumerated lists <http://docutils.sourceforge.net/docs/user/rst/quickref.html#enumerated-lists>`__


Example 1: List with Sublist Items
==================================

.. code-block:: rest

   * item 1
   * item 2 is a longer text with line breaks. We can format and
     indent like this
   * item 3

      * subitem 3.1
      * subitem 3.1

   * item 4


**How it looks:**


* item 1
* item 2 is a longer text with line breaks. We must format and
  indent like this
* item 3

   * subitem 3.1
   * subitem 3.1

* item 4


Example 2: List with Sublist and Error
======================================

.. important::

   This example will not work as expected, because the extra lines
   for the sublist are missing (note *item 3* in bold).

.. code-block:: rest

   * item 1
   * item 2
   * item 3
      * subitem 3.1
      * subitem 3.1
   * item 4


**How it looks:**


* item 1
* item 2
* item 3
   * subitem 3.1
   * subitem 3.1
* item 4

For more information on common errors, see :ref:`rest-common-pitfalls`.

Example 3: Numbered List
========================

.. code-block:: rest

   #. item no 1
   #. item no 2
   
** How it looks:**

#. item no 1
#. item no 2

For more information on numbered lists, see :ref:`styled-numbered-lists`.
