.. include:: ../Includes.txt
.. highlight:: rst

.. _write-doc-extensions-intro:

=====================
Introduction & Basics
=====================


About Extension Documentation
=============================

The documentation for all extensions is structured in the same way: The
extension contains a directory `Documentation` with at least the following files:

* `Index.rst` : contains text to be rendered on the startpage and the toctree
* `Includes.txt` : some basic definitions for sphinx
* `Settings.cfg` : settings

These are the same files and general principles that apply to any documentation
project. See :ref:`general-conventions-dir-and-filenames` for more information.

See https://github.com/TYPO3-Documentation/TYPO3CMS-Example-ExtensionManual for an
example.

The Documentation may deviate from this recommendation, for example it may consist
of only one `Readme.rst` or `Readme.md`. See :ref:`supported-filenames-and-formats`.
Please note that using this has some drawbacks and it is recommended to use the
files as described in :ref:`general-conventions-dir-and-filenames`.

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

Note, that if your system has been installed with composer, not all system extensions may exist
in the system, if each system extension has been required separately as "subtree splitted packages"
(not as `typo3/cms`). Since TYPO3 9, installation of "subtree splitted packages" is mandatory.

For more information on subtree split, see

* `Usetypo3: The TYPO3 Subtree Split and Composer <https://usetypo3.com/typo3-subtree-split-and-composer.html>`__
* :ref:`Installation and Upgrade guide: Composer migration <composer-migration-require-subtree-packages>`

System Extension Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Find the documentation for a system extension on
`Core extensions <https://docs.typo3.org/typo3cms/SystemExtensions/Index.html>`__.

Not all core extensions have documentation at the moment.

For more information about contributing to system extensions, see :ref:`contribute-to-system-extension`
in this guide.

See also :ref:`overview-of-types` for an overview of the issues, source and workflow for various
kinds of documentation, including system extensions.

Third Party Extensions
----------------------

third party extensions are extension that can be created by anyone. They are not included in the TYPO3 core
codebase and are not officially supported by the TYPO3 core team.

Often, but not necessarily, these extensions are hosted on GitHub.

The can be installed by the TYPO3 extension manager or via Composer.

Third Party Extension Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Find the documentation on `Extensions by extension key <https://docs.typo3.org/typo3cms/extensions/Index.html>`__.

For more information about contributing to third party extension documentation or for your own extension, see
:ref:`contribute-to-3rdparty-extension`. See :ref:`how-to-start-documentation-for-ext` for
information about starting extension documentation from scratch.

See also :ref:`overview-of-types` for an overview of the issues, source and workflow for various
kinds of documentation, including third party extensions.
