.. include:: ../Includes.txt
.. highlight:: rst

.. _supported-formats:

==========================================
Formats
==========================================

Using reStructuredText (reST) is strongly recommended.

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

Markdown
========

Currently, you can also use markdown for your documentation.

One problem with markdown is that there are many dialects. Since a while there is a standard **commonmark**.
At https://readthedocs.org people are trying to make commonmark available.
See http://blog.readthedocs.com/adding-markdown-support/ for the details.
Without doing lots of investigations we have implemented the same solution for TYPO3 documentation as well.

This means that our rendering tools detect markdown files as well. They have .md as file ending.

If you’re encountering problems with the rendering of your markdown files, consider switching to reST.

Additional Information
======================

* Eli Bendersky: `"reStructuredText vs. Markdown for technical documentation"
  <https://eli.thegreenplace.net/2017/restructuredtext-vs-markdown-for-technical-documentation/>`__ (February 24, 2017)
* Eric Holscher: `"Why You Shouldn’t Use “Markdown” for Documentation"
  <https://www.ericholscher.com/blog/2016/mar/15/dont-use-markdown-for-technical-docs/>`__ (March 15, 2016)
