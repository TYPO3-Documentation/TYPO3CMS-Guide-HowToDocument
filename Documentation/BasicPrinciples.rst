..  include:: /Includes.rst.txt
..  highlight:: rst
..  _basic-principles:

================
Basic principles
================

..  index:: TYPO3 documentation
..  _whats-typo3-documentation:

What is the TYPO3 documentation?
================================

TYPO3 documentation may be one of the following:

*   It can be one of the `official manuals <https://docs.typo3.org/>`__
    like :ref:`t3coreapi:start`.
*   It can be the documentation of a
    :ref:`system extension <t3home:System-Extensions>`.
*   It can be the documentation of a
    `third-party extension <https://extensions.typo3.org/>`__.
*   TYPO3 documentation can also be a :ref:`Changelog <ext-core:start>`
    entry for the Core, for example documenting a breaking change or a new feature.

..  _common-characteristics-typo3-docs:

Common characteristics of TYPO3 documentation
=============================================

All of these examples have a few things in common:

*   The documentation is rendered and found on https://docs.typo3.org/
*   The documentation has a **common theme**, all pages look similar and use the same styles
*   Most of the documentation can be directly **edited by the community**. For third-party
    extensions, this depends on where and how the source code is hosted and maintained.
*   The source of the documentation is written (mostly) in reStructuredText (**reST**)

..  index:: Official TYPO3 manuals

..  _whats-typo3-documentation-official-manuals:

Official TYPO3 manuals
----------------------

The official TYPO3 manuals are hosted on GitHub. Editing the documentation
requires a GitHub account and involves creating a pull request on GitHub.

Find out more about how to contribute: :ref:`docs-contribute`.


..  index:: Core documentation
..  _whats-typo3-documentation-core-documentation:

Core documentation
------------------

The documentation for the TYPO3 Core (changelog and system extensions) is added
to the TYPO3 source code. For this reason, the workflow of changing
something in the core documentation is very similar to adding a patch
to the core.

Find out more about the :ref:`core contribution workflow <t3contribute:Start>`
in general or about :ref:`t3contribute:Adding-documentation` in the Contribution
Guide.

In addition to using the core workflow, the core documentation can also
be changed via :ref:`"Edit on GitHub" <docs-contribute-github-method>`.
In this case, a Gerrit patch is created automatically from the pull request.


..  index:: Extension manual
..  _whats-typo3-documentation-extension-manuals:

Extension manuals
------------------

The documentation for a third-party extension is maintained within the
source code of that extension.

If :ref:`configured <tip-edit-me-on-github>`, contributors
can also make changes via the :ref:`"Edit on GitHub" <docs-contribute-github-method>`.

This option is currently only available for extensions hosted on GitHub.
