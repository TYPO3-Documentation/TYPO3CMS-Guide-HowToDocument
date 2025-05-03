:navigation-title: Basic principles

..  include:: /Includes.rst.txt
..  _basic-principles:
..  _whats-typo3-documentation:
..  _common-characteristics-typo3-docs:
..  _about:
..  _credits:

=================
Basic principles
=================

TYPO3 documentation is written in **reStructuredText (reST)** and rendered to
HTML using a shared toolchain. Most documentation is hosted on
https://docs.typo3.org and follows a common structure and style.

..  contents:: Table of content

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

..  include:: /_Includes/_LocalRendering.rst.txt

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

We provide a Docker command to get started with documenting an extension:

..  include:: /_Includes/_InitCommand.rst.txt

See also `How to document an extension <https://docs.typo3.org/permalink/h2document:write-doc-extensions-intro>`_.

.. _how-to-get-help:
.. _slack:
.. _help:
.. _contact-us:
.. _get-help-on-writing-docs:

Help and support
================

Need help with TYPO3 documentation? Join the TYPO3 Slack workspace and post your
question in the **#typo3-documentation** channel.

To register, visit:
https://my.typo3.org/index.php?id=35

For general TYPO3 support, see https://typo3.org/help/.

You can also contact the Documentation Team by email:
`documentation@typo3.org <mailto:documentation@typo3.org>`__
