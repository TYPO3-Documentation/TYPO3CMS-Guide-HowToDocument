..  include:: /Includes.rst.txt
..  _reference-site-settings:

=============
Site settings
=============

When an extension features :ref:`Settings definitions <t3coreapi:site-sets-settings-definition>`
for site settings these can be automatically documented by including the settings
definition file. The special syntax `PROJECT:` can be used to load the file
from the directory of the extension instead of the `Documentation` folder only.

..  literalinclude:: _siteSetSettings.rst.txt
    :language: rst
    :caption: Settings.rst

..  include:: _siteSetSettings.rst.txt

The custom parameters `:type:`, `:Label:` etc can be used to configure
which aspects of the settings should be shown in the overview table.

A `:name:` can be used to create a namespace when there are several sets. All
links to the configuration values will be prefixed then.
