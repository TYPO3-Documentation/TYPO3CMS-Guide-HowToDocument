.. include:: ../Includes.txt
.. highlight:: rst

.. _rendering-docs:
.. _rendering-docs-quickstart:

===========================
How to Render Documentation
===========================

This chapter explains how to render a manual locally on your machine
with Docker.

It is recommended to do this if you edit locally before you publish your changes, because
that way you will get a preview of how it is later rendered on the
server.

If you use Docker, you will use the same set of tools locally in Docker that are being used
on the documentation server docs.typo3.org to render the documentation.

Here, we will briefly also explain the other methods for rendering.

.. important::

   Please note that the **Local Editing and Rendering with Docker**
   is currently the **recommended and  fully supported** workflow.
   If you edit on GitHub directly, GitHub preview
   should also be sufficient for making small changes.


.. rst-class:: bignums

   1. Render Documentation Locally Using Docker

      See :ref:`render-documenation-with-docker`

   2. Preview on GitHub

      This method is useful if you are editing documentation directly on
      GitHub

      Please be aware that the preview on GitHub supports reST, but not the
      additional sphinx markup, such as the *toctree* or the
      :ref:`intersphinx <intersphinx>` linking. Because of this, the
      preview is not to be recommended for major changes that involve
      markup beyond basic reST markup.

   3. Extension *sphinx*

      If you install the extension
      `sphinx <https://extensions.typo3.org/extension/sphinx/>`__,
      you can render extension documentation of the extensions that are currently
      installed in the backend of your TYPO3 installation.

   4. Using a Starter Project (Sandbox)

      With this method, you will get a starter project, where you can
      make your changes directly on GitHub. The changes will automatically
      be rendered. To get access to a starter project, you must contact the
      Documentation Team. Use the Slack channel **#typo3-documentation**
      as described in :ref:`slack`.

   5. Various Online or Local Tools for reST Rendering

      These have the same drawbacks as already noted for *Preview on GitHub*.



.. toctree::
   :hidden:
   :glob:

   Quickstart
   Troubleshooting
