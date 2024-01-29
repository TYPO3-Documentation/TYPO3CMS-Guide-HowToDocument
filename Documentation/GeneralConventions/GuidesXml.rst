..  _guides-xml:

================================
:file:`Documentation/guides.xml`
================================

This XML file contains meta information and configuration used during rendering
of a manual.

Example:

..  literalinclude:: _guides-simple.xml
    :caption: Documentation/guides.xml

..  hint::
    If you are migrating from the legacy Sphinx-based rendering and still have
    a :file:`Documentation/Settings.cfg` you can use an automatic migration
    tool to :ref:`migrate the settings.cfg into a guides.xml <migrate_guides_xml>

.. _settings-guides:

The `<guides>` tag
==================

It is used for general configuration during parsing and rendering.

.. _settings-guides-project:

The `<project>` tag
===================

This tag can contain the following meta information:

Project title
-------------

The *project* tag contains the title of the project and is displayed in the
left sidebar (desktop) or the top (mobile) of the theme and in the title meta
tag.

For TYPO3 extensions we suggest to use the extension name in a readable
format:

*   Import / Export tool
*   News
*   Mask

Common values are in the official TYPO3 manuals

#. `<Topic> Guide`, e.g. "Frontend Localization Guide",
   for collections of articles on a specific topic
#. `<Topic> Reference`, e.g. "TSconfig Reference",
   for a complete reference
#. `<Topic> Tutorial`, e.g. "Editors Tutorial",
   for collections of tutorials on a specific topic

.. _settings-guides-version-and-release:

Version and release
-------------------

The attributes *version* and *release* both contain the version of the manual
and mostly correspond to the version of the TYPO3 LTS or TYPO3 extension to
which the documentation refers.

The version is shown below the title in the theme's release switch and in the
title meta tag, the release is not shown currently  - but it should be
kept anyway to satisfy internal requirements.

version
    The major project version, used as the replacement for :rst:`|version|`.
    For example this may be something like 12.4.

release
    The full project version, used as the replacement for :rst:`|release|`
    For example 13.0.0-dev.

If you do not need the separation provided between version and release,
just set them both to the same value.

.. _settings-guides-copyright:

Copyright
---------

The *copyright* attribute contains the copyright claim of the project. It is
displayed in the footer as "© Copyright <copyright>" and has in most use cases
in the TYPO3 world the values:

#.  `since <creation-year> by the TYPO3 contributors`,
    for example "since 1999 by the TYPO3 contributors" (official TYPO3 manuals and TYPO3
    system extensions)
#.  `since <creation-year> by <vendor> & contributors`,
    for example "since 1999 by John Doe & contributors" (third-party TYPO3 extensions)

.. _settings-guides-theme:

TYPO3 Theme settings
====================

Further settings can be made in the XML tag
:xml:`<extension class="\T3Docs\Typo3DocsTheme\DependencyInjection\Typo3DocsThemeExtension">`.
The class attribute is mandatory, it references the extension that is used
to render the documentation with the TYPO3 documentation theme.

..  _preferred_typo3_version:

Preferred TYPO3 Core version
----------------------------

You can set the preferred TYPO3 Core version. This version is used to determine
the desired version for links to other manuals and system extensions.

..  code-block:: xml
    :caption: Documentation/guides.xml

    <extension class="\T3Docs\Typo3DocsTheme\DependencyInjection\Typo3DocsThemeExtension"
               typo3-core-preferred="12.4" />

If no preferred version is set it defaults to `stable`. Possible values are:

`main`, `stable` (latest LTS), `oldstable` (old LTS) or an explicit LTS / eLTS
version like `12.4` or `8.7`.

..  todo: Link to interlink chapter once it is written

.. _settings-guides-github-workflow:

Configure the "Edit on GitHub" button
-------------------------------------

The *github_repository* and *github_branch* attributes should be set to provide
the "Edit on GitHub" button, which allows the reader to jump from the currently
viewed documentation directly to the associated GitHub repository and edit the
page file.

If the project is hosted on GitHub and public contributions are welcome, these
attributes should be set accordingly:

1.  `<user>/<repository>`, for example to "TYPO3-Documentation/TYPO3CMS-Reference-TCA"
    or "FriendsOfTYPO3/extension_builder".
2.  `<branch>`, for example on "main" or "10.x".

For example:

..  code-block:: xml
    :caption: Documentation/guides.xml, excerpt

    <extension class="\T3Docs\Typo3DocsTheme\DependencyInjection\Typo3DocsThemeExtension"
               edit-on-github-branch="main"
               edit-on-github="TYPO3-Documentation/TYPO3CMS-Guide-HowToDocument"
    />


.. _settings-guides-footer-links:

Footer links
------------

The *project_<topic>* attributes provide all links with the name "<Topic>" in
the footer of the documentation that guide the user to other aspects of the
project than the documentation, for example to the project page in the
TYPO3 Extension Repository (TER):

project_home
    is set to the homepage URL of the project. For official TYPO3
    manuals this is the public base URL at docs.typo3.org, for public TYPO3
    extensions this is the associated TER page or a custom project website, for
    example

    *  `https://docs.typo3.org/m/typo3/reference-coreapi/main/en-us/` or
    *  `https://extensions.typo3.org/extension/news`.

project_contact
    is usually set to an email address or Slack channel URL of
    the team behind the project, for example

    *  `mailto:documentation\@typo3.org` or
    *  `https://typo3.slack.com/archives/C028JEPJL`.

project_repository
    is set to the repository of the project's VCS, for
    example

    *  `https://github.com/FriendsOfTYPO3/extension_builder`.

project_issues
    is set to the location where project issues are to be
    created and edited, for example

    *  `https://github.com/FriendsOfTYPO3/extension_builder/issues`

project_discussions
    is used in the rare case that project-related
    discussions take place in locations other than those defined by the
    project_contact and project_issues attributes, for example

    *  `https://github.com/FriendsOfTYPO3/extension_builder/discussions`.

For example:

..  code-block:: xml
    :caption: Documentation/guides.xml, excerpt

    <extension class="\T3Docs\Typo3DocsTheme\DependencyInjection\Typo3DocsThemeExtension"
       project-home="https://docs.typo3.org/m/typo3/docs-how-to-document/main/en-us/"
       project-contact="https://typo3.slack.com/archives/C028JEPJL"
       project-repository="https://github.com/TYPO3-Documentation/TYPO3CMS-Guide-HowToDocument"
       project-issues="https://github.com/TYPO3-Documentation/TYPO3CMS-Guide-HowToDocument/issues"
    />

.. _settings-guides-interlink-mapping:

Interlink mapping
=================

.. todo: describe interlink mapping more detailed

It is possible, though rarely needed to define custom interlink mappings:

For example:

..  code-block:: xml
    :caption: Documentation/guides.xml, excerpt

    <inventory id="sphinx" url="https://www.sphinx-doc.org/en/master/"/>
