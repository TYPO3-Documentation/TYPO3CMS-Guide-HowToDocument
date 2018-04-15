
.. include:: ../Includes.txt
.. highlight:: shell


=======================
Incoming Text Fragments
=======================


What is a TYPO3 documentation?
==============================

((to be written))

Let's assume you have some kind of TYPO3 project. In the context of this
documentation we represent that project by its folder. This could be for
example :file:`my_cool_extension`. In the terminology here that would be
:file:`The_Project`.

The official way to add documentation to that project according to our
conventions goes like this: You create a subfolder :file:`Documentation` and in
that subfolder you start with a text file :file:`Index.rst`. Things you write
there will be the contents of the starting page of your documentation once it
is rendered.

For the following we assume that you are already within the rootfolder of your
project. That is, we assume that you changed directory (`cd The_Project`)
there. The dot (`.`) represent that folder in the following text.

Q:
   Add "TYPO3 documentation" to your project - what does that mean?

A:
   It has "TYPO3 documentation" if the toolchain at the TYPO3 documentation
   server can find something in your project that it can render to html and
   and display nicely on the documentation server.

Q:
   What "TYPO3 documentation" is detected by the documentation renderer?

A:
   Your project should have a file :file:`The_Project/Documentation/Index.rst`.
   This is the top number one choice.

   Since we can't force the world to be an ideal place some fallbacks are
   detected as well. At the moment these different cases are handled with
   priority in this order:

   .. rst-class:: compact-list

   1. :file:`./Documentation/Index.rst`
   2. :file:`./Documentation/index.rst`
   3. :file:`./Documentation/Index.md`
   4. :file:`./Documentation/index.md`
   5. :file:`./README.rst`
   6. :file:`./README.md`
   7. :file:`./doc/manual.sxw`

   If none of these files exist then NO documentation will be rendered.

Q:
   I want to follow this advice and start with a
   :file:`./Documentation/Index.rst`. Is there a more advanced example that I
   can copy from?

A:
   Yes, there is. Get a copy of this T3DocumentationStarter project and start
   with that folder :file:`./Documentation`:

   https://github.com/T3DocumentationStarter/Public-Info-000

Q:
   Ok, I understand that I can write documentation in textfiles in the
   :file:`./Documentation` folder using reST markup. But how can I turn that
   into that nice looking html format I see on the server?

A:
   Since recently this can be easily done if you are using Linux or Mac and
   Docker. It will work with Docker for Windows as well. It's only the 'how-to'
   that's missing for that. So, if you are on Windows and you have Docker, go
   ahead and contribute to the README file.

   To render the documentation locally with Docker: Follow the README at
   https://github.com/t3docs/docker-render-documentation

Q:
   What is happening when I run that Docker container?

A:
   You should start the Docker container at the commandline IN THE ROOTFOLDER
   of your project::

      cd The_Project
      dockrun_t3rdf makehtml

   It may take a minute or two and you should see some printings in the
   terminal window. As a result you should find a folder
   :file:`Documentation-GENERATED-temp`. For example::

      The_Project/
      The_Project/Documentation/
      The_Project/Documentation-GENERATED-temp/

   The rendering normally ends with this hints:

   .. code-block:: none

      Find the (possible) results. For example:

         ./Documentation-GENERATED-temp/.../Index.html
         ./Documentation-GENERATED-temp/.../singlehtml/Index.html
         ./Documentation-GENERATED-temp/.../_pdf/
         ./Documentation-GENERATED-temp/.../_buildinfo/
         ./Documentation-GENERATED-temp/.../_buildinfo/latex/
         ./Documentation-GENERATED-temp/.../_buildinfo/warnings.txt

      The html startpage should be:

         ./Documentation-GENERATED-temp/typo3cms/drafts/project/0.0.0/Index.html

      Please watch out for info about what has happened
      during the rendering:

         ./Documentation-GENERATED-temp/typo3cms/drafts/project/0.0.0/_buildinfo/
         ./Documentation-GENERATED-temp/typo3cms/drafts/project/0.0.0/_buildinfo/README.html
         ./Documentation-GENERATED-temp/typo3cms/drafts/project/0.0.0/_buildinfo/warnings.txt

   .. tip::

      Add 'GENERATED' to your global :file:`~/.gitignore_global`. As an example
      that might look like:

      .. code-block:: none

         *NOT_VERSIONED*
         *GENERATED*
         .idea

((more to be written))


How to start Documentation for Your TYPO3 Extension
===================================================

2016-12-29 by Martin Bless

**Quickstart:**

-  Get yourself one of the T3DocumentationStarter projects that look like
   https://docs.typo3.org/typo3cms/drafts/github/T3DocumentationStarter/Public-Info-000/

-  Read the frontpage of the starter to learn how it works.

-  You may edit directly at Github. Just do a little update and save (=push),
   and some very few minutes later you can reload the page and see what the
   server has rendered for you. You don't have to install or render anything yourself.
   The server will do that for you.

-  Or work with Github as you usually do.

-  To become the owner of a starter project send a mail with your **Github username**
   to the docteam to documentation@typo3.org and ask for a T3DocumentationStarter project.

-  Later: Copy the :file:`./Documentation` folder of the starter project to your extension.
   Write your documentation. Edit the metadata in :file:`./Documentation/Settings.cfg` and
   you are done.

Come to the sunny side of documentation - have fun!



File structure
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


Including files
---------------

*Recapitulation:* Each rst- or md-file will result in a url of its own. At parsing level
these files are processed independently. Toctree directives are controlling the 
menu hierarchy of the contents. For each file intermediate results are stored
and each file will be processed during build.

Some documentation projects have the same snippet of text appear in several places.
In this case it may make sense to *include* text snippets. The `.. include::`
directive does this. What you need to know about *including* files:

1. Includes are performed on a textual basis. 
2. Includes are processed in a very fast manner when the parent file is parsed.
3. Includes do not lead to intermediate results that need to be resolved during build.
4. Since includes are treated as if the text had been written exactly
   where the include is done the text needs to fit with respect to
   indentation ((verify this)) and section levels.
5. You cannot see the source of included text when clicking on "Show source of the page".
6. The "Edit me on Github" button cannot take you directly to the editing of included files.
   It still can be done but needs much more knowledge about the Github interface.

.. attention::

   Includes can easily cause trouble. Think well before using them.
   
.. important::

   Do not use the file endings :file:`.rst` or :file:`.md` for include files
   to prevent Sphinx from treating them as individual source files! In case
   you have many include files this would lead to many warnings and slow down
   the build process considerably.
   
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


Markup: reST
============

((to be written))

TYPO3 documentation uses `reStructuredText` for markup. The rendering chain and tools are built
and optimized to process reST markup. Please go ahead and use that format.

The file ending of reST files is :file:`.rst`.

You can use reST format at Github as well.

You can write H1 and H2 headlines in markdown the same way as reST does it. So for simple
documents like a README file the markup can almost be the same.

The tool `pandoc` can convert existing markdown file into reST format. Do this once and
you are in line with the TYPO3 conventions.

Markup: Markdown
================

One problem with markdown is that there are many dialects. Since a while there is a standard "commonmark".
At https://readthedocs.org people are trying to make commonmark available. See http://blog.readthedocs.com/adding-markdown-support/ for the details. Without doing lots of investigations we have implemented the same
solution for TYPO3 documentation as well. 

This means that our rendering tools detect markdown files as well. They have :file:`.md` as file ending.

If you're encountering problems with the rendering of your markdown files consider switching to reST.
