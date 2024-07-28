:navigation-title: Document extensions

.. include:: /Includes.rst.txt
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

   *  Make sure :ref:`t3coreapi:composer-json` is up to date. (*required*)
   *  Make sure :ref:`settings-cfg` is up to date. (*required*)
   *  A .gitignore is useful, in order to
      prevent accidentally committing the generated documentation in
      :file:`Documentation-GENERATED-temp` to the Git repository. (*recommended*)
   *  An .editorconfig is useful, so the
      recommended :ref:`Coding Guidelines <format-rest-cgl>` will be used within
      an editor or IDE.

   .. code-block:: bash

      # cp .gitignore (make sure you don't accidentally overwrite existing one though!)
      cp -n TYPO3CMS-Example-ExtensionManual/.gitignore <my-extension-directory>/.gitignore
      # cp .editorconfig (make sure you don't accidentally overwrite existing one though!)
      cp -n TYPO3CMS-Example-ExtensionManual/.editorconfig <my-extension-directory>/.editorconfig

   If you plan to host your extension on a public repository, consider
   adding a CONTRIBUTING.rst
   and :ref:`README.rst <readme-rst>` to help guide any future
   contributors.


#. Start adding documentation

   Now it's time to start adding content. Reviewing existing guides can help you structure your own documentation.
   The `news extension <https://docs.typo3.org/p/georgringer/news/main/en-us/Index.html>`__ is a strong example of how extension
   documentation should be written and structured.

#. Populate composer.json

   Complete the :file:`composer.json` as described in :ref:`t3coreapi:composer-json`.

#. Populate guides.xml

   Complete the :file:`guides.xml` as described in :ref:`settings-guides-xml`.

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

Version numbers
===============

docs.typo3.org does no longer show three level version numbers in form of ``Major.Minor.Patch``.
Only the first two levels are shown ``Major.Minor``.

This reduces the amount of documentation while keeping relevant information,
as patch levels should not introduce breaking changes or new features.

.. index:: Rendering; Branches
.. _migrate-branches:
.. _supported-branches:

Supported branches
==================

The rendering supports two branches within repositories:

``main`` / ``master``
   Should contain the current development state, used for upcoming release.
   Every push to these branches triggers a new rendering, available at
   :samp:`https://docs.typo3.org/p/<vendor>/<package>/main/en-us/`.

   Both branch names are supported, but result in the same URL.
   Please use ``main``, ``master`` is only supported for backward compatibility.

``documentation-draft``
   Should contain a draft of the documentation.
   Every push to this branch triggers a new rendering, available at
   :samp:`https://docs.typo3.org/p/<vendor>/<package>/draft/en-us/`
   (same URL as main, except *main* is replaced by *draft*).


   This is not indexed by search engines. This branch can be used to test
   rendering before releasing a new version of an extension.

   In order to test a different rendering, remove the branch, and create it
   again.


.. toctree::
   :maxdepth: 1
   :hidden:

   Webhook
   ReregisterVersions
   FAQ
   ContributeToSystemExtension
   ContributeToThirdPartyExtension
