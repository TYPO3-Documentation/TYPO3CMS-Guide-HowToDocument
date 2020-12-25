.. include:: /Includes.rst.txt
.. highlight:: rst
.. index:: reST; Inline styles
.. _common-pitfalls-inline-style:

==========================
Problems with inline style
==========================


If you use **bold** or *italic*, make sure there is no space between
the markup and the styled text.


Correct syntax
--------------

::

   This is normal text. **This is bold text.**

How it looks:


This is normal text. **This is bold text.**


Wrong syntax
------------

::

   This is normal text. ** This is bold text.**

How it looks:


This is normal text. ** This is bold text.**


Additional information
======================

*  `Docutils cheat-sheet for reStructuredText: Inline markup
   <http://docutils.sourceforge.net/docs/user/rst/quickref.html#inline-markup>`__
