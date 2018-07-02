.. include:: ../Includes.txt

==============
File Structure
==============

((to be written))

Source files
------------

Everything that belongs to the documentation of a project must reside
in a subfolder :file:`PROJECT/Documentation` and below. The only exception
are readme files. A readme file :file:`PROJECT/README.rst` or :file:`PROJECT/README.md`
will be respected and rendered if no other starter file is found.
See `Rendering of README files`_ below.

At the beginning Sphinx will parse each and every reST file (:file:`*.rst`)
and each and every markdown file (:file:`*.md`). Sphinx saves the parsed content
and the resulting structure in intermediate file. Each file is parsed on its own
so the markup of headlines ("section titles") may be different but lead to the
same result.

((Sphinx will then start build the project...)) Sphinx needs to know about a single
file to start with. The file is called the "masterdoc". The masterdoc can use the
`.. toctree::` directive to pull other files in. The hierarchy of those toctree
directives defines the menu hierarchy in the output.

The file hiearchy on disc does not affect the menu hierarchy in any way.

Usually it is desired to have each and every rst- or md-file appear in the menu
somewhere. Sphinx will issue a warning if this isn't the case.

*Hint:* If really needed an input file may be tagged as `:orphan:` right at the beginning.
This will suppress the warning.

.. _how-to-document-including-files:

Including files
---------------

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
   indentation ((verify this)) and section levels.

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
   the build process considerably. Think of using :file:`*.rst.txt`.
   The ending :file:`.rst.txt` can be used in PhpStorm and :file:`.editorconfig`
   to define a reST file type.

.. warning::

   You cannot include files from outside the :file:`Documentation/` folder.


Rendering of README files
-------------------------

The TYPO3 buildchain cares about a :file:`README(.rst|.md)` only if no other
file to start with ("masterdoc") is found. Internally this is happening:

1. The folder :file:`PROJECT/Documentation` is copied to `PROJECT/Documentation/Documentation`.
2. The README file is copied to :file:`PROJECT/Documentation/Index(.rst|.md)`.
3. The whole process then continues normally.

In other words: If the expected start file (masterdoc) is missing but a README
file is present, we copy the README file to the expected place. This moves the
file down one level to a subfolder. Do keep everything relative we move down
the folder :file:`Documentation` one level as well to :file:`Documentation/Documentation`.
