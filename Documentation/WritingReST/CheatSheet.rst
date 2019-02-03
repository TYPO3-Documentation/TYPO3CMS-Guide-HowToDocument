.. This is a comment. It starts with 2 dots and a space
.. This page shows the source code in a code-block.


.. ---------------------------------------------------------------
.. tip: This directive will display the following indented text as
.. text with a green box (as styled by our sphinx template).
.. ---------------------------------------------------------------

.. tip::

   To look at the reST source of this rendered page, scroll to the bottom
   and click on "View page source".

Source (tip):
   .. code-block:: rst

      .. tip::

         To look at the reST source of this rendered page, scroll to the bottom
         and click on "View page source".


More information:

* :ref:`rest-admonitions`

.. -----------------------------------------------------------
.. include directive: Here, it includes the file
.. Includes.txt. All files in the documentation project should
.. do this. Use correct path!
.. -----------------------------------------------------------

.. include:: ../Includes.txt

.. ------------------------------------------------------------------
.. highlight directive: sets the default language for code-blocks.
.. Usually, default is set to PHP in Includes.txt. Here, we set it to
.. rst (for reStructuredText).
.. ------------------------------------------------------------------

.. highlight:: rst


.. ------------------------------------------------------------------------
.. header label:  You can use this to create
.. cross-references: To link to the next section, use :ref:`rest-cheat-sheet`
.. or :ref:`h2document:rest-cheat-sheet` from another manual
.. -------------------------------------------------------------------------


.. ---------------------------------------------------------
.. header: Use (over and) underline to mark a text as header
.. ---------------------------------------------------------

.. _rest-cheat-sheet:

=========================
reST & Sphinx Cheat Sheet
=========================


Source (header with header label):
   .. code-block:: rest

      .. _rest-cheat sheet:
      =========================
      reST & Sphinx Cheat Sheet
      =========================

More information:

* :ref:`Headlines-and-sections`
* :ref:`explicit-link-targets`


This is a Header Level 1
========================

Source (header level 1):
   .. code-block:: rest

      This is a Header Level 1
      ========================



This is a Header Level 2
------------------------

Source (header level 2):
   .. code-block:: rest

      This is a Header Level 2
      ------------------------

External Links
==============

This is an external link: `t3o <https://typo3.org>`__.

Source (external link):

   .. code-block:: rest

      This is an external link: `t3o <https://typo3.org>`__.


Cross-References
================

This is a cross-reference to a section in this manual: :ref:`intersphinx`.

Source (cross-reference):

   .. code-block:: rest

      This is a cross-reference to a section in this manual: :ref:`intersphinx`.


This is a cross-reference with **additional anchor text** "Cross-Reference
with intersphinx" to a section
in this manual: :ref:`Cross-Reference with intersphinx <intersphinx>`.

Source (cross-reference):

   .. code-block:: rest

      This is a ... :ref:`Cross-Reference with intersphinx <intersphinx>`.



More information:

* :ref:`how-to-document-hyperlinks`


List
====

This is a bullet list:

* list item 1
* list item 2

More text. **Important:** Always add blank line before and after list!


Source (list):

   .. code-block:: rest

      This is a bullet list:

      * list item 1
      * list item 2

      More text. **Important:** Always add blank line before and after list!



Code Blocks
===========

.. code-block:: php

   $a = 'hello';

Source (code-block):

   .. code-block:: rest

      .. code-block:: php

            $a = 'hello';

Or (use shorthand `::`):
   (if php is already set as default with `highlight` directive)

   .. code-block:: rest

      ::

            $a = 'hello';

More information:

* :ref:`writing-rest-codeblocks-with-syntax-highlighting`
* :ref:`codeblocks-highlight-directive`



Inline Code, Textroles, Semantic Markup
=======================================

For inline code or for other semantic markup of special texts, use textroles.

Examples:

#. :php:`$result = $a + 23;` (PHP snippet)
#. :typoscript:`lib.hello.value = Hello World!` (TypoScript snippets)
#. :file:`/etc/passwd` (file)
#. :kbd:`ctrl` + :kbd:`s` (keyboard strokes)

Source (inline text with textroles):

   .. code-block:: rest
      :linenos:

      :php:`$result = $a + 23;`
      :typoscript:`lib.hello.value = Hello World!`
      :file:`/etc/passwd`
      :kbd:`ctrl` + :kbd:`s`

More information:

* :ref:`textroles`



Images
======

.. image:: ../images/a4.jpg
   :class: with-shadow

Source (image):

   .. code-block:: rest

      .. image:: ../images/a4.jpg
         :class: with-shadow



Bold & Italic
=============

Normal text, **bold text** and *italic text*.

Source (bold & italic):

   .. code-block:: rest

      Normal text, **bold text** and *italic text*.

More information:

* :ref:`rest-bold-italic`
* :ref:`common-pitfalls-inline-style`


YouTube Videos
==============

.. youtube:: wNxO-aXY5Yw

Source (YouTube):

   .. code-block:: rest

      .. youtube:: wNxO-aXY5Yw
