.. include:: /Includes.rst.txt
.. highlight:: rst
.. index:: ! Reviewing manuals
.. _guidelines-for-reviewing:

================================
Guidelines for reviewing manuals
================================

Reviewing manuals and finding a workflow for this is still a work in progress.

See the :ref:`Related Issues <review-workflow-related-issues>`.


An overview of all manual maintainers and review status is maintained
in the `Wiki <https://wiki.typo3.org/DocTeam/Official_Documentation_Maintenance>`__.


.. index:: Reviewing manuals; Guidelines

Guidelines for reviewing
========================

#. Preferably, an entire branch should be systematically reviewed.
   In that case, just :ref:`add a status to the start page <add-review-info-to-startpage>`
   with information when it was last
   reviewed and for which version.
#. When you come across a single page that is outdated, preferably fix it right away.
   If you can't, :ref:`add a warning <reviewInfoWarning>`, but also make
   sure to write an issue.
#. For branches that have not been entirely reviewed yet and that are too comprehensive
   to do this in one sitting, a procedure should be selected to systematically review.
   This can be decided on a case by case basis for each manual / branch.


What to watch out for while reviewing:

*  **Duplicate content:** Check for similar content in other manuals (and the TYPO3 Wiki).
   Merge duplicate content: Decide where the content should live, remove it in the
   other places and add links.
*  **Remove redundant content:** Keep content short and to the point.
   For things that are not TYPO3-specific: Link elsewhere if good
   documentation is already available elsewhere.
*  **Technical correctness:** Is information correct and up-to-date (for version of
   branch)? Does it propagate good best practices (instead of deprecated ones)?
*  **Didactic:** Is the text easy to understand and follow? For lengthy texts: Is there
   a quick start or a summary at the beginning (Example: :ref:`Logging Quick Start <t3coreapi:logging-quickstart>`)?
*  **Language correctness:** Spelling, grammar, style.

Not everyone is a native English speaker and not everyone knows TYPO3 inside-out. It
is entirely fine to only focus on one aspect at a time (e.g. language) while reviewing.


Examples for review information
===============================

Until we can be sure, that the published documentation is generally correct and up-to-date,
you can add review information.

There are 3 goals here:

#. Warn readers about outdated information (must be visible on the rendered page).
#. Help reviewers to quickly see which state a page is in without having to read the entire
   page.
#. Help reviewers to keep track of reviewed / unreviewed  pages. It should be possible to
   mark pages that have been already checked as ok or not ok and find all unchecked pages
   or find all pages with problems.


.. index::
   Reviewing manuals; Review information
   Reviewing manuals; Outdated contend
   reST directives; Status
.. _add-review-info-to-startpage:

Add review information to the start page
----------------------------------------

Once the entire branch has been reviewed and updated, you can add this
information to the start page:

:Status:
      Tested and reviewed for TYPO3 9.5.5 on April 11, 2019

.. code-block:: rest

   :Status:
         Tested and reviewed for TYPO3 9.5.5 on April 11, 2019

*If* pages become outdated and are not fixed immediately, you can modify
the review information on the start page, e.g.


:Status:
      Last tested and reviewed for TYPO3 9.5.5 on April 11, 2019, some pages outdated

.. code-block:: rest

   :Status:
         Last tested and reviewed for TYPO3 9.5.5 on April 11, 2019, some pages outdated



Examples:

*  :ref:`t3start:start`.


.. index::
   Reviewing manuals; Outdated contend
   reST directives; warning
.. _reviewInfoWarning:

Add warning for outdated content
---------------------------------

If the information is clearly outdated (or incorrect), you should add
a **visible** warning to warn readers.

Better would be to update the page. So, this should only be done in the rare
cases where updating is not possible immediately.

.. warning::

   The information on this page is outdated!

.. code-block:: rest

   .. warning::

      The information on this page is outdated!


.. index::
   Reviewing manuals; Todo
   reST directives; todo

Todo directive
--------------

The "todo" directive will not get rendered by default.

Examples of review information with todo:

.. code-block:: rest

   .. todo:: Needs review: Outdated (2019/5/15 TYPO3 9.5.5)

   .. todo:: Needs review: Improved language (2019/5/15 TYPO3 9.5.5)

In order to render this, add this to :file:`Settings.cfg`:

.. code-block:: none

   [extensions]
   todo_include_todos=True


.. _review-workflow-related-issues:

Related issues
==============

*  `Find a workflow for reviewing / updating / refining manuals <https://github.com/TYPO3-Documentation/T3DocTeam/issues/7>`__
*  `Update the docs before we release the new version. <https://github.com/TYPO3-Documentation/T3DocTeam/issues/70>`__
