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

..  literalinclude:: /_CodeSnippets/_Figure.rst.txt
    :caption: Documentation/MyDocs.rst

More optional parameters for embedding images into ReST: :ref:`Images <h2document:images>`.

..  _guidelines-for-images-formats:

Image formats
=============

*   It is recommended to use PNG for bitmaps (for example screenshots, photographs)
    and SVG for vector graphics images. In any case, you can use :file:`.png`.

..  _guidelines-for-images-screenshot:
..  _automatic-screenshots:

Guidelines for screenshots
==========================

..  note::
    You can use the `example screenshot project <https://docs.typo3.org/permalink/h2document:screenshot-project>`_.
    It already follows most of the rules stated below. The general automatic
    screenshot tool was dropped after TYPO3 v11, as it proved too complicated
    to maintain. The TCA Reference takes its screenshots automatically, see
    `Automatic screenshots in the TCA Reference <https://docs.typo3.org/permalink/h2document:automatic-screenshots-tca-reference>`_.

*   Before adding a screenshot consider if one is necessary. Each new screenshot
    requires maintenance.
*   Use a Composer-based installation of the latest LTS release, or dev-main.
*   Turn the backend into light mode and modern look.
*   Unless you want to demonstrate features of certain system extensions use
    a default installation as described in Getting Started:
    :ref:`Installing TYPO3 with DDEV <t3start:installation-ddev-tutorial>`.
*   If you need an example site package use `t3docs/site-package`.
*   If you need example data use :composer:`t3docs/site-package-data`.
*   As personalized usernames are considered best practice always use username
    "j.doe".
*   Do not install third party extensions unless what you want to demonstrate
    requires one. If possible use one of the extensions from vendor `typo3` or
    `t3docs`.
*   Use PNG or AVIF format (:file:`.png` or :file:`.avif` file ending).
*   If you take a screenshot of a full page it should have 1400 x 1050 px.
*   Size the browser window to at least 1440 x 1050 px before taking backend
    screenshots — narrow viewports collapse the module menu and truncate
    table columns. Capture slightly wider than the 1400 px target, then crop.
*   The content of a backend module is rendered inside an iframe that scrolls
    internally. A "full page" screenshot (for example Playwright's
    `fullPage: true`) captures only the outer frame and cuts off the lower
    part of the module — to capture a tall module view, increase the height
    of the viewport itself and take a normal screenshot.
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

..  _automatic-screenshots-tca-reference:

Automatic screenshots in the TCA Reference
==========================================

The TCA Reference takes its screenshots automatically. :bash:`make screenshots`
sets up a TYPO3 instance with the example extension of the manual and the
records from :file:`Build/Screenshots/create-records.php`. It then takes the
screenshots with Playwright and saves them to
:path:`Documentation/Images/Conference/`.

Each version branch takes its own screenshots, so they show the TYPO3 version
that the branch documents: `main` uses TYPO3 15, and `14.3` uses TYPO3 14.3.

The screenshots are defined in :file:`Build/Screenshots/screenshots.mjs`. To
take only some of them, pass their names:

..  code-block:: bash

    Build/Scripts/runTests.sh -s screenshots <Name>

The example extension in :path:`Documentation/CodeSnippets/my_extension/`
exists only for the code snippets and screenshots of the manual. Readers are
never told to install it.

The section "The example extension and its screenshots" in the
`AGENTS.md of the TCA Reference <https://github.com/TYPO3-Documentation/TYPO3CMS-Reference-TCA/blob/main/AGENTS.md>`_
describes how to add a screenshot. After a full run, check the other images
as well. Many of them change by a few pixels, and only real changes are
committed.

The other manuals still take their screenshots by hand.

..  _guidelines-for-images-screenshot-with-grafics:

Guidelines for screenshots with graphics elements
=================================================

You will often see a screenshot where additional graphic elements have been added in the
documentation. These additional graphic elements may be boxes, numbers or arrows.

*   Use sufficient contrast to ensure additional graphic elements are visible
    across devices and for as many readers as possible, even if they have
    color vision differences.
