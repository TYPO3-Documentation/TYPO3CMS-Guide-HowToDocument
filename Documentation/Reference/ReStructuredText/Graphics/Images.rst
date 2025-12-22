:navigation-title: Images

..  include:: /Includes.rst.txt
..  index:: pair: reST; Images
..  _how-to-document-images:
..  _images:

==================================
Using images in ReST documentation
==================================

You can use the `The example screenshot project <https://docs.typo3.org/permalink/h2document:screenshot-project>`_.
It already follows most of the rules stated below. There has been no automatic
screenshot tool since TYPO3 v11 as it proved to be to complicated to maintain.

..  attention::

    For official and Core manuals please follow the
    `Guidelines for creating images <https://docs.typo3.org/permalink/h2document:guidelines-for-images>`_.

..  _rest-images:

Images and figures in Rest
==========================

We recommend to use the `..  figure::` directive. It works just like
`..  image::` save that you can add a descriptive text as content.

Always use the parameter `:alt:` to add a descriptive text for visually impaired
and search engine / artificial intelligence bots scanning our docs.

Example:

..  literalinclude:: /_CodeSnippets/_Figure.rts.txt

Optional parameters for images and figures:

*   `:target:` link target
*   `:width:` : width of image, use for example px (for example `:width: 100px`
*   `:scale:` : scale images, for example `:scale: 65`

Additional parameters can be found on the docutils page `reStructuredText Directives
<http://docutils.sourceforge.net/0.4/docs/ref/rst/directives.html#image>`__

..  _image-scaled:

Example 1: Scaled image with shadow and link target
===================================================

..  image:: /_Images/a4.jpg
    :alt: Left floating image
    :target: https://typo3.org
    :class: with-shadow
    :scale: 50

..  code-block:: rst
    :linenos:

    ..  figure:: /_Images/a4.jpg
        :alt: some image
        :target: https://typo3.org
        :class: with-shadow
        :scale: 50

..  _image-caption:

Example 2: Image with caption and fixed width
=============================================

..  figure:: /_Images/a4.jpg
    :alt: Left floating image
    :target: https://typo3.org
    :width: 100px

    This is the image caption

..  code-block:: rst
    :linenos:

        ..  figure:: /_Images/a4.jpg
            :alt: some image
            :target: https://typo3.org
            :width: 100px

            This is the image caption

..  _image-zoom:

Image zoom and lightbox features
=================================

The TYPO3 documentation theme provides built-in image zoom and lightbox
features to enhance the viewing experience for images and figures. These
features allow readers to view images in greater detail without leaving
the documentation page.

Available zoom modes
--------------------

The zoom functionality is controlled by adding a CSS class to your figure
or image directive. The following zoom modes are available:

..  rst-class:: dl-parameters

:class:`zoom-lightbox` (default)
    Click to open the image in a full-screen overlay dialog. The lightbox
    provides a dark backdrop and centers the image. Click outside the image
    or press ESC to close.

    **Use case**: Screenshots, diagrams, and any image that benefits from
    full-screen viewing.

:class:`zoom-gallery`
    Click to open the image in a gallery viewer with mouse wheel zoom
    capabilities and navigation controls. Ideal for multiple related images.

    **Use case**: Series of screenshots, step-by-step tutorials, or image
    galleries.

:class:`zoom-inline`
    Enables scroll wheel zoom directly on the image without opening an
    overlay. The image zooms in place within the documentation.

    **Use case**: Detailed diagrams or technical drawings that need frequent
    zoom inspection.

:class:`zoom-lens`
    A magnifier lens follows the cursor when hovering over the image,
    showing a zoomed view of the area under the cursor.

    **Use case**: High-resolution images with fine details, such as UI
    mockups or detailed screenshots.

:class:`zoom-css-only`
    A lightweight, JavaScript-free zoom that enlarges the image on hover
    using only CSS. Provides basic zoom functionality without requiring
    JavaScript.

    **Use case**: Simple zoom needs, or when JavaScript-free fallback is
    required.

Usage examples
--------------

Example 3: Lightbox zoom (default)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

..  figure:: /_Images/a4.jpg
    :alt: Example screenshot
    :class: zoom-lightbox

    Click to open in lightbox. This is the recommended mode for most images.

..  code-block:: rst
    :linenos:

    ..  figure:: /_Images/a4.jpg
        :alt: Example screenshot
        :class: zoom-lightbox

        Click to open in lightbox.

Example 4: Gallery mode with zoom
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

..  code-block:: rst
    :linenos:

    ..  figure:: /_Images/screenshot.png
        :alt: Configuration screen
        :class: zoom-gallery
        :width: 600px

        Opens in gallery mode with zoom controls and navigation.

Example 5: Inline scroll-wheel zoom
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

..  code-block:: rst
    :linenos:

    ..  figure:: /_Images/diagram.png
        :alt: Architecture diagram
        :class: zoom-inline

        Use scroll wheel to zoom in/out directly on this image.

Example 6: Magnifier lens
~~~~~~~~~~~~~~~~~~~~~~~~~~

..  code-block:: rst
    :linenos:

    ..  figure:: /_Images/detailed-ui.png
        :alt: User interface mockup
        :class: zoom-lens

        Hover over the image to see a magnified view.

Accessibility considerations
-----------------------------

All zoom modes are designed with accessibility in mind:

Keyboard navigation
~~~~~~~~~~~~~~~~~~~

*   **Lightbox and Gallery modes**: Full keyboard support

    *   :kbd:`Tab` - Navigate between controls
    *   :kbd:`Enter` or :kbd:`Space` - Open lightbox/gallery
    *   :kbd:`ESC` - Close lightbox/gallery
    *   :kbd:`Arrow keys` - Navigate between images (gallery mode)
    *   :kbd:`+` / :kbd:`-` - Zoom in/out (gallery mode)

*   **Inline zoom mode**: Full keyboard support

    *   :kbd:`Tab` - Focus the image
    *   :kbd:`+` / :kbd:`-` - Zoom in/out
    *   :kbd:`Arrow keys` - Pan when zoomed
    *   :kbd:`ESC` or :kbd:`0` - Reset zoom

*   **Lens mode**: Keyboard activation supported

    *   :kbd:`Tab` - Focus the image
    *   :kbd:`Enter` or :kbd:`Space` - Toggle lens on/off
    *   :kbd:`Arrow keys` - Move lens position
    *   :kbd:`ESC` - Deactivate lens

Screen reader support
~~~~~~~~~~~~~~~~~~~~~~

All zoom modes maintain proper ARIA attributes and provide descriptive
labels for assistive technologies. Always use the `:alt:` parameter to
provide descriptive alternative text for images.

JavaScript-free fallback
~~~~~~~~~~~~~~~~~~~~~~~~

The `zoom-css-only` mode provides a lightweight alternative that works
without JavaScript, ensuring accessibility for users with JavaScript
disabled or in restricted environments.

Best practices
--------------

*   Always include descriptive `:alt:` text for accessibility
*   Use `zoom-lightbox` as the default for most images
*   Consider `zoom-gallery` for related images that tell a story
*   Use `zoom-inline` for technical diagrams that need frequent inspection
*   Specify image width with `:width:` to prevent layout shifts
*   Test zoom functionality with keyboard navigation
