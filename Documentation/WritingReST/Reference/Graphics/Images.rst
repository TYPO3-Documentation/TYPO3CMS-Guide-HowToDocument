..  include:: /Includes.rst.txt
..  highlight:: rst
..  index:: pair: reST; Images
..  _how-to-document-images:
..  _rest-images:
..  _images:

======
Images
======

..  index:: automatic screenshot generation
..  _automatic-screenshots:

Automatic screenshot generation
===============================

See the `README in the t3docs-screenshots <https://github.com/TYPO3-Documentation/t3docs-screenshots/blob/main/README.rst>`__
for more information on automating screenshot generation.

..  index:: reST directives; image

How to use images
=================

Use the `..  image::` directive with additional parameters.

Use `..  figure::` if you want to add a caption to your image.
You can use the same parameters in figure that are defined for image.

The
additional parameters must be indented one level (add 4 spaces to indent).

Recommended parameters for images:

*   `:class: with-shadow`

Alternatively, a border can be defined:

*   `:class: with-border`


Optional parameters for images:

*   `:alt:` : alt text
*   `:target:` link target
*   `:width:` : width of image, use for example px (for example `:width: 100px`
*   `:scale:` : scale images, for example `:scale: 65`

Additional parameters can be found on the docutils page `reStructuredText Directives
<http://docutils.sourceforge.net/0.4/docs/ref/rst/directives.html#image>`__

Examples
========

..  index:: reST; Image scaling

Example 1: Scaled image with shadow and link target
---------------------------------------------------

..  image:: /Images/a4.jpg
    :alt: Left floating image
    :target: https://typo3.org
    :class: with-shadow
    :scale: 50

..  code-block:: rest
    :linenos:

    ..  image:: /Images/a4.jpg
        :alt: some image
        :target: https://typo3.org
        :class: with-shadow
        :scale: 50


**line 1:**
    image directive with path

**line 2:**
    alt-Text

**line 3:**
    link target

**line 4:**
    use a shadow on the image


..  index::
    reST directives; figure
    reST; Image caption

Example 2: Image with caption
-----------------------------

..  figure:: /Images/a4.jpg
    :alt: Left floating image
    :target: https://typo3.org
    :class: with-shadow
    :width: 100px

    This is the image caption

..  code-block:: rest
    :linenos:

        ..  figure:: /Images/a4.jpg
            :alt: some image
            :target: https://typo3.org
            :class: with-shadow
            :width: 100px

            This is the image caption

**line 5:**
    width of image


Example 3: Image with fixed width
---------------------------------

..  image:: /Images/a4.jpg
    :alt: Left floating image
    :target: https://typo3.org
    :class: with-shadow
    :width: 100px


..  code-block:: rest
    :linenos:

    ..  image:: /Images/a4.jpg
        :alt: some image
        :target: https://typo3.org
        :class: with-shadow
        :width: 100px

**line 5:**
    width of image


..  index:: reST; Image floating


Example 4: Image with float-left
--------------------------------

..  image:: /Images/a4.jpg
    :alt: Left floating image
    :target: https://typo3.org
    :class: with-shadow float-left

Some text ...  (will be displayed on the right of the image).

..  rst-class::  clear-both


..  code-block:: rest

    ..  image:: /Images/a4.jpg
        :alt: Left floating image
        :target: https://typo3.org
        :class: with-shadow float-left

    Some text ...  (will be displayed on the right of the image)

    ..  rst-class::  clear-both


..  hint::

    When using float-left, make sure the text is suitable for
    wrapping around images. Here, we use `..  rst-class:: clear-both`
    to reset the floating and start on the left again.


Example 5: Image with border
----------------------------

..  image:: /Images/a4.jpg
    :class: with-border
