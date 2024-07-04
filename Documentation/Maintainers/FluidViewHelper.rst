.. include:: /Includes.rst.txt
..  _fluid-viewhelper-reference-generation:

=====================================
Fluid ViewHelper reference generation
=====================================

The :ref:`Fluid ViewHelper Reference <t3viewhelper:start>` gets automatically
updated by changes to the according ViewHelper classes in the
`TYPO3 Core <https://github.com/TYPO3/typo3>`__ and
the package `Fluid Rendering Engine <https://github.com/TYPO3/Fluid>`__.

The generated documentation specifically depends on the phpDoc-style inline
comments on top of the ViewHelper classes as well as the configured arguments in their
php:`initializeArguments()` method.

Changes in wording or arguments thus need to be made inside the relevant files of these two repositories. For contributions
to the TYPO3 Core, follow the
:ref:`TYPO3 Contribution Guide - Core Development <t3contribute:recommended-reading>`.


..  _fluid-viewhelper-reference-generation-rst:

Generation of the reStructuredText files and JSON files
=======================================================

The `Fluid ViewHelper Documentation Generator <https://github.com/TYPO3-Documentation/fluid-documentation-generator>`
is responsible for creating both a directory structure of :abbr:`rst (reStructuredText)` files and
a json file for each documented Fluid namespace. The Fluid namespaces to be documented are configured
in JSON files in this repository, which also support combining multiple namespaces into one
(because `f:*` in TYPO3 combines both `EXT:fluid` and Fluid Standalone ViewHelpers).

..  _fluid-viewhelper-reference-generation-html:

Rendering the ViewHelper reference to HTML
==========================================

The :abbr:`rst (reStructuredText)` files generated in step
:ref:`fluid-viewhelper-reference-generation-rst` will be saved by the
:ref:`GitHub action <fluid-viewhelper-reference-generation-github-action>` into
the repository `Fluid ViewHelper Reference <https://github.com/TYPO3-Documentation/TYPO3CMS-Reference-ViewHelper>`.

In this repository all files not overridden by the
`Fluid ViewHelper Documentation Generator <https://github.com/TYPO3-Documentation/fluid-documentation-generator>`
are maintained, Including the start page :file:`Index.rst` and the
:ref:`guides.xml <settings-guides-xml>`. This repository is then rendered by
the standard rendering process.

..  _fluid-viewhelper-reference-generation-github-action:

GitHub action "Fluid ViewHelper Documentation"
==============================================

All processes described above are combined for automatic execution as a GitHub
action in the repository `t3docs-ci-deploy <https://github.com/TYPO3-Documentation/t3docs-ci-deploy>`__.
It is triggered automatically once a day, or can be executed manually through the GitHub UI by the TYPO3 Documentation team.

Maintainers needs to occasionally watch for failed or stuck `Workflow runs <https://github.com/TYPO3-Documentation/t3docs-ci-deploy/actions>`__.
