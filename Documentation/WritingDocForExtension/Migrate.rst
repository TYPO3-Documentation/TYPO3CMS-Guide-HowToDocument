.. include:: /Includes.rst.txt
.. index::
   Documentation; Migration
   docs.typo3.org
.. _migrate:
.. _register-for-rendering:

=============================================
Migration: From Sphinx to PHP-based rendering
=============================================

..  note::

    Since the beginning of 2024 you can switch to the new, PHP-based reStructured
    Text rendering to try it out. The new rendering will become mandatory in
    August 2024.

The main difference that concerns you is that the new PHP-base rendering
requires a file called :file:`Documentation/guides.xml` for configuration
while in Sphinx rendering a file called :file:`Docuemtation/Settings.cfg` was
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

`Docker <https://docs.docker.com/install/>`__ needs to be installed on your
operating system for the tool to work:

..  code-block:: shell

    docker run --rm --pull always \
        -v $(pwd):/project \
        -it ghcr.io/typo3-documentation/render-guides:latest \
        migrate Documentation

Try out the rendering locally
=============================

Use our Docker container to render your documentation locally. Read more about
:ref:`local rendering <rendering-docs>`.

Improve your documentation to render without warning
====================================================

If you believe you found a bug in the new PHP-based rendering, please open
an `Issue on GitHub <https://github.com/TYPO3-Documentation/render-guides/issues>`__.

Recommended: Activate automatic testing
=======================================

It is recommended to use an automatic workflow on GitHub Or Gitlab to
ensure the extension's documentation renders without warnings.

..  todo: Add a link to the according chapter
