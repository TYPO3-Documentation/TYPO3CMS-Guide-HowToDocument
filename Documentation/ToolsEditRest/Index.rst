.. include:: ../Includes.txt
.. highlight:: rst

.. _tools:
.. _tools-for-editing-rest:

======================
Tools for Editing reST
======================

When editing reST files locally, you should use an editor or IDE with
good support for syntax highlighting and marking errors in reST.

`PhpStorm <https://www.jetbrains.com/phpstorm/>`__ is commonly used by
developers in the TYPO3 community. It does however cost money.

Good alternatives can be found in the "Free Editors" section of
`StackOverflow: reStructuredText tool support <https://stackoverflow.com/a/2747041/2444812>`__.

The editor or IDE should ideally have the following features:

* syntax highlighting for reST
* show syntax errors
* provide possibility to use (configurable) code snippets for easy insertion of
  directives
* provide keyboard shortcuts and configurable commands for running
  Docker
* built in spell checking (English)

Setup your editor / IDE to use the .editorconfig file, which already
exists in most documentation repositories. This will set up your
editor / IDE to comply with our :ref:`basic coding guidelines
<format-rest-cgl>`.

You may have to install
an additional plugin, see `EditorConfig <https://editorconfig.org/#download>`__.

PhpStorm
========

reStructuredText Plugin
-----------------------

You should activate the `reStructuredText plugin <https://plugins.jetbrains.com/plugin/7124-restructuredtext-support>`__
that will assist you when editing reST
files. In order to activate a plugin, press :kbd:`ctrl + alt + s`, then
select :guilabel:`Plugins`, search for the plugin and enable it (mark
checkbox).

.. image:: ../images/phpstorm-rest-plugin.png
   :class: with-shadow

If the Plugin is not installed yet, you may have to :guilabel:`Browse
repositories`, select the plugin and click the green :guilabel:`Install` button.

Some errors in formatting will be pointed out:

.. image:: ../images/phpstorm-rest-warning.png
   :class: with-shadow

.. _phpstorm-editorconfig:

EditorConfig Plugin
-------------------

Additionally, (download) and enable the `EditorConfig <https://plugins.jetbrains.com/plugin/7294-editorconfig>`__
plugin in order to get correct Coding Guideline settings like indent width already defined in
.editorconfig file of documentation project.

Spellchecking
-------------

You can add some specific TYPO3 spellings to PhpStorms internal dictionary.
Just place the cursor on the word, click alt-enter and then "Save to dictionary".

.. image:: ../images/phpstorm-add-to-dictionary.png
   :class: with-shadow


For more information, see the `Spellchecking <https://www.jetbrains.com/help/phpstorm/spellchecking.html>`__
PhpStorm page.


