.. include:: /Includes.rst.txt
.. highlight:: rst
.. index:: reST; Lists

===================
Problems with lists
===================

If you use lists, make sure there is an empty line before and after the
list. If you use lists with sublevels, make sure there is an empty line
between the levels and the sublevel items are left-aligned with the
parent item text.

The same applies for bullet lists and enumerated lists.


Correct syntax
==============

Example 1: Bullet list
~~~~~~~~~~~~~~~~~~~~~~

..  code-block:: rest

   this is some text

   *  this is a list item
   *  another item

   more text

**How it looks:**

this is some text

*  this is a list item
*  another item

more text


Example 2: List with sublist
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

..  code-block:: rest

   this is some text

   *  this is a list item

      *  this is a sublevel list item
      *  another item

   this is more text


How it looks:

this is some text

*  this is a list item

   *  this is a sublevel list item
   *  another item

this is more text


Wrong syntax
------------

..  code-block:: rest

   this is some text
   *  this is a list item
   *  another item
   more text

How it looks:

this is some text
*  this is a list item
*  another item
more text


Additional information
======================

*  `Docutils cheat-sheet for reStructuredText: Bullet list
   <http://docutils.sourceforge.net/docs/user/rst/quickref.html#bullet-lists>`__
*  :ref:`Section on lists in this guide <rest-lists>`
*  `Docutils cheat-sheet for reStructuredText: Enumerated lists
   <http://docutils.sourceforge.net/docs/user/rst/quickref.html#enumerated-lists>`__
