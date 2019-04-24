.. This is a comment. It starts with 2 dots and a space

.. -----------------------------------------------------------
   include directive: Here, it includes the file
   Includes.txt. All files in the documentation project should
   do this. Use correct path!
   -----------------------------------------------------------

.. include:: ../Includes.txt

.. ------------------------------------------------------------------
   highlight directive: sets the default language for code-blocks.
   Usually, default is set to PHP in Includes.txt. Here, we set it to
   rst (for reStructuredText).
   ------------------------------------------------------------------

.. highlight:: rst


.. ------------------------------------------------------------------------
   header label:  You can use this to create
   cross-references: To link to the next section, use :ref:`rest-cheat-sheet`
   or :ref:`h2document:rest-cheat-sheet` from another manual
   -------------------------------------------------------------------------


.. ---------------------------------------------------------
   header: Use (over and) underline to mark a text as header
   ---------------------------------------------------------

.. _rest-cheat-sheet:

=========================
reST & Sphinx Cheat Sheet
=========================


Source (header with header label):
   .. code-block:: rest

      .. _rest-cheat-sheet:
      =========================
      reST & Sphinx Cheat Sheet
      =========================

More information:

* :ref:`Headlines-and-sections`
* :ref:`explicit-link-targets`


This is a Header Level 1
========================

Source (header level 1)::

      This is a Header Level 1
      ========================



This is a Header Level 2
------------------------

Source (header level 2)::

      This is a Header Level 2
      ------------------------

This is a Header Level 3
~~~~~~~~~~~~~~~~~~~~~~~~

Source (header level 3)::

      This is a Header Level 3
      ~~~~~~~~~~~~~~~~~~~~~~~~

.. _cheat-sheet-links:

:ref:`Links <how-to-document-hyperlinks>`
=========================================

.. _cheat-sheet-external-links:

External Links
--------------

This is an external link: `t3o <https://typo3.org>`__.

Source (external link)::

   This is an external link: `t3o <https://typo3.org>`__.

:ref:`cheat-sheet-intersphinx`

Cross-References
----------------

This is a cross-reference to a section in this manual: :ref:`intersphinx`.

Source::

   This is a cross-reference to a section in this manual: :ref:`intersphinx`.


.. t3-field-list-table::
 :header-rows: 1

 - :Anchor:
   :ThisManual:   Link to: Same manual
   :OtherManual:  Link to: Other manual

 - :Anchor:       **Explicit** anchor text
   :ThisManual:   1) ``:ref:`Cross Reference <intersphinx>```
                  :ref:`Cross Reference <intersphinx>`
   :OtherManual:  2) ``:ref:`TSref <t3tsref:start>```
                  :ref:`TSref <t3tsref:start>`

 - :Anchor:       **Automatic** anchor text
   :ThisManual:   3) ``:ref:`intersphinx```
                  :ref:`intersphinx`
   :OtherManual:  4) ``:ref:`t3tsref:start```
                  :ref:`t3tsref:start`

.. tip::

   When you are linking to another manual, make sure the
   shortcut (e.g. "t3tsref") is included in :ref:`settings-cfg`::

      [intersphinx_mapping]

      t3tsref       = https://docs.typo3.org/typo3cms/TyposcriptReference/




:ref:`Lists <rest-lists>`
=========================

This is a bullet list:

* list item 1
* list item 2

More text. **Important:** Always add blank line before and after list!

.. code-block:: rest

   This is a bullet list:

   * list item 1
   * list item 2

   More text. **Important:** Always add blank line before and after list!



:ref:`Code Blocks <writing-rest-codeblocks-with-syntax-highlighting>`
=====================================================================

Code Block Directive
--------------------

**How it looks:**

.. code-block:: php

   $a = 'hello';

Source::

  .. code-block:: php

     $a = 'hello';


Literal Block (`::`)
--------------------

Or, use the literal block markup `::` if PHP is already set as default
with `highlight` directive and you want to combine a text with a colon,
followed by the code block.

**How it looks:**

Assign the variable a::

   $a = 'hello';

Source::

   Assign the variable a::

      $a = 'hello';


:ref:`Inline Code, Textroles <textroles>`
=========================================

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



:ref:`Bold & Italic <rest-bold-italic>`
=======================================

Normal text, **bold text** and *italic text*.

Source (bold & italic):

   .. code-block:: rest

      Normal text, **bold text** and *italic text*.


:ref:`Images <rest-images>`
===========================

.. image:: ../images/a4.jpg
   :class: with-shadow

Source (image):

   .. code-block:: rest

      .. image:: ../images/a4.jpg
         :class: with-shadow



:ref:`YouTube Videos <youtube>`
===============================

.. youtube:: wNxO-aXY5Yw

Source (YouTube):

   .. code-block:: rest

      .. youtube:: wNxO-aXY5Yw



:ref:`Styled Numbered Lists <big-nums>`
=======================================

This is often used, for a Quick Start section, involving a few numbered steps:

With Big Numbers
----------------

This is an example with a code block (:rst:`::`) embedded in the sections.

*Source:* ::

   .. rst-class:: bignums

   1. Embed an image

      Source::

         .. image: some_image.png
            :class: with-shadow

   2. Two

      Do something else ...

*How it looks:*

.. rst-class:: bignums

1. Embed an image

   Source::

      ../images/a4.jpg
         :class: with-shadow

2. Two

   Do something else ...


:ref:`Tips, Hints, Important <rest-admonitions>`
================================================

.. ---------------------------------------------------------------
   tip: This directive will display the following indented text as
   text with a green box (as styled by our sphinx template).
   ---------------------------------------------------------------

.. tip::

   To look at the reST source of this rendered page, scroll to the bottom
   and click on "View page source".

Source (tip):
   .. code-block:: rst

      .. tip::

         To look at the reST source of this rendered page, scroll to the bottom
         and click on "View page source".

