:orphan:

.. include:: Includes.txt

.. _Tip-of-the-day:

=============
Did you know?
=============

See also: :ref:`tips-extension-authors`


.. _tip-of-the-day-trigger-rebuild:
.. rst-class:: panel panel-default

Trigger Documentation Rendering on the Documentation Server
===========================================================

Usually, extension documentation should be rerendered automatically.

If you made a change that has been merged, but it is not yet visible,
do the following:

#. Wait up to 10 minutes
#. Reload your browser

You may also render the repository locally, to make sure there are
no build errors breaking the rendering. See :ref:`render-troubleshooting-errors`.

You can also look in the files in :file:`_buildinfo` online to see the
exitcodes and warnings. For example, for this manual:

https://docs.typo3.org/typo3cms/HowToDocument/stable/_buildinfo/

If this yields no results, you can iniate a rebuild:

To trigger a rebuild of a manual, click the "request_rebuild.php" file
in the respective .../\*.git.make folder.

Here are the links:

- Request rebuild for `the official TYPO3 CMS manuals <https://docs.typo3.org/~mbless/github.com/TYPO3-Documentation/TYPO3/>`_
- Request rebuild for `TYPO3 system extension manuals <https://docs.typo3.org/~mbless/git.typo3.org/TYPO3CMS/Extensions>`_
- Request rebuild for `manuals of extensions hosted on GitHub <https://docs.typo3.org/~mbless/github.com>`_



.. _tip-of-the-day-2017-02-13:
.. rst-class:: panel panel-default

'toctree' and the Hierarchical Structure of a Manual
====================================================

**Update:** Part of this description has been migrated to
:ref:`rest-menu-hierachy`.
(2019-01-06).

2017-02-13 by Martin Bless

TYPO3 documentation usually starts with a textfile :file:`PROJECT/Documentation/Index.rst`.
The text may go into more than one textfile and these can be "pulled in" and
referenced by the
`.. toctree:: <http://www.sphinx-doc.org/en/stable/markup/toctree.html>`__
directive. Note:

#. Each `.. toctree::` directive creates a *sublevel* of headlines in the menu.

#. The sublevel refers to the *current level*.

Problem
   Sometimes you don't get what you expect:

   .. code-block:: rst

      ================
      My Documentation
      ================

      Introduction
      ============
      This project does something very useful ...
      See the individual chapters.

      .. toctree::

         Chapter-1
         Chapter-2
         Chapter-3

   The example feels very natural. We are thinking of the introduction
   followed by the single chapters. Unfortunately we get something different.
   The chapters will all be a *subpart* of *Introduction* and not at the same level.
   It is exactly what the Sphinx documentation states and there is no easy way to
   "tweak" this behavior.

Solution
   Use these rules of thumb:

   #. All or nothing: Pull in *all* content of a given level via `toctree`
      or don't use `toctree` at all.

   #. Or, in other words:
      Do not use a headline ("section") in a document before a `.. toctree::`
      directive unless you really want to place the pulled in documents
      at a *sublevel of that section*.

   Here is how we can fix the example: Move the introduction to an extra
   file and pull it in just like the others.

   **Fixed example:**

   .. code-block:: rst

      ================
      My Documentation
      ================

      You can have text here. But don't introduce headlines,
      if you want to have the pulled in files at the same level.

      .. toctree::

         Introduction
         Chapter-1
         Chapter-2
         Chapter-3

   Now the *document titles* (not shown here) of the files :file:`Introduction.rst`,
   :file:`Chapter-1.rst`, :file:`Chapter-2` and :file:`Chapter-3` will all be at the
   sublevel of `My Documentation` in the menu.


.. _tip-of-the-day-2016-10-08:
.. rst-class:: panel panel-default

How to Write Inline Code
========================

**Update:** This information has been migrated to :ref:`Inline-Code`
and extended (2019-01-06).


2016-10-08 by Martin Bless

Preferred: Use Single Backticks ` ... `
---------------------------------------

1. In general we are using `interpreted text roles`_ for small inline
   code snippets. Surround the code by *single backticks* and don't start or end
   the code with whitespace. Example: Type ```2 + 2 = 4``` to get `2 + 2 = 4`
   as result.

2. Just write the code as it is - don't escape or double anything.

3. Even better: Explicitly specify what kind of code (= textrole) it is. This better shows
   the semantics and in the output there may be a a special coloring or highlighting (on the way):

   ================ ================================================= ============================================ ===
   Role             Source                                            Output                                       Note
   ================ ================================================= ============================================ ===
   (default)        ```result = (1 + x) * 32```                       `result = (1 + x) * 32`                      This works because in :file:`Includes.txt` we set the default role to ``:code:`...```
   aspect           ``:aspect:`Description:```                        :aspect:`Description:`                       For better optics
   code             ``:code:`result = (1 + x) * 32```                 :code:`result = (1 + x) * 32`
   file             ``:file:`/etc/passwd```                           :file:`/etc/passwd`
   js               ``:js:`var f = function () {return 1;}```         :js:`var f = function () {return 1;}`
   html             ``:html:`<a href="#">```                          :html:`<a href="#">`
   ts               ``:ts:`lib.hello.value = Hello World!```          :ts:`lib.hello.value = Hello World!`
   typoscript       ``:typoscript:`lib.hello.value = Hello World!```  :typoscript:`lib.hello.value = Hello World!`
   php              ``:php:`$result = $a + 23;```                     :php:`$result = $a + 23;`
   ================ ================================================= ============================================ ===


When to Use Literal Code \`\`...``
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



.. _tip-of-the-day-2016-09-11:
.. rst-class:: panel panel-default

Optional: Add borders to Your Images
====================================

**Update:** It is now also possible to add a drop shadow (`:class: with-shadow`)
to images. For an up-to-date
description of how to embed images, see
:ref:`how-to-document-images` (2019-01-06).

2016-09-11 by Martin Bless

The next version of the `t3SphinxThemeRtd`_ (following 3.6.0) will know a general css class `with-border`.
Some images look best without an extra border because their outline is clearly visible. Others benefit from
having a border because they are not separated enough from the background. Example:

.. _t3SphinxThemeRtd: https://github.com/TYPO3-Documentation/t3SphinxThemeRtd

1. Here is the markup to include an image as a 'figure'. Figures always are of css type 'block' and can have
   a caption::

      .. figure:: images/2016-09-11-2.png


2. And this is what we see. The image is not clearly distinguished:

   .. figure:: images/2016-09-11-2.png

3. Now the same markup plus the extra class::

      .. figure:: images/2016-09-11-2.png
         :class: with-shadow

   .. figure:: images/2016-09-11-2.png
      :class: with-shadow



