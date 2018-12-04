.. include:: ../Includes.txt
.. highlight:: rst

.. _including-files:

===============
Including Files
===============


*Recapitulation:* Each rst- or md-file will result in a url of its own. At parsing level
these files are processed independently. Toctree directives are controlling the
menu hierarchy of the contents. For each file intermediate results are stored
and each file will be processed during build.

Some documentation projects have the same snippet of text appear in several places.
In this case it may make sense to *include* text snippets. The `.. include::`
directive does this. What you need to know about *including* files:

.. _how-to-document-including-files-advantages:

Advantages
~~~~~~~~~~
#. Includes are performed on a textual basis and therefore
   processed in a very fast manner when the parent file is parsed.

#. Includes do not lead to intermediate results that need to be resolved during build.

.. _how-to-document-including-files-disadvantages:

Disadvantages
~~~~~~~~~~~~~
#. Since includes are treated as if the text had been written exactly
   where the include is done the text needs to fit with respect to
   the section levels.

#. You cannot see the source of included text when clicking on "Show source of the page".

#. The "Edit me on Github" button cannot take you directly to the editing of included files.
   It still can be done but needs much more knowledge about the Github interface.

#. When Sphinx reports warnings and errors the exact text location can be much harder to spot.

.. _how-to-document-including-files-recommendations:

Recommendations
~~~~~~~~~~~~~~~

.. attention::

   Includes can easily cause trouble. Think well before using them.

.. important::

   Do not use the file endings :file:`.rst` or :file:`.md` for include files
   to prevent Sphinx from treating them as individual source files! In case
   you have many include files this would lead to many warnings and slow down
   the build process considerably. Use :file:`*.rst.txt`.
   The ending :file:`.rst.txt` can be used in PhpStorm and :file:`.editorconfig`
   to define a reST file type.

.. warning::

   You cannot include files from outside the :file:`Documentation/` folder.

