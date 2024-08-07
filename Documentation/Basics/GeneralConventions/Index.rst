.. include:: /Includes.rst.txt
.. index:: Documentation; Content style guide
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

#. Version hints

   :ref:`version-hints` describes how to add version hints for new sections
   or chapters:

   .. code-block:: rst

      .. deprecated:: 10.2
         The hook shown here is deprecated since TYPO3 10.2 - use a custom
         :ref:`PSR-15 middleware<request-handling>` instead.

      .. versionadded:: 10.2
         Starting with TYPO3 10.2 hooks and signals have been replaced by a PSR-14 based
         event dispatching system.

      .. versionchanged:: 2.3.1
         This feature was changed ...

#. Link to the changelog

   :ref:`link-to-changelog` describes how to link to the changelog:

   .. code-block:: rst

      :ref:`ext_core:feature-101544-1691063522`


#. Coding guidelines for headers

   Headline underline should follow :ref:`rest-cgl-headline-underlines`

   .. code-block:: rst

      =====
      Title
      =====

      First header level
      ==================

      Second header level
      -------------------

      Third header level
      ~~~~~~~~~~~~~~~~~~

   .. seealso::

      *  :ref:`format-rest-cgl`

#. Refer to elements in the GUI with :rst:`:guilabel:`

   Example:

   .. code-block:: rst

      :guilabel:`Admin Tools > Extensions`

   This will look like this: :guilabel:`Admin Tools > Extensions`

..  toctree::
    :caption: Table of contents
    :maxdepth: 1

    ReviewPolicy
    ContentStyleGuide
    Glossary
    Format
    CodingGuidelines
    GuidelinesForImages
    Licenses
