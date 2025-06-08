:navigation-title: Screenshot container

..  include:: /Includes.rst.txt
..  _screenshot-container:

==================================
TYPO3 Screenshots Docker container
==================================

We have prepared a Docker container that you can use to create screenshots
for the official documentation, which already follows out
`Guidelines for screenshots <https://docs.typo3.org/permalink/h2document:automatic-screenshots>`_.

..  contents:: Table of content

..  seealso::

    *   `Guidelines for screenshots in the official documentation <https://docs.typo3.org/permalink/h2document:automatic-screenshots>`_
    *   `linawolf/typo3-screenshots <https://hub.docker.com/repository/docker/linawolf/typo3-screenshots/general>`_
    *   `Ready to use Project for Screenshots (GitHub) <https://github.com/TYPO3-Documentation/site-introduction>`_

..  _screenshot-quick:

Quick screenshots using Docker
==============================

You can run the screenshot project locally using the prebuilt Docker image:

..  code-block:: bash

    docker run -d --name typo3-screenshots -p 8080:80 linawolf/typo3-screenshots

    # Follow the logs to track progress:
    docker logs -f typo3-screenshots

Once setup is complete, open:

http://localhost:8080/typo3

..  note::

    The container resets on every run. It is ideal for reproducible test
    environments and fresh screenshots.

..  _screenshot-reset:

Resetting the container
=======================

To start fresh, you can stop and remove the running container, then launch it
again.

..  code-block:: bash

    docker stop typo3-screenshots
    docker rm typo3-screenshots
    docker run -d --name typo3-screenshots -p 8080:80 linawolf/typo3-screenshots

This gives you a clean TYPO3 instance every time.

..  _screenshot-ssh:

Accessing the container shell
=============================

You can access the container's shell to explore the file system, install
additional extensions, or run TYPO3 CLI commands:

..  code-block:: bash

    docker exec -it typo3-screenshots bash

This drops you into a terminal session inside the container.

After accessing the container shell, you can exit
at any time by typing:

..  code-block:: bash

    exit

This will close the interactive shell session and return you to your host
terminal.

..  _screenshot-composer:

Installing additional extensions with Composer
==============================================

Once inside the container (via :ref:`screenshot-ssh`), you can install TYPO3
extensions using Composer. For example:

..  code-block:: bash

    composer require typo3/cms-lowlevel

Then you can run the setup command to register the extension:

..  code-block:: bash

    ./vendor/bin/typo3 extension:setup

..  note::

    Since the container resets every time, any installed extension will be lost
    on restart unless you build a new image with those extensions included. This
    is intentional to ensure a consistent environment for screenshots.

..  _screenshot-commands:

Running TYPO3 CLI commands
==========================

To run any TYPO3 CLI command inside the container, use:

..  code-block:: bash

    docker exec -it typo3-screenshots ./vendor/bin/typo3 <command>

Examples:

..  code-block:: bash

    docker exec -it typo3-screenshots ./vendor/bin/typo3 list
    docker exec -it typo3-screenshots ./vendor/bin/typo3 extension:setup
    docker exec -it typo3-screenshots ./vendor/bin/typo3 language:update
