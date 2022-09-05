..  include:: /Includes.rst.txt
..  highlight:: rst
..  index::
    reST; Toctree
    Manual; Hierarchical structure
..  _toctree:
..  _rest-menu-hierachy:

==================================================
Toctree and the hierarchical structure of a manual
==================================================

You can define what should be included in the menu with the
`..  toctree:: <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-toctree>`__ directive.
Only `.rst` files that are included in a toctree, are included in the menu.

The toctree directive can also be used to display a table of contents
on current page (if :hidden: is not added in toctree).

The first headline of an .rst file is its "doctitle". That is the document's
title property. The title and the following headlines are used for
cross-references and appear in menus and table of contents.

..  index:: reST directives; toctree

General rules for using `..toctree::`
=====================================

..  rst-class:: bignums

1. Each .rst file should have a doctitle, for example:

    ..  code-block:: rest

        ==========
        Some Title
        ==========

2. Do not use any additional headlines in the file **if** it contains a `..  toctree::` directive.

*Note:* What we call "headlines" here is called "sections" in reST-jargon, see :ref:`Headlines-and-sections`.


Toctree examples
================


Example: hidden
---------------

This will create a menu, using the header of Introduction/Index.rst and Configuration/Index.rst.
The menu structure is not displayed as a table of contents on the current page ("hidden").

..  code-block:: rest
    :linenos:

        ..  toctree::
            :hidden:

            Introduction/Index
            Configuration/Index


Example: glob, not hidden, titlesonly
-------------------------------------

This will read all files and create a menu. It will also render the menu
structure on the current page. It will read the files using globbing (*),
meaning you do not need to explicitly write the file names. If new files are added,
the menu will be updated automatically. Only the doctitle (first header in
file) will be displayed (titlesonly).

..  code-block:: rest
    :linenos:


        ..  toctree::
            :glob:
            :titlesonly:

            *

Example: https://docs.typo3.org/typo3cms/ContributionWorkflowGuide/Appendix/Index.html


How it works
============

2017-02-13 by Martin Bless

TYPO3 documentation usually starts with the file :file:`PROJECT/Documentation/Index.rst`.
The text may go into more than one textfile and these can be "pulled in" and
referenced by the
`..  toctree:: <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-toctree>`__
directive. Note:

#.  Each `..  toctree::` directive creates a *sublevel* of headlines in the menu.

#.  The sublevel refers to the *current level*.

Problem
    Sometimes you don't get what you expect:

    ..  code-block:: rst

        ================
        My Documentation
        ================

        Introduction
        ============
        This project does something very useful ...
        See the individual chapters.

        ..  toctree::

            Chapter-1
            Chapter-2
            Chapter-3

    The example feels very natural. We are thinking of the introduction
    followed by the single chapters. Unfortunately we get something different.
    The chapters will all be a *subpart* of *Introduction* and not at the same level.
    It is exactly what the Sphinx documentation states and there is no easy way to
    "tweak" this behavior.

Solution
    Use these rules of thumb:

    #.  All or nothing: Pull in *all* content of a given level via `toctree`
        or don't use `toctree` at all.

    #.  Or, in other words:
        Do not use a headline ("section") in a document before a `..  toctree::`
        directive unless you really want to place the pulled in documents
        at a *sublevel of that section*.

    Here is how we can fix the example: Move the introduction to an extra
    file and pull it in just like the others.

    **Fixed example:**

    ..  code-block:: rst

        ================
        My Documentation
        ================

        You can have text here. But don't introduce headlines,
        if you want to have the pulled in files at the same level.

        ..  toctree::

            Introduction
            Chapter-1
            Chapter-2
            Chapter-3

    Now the *document titles* (not shown here) of the files :file:`Introduction.rst`,
    :file:`Chapter-1.rst`, :file:`Chapter-2` and :file:`Chapter-3` will all be at the
    sublevel of `My Documentation` in the menu.

