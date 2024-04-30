..  include:: /Includes.rst.txt
..  index::
    reST; Directory tree
..  _writing-rest-directory-tree:

==============
Directory tree
==============

You can use the directive `.. directory-tree:: ` to make a nested list look like
an expandable directory tree. This is helpful in discussing file structure for
extensions or projects.

..  _writing-rest-directory-tree-example-basic:

Example: A basic directory tree, two levels expanded
=====================================================

..  directory-tree::
    :level: 2
    :show-file-icons: true

    *   EXT:my_sitepackage/Resources/Private/Templates/

        *   Layouts

            *   Default.html
            *   WithoutHeader.html

        *   Pages

            *   Default.html
            *   StartPage.html
            *   TwoColumns.html
            *   With_sidebar.html

        *   Partials

            *   Footer.html
            *   Sidebar.html
            *   Menu.html

..  code-block:: rst
    :caption: EXT:my_extension/Documentation/SomeDocument.rst

    ..  directory-tree::
        :level: 2
        :show-file-icons: true

        *   EXT:my_sitepackage/Resources/Private/Templates/

            *   Layouts

                *   Default.html
                *   WithoutHeader.html

            *   Pages

                *   Default.html
                *   StartPage.html
                *   TwoColumns.html
                *   With_sidebar.html

            *   Partials

                *   Footer.html
                *   Sidebar.html
                *   Menu.html


..  _writing-rest-directory-tree-example-empty-folders:

Example: A page tree with empty folders
=======================================

..  directory-tree::

    *   :path:`Classes`
    *   :path:`Configuration`

        *   :path:`Backend`
        *   :path:`Extbase`

            *   :path:`Persistence`

        *   :path:`TCA`
        *   :path:`TsConfig`
        *   :path:`TypoScript`
        *   :file:`Icons.php`
        *   :file:`page.tsconfig`
        *   :file:`Services.yaml`
        *   :file:`user.tsconfig`

    *   :path:`Documentation`
    *   :path:`Resources`

        *   :path:`Private`

            *   :path:`Language`

        *   :path:`Public`

    *   :path:`Tests`
    *   :file:`composer.json`
    *   :file:`ext_emconf.php`
    *   :file:`ext_localconf.php`
    *   :file:`ext_tables.sql`

..  code-block:: rst
    :caption: EXT:my_extension/Documentation/SomeDocument.rst

    ..  directory-tree::

        *   :path:`Classes`
        *   :path:`Configuration`

            *   :path:`Backend`
            *   :path:`Extbase`

                *   :path:`Persistence`

            *   :path:`TCA`
            *   :path:`TsConfig`
            *   :path:`TypoScript`
            *   :file:`Icons.php`
            *   :file:`page.tsconfig`
            *   :file:`Services.yaml`
            *   :file:`user.tsconfig`

        *   :path:`Documentation`
        *   :path:`Resources`

            *   :path:`Private`

                *   :path:`Language`

            *   :path:`Public`

        *   :path:`Tests`
        *   :file:`composer.json`
        *   :file:`ext_emconf.php`
        *   :file:`ext_localconf.php`
        *   :file:`ext_tables.sql`

..  _writing-rest-directory-tree-properties:

Properties
==========

..  confval:: level
    :name: directory-tree-level
    :type: int
    :default: unlimited

    Limit the levels of the tree initially shown expanded.

..  confval:: show-file-icons
    :name: directory-tree-show-file-icons
    :type: bool
    :default: false

    Display a folder icon beside each entry that has a sub-entry, a file icon
    otherwise.
