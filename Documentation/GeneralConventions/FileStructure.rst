.. include:: /Includes.rst.txt

.. index:: File structure
.. _file-structure:

==============
File structure
==============

This page explains the general file structure of a TYPO3 documentation that can
be rendered with the :ref:`rendering toolchain <rendering-docs>`. The toolchain
itself uses a `Sphinx theme <https://typo3-documentation.github.io/sphinx_typo3_theme/>`__
for converting reStructuredText (reST) or Markdown to HTML.

.. contents:: Table of Contents:
   :backlinks: top
   :class: compact-list
   :depth: 2
   :local:


.. _file-structure-general:

General
=======

In order for the documentation to be rendered, you need at least

#. an index file in one of the following locations in weighted order:

   -  :file:`Documentation/Index.rst`
   -  :file:`Documentation/index.rst`
   -  :file:`Documentation/Index.md`
   -  :file:`Documentation/index.md`
   -  :file:`README.rst`
   -  :file:`README.md`

#. and a theme configuration file under

   - :file:`Documentation/Settings.cfg`.

Further conventions are:

*  reST files have the extension **.rst**.
*  Markdown files have the extension **.md**.
*  Included reST files have the extension **.rst.txt**.
*  Use **CamelCase** for directory and file names,
   for example: Documentation/GeneralConventions/FileStructure.rst.

These conventions pave the way for the *full documentation* and the
*single file documentation* style, the first being preferred for several
reasons.


.. index:: Full documentation
.. _full-documentation:

Full documentation
==================

This is the recommended setup and is commonly used in the official TYPO3 manuals
and extension documentation.

This structure splits the documentation for the VCS host (README.rst) and the
Sphinx theme (Documentation/) and allows full use of a continuously expanded set
of :ref:`custom content elements <rest-reference>`, like UML diagrams, which are
only supported by the theme. This structure allows to add multiple pages to
the documentation and build a full page tree.

The Settings.cfg configuration file allows you to set theme variables, i.e. the
project title, release version and the like.

Of course, you can also use a README.md instead of a README.rst file as both
markup languages are supported by the common VCS hosts.

.. code-block:: none

   .
   ├── README.rst
   └── Documentation
       ├── genindex.rst
       ├── Includes.rst.txt
       ├── Index.rst
       ├── Settings.cfg
       ├── Sitemap.rst
       └── ..


.. index:: File structure; README.rst, README.rst
.. _readme-rst:
.. _about-file:

README.rst
----------

Full documentation contains both a README.rst and a Documentation/Index.rst
file. To avoid redundancy in both places, the README.rst in this case usually
contains only a summary and links to all aspects of the project, i.e. the VCS
repository, the published documentation and - if available - the TYPO3 Extension
Repository (TER) page to guide the reader to the next steps. This could be for
example:

.. code-block:: rst

   <badges>

   =========
   <project>
   =========

   <abstract>

   :Repository:  https://<vcs-repository>
   :Read online: https://docs.typo3.org/p/<package-name>/main/en-us/
   :TER:         https://extensions.typo3.org/extension/<extension-key>/

or as README.md alternatively:

.. code-block:: md

   <badges>

   # <project>

   <abstract>

   |                  | URL                                                           |
   |------------------|---------------------------------------------------------------|
   | **Repository:**  | https://<vcs-repository>                                      |
   | **Read online:** | https://docs.typo3.org/p/<package-name>/main/en-us/           |
   | **TER:**         | https://extensions.typo3.org/extension/<extension-key>/       |


.. _readme-rst-badges:

Badges
^^^^^^

Point out interesting statistics of your extension or package in the *badges*
placeholder, which should include the latest release version, the total and
monthly download rate and the supported TYPO3 versions:

.. code-block:: rst

   .. image:: https://poser.pugx.org/<package-name>/v/stable
      :alt: Latest Stable Version
      :target: https://extensions.typo3.org/extension/<extension-key>/

   .. image:: https://img.shields.io/badge/TYPO3-11-orange.svg
      :alt: TYPO3 11
      :target: https://get.typo3.org/version/11

   .. image:: https://poser.pugx.org/<package-name>/d/total
      :alt: Total Downloads
      :target: https://packagist.org/packages/<package-name>

   .. image:: https://poser.pugx.org/<package-name>/d/monthly
      :alt: Monthly Downloads
      :target: https://packagist.org/packages/<package-name>

or for the README.md alternatively:

.. code-block:: md

   [![Latest Stable Version](https://poser.pugx.org/<package-name>/v/stable)](https://extensions.typo3.org/extension/<extension-key>/)
   [![TYPO3 11](https://img.shields.io/badge/TYPO3-11-orange.svg?style=flat-square)](https://get.typo3.org/version/11)
   [![Total Downloads](https://poser.pugx.org/<package-name>/d/total)](https://packagist.org/packages/<package-name>)
   [![Monthly Downloads](https://poser.pugx.org/<package-name>/d/monthly)](https://packagist.org/packages/<package-name>)

Remove this field if the project is no extension or package.


.. _readme-rst-project:

Project
^^^^^^^

The *project* placeholder contains the title of the project.

Common values are in the official TYPO3 manuals

#. `<Topic> Guide`, e.g. "Installation and Upgrade Guide",
   for collections of articles on a specific topic
#. `<Topic> Reference`, e.g. "TCA Reference",
   for a complete encyclopedia
#. `<Topic> Tutorial`, e.g. "Getting Started Tutorial",
   for collections of tutorials on a specific topic

in TYPO3 system extensions

*  `TYPO3 CMS <Topic> (<package-name>)`, e.g. "TYPO3 CMS Extbase (typo3/cms-extbase)".

and in TYPO3 third-party extensions

*  `TYPO3 extension <extension-key>`, e.g. "TYPO3 extension \`\`mask\`\`".


.. _readme-rst-abstract:

Abstract
^^^^^^^^

The *abstract* placeholder contains a short and precise description of the
project with as many keywords as possible in as few sentences as possible. It
helps the decision maker to quickly decide whether the project is worth
considering and whether or not to read the full documentation. It should be
aligned with the abstract of Index.rst and - if available - the description
fields of ext_emconf.php and composer.json.


.. index:: File structure; Documentation/Index.rst, Index.rst
.. _index-rst:
.. _start-file:

Documentation/Index.rst
-----------------------

The documentation index file at Documentation/Index.rst is the starting
point of the main documentation. It usually contains general information about
the manual, a summary of its purpose and a table of contents that refers to
further pages. Besides these basic parts of this file, it includes - like any
other reST file - the reST style file Includes.rst.txt:

.. code-block:: rst

   .. include:: /Includes.rst.txt

   =========
   <project>
   =========

   :Extension key:
      <extension-key>

   :Package name:
      <package-name>

   :Version:
      |release|

   :Language:
      en

   :Author:
      <author>

   :License:
      This document is published under the
      `Creative Commons BY 4.0 <https://creativecommons.org/licenses/by/4.0/>`__
      license.

   :Rendered:
      |today|

   ----

   <abstract>

   ----

   **Table of Contents:**

   <table-of-contents>

   .. Meta Menu

   <meta-menu>

All variables of the `|name|` pattern are automatically replaced by the Sphinx
theme, partly from Settings.cfg, partly by internal calculations. For more
information about all available variables, see the
:doc:`Replacements <t3sphinxtest:Replacements/Index>` chapter of the Sphinx
theme documentation.

The placeholders of pattern `<name>` must be replaced manually by the author of
the documentation:


.. _index-rst-project:

Project
^^^^^^^

The *project* placeholder corresponds best to the project property of
Settings.cfg and - in case of a TYPO3 extension documentation - to the title
field of ext_emconf.php.


.. _index-rst-extension-key:

Extension key
^^^^^^^^^^^^^

The *extension-key* placeholder contains the TYPO3 extension key in case of a
TYPO3 extension documentation.

Remove this field if the project has no extension key.


.. _index-rst-package-name:

Package name
^^^^^^^^^^^^

The *package-name* placeholder contains the Composer package name of the
project.

Remove this field if the project is no installable package.


.. _index-rst-author:

Author
^^^^^^

The *author* placeholder best matches the copyright holders in the Settings.cfg
copyright property, since the authors of an open source project are also
copyright holders. It is also a good place to mention initiators and outstanding
contributors.


.. _index-rst-abstract:

Abstract
^^^^^^^^

The *abstract* placeholder contains a short and precise description of the
project. It should follow the abstract of README.rst and - if available - the
description fields of ext_emconf.php and composer.json.


.. _index-rst-table-of-contents:

Table of contents
^^^^^^^^^^^^^^^^^

The *table-of-contents* placeholder contains a rough table of contents (TOC),
which - in combination with the abstract - should give the reader a quick
overview. The TOC is built with the
:doc:`toctree directive <WritingReST/MenuHierarchy>` as follows:

.. code-block:: rst

   .. toctree::
      :maxdepth: 2
      :titlesonly:

      Introduction/Index
      Installation/Index
      Configuration/Index
      Usage/Index
      Contribution/Index

The *maxdepth* property limits the depth of the page tree and *titlesonly*
specifies that only the titles of the pages are displayed, no other headings.
Both should emphasize the nature of an overview.

The pages in the body of the directive are included in the TOC, and TOCs in
those pages are resolved recursively. The documentation author must edit the
list and provide a reST document at each of these file paths, interpreting the
file paths as relative to the current file.

In general, the file hierarchy should match the menu hierarchy, and a page must
be placed at either :file:`<page-name>.rst` or :file:`<page-name>/Index.rst`
- the latter if subpages exist or are expected. For example, the page of the
menu path "Usage > TYPO3 Backend > Shop Dashboard" should be stored at:

.. code-block:: none

   .
   └── Documentation
       └── Usage
           └── Typo3Backend
               └── ShopDashboard.rst

or - if it has the subpage "Sell Widget" - at

.. code-block:: none

   .
   └── Documentation
       └── Usage
           └── Typo3Backend
               └── ShopDashboard
                   ├── Index.rst
                   └── SellWidget.rst


.. _index-rst-meta-menu:

Meta menu
^^^^^^^^^

The *meta-menu* placeholder builds a second menu that is not visible in the
content area of the page, but only in the left sidebar (desktop) or toggle menu
(mobile) - separate from the main menu. It contains links to functional pages,
such as the :ref:`Sitemap.rst <sitemap-rst>` and the
:ref:`genindex.rst <genindex-rst>`, which do not provide content specific to
this documentation, as follows:

.. code-block:: rst

   .. toctree::
      :hidden:

      Sitemap
      genindex


.. index:: File structure; Documentation/Includes.rst.txt, Includes.rst.txt
.. _includes-rst-txt:

Documentation/Includes.rst.txt
------------------------------

Default style configurations are bundled in a central
Documentation/Includes.rst.txt file and included at the beginning of
each reST file. An absolute file path should be passed to use the same include
statement on every page, regardless of which folder level the reST file is in:

.. code-block:: rst

   .. include:: /Includes.rst.txt

Normally, the include directive is used with files with the extension *.txt*.
To help your IDE associate reST syntax highlighting with the included files,
we use the specific *.rst.txt* file extension.

Typical style configurations in TYPO3 documentation are definitions of custom
text roles that allow :ref:`inline code <Inline-Code>` to be written. This is a
typical Includes.rst.txt that provides text roles for most programming and
markup languages used in a TYPO3 project:

.. code-block:: rst

   .. More information about this file:
   .. https://docs.typo3.org/m/typo3/docs-how-to-document/main/en-us/GeneralConventions/FileStructure.html#includes-rst-txt

   .. ----------
   .. text roles
   .. ----------

   .. role:: aspect(emphasis)
   .. role:: bash(code)
   .. role:: css(code)
   .. role:: html(code)
   .. role:: js(code)
   .. role:: php(code)
   .. role:: rst(code)
   .. role:: sep(strong)
   .. role:: sql(code)

   .. role:: tsconfig(code)
      :class: typoscript

   .. role:: typoscript(code)
   .. role:: xml(code)
      :class: html

   .. role:: yaml(code)

   .. default-role:: code

   .. ---------
   .. highlight
   .. ---------

   .. By default, code blocks use PHP syntax highlighting

   .. highlight:: php

The text roles that have been assigned a specific class mimic the syntax
highlighting of another language. This is done to avoid confusing the reader
with too many different colors. For example, XML inline code may be semantically
marked with `:xml:`, but under the hood it uses the same highlighting as
`:html:`.


.. index:: File structure; Documentation/Sitemap.rst, Sitemap.rst
.. _sitemap-rst:

Documentation/Sitemap.rst
-------------------------

The Sitemap.rst contains the sitemap of the documentation. It is an almost empty
file that is automatically filled by the Sphinx template.

.. code-block:: rst

   :template: sitemap.html

   .. include:: /Includes.rst.txt

   =======
   Sitemap
   =======

   .. The sitemap.html template will insert here the page tree automatically.


.. index:: File structure; Documentation/genindex.rst, genindex.rst
.. _genindex-rst:

Documentation/genindex.rst
--------------------------

The genindex.rst shows a list of all indexes of the documentation pages. It is
an almost empty file that is automatically filled by Sphinx. An index can be
manually applied to each documentation location using the
:rst:dir:`index directive <sphinx:index>`.
In addition, some content elements automatically generate indexes, such as the
:doc:`configuration values <WritingReST/Confval>` and
:doc:`PHP domain <WritingReST/Phpdomain>` elements.

.. code-block:: rst

   .. include:: /Includes.rst.txt

   =====
   Index
   =====

   .. Sphinx will insert here the general index automatically.


.. index:: File structure; Documentation/Settings.cfg, Settings.cfg
.. _settings-cfg:

Documentation/Settings.cfg
--------------------------

This file contains the configuration for the Sphinx theme. The configuration
values are used to fill placeholders in the theme. It consists of sections
starting with a keyword in brackets, e.g. ``[general]``: Make sure that all
properties are in the correct section!

.. code-block:: none

   # More information about this file:
   # https://docs.typo3.org/m/typo3/docs-how-to-document/main/en-us/GeneralConventions/FileStructure.html#settings-cfg

   [general]

   project     = <project>
   version     = <version>
   release     = <release>
   copyright   = <copyright>

   [html_theme_options]

   # "Edit on GitHub" button
   github_repository    = <github-repository>
   github_branch        = <github-branch>

   # Footer links
   project_home         = <project-home>
   project_contact      = <project-contact>
   project_repository   = <project-repository>
   project_issues       = <project-issues>
   project_discussions  = <project-discussions>

   use_opensearch       = <use-opensearch>

   [intersphinx_mapping]

   # Official TYPO3 manuals
   # h2document     = https://docs.typo3.org/m/typo3/docs-how-to-document/main/en-us/
   # t3cheatsheets  = https://docs.typo3.org/m/typo3/docs-cheatsheets/main/en-us/
   # t3contribute   = https://docs.typo3.org/m/typo3/guide-contributionworkflow/main/en-us/
   # t3coreapi      = https://docs.typo3.org/m/typo3/reference-coreapi/main/en-us/
   # t3docteam      = https://docs.typo3.org/m/typo3/team-t3docteam/main/en-us/
   # t3editors      = https://docs.typo3.org/m/typo3/tutorial-editors/main/en-us/
   # t3extbasebook  = https://docs.typo3.org/m/typo3/book-extbasefluid/main/en-us/
   # t3extexample   = https://docs.typo3.org/m/typo3/guide-example-extension-manual/main/en-us/
   # t3home         = https://docs.typo3.org/
   # t3install      = https://docs.typo3.org/m/typo3/guide-installation/main/en-us/
   # t3l10n         = https://docs.typo3.org/m/typo3/guide-frontendlocalization/main/en-us/
   # t3sitepackage  = https://docs.typo3.org/m/typo3/tutorial-sitepackage/main/en-us/
   # t3start        = https://docs.typo3.org/m/typo3/tutorial-getting-started/main/en-us/
   # t3tca          = https://docs.typo3.org/m/typo3/reference-tca/main/en-us/
   # t3translate    = https://docs.typo3.org/m/typo3/guide-frontendlocalization/main/en-us/
   # t3tsconfig     = https://docs.typo3.org/m/typo3/reference-tsconfig/main/en-us/
   # t3tsref        = https://docs.typo3.org/m/typo3/reference-typoscript/main/en-us/
   # t3ts45         = https://docs.typo3.org/m/typo3/tutorial-typoscript-in-45-minutes/main/en-us/
   # t3viewhelper   = https://docs.typo3.org/other/typo3/view-helper-reference/main/en-us/
   # t3upgrade      = https://docs.typo3.org/m/typo3/guide-installation/main/en-us/

   # TYPO3 system extensions
   # ext_adminpanel     = https://docs.typo3.org/c/typo3/cms-adminpanel/main/en-us/
   # ext_core           = https://docs.typo3.org/c/typo3/cms-core/main/en-us/
   # ext_dashboard      = https://docs.typo3.org/c/typo3/cms-dashboard/main/en-us/
   # ext_felogin        = https://docs.typo3.org/c/typo3/cms-felogin/main/en-us/
   # ext_form           = https://docs.typo3.org/c/typo3/cms-form/main/en-us/
   # ext_fsc            = https://docs.typo3.org/c/typo3/cms-fluid-styled-content/main/en-us/
   # ext_impexp         = https://docs.typo3.org/c/typo3/cms-impexp/main/en-us/
   # ext_indexed_search = https://docs.typo3.org/c/typo3/cms-indexed-search/main/en-us/
   # ext_linkvalidator  = https://docs.typo3.org/c/typo3/cms-linkvalidator/main/en-us/
   # ext_lowlevel       = https://docs.typo3.org/c/typo3/cms-lowlevel/main/en-us/
   # ext_recycler       = https://docs.typo3.org/c/typo3/cms-recycler/main/en-us/
   # ext_redirects      = https://docs.typo3.org/c/typo3/cms-redirects/main/en-us/
   # ext_rte_ckeditor   = https://docs.typo3.org/c/typo3/cms-rte-ckeditor/main/en-us/
   # ext_scheduler      = https://docs.typo3.org/c/typo3/cms-scheduler/main/en-us/
   # ext_seo            = https://docs.typo3.org/c/typo3/cms-seo/main/en-us/
   # ext_workspaces     = https://docs.typo3.org/c/typo3/cms-workspaces/main/en-us/

The placeholders of pattern `<name>` must be replaced manually by the author of
the documentation, and commented or set empty if not required.

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

*  `<major>.<minor>`, e.g. "11.5", or
*  `<major>.<minor>.<fix>`, e.g. "11.5.1", or
*  `main (development)`.

For the release switch entries, only the major and minor versions are
considered.


.. _settings-cfg-copyright:

Copyright
^^^^^^^^^

The *copyright* property contains the copyright claim of the project. It is
displayed in the footer as "© Copyright <copyright>" and has in most use cases
of the TYPO3 world the values:

#. `since <creation-year> by the TYPO3 contributors`,
   e.g. "since 1999 by the TYPO3 contributors" (official TYPO3 manuals and TYPO3
   system extensions)
#. `since <creation-year> by <vendor> & contributors`,
   e.g. "since 1999 by dkd & contributors" (third-party TYPO3 extensions)


.. _settings-cfg-github-workflow:

GitHub workflow
^^^^^^^^^^^^^^^

The *github_repository* and *github_branch* properties must be set to provide
the "Edit on GitHub" button, which allows the reader to jump from the currently
viewed documentation directly to the associated GitHub repository and edit the
page file.

If the project is hosted on GitHub and public contributions are desired, these
properties should be set accordingly:

1. `<user>/<repository>`, for example to "TYPO3-Documentation/TYPO3CMS-Reference-TCA"
   or "FriendsOfTYPO3/extension_builder".
2. `<branch>`, for example on "main" or "10.x".


.. _settings-cfg-footer-links:

Footer links
^^^^^^^^^^^^

The *project_<topic>* properties provide all links with the name "<Topic>" in
the footer of the documentation that guide the user to other aspects of the
project than the documentation, for example to the project page in the TER:

*  *project_home* is set to the homepage URL of the project. For official TYPO3
   manuals this is the public base URL at docs.typo3.org, for public TYPO3
   extensions this is the associated TER page or a custom project website, for
   example

   *  "\https://docs.typo3.org/m/typo3/reference-coreapi/main/en-us/" or
   *  "\https://extensions.typo3.org/extension/news".

*  *project_contact* is usually set to an email address or Slack channel URL of
   the team behind the project, for example

   *  "\mailto:documentation\@typo3.org" or
   *  "\https://typo3.slack.com/archives/C028JEPJL".

*  *project_repository* is set to the repository of the project's VCS, for
   example

   *  "\https://github.com/FriendsOfTYPO3/extension_builder".

*  *project_issues* is set to the location where project issues are to be
   created and edited, for example

   *  "\https://github.com/FriendsOfTYPO3/extension_builder/issues".

*  *project_discussions* is used in the rare case that project-related
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

.. code-block:: rst

   :doc:`t3start:Extensions/Management`

and the fragment :samp:`#install-extension-with-composer` on the same page with

.. code-block:: rst

   :ref:`t3start:install-extension-with-composer`

The prerequisite is that the target manual is also compiled with Sphinx and
provides an objects.inv file in the root of the documentation that
contains all reference targets. Since this file is binary, the rendering
toolchain provides a twin objects.inv.json file that allows the reader
to easily look up reference targets. An example of this is this
`production objects.inv.json <https://docs.typo3.org/m/typo3/tutorial-getting-started/main/en-us/objects.inv.json>`__.

If a target reference becomes unavailable during documentation rendering, for
example if it has been permanently removed, a warning is issued and stored in
the toolchain log file at :file:`Documentation-GENERATED-temp/Result/project/0.0.0/_buildinfo/warnings.txt`.


.. index:: Single file documentation
.. _single-file-documentation:

Single file documentation
=========================

This setup is not recommended, but can be handy for those who want to publish
their documentation on docs.typo3.org and want to keep their mono README.rst
documentation style for now.

This structure allows the author to minimize effort by maintaining a single
documentation file that is interpreted simultaneously by the VCS host
and the Sphinx theme. On the other hand, the author only has
the reduced set of content elements supported by the former, rather than using
the theme's rich selection of :ref:`custom content elements <rest-reference>`.

Of course, you can also use a README.md instead of a README.rst file if you
prefer its syntax.

.. code-block:: none

   .
   ├── README.rst
   └── Documentation
       └── Settings.cfg


.. _single-file-documentation-readme-rst:

README.rst
----------

For single file documentation, the README.rst contains the entire documentation.
This should also contain links to all aspects of the project to guide the reader
to the next steps, for example

.. code-block:: rst

   <badges>

   =========
   <project>
   =========

   <abstract>

   Installation
   ============
   ..

   Configuration
   =============
   ..

   Usage
   =====
   ..

   :Repository:  https://<vcs-repository>
   :Read online: https://docs.typo3.org/p/<package-name>/main/en-us/
   :TER: https://extensions.typo3.org/extension/<extension-key>/

or as README.md alternatively:

.. code-block:: md

   <badges>

   # <project>

   <abstract>

   ## Installation
   ..

   ## Configuration
   ..

   ## Usage
   ..

   |                  | URL                                                           |
   |------------------|---------------------------------------------------------------|
   | **Repository:**  | https://<vcs-repository>                                      |
   | **Read online:** | https://docs.typo3.org/p/<package-name>/main/en-us/           |
   | **TER:**         | https://extensions.typo3.org/extension/<extension-key>/       |

For more details, see the explanation of :ref:`README.rst <readme-rst>` in the
full documentation section.


.. _single-file-documentation-settings-cfg:

Documentation/Settings.cfg
--------------------------

This file contains the configuration for the Sphinx theme. See the explanation
of :ref:`Settings.cfg <settings-cfg>` in the full documentation section for more
details.

.. note::

   You can reduce the single file documentation even further by omitting the
   Settings.cfg - which is even less recommended, but works. All Sphinx
   theme variables will then fall back to their default values, e.g. the project
   title will then be "The Project's Title" and the release version "0.0.0".


.. _examples:

Examples
========

These are some good examples of TYPO3 full and single file documentation in the
wild.


.. _examples-official-typo3-manuals:

Official TYPO3 manuals
----------------------

.. table::
   :widths: 25, 75

   =========================  ==================================================
   Project                    Links
   =========================  ==================================================
   TSconfig Reference (full)  `README.rst <https://github.com/TYPO3-Documentation/TYPO3CMS-Reference-TSconfig>`__ |
                              `Settings.cfg <https://github.com/TYPO3-Documentation/TYPO3CMS-Reference-TSconfig/blob/main/Documentation/Settings.cfg>`__ |
                              `Index.rst <https://github.com/TYPO3-Documentation/TYPO3CMS-Reference-TSconfig/blob/main/Documentation/Index.rst>`__ |
                              `Includes.rst.txt <https://github.com/TYPO3-Documentation/TYPO3CMS-Reference-TSconfig/blob/main/Documentation/Includes.rst.txt>`__ |
                              `Read online <https://docs.typo3.org/m/typo3/reference-tsconfig/main/en-us/>`__
   =========================  ==================================================


.. _examples-typo3-system-extension-documentation:

TYPO3 system extension documentation
------------------------------------

.. table::
   :widths: 25, 75

   ===========================  ================================================
   Project                      Links
   ===========================  ================================================
   Import / Export (full)       `README.rst <https://github.com/TYPO3/typo3/tree/main/typo3/sysext/impexp>`__ |
                                `Settings.cfg <https://github.com/TYPO3/typo3/blob/main/typo3/sysext/impexp/Documentation/Settings.cfg>`__ |
                                `Index.rst <https://github.com/TYPO3/typo3/blob/main/typo3/sysext/impexp/Documentation/Index.rst>`__ |
                                `Includes.rst.txt <https://github.com/TYPO3/typo3/blob/main/typo3/sysext/impexp/Documentation/Includes.rst.txt>`__ |
                                `Read online <https://docs.typo3.org/c/typo3/cms-impexp/main/en-us/>`__
   ===========================  ================================================


.. _examples-typo3-third-party-extension-documentation:

TYPO3 third-party extension documentation
-----------------------------------------

.. table::
   :widths: 25, 75

   ========================  ===================================================
   Project                   Links
   ========================  ===================================================
   Extension Builder (full)  `README.rst <https://github.com/FriendsOfTYPO3/extension_builder>`__ |
                             `Settings.cfg <https://github.com/FriendsOfTYPO3/extension_builder/blob/master/Documentation/Settings.cfg>`__ |
                             `Index.rst <https://github.com/FriendsOfTYPO3/extension_builder/blob/master/Documentation/Index.rst>`__ |
                             `Includes.rst.txt <https://github.com/FriendsOfTYPO3/extension_builder/blob/master/Documentation/Includes.rst.txt>`__ |
                             `Read online <https://docs.typo3.org/p/friendsoftypo3/extension-builder/main/en-us/>`__
   ------------------------  ---------------------------------------------------
   Make (single)             `README.md <https://github.com/b13/make>`__ |
                             `Settings.cfg <https://github.com/b13/make/blob/main/Documentation/Settings.cfg>`__ |
                             `Read online <https://docs.typo3.org/p/b13/make/main/en-us/>`__
   ========================  ===================================================


.. _examples-php-application-documentation:

PHP application documentation
-----------------------------

.. table::
   :widths: 25, 75

   ==================  =========================================================
   Project             Links
   ==================  =========================================================
   Surf (full)         `README.md <https://github.com/TYPO3/Surf>`__ |
                       `Settings.cfg <https://github.com/TYPO3/Surf/blob/master/Documentation/Settings.cfg>`__ |
                       `Index.rst <https://github.com/TYPO3/Surf/blob/master/Documentation/Index.rst>`__ |
                       `Includes.txt <https://github.com/TYPO3/Surf/blob/master/Documentation/Includes.txt>`__ |
                       `Read online <https://docs.typo3.org/other/typo3/surf/main/en-us/>`__
   ------------------  ---------------------------------------------------------
   Tailor (single)     `README.md <https://github.com/TYPO3/tailor>`__ |
                       `Read online <https://docs.typo3.org/other/typo3/tailor/main/en-us/>`__
   ==================  =========================================================

.. seealso::

   Although it is possible to write every single line of a full documentation
   from scratch, the TYPO3 community provides tools to support you:

   *  A `sample manual <https://github.com/TYPO3-Documentation/TYPO3CMS-Example-ExtensionManual>`__
      is available to be immediately copied into your own extension.
   *  The `Extension Builder <https://extensions.typo3.org/extension/extension_builder>`__
      optionally generates a sample documentation together with the extension
      skeleton.
   *  TYPO3 Core developers use the `ReST Helper <https://forger.typo3.com/utilities/rst>`__
      to kickoff a new TYPO3 changelog entry.
