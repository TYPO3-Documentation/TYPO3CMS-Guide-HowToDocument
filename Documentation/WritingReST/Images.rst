.. include:: /Includes.rst.txt
.. highlight:: rst


.. _how-to-document-images:
.. _rest-images:
.. _images:

======
Images
======


How to Use Images
=================

Use the `.. image::` directive with additional parameters.

Use `.. figure::` if you want to add a caption to your image.
You can use the same parameters in figure that are defined for image.

The
additional parameters must be indented one level (add 3 spaces to indent).

Recommended parameters for images:

*  `:class: with-shadow`

Alternatively, a border can be defined:

*  `:class: with-border`


Optional parameters for images:

*  `:alt:` : alt text
*  `:target:` link target
*  `:width:` : width of image, use for example px (e.g. `:width: 100px`
*  `:scale:` : scale images, e.g. `:scale: 65`

Additional parameters can be found on the docutils page `reStructuredText Directives
<http://docutils.sourceforge.net/0.4/docs/ref/rst/directives.html#image>`__

Examples
========


Example 1: Scaled Image With Shadow and Link Target
---------------------------------------------------

.. image:: ../images/a4.jpg
   :alt: Left floating image
   :target: https://typo3.org
   :class: with-shadow
   :scale: 50

.. code-block:: rest
   :linenos:

   .. image:: ../images/a4.jpg
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

Example 2: Image With Caption
-----------------------------

.. figure:: ../images/a4.jpg
   :alt: Left floating image
   :target: https://typo3.org
   :class: with-shadow
   :width: 100px

   This is the image caption

.. code-block:: rest
   :linenos:

      .. figure:: ../images/a4.jpg
         :alt: some image
         :target: https://typo3.org
         :class: with-shadow
         :width: 100px

         This is the image caption

**line 5:**
   width of image


Example 3: Image With Fixed Width
---------------------------------

.. image:: ../images/a4.jpg
   :alt: Left floating image
   :target: https://typo3.org
   :class: with-shadow
   :width: 100px


.. code-block:: rest
   :linenos:

   .. image:: ../images/a4.jpg
      :alt: some image
      :target: https://typo3.org
      :class: with-shadow
      :width: 100px

**line 5:**
   width of image




Example 4: Image with float-left
--------------------------------

.. image:: ../images/a4.jpg
   :alt: Left floating image
   :target: https://typo3.org
   :class: with-shadow float-left

Some text ... (will be displayed on the right of the image).

.. rst-class::  clear-both


.. code-block:: rest

   .. image:: ../images/a4.jpg
      :alt: Left floating image
      :target: https://typo3.org
      :class: with-shadow float-left

   Some text ... (will be displayed on the right of the image)

   .. rst-class::  clear-both


.. hint::

   When using float-left, make sure the text is suitable for
   wrapping around images. Here, we use `.. rst-class:: clear-both`
   to reset the floating and start on the left again.

Example 5: Image with border
--------------------------------

.. image:: ../images/a4.jpg
   :class: with-border
