:navigation-title: guides.xml

..  _guides-xml:

===========================================
Configuration of the rendering - guides.xml
===========================================

This XML file contains meta information and configuration used during rendering
of a manual.

..  rubric:: Example:

..  literalinclude:: _guides-simple.xml
    :caption: Documentation/guides.xml

..  hint::
    If you are migrating from the legacy Sphinx-based rendering and still have
    a :file:`Documentation/Settings.cfg` you can use an automatic migration
    tool to :ref:`migrate the Settings.cfg into a guides.xml <migrate_guides_xml>`

..  contents:: Table of Contents:
    :local:


..  confval-menu::
    :display: tree

    .. _settings-guides:

    ..  confval:: <guides>
        :name: guides

        The :xml:`<guides>` tag is the root tag of the :file:`Documentation/guides.xml`.
        It is used for general configuration during parsing and rendering.

        The following settings can be relevant for TYPO3 themed documentation:

        ..  _settings-guides-default-code-language:

        ..  confval:: default-code-language
            :name: guides-default-code-language
            :type: string

            Can be used to set the code-language that should be used for
            :ref:`code-blocks <codeblock-directive>` if no language is set.

            We advice to set the language to be used in each code-block however.

        ..  _settings-guides-default-code-language-example:

        ..  rubric:: Example: Use `typoscript` as default language for code-blocks

        ..  code-block:: xml
            :caption: EXT:my_extension/Documentation/guides.xml (excerpt)
            :emphasize-lines: 4

            <?xml version="1.0" encoding="UTF-8"?>
            <guides xmlns="https://www.phpdoc.org/guides" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                    xsi:schemaLocation="https://www.phpdoc.org/guides ../vendor/phpdocumentor/guides-cli/resources/schema/guides.xsd"
                    default-code-language="typoscript"
            >
                <!-- [...] -->
            </guides>

        ..  _settings-guides-max-menu-depth:

        ..  confval:: max-menu-depth
            :name: guides-max-menu-depth
            :type: integer
            :Default: `PHP_INT_MAX`

            Limits the main menu to a certain amount of levels. As level creation is
            one of the main bottle-necks that can slow down rendering it can be helpful
            to limit the levels in the menu in some use cases.

        ..  _settings-guides-max-menu-depth-example:

        ..  rubric:: Example: Limit the menu to 2 levels

        The changelog (documentation of the extension "core") consists of several thousands of
        pages. The reason is that very long lists of changelog entries in the menu are not helpful to
        the user and slow down the search.

        ..  code-block:: xml
            :caption: EXT:core/Documentation/guides.xml (excerpt)
            :emphasize-lines: 4

            <?xml version="1.0" encoding="UTF-8"?>
            <guides xmlns="https://www.phpdoc.org/guides" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                    xsi:schemaLocation="https://www.phpdoc.org/guides ../vendor/phpdocumentor/guides-cli/resources/schema/guides.xsd"
                    max-menu-depth="2"
            >
                <!-- [...] -->
            </guides>


    .. _settings-guides-interlink-mapping:

    ..  confval:: <inventory>
        :name: inventory

        The :xml:`<inventory>` tag is located directly in the :ref:`guides tag <settings-guides>`.
        There can be 0 or more :xml:`<inventory>` tags, each defines one Interlink
        inventory.

        A list of globally available Interlink (formerly "Intersphinx") repositories
        can be found in :ref:`Available default inventories <t3renderguides:available-default-inventories>`

        It is possible, though rarely needed to define custom interlink mappings:

        For example:

        ..  code-block:: xml
            :caption: Documentation/guides.xml, excerpt

            <inventory id="sphinx" url="https://www.sphinx-doc.org/en/master/"/>


    .. _settings-guides-project:

    ..  confval:: <project>
        :name: project

        The :xml:`<project>` tag is located directly in the :ref:`guides tag <settings-guides>`.
        There can be 0 or 1 tag of that name.

        This tag can contain the following meta information:

        .. _settings-guides-project-title:

        ..  confval:: title
            :name: guides-project-title
            :type: string

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

        .. _settings-guides-project-title-example:

        ..  rubric:: Example: Set the title of a project, including version, release and copyright

        ..  code-block:: xml
            :caption: EXT:news/Documentation/guides.xml (excerpt)

            <?xml version="1.0" encoding="UTF-8"?>
            <guides xmlns="https://www.phpdoc.org/guides" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                    xsi:schemaLocation="https://www.phpdoc.org/guides ../vendor/phpdocumentor/guides-cli/resources/schema/guides.xsd"
            >
                <project title="News system"
                         version="local"
                         copyright="since 2010 by Georg Ringer &amp; Contributors"
                />
            </guides>

        .. _settings-guides-version-and-release:

        ..  confval:: version
            :name: guides-project-version
            :type: string

            When documentation is rendered in the GitHub action for deployment onto
            https://docs.typo3.org **the version is set automatically** to the extension's
            version derived from the Git tag. Setting the version in the
            :file:`guides.xml` only affects local rendering.

        ..  confval:: release
            :name: guides-project-release
            :type: string

            You can set the `release` property to the release number of your
            document and output this value using :rst:`|release|` within
            your text if you desire to. Usually it is not used.

        .. _settings-guides-copyright:

        ..  confval:: copyright
            :name: guides-project-copyright
            :type: string

            The *copyright* attribute contains the copyright claim of the project. It is
            displayed in the footer as "© Copyright <copyright>" and has in most use cases
            in the TYPO3 world the values:

            #.  `since <creation-year> by the TYPO3 contributors`,
                for example "since 1999 by the TYPO3 contributors" (official TYPO3 manuals and TYPO3
                system extensions)
            #.  `since <creation-year> by <vendor> & contributors`,
                for example "since 1999 by John Doe & contributors" (third-party TYPO3 extensions)

    .. _settings-guides-theme:

    ..  confval:: <extension>
        :name: extension

        The :xml:`<extension>` tag is located directly in the :ref:`guides tag <settings-guides>`.

        TYPO3 Theme specific settings can be made in the tag
        :xml:`<extension class="\T3Docs\Typo3DocsTheme\DependencyInjection\Typo3DocsThemeExtension">`.

        There can be 0 or more tags of that name, however only one :xml:`<extension>` tag
        should be defined for the TYPO3 documentation theme.

        The class attribute is mandatory, it references the extension that is used
        to render the documentation with the TYPO3 documentation theme.

        .. _settings-guides-github-workflow:

        ..  confval:: edit-on-github-*
            :name: guides-extension-edit-on-github-workflow

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

        ..  _settings-guides-edit-on-github:

        ..  confval:: edit-on-github
            :name: guides-extension-edit-on-github
            :type: string
            :Sytanx: [GitHub Organiziation or user]/[Repository]
            :Default: `""`

            If this configuration is set, a button "Edit on GitHub" is displayed on each
            page of the manual.

        ..  _settings-guides-edit-on-github-example:

        ..  rubric:: Example: Display a button to edit in the repository of news

        ..  code-block:: xml
            :caption: EXT:news/Documentation/guides.xml (excerpt)

            <?xml version="1.0" encoding="UTF-8"?>
            <guides xmlns="https://www.phpdoc.org/guides" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                    xsi:schemaLocation="https://www.phpdoc.org/guides ../vendor/phpdocumentor/guides-cli/resources/schema/guides.xsd"
            >
                  <extension class="\T3Docs\Typo3DocsTheme\DependencyInjection\Typo3DocsThemeExtension"
                       edit-on-github-branch="main"
                       edit-on-github="georgringer/news"
            />
            </guides>

        ..  _settings-guides-edit-on-github-branch:

        ..  confval:: edit-on-github-branch
            :name: guides-extension-edit-on-github-branch
            :type: string
            :Default: `main`

            The branch that should be used for the "Edit on GitHub" button.


        ..  _settings-guides-edit-on-github-branch-example:

        ..  rubric:: Example: Display a button to edit in the repository of tt_news on branch master

        ..  code-block:: xml
            :caption: EXT:news/Documentation/guides.xml (excerpt)

            <?xml version="1.0" encoding="UTF-8"?>
            <guides xmlns="https://www.phpdoc.org/guides" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                    xsi:schemaLocation="https://www.phpdoc.org/guides ../vendor/phpdocumentor/guides-cli/resources/schema/guides.xsd"
            >
                <extension class="\T3Docs\Typo3DocsTheme\DependencyInjection\Typo3DocsThemeExtension"
                           edit-on-github-branch="master"
                           edit-on-github="FriendsOfTYPO3/tt_address"
                />
            </guides>


        ..  _settings-guides-edit-on-github-directory:

        ..  confval:: edit-on-github-directory
            :name: guides-extension-edit-on-github-directory
            :type: string
            :Default: `Documentation`

            The directory in which the documentation can be found. The GitHub render
            action currently does not support using other directories
            then :folder:`Documentation/`.

            This setting is used exclusively for system extension manuals as the TYPO3
            Core is kept in a mono repository on GitHub.

        ..  rubric:: Example: Set the GitHub directory for a system extension

        ..  code-block:: xml
            :caption: EXT:adminpanel/Documentation/guides.xml (excerpt)

            <?xml version="1.0" encoding="UTF-8"?>
            <guides xmlns="https://www.phpdoc.org/guides" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                    xsi:schemaLocation="https://www.phpdoc.org/guides ../vendor/phpdocumentor/guides-cli/resources/schema/guides.xsd"
            >
                <extension class="\T3Docs\Typo3DocsTheme\DependencyInjection\Typo3DocsThemeExtension"
                           edit-on-github-branch="main"
                           edit-on-github="typo3/typo3"
                           edit-on-github-directory="typo3/sysext/adminpanel/Documentation/"
                />
            </guides>

        .. _settings-guides-interlink-shortcode:

        ..  confval:: interlink-shortcode
            :name: guides-extension-interlink-shortcode
            :type: string
            :Default: `somemanual`

            The interlink shortcode will be displayed in the "Reference this headline"
            dialog when users click on the link symbol beside a headline or other
            linkable element.

            These references can be used to link to your manual from other documents
            rendered with the TYPO3 theme. However they will only work if you follow
            these rules:

            *   TYPO3 third-party extensions: Composer name, example: `georgringer/news`
            *   System extensions: Composer name, example: `typo3/cms-adminpanel`
            *   A shortcode supported by the theme:
                :ref:`Available default inventories <t3renderguides:available-default-inventories>`

        ..  figure:: /_Images/ReferenceThisHeadlineDialog.png
            :alt: Reference a headline dialog showing the shortcode georgringer/news

            Reference a headline in the EXT:news manual

        .. _settings-guides-project-links:

        ..  confval:: project_*
            :name: guides-extension-project-links

            The *project_<topic>* attributes provide all links with the name "<Topic>" in
            the footer of the documentation that guide the user to other aspects of the
            project than the documentation, for example to the project page in the
            TYPO3 Extension Repository (TER):

        .. _settings-guides-project_home:

        ..  confval:: project_home
            :name: guides-extension-project_home
            :type: string

            is set to the homepage URL of the project. For official TYPO3
            manuals this is the public base URL at docs.typo3.org, for public TYPO3
            extensions this is the associated TER page or a custom project website, for
            example

            *  `https://docs.typo3.org/m/typo3/reference-coreapi/main/en-us/` or
            *  `https://extensions.typo3.org/extension/news`.

        .. _settings-guides-project_contact:

        ..  confval:: project_contact
            :name: guides-extension-project-contact
            :type: string

            is usually set to an email address or Slack channel URL of
            the team behind the project, for example

            *  `mailto:documentation\@typo3.org` or
            *  `https://typo3.slack.com/archives/C028JEPJL`.

        .. _settings-guides-project_repository:

        ..  confval:: project_repository
            :name: guides-extension-project_repository
            :type: string

            is set to the repository of the project's VCS, for
            example

            *  `https://github.com/FriendsOfTYPO3/extension_builder`.

        .. _settings-guides-project_issues:

        ..  confval:: project_issues
            :name: guides-extension-project-issues
            :type: string

            is set to the location where project issues are to be
            created and edited, for example

            *  `https://github.com/FriendsOfTYPO3/extension_builder/issues`


        .. _settings-guides-project_discussions:

        ..  confval:: project_discussions
            :name: guides-extension-project-discussions
            :type: string

            is used in the rare case that project-related
            discussions take place in locations other than those defined by the
            project_contact and project_issues attributes, for example

            *  `https://github.com/FriendsOfTYPO3/extension_builder/discussions`.


        .. _settings-guides-project-links-example:

        ..  rubric:: Example: Project links for a third-party extension

        ..  code-block:: xml
            :caption: EXT:news/Documentation/guides.xml (excerpt)

            <?xml version="1.0" encoding="UTF-8"?>
            <guides xmlns="https://www.phpdoc.org/guides" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                    xsi:schemaLocation="https://www.phpdoc.org/guides ../vendor/phpdocumentor/guides-cli/resources/schema/guides.xsd"
            >
                <extension class="\T3Docs\Typo3DocsTheme\DependencyInjection\Typo3DocsThemeExtension"
                       project-home="https://extensions.typo3.org/extension/news/"
                       project-contact="https://typo3.slack.com/archives/C03TG7QJT"
                       project-repository="https://github.com/georgringer/news"
                       project-issues="https://github.com/georgringer/news/issues"
            />
            </guides>

        .. _settings-guides-project-links-core-example:

        ..  rubric:: Example: Project links for a system extension

        ..  code-block:: xml
            :caption: EXT:adminpanel/Documentation/guides.xml (excerpt)

            <?xml version="1.0" encoding="UTF-8"?>
            <guides xmlns="https://www.phpdoc.org/guides" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                    xsi:schemaLocation="https://www.phpdoc.org/guides ../vendor/phpdocumentor/guides-cli/resources/schema/guides.xsd"
                >
                <extension class="\T3Docs\Typo3DocsTheme\DependencyInjection\Typo3DocsThemeExtension"
                           project-home="https://extensions.typo3.org/extension/adminpanel/"
                           project-contact="https://typo3.slack.com/archives/C025BQLFA"
                           project-repository="https://github.com/typo3/typo3"
                           project-issues="https://forge.typo3.org/projects/typo3cms-core/issues"
                />
            </guides>


        .. _settings-guides-project-links-reference-example:

        ..  rubric:: Example: Project links for a reference or guide

        ..  code-block:: xml
            :caption: Reference-TSconfig Documentation/guides.xml (excerpt)

            <?xml version="1.0" encoding="UTF-8"?>
            <guides xmlns="https://www.phpdoc.org/guides" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                    xsi:schemaLocation="https://www.phpdoc.org/guides ../vendor/phpdocumentor/guides-cli/resources/schema/guides.xsd"
                 >
                <extension class="\T3Docs\Typo3DocsTheme\DependencyInjection\Typo3DocsThemeExtension"
                           project-home="https://docs.typo3.org/m/typo3/reference-tsconfig/main/en-us/"
                           project-contact="https://typo3.slack.com/archives/C028JEPJL"
                           project-repository="https://github.com/TYPO3-Documentation/TYPO3CMS-Reference-TSconfig"
                           project-issues="https://github.com/TYPO3-Documentation/TYPO3CMS-Reference-TSconfig/issues"
                />
            </guides>


        ..  _settings-guides-preferred_typo3_version:

        ..  confval:: typo3-core-preferred
            :name: guides-extension-typo3-core-preferred
            :type: string
            :Default: `stable`

            You can set the preferred TYPO3 Core version. This version is used to determine
            the desired version for links to other manuals and system extensions.

            ..  code-block:: xml
                :caption: Documentation/guides.xml

                <extension class="\T3Docs\Typo3DocsTheme\DependencyInjection\Typo3DocsThemeExtension"
                           typo3-core-preferred="stable" />

            If no preferred version is set it defaults to `stable`. Possible values are:

            `main`, `stable` (latest LTS), `oldstable` (old LTS) or an explicit LTS / eLTS
            version like `12.4` or `8.7`.

        ..  rubric:: Example: Set the preferred TYPO3 Core version to 11.5

        At the time of writing the extension :t3ext:`news` is compatible with TYPO3 v11.5
        and v12.4. When :ref:`referencing <cheat-sheet-intersphinx>` Core manuals or
        extensions, we want the links to go automatically to version 11.5 of that
        reference or core extension. Therefore we set the preferred TYPO3 Core version
        to that value:

        ..  code-block:: xml
            :caption: EXT:news/Documentation/guides.xml (excerpt)

            <?xml version="1.0" encoding="UTF-8"?>
            <guides xmlns="https://www.phpdoc.org/guides" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                    xsi:schemaLocation="https://www.phpdoc.org/guides ../vendor/phpdocumentor/guides-cli/resources/schema/guides.xsd"
            >
                 <extension class="\T3Docs\Typo3DocsTheme\DependencyInjection\Typo3DocsThemeExtension"
                       typo3-core-preferred="11.5"
            </guides>

        ..  rubric:: Example: Always link to the latest stable TYPO3 version

        If you want your links to always go to the latest stable long time support version
        (LTS) of the TYPO3 Core, you can set :confval:`guides-extension-typo3-core-preferred` to stable.

        At the time of writing references to official manuals and Core extensions will
        be rendered to version 12.4. Once TYPO3 13 LTS is released they will automatically
        switch to the according version on next re-rendering.

        ..  code-block:: xml
            :caption: EXT:my_extension/Documentation/guides.xml (excerpt)

            <?xml version="1.0" encoding="UTF-8"?>
            <guides xmlns="https://www.phpdoc.org/guides" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                    xsi:schemaLocation="https://www.phpdoc.org/guides ../vendor/phpdocumentor/guides-cli/resources/schema/guides.xsd"
            >
                 <extension class="\T3Docs\Typo3DocsTheme\DependencyInjection\Typo3DocsThemeExtension"
                       typo3-core-preferred="stable"
            </guides>

