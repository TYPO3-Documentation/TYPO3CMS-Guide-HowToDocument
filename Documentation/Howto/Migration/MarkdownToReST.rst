:navigation-title: Markdown to ReST

..  include:: /Includes.rst.txt
..  index::
    Documentation; Migration
    docs.typo3.org
..  _migrate-markdown-to-rest:

=============================================
Migration: Markdown to reStructuredText (ReST)
=============================================

Markdown is very popular and widely used for documentation. However, ReST is more powerful and flexible.
The TYPO3 documentation toolchain contains a lot of features that are only available with ReST.
Because of the extendability of ReST. This guide explains how to migrate Markdown files to ReST,
using the TYPO3 documentation toolchain.

Unless you have a specific reason to migrate to ReST, it is perfectly fine to keep using Markdown.
The TYPO3 documentation toolchain supports both formats.

..  note::

    This guide assumes you have already set up the TYPO3 documentation toolchain.
    If you haven't, please follow the instructions in the :ref:`rendering-docs` guide.

..  _migrate-markdown-to-rest-conversion:

Converting Markdown to ReST
===========================

The first step is to convert the Markdown files to ReST. This can be done using
our rendering toolchain. This will convert the Markdown files to ReST format.
We will use ``Documentation-Migrated`` as the output directory.

..  tabs::

    ..  group-tab:: Linux

        ..  code-block:: bash

            mkdir -p Documentation-Migrated
            docker run --rm --pull always -v $(pwd):/project -it ghcr.io/typo3-documentation/render-guides:latest --theme=rst --output-format=rst --output Documentation-Migrated

    .. group-tab:: MacOS

        ..  code-block:: bash

            mkdir -p Documentation-Migrated
            docker run --rm --pull always -v $(pwd):/project -it ghcr.io/typo3-documentation/render-guides:latest --theme=rst --output-format=rst --output Documentation-Migrated

    ..  group-tab:: Windows

        ..  code-block:: powershell

            New-Item -ItemType Directory -Force -Path ".\Documentation-Migrated"
            docker run --rm --pull always -v ${PWD}:/project -it ghcr.io/typo3-documentation/render-guides:latest --theme=rst --output-format=rst --output Documentation-Migrated

Now we can copy the ``guides.xml`` from the original directory documentation directory to the new directory. And remove the
option ``input-format="md"``. This will tell the rendering toolchain to use the ReST files instead of the Markdown files.

Last step is to swap the directories. Rename the original directory to ``Documentation-Markdown`` and the new directory ``Documentation-Migrated`` to ``Documentation``.

The basic migration is now done. Some manual adjustments might be necessary, as the conversion is not perfect.

..  tip::

    If you notice any issues with the conversion, please report them to the :ref:`TYPO3 documentation team <contact-us>`.
