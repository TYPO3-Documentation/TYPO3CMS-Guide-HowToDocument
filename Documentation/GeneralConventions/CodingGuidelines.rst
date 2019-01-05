.. include:: ../Includes.txt
.. highlight:: rst

.. _format-rest-cgl:

================================
Coding Guidelines for reST Files
================================

Basic Formatting Rules
======================

Encoding
--------

* use utf-8

Whitespace and Indenting
------------------------

.. important::

   Always use indentation levels correctly (3 spaces). Your code may not
   be rendered as expected if you do not.

* remove white space from the end of lines (= no trailing tabs or spaces)
* don't use tabs
* one indentenation level consists of **three spaces**
* code examples use three spaces as indentation level as well

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
  * Files can be easily edited directly on Github
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

   # MD-Files
   [*.md]
   charset = utf-8
   end_of_line = lf
   insert_final_newline = true
   trim_trailing_whitespace = true
   indent_style = space
   indent_size = 4


This sample .editorconfig will instruct your editor / IDE to:

* use utf8 as encoding (line 7)
* use spaces instead of tabs (line 11)
* use 3 spaces for indenting (line 12)
* remove trailing whitespace (line 10)


Special Characters
------------------

The only way to include "special" characters is to use them directly

.. _rest-refer-to-gui-elements:


Referring to GUI Elements
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


Refer to Keystrokes
===================

When pointing out keyboard shortcuts or keystroke sequences, use
:ref:`textrole <textroles>` kbd.

Example:

.. code-block:: rest

   Press :kbd:`ctrl` + :kbd:`s`

Result:

   Press :kbd:`ctrl` + :kbd:`s`

