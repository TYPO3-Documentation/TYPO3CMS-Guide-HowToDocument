:navigation-title: Markdown to reST

..  include:: /Includes.rst.txt
..  index::
    Documentation; Migration
    docs.typo3.org
..  _migrate-markdown-to-rest:

==============================================
Migration: Markdown to reStructuredText (reST)
==============================================

Markdown is very popular and widely used for documentation. However, reST is more powerful and flexible.
The TYPO3 documentation toolchain contains a lot of features that are only available with reST.
Because of the extendability of reST. This guide explains how to migrate Markdown files to reST,
using the TYPO3 documentation toolchain.

Unless you have a specific reason to migrate to reST, it is perfectly fine to keep using Markdown.
The TYPO3 documentation toolchain supports both formats.

..  note::

    This guide assumes you have already set up the TYPO3 documentation toolchain.
    If you haven't, please follow the :ref:`instructions for rendering documentation <rendering-docs>`.

..  _migrate-markdown-to-rest-conversion:

Converting Markdown to reST
===========================

The first step is to convert the Markdown files to reST. This can be done using
our rendering toolchain. This will convert the Markdown files to reST format.
We will use :file:`Documentation-Migrated` as the output directory.

..  tabs::

    ..  group-tab:: Linux

        ..  code-block:: bash

            mkdir -p Documentation-Migrated
            docker run --rm --pull always -v $(pwd):/project -it ghcr.io/typo3-documentation/render-guides:latest --theme=rst --output-format=rst --output Documentation-Migrated

    ..  group-tab:: macOS

        ..  code-block:: bash

            mkdir -p Documentation-Migrated
            docker run --rm --pull always -v $(pwd):/project -it ghcr.io/typo3-documentation/render-guides:latest --theme=rst --output-format=rst --output Documentation-Migrated

    ..  group-tab:: Windows

        ..  code-block:: powershell

            New-Item -ItemType Directory -Force -Path ".\Documentation-Migrated"
            docker run --rm --pull always -v ${PWD}:/project -it ghcr.io/typo3-documentation/render-guides:latest --theme=rst --output-format=rst --output Documentation-Migrated

..  note::
    :bash:`--output` is resolved inside the container, so the path has to stay
    below the mounted volume (:bash:`-v $(pwd):/project`). A path outside it is
    written to the container's own file system and disappears with the
    container, while the command still reports the files as placed. The
    relative :file:`Documentation-Migrated` above satisfies this.

Now we can copy the :file:`guides.xml` from the original documentation directory to the new directory. And remove the
option `input-format="md"`. This will tell the rendering toolchain to use the reST files instead of the Markdown files.

Last step is to swap the directories. Rename the original directory to :file:`Documentation-Markdown` and the new directory :file:`Documentation-Migrated` to :file:`Documentation`.

The basic migration is now done. Some manual adjustments might be necessary, as the conversion is not perfect.

..  tip::

    If you notice any issues with the conversion, please report them to the :ref:`TYPO3 Documentation Team <contact-us>`.
