.. include:: /Includes.rst.txt
.. index::
   ! Images
   Screenshots
   see: Screenshots; Images
.. _guidelines-for-images:

==============================
Guidelines for creating images
==============================

Read here how to embed an image into ReST: :ref:`Images <h2document:images>`.

For accessibility reasons always use provide an alt text.

.. _guidelines-for-images-formats:

Image formats
-------------

*  It is recommended to use PNG for bitmaps (for example screenshots, photographs)
   and SVG for vector graphics images. In any case, you can use .png.


.. _guidelines-for-images-screenshot:

Guidelines for screenshots
==========================

..  note::
    We do not have an automatic screenshot tool working with current TYPO3
    versions at the moment. The automatic screenshot tool we were working on
    never worked beyond TYPO3 11 LTS.

*   Before adding a screenshot consider if one is necessary. Each new screenshot
    requires maintenance.
*   Use a Composer-based installation of the latest LTS release, or dev-main.
*   Turn the backend into light mode and modern look.
*   Unless you want to demonstrate features of certain system extensions use
    a default installation as described in Getting Started:
    :ref:`Installing TYPO3 with DDEV <t3start:installation-ddev-tutorial>`.
*   If you need an example site package use :composer:`t3docs/site-package.
*   If you need example data use :composer:`t3docs/site-package-data`
*   As personalized usernames are considered best practice always use username
    "kasper"
*   Do not install third party extensions unless what you want to demonstrate
    requires one. If possible use one of the extensions from vendor `typo3` or
    `t3docs`.
*   use PNG format (.png file ending)
*   If you take a screenshot of a full page it should have 1400 x 1050 px
*   Use only parts of a full page when possible, the flatter the screenshot the
    less room it takes.
*   When reviewing screenshots take into consideration that taking screenshots
    is a lot of effort.

.. _guidelines-for-images-screenshot-with-grafics:

Guidelines for screenshots with graphics elements
=================================================

You will often see a screenshot where additional graphic elements have been added in the
documentation. These additional graphic elements may be boxes, numbers or arrows.

*   Use sufficient contrast to ensure additional graphic elements are visible
    across devices and for as many readers as possible, even if the do not see
    a difference between red and green.
