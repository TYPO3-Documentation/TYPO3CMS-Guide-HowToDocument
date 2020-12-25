.. include:: /Includes.rst.txt
.. highlight:: rst

.. index:: reST; Syntax
.. _basic-rest-syntax:

==========================
Basic reST & Sphinx syntax
==========================

.. note::

   Some of this text was taken from the Wiki page:
   https://wiki.typo3.org/ReST_Syntax

The .rst files are written in reStructuredText (reST) format. They
contain text with additional markup.


.. index:: reST; Paragraphs

Paragraphs
==========

New paragraphs in the output are created by an empty line
between two paragraphs in your reST file::

   This is a paragraph.

   This is another paragraph.


.. index:: reST; Comments

Comments
========

Comments can be written like this::

   .. this is a comment
   .. with another line

Or::

   .. this is a comment
      with another line


.. index:: reST; Indentation

Indentation
===========

In reST, the indentation of a block of lines is often important. The exact number of spaces,
which are used to indent a block of text, does not matter. But what does matter, is that all lines
of the block are indented with exactly the same number of spaces.

We use the convention of 3 spaces per indenting level (see :ref:`cgl-indenting`).

Let's look at an example:

The following directive inserts an image in the rendered page. All lines beginning with line
two must be indented with one indenting level (3 spaces).

.. code-block:: rest
   :linenos:

   .. _image: someimage.png
      :class: with-shadow
      :alt: Explanation of image


.. index:: reST; Escaping characters

Escaping characters
===================

If you want to use a character, which would create some special reST markup,
with its normal meaning, you must escape it with a prepended "\".

E.g. surrounding text with "*" signs normally makes it show up in italics. By
escaping the special characters "*" you make the stars normal text characters::

   \*non-italic\*
