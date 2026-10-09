..  include:: /Includes.rst.txt
..  index::
    reST; confval
    reST; Configuration values
..  _rest-confval:

==============================
Configuration values (confval)
==============================

The :rst:`confval` directive can be used to document configuration values
in a structured way, independent of the programming language.
In a TYPO3 context, it can be used to document configuration values
stored in PHP arrays (TCA, global configuration variables),
TypoScript (TypoScript setup, TSconfig), XML (FlexForms, XLIFF) and
YAML (SiteConfiguration, EXT:form).

Using the :rst:`confval` directive has several benefits:

*   The display is independent of the language of the configuration value
    – for example, unlike :ref:`PHP domain <rest-phpdomain>`.
*   You can link directly to configuration values.
*   The content element presents the data and its attributes in a
    well-structured way.

Each configuration value name may only be used once. In large references
with different contexts you can define individual configuration schemas for
each context.

..  contents:: Table of contents

..  _rest-confval-examples:

Examples
========

..  _rest-confval-examples-required-configuration-value:

Required configuration value
----------------------------

..  confval:: label
    :name: some-unique-label
    :required: true
    :type: string or LLL reference

    The name of the field as shown in the form.

..  code-block:: rst

    ..  confval:: label
        :name: some-unique-label
        :required: true
        :type: string or LLL reference

        The name of the field as shown in the form.

..  _rest-confval-examples-example-configuration-value:

Example: configuration value with default value and custom parameter
--------------------------------------------------------------------

..  confval:: fileCreateMask
    :name: some-unique-fileCreateMask
    :type: text
    :default: 0664
    :Path: :php:`$GLOBALS['TYPO3_CONF_VARS']['SYS']['fileCreateMask']`

    File mode mask for Unix file systems (when files are uploaded/created).

..  code-block:: rst

    ..  confval:: fileCreateMask
        :name: some-unique-fileCreateMask
        :type: text
        :default: 0664
        :Path: :php:`$GLOBALS['TYPO3_CONF_VARS']['SYS']['fileCreateMask']`

        File mode mask for Unix file systems (when files are uploaded/created).

..  _rest-confval-confval-directive-api:

Confval directive API
=====================

Each confval must have at least a title. If that title is not unique within
the manual the confval must also have the `:name:` attribute, followed by a
unique name. Names are case-insensitive and convert all special signs into a dash.

..  code-block:: rst

    ..  confval:: [title]
        :name: [unique-name]

There are several reserved attributes:

`:type:`
    The type of the configuration value.
`:default:`
    The default value
`:required:`
    Is the configuration value required.
`:name:`
    The unique identifier, reserved internally by reStructuredText.
`:class:`
    Reserved internally by reStructuredText.
`noindex`
    Exclude from being able to be referenced and form indexes. Useful for
    confvals that should be repeatedly displayed in different locations.
`:added:`, `:changed:`, `:deprecated:`, `:removed:`
    The version in which the configuration value was added, changed,
    deprecated, or removed. See
    `Versions of a configuration value <https://docs.typo3.org/permalink/h2document:rest-confval-versions>`_.
`:parent:`
    The `:name:` of the configuration value that this one is a property
    of. The box of the configuration value does not show it. See
    `Properties of another configuration value <https://docs.typo3.org/permalink/h2document:rest-confval-parent>`_.

All other attributes are output the way they are written:

..  confval:: someSetting
    :name: some-unique-someSetting
    :type: string
    :Path: :php:`$GLOBALS['TYPO3_CONF_VARS']['SYS']['someSetting']`
    :Some value: Lorem Ipsum

    Lorem Ipsum Dolor sit

..  code-block:: rst

    ..  confval:: fileCreateMask
        :name: some-unique-someSetting
        :type: string
        :default: 0664
        :Path: :php:`$GLOBALS['TYPO3_CONF_VARS']['SYS']['fileCreateMask']`

        Lorem Ipsum Dolor sit

..  _rest-confval-versions:

Versions of a configuration value
=================================

Use the options :rst:`:added:`, :rst:`:changed:`, :rst:`:deprecated:`, and
:rst:`:removed:` to say in which version a configuration value was added,
changed, deprecated, or removed. Each option takes a version, such as
`14.0`. Optionally, put the changelog entry after the version, separated by
a space:

..  code-block:: rst

    ..  confval:: showSubmoduleOverview
        :name: backend-module-showSubmoduleOverview
        :type: bool
        :default: false
        :added: 14.0 feature-107712-1760548718

        If true and if a module has submodules, the submodules that the
        backend user has access to are displayed as a set of cards.

..  confval:: showSubmoduleOverview
    :name: backend-module-showSubmoduleOverview
    :type: bool
    :default: false
    :added: 14.0 feature-107712-1760548718

    If true and if a module has submodules, the submodules that the
    backend user has access to are displayed as a set of cards.

Each option shows as a row in the list of fields of the configuration value.
The changelog entry shows as a link, with the title of the entry as the link
text. The changelog entry takes the same values as the option
`:changelog: of a version directive <https://docs.typo3.org/permalink/h2document:rest-versions-changelog-option>`_.

Inside a :rst:`confval`, use these options instead of a
`version directive <https://docs.typo3.org/permalink/h2document:rest-versions>`_.
The index of the configuration values reads the options, but it cannot read
a directive in the description.
A version directive with text that is tied to the version transition, such
as how to migrate, can stay in the description.

A configuration value whose default changed, with a directive that says what
the default was before. This text becomes obsolete once the directive is
pruned, so it stays in the directive:

..  code-block:: rst

    ..  confval:: cache_period
        :name: config-cache-period
        :type: integer
        :default: `31536000` *(= 365 days)*

        ..  versionchanged:: 14.3.1
            The default was raised from `86400` (24 hours) to `31536000`
            (365 days). TYPO3 v14.3.0 and TYPO3 v13.4 and below use `86400`.

        The number of seconds a page can remain in the cache.

..  confval:: cache_period
    :name: config-cache-period
    :type: integer
    :default: `31536000` *(= 365 days)*

    ..  versionchanged:: 14.3.1
        The default was raised from `86400` (24 hours) to `31536000`
        (365 days). TYPO3 v14.3.0 and TYPO3 v13.4 and below use `86400`.

    The number of seconds a page can remain in the cache.

A configuration value that was removed is no longer described with the
options that are still in use. Move its :rst:`confval` to the page that
collects removed content, often the page shown for a link that is not found,
and say there when it was removed:

..  code-block:: rst

    ..  confval:: maxDBListItems
        :name: maxDBListItems
        :type: integer
        :removed: 14.0

        Use the page TSconfig option `mod.web_list.itemsLimitSingleTable`
        instead.

..  confval:: maxDBListItems
    :name: maxDBListItems
    :type: integer
    :removed: 14.0

    Use the page TSconfig option `mod.web_list.itemsLimitSingleTable`
    instead.

If the value of an option does not start with a version, or the changelog
entry does not exist, the rendering shows a warning.

..  _rest-confval-confval-menu:

Confval menu
============

Confval entries can be listed in a special menu type, the confval-menu directive.

If you put the directive somewhere on the page it will list all confvals that
can be found on that page:

..  confval-menu::
    :name: confval-group-1
    :display: table
    :type:
    :default:
    :exclude: confval-1, confval-2

..  code-block:: rst

    ..  confval-menu::
        :name: confval-group-1
        :display: table
        :type:
        :default:
        :exclude: confval-1, confval-2


If you use a confval menu together with nested confvals it will only list
its child confvals. This is useful if you have several groups of confvals on
the same page and want to list them in separate menus:

..  confval-menu::
    :name: confval-group-2
    :display: table
    :type:

    ..  confval:: confval-1
        :type: string

        Some Description

    ..  confval:: confval-2
        :type: string
        :default: 'Hello World'

        Some Description

..  code-block:: rst

    ..  confval-menu::
        :name: confval-group-2
        :display: table
        :type:

        ..  confval:: confval-1
            :type: string

            Some Description

        ..  confval:: confval-2
            :type: int
            :default: 'Hello World'

            Some Description

..  _rest-confval-parent:

Properties of another configuration value
=========================================

A configuration value can be a property of another one, for example the
properties of the content object `TEXT` in the TypoScript reference. If you
nest the confvals of the properties inside the confval of the object, they
show as rubrics inside one large box.

To keep each property under its own headline, set the option :rst:`:parent:`
on the confval menu that lists the properties. Write the `:name:` of the
parent confval, as in :rst:`:exclude:`:

..  code-block:: rst

    ..  confval-menu::
        :display: table
        :parent: cobj-text
        :type:

Every confval that the menu lists becomes a property of the confval
`cobj-text`. The index of the configuration values, :file:`confvals.json`,
contains `"parent": "confval-cobj-text"` for each of them.

The menu does not list the parent confval itself. A page that documents an
object and its properties side by side needs no :rst:`:exclude:` for the
confval of the object.

A second object on the same page is different. For example, the page of
`USER` also documents `USER_INT`, and the menu lists it as a property of
`USER`. Exclude its confval with :rst:`:exclude:`.

A single confval can name its parent with its own option :rst:`:parent:`:

..  code-block:: rst

    ..  confval:: value
        :name: text-value
        :parent: cobj-text
        :type: string

        Text, which you want to output.

If more than one source names a parent, the first of these wins:

#.  The confval in which the confval is nested.
#.  The option :rst:`:parent:` of the confval itself.
#.  The option :rst:`:parent:` of the confval menu that lists it.

If two confval menus with different parents list the same confval, it keeps
the parent of the first menu, and the rendering shows a warning.

..  _rest-confval-confval-menu-directive:

Confval-menu directive API
==========================

The confval-menu directive has the following options:

`:display:`
    `table`, `list`, `tree`: Different display forms, try them out
`:name:`
    A unique identifier for the confval menu for the "to top" button
`:class:`
    Reserved by reStructuredText
`:exclude-noindex:`
    Exclude all confvals that have the option `:noindex:`.
`:exclude:`
    Comma separated list of all identifiers / titles of convals to be excluded.
`:parent:`
    The `:name:` of a confval. Every confval that the menu lists becomes a
    property of it, and the menu does not list the confval itself. See
    `Properties of another configuration value <https://docs.typo3.org/permalink/h2document:rest-confval-parent>`_.

All other parameters can be used to trigger listing of the property of the exact
same name.
