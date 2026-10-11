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

More optional parameters for embedding images into reST: :ref:`Images <h2document:images>`.

..  _guidelines-for-images-alt-text:

What the alt text must contain
==============================

The alt text says what the image shows. Name the messages, labels, and values
that the text around the image relies on. A reader who cannot see the image
depends on the alt text. So does an agent that would otherwise have to load
the image to read it.

A description of the kind of image is not enough:

..  code-block:: rst
    :caption: Wrong: the alt text names the kind of image only

    ..  figure:: /Images/ErrorPage.png
        :alt: Error page of a site without TypoScript

Write the text that the image shows instead:

..  code-block:: rst
    :caption: Correct: the alt text holds the message of the image

    ..  figure:: /Images/ErrorPage.png
        :alt: Error page "500 Internal Server Error" with the reason "No site
            configuration or TypoScript template record found!"

The same applies to the output of code:

..  code-block:: rst
    :caption: Wrong and correct alt text for a debug output

    :alt: Output of a SplitProcessor, including debug output

    :alt: Dump of the variable urlParts with 10 parts: "https:", an empty
        string, "docs.typo3.org", and the output that shows the parts
        separated by slashes

..  _guidelines-for-images-alt-text-length:

Long alt texts
--------------

Never shorten an alt text to keep a line below 80 characters. Wrap it
instead: continue the text on the next line, indented below :rst:`:alt:`.
The rendering joins the lines into one alt text, as in the examples above.

..  _guidelines-for-images-alt-text-update:

Update the alt text with the image
----------------------------------

When you replace a screenshot, by hand or with a screenshot tool, compare the
new image with its alt text. If the text in the image changed, such as a
message, a menu item, a label, or the number of entries, update the alt text
as well.

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
