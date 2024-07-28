.. include:: /Includes.rst.txt

.. index:: File structure
.. _file-structure:

==============
File structure
==============

This page explains the general file structure of a TYPO3 documentation that can
be rendered with the :ref:`rendering toolchain <rendering-docs>`.

..  contents:: Table of Contents:
    :backlinks: top
    :class: compact-list
    :depth: 2
    :local:

.. _file-structure-general:

General
=======

In order for the documentation to be rendered, you need at least

*   A valid :ref:`composer.json <t3coreapi-stable:files-composer-json>`
*   A documentation entry point either for a :ref:`multi-page manual <full-documentation>`
    or for the rendering of a :ref:`single README file <single-file-documentation>`.

The following rules are mandatory or your documentation will not render:

*   :abbr:`reST (reStructured Text)` files MUST have the extension :file:`.rst'.
*   Markdown files MUST have the extension :file:`.md'.

Further conventions are:

*   :ref:`Included reST files <including-files>` SHOULD have the extension
    :file:`.rst.txt`.
*   Use **CamelCase** for directory and file names,
    for example: :file:`Documentation/GeneralConventions/FileStructure.rst`.
*   Each directory SHOULD have a file named :file:`Index.rst` it is used as
    fallback if a page is not found during switching versions.

.. index:: Full documentation
.. _full-documentation:

Full documentation
==================

To render a complete documentation manual you need a folder called
:file:`Documentation` with at least a reStructured Text file as entry point named
:file:`Documentation\Index.rst` and a configuration file called
:file:`Documentation\guides.xml`. Add more files as needed.

You can keep a :file:`README.md` or :file:`README.rst` file with basic
information and a link to the published manual in the root folder of the extension. These files will be commonly
displayed on GitHub and GitLab.

.. code-block:: none

   .
   ├── composer.json
   ├── README.rst
   └── Documentation
       ├── guides.xml
       ├── Index.rst
       ├── Sitemap.rst
       └── ..

.. index:: File structure; Documentation/Index.rst, Index.rst
.. _index-rst:
.. _start-file:

Start page: :file:`Documentation/Index.rst`
-------------------------------------------

The documentation start page (:file:`Documentation/Index.rst`) is the entry
point of the main documentation. It usually contains general information about
the manual, a summary of its purpose and a table of contents that refers to
further pages.

The start page should contain an anchor target :rst:`..  _start:` above its
document title. This way you can link to a documents start page by:

..  code-block:: rst

    See :ref:`TYPO3 Explained <t3coreapi:start>`.

If your manual has more pages then this start page it must contain a table of content
directive called :rst:`..  toctree::`. The `toctree` on the start page
defines which pages will be displayed in main navigation of the rendered
manual.

.. _index-rst-table-of-contents:

Configure the menu - the toctree
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The `toctree` on the start page can be hidden, it then only influences the main
navigation:

..  code-block:: rst

    ..  toctree::
        :hidden:

        Introduction/Index
        Installation/Index
        Configuration/Index
        Usage/Index
        Contribution/Index

Or it can be inserted visibly into the start page to provide an entry point:

..  code-block:: rst

    ..  toctree::
        :maxdepth: 2
        :titlesonly:

        Introduction/Index
        Installation/Index
        Configuration/Index
        Usage/Index
        Contribution/Index

For large pages it is advisable to limit the number of menu levels that will
be displayed on the startpage by setting :rest:`:maxdepth:`. This will not
limit the level of pages displayed in the main navigation.

For more information on possible options on the `toctree` directive see
chapter :ref:`Toctrees in the reST reference <toctree>`.

It is possible to use more then one `toctree` directive on the start page.
Each `toctree` should have a :rst:`:caption:` in this case.

The main navigation will then be divided into sections labeled by those
captions. The menu of the manual you are currently reading is an example for
that:

..  code-block:: rst
    :caption: Documentation/Index.rst

    ..  toctree::
        :hidden:
        :caption: Basics

        About
        HowToGetHelp
        ...

    .. toctree::
        :hidden:
        :caption: Howtos

        WritingContent/Index
        WritingDocForExtension/Index
        ...

    ..  toctree::
        :hidden:
        :caption: Advanced

        HowToAddTranslation/Index
        GeneralConventions/HowToUpdateDocs
        GeneralConventions/ReviewInformation

    ..  toctree::
        :hidden:
        :caption: Maintainers

        Maintainers/Index

.. index:: File structure; Documentation/Sitemap.rst, Sitemap.rst
.. _sitemap-rst:

Optional: :file:`Documentation/Sitemap.rst`
-------------------------------------------

The :file:`Sitemap.rst` contains the sitemap of the documentation.
It is an almost empty file that is automatically filled during rendering.

..  code-block:: rst

    :template: sitemap.html

    .. include:: /Includes.rst.txt

    =======
    Sitemap
    =======

    .. The sitemap.html template will insert here the page tree automatically.


.. index:: File structure; Documentation/Settings.cfg, Settings.cfg
.. _settings-cfg:
.. _settings-guides-xml:

Settings: :file:`Documentation/guides.xml`
--------------------------------------------

This file contains the metadata and configuration for the rendering with the
TYPO3 theme.

Read more about the :ref:`guides-xml`.

..  hint::
    If you are migrating from the legacy Sphinx-based rendering and still have
    a :file:`Documentation/Settings.cfg` you can use an automatic migration
    tool to :ref:`migrate the settings.cfg into a guides.xml <migrate_guides_xml>`.

Example:

..  literalinclude:: _guides-simple.xml
    :capition: Documentation/guides.xml


.. index:: Single file documentation
.. _single-file-documentation:

Single file documentation (README)
==================================

For third-party TYPO3 extensions that do not require extended documentation
you can also publish a :file:`README.rst` or :file:`README.md` to
https://docs.typo3.org/

For this workflow the :file:`README(.rst/.md)` MUST be situated in the
extension's root folder. The :file:`Documentation/' folder can then be omitted.

:file:`README.rst`
------------------

For single file documentation, the :file:`README.rst` contains the entire
documentation.

This should also contain links to all aspects of the project to guide the reader
to the next steps, for example

..  tabs::

    ..  group-tab:: Rest

        ..  include:: /_CodeSnippets/FileStructure/ReadmeRstStandalone.rst.txt

    ..  group-tab:: Markdown

        ..  include:: /_CodeSnippets/FileStructure/ReadmeMdStandalone.rst.txt
