:navigation-title: Automatic re-rendering (WYSIWYG)

..  _rendering-wysiwyg:
..  _live-rendering:

============================================================
Automatic re-rendering when writing documentation locally
============================================================
In case you write complex `reST` markup you may want immediate visual
feedback on your changes, without triggering the rendering manually every time.

`render-guides` can serve the rendered documentation via a local web-server
and automatically re-render the documentation when changes in the source files
are detected.

This enables a WYSIWYG-like editing experience with your editor
and browser side-by-side.

..  contents::

..  _rendering-wysiwyg-prerequisites:

Prerequisites
=============

Configure the rendering as described here: :ref:`render-documentation-with-docker`.

The only thing that changes is the render command you use (see below).

..  _rendering-wysiwyg-docker:

Usage with Docker
=================

..  tabs::

    ..  group-tab:: Linux

        ..  code-block:: bash

            docker run --rm -it --pull always \
              -v "./Documentation:/project/Documentation" \
              -v "./Documentation-GENERATED-temp:/project/Documentation-GENERATED-temp" \
              -p 1337:1337 ghcr.io/typo3-documentation/render-guides:latest --config="Documentation" --watch
            xdg-open "http://localhost:1337/Index.html"

    ..  group-tab:: MacOS

        ..  code-block:: bash

            docker run --rm -it --pull always \
              -v "./Documentation:/project/Documentation" \
              -v "./Documentation-GENERATED-temp:/project/Documentation-GENERATED-temp" \
              -p 1337:1337 ghcr.io/typo3-documentation/render-guides:latest --config="Documentation" --watch
            open "http://localhost:1337/Index.html"

    ..  group-tab:: Windows

        ..  code-block:: powershell

            docker run --rm -it --pull always \
              -v "./Documentation:/project/Documentation" \
              -v "./Documentation-GENERATED-temp:/project/Documentation-GENERATED-temp" \
              -p 1337:1337 ghcr.io/typo3-documentation/render-guides:latest --config="Documentation" --watch
            start "http://localhost:1337/Index.html"

The command above can also be added to your project's `Makefile`.

Or you can create a bash alias like:

..  code:: bash

    alias render-wysiwyg="docker run --rm -it --pull always \
                            -v './Documentation:/project/Documentation' \
                            -v './Documentation-GENERATED-temp:/project/Documentation-GENERATED-temp' \
                            -p 1337:1337 ghcr.io/typo3-documentation/render-guides:latest --watch"

..  note::

    If your host operating system already utilizes the TCP port `1337`
    you need to adapt that command to use another free TCP port. For this
    you can change the port number behind the :bash:`-p` parameter. To use
    port `8080` the bash code needs to be adapted like this: :bash:`-p 8080:1337`.

    Also adapt the port in the URL. In the example above the server would be
    accessible via `http://localhost:8080` instead of `http://localhost:1337`.

..  _rendering-wysiwyg-docker-compose:

Usage with Docker Compose
=========================

If you are using `docker-compose <https://docs.docker.com/compose/>`_ to manage your
development environment, you can add a service for the automatic re-rendering like this:

..  code-block:: yaml
    :caption: docker-compose.yml

    services:
      render-wysiwyg:
        restart: "no"
        image: ghcr.io/typo3-documentation/render-guides:latest
        ports:
          - "1337:1337"
        volumes:
          - ./Documentation:/project/Documentation
          - ./Documentation-GENERATED-temp:/project/Documentation-GENERATED-temp
        command: ["--config=Documentation", "--watch"]

..  note::

    `render-guides` was never optimized for long running services. You might need
    to restart the container from time to time to free up resources.

..  _rendering-wysiwyg-ddev:

Usage with DDEV
===============

For integration with DDEV projects, a DDEV addon is available at
https://github.com/TYPO3-Documentation/ddev-typo3-docs.

When you start your DDEV project, this addon starts the automatic re-rendering
of the documentation at `http://<yourproject>.ddev.site:1337/`.

In this environment, users do not need to execute a manual `docker run` command.

..  _rendering-wysiwyg-limitations:

Limitations
===========

Not all changes in the source files can be detected automatically,
or will impact the rendered output immediately:

*   Changes in :file:`guides.xml`
*   New added files
*   Menu changes
*   Moving files

**In such cases, a manual re-rendering is required.**

..  note::

    Some editors (like `VIM`) create temporary files when opening files
    for editing. This will not be detected as a change to the
    actual file and thus not trigger a re-rendering.
