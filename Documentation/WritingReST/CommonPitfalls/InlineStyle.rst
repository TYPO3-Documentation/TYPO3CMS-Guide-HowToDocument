.. include:: ../../Includes.txt
.. highlight:: rst

.. _common-pitfalls-inline-style:

==========================
Problems With Inline Style
==========================


If you use **bold** or *italic*, make sure there is no space between
the markup and the styled text.


Correct Syntax
--------------

::

   This is normal text. **This is bold text.**

How it looks:


   This is normal text. **This is bold text.**

Wrong Syntax
------------

::

   This is normal text. ** This is bold text.**

How it looks:


   This is normal text. ** This is bold text.**


Additional Information
======================

* `Docutils cheat-sheet for reStructuredText: Inline markup
  <http://docutils.sourceforge.net/docs/user/rst/quickref.html#inline-markup>`__
