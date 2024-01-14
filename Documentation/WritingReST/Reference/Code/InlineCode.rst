
..  include:: /Includes.rst.txt
..  highlight:: rst
..  index::
    reST; Inline code
..  _Inline-Code:

========================
Inline code & text roles
========================


..  hint::

  Too much inline code can make the information on a page highly
  unreadable. If this is the case, consider using
  :ref:`writing-rest-codeblocks-with-syntax-highlighting`.


..  index:: reST; Markup

How to semantically mark up specific text
=========================================

There are several ways to semantically mark specific parts of the text. The main goal is to be able to use
a consistent style for specific parts of the text, for example code fragments, file names and GUI
elements.

..  index:: reST; Text roles
..  _text-roles:

Using text roles
----------------

1.  **Preferred:** Use `Sphinx interpreted text roles <http://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html>`__
    to explicitly specify what kind of text / code (text role) it is. This shows
    the semantics and in the output there may be a a special coloring or highlighting:

    ================ ================================================= ============================================= ====
    Role             Source                                            Output                                        Note
    ================ ================================================= ============================================= ====
    (default)        ```result = (1 + x) * 32```                       `result = (1 + x) * 32`                       This works because in :file:`Includes.rst.txt` we set the default role to ``:code:`...```

    aspect           ``:aspect:`Description:```                        :aspect:`Description:`                        For better optics
    bash             ``:bash:`find . -type d | grep typo3```           :bash:`find . -type d | grep typo3`
    css              ``:css:`.h1 {font-size:150%}```                   :css:`.h1 {font-size:150%}`
    html             ``:html:`<a href="#">```                          :html:`<a href="#">`
    issue            ``:issue:`12345```                                :issue:`12345`                                To link to a TYPO3 issue.
    js               ``:js:`var f = function () {return 1;}```         :js:`var f = function () {return 1;}`
    php              ``:php:`$result = $a + 23;```                     :php:`$result = $a + 23;`
    rst              ``:rst:`..  image:: /path/to/img.jpg```            :rst:`..  image:: /path/to/img.jpg`
    sep              ``:sep:`|```                                      :sep:`|`                                      To give the separator '\|' a special style in some contexts like :ref:`Styled-Definition-Lists`
    sql              ``:sql:`SELECT * FRAM pages WHERE hidden=0;```    :sql:`SELECT * FRAM pages WHERE hidden=0;`
    typoscript       ``:typoscript:`lib.hello.value = Hello World!```  :typoscript:`lib.hello.value = Hello World!`
    xml              ``:xml:`<?xml version="1.0" encoding="UTF-8"?>``` :xml:`<?xml version="1.0" encoding="UTF-8"?>`
    yaml             ``:yaml:`- {name: John Smith, age: 33}```         :yaml:`- {name: John Smith, age: 33}`
    ================ ================================================= ============================================= ====





    `Standard Sphinx interpreted text roles
    <http://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#other-semantic-markup>`__:

    ================ ================================================= ============================================ ===
    Role             Source                                            Output                                       Note
    ================ ================================================= ============================================ ===
    abbr             ``:abbr:`LIFO (last-in, first-out)```             :abbr:`LIFO (last-in, first-out)`            An abbreviation. If the role content contains a parenthesized explanation, it will be treated specially: it will be shown in a tool-tip in HTML, and output only once in LaTeX.
    code             ``:code:`result = (1 + x) * 32```                 :code:`result = (1 + x) * 32`
    command          ``:command:`rm```                                 :command:`rm`                                The name of an OS-level command, such as rm.
    dfn              ``:dfn:`something```                              :dfn:`something`                             Mark the defining instance of a term in the text. (No index entries are generated.)
    file             ``:file:`/etc/passwd```                           :file:`/etc/passwd`
    guilabel         ``:guilabel:`&Cancel```,                          :guilabel:`&Cancel`,                         Labels presented as part of an interactive user interface should be marked using guilabel. This includes labels from text-based interfaces such as those created using curses or other text-based libraries. Any label used in the interface should be marked with this role, including button labels, window titles, field names, menu and menu selection names, and even values in selection lists.
                     ``:guilabel:`O&k```,                              :guilabel:`O&k`,
                     ``:guilabel:`&Reset```,                           :guilabel:`&Reset`,
                     ``:guilabel:`F&&Q```                              :guilabel:`F&&Q`
    kbd              ``Press :kbd:`ctrl` + :kbd:`s```                  Press :kbd:`ctrl` + :kbd:`s`                 Mark a sequence of keystrokes. What form the key sequence takes may depend on platform- or application-specific conventions. When there are no relevant conventions, the names of modifier keys should be spelled out, to improve accessibility for new users and non-native speakers. For example, an xemacs key sequence may be marked like :kbd:`C` + :kbd`x`, :kbd:`C` + :kbd:`f`, but without reference to a specific application or platform, the same sequence should be marked as :kbd:`ctrl` + :kbd:`x`, :kbd:`ctrl` + :kbd:`f`.
    mailheader       ``:mailheader:`Content-Type```                    :mailheader:`Content-Type`                   The name of an RFC 822-style mail header. This markup does not imply that the header is being used in an email message, but can be used to refer to any header of the same “style.” This is also used for headers defined by the various MIME specifications. The header name should be entered in the same way it would normally be found in practice, with the camel-casing conventions being preferred where there is more than one common usage.
    ref              ``:ref:`Inline-Code```                            :ref:`Inline-Code`                           Sphinx cross-referencing
    ================ ================================================= ============================================ ===

    `Standard Docutils interpreted text roles
    <http://docutils.sourceforge.net/docs/ref/rst/roles.html#standard-roles>`__:

    ..  tip::

        For more information about the `ref` directive, see :ref:`how-to-document-hyperlinks`.

    ================== ================================================= ============================================ ===
    Role               Source                                            Output                                       Note
    ================== ================================================= ============================================ ===
    emphasis           ``:emphasis:`text`, *text*``                      :emphasis:`text`, *text*
    literal            ``:literal:`\ \ abc```                            :literal:`\ \ abc`
    literal            ``:literal:`text`, ''text''`` (backticks!)        :literal:`text`, ``text``
    math               ``:math:`A_\text{c} = (\pi/4) d^2```              :math:`A_\text{c} = (\pi/4) d^2`             The math role marks its content as mathematical notation (inline formula). The input format is LaTeX math syntax without the “math delimiters“ ($ $).
    rfc, rfc-reference ``:RFC:`2822```                                   :RFC:`2822`
    strong             ``:strong:`text`, **text**``                      :strong:`text`, **text**                     Implements strong emphasis.
    subscript          ``:subscript:`subscripted```                      :subscript:`subscripted`
    superscript        ``:superscript:`superscripted```                  :superscript:`superscripted`
    t, title-reference ``:t:`Design Patterns```                          :t:`Design Patterns`                         The :title-reference: role is used to describe the titles of books, periodicals, and other materials.
    ================== ================================================= ============================================ ===


2.  As an alternative, you can use the default text role for small inline
    code snippets, but it is better to use specific text roles. However, if no
    text role exists, you may use this to mark the text.

    Surround the code by *single backticks* and don't start or end
    the code with whitespace. Example: Type ```2 + 2 = 4``` to get `2 + 2 = 4`
    as result.

3.  Just write the code as it is. This may make the text more difficult to read.
    Use your common sense.

..  index:: reST; Literal code

When to use literal code \`\`...``
----------------------------------

Things get tricky if your inline code already contains single backquotes (backticks).

4.  In many cases you can still use the *interpreted text role* as described in 1. to 3.
    For example we can write ``:code:`:html:`<br>```` to get :code:`:html:`<br>``

    This is possible if (a) your code doesn't start with a backtick and (b) if no backtick in
    your code has a trailing whitespace.

5.  **But:** To be really free to include inline any code containing backticks you will want to use
    `inline literals`_. Again: Don't escape or double anything, whitespace is maintained.
    *Example:*

    Write::

        SQL-example code: ``SELECT  `tt_content` . `bodytext`  AS  `t1` . `text`;``

    to get:

    SQL-example code: ``SELECT  `tt_content` . `bodytext`  AS  `t1` . `text`;``

    **The drawbacks** of literal inline code notation are:

    *   there is no way to semantically classify the kind of code
    *   there is no special coloring or highlighting
    *   the raw reST code looks less beautiful and is less readable

..  _interpreted text roles: http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#interpreted-text
..  _inline literals: http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#inline-literals

Inline code versus code blocks
==============================

The name for - very - small code snippets that occur within normal text flow
within sentences is *inline code*.

*inline code*

*   is styled somewhat differently,
*   has **no** syntax highlighting,
*   does **not** need to be syntactically correct,
*   can be compared to `<span>...</span>` tags in html

In contrast, *code-blocks*

*   appear "as a box",
*   can have syntax highlighting,
*   need to be syntactically correct in order to have highlighting,
*   can be compared to `<pre>...</pre>` blocks in html,
*   use predefined names for the different languages that come with Pygments,
    the syntax highlighter.


Definition of text roles
========================

For all officials TYPO3 manuals `php` is set as default highlight
language with the exception of the TypoScript manuals, where `typoscript` is
the default.

You need a custom text role?
----------------------------

You need another 'language' to mark up inline?

You are free to define additional text roles *in your project* or even
*on an individual page* as you like. Make use of the `role directive
<http://docutils.sourceforge.net/docs/ref/rst/directives.html#role>`__.
Example: You want 'haskell'? Define that role as derivative of 'code'::

  ..  role:: haskell(code)

You may then write::

    Here is some :haskell:`haskell inline code` in the sentence.

The immediate advantage will be that you can explicitly markup your source
code semantically and declare snippets to be 'Haskell'. The visual appearance
will be that of 'code' until a special css class has been defined. Feel free to
open a request `here
<https://github.com/TYPO3-Documentation/t3SphinxThemeRtd/issues>`__. Look at
this html to understand the technical background:


..  code-block:: html

    <code class="code haskell docutils literal">
        <span class="pre">haskell inline code</span>
    </code>

A default styling for :html:`class="code"` exists and is in effect until
overridden by a special styling :html:`class="code.haskell"` that needs to
be defined.
