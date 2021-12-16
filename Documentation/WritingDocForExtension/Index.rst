.. include:: /Includes.rst.txt
.. highlight:: rst
.. index:: Documentation; Extension
.. _writing-doc-for-ext-start:
.. _how-to-start-docs-extension:
.. _extension-documentation-files:
.. _write-doc-extensions-intro:

============================
How to document an extension
============================

This chapter explains how to write documentation for a new extension.

This guide uses the `example extension manual <https://github.com/TYPO3-Documentation/TYPO3CMS-Example-ExtensionManual>`__
as a template for starting out. It contains a working navigation panel, a range of example content and adheres to the guidelines
laid out in the :ref:`general-conventions` chapter.

Rendering the documentation locally
-----------------------------------

Docker is required to run the rendering toolchain locally. By rendering the documentation this way, proofreading and
checking for typos and testing links can be carried out before the documentation is committed. The
:ref:`render-documenation-with-docker` has more information on how this toolchain is set up and configured.

Using the documentation-draft branch to preview changes
-------------------------------------------------------

Alternatively, a `documentation-draft` branch can be created in the documentation repository.
Once committed, this will render the documentation and make it available publicly, but it will only be visible
when the "draft" drop-down is selected when viewing the rendered documentation. Documentation under the draft branch will not be indexed
by search engines. Visit the :ref:`supported-branches` section for more information.

Creating extension documentation using the sample manual
--------------------------------------------------------

.. rst-class:: bignums-xxl

#. Clone the sample extension manual

   In a temporary directory, clone the GitHub project
   `sample extension manual <https://github.com/TYPO3-Documentation/TYPO3CMS-Example-ExtensionManual>`__

   .. code-block:: bash

      git clone https://github.com/TYPO3-Documentation/TYPO3CMS-Example-ExtensionManual.git

   Copy the entire :file:`Documentation` directory, so that it
   is a subdirectory located within your extension, for example:

   .. code-block:: bash

      cp -r TYPO3CMS-Example-ExtensionManual/Documentation <my-extension-directory>/

#. Add or modify additional files

   *  Make sure :ref:`composer-json` is up to date. (*required*)
   *  Make sure :ref:`settings-cfg` is up to date. (*required*)
   *  :ref:`gitignore-in-filenames` is useful, in order to
      prevent accidentally committing the generated documentation in
      :file:`Documentation-GENERATED-temp` to the Git repository. (*recommended*)
   *  :ref:`editorconfig-in-filenames` is useful, so the
      recommended :ref:`Coding Guidelines <format-rest-cgl>` will be used within
      an editor or IDE. :ref:`phpstorm-editorconfig` contains further information
      for PhpStorm users. (*recommended*)

   .. code-block:: bash

      # cp .gitignore (make sure you don't accidentally overwrite existing one though!)
      cp -n TYPO3CMS-Example-ExtensionManual/.gitignore <my-extension-directory>/.gitignore
      # cp .editorconfig (make sure you don't accidentally overwrite existing one though!)
      cp -n TYPO3CMS-Example-ExtensionManual/.editorconfig <my-extension-directory>/.editorconfig

   If you plan to host your extension on a public repository, consider
   adding a :ref:`CONTRIBUTING.rst <contributing-rst>`
   and :ref:`README.rst <readme-rst>` to help guide any future
   contributors.


#. Start adding documentation

   Now it's time to start adding content. Reviewing existing guides can help you structure your own documentation.
   The `news extension <https://docs.typo3.org/p/georgringer/news/main/en-us/Index.html>`__ is a strong example of how extension
   documentation should be written and structured.

#. Populate composer.json

   Complete the :file:`composer.json` as described in :ref:`composer-json`.

#. Populate Settings.cfg

   Complete the :file:`Settings.cfg` as described in :ref:`settings-cfg`.

#. Render documentation

   Before publishing changes, make sure the documentation is rendered correctly, either
   by :ref:`rendering it locally <render-documenation-with-docker>` or by using the :ref:`draft branch <migrate-branches>`
   to preview the changes.

#. Publish when ready

   The documentation needs to be :ref:`made publicly available <t3coreapi:publish-extension>`.

   In order to trigger the documentation rendering process, a :ref:`webhook needs to be added <webhook>`.

.. tip::

   Consider hosting your extension repository on either GitHub, Bitbucket or GitLab.
   That way others can report issues and assist you by creating change requests to help
   improve both the extensions documentation and the code.

.. toctree::
   :maxdepth: 1
   :hidden:

   Migrate
   Webhook
   ReregisterVersions
   FAQ
   ContributeToSystemExtension
   ContributeToThirdPartyExtension
