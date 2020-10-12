.. include:: /Includes.txt

.. highlight:: shell

.. _backport-changes:

================
Backport changes
================

Most of the time changes will be made to master and backported.

When creating a PR, it is possible to add the Releases in the
:ref:`commit message <general-conventions-commit-messages>`
(as done in the core):

.. code-block:: none

   Releases: master, 10.4

However, this is not enforced and not always done. In any case, it is
up to the user merging a PR to decide how far the changes are to be
backported.

Here are some tips and conventions:

Who should backport?
====================

The user merging should take care of the backporting.

Up to which version?
====================

**Convention:** We backport to the versions still in LTS
(if the change applies to them).

There may be reasons to do this differently:

* Decisions about which versions to backport to are at
  the discretion of this user doing the merging.
* Sometimes too many changes are necessary because of merge conflicts.
  Sometimes, the structure has changed. In this case,
  decide if it is worth the effort.


How to merge?
=============

Using the second option in the green "Merge pull request" button
:guilabel:`Squash and merge` has proven useful for a number of
reasons:

#. This merges everything into one commit which makes it easier
   to cherry pick
#. This automatically adds the PR number into the commit message
   which adds a reference to the original PR when
   merging or cherry-picking this to another branch. That way
   the backport process is visible in the pull request.

If there are more than 1 contributor who committed changes, a
text about additional authors is automatically added to the commit.


How to backport?
================

If you cherry-pick a commit locally, you can (optionally) use -x to
automatically insert information that this is a cherry-pick and
the original commit id.

This makes the history clearer. Sometimes minor changes have
to be done while backporting to fix merge conflicts.

.. code-block:: shell

   git cherry-pick -x <commit-id>


This is how the commit might look like:

.. code-block:: shell

   Author: Author <email>
   Date:   Fri Jun 26 15:50:08 2020 +0200

      [TASK] Subject

      (cherry picked from commit 609493dd8893cbac7ad78aa38a23e02d011bb0c2)


