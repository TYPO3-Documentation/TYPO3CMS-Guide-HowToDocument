.. include:: ../Includes.txt
.. highlight:: bash

.. _rendering-docs-quickstart:


===================================
Rendering Documentation with Docker
===================================

We offer a Docker image for rendering the documentation on your local computer. Using
our Docker image you do not have to install the required packages (e.g. sphinx) on your
computer.

Please refer to the documentation in the `t3docs/docker-render-documentation
<https://github.com/t3docs/docker-render-documentation/blob/master/README.rst>`__
project on GitHub.


Following is a short summary of the basic commands you will typically use. Once
you have `installed Docker <https://www.docker.com/get-started>`__, this should
"just work". If you do run into problems,
please see `t3docs/docker-render-documentation
<https://github.com/t3docs/docker-render-documentation/blob/master/README.rst>`__
, check the :ref:`rendering-docs-troubleshooting`
page or :ref:`ask for help <how-to-get-help>`.


Run these in a terminal in the parent directory of the Documenation directory:

.. code-block:: bash
  :linenos:

   source <(docker run --rm t3docs/render-documentation show-shell-commands)
   dockrun_t3rdf makehtml
   # on MacOS
   open "Documentation-GENERATED-temp/Result/project/0.0.0/Index.html"
   # on Linux
   xdg-open "Documentation-GENERATED-temp/Result/project/0.0.0/Index.html"
   # on Windows
   start "Documentation-GENERATED-temp/Result/project/0.0.0/Index.html"


#. line 1: **Prepare Docker:**
   This will not only pull the image and run the Docker container, it
   will make the commands like `dockrun_t3rdf` available in your current terminal.
   You must do this again for every new terminal you open.
   This command may take a while. The next run will be faster because
   it won't have to pull the Docker image again!
#. line 2: **Render the documentation:** This will automatically find the documentation
   in the :file:`Documentation`
   subfolder. It will create a directory :file:`Documentation-GENERATED-temp`
   and write the results there.
#. line 3 etc.: **View the documentation:**
   You can now view the rendered documentation in your browser.
   Look at the hints that are shown in the terminal.
   If you structured the documentation correctly, :file:`Index.rst` is
   always on the top level directory under the directory :file:`Documentation`.
   The renderer will create the file :file:`Index.html` from that. The path
   is always the same.
   So, depending on what operating system you are on and how it is configured,
   you can use one of the command above for opening the startpage Index.html in the browser.


When you make additional changes, you can repeat, starting with step 2.

Press reload (e.g. CTRL-r) in your browser to view the changes.

.. tip::

   Create aliases for the commands that work best for you now!

