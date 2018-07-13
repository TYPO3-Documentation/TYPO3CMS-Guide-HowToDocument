.. include:: ../Includes.txt
.. highlight:: rst

.. _rendering-docs:

==============
Rendering docs
==============

This chapter explains how to render the docs locally on your machine
with docker.

It is recommended to do this before you publish your changes, because
that way you will get a preview of how it is later rendered on the
server.

Using docker, you will use the same set of tools that are being used
on the documentation server docs.typo3.org to render the documentation.

Here, we will briefly also explain the other methods for rendering.

.. important::

   Please note that the **docker** method is currently the **recommended and
   fully supported** method.


.. rst-class:: bignums

   1. (recommended) docker method

      See :ref:`rendering-docs-quickstart`

   2. Extension *sphinx*

      If you install the extension
      `sphinx <https://extensions.typo3.org/extension/sphinx/>`__,
      you can render the extension
      documentation of the extensions that are currently installed in the
      Backend of your TYPO3 installation.

   3. Preview on Github

      This method is useful if you are editing documentation directly on
      Github

      Please be aware that the preview supports reST, but not the
      additional sphinx markup, such as the *toctree* or the
      :ref:`intersphinx <intersphinx>`__ linking. Because of this, the
      preview is not to be recommended for major changes that involve
      markup beyond basic reST markup.

   4. Using a Starter project (Sandbox)

      With this method, you will get a starter project, where you can
      make your changes directly on Github. The changes will automatically
      be rendered.

   5. Various online or local tools for reST rendering

      These have the same drawbacks as already noted on "Preview on Github".



.. toctree::
   :hidden:
   :glob:

   Quickstart
   Troubleshooting