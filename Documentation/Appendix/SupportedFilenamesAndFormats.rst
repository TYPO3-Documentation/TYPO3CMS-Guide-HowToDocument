.. include:: ../Includes.txt
.. highlight:: rst

.. _supported-filenames-and-formats:

============================================
Additionally supported filenames and formats
============================================


.. important::

   This information is included for the sake of completeness. It is however
   not recommended to do it this way. For best results, follow the guidelines
   in :ref:`general-conventions`.

Name of start page
==================


It is recommended to name the startpage `Documentation/Index.rst`. The following
is also supported (in this order):

#. :file:`Documentation/Index.rst`
#. :file:`Documentation/index.rst`
#. :file:`Documentation/Index.md`
#. :file:`Documentation/index.md`
#. :file:`README.rst`
#. :file:`README.md`


If none of these files exist, no documentation will be rendered.


Rendering formats
=================

Using reST is strongly recommended.

reST (recommended)
------------------

TYPO3 documentation uses reStructuredText for markup. The rendering
chain and tools are built and optimized to process reST markup. Please
go ahead and use that format.

The file ending of reST files is .rst.

The tool `pandoc` can convert existing markdown file into reST format.
Do this once and you are in line with the TYPO3 conventions.


Markdown
--------

Currently, you can also use markdown for your documentation.

One problem with markdown is that there are many dialects. Since a while there is a standard “commonmark”.
At https://readthedocs.org people are trying to make commonmark available.
See http://blog.readthedocs.com/adding-markdown-support/ for the details.
Without doing lots of investigations we have implemented the same solution for TYPO3 documentation as well.

This means that our rendering tools detect markdown files as well. They have .md as file ending.

If you’re encountering problems with the rendering of your markdown files, consider switching to reST.

