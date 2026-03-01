:navigation-title: Float and alignment

..  include:: /Includes.rst.txt
..  _image-float-alignment:

==========================================
Image and figure floating and alignment
==========================================

..  versionadded:: 0.37.0
    Float and alignment support for images and figures was introduced in
    render-guides version 0.37.0.

Images and figures can be floated to the left or right so that surrounding
text wraps around them. This is useful for inline illustrations, icons,
or any image that should be embedded within a text flow rather than
displayed as a standalone block.

There are two ways to apply floating:

1.  **CSS classes** ``:class: float-left`` or ``:class: float-right`` — works on
    both ``..  image::`` and ``..  figure::`` directives.
2.  The ``:align:`` **option** — ``:align: left``, ``:align: right``, or ``:align: center``
    — works on ``..  figure::`` directives (internally mapped to the same CSS
    classes).

Both approaches produce the same visual result. Use whichever fits your
preference.

.. _image-float-css-classes:

Float with CSS classes
======================

Add ``float-left`` or ``float-right`` to the ``:class:`` option. You can combine
these with other classes such as ``with-shadow`` or ``with-border``:

..  code-block:: rst

    ..  figure:: /Images/MyImage.png
        :alt: Description of the image
        :class: float-left with-shadow

        Caption text here

    Surrounding text will wrap to the right of the image.

.. _image-float-align-option:

Align option
============

The ``:align:`` option on ``..  figure::`` directives supports ``left``, ``right``,
and ``center``. Values ``left`` and ``right`` produce the same floating behavior
as the CSS classes:

..  code-block:: rst

    ..  figure:: /Images/MyImage.png
        :alt: Description of the image
        :align: right

        Caption text here

    Surrounding text will wrap to the left of the image.

Using ``:align: center`` centers the figure without any text wrapping.

.. _image-float-clearing:

Clearing floats
===============

After a floated image, you may want subsequent content to appear below the
image rather than wrapping around it. Use the ``clear-both`` class to clear
floats:

..  code-block:: rst

    ..  figure:: /Images/MyImage.png
        :alt: Description of the image
        :class: float-left

        Caption

    This text wraps around the image.

    ..  rst-class:: clear-both

    This text appears below the image.

The ``..  rst-class:: clear-both`` directive applies the CSS ``clear: both``
property to the next element, forcing it below any floated content.

.. _image-float-responsive:

Responsive behavior
===================

Floated images automatically switch to full-width block display on small
screens (below 576px). This ensures readable text on mobile devices
without horizontal scrolling.

.. _image-float-example-8:

Example 8: Figure floated left
------------------------------

..  figure:: /_Images/a4.jpg
    :alt: Example figure floated left
    :class: float-left with-shadow
    :width: 150px

    A figure floated to the left

Typesetting is the composition of text by means of arranging physical types
or the digital equivalents. Stored letters and other symbols are retrieved
and ordered according to a language's orthography for visual display.
Typesetting requires one or more fonts.

..  rst-class:: clear-both

..  code-block:: rst

    ..  figure:: /_Images/a4.jpg
        :alt: Example figure floated left
        :class: float-left with-shadow
        :width: 150px

        A figure floated to the left

    Typesetting is the composition of text by means of arranging
    physical types or the digital equivalents. ...

    ..  rst-class:: clear-both

.. _image-float-example-9:

Example 9: Figure aligned right
--------------------------------

..  figure:: /_Images/a4.jpg
    :alt: Example figure aligned right
    :align: right
    :width: 150px

    A figure aligned right via ``:align:``

Typesetting is the composition of text by means of arranging physical types
or the digital equivalents. Stored letters and other symbols are retrieved
and ordered according to a language's orthography for visual display.
Typesetting requires one or more fonts.

..  rst-class:: clear-both

..  code-block:: rst

    ..  figure:: /_Images/a4.jpg
        :alt: Example figure aligned right
        :align: right
        :width: 150px

        A figure aligned right via :align:

    Typesetting is the composition of text by means of arranging
    physical types or the digital equivalents. ...

    ..  rst-class:: clear-both

.. _image-float-example-10:

Example 10: Image floated left with shadow
-------------------------------------------

..  image:: /_Images/a4.jpg
    :alt: Example image floated left
    :class: float-left with-shadow
    :width: 150px

Typesetting is the composition of text by means of arranging physical types
or the digital equivalents. Stored letters and other symbols are retrieved
and ordered according to a language's orthography for visual display.
Typesetting requires one or more fonts.

..  rst-class:: clear-both

..  code-block:: rst

    ..  image:: /_Images/a4.jpg
        :alt: Example image floated left
        :class: float-left with-shadow
        :width: 150px

    Typesetting is the composition of text by means of arranging
    physical types or the digital equivalents. ...

    ..  rst-class:: clear-both

.. _image-float-best-practices:

Best practices for floating
============================

*   Always use ``..  rst-class:: clear-both`` after floated content to prevent
    layout issues with subsequent sections
*   Set an explicit ``:width:`` on floated images to control how much space
    text has to wrap around
*   Floated figures are limited to 50% of the page width to ensure readability
*   Prefer ``:align:`` on figures for cleaner RST syntax; use ``:class:`` when you
    need to combine float with other classes like ``with-shadow``
*   Test on narrow viewports to verify the responsive behavior
