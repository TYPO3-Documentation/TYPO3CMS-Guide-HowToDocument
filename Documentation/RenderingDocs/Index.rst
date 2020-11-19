.. include:: ../Includes.txt
.. highlight:: rst

.. _rendering-docs:
.. _rendering-docs-quickstart:

===========================
How to Render Documentation
===========================

This chapter explains how to render a manual locally on your machine
with Docker in order to test the rendering.

It is recommended to do this if you edit locally before you publish your changes, because
that way you will get a preview of how it is later rendered on the
server.

If you use Docker, you will use the same set of tools locally in Docker that are being used
on the documentation server docs.typo3.org to render the documentation.

Here, we will briefly also explain the other methods for rendering.

.. important::

   The method of using a starter project (sandbox) with an URL such as
   `/typo3cms/drafts/github/T3DocumentationStarter/Public-Info-056/` is now deprecated.
   You can still find your existing starter project on GitHub (https://github.com/T3DocumentationStarter)
   and render this locally.

.. important::

   Please note that the :ref:`Local Editing and Rendering with Docker <render-documenation-with-docker>`
   is currently the **recommended and  fully supported** workflow.
   If you edit on GitHub directly, GitHub preview should also be sufficient for making small changes.


.. rst-class:: bignums

   #. Render Documentation Locally Using Docker

      *  :ref:`render-documenation-with-docker` (should work on Linux)
      *  :ref:`render-with-docker-compose` (should work better on MacOS
         or Windows, but is still being tested)

   #. Preview on GitHub

      This method is useful if you are editing documentation directly on
      GitHub

      Please be aware that the preview on GitHub supports reST, but not the
      additional sphinx markup, such as the *toctree* or the
      :ref:`intersphinx <intersphinx>` linking. Because of this, the
      preview is not to be recommended for major changes that involve
      markup beyond basic reST markup.

   #. Preview using documentation-draft

      You can use the `documentation-draft` to get a preview for your extensions.
      See :ref:`migrate-branches`.

   #. Extension *sphinx*

      If you install the extension
      `sphinx <https://extensions.typo3.org/extension/sphinx/>`__,
      you can render extension documentation of the extensions that are currently
      installed in the backend of your TYPO3 installation.

      This method has the drawback that sphinx must be installed on the system
      where the TYPO3 installation is running. The extension provides ways to
      do this, but there may be version conflicts and other difficulties.

      Using Docker avoids these problems by providing an entire self-contained
      environment including operating system and all required packages.

   #. Various Online or Local Tools for reST Rendering

      These have the same drawbacks as already noted for *Preview on GitHub*.



.. toctree::
   :hidden:
   :glob:

   Quickstart
   RenderWithDockerCompose
   Troubleshooting
