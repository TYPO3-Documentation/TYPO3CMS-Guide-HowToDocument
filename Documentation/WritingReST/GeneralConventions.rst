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


For your own texts you may use any style you want.

For “official” manuals (on docs.typo3.org) you should follow these conventions:


Formatting
==========

Encoding
--------

* use utf-8

Whitespace and indenting
------------------------

* remove white space from the end of lines (= no trailing tabs or spaces)
* don't use tabs
* one indentenation level consists of three spaces
* code examples use three spaces as indentation level as well

Line length
-----------

* Keep lines shorter than 80 characters.
* if in doubt about the length: use short lines!

  * That way reST is readable as source as well
  * Files can be easily edited directly on Github
  * Files can be compared in a diff view

Other
-----

* do not use in headlines ``A :ts:`page` value``
* the only way to include "special" characters is to use them directly