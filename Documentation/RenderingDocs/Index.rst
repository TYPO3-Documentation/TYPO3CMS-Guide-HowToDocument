.. include:: /Includes.rst.txt
.. highlight:: rst
.. Index::
    pair: Documentation; Rendering
    Rendering; Locally
    Rendering; Docker
    Rendering; Commands
.. _rendering-docs:
.. _rendering-docs-quickstart:
.. _render-documenation-with-docker:
.. _render-documentation-with-docker:


===========================
How to render documentation
===========================

This page explains how to render a manual locally on your machine
with Docker in order to test the rendering.

Run these commands in a terminal in the parent directory of the directory
:file:`Documentation`. You should use a bash compatible shell, if possible.

If you run into a problem while rendering, check :ref:`rendering-docs-troubleshooting`,
`report an issue <https://github.com/t3docs/docker-render-documentation/issues/new>`__
or :ref:`ask for help <get-help-on-writing-docs>`.


.. rst-class:: bignums-xxl

    #.  Install Docker: https://docs.docker.com/install/

    #.  Preparations

        The docker image is not listed on Docker Hub (hub.docker.com) anymore, therefore some preparations
        need to be done once:

        ..  code-block:: bash

            # pull 'latest' version from GitHub container repository
            docker pull ghcr.io/t3docs/render-documentation

            # The "real" tag is independent of the container repository,
            # so let's just create that extra "real" and "generic" tag
            docker tag ghcr.io/t3docs/render-documentation t3docs/render-documentation

            # verify it worked
            docker run --rm t3docs/render-documentation --version

    #.  Make 'dockrun_t3rd' available in current terminal

        .. code-block:: bash

            eval "$(docker run --rm t3docs/render-documentation show-shell-commands)"

        This will run the Docker container and print out shell code. Once "eval-uated" 
        the code defines a helper function named `dockrun_t3rd`. This function relieves 
        you of the work of setting the volumes and rights correctly when running the 
        container and ensures a folder for the rendering results is provided. Executing 
        the code with `eval` defines the function for your current terminal. Don't forget
        the quotes around everything that goes into eval. Either define the function each
        time you open a new terminal window or add the line to the startup file of your
        shell like `~/.bashrc` or `.zshrc`.

    #.  Run dockrun_t3rd

        .. code-block:: bash

            dockrun_t3rd makehtml

        This will automatically find the documentation in the
        :file:`Documentation` subfolder. It will create a directory
        :file:`Documentation-GENERATED-temp` and write the results there.

    #.  Open generated documentation

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


.. toctree::
   :hidden:
   :glob:

   Troubleshooting
