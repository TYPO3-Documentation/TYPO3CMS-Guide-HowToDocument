.. include:: /Includes.rst.txt
.. Index::
    pair: Documentation; Rendering
    Rendering; Locally
    Rendering; Docker
    Rendering; Commands
.. _rendering-docs:
.. _rendering-docs-quickstart:
.. _render-documenation-with-docker:
.. _render-documentation-with-docker:

=========================================
Render documentation with the TYPO3 theme
=========================================

..  contents::

Rendering the :file:`Documentation` folder locally with Docker
==============================================================

You can render the documentation of an official TYPO3 manual or a third-party
manual with the following steps:

#.  Clone the repository containing the documentation.

#.  Navigate to the extension's root folder, the directory which contains the
    :file:`composer.json`.

#.  Check if there is documentation to be rendered:

    A folder called :file:`Documentation` containing at least the files
    :file:`Index.rst` and :file:`guides.xml`.

#.  Choose your preferred method of rendering (See below):

Make sure that `Docker <https://www.docker.com/>`__ is installed on your system.

..  tip::

    Did you know: Instead of the :bash:`docker` client you can also use
    the lightweight drop-in replacement `Podman <https://podman.io/>`__ to run
    the mentioned containers by replacing all :bash:`docker` commands in the
    following steps with :bash:`podman`.

..  tabs::

    ..  group-tab:: Linux

        ..  code-block:: bash

            mkdir -p Documentation-GENERATED-temp
            docker run --rm --pull always -v $(pwd):/project -it ghcr.io/typo3-documentation/render-guides:latest --config=Documentation
            xdg-open "Documentation-GENERATED-temp/Index.html"

    .. group-tab:: MacOS

        ..  code-block:: bash

            mkdir -p Documentation-GENERATED-temp
            docker run --rm --pull always -v $(pwd):/project -it ghcr.io/typo3-documentation/render-guides:latest --config=Documentation
            open "Documentation-GENERATED-temp/Index.html"

    ..  group-tab:: Windows

        ..  code-block:: powershell

            New-Item -ItemType Directory -Force -Path ".\Documentation-GENERATED-temp"
            docker run --rm --pull always -v ${PWD}:/project -it ghcr.io/typo3-documentation/render-guides:latest --config=Documentation
            start "Documentation-GENERATED-temp/Index.html"

..  _rendering-wysiwyg:

Rendering with more WYSIWYG-feeling (automatic re-rendering)
------------------------------------------------------------

You want to write complex `reST` markup and directly see the
rendered output, browser side-by-side with your editor? Then
this section is for you!

Often, especially in the later stages of creating documentation, you
just edit small parts of the reST files, render the outcome manually
and happily commit your changes.

However, in cases you write larger sections of text, you may want
to get more immediate visual feedback on your changes, but do not
want to manually trigger the rendering time and again.

To make this easier, the project `garvinhicking/typo3-documentation-browsersync
<https://github.com/garvinhicking/typo3-documentation-browsersync>`__
has been created. This docker container solution provides an environment
which permanently watches changes to any of the reST files and automatically
triggers a re-rendering. The generated HTML output is then served with a
local web server (vite-based) in which your browser automatically hot-reloads
all changes and keeps the scroll position.

This allows you to have a browser window next to your reST file editor
to view progress.

Since that whole environment is based on the official
:ref:`TYPO3 documentation rendering container <t3renderguides:start>`
and utilizes a docker container, it is simple to use. Also, all updates
to the `render-guides` project are automatically merged into that
project, so all bugfixes and new features of the PHP-based rendering always
are in sync with this WYSIWYG-project, with a possibility of this becoming
a regular TYPO3-documentation project (given positive feedback).

The project itself has `documentation on the technical details
<https://github.com/garvinhicking/typo3-documentation-browsersync/blob/main/README.md>`__
but all you need is this docker/podman command:

..  tabs::

    ..  group-tab:: Linux

        ..  code-block:: bash

            docker run --rm -it --pull always \
              -v "./Documentation:/project/Documentation" \
              -v "./Documentation-GENERATED-temp:/project/Documentation-GENERATED-temp" \
              -p 5173:5173 ghcr.io/garvinhicking/typo3-documentation-browsersync:latest
            xdg-open "http://localhost:5173/Documentation-GENERATED-temp/Index.html"

    .. group-tab:: MacOS

        ..  code-block:: bash

            docker run --rm -it --pull always \
              -v "./Documentation:/project/Documentation" \
              -v "./Documentation-GENERATED-temp:/project/Documentation-GENERATED-temp" \
              -p 5173:5173 ghcr.io/garvinhicking/typo3-documentation-browsersync:latest
            open "http://localhost:5173/Documentation-GENERATED-temp/Index.html"

    ..  group-tab:: Windows

        ..  code-block:: powershell

            docker run --rm -it --pull always \
              -v "./Documentation:/project/Documentation" \
              -v "./Documentation-GENERATED-temp:/project/Documentation-GENERATED-temp" \
              -p 5173:5173 ghcr.io/garvinhicking/typo3-documentation-browsersync:latest
            start "http://localhost:5173/Documentation-GENERATED-temp/Index.html"

The command above can also be added to your project's `Makefile` or
you can create a bash alias like:

..  code:: bash

    alias render-wysiwyg="docker run --rm -it --pull always \
                            -v './Documentation:/project/Documentation' \
                            -v './Documentation-GENERATED-temp:/project/Documentation-GENERATED-temp' \
                            -p 5173:5173 ghcr.io/garvinhicking/typo3-documentation-browsersync:latest'"

..  note::

    If anything on your host operating system already utilizes the TCP port
    `5173` you need to adapt that command to use another free TCP port for you,
    and adapt the port in the web-browser URL.


Publishing extension documentation to docs.typo3.org
====================================================

For your documentation to be published to https://docs.typo3.org, your
TYPO3 extension has to have a valid :file:`composer.json` and either a folder
called :file:`Documentation` with a :file:`Documentation/Index.rst` and
a :file:`Documentation/guides.xml` or a :file:`README.rst` / :file:`README.md`
in the extension's root directory.

The extension has to be publicly available on GitHub or GitLab. You have to
establish a :ref:`Webhook <webhook>` and the Documentation Team has to
:ref:`approve <approval-intercept>` your first rendering.

Introduce automatic testing for extension documentation
=======================================================

It is recommended to make sure your documentation always renders without
warning. On GitHub or GitLab you can introduce actions that test your
documentation automatically:

.. tabs::

    ..  group-tab:: GitHub

        ..  code-block:: yaml
            :caption: .github/workflows/documentation.yml

            name: test documentation

            on: [ push, pull_request ]

            jobs:
              tests:
                name: documentation
                runs-on: ubuntu-latest
                steps:
                  - name: Checkout
                    uses: actions/checkout@v4

                  - name: Test if the documentation will render without warnings
                    run: |
                      mkdir -p Documentation-GENERATED-temp \
                      && docker run --rm --pull always -v $(pwd):/project \
                         ghcr.io/typo3-documentation/render-guides:latest --config=Documentation --no-progress --fail-on-log

    .. group-tab:: GitLab

        ..  code-block:: bash
            :caption: .gitlab-ci.yml

            stages:
              - test

            test_documentation:
              stage: test
              script:
                - mkdir -p Documentation-GENERATED-temp
                - docker run --rm --pull always -v $(pwd):/project ghcr.io/typo3-documentation/render-guides:latest --config=Documentation --no-progress --fail-on-log
              tags:
                - docker

