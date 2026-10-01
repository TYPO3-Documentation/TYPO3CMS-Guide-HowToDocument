:navigation-title: Float and alignment

..  include:: /Includes.rst.txt
..  _image-float-alignment:

=======================================
Image and figure floating and alignment
=======================================

..  versionadded:: 0.37.0
    Float and alignment support for images and figures was introduced in
    render-guides version 0.37.0.

Images and figures can be floated to the left or right so that surrounding
text wraps around them. This is useful for inline illustrations, icons,
or any image that should be embedded within a text flow rather than
displayed as a standalone block.

..  _image-float-css-classes:
..  _image-float-align-option:

Align option
============

Use the :rst:`:align:` option to float an image or figure. It works on both
:rst:`..  image::` and :rst:`..  figure::` directives and supports :rst:`left`,
:rst:`right`, and :rst:`center`. Other classes such as :rst:`with-shadow` go
into the :rst:`:class:` option next to it:

..  code-block:: rst

    ..  figure:: /Images/MyImage.png
        :alt: Description of the image
        :align: right
        :class: with-shadow

        Caption text here

    Surrounding text will wrap to the left of the image.

Using :rst:`:align: center` centers the figure without any text wrapping.

The CSS classes :rst:`float-start` and :rst:`float-end` in :rst:`:class:` still
float an image the same way. The Bootstrap 4 class names :rst:`float-left` and
:rst:`float-right` are deprecated: the renderer rewrites them to
:rst:`float-start` and :rst:`float-end` and logs a warning.

..  _image-float-clearing:

Clearing floats
===============

After a floated image, you may want subsequent content to appear below the
image rather than wrapping around it. Use the :rst:`clear-both` class to clear
floats:

..  code-block:: rst

    ..  figure:: /Images/MyImage.png
        :alt: Description of the image
        :align: left

        Caption

    This text wraps around the image.

    ..  rst-class:: clear-both

    This text appears below the image.

The :rst:`..  rst-class:: clear-both` directive applies the CSS `clear: both`
property to the next element, forcing it below any floated content.

..  _image-float-responsive:

Responsive behavior
===================

Floated images automatically switch to full-width block display on small
screens (below 576px). This ensures readable text on mobile devices
without horizontal scrolling.

..  _image-float-example-8:

Example 8: figure floated left
------------------------------

..  figure:: /_Images/a4.jpg
    :alt: Example figure floated left
    :align: left
    :class: with-shadow
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
        :align: left
        :class: with-shadow
        :width: 150px

        A figure floated to the left

    Typesetting is the composition of text by means of arranging
    physical types or the digital equivalents. ...

    ..  rst-class:: clear-both

..  _image-float-example-9:

Example 9: figure aligned right
-------------------------------

..  figure:: /_Images/a4.jpg
    :alt: Example figure aligned right
    :align: right
    :width: 150px

    A figure aligned right via :rst:`:align:`

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

..  _image-float-example-10:

Example 10: image floated left with shadow
------------------------------------------

..  image:: /_Images/a4.jpg
    :alt: Example image floated left
    :align: left
    :class: with-shadow
    :width: 150px

Typesetting is the composition of text by means of arranging physical types
or the digital equivalents. Stored letters and other symbols are retrieved
and ordered according to a language's orthography for visual display.
Typesetting requires one or more fonts.

..  rst-class:: clear-both

..  code-block:: rst

    ..  image:: /_Images/a4.jpg
        :alt: Example image floated left
        :align: left
        :class: with-shadow
        :width: 150px

    Typesetting is the composition of text by means of arranging
    physical types or the digital equivalents. ...

    ..  rst-class:: clear-both

..  _image-float-best-practices:

Best practices for floating
===========================

*   Always use :rst:`..  rst-class:: clear-both` after floated content to prevent
    layout issues with subsequent sections
*   Set an explicit :rst:`:width:` on floated images to control how much space
    text has to wrap around
*   Floated figures are limited to 50% of the page width to ensure readability
*   Prefer :rst:`:align:` for floating; add other classes like :rst:`with-shadow`
    with :rst:`:class:` next to it
*   Test on narrow viewports to verify the responsive behavior
