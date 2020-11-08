.. include:: /Includes.rst.txt
.. highlight:: rst

.. _how-to-start-documentation-for-ext:
.. _writing-doc-for-ext-from-scratch:
.. _doc-for-ext-from-example:

=================================================
Start Extension Documentation From Example Manual
=================================================

.. tip::

   This page is a "quick start". If you are just getting started, you
   may want to look at :ref:`writing-doc-for-ext-start` and some of
   the resources listed there first.

This description uses the example extension manual:

* `repository on GitHub <https://github.com/TYPO3-Documentation/TYPO3CMS-Example-ExtensionManual>`__
* `rendered documentation <https://docs.typo3.org/typo3cms/ExtensionManualExample/>`__

.. rst-class:: bignums-xxl

#. Clone sample extension manual

   In a temporary directory, clone the GitHub project
   `sample extension manual <https://github.com/TYPO3-Documentation/TYPO3CMS-Example-ExtensionManual>`__

   .. code-block:: bash

      git clone https://github.com/TYPO3-Documentation/TYPO3CMS-Example-ExtensionManual.git

   Move or copy the entire :file:`Documentation` directory, so that the Documentation
   directory is a direct subdirectory of the extension, e.g.

   .. code-block:: bash

      cp -r TYPO3CMS-Example-ExtensionManual/Documentation <extension-directory>/

#. Add or modify additional files

   * (*required*) Make sure :ref:`composer-json` is up to date.
   * (*required*) Make sure :ref:`settings-cfg` is up to date.
   * (*recommended*) :ref:`gitignore-in-filenames` is useful, in order to
     prevent accidentally commiting the generated documentation in
     :file:`Documentation-GENERATED-temp` to the Git repository.
   * (*recommended*) :ref:`editorconfig-in-filenames` is useful, so the
     recommended :ref:`Coding Guidelines <format-rest-cgl>` will be used within
     editor or IDE. :ref:`phpstorm-editorconfig` contains further information
     for PhpStorm.

   .. code-block:: bash

      # cp .gitignore (make sure you don't accidentally overwrite existing one though!)
      cp -n TYPO3CMS-Example-ExtensionManual/.gitignore <extension-directory>/.gitignore
      # cp .editorconfig (make sure you don't accidentally overwrite existing one though!)
      cp -n TYPO3CMS-Example-ExtensionManual/.editorconfig <extension-directory>/.editorconfig

   You may also want to consider adding :ref:`CONTRIBUTING.rst <contributing-rst>`
   and :ref:`README.rst <readme-rst>` to your extension,
   if you plan to host your extension on a public repository.

#. Edit documentation

   Start editing away. Use the existing text to guide you. Look at other
   extension manuals (for example `form <https://docs.typo3.org/typo3cms/extensions/form/>`__)
   for inspiration. (You can find a link to the repository in the footer.)

#. Fill out composer.json

   Be sure to fill out :file:`composer.json` correctly as described in :ref:`composer-json`.

#. Fill out Settings.cfg

   Be sure to fill out :file:`Settings.cfg` correctly as described in :ref:`settings-cfg`.

#. Render documentation

   Before publishing changes, make sure the documentation is rendered correctly.

   Look at :ref:`render-documenation-with-docker` for a quick start, how to
   render locally.

   There is also a :ref:`draft branch <migrate-branches>` that allows to render
   a preview at docs.typo3.org.

#. Publish when done

   If you are working on your own extension, :ref:`make it publicly available
   <t3coreapi:publish-extension>`

   In order to trigger documentation rendering on the documentation server you have to
   add a webhook, see :ref:`webhook`.

.. tip::

   Think about hosting your extension repository on GitHub, Bitbucket or GitLab.
   That way others can report issues and assist you by creating change requests
   for the documentation and code!

