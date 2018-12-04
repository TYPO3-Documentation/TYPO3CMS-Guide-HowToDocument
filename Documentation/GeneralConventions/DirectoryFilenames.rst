.. include:: ../Includes.txt
.. highlight:: rst

.. _general-conventions-dir-and-filenames:

========================
Directory and File Names
========================

* All documentation resides in a :file:`Documentation` subfolder
* This folder contains the files :file:`Settings.cfg`, :file:`Includes.txt` and :file:`Index.rst`
* Use CamelCase for file and directory names.
* reSt files have ending **.rst**
* Included files have ending **.rst.txt**


.. code-block:: none

  Documentation/
  |
   --> Settings.cfg
  |
   --> Includes.txt
  |
   --> Index.rst
  |
   --> Topic1/
         |
         -> Index.rst
         -> Subtopic1.rst
         -> Subtopic2.rst

If the documentation follows these conventions, the documentation rendering toolchain
automatically detects the documentation and renders it correctly on the documentation
server.

It is **strongly recommended** to do it the way it is described here.
For alternatives, please look at :ref:`supported-filenames-and-formats`.


Information about Basic Files
=============================

.. _settings-cfg:

Settings.cfg
------------

file: `Documentation/Settings.cfg`

This file must be adapted for the manual. It contains some meta information. It also
contains start urls for the intersphinx linking mechanism.

Use the file in `T3DocTeam: Settings.cfg <https://github.com/TYPO3-Documentation/T3DocTeam/blob/master/Documentation/Settings.cfg>`__
as an up-to-date example!

The file consists of sections, which start with a keyword in brackets, such as `[general]`.
Make sure that all directives exist in the correct section.

(minimal) example:


.. code-block:: none
   :linenos:


      [general]

      project     = T3DocTeam-at-Work
      version     = 1.0
      release     = 1.0.0
      t3author    = TYPO3 Documentation Team
      copyright   = since ever by the author(s)

      description = The TYPO3 Documentation team is taking notes here.


      [html_theme_options]

      # to get the "Edit me on Github Button"
      github_branch        = master
      github_repository    = typo3-documentation/t3docteam

      # Fill in values to get links in the "Related Links" section at the lower left
      project_contact      =
      project_discussions  =
      project_home         =

      # Replace url with link to your issue
      project_issues       = https://github.com/typo3-documentation/t3docteam/issues

      # Replace url with link to your repository
      project_repository   = https://github.com/typo3-documentation/t3docteam/


      [intersphinx_mapping]

      h2document    = https://docs.typo3.org/typo3cms/HowToDocument/
      rendert3docs  = https://docs.typo3.org/typo3cms/RenderTYPO3DocumentationGuide/
      t3contribute  = https://docs.typo3.org/typo3cms/ContributionWorkflowGuide/
      t3coreapi     = https://docs.typo3.org/typo3cms/CoreApiReference
      t3tsconfig    = https://docs.typo3.org/typo3cms/TSconfigReference
      t3editors     = https://docs.typo3.org/typo3cms/EditorsTutorial/
      t3extbase     = https://docs.typo3.org/typo3cms/ExtbaseGuide
      t3extbasebook = https://docs.typo3.org/typo3cms/ExtbaseFluidBook/
      t3home        = https://docs.typo3.org/typo3cms/
      t3inside      = https://docs.typo3.org/typo3cms/InsideTypo3Reference/
      t3install     = https://docs.typo3.org/typo3cms/InstallationGuide/
      t3l10n        = https://docs.typo3.org/typo3cms/FrontendLocalizationGuide/
      t3start       = https://docs.typo3.org/typo3cms/GettingStartedTutorial/
      t3tca         = https://docs.typo3.org/typo3cms/TCAReference/
      t3sitepkg     = https://docs.typo3.org/typo3cms/SitePackageTutorial/
      t3ts45        = https://docs.typo3.org/typo3cms/TyposcriptIn45MinutesTutorial/
      t3tsconfig    = https://docs.typo3.org/typo3cms/TSconfigReference/
      t3tsref       = https://docs.typo3.org/typo3cms/TyposcriptReference/

      [extensions]

      # for embedding YouTube videos
      any_name_youtube = sphinxcontrib.youtube


.. _includes-txt:

Includes.txt
------------

file: `Documentation/Includes.txt`

This file can be the same for all Documentation projects.

Use the file in `T3DocTeam: Includes.txt <https://github.com/TYPO3-Documentation/T3DocTeam/blob/master/Documentation/Includes.txt>`__
as an up-to-date example.

Example:

.. code-block:: rest
   :linenos:

      .. This is 'Includes.txt'. It is included at the very top of each and
      every ReST source file in THIS documentation project (= manual).

      .. role:: aspect (emphasis)
      .. role:: html(code)
      .. role:: js(code)
      .. role:: php(code)
      .. role:: sep (strong)
      .. role:: typoscript(code)

      .. role:: ts(typoscript)
         :class: typoscript

      .. default-role:: code
      .. highlight:: php


.. _index-rst:

Index.rst
---------

file: `Documenation/Index.rst`

This file must be adapted for the manual. It contains text that is displayed on the startpage
as well as the toctree.

Use the file in `T3DocTeam: Index.rst <https://github.com/TYPO3-Documentation/T3DocTeam/blob/master/Documentation/Index.rst>`__
as an example.

Example:

.. code-block:: rest
   :linenos:

      .. include:: Includes.txt

      =================
      T3DocTeam at Work
      =================

      some text


   .. toctree::
      :hidden:

      Introduction/Index
      Configuration/Index


* line 1 : every .rst file should include Includes.txt
* line 3-5: the header
* line 10-14: the toctree, which specifically includes the files Introduction/Index.rst, Configuration/Index.rst


