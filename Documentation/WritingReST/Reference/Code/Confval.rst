..  include:: /Includes.rst.txt
..  highlight:: rst
..  index::
    reST; confval
    reST; Configuration values
..  _rest-confval:

===============================
Configuration values (confval)
===============================

The :rst:`confval` directive can be used to document configuration values
in a structured way, independent of the programming language.
In a TYPO3 context, it can be used to document configuration values
stored in PHP arrays (TCA, global configuration variables),
TypoScript (TypoScript setup, TSconfig), XML (FlexForms, XLIFF) and
YAML (SiteConfiguration, EXT:form).

Using the :rst:`confval` directive has several benefits:

*   The display is independent of the language of the configuration value
    – for example, unlike :ref:`PHP domain <rest-phpdomain>`.
*   The values appear automatically in the generated keyword index.
*   You can link directly to configuration values.
*   The content element presents the data and its attributes in a
    well-structured way.

Examples
========

Required configuration value
----------------------------

..  confval:: label

    :Required: true
    :type: string or LLL reference
    :Scope: Display
    :Path: $GLOBALS > TCA > [table] > columns > [field]

    The name of the field as shown in the form.

..  code-block:: rst

    ..  confval:: label

        :Required: true
        :type: string or LLL reference
        :Scope: Display
        :Path: $GLOBALS > TCA > [table] > columns > [field]

        The name of the field as shown in the form.

Configuration value with default value
--------------------------------------

..  confval:: fileCreateMask

    :type: text
    :Default: 0664
    :Path: $GLOBALS > TYPO3_CONF_VARS > SYS

    File mode mask for Unix file systems (when files are uploaded/created).

..  code-block:: rst

    ..  confval:: fileCreateMask

        :type: text
        :Default: 0664
        :Path: $GLOBALS > TYPO3_CONF_VARS > SYS

        File mode mask for Unix file systems (when files are uploaded/created).
