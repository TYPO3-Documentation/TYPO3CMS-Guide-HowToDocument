.. include:: ../../Includes.txt
.. highlight:: rst


=====================
Problems with Headers
=====================


If you use section titles (headers), the underline must be **at least** as long as the text.

Though you can make the underlines longer than the text, common practice
througout the docs is to to keep it the same length.

.. tip::

   If you use an IDE with good reStructuredText support, it should point
   out this error correctly, for example if you use PhpStorm, enable
   the `reStructuredText plugin <https://plugins.jetbrains.com/plugin/7124-restructuredtext-support>`__.



Correct Syntax
==============

::

   ================
   This is a Header
   ================

   Another Header
   ==============


   This Is Also Correct but Not Recommended
   ======================================================


Wrong Syntax
============


::

   Another header
   ------------




Additional Information
======================

* :ref:`Headlines-and-sections`
* `reStructuredText Primer: Sections <http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#sections>`__
