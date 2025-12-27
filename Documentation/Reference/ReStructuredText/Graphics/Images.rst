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

..  versionadded:: 0.2.0
    The image zoom feature was introduced in render-guides version 0.2.0.

The TYPO3 documentation theme provides built-in image zoom and lightbox
features to enhance the viewing experience for images and figures. These
features allow readers to view images in greater detail without leaving
the documentation page.

Available zoom modes
--------------------

The zoom functionality is controlled by the `:zoom:` option on figure
and image directives. The following zoom modes are available:

..  rst-class:: dl-parameters

`lightbox`
    Click to open the image in a full-screen overlay dialog. The lightbox
    provides a dark backdrop and centers the image. Click outside the image
    or press Escape to close. A zoom indicator icon appears on the image.

    **Use case**: Screenshots, diagrams, and any image that benefits from
    full-screen viewing. This is the recommended mode for most images.

`gallery`
    Click to open the image in a gallery viewer with mouse wheel zoom
    and navigation between grouped images. Use the `:gallery:` option to
    group related images together.

    **Use case**: Series of screenshots, step-by-step tutorials, or image
    collections that should be navigable together.

`inline`
    Enables scroll wheel zoom directly on the image without opening an
    overlay. When zoomed, drag to pan. Double-click or press Escape to reset.

    **Use case**: Detailed diagrams or technical drawings that need frequent
    zoom inspection without leaving context.

`lens`
    A magnifier lens follows the cursor when hovering over the image,
    showing a zoomed view. A result panel appears beside the image with
    the magnified area.

    **Use case**: High-resolution images with fine details, such as UI
    mockups or detailed screenshots.

Directive options
-----------------

The following options are available for the figure and image directives:

..  rst-class:: dl-parameters

`:zoom:`
    The zoom mode to use. One of: `lightbox`, `gallery`, `inline`, `lens`.

`:gallery:`
    Group name for gallery mode. Images with the same gallery name can be
    navigated together. Only used with `:zoom: gallery`.

`:zoom-indicator:`
    Whether to show the zoom indicator icon. Set to `false` to hide it.
    Default is `true` (shown).

`:zoom-factor:`
    Magnification factor for lens mode. Default is `2`. Higher values
    provide stronger magnification. Only used with `:zoom: lens`.

Usage examples
--------------

Example 3: Lightbox zoom
~~~~~~~~~~~~~~~~~~~~~~~~~

..  figure:: /_Images/a4.jpg
    :alt: Example screenshot
    :zoom: lightbox
    :class: with-border with-shadow

    Click to open in lightbox. This is the recommended mode for most images.

..  code-block:: rst

    ..  figure:: /_Images/a4.jpg
        :alt: Example screenshot
        :zoom: lightbox
        :class: with-border with-shadow

        Click to open in lightbox.

Example 4: Gallery mode with grouped images
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

..  code-block:: rst

    ..  figure:: /_Images/step1.png
        :alt: Step 1
        :zoom: gallery
        :gallery: tutorial

        First step of the tutorial.

    ..  figure:: /_Images/step2.png
        :alt: Step 2
        :zoom: gallery
        :gallery: tutorial

        Second step - navigate with arrow keys.

Example 5: Inline scroll-wheel zoom
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

..  code-block:: rst

    ..  figure:: /_Images/diagram.png
        :alt: Architecture diagram
        :zoom: inline

        Use scroll wheel to zoom in/out directly on this image.

Example 6: Magnifier lens
~~~~~~~~~~~~~~~~~~~~~~~~~~

..  code-block:: rst

    ..  figure:: /_Images/detailed-ui.png
        :alt: User interface mockup
        :zoom: lens

        Hover over the image to see a magnified view.

Example 7: Hidden zoom indicator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

..  code-block:: rst

    ..  figure:: /_Images/screenshot.png
        :alt: Screenshot
        :zoom: lightbox
        :zoom-indicator: false

        Lightbox without visible indicator icon.

Accessibility considerations
-----------------------------

All zoom modes are designed with accessibility in mind:

Keyboard navigation
~~~~~~~~~~~~~~~~~~~

*   **Lightbox and Gallery modes**: Full keyboard support

    *   :kbd:`Tab` - Navigate to image and controls
    *   :kbd:`Enter` or :kbd:`Space` - Open lightbox/gallery
    *   :kbd:`Escape` - Close lightbox/gallery
    *   :kbd:`Arrow Left` / :kbd:`Arrow Right` - Navigate between images (gallery)
    *   :kbd:`+` / :kbd:`-` - Zoom in/out (gallery)

*   **Inline zoom mode**: Full keyboard support

    *   :kbd:`Tab` - Focus the image
    *   :kbd:`+` / :kbd:`-` - Zoom in/out
    *   :kbd:`Arrow keys` - Pan when zoomed
    *   :kbd:`Escape` or :kbd:`0` - Reset zoom

*   **Lens mode**: Keyboard activation supported

    *   :kbd:`Tab` - Focus the image
    *   :kbd:`Enter` or :kbd:`Space` - Toggle lens on/off
    *   :kbd:`Arrow keys` - Move lens position
    *   :kbd:`Escape` - Deactivate lens

Screen reader support
~~~~~~~~~~~~~~~~~~~~~~

All zoom modes maintain proper ARIA attributes and provide descriptive
labels for assistive technologies. Always use the `:alt:` option to
provide descriptive alternative text for images.

Reduced motion support
~~~~~~~~~~~~~~~~~~~~~~~

The zoom functionality respects the `prefers-reduced-motion` media query.
When reduced motion is preferred, transitions and animations are disabled.

Best practices
--------------

*   Always include descriptive `:alt:` text for accessibility
*   Use `lightbox` as the default for most images
*   Use `:gallery:` to group related images for navigation
*   Use `inline` for technical diagrams that need frequent inspection
*   Combine with `:class: with-border with-shadow` for better visual presentation
*   Test zoom functionality with keyboard navigation
