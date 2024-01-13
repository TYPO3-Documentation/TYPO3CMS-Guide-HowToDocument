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

=========================================
Render documentation with the TYPO3 theme
=========================================

..  contents::

Rendering the :file:`Documentation` folder locally with Docker
==============================================================

You can render the documentation of an official TYPO3 manual or a third party
manual with the following steps:

#.  Clone the repository containing the documentation.

#.  Navigate to the directory, which contains the :file:`composer.json`

#.  Check if there is documentation to be rendered:

    A folder called :file:`Documentation` containing at least the files
    :file:`Index.rst` and :file:`guides.xml`.

#.  Choose your prefered method of rendering (See bellow):

Make sure that `Docker <https://www.docker.com/>`__ is installed on your system.

.. tabs::

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

            start "Documentation-GENERATED-temp/Index.html"
            docker run --rm --pull always -v ${PWD}:/project -it ghcr.io/typo3-documentation/render-guides:latest --config=Documentation
            open "Documentation-GENERATED-temp/Index.html"

Rendering extension documentation to docs.typo3.org
===================================================

For your documentation to be rendered to our server https://docs.typo3.org, your
TYPO3 extension has to have a valid :file:`composer.json` and either a folder
called :file:`Documentation` with a :file:`Documentation/Index.rst` and
a :file:`Documentation/guides.xml` or a :file:`README.rst` / :file:`README.md` on
the level of your :file:`composer.json`.

The extension has to be publicly available on GitHub or GitLab. You have to
introduce a :ref:`Webhook <webhook>` and the Documentation Team has to
:ref:`approve <approval-intercept>` your first rendering request on a tool
called "Intercept".

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

