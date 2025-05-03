:navigation-title: Basic principles

..  include:: /Includes.rst.txt
..  _basic-principles:
..  _whats-typo3-documentation:
..  _common-characteristics-typo3-docs:

=================
Basic principles
=================

TYPO3 documentation is written in **reStructuredText (reST)** and rendered to
HTML using a shared toolchain. Most documentation is hosted on
https://docs.typo3.org and follows a common structure and style.

..  _documentation-types:
..  _doc-type-tutorial:
..  _doc-type-guide:
..  _doc-type-reference:
..  _doc-type-official:
..  _doc-type-community:
..  _overview-of-types:
..  _about-typo3-extensions:

Types of documentation
======================

Documentation may include:

*   Official manuals (e.g. :ref:`t3coreapi:start`)
*   System extension manuals
*   Core changelog entries
*   Third-party extension manuals

..  _whats-rendering:

Rendering
=========

Rendering converts `.rst` source files into styled HTML output. You can preview
docs locally using the official Docker container:

..  _contribution-matrix:

Contributing to official documentation
======================================

Everyone is welcome to contribute to TYPO3’s official documentation.

Most manuals are hosted on GitHub. You can suggest changes directly by clicking
:guilabel:`Edit on GitHub` on any page.

For larger contributions or local editing, see the full guide at
:ref:`docs-contribute`.

..  _doc-type-extension-manual:

Documenting your own extension
==============================

To document your TYPO3 extension, create a :file:`Documentation` folder in your
extension and add `.rst` files following the standard structure.

If your extension is hosted on GitHub and correctly configured, contributors
can use the :guilabel:`Edit on GitHub` button to propose changes.

See :ref:`how-to-start-docs-extension` to get started with the recommended setup.
