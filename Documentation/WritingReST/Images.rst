.. include:: ../Includes.txt
.. highlight:: rst


.. _how-to-document-images:

======
Images
======


How to use images
=================

Use the `.. image::` directive with additional parameters. The
additional parameters must be indented one level (add 3 spaces to indent).

Some parameters for images:

* `:alt:` : alt text
* `:target:` link target
* `:class:` css class, e.g. `with-shadow`, `with-border`


Examples
========


Example 1: Image with shadow and link target
--------------------------------------------

.. image:: ../images/a4.jpg
   :alt: Left floating image
   :target: https://typo3.org
   :class: with-shadow

.. code-block:: rest
   :linenos:

   .. image:: ../images/a4.jpg
      :alt: some image
      :target: https://typo3.org
      :class: with-shadow


**line 1:**
   image directive with path

**line 2:**
   alt-Text

**line 3:**
   link target

**line 4:**
   use a shadow on the image


Example 2: Image with fixed width
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




Example 3: Image with float-left
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
