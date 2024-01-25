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
    :file:`.rst.txt'.
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

The documentation index file at :file:`Documentation/Index.rst` is the starting
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
        :caption: HOWTOS

        WritingContent/Index
        WritingDocForExtension/Index
        ...

    ..  toctree::
        :hidden:
        :caption: ADVANCED

        HowToAddTranslation/Index
        GeneralConventions/HowToUpdateDocs
        GeneralConventions/ReviewInformation

    ..  toctree::
        :hidden:
        :caption: MAINTAINERS

        Maintainers/Index

.. index:: File structure; Documentation/Includes.rst.txt, Includes.rst.txt
.. _includes-rst-txt:

Global rst settings: :file:`Documentation/Includes.rst.txt`
-----------------------------------------------------------

Default style configurations are bundled in a central
Documentation/Includes.rst.txt file and included at the beginning of
each reST file. An absolute file path should be passed to use the same include
statement on every page, regardless of which folder level the reST file is in:

..  code-block:: rst

    ..  include:: /Includes.rst.txt

Normally, the include directive is used with files with the extension *.txt*.
To help your IDE associate reST syntax highlighting with the included files,
we use the specific *.rst.txt* file extension.

Typical style configurations in TYPO3 documentation are definitions of custom
text roles that allow :ref:`inline code <Inline-Code>` to be written. This is a
typical Includes.rst.txt that provides text roles for most programming and
markup languages used in a TYPO3 project:

..  tabs::

    ..  group-tab:: With placeholders

        ..  include:: /CodeSnippets/FileStructure/IncludesRstTxt.rst.txt

    ..  group-tab:: Third party extension

        ..  include:: /CodeSnippets/FileStructure/Examples/IncludesRstTxt.rst.txt

    ..  group-tab:: System extension

        ..  include:: /CodeSnippets/FileStructure/Dashboard/IncludesRstTxt.rst.txt

    ..  group-tab:: Official manual

        ..  include:: /CodeSnippets/FileStructure/GettingStarted/IncludesRstTxt.rst.txt

The text roles that have been assigned a specific class mimic the syntax
highlighting of another language. This is done to avoid confusing the reader
with too many different colors. For example, XML inline code may be semantically
marked with `:xml:`, but under the hood it uses the same highlighting as
`:html:`.


.. index:: File structure; Documentation/Sitemap.rst, Sitemap.rst
.. _sitemap-rst:

Optional: :file:`Documentation/Sitemap.rst`
-------------------------------------------

The :file:`Sitemap.rst` contains the sitemap of the documentation.
It is an almost empty file that is automatically filled by the Sphinx template.

..  code-block:: rst

    :template: sitemap.html

    .. include:: /Includes.rst.txt

    =======
    Sitemap
    =======

    .. The sitemap.html template will insert here the page tree automatically.


.. index:: File structure; Documentation/genindex.rst, genindex.rst
.. _genindex-rst:

Optional: Automatic index: :file:`Documentation/genindex.rst`
-------------------------------------------------------------

The genindex.rst shows a list of all indexes of the documentation pages. It is
an almost empty file that is automatically filled by Sphinx. An index can be
manually applied to each documentation location using the
:rst:dir:`index directive <sphinx:index>`.
In addition, some content elements automatically generate indexes, such as the
:ref:`configuration values <rest-confval>` and
:ref:`PHP domain <rest-phpdomain>` elements.

..  code-block:: rst

    .. include:: /Includes.rst.txt

    =====
    Index
    =====

    .. Sphinx will insert here the general index automatically.


.. index:: File structure; Documentation/Settings.cfg, Settings.cfg
.. _settings-cfg:

Settings: :file:`Documentation/Settings.cfg`
--------------------------------------------

This file contains the configuration for the Sphinx theme. The configuration
values are used to fill placeholders in the theme. It consists of sections
starting with a keyword in brackets, e.g. ``[general]``: Make sure that all
properties are in the correct section!

..  tabs::

    ..  group-tab:: With placeholders

        ..  include:: /CodeSnippets/FileStructure/SettingsCfg.rst.txt

        The placeholders of pattern `<name>` must be replaced manually by the author of
        the documentation, and commented or set empty if not required.

    ..  group-tab:: Third party extension

        ..  include:: /CodeSnippets/FileStructure/Examples/SettingsCfg.rst.txt

    ..  group-tab:: System extension

        ..  include:: /CodeSnippets/FileStructure/Dashboard/SettingsCfg.rst.txt

    ..  group-tab:: Official manual

        ..  include:: /CodeSnippets/FileStructure/GettingStarted/SettingsCfg.rst.txt

.. _settings-cfg-project:

Project
^^^^^^^

The *project* property contains the title of the project and is displayed in the
left sidebar (desktop) or the top (mobile) of the theme and in the title meta
tag.

Common values are in the official TYPO3 manuals

#. `<Topic> Guide`, e.g. "Frontend Localization Guide",
   for collections of articles on a specific topic
#. `<Topic> Reference`, e.g. "TSconfig Reference",
   for a complete encyclopedia
#. `<Topic> Tutorial`, e.g. "Editors Tutorial",
   for collections of tutorials on a specific topic

and in TYPO3 extension documentations

*  `<Topic>`, e.g. "Import / Export" or "Mask".


.. _settings-cfg-version-and-release:

Version and release
^^^^^^^^^^^^^^^^^^^

The properties *version* and *release* both contain the version of the manual
and mostly correspond to the version of the TYPO3 LTS or TYPO3 extension to
which the documentation refers.

The version is shown below the title in the theme's release switch and in the
title meta tag, the release is not shown currently  - but it should be
kept anyway to satisfy internal requirements.

Normally both properties are set to the same value, either

*   `<major>.<minor>`, e.g. "11.5", or
*   `<major>.<minor>.<fix>`, e.g. "11.5.1", or
*   `main (development)`.

For the release switch entries, only the major and minor versions are
considered.


.. _settings-cfg-copyright:

Copyright
^^^^^^^^^

The *copyright* property contains the copyright claim of the project. It is
displayed in the footer as "© Copyright <copyright>" and has in most use cases
of the TYPO3 world the values:

#.  `since <creation-year> by the TYPO3 contributors`,
    for example "since 1999 by the TYPO3 contributors" (official TYPO3 manuals and TYPO3
    system extensions)
#.  `since <creation-year> by <vendor> & contributors`,
    for example "since 1999 by dkd & contributors" (third-party TYPO3 extensions)


.. _settings-cfg-github-workflow:

GitHub workflow
^^^^^^^^^^^^^^^

The *github_repository* and *github_branch* properties must be set to provide
the "Edit on GitHub" button, which allows the reader to jump from the currently
viewed documentation directly to the associated GitHub repository and edit the
page file.

If the project is hosted on GitHub and public contributions are desired, these
properties should be set accordingly:

1.  `<user>/<repository>`, for example to "TYPO3-Documentation/TYPO3CMS-Reference-TCA"
    or "FriendsOfTYPO3/extension_builder".
2.  `<branch>`, for example on "main" or "10.x".


.. _settings-cfg-footer-links:

Footer links
^^^^^^^^^^^^

The *project_<topic>* properties provide all links with the name "<Topic>" in
the footer of the documentation that guide the user to other aspects of the
project than the documentation, for example to the project page in the TER:

*   *project_home* is set to the homepage URL of the project. For official TYPO3
    manuals this is the public base URL at docs.typo3.org, for public TYPO3
    extensions this is the associated TER page or a custom project website, for
    example

    *  "\https://docs.typo3.org/m/typo3/reference-coreapi/main/en-us/" or
    *  "\https://extensions.typo3.org/extension/news".

*   *project_contact* is usually set to an email address or Slack channel URL of
    the team behind the project, for example

    *  "\mailto:documentation\@typo3.org" or
    *  "\https://typo3.slack.com/archives/C028JEPJL".

*   *project_repository* is set to the repository of the project's VCS, for
    example

    *  "\https://github.com/FriendsOfTYPO3/extension_builder".

*   *project_issues* is set to the location where project issues are to be
    created and edited, for example

    *  "\https://github.com/FriendsOfTYPO3/extension_builder/issues".

*   *project_discussions* is used in the rare case that project-related
    discussions take place in locations other than those defined by the
    project_contact and project_issues properties, for example

    *  "\https://github.com/FriendsOfTYPO3/extension_builder/discussions".


.. _settings-cfg-use-opensearch:

Use OpenSearch
^^^^^^^^^^^^^^

If the *use_opensearch* property is set to the public URL of the documentation,
Sphinx renders an OpenSearch description file of the documentation, which allows
most browsers to treat the internal search of your documentation as a global
search engine and include it in their search bar like any other search engine.
This seems useful if your documentation is a large reference that is of high
public interest and likely to be searched frequently by readers. Good examples
of this are the PHP or TYPO3 Core references, for example
"\https://docs.typo3.org/m/typo3/reference-typoscript/main/en-us/", while the
TYPO3 extension documentations probably are not.


.. _settings-cfg-intersphinx-mapping:

Intersphinx mapping
^^^^^^^^^^^^^^^^^^^

The *[intersphinx_mapping]* section contains base URLs of public manuals for
convenient and verified cross-referencing.

For example, if you uncomment the *t3start* mapping in the Settings.cfg above,
the :samp:`https://docs.typo3.org/m/typo3/tutorial-getting-started/main/en-us/Extensions/Management.html`
page can be referenced with

..  code-block:: rst

    :doc:`t3start:Extensions/Management`

and the fragment :samp:`#install-extension-with-composer` on the same page with

..  code-block:: rst

    :ref:`t3start:install-extension-with-composer`

The prerequisite is that the target manual is also compiled with Sphinx and
provides an objects.inv file in the root of the documentation that
contains all reference targets. Since this file is binary, the rendering
toolchain provides a twin :file:`objects.inv.json` file that allows the reader
to easily look up reference targets. An example of this is this
`production objects.inv.json <https://docs.typo3.org/m/typo3/tutorial-getting-started/main/en-us/objects.inv.json>`__.

If a target reference becomes unavailable during documentation rendering, for
example if it has been permanently removed, a warning is issued and stored in
the toolchain log file at :file:`Documentation-GENERATED-temp/Result/project/0.0.0/_buildinfo/warnings.txt`.


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

        ..  include:: /CodeSnippets/FileStructure/ReadmeRstStandalone.rst.txt

    ..  group-tab:: Markdown

        ..  include:: /CodeSnippets/FileStructure/ReadmeMdStandalone.rst.txt
