
.. include:: ../Includes.txt
.. highlight:: shell


=========================
Markup: reST and Markdown
=========================

((to be written))

Markup: reST
============

TYPO3 documentation uses `reStructuredText` for markup. The rendering chain and tools are built
and optimized to process reST markup. Please go ahead and use that format.

The file ending of reST files is :file:`.rst`.

You can use reST format at Github as well.

You can write H1 and H2 headlines in markdown the same way as reST does it. So for simple
documents like a README file the markup can almost be the same.

The tool `pandoc` can convert existing markdown file into reST format. Do this once and
you are in line with the TYPO3 conventions.

Markup: Markdown
================

One problem with markdown is that there are many dialects. Since a while there is a standard "commonmark".
At https://readthedocs.org people are trying to make commonmark available. See http://blog.readthedocs.com/adding-markdown-support/ for the details. Without doing lots of investigations we have implemented the same
solution for TYPO3 documentation as well.

This means that our rendering tools detect markdown files as well. They have :file:`.md` as file ending.

If you're encountering problems with the rendering of your markdown files consider switching to reST.
