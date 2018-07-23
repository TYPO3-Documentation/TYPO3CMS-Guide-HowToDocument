.. include:: ../Includes.txt
.. highlight:: bash

.. _rendering-docs-quickstart:


===================================
Rendering documentation with docker
===================================


If you run into problems, see :ref:`how-to-get-help`.

.. rst-class:: bignums-xxl

1. Install docker

   See `Get docker <https://www.docker.com/get-docker>`__

2. docker run

   In a terminal (shell) run:

   .. code-block:: bash

      source <(docker run --rm t3docs/render-documentation show-shell-commands)

   This will not only pull the image and run the docker container, it
   will make the commands available in your current terminal.

   You must do this again for every new terminal you open.

   This command may take a while. The next run will be faster because
   it won't have to pull the docker image again!

3. Change directory (if necessary)

   In the **same terminal** move to the place where your documentation is stored.
   Go to the parent directory of the :file:`Documentation` subfolder.

4. Render the documentation

   .. code-block:: bash

      dockrun_t3rdf makehtml

   This will automatically find the documentation in the :file:`Documentation`
   subfolder. It will create a directory :file:`Documentation-GENERATED-temp`
   and write the results there.

   If you run into problems, check the :ref:`rendering-docs-troubleshooting`
   page!

5. View the documentation

   You can now view the rendered documentation in your browser.

   Look at the hints that are shown in the terminal.

   Use an URL
   beginning with `file:///` to access the files in the rendered directory:
   `file:///` ... `Documentation-GENERATED-temp/Result/project/0.0.0/Index.html`.

   If you structured the documentation correctly, an :file:`Index.rst` is
   always on the top level directory under the directory :file:`Documentation`.

   The renderer will create the file :file:`Index.html` from that. The path
   is always the same.

   So, depending on what operating system you are on and how it is configured,
   you can use this command as a shortcut for opening the docs in the browser:

   .. code-block:: bash

      open "file:///$(pwd)/Documentation-GENERATED-temp/Result/project/0.0.0/Index.html"

   Try `xdg-open` (for Linux) or `start` (for Windows) instead of `open` if this does not work for you.

   .. tip::

      Create aliases for these command now. You can reuse them.

6. Repeat

   Verify if the documentation has been rendered correctly by viewing the results
   in the browser. Make more changes if necessary. Rerender with step 5.

   Press reload (e.g. CTRL-r) in your browser to view the changes.

7. Check .gitignore / .gitignore_global

   As a precaution, add the generated directory :file:`Documentation-GENERATED-temp`
   to your :file:`~/.gitignore_global` if it is not already in the :file:`.gitignore` file
   in the project.


.. tip::

   Create aliases for the commands that works best for you now!


.. seealso::

  `Docker rendering Readme on Github <https://github.com/t3docs/docker-render-documentation/blob/master/README.rst>`__
