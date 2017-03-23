
.. include:: ../../Includes.txt
.. highlight:: rst

=================
The Menu Hiearchy
=================


'toctree' and the hierarchical structure of a manual
====================================================

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
   follwed by the single chapters. Unfortunately we get something different.
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

