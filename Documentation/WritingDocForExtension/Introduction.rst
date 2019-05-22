.. include:: ../Includes.txt
.. highlight:: rst

.. _write-doc-extensions-intro:

=====================
Introduction & Basics
=====================

.. _extension-documentation-files:

Extension Documentation Files
=============================

The documentation for extensions is structured in a similar way as the documentation
for official manuals.

See :ref:`general-conventions-dir-and-filenames` for more details on these files.

See https://github.com/TYPO3-Documentation/TYPO3CMS-Example-ExtensionManual for an
example.

See :ref:`writing-doc-for-ext-from-scratch` if you want to start extension documentation
right now.

About TYPO3 Extensions
======================

In TYPO3, basically everything is an extension. There are system extensions
and third party extensions:

System Extensions
-----------------

System extensions (or core extensions) are extensions that are maintained
in the TYPO3 source. For a list of system extensions, look in the Extension
Manager or in the TYPO3 source, e.g. `GitHub: TYPO3.CMS: /typo3/sysext
<https://github.com/TYPO3/TYPO3.CMS/tree/master/typo3/sysext>`__.

Examples for system extensions are:

* `ext:form <https://docs.typo3.org/typo3cms/extensions/form/>`__
* `ext:fluid_styled_content <https://docs.typo3.org/typo3cms/extensions/fluid_styled_content/>`__
* `ext:rte_ckeditor <https://docs.typo3.org/typo3cms/extensions/rte_ckeditor/>`__

Note, that if your system has been installed with Composer, not all system extensions may exist
in the system, if each system extension has been required separately as "subtree splitted packages"
(not as `typo3/cms`). Since TYPO3 9, installation of "subtree splitted packages" is mandatory.

For more information on subtree split, see

* `Usetypo3: The TYPO3 Subtree Split and Composer <https://usetypo3.com/typo3-subtree-split-and-composer.html>`__
* :ref:`Installation and Upgrade guide: Composer migration <composer-migration-require-subtree-packages>`

System Extension Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Find the documentation for a system extension on
`System extensions <https://docs.typo3.org/typo3cms/SystemExtensions/Index.html>`__.

Not all system extensions have documentation at the moment.

For more information about contributing to system extensions, see :ref:`contribute-to-system-extension`
in this guide.

See also :ref:`overview-of-types` for an overview of the issues, source and workflow for various
kinds of documentation, including system extensions.

Third Party Extensions
----------------------

Third party extensions are extension that can be created by anyone. They are not included in the TYPO3 core
codebase and are not officially supported by the TYPO3 core team.

Often, but not necessarily, these extensions are hosted on GitHub.

They can be installed by the TYPO3 Extension Manager or via Composer.

Third Party Extension Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Find the documentation on `Extensions by extension key <https://docs.typo3.org/typo3cms/extensions/Index.html>`__.

For more information about contributing to third party extension documentation or for your own extension, see
:ref:`contribute-to-3rdparty-extension`. See :ref:`how-to-start-documentation-for-ext` for
information about starting extension documentation from scratch.

See also :ref:`overview-of-types` for an overview of the issues, source and workflow for various
kinds of documentation, including third party extensions.
