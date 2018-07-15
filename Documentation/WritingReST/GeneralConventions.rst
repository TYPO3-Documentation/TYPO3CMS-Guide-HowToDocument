.. include:: ../Includes.txt
.. highlight:: rst

.. _Formatting-reST-Source-Files:

==================================
General Conventions for reST files
==================================

**On this page:**

.. rst-class:: compact-list

.. contents::
   :local:
   :backlinks: top


Includes.txt
============

Every reST file must include the file Includes.txt. Use the correct path!

.. code-block:: rest

   .. include:: ../Includes.txt

Encoding
========

* use utf-8

Whitespace and indenting
========================

.. important::

   Always use indentation levels correctly (3 spaces). Your code may not
   be rendered correctly if you do not.

* remove white space from the end of lines (= no trailing tabs or spaces)
* don't use tabs
* one indentenation level consists of three spaces
* code examples use three spaces as indentation level as well

Example:

.. code-block:: rest
  :linenos:

   .. image:: ../images/a4.jpg
      :alt: Left floating image
      :target: https://typo3.org
      :class: with-shadow


* lines 2-4 must be indented one level (3 spaces)


Line length
===========

* Keep lines shorter than 80 characters.
* if in doubt about the length: use short lines!

  * That way reST is readable as source as well
  * Files can be easily edited directly on Github
  * Files can be compared in a diff view

Miscellaneous
=============

* do not use in headlines ``A :ts:`page` value``
* the only way to include "special" characters is to use them directly