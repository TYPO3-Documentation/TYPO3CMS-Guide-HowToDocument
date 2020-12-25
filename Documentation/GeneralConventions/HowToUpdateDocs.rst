.. include:: /Includes.rst.txt
.. highlight:: rst
.. index::
   Documentation; Update
   Documentation; New releases
.. _howto-update-docs:
.. _update-docs:

=====================================
Update documentation for new releases
=====================================

Once a new TYPO3 release comes out, the main documentation (e.g. :ref:`t3coreapi:start`,
:ref:`t3tca:start` etc.) must be updated.

Here, we describe some best practices for updating the official documentation
for a new TYPO3 release. We stick to the core conventions as much as possible because that
makes it easier for everyone to contribute to documentation and core.


.. index::
   Documentation; Deprecations
   Documentation; Breaking changes

How to handle deprecations and breaking changes
===============================================

.. important::

   We used to follow the conventions, that deprecated features were entirely removed from the
   documentation as soon as they are deprecated. This no longer applies: We recommend to
   add some information about the deprecation where this may be helpful.

This has the disadvantage that the documentation must be modified twice: once to point out
the deprecation, and finally to remove it.

But, on the other hand, we have found that it is more user friendly to **document the
deprecation and the alternative to make migration easier**. This mean, we do not (yet)
remove the deprecated information entirely. This gives people more
time to adjust to the changes. Also, deprecated features may still be used, but if the
documentation were removed entirely, a search for documentation would direct everyone to a previous
version where the feature is still documented without mentioning the deprecation.

See the next section for some examples.

.. index::
   Documentation; Version hints
   reST; Version hints
   reST; `deprecated`
   reST; `versionadded`
   reST; `versionchanged`

How to add version hints
========================

Example, how you can point out **deprecations**::

   .. deprecated:: 10.2
      The hook shown here is deprecated since TYPO3 10.2 - use a custom
      :ref:`PSR-15 middleware<request-handling>` instead.

New **feature**::

   .. versionadded:: 10.2
      Starting with TYPO3 10.2 hooks and signals have been replaced by a PSR-14 based
      event dispatching system.


Changes::

   .. versionchanged:: 2.3.1
      This feature was changed ...

Further information:

*  see the open issue: `Should we display version hints <https://github.com/TYPO3-Documentation/T3DocTeam/issues/14>`__
*  General section about reST CGL: :ref:`version-hints`

.. index::
   reST; Changelog links
   reST; `:doc:`

Link to changelog
=================

How to link to the changelog is described in :ref:`link-to-changelog`.

.. code-block:: rest

   :doc:`t3core:Changelog/8.1/Deprecation-75625-DeprecatedCacheClearingOptions`

For this to work, t3core must be defined in :file:`Settings.cfg`


.. index:: Updates; Issues

Issues
======

*  It is not necessary to create an issue for every change.


.. index:: pair: Updates; Commit messages

Commit messages
===============

The commit message can point out the releases to which the change should apply
(as in the core commits), e.g. `Releases: master, 9.5`, see
:ref:`general-conventions-commit-messages`.

You can link to the issue for the changes in the team repository, for example::

   Related: TYPO3-Documentation/T3DocTeam#121


.. index:: Updates; Several releases

Applying changes to several releases
====================================

Sometimes a necessary change applies to several major versions. Example: A change in
the documentation is necessary in current master (10) and also in 9.5 branch.

If this is the case, it is recommended to:

*  apply the change to the lower version (9.5 in our example) first, and then create
   another PR for the higher version making necessary additional changes. This is the
   reverse order of what is being used in the Core!
*  The person merging the commit should take care of merging into other branches as well
   (in case that is necessary). This is the same convention as in the core.
*  The changes can be bundled into one commit and the commit / PR can have a subject
   such as:

.. code-block:: none

   [TASK] Update with changes from 9.5.3

This makes it easier to find related changes and check for which version a branch was last
updated.


.. index::
   Documentation; Status
   reST; `:Status:`

How to mark what state a manual is in
=====================================

In order to keep track of which changes have already been applied and give readers hints
about how up to date a manual is, you can optionally add a "Status" to the start page
(:file:`Documentation/Index.rst`).

For example::

   :Status:
      ok (Fully reviewed for TYPO3 9.5.9 on July 22, 2019)

If the manual has not been fully reviewed, but all changelogs up to 9.5.9 have been
applied, you might use::


   :Status:
      needs review (All changelogs <= TYPO3 9.5.9 have been applied)

See :ref:`t3start:start`.


Work in progress
================

Several suggestions have been made to improve the process but these still require
more work or a decision, e.g.

*  `Should we display version hints <https://github.com/TYPO3-Documentation/T3DocTeam/issues/14>`__
*  `Link to changelog <https://github.com/TYPO3-Documentation/TYPO3CMS-Guide-HowToDocument/issues/110>`__
*  `How can we get changes added to documentation early? And what is master: master or latest release? <https://github.com/TYPO3-Documentation/T3DocTeam/issues/133>`__
*  `Add information when page / manual was last reviewed and what state it is in <https://github.com/TYPO3-Documentation/T3DocTeam/issues/73>`__
*  `Find a workflow for reviewing / updating / refining manuals <https://github.com/TYPO3-Documentation/T3DocTeam/issues/7>`__

