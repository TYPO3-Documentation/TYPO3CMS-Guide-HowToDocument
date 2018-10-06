.. include:: ../Includes.txt

.. highlight:: rst


.. _rest-common-pitfalls:

===============
Common pitfalls
===============

Here we describe some common mistakes. Read this page before you start
in order to avoid common errors.

Problem with inline style
=========================

If you use **bold** or *italic*, make sure there is no space between the markup
and the text.

**See also:**

* `Docutils cheat-sheet for reStructuredText: Inline markup <http://docutils.sourceforge.net/docs/user/rst/quickref.html#inline-markup>`__

Do:
---

::

   This is normal text. **This is bold text.**
   
**How it looks:**

This is normal text. **This is bold text.**

Don't:
------

::

   This is normal text. ** This is bold text.**

**How it looks:**

This is normal text. ** This is bold text.**

Problems with lists
===================

If you use lists, make sure there is an empty line before and after the
list. If you use lists with sublevels, make sure there is an empty line
between the levels.

The same applies for bullet lists and enumerated lists

**See also:** 

* `Docutils cheat-sheet for reStructuredText: Bullet list <http://docutils.sourceforge.net/docs/user/rst/quickref.html#bullet-lists>`__
* :ref:`Section on lists in this guide <rest-lists>`
* `Docutils cheat-sheet for reStructuredText: Enumerated lists <http://docutils.sourceforge.net/docs/user/rst/quickref.html#enumerated-lists>`__

Do
--

Example 1: Bullet list
~~~~~~~~~~~~~~~~~~~~~~

::

   this is some text

   * this is a list item
   * another item

   more text

**How it looks:**

this is some text

* this is a list item
* another item

more text

Example 2: Enumerated list
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   this is some text
   
   #. This is a list item
   #. Another item
   
   more text
   
**How it looks:**

this is some text

#. This is a list item
#. Another item

more text


Example 3: List with sublist
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

   this is some text

   * this is a list item

      * this is a sublevel list item
      * another item

   this is more text


**How it looks:**

this is some text

* this is a list item

   * this is a sublevel list item
   * another item

this is more text


Don't
-----

::

   this is some text
   * this is a list item
   * another item
   more text

**How it looks:**

this is some text
* this is a list item
* another item
more text

Problem with indents
====================

Always indent correctly (3 spaces per level)

Do
--

::

   .. image:: ../images/a4.jpg
      :width: 100px
      :class: with-shadow

**How it looks**

.. image:: ../images/a4.jpg
   :width: 100px
   :class: with-shadow

Don't
-----

Here, `:width:` is indented with only 2 spaces. The image will not be
rendered at all!

::

   .. image:: ../images/a4.jpg
     :width: 100px
      :class: with-shadow

**How it looks**

.. image:: ../images/a4.jpg
  :width: 100px
   :class: with-shadow
