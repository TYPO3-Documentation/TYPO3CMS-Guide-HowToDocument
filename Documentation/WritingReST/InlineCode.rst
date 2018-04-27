
.. include:: ../Includes.txt
.. highlight:: rst

===========
Inline Code
===========

'inline code' versus 'code-blocks'
==================================

The name for - very - small code snippets that occur within normal text flow
within sentences is *inline code*.

*inline code*

- is styled somewhat differently,
- has **no** syntax highlighting,
- does **not** need to be syntactically correct,
- can be compared to `<span>...</span>` tags in html,
- and is made up by self-defined names. For example, look at the :file:`../../Includes.txt`
  file to see how `:php:`, `:ts:` are defined.

In contrast, *code-blocks*

- appear "as a box",
- can have syntax highlighting,
- need to be syntactically correct in order to have highlighting,
- can be compared to `<pre>...</pre>` blocks in html,
- use predefined names for the different languages that come with Pygments,
  the syntax highlighter.



How to write inline code
========================

2016-10-08 by Martin Bless

Preferred: Use single backticks ` ... `
---------------------------------------

1. In general we are using `interpreted text roles`_ for small inline
   code snippets. Surround the code by *single backticks* and don't start or end
   the code with whitespace. Example: Type ```2 + 2 = 4``` to get `2 + 2 = 4`
   as result.

2. Just write the code as it is - don't escape or double anything.

3. Even better: Explicitely specify what kind of code (= textrole) it is. This better shows
   the semantics and in the output there may be a a special coloring or highlighting (on the way):

   ================ ================================================= ============================================ ===
   Role             Source                                            Output                                       Note
   ================ ================================================= ============================================ ===
   (default)        ```result = (1 + x) * 32```                       `result = (1 + x) * 32`                      This works because in :file:`Includes.txt` we set the default role to ``:code:`...```
   aspect           ``:aspect:`Description:```                        :aspect:`Description:`                       For better optics
   code             ``:code:`result = (1 + x) * 32```                 :code:`result = (1 + x) * 32`
   file             ``:file:`/etc/passwd```                           :file:`/etc/passwd`
   html             ``:html:`<a href="#">```                          :html:`<a href="#">`
   js               ``:js:`var f = function () {return 1;}```         :js:`var f = function () {return 1;}`
   kbd              ``Press :kbd:`ctrl` + :kbd:`s```                  Press :kbd:`ctrl` + :kbd:`s`
   php              ``:php:`$result = $a + 23;```                     :php:`$result = $a + 23;`
   sep              ``:sep:`|```                                      :sep:`|`                                     To style the separator '\|'
   ts               ``:ts:`lib.hello.value = Hello World!```          :ts:`lib.hello.value = Hello World!`
   typoscript       ``:typoscript:`lib.hello.value = Hello World!```  :typoscript:`lib.hello.value = Hello World!`
   ================ ================================================= ============================================ ===


When to use literal code \`\`...``
----------------------------------

Things get tricky if your inline code already contains single backquotes (backticks).

4. In many cases you can still use the *interpreted textrole* as described in 1. to 3.
   For example we can write ``:code:`:html:`<br>```` to get :code:`:html:`<br>``

   This is possible if (a) your code doesn't start with a backtick and (b) if no backtick in
   your code has a trailing whitespace.

5. **But:** To be really free to include inline any code containing backticks you will want to use
   `inline literals`_. Again: Don't escape or double anything, whitespace is maintained.
   *Example:*

      Write

         .. code-block:: rst

            SQL-example code: ``SELECT  `tt_content` . `bodytext`  AS  `t1` . `text`;``

      to get:

         SQL-example code: ``SELECT  `tt_content` . `bodytext`  AS  `t1` . `text`;``

   **The drawbacks** of literal inline code notation are:

   -  there is no way to semantically classify the kind of code
   -  there is no special coloring or highlighting
   -  the raw reST code looks less beautiful and is less readable

.. _interpreted text roles: http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#interpreted-text
.. _inline literals: http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#inline-literals

