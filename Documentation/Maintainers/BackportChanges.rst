.. include:: /Includes.rst.txt
.. highlight:: shell
.. index:: Changes; Backporting
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

Community user: What should I do if I found an error in the documentation that applies to several versions?
===========================================================================================================

Apply your changes to the latest version you have verified your change 
to work with. If it is possible, apply your changed to the branch `master`.  

Leave a hint about which versions you have tested, for example:

.. code-block:: none
   Verified this on 10.4 and 9.5, I suspect it will also still be the case on master. Could
   someone verify this please?

   Releases: master, 10.4, 9.5
   
The backporting itself will be done by the maintainers of the documentation team.
Sometimes automatic backporting is not possible due to changes in the documentation 
structure. In such a case you will be asked if you would like to provide a pull 
request for the back versions.

.. note::
   Only bugs will be backported more then one version. Improvements etc can only be 
   backported to the latest LTS release.


Merger: The pull request need to be backported, what should I do?
=================================================================

When the PR needs also to be backported, put a note about the versions in a comments 
if they are not there yet:

.. code-block:: none

   Releases: master, 10.4
   
Add the label `backport required` to the PR. Merge the PR into master whenever possible.
Otherwise merge it into the latest version it applies to.

Who is doing the backport?
==========================

As it is usually more work to do each backport separately as doing them all at once we 
collect the backports by marking the PR with the label `label:"backport required"`.

The maintainer doing the sweeping week will then apply all backports that can be done 
automatically by the end of the month. Backports that need to be handed manually can be 
send back to the author of the PR. In such a case a separate PR for the version in question 
needs to be made by the author.

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


.. index:: GitHub; Squash and merge

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

.. seealso::

   * `Configuring commit squashing for pull requests <https://docs.github.com/en/free-pro-team@latest/github/administering-a-repository/configuring-commit-squashing-for-pull-requests>`__


.. index:: GitHub; Backport

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


