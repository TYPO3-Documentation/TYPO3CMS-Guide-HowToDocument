.. include:: /Includes.rst.txt
.. highlight:: bash
.. Index:: Rendering; Docker
.. _render-documenation-with-docker:
.. _render-documentation-with-docker:

=======================================
Rendering the documentation with Docker
=======================================

Here, we show the basic rendering commands for rendering locally with the official Docker container.

These commands work best on Linux, but may also work on Mac or Windows (depending
on your system). You should use a bash compatible shell, if possible.

If you run into a problem while rendering, check :ref:`rendering-docs-troubleshooting`,
`report an issue <https://github.com/t3docs/docker-render-documentation/issues/new>`__
or :ref:`ask for help <get-help-on-writing-docs>`.


Run these commands in a terminal in the parent directory of the directory :file:`Documentation`.

Prerequisites
=============

Install Docker:

*  https://docs.docker.com/install/


.. Index:: Rendering; Commands

Commands to render the documentation
====================================

.. rst-class:: bignums-xxl

#. Preparations

   The docker image is not listed on dockerhub (hub.docker.com) anymore, therefor some perparations 
   need to be done once
   
   .. code-block:: bash
   
      docker pull ghcr.io/t3docs/render-documentation:v3.0.dev30
      docker tag ghcr.io/t3docs/render-documentation:v3.0.dev30 t3docs/render-documentation:develop

#. Make dockrun_t3rd available in current terminal

   .. code-block:: bash
      
      source <(docker run --rm t3docs/render-documentation show-shell-commands)

   .. tip::

      If this command does not work on your platform,
      look at :ref:`render-troubleshooting-source`
      for alternatives.

#. Run dockrun_t3rd

   Please use this command in the parent folder of your documentation. In most cases you will
   have a folder :file:`Documentation`. You must run this command one level above.

   .. code-block:: bash

      dockrun_t3rd makehtml

#. Open generated documentation

   Look at the output of the previous command to see where the
   generated documentation is located or use one of these commands
   to directly open the start page in a browser:

   .. tabs::

      .. group-tab:: Linux

         .. code-block:: bash

            xdg-open "Documentation-GENERATED-temp/Result/project/0.0.0/Index.html"

      .. group-tab:: MacOS

         .. code-block:: bash

            open "Documentation-GENERATED-temp/Result/project/0.0.0/Index.html"

      .. group-tab:: Windows

         .. code-block:: powershell

            start "Documentation-GENERATED-temp/Result/project/0.0.0/Index.html"


Explanations
============

The numbers correspond to the steps:


#. **Prepare dockrun_t3rd:**
   This will run the Docker container, in order to
   make the command `dockrun_t3rd` available in your current terminal.
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


When you make additional changes, you can run step 2 again and reload the page
in your browser.


Example aliases
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

   # run docker, generate documentation and open result in browser
   alias t3doc='t3docrun && t3docmake && t3docopen'
