.. include:: ../Includes.txt
.. highlight:: rst

.. _writing-doc-for-ext-start:
.. _how-to-start-docs-extension:
.. _extension-documentation-files:
.. _write-doc-extensions-intro:

============================
How to Document an Extension
============================

.. important::

   When redirected here, :ref:`migrate` might be the place to check out for
   information about how to migrate existing documentation.


This chapters explains how to write documentation for an extension or make
changes to existing documentation of extensions. The extension may be a
third party extension by someone else or one you maintain yourself. It may
also be a system extension in the core.

The documentation for extensions has the same structure as the documentation
for official manuals. See :ref:`general-conventions-dir-and-filenames` for more details
on these files.

If you want to start new extension documentation, there are 2 ways to start:

#. :ref:`doc-for-ext-from-example`
#. :ref:`doc-for-ext-with-extension-builder`

This chapter assumes that you create, maintain and render the documentation for your extension
using :ref:`local editing and rendering with Docker <rendering-docs>`. It
requires Docker for running the rendering toolchain locally on
your computer to check if the documentation is rendered correctly.

An alternative for this is using a `documentation-draft` branch in your repository.
This will render the documentation as draft (which is not indexed by search engines).
You can use this to test changes. See :ref:`migrate-branches` for more information.


This chapter walks you through extension documentation. It provides links to
additional information, but you may also want to look at the following basic
resources:

* If necessary, ask for help as explained in :ref:`how-to-get-help`.
* :ref:`Coding Guidelines <format-rest-cgl>`
* :ref:`general-conventions-dir-and-filenames`
* :ref:`rest-cheat-sheet`
* :ref:`render-documenation-with-docker`
* :ref:`about-typo3-extensions`


.. toctree::
   :maxdepth: 1
   :hidden:

   CreateFromScratch
   CreateWithExtensionBuilder
   Migrate
   Webhook
   ExtensionAuthorTips
   ContributeToSystemExtension
   ContributeToThirdPartyExtension
   FAQ
