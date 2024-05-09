.. include:: /Includes.rst.txt
..  _fluid-viewhelper-reference-generation:

=====================================
Fluid ViewHelper reference generation
=====================================

The :ref:`Fluid ViewHelper Reference <t3viewhelper:start>` gets automatically
updated by changes to the according ViewHelper classes in the
`TYPO3 Core <https://github.com/TYPO3/typo3>`__ and
the package `Fluid Rendering Engine <https://github.com/TYPO3/Fluid>`__.

Context changes need to be made in those two repositories. For contributions
to the TYPO3 Core, follow the
:ref:`TYPO3 Contribution Guide - Core Development <t3contribute:recommended-reading>`.


..  _fluid-viewhelper-reference-generation-schema:

The Fluid ViewHelper schema generator
=====================================

The PHP files defining the ViewHelpers are transferred into :file:`schema.xsd`
files. The package `fluid-schema-generator <https://github.com/TYPO3/Fluid.SchemaGenerator>`__
is responsible for this step. So if information is already missing in the
:file:`schema.xsd`, adjustments need to be made here. The information from the
:file:`schema.xsd` files is also used by IDEs for context sensitive help in
editors etc.

You can regenerate the :file:`schema.xsd` files for local testing like this:

..  code-block:: bash

    git clone git@github.com:typo3/typo3.git core
    cd core
    composer require -o -n --no-progress typo3/fluid-schema-generator "^2.1"
    mkdir -p ../schemas/typo3fluid/fluid/latest
    ./bin/generateschema TYPO3Fluid\\\Fluid > ../schemas/typo3fluid/fluid/latest/schema.xsd
    mkdir -p ../schemas/typo3/core/latest
    ./bin/generateschema TYPO3\\\CMS\\\Core > ../schemas/typo3/core/latest/schema.xsd
    mkdir -p ../schemas/typo3/fluid/latest
    ./bin/generateschema TYPO3\\\CMS\\\Fluid > ../schemas/typo3/fluid/latest/schema.xsd
    mkdir -p ../schemas/typo3/backend/latest
    ./bin/generateschema TYPO3\\\CMS\\\Backend > ../schemas/typo3/backend/latest/schema.xsd

The TYPO3 Core will automatically install Fluid Rendering Engine in the version
used by that Core version.

..  _fluid-viewhelper-reference-generation-rst:

Generation of the reSTructured text files
=========================================

The :abbr:`rst (reSTructured text)` files get generated from the
:file:`schema.xsd` files (See section
:ref:`fluid-viewhelper-reference-generation-schema`) with the help of the
following tool:
`Fluid ViewHelper Documentation Generator <https://github.com/TYPO3-Documentation/fluid-documentation-generator>`.

So if the desired information is contained in the :file:`schema.xsd` files but
not the rst sources, the problem might have to be fixed here.

..  _fluid-viewhelper-reference-generation-html:

Rendering the ViewHelper reference to HTML
==========================================

The :abbr:`rst (reSTructured text)` files generated in step
:ref:`fluid-viewhelper-reference-generation-rst` will be saved by the
:ref:`GitHub action <fluid-viewhelper-reference-generation-github-action>` into
repository `Fluid ViewHelper Reference <https://github.com/TYPO3-Documentation/TYPO3CMS-Reference-ViewHelper>`.

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

Watch for failed or stuck `Actions <https://github.com/TYPO3-Documentation/t3docs-ci-deploy/actions>`__.
