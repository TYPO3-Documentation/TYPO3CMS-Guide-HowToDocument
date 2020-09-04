.. include:: ../Includes.txt
.. highlight:: rst

.. _format-rest-cgl:

================================
Coding guidelines for reST files
================================

Basic formatting rules
======================

Encoding
--------

* use utf-8

.. _cgl-indenting:

Whitespace and indenting
------------------------

.. important::

   Always use indentation levels correctly. Your code may not
   be rendered as expected if you do not.

* remove white space from the end of lines (= no trailing tabs or spaces)
* don't use tabs
* one indentation level consists of **three spaces**
* code examples use three spaces as indentation level as well

.. note::

   Currently, the documentation is not always indented consistently.
   In some manuals, an indentation level of 4 spaces was used instead.
   We currently recommend to use what has been used on the page you
   are currently editing.

Example:

.. code-block:: rest
  :linenos:

   .. image:: ../images/a4.jpg
      :alt: Left floating image
      :target: https://typo3.org
      :class: with-shadow


* lines 2-4 must be indented one level (3 spaces)


Line Length
-----------

* Keep lines shorter than 80 characters.
* if in doubt about the length: use short lines!

  * That way reST is readable as source as well
  * Files can be easily edited directly on GitHub
  * Files can be compared in a diff view


.. _editorconfig:

.editorconfig
-------------


Most of our documentation projects contain an .editorconfig file.

Use this file to setup your editor / IDE correctly. With some, everything will
just work automatically. With others, you will need to download a plugin. This
is explained on the `Editorconfig <http://EditorConfig.org>`__ page.

Sample contents of :file:`.editorconfig`

.. code-block:: bash
   :linenos:

   # EditorConfig is awesome: http://EditorConfig.org

   # top-most EditorConfig file? false = no!
   root = false

   [{*.rst,*.rst.txt}]
   charset = utf-8
   end_of_line = lf
   insert_final_newline = true
   trim_trailing_whitespace = true
   indent_style = space
   indent_size = 3
   max_line_length = 80

   # MD-Files
   [*.md]
   charset = utf-8
   end_of_line = lf
   insert_final_newline = true
   trim_trailing_whitespace = true
   indent_style = space
   indent_size = 4
   max_line_length = 80


This sample .editorconfig will instruct your editor / IDE to:

* use utf8 as encoding (line 7)
* use spaces instead of tabs (line 11)
* use 3 spaces for indenting (line 12)
* remove trailing whitespace (line 10)


Special characters
------------------

The only way to include "special" characters is to use them directly

.. _rest-cgl-headline-underlines:

Headline underlining
====================

In reStructuredText it is possible to use any type of underlining. The first
used will be recognized as level 1 etc.

However, adhering to the standard for TYPO3 documentation makes it easier for
other contributors to find their way around a file and pick the correct underlining
for the header level.

Use the conventions as defined in :ref:`Headlines-and-sections`.

This underlining is used **per (.rst) file**. It does not matter where in the toctree
the file is. You always start with underlining for level 1 (title) in each
file::



   ========
   1. Title
   ========

   2. Header Level 1
   =================

   3. Header Level 2
   -----------------

   4. Header Level 3
   ~~~~~~~~~~~~~~~~~

   5. Header Level 4
   """""""""""""""""

   6. Header Level 5
   '''''''''''''''''

   7. Header Level 6
   ^^^^^^^^^^^^^^^^^

   8. Header Level 7
   #################

   etc.

.. _version-hints:

How to add version hints
========================

Example, how you can point out **deprecations**::

   .. deprecated:: 10.2
      The hook shown here is deprecated since TYPO3 10.2 - use a custom
      :ref:`PSR-15 middleware<request-handling>` instead.

New **feature**::

   .. versionadded:: 10.2
      Starting with TYPO3 10.2 hooks and signals have been replaced by a PSR-14 based
      event dispatching system.

Changes::

   .. versionchanged:: 2.3.1
      This feature was changed ...

For more information, see the open issue:

* `Should we display version hints <https://github.com/TYPO3-Documentation/T3DocTeam/issues/14>`__

.. _link-to-changelog:

Link to changelog
=================

Linking to the changelog should not be necessary if all necessary information has been transferred
to the documentation, but it is not discouraged either.

The changelog often does not have a title label, so you cannot easily link to it with `:ref:`.

You can use the method described in `How to link to a changelog <https://github.com/TYPO3-Documentation/TYPO3CMS-Guide-HowToDocument/issues/110>`__:

.. code-block:: rest

   :doc:`t3core:Changelog/8.1/Deprecation-75625-DeprecatedCacheClearingOptions`

For this to work, t3core must be defined in :file:`Settings.cfg`:

.. code-block:: none

   t3core = https://docs.typo3.org/c/typo3/cms-core/master/en-us/


.. _rest-refer-to-gui-elements:

Referring to GUI elements
=========================

If you describe something that needs to be selected from a menu or other GUI
element or clicked one after the other, use *>* as separator and use
:ref:`textrole guilabel <textroles>`.

.. important::

   Use the spelling of the word as used in the GUI!

Examples:

.. code-block:: rest

   Select :guilabel:`File > Open`

How it looks:
   Select :guilabel:`File > Open`

.. code-block:: rest

   Click on :guilabel:`ADMIN TOOLS > Extensions` in the backend.

How it looks:
   Click on :guilabel:`ADMIN TOOLS > Extensions` in the backend.


Refer to keystrokes
===================

When pointing out keyboard shortcuts or keystroke sequences, use
:ref:`textrole <textroles>` kbd.

Example:

.. code-block:: rest

   Press :kbd:`ctrl` + :kbd:`s`

How it looks:
   Press :kbd:`ctrl` + :kbd:`s`

