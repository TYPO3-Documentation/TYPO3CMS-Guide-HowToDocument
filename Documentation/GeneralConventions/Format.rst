.. include:: /Includes.rst.txt
.. highlight:: rst

.. _supported-formats:

========================
Formats (reST, Markdown)
========================


.. _formats-rest:

reST
====

.. important::

   The entire official documentation uses reST only. This includes
   the the Guides, Tutorials, "TYPO3 Explained", Reference,
   the Changelog and system extensions.

The rendering chain and tools are built and optimized to process reST markup. Please
go ahead and use that format.

The file ending of reST files is .rst.

The tool `pandoc` can convert existing markdown file into reST format.
Do this once and you are in line with the TYPO3 conventions.


.. _formats-markdown:

Markdown
========

Currently, you can also use markdown for your (extension) documentation.

One problem with markdown is that there are many dialects. Since a while there is a standard **commonmark**.
At https://readthedocs.org people are trying to make commonmark available.
See http://blog.readthedocs.com/adding-markdown-support/ for the details.
Without doing lots of investigations we have implemented the same solution for TYPO3 documentation as well.

This means that our rendering tools detect markdown files as well. They have .md as file ending.

If you’re encountering problems with the rendering of your markdown files, consider switching to reST.


reST vs. Markdown
=================

Victor Zverovich makes the comparison::

   According to John Gruber, the inventor of Markdown, “Markdown’s syntax is intended for one
   purpose: to be used as a format for writing for the web.” and, in particular, it supports inline HTML.
   reStructuredText on the other hand is specifically designed for writing technical documentation.


readthedocs::

   "It should be noted that Commonmark doesn’t support a lot of the concepts that RST lets you represent.
   In particular, there is no standardized way in Commonmark to represent inline or block levels constructs.
   So things like the toctree directive and :ref: markup don’t have an analog."

`Read the Docs & Sphinx now support Commonmark <https://blog.readthedocs.com/adding-markdown-support/>`__ (2015)


**reST (with our Sphinx Toolchain)**

`+`

*  extendable
*  semantic markup
*  cross-references across manuals (links still work if text is moved - unless moved to a different manual)
*  richer feature set

`-`

*  Syntax may be unusual and rendering breaks if not done correctly, e.g.

   *  indenting is important
   *  new lines are important, e.g. before, after and between bullet lists
   *  more, see :ref:`rest-common-pitfalls`

*  some people simply hate it

**Markdown**

`+`

*  in general better tool support
*  widely supported
*  syntax is (mostly) simpler and easier to read

`-`

*  various flavors (unless **commonmark** is used)
*  less features


Additional information
----------------------


*  Eli Bendersky: `"reStructuredText vs. Markdown for technical documentation"
   <https://eli.thegreenplace.net/2017/restructuredtext-vs-markdown-for-technical-documentation/>`__ (February 24, 2017)
*  Victor Zverovich: `"reStructuredText vs Markdown for documentation" <https://www.zverovich.net/2016/06/16/rst-vs-markdown.html>`__ (2016)
*  Eric Holscher: `"Why You Shouldn’t Use “Markdown” for Documentation"
   <https://www.ericholscher.com/blog/2016/mar/15/dont-use-markdown-for-technical-docs/>`__ (March 15, 2016)
*  Eric Holscher: `Read the Docs & Sphinx now support Commonmark <https://blog.readthedocs.com/adding-markdown-support/>`__ (2015)
