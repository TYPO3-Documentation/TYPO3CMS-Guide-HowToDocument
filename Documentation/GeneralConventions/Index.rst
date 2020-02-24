.. include:: ../Includes.txt
.. highlight:: rst

.. _general-conventions:
.. _conventions:

=================================
Documentation content style guide
=================================

This contains conventions, coding guidelines and best practices for TYPO3
documentation. In general, the documentation follows the conventions as
described in the following sections.

Finding common conventions is an ongoing task. Some of the decisions are
still pending. For a list of open topics, see the "Documentation" category
on `decisions.typo3.org <https://decisions.typo3.org/c/documentation>`__

The most important conventions are summarized on this page, the rest can
be found in the subchapters.

.. rst-class:: bignums-xxl

#. Title capitalization

   Use :ref:`sentence case <spelling-title-case>` - this means the title and
   headers will be capitalized like normal sentences. The first word
   is always capitalized and the rest is spelled as they would in
   "normal text".

   This is different from "TYPO3 content style guide" which capitalizes
   more words in the title. Capitalization in the documentation is still
   inconsistent currently, so you cannot rely on existing pages to show
   the correct convention.

#. Spelling

   Use common spelling for American English. Some specific TYPO3 terms
   have a special spelling. See :ref:`spelling-ref`

#. Coding guidelines for headers

   Headline underline should follow :ref:`rest-cgl-headline-underlines`::

      =====
      Title
      =====

      First header level
      ==================

      Second header level
      -------------------

      Third header level
      ~~~~~~~~~~~~~~~~~~

**Table of contents**

.. toctree::
   :maxdepth: 1

   ContentStyleGuide
   Glossary
   DirectoryFilenames
   Format
   MenuHierarchy
   CodingGuidelines
   GuidelinesForImages
   CommitMessages
   Licenses
