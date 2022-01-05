.. include:: /Includes.rst.txt
.. highlight:: rst
.. index::
   reST; confval
   reST; Configuration values
.. _restContentConfval:

===============================
Configuration values (confval)
===============================

Configuration values (directive :rst:`confval`) can be used to document
structured configuration values independent from the language they are
configured in. The :rst:`confval` directive can be used to document
configuration stored in PHP arrays (TCA, global configuration variables),
TypoScript (TypoScript setup, TSconfig), XML (FlexForms, XLIFF) and YAML
(SiteConfiguration, EXT:form).

Using the :rst:`confval` directive has several benefits:

*  The display is independent from the language of the configuration value
*  The values appear automatically in on the generated keyword index
*  You can link configuration values directly
*  Configuration values can be typed, required and have default values
*  The reST contains only semantic but no design information.

Examples
========

Requiered confval
-----------------

.. code-block:: rst

   .. confval:: label

      :Required: true
      :type: string or LLL reference
      :Scope: Display
      :Path: $GLOBALS > TCA > [table] > columns > [field]

      The name of the field as shown in the form

Rendered it looks like this:

.. confval:: label

   :Required: true
   :type: string or LLL reference
   :Scope: Display
   :Path: $GLOBALS > TCA > [table] > columns > [field]

   The name of the field as shown in the form

Confval with default value
--------------------------


.. code-block:: rst

   .. confval:: fileCreateMask

      :type: text
      :Default: 0664
      :Path: $GLOBALS > TYPO3_CONF_VARS > SYS

      File mode mask for Unix file systems (when files are uploaded/created).

.. confval:: fileCreateMask

   :type: text
   :Default: 0664
   :Path: $GLOBALS > TYPO3_CONF_VARS > SYS

   File mode mask for Unix file systems (when files are uploaded/created).

