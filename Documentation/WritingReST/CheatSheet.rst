..  include:: /Includes.rst.txt

..  ------------------------------------------------------------------------
    header label:  You can use this to create
    cross-references: To link to the next section, use :ref:`rest-cheat-sheet`
    or :ref:`h2document:rest-cheat-sheet` from another manual
    -------------------------------------------------------------------------


..  ---------------------------------------------------------
    header: Use (over and) underline to mark a text as header
    ---------------------------------------------------------

..  index:: reST; Cheat sheet
..  _rest-cheat-sheet:

==========================
Cheat sheet: reST & Sphinx
==========================

:ref:`Headlines <Headlines-and-sections>`
=========================================

Every reST (.rst) file should use these underlining styles. In reST, you can use different
styles in any order you want. These are our conventions for TYPO3 documentation.

..  code-block:: rest
    :linenos:

        ========
        DocTitle
        ========

        Then use underlining only:

        ..  _header1:

        Header 1
        ========

        Header 1.1
        ----------

        Header 1.1.1
        ~~~~~~~~~~~~

        Header 1.1.1.1
        """"""""""""""

*   line 1-3: This is the doc title. Every .rst file should have one.
*   line 7: header label. This can be used for cross-referencing to this section:

    ..  code-block:: rest

        :ref:`header1`

*   9-10: Header level 1
*   etc.

..  seealso::
    *   :ref:`Headlines-and-sections`
    *   :ref:`explicit-link-targets`


..  _cheat-sheet-links:

:ref:`Links <how-to-document-hyperlinks>`
=========================================


..  index:: reST; External links
..  _cheat-sheet-external-links:

External links
--------------

method 1:

..  code-block:: rest

    `anchor text <URL>`__

    Check out more information on `t3o <https://typo3.org>`__.

(with one or two underscores at the end, if in doubt, use two)

method 2: "External Hyperlink Targets":

..  code-block:: rest

    Check out more information on t3o_

    _t3o: https://typo3.org

This may be more convenient if you use a link several times.


..  index::
    reST; Cross references
    reST roles; ref
..  _cheat-sheet-intersphinx:

Cross references
----------------

When linking within docs.typo3.org, you should use this method of cross-referencing.

Use it to link to a section in this manual:

..  code-block:: rest

    :ref:`intersphinx`

A section with the label **intersphinx** must exist! It is placed before the header:

..  code-block:: rest

    ..  _intersphinx:

    Intersphinx
    ===========

Or, when cross-referencing to other manuals:

..  code-block:: rest

    :ref:`shortcut:label`

:ref:`h2document:intersphinx`


When you are linking to another manual, make sure the
shortcut (here: "h2document") is included in :ref:`settings-cfg`:

..  code-block:: none

    [intersphinx_mapping]

    h2document         = https://docs.typo3.org/m/typo3/docs-how-to-document/main/en-us/Index.html
    ...

We use the same conventions for naming the shortcuts in :file:`Settings.cfg`,
see :ref:`settings-cfg`. Not used manuals are commented out.


..  tip::

    This is a cool feature, where reST & Sphinx shines: Even when a section is
    moved to another page (which effectively changes the URL), the link will still work!

..  t3-field-list-table::
    :header-rows: 1

    -  :Anchor:
        :ThisManual:    Link to: Same manual
        :OtherManual:  Link to: Other manual

    -  :Anchor:         **Explicit** anchor text
        :ThisManual:    ``:ref:`Cross Referencing <intersphinx>```
        :OtherManual:  ``:ref:`Cross Referencing <t3docwrite:intersphinx>```

    -  :Anchor:         **Automatic** anchor text
        :ThisManual:    ``:ref:`intersphinx```
        :OtherManual:  ``:ref:`t3docwrite:intersphinx```

..  index:: reST; Preventing links
..  _cheat-sheet-preventing-links:

Preventing links
----------------

Prevent unintentional linking of simple URLs with the :code:`:samp:` directive:

..  code-block:: rest

    The TYPO3 backend can be accessed via :samp:`https://example.org/typo3` ..

and emphasize parts of the URL with curly braces:

..  code-block:: rest

    The *route* is the "speaking URL" as a whole without the domain part,
    for example :samp:`https://example.org/{<path>}`.

..  index:: reST; Hypothetical domains
..  _cheat-sheet-hypothetical-domains:

Hypothetical domains
--------------------

If the domain name of an URL does not matter, but serves as a placeholder,
choose from this list of dummy domains – in this order:

1. :samp:`https://example.org`
2. :samp:`https://example.com`
3. :samp:`https://example.net`

and use for explicit mention of the local development context:

4. :samp:`https://example.localhost`.

For further dummy domains use subdomains of the domains listed above such as

-  :samp:`https://staging.example.org`
-  :samp:`https://production.example.org`.

..  seealso::

    *   :ref:`link-targets-explanation` (labels)
    *   :ref:`intersphinx`
    *   :ref:`settings-cfg`



..  index::
    reST; Lists
    reST; Bullet lists

:ref:`Lists <rest-lists>`
=========================

**How it looks:**

To create a bullet list:

*   add a blank line before and after the list
*   indent the list item text by 4 spaces - including the item sign
*   to create a nested list:

    *   indent the items by 4 spaces (left-align with parent item text)
    *   apply rules of parent list (blank lines, item text indentation, ..)

More text.

Source:

..  code-block:: rest

    To create a bullet list:

    *   add a blank line before and after the list
    *   indent the list item text by 4 spaces - including the item sign
    *   to create a nested list:

        *   indent the items by 4 spaces (left-align with parent item text)
        *   apply rules of parent list (blank lines, item text indentation, ..)

    More text.


..  index:: reST; Numbered lists

:ref:`numbered-lists`
=====================

**How it looks:**

To create a numbered list:

#.  add a blank line before and after the list
#.  indent the list item text by 4 spaces - including the item sign
#.  to create a nested list:

    #. indent the items by 4 spaces (left-align with parent item text)
    #. apply rules of parent list (blank lines, item text indentation, ..)

More text.

Source:

..  code-block:: rest

    To create a numbered list:

    #.  add a blank line before and after the list
    #.  indent the list item text by 4 spaces - including the item sign
    #.  to create a nested list:

        #. indent the items by 4 spaces (left-align with parent item text)
        #. apply rules of parent list (blank lines, item text indentation, ..)

    More text.


..  index:: reST; Code blocks

:ref:`Code Blocks <writing-rest-codeblocks-with-syntax-highlighting>`
=====================================================================

..  important::

    Use syntactically correct code in your code blocks.


..  index:: reST directives; code-block

Code block directive
--------------------

**How it looks:**

..  code-block:: php

    $a = 'hello';
    $b = 'something';

Source:

..  code-block:: rest
    :linenos:

    ..  code-block:: php

        $a = 'hello';
        $b = 'something';

This uses the **directive** "code-block" (line 1)

..  important::

    Make sure to indent correctly. The lines of the code-block (line 3+)
    must be indented (4 spaces).

Placeholders
------------

Use the `Backus-Naur form <https://en.wikipedia.org/wiki/Backus-Naur_form>`__ like `<placeholder-name>` for placeholders in code and
URLs.

Examples:

#. :php:`class <Entity>Controller extends ActionController`
#. `typo3/sysext/core/bin/typo3 impexp:import <file>`
#. :samp:`https://example.org/typo3/main?token=<token-id>`

For XML and HTML, use the comment tag :html:`<!-- placeholder-name -->`.


..  index:: reST roles

:ref:`Inline code, text roles <text-roles>`
===========================================

For inline code or for other semantic markup of special texts, use text roles.

**How it looks:**

#. :php:`$result = $a + 23;` (PHP snippet)
#. :typoscript:`lib.hello.value = Hello World!` (TypoScript snippets)
#. :file:`/etc/passwd` (file)
#. :kbd:`ctrl` + :kbd:`s` (keyboard strokes)

Source:

..  code-block:: rest
    :linenos:

    :php:`$result = $a + 23;`
    :typoscript:`lib.hello.value = Hello World!`
    :file:`/etc/passwd`
    :kbd:`ctrl` + :kbd:`s`


..  index::
    reST; Bold
    reST; Italic

:ref:`Bold & italic <rest-bold-italic>`
=======================================

**How it looks:**

Normal text, **bold text** and *italic text*.

Source:

..  code-block:: rest

    Normal text, **bold text** and *italic text*.


..  index::
    reST; Images
    reST directives; image

:ref:`Images <rest-images>`
===========================

**How it looks:**

..  image:: /Images/a4.jpg
    :class: with-shadow

Source:

..  code-block:: rest

    ..  image:: /Images/a4.jpg
        :class: with-shadow

Another example:

..  code-block:: rest

    ..  image:: /Images/a4.jpg
        :class: with-shadow
        :target: https://typo3.org
        :alt: alt text
        :width: 100px

..  seealso::

    *   :ref:`images`


..  index::
    reST; YouTube videos
    reST directives; youtube

:ref:`YouTube videos <youtube>`
===============================

**How it looks:**

..  youtube:: wNxO-aXY5Yw

Source:

..  code-block:: rest

    ..  youtube:: wNxO-aXY5Yw


..  index::
    reST; Styled numbered lists
    reST classes; bignums

:ref:`Styled numbered lists <big-nums>`
=======================================

This is often used, for a Quick Start section, involving a few numbered steps:

With Big Numbers
----------------

This is an example with a code block (:rst:`::`) embedded in the sections.

**How it looks:**

..  rst-class:: bignums

1.  Embed an image

    Source::

        /Images/a4.jpg
            :class: with-shadow

2.  Two

    Do something else ...

Source:

..  code-block:: rest

    ..  rst-class:: bignums

    1.  Embed an image

        Source:

        ..  code-block:: rest

            ..  image: some_image.png
                :class: with-shadow

    2.  Two

        Do something else ...


With Big Numbers XXL
--------------------

**How it looks:**

..  rst-class:: bignums-xxl

1.  Embed an image

    Source:

    ..  code-block:: rest

        /Images/a4.jpg
            :class: with-shadow

2.  Two

    Do something else ...

Source:

..  code-block:: rest

    ..  rst-class:: bignums-xxl

    1.  Embed an image

        Source:

        ..  code-block:: rest

            ..  image: some_image.png
                :class: with-shadow

    2.  Two

        Do something else ...


:ref:`Configuration values <rest-confval>` (confval)
====================================================

**How it looks:**

..  confval:: title

    :Required: true
    :type: string or LLL reference
    :Scope: Display
    :Path: $GLOBALS > TCA > [table] > columns > [field]

    The name of the field as shown in the form.

Source:

..  code-block:: rst

    ..  confval:: title

        :Required: true
        :type: string or LLL reference
        :Scope: Display
        :Path: $GLOBALS > TCA > [table] > columns > [field]

        The name of the field as shown in the form.


:ref:`PHP domain <rest-phpdomain>`
==================================

**How it looks:**

..  php:namespace::  Vendor\MyExtension

..  php:class:: DateTime

    Datetime class

    ..  php:method:: setDate($year, $month, $day)

        Set the date.

        :param int $year: The year.
        :param int $month: The month.
        :param int $day: The day.
        :returns: Either false on failure, or the datetime object for method chaining.

Source:

..  code-block:: rst

    ..  php:namespace::  Vendor\MyExtension

    ..  php:class:: DateTime

        Datetime class

        ..  php:method:: setDate($year, $month, $day)

            Set the date.

            :param int $year: The year.
            :param int $month: The month.
            :param int $day: The day.
            :returns: Either false on failure, or the datetime object for method chaining.


..  index:: reST; Admonitions

:ref:`Tips, hints, important <rest-admonitions>` (Admonitions)
==============================================================

..  ---------------------------------------------------------------
    tip: This directive will display the following indented text as
    text with a green box (as styled by our sphinx template).
    ---------------------------------------------------------------

Visit :ref:`h2document:rest-admonitions` to see the available admonitions.

**How it looks:**

..  tip::

    To look at the reST source of this rendered page, scroll to the top
    and click on :guilabel:`View source`.

Source:

..  code-block:: rst

    ..  tip::

        To look at the reST source of this rendered page, scroll to the bottom
        and click on "View page source".


:ref:`Cards <rest-cards>`
=========================

**How it looks:**

..  container:: row m-0 p-0

    ..  container:: col-md-6 pl-0 pr-3 py-3 m-0

        ..  container:: card px-0 h-100

            ..  rst-class:: card-header h3

                ..  rubric:: :ref:`Pages <t3editors:pages>`

            ..  container:: card-body

                The Page Management Guide introduces TYPO3's Page Tree and explains how pages are created and managed.

            ..  container:: card-footer pb-0

                ..  rst-class:: horizbuttons-striking-m

                -  `11 <https://docs.typo3.org/m/typo3/tutorial-editors/11.5/en-us/Pages/Index.html>`__

Source:

..  code-block:: rst

    ..  container:: row m-0 p-0

    ..  container:: col-md-6 pl-0 pr-3 py-3 m-0

        ..  container:: card px-0 h-100

            ..  rst-class:: card-header h3

                ..  rubric:: :ref:`Pages <t3editors:pages>`

            ..  container:: card-body

                The Page Management Guide introduces TYPO3's Page Tree and explains how pages are created and managed.

            ..  container:: card-footer pb-0

                ..  rst-class:: horizbuttons-striking-m

                -  `11 <https://docs.typo3.org/m/typo3/tutorial-editors/11.5/en-us/Pages/Index.html>`__


:ref:`Tabs <rest-tabs>`
=======================

**How it looks:**

..  tabs::

    ..  group-tab:: bash

        ..  code-block:: bash

            touch example-project-directory/public/FIRST_INSTALL

    ..  group-tab:: powershell

        ..  code-block:: powershell

            echo $null >> public/FIRST_INSTALL

Source:

..  code-block:: rst

    ..  tabs::

        ..  group-tab:: bash

            ..  code-block:: bash

                touch example-project-directory/public/FIRST_INSTALL

        ..  group-tab:: powershell

            ..  code-block:: powershell

                echo $null >> public/FIRST_INSTALL


:ref:`Graphs <graphviz-graphs>`
===============================

**How it looks:**

..  graphviz::

    graph {
        user [
            shape=plaintext;
            width=4;
            label="User";
            style="";
        ]
        view [
            shape=box;
            width=4;
            label=<<B>View</B><BR/>Displaying the data>;
        ]
        controller [
            shape=box;
            width=4;
            label=<<B>Controller</B><BR/>Control of functionality>;
        ]
        model [
            shape=box;
            width=4;
            label=<<B>Model</B><BR/>Domain model and domain logic>;
        ]
        user -- view -- controller -- model;
    }

Source:

..  code-block:: rest

    ..  graphviz::

        graph {
            user [
                shape=plaintext;
                width=4;
                label="User";
                style="";
            ]
            view [
                shape=box;
                width=4;
                label=<<B>View</B><BR/>Displaying the data>;
            ]
            controller [
                shape=box;
                width=4;
                label=<<B>Controller</B><BR/>Control of functionality>;
            ]
            model [
                shape=box;
                width=4;
                label=<<B>Model</B><BR/>Domain model and domain logic>;
            ]
            user -- view -- controller -- model;
        }


:ref:`Diagrams <plantuml-diagrams>`
===================================

**How it looks:**

..  uml::

    == Initialization ==

    Alice -> Bob: Authentication Request
    Bob --> Alice: Authentication Response

    == Repetition ==

    Alice -> Bob: Another authentication Request
    Alice <-- Bob: another authentication Response

Source:

..  code-block:: rest

    ..  uml::

        == Initialization ==

        Alice -> Bob: Authentication Request
        Bob --> Alice: Authentication Response

        == Repetition ==

        Alice -> Bob: Another authentication Request
        Alice <-- Bob: another authentication Response


:ref:`Sidebar <rest-sidebar>`
=============================

Source / **How it looks**:

..  sidebar:: reST content elements

    * :ref:`Cards <rest-cards>`
    * :ref:`Tabs <rest-tabs>`
    * :ref:`Configuration values <rest-confval>`

..  code-block:: rst

    ..  sidebar:: reST content elements

        * :ref:`Cards <rest-cards>`
        * :ref:`Tabs <rest-tabs>`
        * :ref:`Configuration values <rest-confval>`
