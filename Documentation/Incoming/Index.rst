
.. include:: ../Includes.txt
.. highlight:: shell


==============
Incoming Ideas
==============


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
