:navigation-title: Live rendering (WYSIWYG)

..  _rendering-wysiwyg:
..  _live-rendering:

============================================================
Rendering with more WYSIWYG-feeling (automatic re-rendering)
============================================================

You want to write complex `reST` markup and directly see the
rendered output, browser side-by-side with your editor? Then
this section is for you!

Often, especially in the later stages of creating documentation, you
just edit small parts of the reST files, render the outcome manually
and happily commit your changes.

However, in cases you write larger sections of text, you may want
to get more immediate visual feedback on your changes, but do not
want to manually trigger the rendering time and again.

To make this easier, `render-guides` can serve the rendered documentation
via a local web-server and automatically re-render the documentation
when changes in the source files are detected. This gives you a more
WYSIWYG-like experience when writing documentation.

This allows you to have a browser window next to your reST file editor
to view progress.

..  tabs::

    ..  group-tab:: Linux

        ..  code-block:: bash

            docker run --rm -it --pull always \
              -v "./Documentation:/project/Documentation" \
              -v "./Documentation-GENERATED-temp:/project/Documentation-GENERATED-temp" \
              -p 1337:1337 ghcr.io/typo3-documentation/render-guides:latest --config="Documentation" --watch
            xdg-open "http://localhost:1337/Index.html"

    .. group-tab:: MacOS

        ..  code-block:: bash

            docker run --rm -it --pull always \
              -v "./Documentation:/project/Documentation" \
              -v "./Documentation-GENERATED-temp:/project/Documentation-GENERATED-temp" \
              -p 1337:1337 ghcr.io/typo3-documentation/render-guides:latest --config="Documentation" --watch
            xdg-open "http://localhost:1337/Index.html"
    ..  group-tab:: Windows

        ..  code-block:: powershell

            docker run --rm -it --pull always \
              -v "./Documentation:/project/Documentation" \
              -v "./Documentation-GENERATED-temp:/project/Documentation-GENERATED-temp" \
              -p 1337:1337 ghcr.io/typo3-documentation/render-guides:latest --config="Documentation" --watch
            xdg-open "http://localhost:1337/Index.html"

The command above can also be added to your project's `Makefile` or
you can create a bash alias like:

..  code:: bash

    alias render-wysiwyg="docker run --rm -it --pull always \
                            -v './Documentation:/project/Documentation' \
                            -v './Documentation-GENERATED-temp:/project/Documentation-GENERATED-temp' \
                            -p 1337:1337 ghcr.io/typo3-documentation/render-guides:latest --watch"

..  note::

    If anything on your host operating system already utilizes the TCP port
    `1337` you need to adapt that command to use another free TCP port for you,
    and adapt the port in the web-browser URL.
    You can do this by changing the :bash:`-p` parameter, e.g. to
    :bash:`-p 8080:1337` to use TCP port `8080` on your host system.

Docker compose
==============

If you are using `docker-compose <https://docs.docker.com/compose/>`_ to manage your
development environment, you can add a service for the live rendering like this:

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

.. note::

   Render guides was never optimized for long running services. You might need
   to restart the container from time to time to free up resources.

DDev
====

For integration with DDEV projects, a DDEV addon has been created at https://github.com/TYPO3-Documentation/ddev-typo3-docs.
This can be used to automatically start the live documentation preview within the DDEV project at http://<yourproject>.ddev.site:1337/
whenever you start that project, and can directly view and work on documentation alongside the project.
In this environment, users do not even need to execute a manual `docker run` command anymore, and have full integration at hand.

Limitations
===========

Not all changes in the source files can be detected automatically, or will
impact the rendered output immediately. In such cases, a manual re-rendering
is required. Examples are:

* Changes in :file:`guides.xml`
* New added files
* Menu changes
* Moving files

.. note::

    Please be aware that some editors (like e.g. `VIM`) create temporary files
    when opening files for editing. This will not be detected as a change to the
    actual file and thus not trigger a re-rendering.
