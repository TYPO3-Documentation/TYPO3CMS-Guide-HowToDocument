.. This is a comment. It starts with 2 dots and a space

.. -----------------------------------------------------------
   include directive: Here, it includes the file
   Includes.rst.txt. All files in the documentation project should
   do this. Use correct path!
   -----------------------------------------------------------

.. include:: /Includes.rst.txt

.. ------------------------------------------------------------------
   highlight directive: sets the default language for code-blocks.
   Usually, default is set to PHP in Includes.rst.txt. Here, we set it to
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

Every reST (.rst) file should use these underlining styles. In reST, you can use different
styles in any order you want. These are our conventions for TYPO3 documentation.

.. code-block:: rest
   :linenos:

      ========
      DocTitle
      ========

      Then use underlining only:

      .. _header1:

      Header 1
      ========

      Header 1.1
      ----------

      Header 1.1.1
      ~~~~~~~~~~~~

      Header 1.1.1.1
      """"""""""""""

*  line 1-3: This is the doc title. Every .rst file should have one.
*  line 7: header label. This can be used for cross-referencing to this section::

    :ref:`header1`

*  9-10: Header level 1
*  etc.



.. seealso::
   *  :ref:`Headlines-and-sections`
   *  :ref:`explicit-link-targets`



.. _cheat-sheet-links:

:ref:`Links <how-to-document-hyperlinks>`
=========================================

.. _cheat-sheet-external-links:

External Links
--------------

method 1::

   `anchor text <URL>`__

   Check out more information on `t3o <https://typo3.org>`__.

(with one or two underscores at the end, if in doubt, use two)

method 2: "External Hyperlink Targets"::

   Check out more information on t3o_

   _t3o: https://typo3.org

This may be more convenient if you use a link several times.

.. _cheat-sheet-intersphinx:

Cross-References
----------------

When linking within docs.typo3.org, you should use this method of cross-referencing.

Use it to link to a section in this manual::

   :ref:`intersphinx`

A section with the label **intersphinx** must exist! It is placed before the header::

   .. _intersphinx:

   Intersphinx
   ===========

Or, when cross-referencing to other manuals::

   :ref:`shortcut:label`

   :ref:`h2document:intersphinx`


When you are linking to another manual, make sure the
shortcut (here: "h2document") is included in :ref:`settings-cfg`::

      [intersphinx_mapping]

      h2document       = https://docs.typo3.org/m/typo3/docs-how-to-document/master/en-us/Index.html
      ...

We use the same conventions for naming the shortcuts in :file:`Settings.cfg`,
see :ref:`settings-cfg`. Not used manuals are commented out.


.. tip::

   This is a cool feature, where reST & Sphinx shines: Even when a section is
   moved to another page (which effectively changes the URL), the link will still work!

.. t3-field-list-table::
   :header-rows: 1

   -  :Anchor:
      :ThisManual:   Link to: Same manual
      :OtherManual:  Link to: Other manual

   -  :Anchor:       **Explicit** anchor text
      :ThisManual:   ``:ref:`Cross Referencing <intersphinx>```
      :OtherManual:  ``:ref:`Cross Referencing <t3docwrite:intersphinx>```

   -  :Anchor:       **Automatic** anchor text
      :ThisManual:   ``:ref:`intersphinx```
      :OtherManual:  ``:ref:`t3docwrite:intersphinx```


.. seealso::

   *  :ref:`link-targets-explanation` (labels)
   *  :ref:`intersphinx`
   *  :ref:`settings-cfg`




:ref:`Lists <rest-lists>`
=========================

To create a bullet list:

*  add a blank line before and after the list
*  indent the list item text by 3 spaces - including the item sign
*  to create a nested list:

   *  indent the items by 3 spaces (left-align with parent item text)
   *  apply rules of parent list (blank lines, item text indentation, ..)

More text.

.. code-block:: rest

   To create a bullet list:

   *  add a blank line before and after the list
   *  indent the list item text by 3 spaces - including the item sign
   *  to create a nested list:

      *  indent the items by 3 spaces (left-align with parent item text)
      *  apply rules of parent list (blank lines, item text indentation, ..)

   More text.



:ref:`numbered-lists`
=====================

To create a numbered list:

#. add a blank line before and after the list
#. indent the list item text by 3 spaces - including the item sign
#. to create a nested list:

   #. indent the items by 3 spaces (left-align with parent item text)
   #. apply rules of parent list (blank lines, item text indentation, ..)

More text.

.. code-block:: rest

   To create a numbered list:

   #. add a blank line before and after the list
   #. indent the list item text by 3 spaces - including the item sign
   #. to create a nested list:

      #. indent the items by 3 spaces (left-align with parent item text)
      #. apply rules of parent list (blank lines, item text indentation, ..)

   More text.



:ref:`Code Blocks <writing-rest-codeblocks-with-syntax-highlighting>`
=====================================================================

.. important::

   Use syntactically correct code in your codeblocks.

Code Block Directive
--------------------

**How it looks:**

.. code-block:: php

   $a = 'hello';
   $b = 'something';

Source:

.. code-block:: rest
   :linenos:

   .. code-block:: php

      $a = 'hello';
      $b = 'something';

This uses the **directive** "code-block" (line 1)

.. important::

   Make sure to indent correctly. The lines of the code-block (line 3+)
   must be indented (3 spaces).

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


:ref:`Inline code, text roles <text-roles>`
===========================================

For inline code or for other semantic markup of special texts, use text roles.

Examples:

#. :php:`$result = $a + 23;` (PHP snippet)
#. :typoscript:`lib.hello.value = Hello World!` (TypoScript snippets)
#. :file:`/etc/passwd` (file)
#. :kbd:`ctrl` + :kbd:`s` (keyboard strokes)

Source (inline text with text roles):

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

Another example:

.. code-block:: rest

   .. image:: ../images/a4.jpg
      :class: with-shadow
      :target: https://typo3.org
      :alt: alt text
      :width: 100px

.. seealso::

   *  :ref:`images`


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

With Big Numbers XXL
--------------------

*Source:* ::

   .. rst-class:: bignums-xxl

   1. Embed an image

      Source::

         .. image: some_image.png
            :class: with-shadow

   2. Two

      Do something else ...

*How it looks:*

.. rst-class:: bignums-xxl

1. Embed an image

   Source::

      ../images/a4.jpg
         :class: with-shadow

2. Two

   Do something else ...


:ref:`Tips, Hints, Important <rest-admonitions>` (Admonitions)
==============================================================

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

