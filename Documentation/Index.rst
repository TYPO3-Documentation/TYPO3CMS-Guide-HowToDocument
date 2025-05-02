:navigation-title: How to Document
.. include:: /Includes.rst.txt
..  _start:
.. index:: ! Writing documentation

=====================
How to Document TYPO3
=====================

:Version:
    |release|

:Language:
    en

:Author:
    TYPO3 contributors

:License:
    This document is published under the
    `Creative Commons BY 4.0 <https://creativecommons.org/licenses/by/4.0/>`__
    license.

:Rendered:
    |today|

----

This guide contains information about contributing to TYPO3 documentation,
writing documentation for TYPO3 extensions and formatting with
reStructuredText (reST).

----

..  card-grid::
    :columns: 1
    :columns-md: 2
    :gap: 4
    :class: pb-4
    :card-height: 100

    ..  card:: Migration

        Migrate your documentation to the new, PHP-based reST rendering.

        ..  card-footer:: :ref:`How to migrate to the new rendering <migrate>`
            :button-style: btn btn-secondary stretched-link


    ..  card:: Cheat sheet: reStructuredText

        Go tho the cheat sheet containing a quick overview on how to use reStructuredText.

        ..  card-footer:: :ref:`Go to the reST Cheat sheet <rest-cheat-sheet>`
            :button-style: btn btn-secondary stretched-link

    ..  card:: Edit on GitHub

        This chapter explains how to apply quick changes to the documentation
        you are reading by applying the "Edit on GitHub" workflow. All you
        need is a GitHub account.

        ..  card-footer:: :ref:`How to make quick fixes <docs-contribute-github-method>`
            :button-style: btn btn-secondary stretched-link

    ..  card:: Local rendering

        Using your local machine instead of editing documentation on GitHub has
        many advantages, it includes the freedom to choose which IDE you make
        your changes in and it also gives you the ability to experiment and
        preview your changes locally before submitting them for approval.

        ..  card-footer:: :ref:`How to work locally with documentation <docs-contribute-git-docker>`
            :button-style: btn btn-secondary stretched-link

    ..  card:: Extension documentation

        This chapter explains how to write documentation for a new extension.

        ..  card-footer:: :ref:`How to document an extension <write-doc-extensions-intro>`
            :button-style: btn btn-secondary stretched-link

    ..  card:: System Extensions

        The chapter contains information on how you can make changes to system extension documentation.

        ..  card-footer:: :ref:`How to document system extensions <contribute-to-system-extension>`
            :button-style: btn btn-secondary stretched-link

..  toctree::
    :hidden:
    :caption: BASICS

    Basics/About
    Basics/HowToGetHelp
    Basics/BasicPrinciples
    Basics/RstCheatSheet
    Basics/MdCheatSheet


..  toctree::
    :hidden:
    :caption: REFERENCE
    :glob:

    Reference/*
    Reference/ReStructuredText/Index
    Reference/CodingGuidelines/Index

..  toctree::
    :hidden:
    :caption: HOWTOS

    Howto/*
    Howto/*/Index

..  toctree::
    :hidden:
    :caption: ADVANCED

    Advanced/Index

..  toctree::
    :hidden:
    :caption: MAINTAINERS

    Maintainers/Index

..  Meta Menu

..  toctree::
    :hidden:

    Sitemap
