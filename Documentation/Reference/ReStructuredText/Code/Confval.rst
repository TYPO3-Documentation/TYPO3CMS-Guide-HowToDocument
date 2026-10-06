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

    ..  confval:: is_static
        :name: ctrl-is-static
        :type: boolean
        :removed: 14.0 breaking-106863-1749629371

        Marks a table as one that holds static reference data.

..  confval:: is_static
    :name: ctrl-is-static
    :type: boolean
    :removed: 14.0 breaking-106863-1749629371

    Marks a table as one that holds static reference data.

Each option shows as a row in the list of fields of the configuration value.
The changelog entry shows as a link, with the title of the entry as the link
text. The changelog entry takes the same values as the option
`:changelog: of a version directive <https://docs.typo3.org/permalink/h2document:rest-versions-changelog-option>`_.

Inside a :rst:`confval`, use these options instead of a
`version directive <https://docs.typo3.org/permalink/h2document:rest-versions>`_.
The index of the configuration values reads the options, but it cannot read
a directive in the description.

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

All other parameters can be used to trigger listing of the property of the exact
same name.
