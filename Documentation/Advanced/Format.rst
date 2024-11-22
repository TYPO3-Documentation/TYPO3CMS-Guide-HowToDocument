.. include:: /Includes.rst.txt
.. index:: Documentation; Formats
.. _supported-formats:

========================
Formats (reST, Markdown)
========================


.. index::
   Documentation; reST
   reST
.. _formats-rest:

reST
====

.. important::

   The entire official documentation uses reST only. This includes
   the the Guides, Tutorials, "TYPO3 Explained", Reference,
   the Changelog and system extensions.

The rendering chain and tools are built and optimized to process reST markup. We
recommend using this format for your documentation. As reST is more feature-rich,
and you will benefit from the advanced features of the TYPO3 documentation toolchain.

The file ending of reST files is .rst.

When you started your documentation in markdown, you can convert it to reST using
our migration tool.

.. index::
   Documentation; Markdown
   Markdown
.. _formats-markdown:

Markdown
========

However we do highly recommend using reST for your documentation, we also support markdown for
your (extension) documentation. The file ending of markdown files is .md.

Our toolchain supports the `commonmark dialect of markdown <https://commonmark.org/>`__.
This is a standardized version of markdown. We do not support other markdown dialects, although
they might work. We cannot guarantee that they will work in the future.
You can consult our Markdown reference for more information.

.. index::
   reST; vs. Markdown
   Markdown; vs. reST

reST vs. Markdown
=================

Victor Zverovich makes the comparison:

   According to John Gruber, the inventor of Markdown, “Markdown’s syntax is intended for one
   purpose: to be used as a format for writing for the web.” and, in particular, it supports inline HTML.
   reStructuredText on the other hand is specifically designed for writing technical documentation.


readthedocs:

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

*  Syntax may be unusual and rendering breaks if not done correctly, for example

   *  indenting is important
   *  new lines are important, for example before, after and between bullet lists

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
