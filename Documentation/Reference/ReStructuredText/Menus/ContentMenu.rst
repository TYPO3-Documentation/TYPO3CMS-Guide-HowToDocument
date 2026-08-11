..  include:: /Includes.rst.txt
..  index::
    Menus; Content
..  _content-menu:

============
Content menu
============

You can display the titles of the current page as a content menu.

The simplest content menu can be created like this:

..  code-block:: rst

    ..  contents::
        :local:

Showing only a local content menu of all headlines, excluding the page header:

..  contents::
    :local:

You can also limit the levels and or give the contents menu a title:

..  code-block:: rst

    ..  contents:: Table of Contents
        :local:
        :depth: 1

To limit the header to a given depth:

..  contents:: Table of Contents
    :local:
    :depth: 1


..  _content-menu-topic-1:

Topic 1
=======

Here we go.

..  _content-menu-topic-1-subtopic-1-1:

Subtopic 1.1
------------

Here we dive deeper

..  _content-menu-topic-1-subtopic-1-1-subsubtopic-1-1:

Subsubtopic 1.1.1
~~~~~~~~~~~~~~~~~

And this is even more specific.

..  _content-menu-topic-2:

Topic 2
=======

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod
tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.

..  _content-menu-topic-2-subtopic-2-1:

Subtopic 2.1
------------

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod
tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.

..  _content-menu-topic-2-subtopic-2-2:

Subtopic 2.2
------------


Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod
tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.

..  _content-menu-topic-2-subtopic-2-2-subsubtopic-2-2:

Subsubtopic 2.2.1
~~~~~~~~~~~~~~~~~

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod
tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.
