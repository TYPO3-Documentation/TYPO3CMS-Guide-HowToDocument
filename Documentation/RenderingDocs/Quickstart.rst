
.. include:: ../Includes.txt
.. highlight:: bash

.. _render-documenation-with-docker:

===================================
Rendering Documentation with Docker
===================================

Here, we show the basic rendering commands for rendering locally with the official Docker container.

These commands work best on Linux, but may also work on Mac or Windows (depending
on your system). You should use a bash compatible shell, if possible.

.. tip::

   If these commands do not work on your platform, please
   see the more extensive `Docker Render Readme (GitHub) <https://github.com/t3docs/docker-render-documentation#quickstart-on-linux-or-macos>`__
   for additional information.

If you run into a problem while rendering, `report an issue <https://github.com/t3docs/docker-render-documentation/issues/new>`__
or :ref:`ask for help <get-help-on-writing-docs>`.


Run these commands in a terminal in the parent directory of the directory :file:`Documentation`.

Commands to Render Documentation
================================

.. code-block:: bash
   :linenos:

   docker pull t3docs/render-documentation
   source <(docker run --rm t3docs/render-documentation show-shell-commands)
   # If the command above will fail, please run the following three commands:
   # mkdir -p ~/bin
   # docker run --rm t3docs/render-documentation show-shell-commands > ~/bin/t3docs
   # source ~/bin/t3docs
   dockrun_t3rd makehtml
   xdg-open "Documentation-GENERATED-temp/Result/project/0.0.0/Index.html"

Explanations, the numbers correspond to the line numbers in code snippet:

#. **docker pull**
   You can run this every time before docker run, but it is not necessary
   unless you want to make sure the docker image gets updated.
   The next run will usually be faster because
   it will only pull (download) the Docker image again if a newer one is
   available.
#. **Prepare dockrun_t3rd:**
   This will not only run the Docker container, it
   will make the command `dockrun_t3rd` available in your current terminal.
   You must do this again for every new terminal you open.
#. **Render the documentation:** This will automatically find the documentation
   in the :file:`Documentation`
   subfolder. It will create a directory :file:`Documentation-GENERATED-temp`
   and write the results there.
#. **View the documentation:**
   You can now view the rendered documentation in your browser.

   On Mac use `open` and on Windows `start` instead of `xdg-open`.

   Look at the hints that are shown in the terminal.
   If you structured the documentation correctly, :file:`Index.rst` is
   always on the top level directory under the directory :file:`Documentation`.
   The renderer will create the file :file:`Index.html` from that. The path
   is always the same.

   If the open command does not work for you, create a URL you can open::

      echo "file://"$(pwd)/"Documentation-GENERATED-temp/Result/project/0.0.0/Index.html"


When you make additional changes, you can run step 3 again and reload the page
in your browser.


Example Aliases
===============

.. tip::

   Create aliases for the commands that work for you. Or add them to your
   profile. Example aliases are
   also listed in :ref:`t3contribute:aliases`.

   It might also be a good idea to create command shortcuts in your IDE.

.. code-block:: bash

   # run docker container and source shell commands
   alias t3docrun='source <(docker run --rm t3docs/render-documentation show-shell-commands)'

   # build docs
   alias t3docmake='dockrun_t3rd makehtml'

   # open generated docs in browser (uses t3open alias, see above)
   # - use xdg-open for Linux
   # - use open for Mac instead !!!
   alias t3docopen='xdg-open "file:///$(pwd)/Documentation-GENERATED-temp/Result/project/0.0.0/Index.html"'

   # remove generated docs
   alias t3docclean='rm -rf Documentation-GENERATED-temp/'

   # --- combined aliases ---

   # run docker, generate documenation and open result in browser
   alias t3doc='t3docrun && t3docmake && t3docopen'





