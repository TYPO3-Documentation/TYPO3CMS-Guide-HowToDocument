..  include:: /Includes.rst.txt
..  highlight:: rst
..  index::
    Menus; Content
..  _content-menu:

============
Content menu
============

You can display the titles of the current page as a content menu.

The simplest content menu can be created like this::

    ..  contents::
        :local:

Showing only a local content menu of all headlines, excluding the page header:

..  contents::
    :local:

You can also limit the levels and or give the contents menu a title::

    ..  contents:: Table of Contents
        :local:
        :depth: 1

To limit the header to a given depth:

..  contents:: Table of Contents
    :local:
    :depth: 1


Topic 1
=======

Here we go.

Subtopic 1.1
------------

Here we dive deeper

Subsubtopic 1.1.1
~~~~~~~~~~~~~~~~~

And this is even more specific.

Topic 2
=======

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod
tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.

Subtopic 2.1
------------

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod
tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.

Subtopic 2.2
------------


Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod
tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.

Subsubtopic 2.2.1
~~~~~~~~~~~~~~~~~

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod
tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.
