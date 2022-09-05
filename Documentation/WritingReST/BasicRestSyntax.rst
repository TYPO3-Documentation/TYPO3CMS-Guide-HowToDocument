..  include:: /Includes.rst.txt
..  highlight:: rst
..  index:: reST; Syntax
..  _basic-rest-syntax:

==========================
Basic reST & Sphinx syntax
==========================

The .rst files are written in reStructuredText (reST) format. They
contain text with additional markup.


..  index:: reST; Paragraphs

Paragraphs
==========

New paragraphs in the output are created by an empty line
between two paragraphs in your reST file::

    This is a paragraph.

    This is another paragraph.


..  index:: reST; Comments

Comments
========

Comments can be written like this::

    ..  this is a comment
    ..  with another line

Or like this::

    ..  this is a comment
        with another line


..  index:: reST; Indentation

Indentation
===========

In reST, the indentation of a block of lines is often important. The exact number of spaces,
which are used to indent a block of text, does not matter. But what does matter, is that all lines
of the block are indented with exactly the same number of spaces.

We use the convention of 4 spaces per indenting level (see :ref:`cgl-indenting`).

Let's look at an example:

The following directive inserts an image in the rendered page. All lines beginning with line
two must be indented to the same leve. The convention is to use 4 spaces for one
level of indentation.

..  code-block:: rest

    ..  image:: someimage.png
        :class: with-border with-shadow
        :alt: Textual alternative to the image


..  index:: reST; Escape characters

Escape characters
=================

If you want to use a character, which would create some special reST markup,
with its normal meaning, you must escape it with a prepended "\".

For example surrounding text with "*" signs normally makes it show up in italics. By
escaping the special characters "*" you make the stars normal text characters::

    \*non-italic\*
