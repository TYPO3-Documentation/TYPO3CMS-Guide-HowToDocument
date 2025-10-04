..  include:: /Includes.rst.txt
..  index::
    ! Images
    Screenshots
    see: Screenshots; Images
..  _guidelines-for-images:

==============================
Guidelines for creating images
==============================

For accessibility reasons **always** provide an alt text:

..  literalinclude:: /_CodeSnippets/_Figure.rts.txt

More option for embedding images into ReST: :ref:`Images <h2document:images>`.

..  _guidelines-for-images-formats:

Image formats
=============

*  It is recommended to use PNG for bitmaps (for example screenshots, photographs)
   and SVG for vector graphics images. In any case, you can use .png.

..  _guidelines-for-images-screenshot:
..  _automatic-screenshots:

Guidelines for screenshots
==========================

..  note::
    You can use the `The example screenshot project <https://docs.typo3.org/permalink/h2document:screenshot-project>`_.
    It already follows most of the rules stated below. There has been no automatic
    screenshot tool since TYPO3 v11 as it proved to be to complicated to maintain.

*   Before adding a screenshot consider if one is necessary. Each new screenshot
    requires maintenance.
*   Use a Composer-based installation of the latest LTS release, or dev-main.
*   Turn the backend into light mode and modern look.
*   Unless you want to demonstrate features of certain system extensions use
    a default installation as described in Getting Started:
    :ref:`Installing TYPO3 with DDEV <t3start:installation-ddev-tutorial>`.
*   If you need an example site package use `t3docs/site-package`.
*   If you need example data use :composer:`t3docs/site-package-data`
*   As personalized usernames are considered best practice always use username
    "j.doe"
*   Do not install third party extensions unless what you want to demonstrate
    requires one. If possible use one of the extensions from vendor `typo3` or
    `t3docs`.
*   use PNG format (.png file ending)
*   If you take a screenshot of a full page it should have 1400 x 1050 px
*   Use only parts of a full page when possible, the flatter the screenshot the
    less room it takes.
*   When reviewing screenshots take into consideration that taking screenshots
    is a lot of effort.

..  _screenshot-project:

The example screenshot project
==============================

We have a ready to use TYPO3 project that you can run in GitHub Codespaces
or locally on DDEV to make screenshots:

`Ready to use Project for screenshots <https://github.com/TYPO3-Documentation/site-introduction/blob/main/README.md>`_

..  _guidelines-for-images-screenshot-with-grafics:

Guidelines for screenshots with graphics elements
=================================================

You will often see a screenshot where additional graphic elements have been added in the
documentation. These additional graphic elements may be boxes, numbers or arrows.

*   Use sufficient contrast to ensure additional graphic elements are visible
    across devices and for as many readers as possible, even if they have
    color vision differences.
