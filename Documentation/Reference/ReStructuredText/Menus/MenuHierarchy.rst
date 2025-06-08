:navigation-title: Main menu

..  include:: /Includes.rst.txt
..  _toctree:
..  _rest-menu-hierachy:

=========================================
Main menu of a TYPO3 documentation manual
=========================================

A manual consisting of more then one page should have a menu displayed on the
left side of each page.

There are different strategies to get such a menu:

..  _menu-automatic:

Automatically created alphabetic menu
=====================================

If you do not want to deal with creating menus you can use the automatic menu.

Add the following option to the `<guides>` tag in your
:file:`Documentation/guides.xml`:

..  code-block:: xml
    :caption: Documentation/guides.xml

    <guides
        automatic-menu="true"
        <!-- ... -->

Using the `.. toctree::` directive takes no effect in adjusting the menu then.
When you use the automatic menu you cannot influence the order in the menu.

..  _menu-semi-automatic:

Semi-automatic menu
===================

If you want to display some pages on top (like installation and introduction)
but list all other pages automatically you can use a `..  toctree::` directive
with a glob pattern on your start page:

..  code-block:: rst
    :caption: Documentation/Index.rst

    ..  toctree::
        :glob:
        :hidden:

        Introduction
        Installation
        Usage/Index
        *
        */Index

The menu will now contain first the listed pages, then all other `.rst` files
in the root directory, then all `Index.rst` files in subdirectories. If you
have additional `.rst` files in sub directories, you need to add such a toctree
to the `Index.rst` in the sub directory.

If you use the `The init command <https://docs.typo3.org/permalink/h2document:init-command>`_
to create a new ReST documentation we prepared such a menu for you.

..  _menu-manual:

Manual menu using the toctree directive
=======================================

You can define what should be included in the menu with the
`..  toctree:: <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-toctree>`__ directive.
Only `.rst` files that are included in a toctree, are included in the menu.

The toctree directive can also be used to display a table of contents
on current page (if :hidden: is not added in toctree).

The first headline of an .rst file is its "doctitle". That is the document's
title property. The title and the following headlines are used for
cross-references and appear in menus and table of contents.

..  _menu-hidden:

`:hidden:` option
-----------------

If you do not want to display the menu in the place where the toctree is
defined use the `:hidden:` option. The toctree will only be used to define
the right hand menu then.

..  code-block:: rst
    :linenos:

    ..  toctree::
        :hidden:

        Introduction/Index
        Configuration/Index

..  _menu-titlesonly:

`:titlesonly:` and `:maxdepth:` options
---------------------------------------

If the menu is not hidden by default **all** headlines from the included pages
will be displayed. If you use the option `:titlesonly:` only the page titles are
displayed.

..  code-block:: rst
    :linenos:

    ..  toctree::
        :glob:
        :titlesonly:
        :maxdepth: 2

        *

You can limit the number of submenu points to be displayed in the place the
menu was entered by using option `:maxdepth:`. Neither option influences the
right hand menu.

..  _menu-rules:

General rules for using pages
=============================

Each `.rst` file that is included in the menu **must** have a page title and
should have a short
`navigation title <https://docs.typo3.org/permalink/h2document:navigation-title>`_.

..  literalinclude:: _Include/_page.rst.txt
    :caption: Documentation/Introduction.rst

If a page should not be included in the menu it must be marked as `:orphan:` in
the first line. Orphaned pages are not included in semi-automatic menus with
the `:glob:` option. See `Orphaned pages <https://docs.typo3.org/permalink/h2document:rest-orphans>`_.

Each non orphaned page **must** be included in the menu **exactly once**.
Including the same page in multiple pages in the menu will cause warnings and
might produce unexpected results.
