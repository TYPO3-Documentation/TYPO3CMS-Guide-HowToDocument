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



Render on Linux
===============

Run these in a terminal in the parent directory of the Documentation directory every
time you wish to render:

.. code-block:: bash
  :linenos:

   docker pull t3docs/render-documentation
   source <(docker run --rm t3docs/render-documentation show-shell-commands)
   dockrun_t3rdf makehtml
   xdg-open "Documentation-GENERATED-temp/Result/project/0.0.0/Index.html"

#. Line 1: **docker pull**
   You can run this every time before docker run, but it is not necessary
   unless you want to make sure the docker image gets updated. 
   The next run will usually faster because
   it will only pull (download) the Docker image again if a newer one is
   available.
#. Line 2: **Prepare dockrun_t3rdf:**
   This will not only run the Docker container, it
   will make the command `dockrun_t3rdf` available in your current terminal.
   You must do this again for every new terminal you open.
   This command may take a while. 
#. line 3: **Render the documentation:** This will automatically find the documentation
   in the :file:`Documentation`
   subfolder. It will create a directory :file:`Documentation-GENERATED-temp`
   and write the results there.
#. line 4 etc.: **View the documentation:**
   You can now view the rendered documentation in your browser.
   Look at the hints that are shown in the terminal.
   If you structured the documentation correctly, :file:`Index.rst` is
   always on the top level directory under the directory :file:`Documentation`.
   The renderer will create the file :file:`Index.html` from that. The path
   is always the same.
   If xdg-open does not work for you, create a URL you can open::
   
      echo "file://"$(pwd)/"Documentation-GENERATED-temp/Result/project/0.0.0/Index.html"


When you make additional changes, you can run step 3 again and reload page
in browser.

.. tip::

   Press reload (e.g. :kbd:`ctrl + r`) in your browser to view the changes.

Render on MacOS
===============

Run the same commands as for Linux but replace xdg-open with open::

   open "Documentation-GENERATED-temp/Result/project/0.0.0/Index.html"
   
If open does not work for you, create a URL you can open::
   
   echo "file://"$(pwd)/"Documentation-GENERATED-temp/Result/project/0.0.0/Index.html"

You may also want to try :ref:`render-with-docker-compose` for an 
alternative workflow.

Render on Windows
=================

On Windows, it depends what kind of a shell (terminal) you are using.

* With Cygwin, the Linux workflow should work. Just replace xdg-open with start
* With Powershell, you might want to replace `source` with `.`::

      docker run --rm t3docs/render-documentation show-shell-commands > start.bat
      . .\start.bat
      

As an alternative, try :ref:`render-with-docker-compose`.


.. _render-with-docker-compose:

Render With Docker Composer
===========================


.. important::

   This section is currently under construction. 

The commands previously described may not work on your system. Additionally,
you may find that once you have set it up, working with Docker Compose
will simplify the workflow.

Prerequisites:

* Additionally to Docker, you will need to install Docker Compose. On Mac
  or Windows this will most likely already be the case, see `Install Docker Compose
  <https://docs.docker.com/compose/install/>`__: *On desktop systems like Docker
  Desktop for Mac and Windows, Docker Compose is included as part of those desktop installs.*
  
#. Create a docker-compose.yml file. This will usually be the same for all 
   documentation projects. 
   
   .. code-block:: yaml
      :lineno:
   
      version: '2'
      services:
         typo3_contrib:
            image: t3docs/render-documentation:latest
            volumes:
            - ./:/PROJECT:ro
            - ./Documentation-GENERATED-temp:/RESULT
            command: makehtml

#. Run docker-compose

   If docker-compose.yml is in current directory::

      docker-compose up      
      
   If yaml file is named differently::
   
      docker-compose up -f <path>

Where you create the docker-compose.yml file is up to you. You can create it in the
documentation project you work on or create a general one you use for all documentation
projects. Just don't commit files with your specific settings to a public repository.


   
  
