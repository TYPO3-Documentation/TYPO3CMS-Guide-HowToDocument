.. include:: ../Includes.txt
.. highlight:: rst

.. _how-to-start-documentation-for-ext:
.. _writing-doc-for-ext-from-scratch:

===================================================
How to Start Documentation for Your TYPO3 Extension
===================================================

This chapter describes how to create documentation for your extension
using *local editing and rendering with Docker*. It
requires Docker for running the rendering toolchain locally on
your computer to check if the documentation is rendered correctly.

This is the preferred workflow, but if you have problems with
Docker see the alternative for rendering described under :ref:`rendering-docs`.

.. tip::
   If necessary, ask for help as explained in :ref:`how-to-get-help`.

There are basically 2 ways to start, depending on whether
you used the extension_builder to start your extension:

#. :ref:`doc-for-ext-with-extension-builder`
#. :ref:`doc-for-ext-from-example`

.. _doc-for-ext-with-extension-builder:

Method 1: Start Documentation With Extension Builder
====================================================

If you used the `extension_builder <https://github.com/FriendsOfTYPO3/extension_builder>`__
to generate your extension, it will already have created a :file:`Documentation.tmpl`
directory in your extension folder. Rename this directory to :file:`Documentation`.

.. code-block:: bash

   mv Documentation.tmpl Documentation

Then continue with step 3 of the next section.


.. _doc-for-ext-from-example:

Method 2: Start Documentation from Example Manual
=================================================



.. rst-class:: bignums-xxl

1. Clone sample extension manual

   In a temporary directory, clone the GitHub project
   `sample extension manual <https://github.com/TYPO3-Documentation/TYPO3CMS-Example-ExtensionManual>`__

   .. code-block:: bash

      git clone https://github.com/TYPO3-Documentation/TYPO3CMS-Example-ExtensionManual.git

   Move or copy the entire :file:`Documentation` directory, so that the Documentation
   directory is a direct subdirectory of your extension, e.g.

   .. code-block:: bash

      cp -r TYPO3CMS-Example-ExtensionManual/Documentation <extension-directory>/

2. Add additional files

   Some files are not mandatory, but it is recommended to use them:

   * :ref:`gitignore-in-filenames` is useful, so you don't accidentally commit
     the generated documentation in :file:`Documentation-GENERATED-temp` to your Git
     repository.
   * :ref:`editorconfig-in-filenames` is useful, so you will use the
     recommended :ref:`Coding Guidelines <format-rest-cgl>`
     in your editor or IDE. You may need to set this
     up first (see :ref:`phpstorm-editorconfig` for PhpStorm).

   .. code-block:: bash

      # cp .gitignore (make sure you don't accidentally overwrite existing one though!)
      cp -n TYPO3CMS-Example-ExtensionManual/.gitignore <extension-directory>/.gitignore
      # cp .editorconfig (make sure you don't accidentally overwrite existing one though!)
      cp -n TYPO3CMS-Example-ExtensionManual/.editorconfig <extension-directory>/.editorconfig

   You may also want to consider adding :ref:`CONTRIBUTING.rst <contributing-rst>`
   and :ref:`README.rst <readme-rst>` to your extension,
   if you plan to host the repository on GitHub.

3. Edit the documentation

   Start editing away. Use the existing text to guide you. Look at other
   extension manuals (for example `sphinx <https://docs.typo3.org/typo3cms/extensions/sphinx/>`__)
   for inspiration. (Click on "Related Links" to jump to the repository or scroll to
   bottom of rendered page and click on "View page source" to see reST source.)

   Check out the section on :ref:`reST <Formatting-with-reST>` to see how to format headlines,
   code-blocks, images etc. and use the :ref:`rest-cheat-sheet` as a handy reference.

4. Fill out Settings.cfg

   Be sure to fill out :file:`Settings.cfg` correctly as described in :ref:`settings-cfg`.

5. Render the Documentation Locally

   Before you publish your changes, make sure the documentation is rendered
   correctly.

   Look at `Rendering Documentation With Docker <https://github.com/t3docs/docker-render-documentation/blob/master/README.rst>`__ for a quick start.

6. When You Are Done, Publish Your Changes

   If you are working on your own extension, `make it publicly available
   <https://extensions.typo3.org/faq/publish-an-extension/>`__.
   The documentation will then automatically be rendered on docs.typo3.org.

.. tip::

   Think about hosting your extension repository on GitHub.
   That way others can report issues and assist you by creating change requests
   for the documentation and code!

