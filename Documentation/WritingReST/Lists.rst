.. include:: ../Includes.txt
.. highlight:: rst

.. _rest-lists:

=====
Lists
=====

* Each item of a list should start with a `*` or `-` and a space after it
* Lists should have an empty line before and after
* Sublists should also precede with an extra newline
* Indent sublists with 3 spaces

Example 1: List with sublist items
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


Example 2: List with sublist and error
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
