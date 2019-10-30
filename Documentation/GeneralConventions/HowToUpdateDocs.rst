.. include:: ../Includes.txt
.. highlight:: rst

.. _howto-update-docs:
.. _update-docs:

=====================================
Update Documentation for New Releases
=====================================

Once a new TYPO3 release comes out, the main documentation (e.g. :ref:`t3coreapi:start`,
:ref:`t3tca:start` etc.) must be updated.

Here, we describe some best practices for updating the official documentation
for a new TYPO3 release. We stick to the core conventions as much as possible because that
makes it easier for everyone to contribute to documentation and core.

.. hint::

   These are not strict rules, but rather recommendations. If a better method is found and
   used, please update this page.

How to Handle Deprecations and Breaking Changes
===============================================

.. important::

   We used to follow the conventions, that deprecated features were entirely removed from the
   documentation as soon as they are deprecated. This no longer applies: We recommend to
   add some information about the deprecation where this may be helpful.

This has the disadvantage that the documentation must be modified twice: once to point out
the documentation, and finally to remove it.

But, on the other hand, we have found that it is more user friendly to **document the
deprecation and the alternative to make migration easier**. This mean, we do not (yet)
remove the deprecated information entirely. This gives people more
time to adjust to the changes. Also, deprecated features may still be used, but if the
documentation were removed entirely, a search for documentation would direct everyone to a previous
version where the feature is still documented without mentioning the deprecation.

While we recommend for developers to read the Changelogs we should not make this a necessary
requirement. It should be possible to get enough information from reading the main docs.

Here are some examples, how you can point out deprecations:

.. code-block:: rest

   .. warning::
      The hook shown here is deprecated since TYPO3 v9 - use a custom
      :ref:`PSR-15 middleware<request-handling>` instead.


.. code-block:: rest

   .. note::
      Starting with TYPO3 v10 hooks and signals have been replaced by a PSR-14 based
      event dispatching system.

.. code-block:: rest

   The symfony expression language has been implemented for TypoScript conditions in
   both frontend and backend since TYPO3 9.4.


see

* :ref:`t3coreapi:hooks-creation`
* :ref:`t3tsref:conditions`


Issues
======

* It is not necessary to create an issue for every change.

Commit Messages
===============

The commit message can point out the releases to which the change should apply
(as in the core commits), e.g. `Releases: master, 9.5`, see
:ref:`general-conventions-commit-messages`.

Applying Changes to Several Releases
====================================

Sometimes a necessary change applies to several major versions. Example: A change in
the documentation is necessary in current master (10) and also in 9.5 branch.

If this is the case, it is recommended to:

* apply the change to the lower version (9.5 in our example) first, and then create
  another PR for the higher version making necessary additional changes. This is the
  reverse order of what is being used in the core!
* The person merging the commit should take care of merging into other branches as well
  (in case that is necessary). This is the same convention as in the core.
* The changes can be bundled into one commit and the commit / PR can have a subject
  such as:

.. code-block:: none

   [TASK] Update with changes from 9.5.3

This makes it easier to find related changes and check for which version a branch was last
updated.

How to Mark What State a Manual is in
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


Work in Progress
================

Several suggestions have been made to improve the process but these still require
more work or a decision, e.g.

* `Should we display version hints <https://github.com/TYPO3-Documentation/T3DocTeam/issues/14>`__
* `Add information when page / manual was last reviewed and what state it is in <https://github.com/TYPO3-Documentation/T3DocTeam/issues/73>`__
* `Find a workflow for reviewing / updating / refining manuals <https://github.com/TYPO3-Documentation/T3DocTeam/issues/7>`__

