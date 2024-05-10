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


..  _fluid-viewhelper-reference-generation-schema:

The Fluid ViewHelper schema generator
=====================================

The PHP files defining the ViewHelpers are transferred into :file:`schema.xsd`
files. The package `fluid-schema-generator <https://github.com/TYPO3/Fluid.SchemaGenerator>`__
is responsible for this step, automatically executed via triggered GitHub actions. If information is missing in the
:file:`schema.xsd`, adjustments need to be made in the PHP files. :file:`schema.xsd` files are considered "read-only" due to their auto-generated nature. The information from the
:file:`schema.xsd` files can, if configured through plugins, also used by IDEs for context sensitive help in
editors etc.

You can generate the :file:`schema.xsd` files yourself for local testing, like this:

..  code-block:: bash

    git clone git@github.com:typo3/typo3.git core
    cd core
    composer require -o -n --no-progress typo3/fluid-schema-generator
    mkdir -p ../schemas/typo3fluid/fluid/latest
    ./bin/generateschema TYPO3Fluid\\\Fluid > ../schemas/typo3fluid/fluid/latest/schema.xsd
    mkdir -p ../schemas/typo3/core/latest
    ./bin/generateschema TYPO3\\\CMS\\\Core > ../schemas/typo3/core/latest/schema.xsd
    mkdir -p ../schemas/typo3/fluid/latest
    ./bin/generateschema TYPO3\\\CMS\\\Fluid > ../schemas/typo3/fluid/latest/schema.xsd
    mkdir -p ../schemas/typo3/backend/latest
    ./bin/generateschema TYPO3\\\CMS\\\Backend > ../schemas/typo3/backend/latest/schema.xsd

The composer step will automatically require the Fluid Rendering Engine in the version
used by the Core version you fetched via GIT (by default, `main`).

..  _fluid-viewhelper-reference-generation-rst:

Generation of the reStructuredText files
=========================================

The :abbr:`rst (reStructuredText)` files get generated from the
:file:`schema.xsd` files (See section
:ref:`fluid-viewhelper-reference-generation-schema`) with the help of the
following tool:
`Fluid ViewHelper Documentation Generator <https://github.com/TYPO3-Documentation/fluid-documentation-generator>`.

Please note that the TYPO3 Core initially uses `reStructuredText` formatting
inside the phpDoc comments already,  and this is passed on to the :file:`schema.xsd`
files with exactly that formatting.
IDEs may want to interpret  these schemas with expected HTML or MarkDown syntax,
so you may see raw `reStructuredText` output in this case.
The generated Documentation for `docs.typo3.org` takes care of
transforming the generated  :file:`.rst` files to HTML, by utilizing the
https://github.com/TYPO3-Documentation/render-guides project.


If any of the ViewHelper source code documentation is only contained in the :file:`schema.xsd` files but
not the generated standalone :file:`.rst` files, a bug in that generator may exist and needs adressing.

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
