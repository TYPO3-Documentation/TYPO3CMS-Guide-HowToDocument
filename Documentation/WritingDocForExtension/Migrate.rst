..  include:: /Includes.rst.txt
..  index::
    Documentation; Migration
    docs.typo3.org
..  _migrate:
..  _register-for-rendering:

=============================================
Migration: From Sphinx to PHP-based rendering
=============================================

..  note::

    Since the beginning of 2024 you can switch to the new, PHP-based reStructured
    Text rendering to try it out. The new rendering will become mandatory in
    August 2024.

The main difference that concerns you is that the new PHP-base rendering
requires a file called :file:`Documentation/guides.xml` for configuration
while in Sphinx rendering a file called :file:`Documentation/Settings.cfg` was
used. In the transition period we detect if a file called
:file:`Documentation/guides.xml` is present and then switch to the new
PHP-based rendering.

..  _migrate_guides_xml:

Create the settings file :file:`Documentation/guides.xml`
=========================================================

The Docker container for the new PHP-based rendering additionally contains
a migration tool. This tool can be used to automatically create a
:file:`Documentation/guides.xml` from the information contained in your
:file:`Documentation/Settings.cfg`.

`Docker <https://docs.docker.com/install/>`__ (or a drop-in replacement like
`Podman <https://podman.io>`__) needs to be installed on your
operating system for the tool to work:

..  tabs::

    ..  group-tab:: Docker

        ..  code-block:: bash

            docker run --rm --pull always \
              -v $(pwd):/project \
              -it ghcr.io/typo3-documentation/render-guides:latest \
              migrate Documentation

    .. group-tab:: Podman

        ..  code-block:: bash

            podman run --rm --pull always \
              -v $(pwd):/project \
              -it ghcr.io/typo3-documentation/render-guides:latest \
              migrate Documentation


The last parameter (:bash:`Documentation`) is the name of the directory, where your
:file:`Settings.cfg` is currently placed in.

After the migration is performed, you will see output about which settings were
converted, if some old settings were discarded, or errors occurred.

Try out the rendering locally
=============================

Use our Docker container to render your documentation locally. Read more about
:ref:`local rendering <rendering-docs>`.

..  _migrate-detailed-steps:

Further steps to adapt to the new rendering
===========================================

You should perform the following tasks to conclude the migration to the
new rendering tool:

..  rst-class:: bignums

1.  Improve your documentation to render without warning

    Rendering your documentation should not yield any warnings or errors.

    If you get error messages, often they refer to wrong indentation, missing
    :ref:`interlinks <settings-guides-interlink-mapping>`, orphaned files or
    outdated ReST identifiers.

    If you are unable to address a warning/error with changes in your documentation
    feel free to ask in Slack channel #typo3-documentation (see :ref:`how-to-get-help`).

    If you believe you found a specific bug in the new PHP-based rendering, please open
    an `Issue on GitHub <https://github.com/TYPO3-Documentation/render-guides/issues>`__.

2.  Remove outdated files

    After you have created the :file:`guides.xml` file, you can remove the old
    :file:`Settings.cfg` file.

    You can also delete the files :file:`genindex.rst` which was previously used
    to generate an index.

3.  Adapt :file:`Includes.rst.txt`

    The main documentation directory can contain a file :file:`Includes.rst.txt`
    to include any fixed text, which will be placed on every page of your rendered
    documentation.

    Previously it was also used to define a list of utilized directives/roles.

    You can either remove that file, or add your fixed text to it. If you remove
    the file, remember to also remove all references pointing to that file, like:

    ..  code-block:: text
        :caption: Documentation/Index.rst

        ..  include:: /Includes.rst.txt

    Most official documentation uses this as the stub of the file:

    ..  code-block:: text
        :caption: Documentation/Includes.rst.txt

        ..  You can put central messages to display on all pages here

4.  Remove the entry `genindex` from :file:`Index.rst` (Index/Glossary)

    If you previously had a :file:`genindex.rst` file, this optional index
    (or glossary) was rendered as a page through an entry in the file :file:`Index.rst`
    like this:

    ..  code-block:: text
        :caption: Documentation/Index.rst
        :emphasize-lines: 17

        **Table of Contents:**

        .. toctree::
           :maxdepth: 2
           :titlesonly:

           Introduction/Index
           Installation/Index
           Details/Index

        .. Meta Menu

        .. toctree::
           :hidden:

           Sitemap
           genindex

    Remove the entry `genindex` from the list.

    ..  hint::

        See :ref:`migrate-glossary` for details about the future of the
        index (glossary) generation.

5.  Prevent code snippets with :file:`.rst` extension

    All files with the extension :file:`.rst` will be interpreted by the new rendering,
    and every file that is just a code snippet placed in an external file
    should be renamed to use a :file:`.rst.txt` extension instead.

Recommendations
===============

The following list is not a requirement to utilize the new rendering, but
follows "best practice" to make the most of your documentation project.

..  _migrate-to-makefile:

Add a :file:`Makefile` to your project
--------------------------------------

A :file:`Makefile` is a simple command line runner configuration file, which requires
the utility `GNU make <https://www.gnu.org/software/make/manual/make.html>`_
to be available on your Unix-based Operating System (Linux, macOS, WSL on Windows
for example).

This allows you to perform shortcuts to render your documentation instead
of typing a long :bash:`docker run...` or :bash:`podman run...` command:

..  code-block:: shell

    make docs

For inspiration, check out the :file:`Makefile` of the main PHP-based rendering
repository:

https://github.com/TYPO3-Documentation/render-guides/blob/main/Makefile

A small example :file:`Makefile`:

..  literalinclude:: _Makefile
    :caption: Makefile

..  hint::

    Makefile blocks need to be indented with a TAB character, not spaces.
    If your project comes with an :ref:`editorconfig` definition for
    code formatting, you should add the following:

    ..  code-block:: text

        [Makefile]
        # Use tabs for indentation (Makefiles require tabs)
        indent_style = tab


..  _migrate-to-testing-workflow:

Activate automatic testing in your project
------------------------------------------

It is recommended to use an automatic workflow on GitHub Or GitLab to
ensure the extension's documentation renders without warnings.

An example workflow on GitHub would be established via this file in
:file:`.github/actions/documentation.yml`:

..  literalinclude:: _documentation.yml
    :caption: .github/actions/documentation.yml


This creates a workflow entry `Test documentation`, so that on every push to your
repository, and every pull request, the rendering is executed. A commit will then
not be possible, if the rendering fails. The workflow run will be marked with an error,
and shown on pull requests.

..  _migrate-glossary:

To be discussed: Index generation (glossary)
============================================

The Sphinx rendering allowed to utilize a syntax like the following to
add indexes to your documentation:

..  code-block::
    :caption: Documentation/Index.rst

    ..  index::
        XLIFF; Files
        File; XLIFF

The automatically generated file :file:`genindex.html` would show a
two-column layout of all indexes, with the pages that they were used on.

The new PHP-based rendering does not (yet) support this indexing.

The current recommendation is to only remove the :file:`genindex.rst` file
from your documentation directory, but keep all the placed `..  index`
directives. If at some point the automatic index-generation is re-introduced,
your old indexes will be able to show up again.
