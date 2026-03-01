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
*   `:zoom:` : enable zoom functionality (see :ref:`image-zoom`)
*   `:class:` : CSS classes, for example `with-shadow`, `with-border`, `float-left`,
    `float-right` (see :ref:`image-float-alignment`)
*   `:align:` : alignment/float for figures: `left`, `right`, `center`
    (see :ref:`image-float-alignment`)

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
    :width: 100px
    :zoom: lightbox

    This is the image caption

..  code-block:: rst
    :linenos:

        ..  figure:: /_Images/a4.jpg
            :alt: some image
            :width: 100px
            :zoom: lightbox

            This is the image caption
