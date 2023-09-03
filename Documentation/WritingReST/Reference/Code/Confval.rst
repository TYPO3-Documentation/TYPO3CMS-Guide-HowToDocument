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

Each configuration value name may only be used once. In large references
with different contexts you can define individual configuration schemas for
each context.

Define a configuration schema
=============================

The directive :rst:`confval` is predefined and can not be configured.

To introduce a new configuration schema add the following section to
the manuals :file:`Documentation/Settings.cfg`:

..  code-block:: none
    :caption: EXT:my_extension/Documentation/Settings.cfg


    [sphinx_object_types_to_add]

    my-custom-directive =  my-custom-directive // my-custom-directive // My Cool Configuration Value section

It is possible to define several configuration schemes by listing them each in
one line, for example in the TypoScript reference we have one configuration
scheme for each content object like :typoscript:`TEXT`, :typoscript:`COA`
or :typoscript:`FILE`:

..  code-block:: none
    :caption: reference-typoscript/Documentation/Settings.cfg


    [sphinx_object_types_to_add]

    cobj-coa =  cobj-coa // cobj-coa // Content object COA
    cobj-file =  cobj-file // cobj-file // Content object FILE
    cobj-text =  cobj-text // cobj-text // Content object TEXT

The can then be used to define configuration values for each TypoScript
content object type using the directive used in the first part of the definition
after the `=` sign, for example:

..  cobj-text:: value

    :Data type: string / stdWrap

    Text, which you want to output.

..  code-block:: rst

    ..  cobj-text:: value

        :Data type: string / string / stdWrap

        Text, which you want to output.

You can link to the specific configuration value by second part of the
definition, the one after the first `//` sign:

**Example**

Use the :cobj-text:`value` property of the :typoscript:`TEXT` content element.
Wrap it by :cobj-text:`stdWrap`. Note that the :cobj-text:`stdWrap` property
works different from the one from the :cobj-coa:`stdWrap` property of the
:typoscript:`COA` content object...

..  code-block:: rst

    Use the :cobj-text:`value` property of the :typoscript:`TEXT` content element.
    Wrap it by :cobj-text:`stdWrap`. Note that the :cobj-text:`stdWrap` property
    works different from the one from the :cobj-coa:`stdWrap` property of the
    :typoscript:`COA` content object...

The third entry of the configuration is used as label in the automatic Index
entries (:ref:`genindex.rst <genindex-rst>`):

..  figure:: /Images/CustomConfigurationIndexEntries.png

    Automatic entries on the page :ref:`genindex.rst <genindex-rst>`.

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

Custom configuration schemas
----------------------------

:typoscript:`TEXT`

..  cobj-text:: stdWrap

    :Data type: stdWrap

    stdWrap properties in the :typoscript:`TEXT` content element


:typoscript:`COA`

..  cobj-coa:: stdWrap

    :Data type: stdWrap

    stdWrap properties in the :typoscript:`COA` content element

..  cobj-coa:: 1,2,3, ...

    :Data type: conten object

    Any content object to be displayed


:typoscript:`FILE`

A file can also be put in the property :cobj-coa:`1,2,3, ...` of a
:typoscript:`COA` content object.

..  cobj-file:: file

    :Data type: file

    The file to be displayed

..  cobj-file:: stdWrap

    :Data type: stdWrap

    stdWrap properties in the :typoscript:`FILE` content element


..  code-block:: rst

    :typoscript:`TEXT`

    ..  cobj-text:: stdWrap

        :Data type: stdWrap

        stdWrap properties in the :typoscript:`TEXT` content element


    :typoscript:`COA`

    ..  cobj-coa:: stdWrap

        :Data type: stdWrap

        stdWrap properties in the :typoscript:`COA` content element

    ..  cobj-coa:: 1,2,3, ...

        :Data type: conten object

        Any content object to be displayed


    :typoscript:`FILE`

    A file can also be put in the property :cobj-coa:`1,2,3, ...` of a
    :typoscript:`COA` content object.

    ..  cobj-file:: file

        :Data type: file

        The file to be displayed

    ..  cobj-file:: stdWrap

        :Data type: stdWrap

        stdWrap properties in the :typoscript:`FILE` content element
