..  include:: /Includes.rst.txt
..  highlight:: shell
..  index:: Changes; Backporting
..  _backport-changes:

================
Backport changes
================

Most of the time changes will be made to branch `main` and backported.

When creating a pull request, it is possible to add a `Releases` line in the
:ref:`commit message <general-conventions-commit-messages>`
(as done in the Core):

..  code-block:: text

    Releases: main, 12.4

However, this is not enforced and not always done. In any case, it is
up to the user merging a PR to decide how far the changes are to be
backported.

Here are some tips and conventions:

Community user: What should I do if I found an error in the documentation that applies to several versions?
===========================================================================================================

Apply your changes to the latest version you have verified your change
to work with. If it is possible, apply your change to the "main" branch.

Leave a hint about which versions you have tested, for example:

..  code-block:: text

    Verified this on 12.4 and 11.5, I suspect it will also still be the case on
    main. Could someone verify this please?

    Releases: main, 12.4, 11.5

The backporting itself will be done by the maintainers of the Documentation Team.
Sometimes automatic backporting is not possible due to changes in the documentation
structure. In such a case, you may be asked, if you would like to provide a pull
request for the back versions.

..  note::
    Only bugs will be backported more then one version. Improvements, etc may
    only be backported to the latest LTS release.


Merger: The pull request needs to be backported, what should I do?
==================================================================

When the pull request needs to be backported, add labels for all needed versions
to the pull request.

Example: If the pull request needs to be backported to version 12.4 and 11.5,
add the corresponding labels :guilabel:`backport 12.4` and
:guilabel:`backport 11.5`. The labels will trigger an automatic backport once
the current pull request is merged or the label is added to an already merged
pull request.

How do automatic backports work
===============================

The :abbr:`CI (Continous Integration)` runner will create a separate pull
request for each version that has been labeled - if, and only if, it can do the
cherry-picking into the branch without conflicts.

If the automatic backport is successful, a new pull request will be created for
the backport. This pull request can be approved and merged manually.

If the backport fails, a comment will be added to the original pull request. The
label :guilabel:`backport failed` will be added to the original pull request and
manual cherry-picking is required.

Up to which version?
====================

**Convention:** We backport to the newest LTS version unless the changes only
apply to the main version. Major errors and bug may be backported to the
older LTS version.

There may be reasons to do this differently:

*   Decisions about which versions to backport to are at the discretion of the
    user doing the merging.
*   Sometimes too many changes are necessary because of merge conflicts.
    Sometimes, the structure has changed. In this case, decide if it is worth
    the effort.


..  index:: GitHub; Squash and merge

How to merge?
=============

Using the second option in the green :guilabel:`Merge pull request` button
:guilabel:`Squash and merge` has proven useful for a number of
reasons:

*   This merges everything into one commit which makes it easier
    to cherry-pick.
*   This automatically adds the pull request number into the commit message
    which adds a reference to the original pull request when merging or
    cherry-picking this to another branch. That way the backport process is
    visible in the pull request.

If there are more than one contributor who committed changes, a text about
additional authors is automatically added to the commit.

..  seealso::

    *   `Configuring commit squashing for pull requests <https://docs.github.com/en/free-pro-team@latest/github/administering-a-repository/configuring-commit-squashing-for-pull-requests>`__


..  index:: GitHub; Backport

How to backport manually?
=========================

If you cherry-pick a commit locally, you can (optionally) use :shell:`-x` to
automatically insert information that this is a cherry-pick and
the original commit ID.

This makes the history clearer. Sometimes minor changes have
to be done while backporting to fix merge conflicts.

..  code-block:: shell

    git cherry-pick -x <commit-id>


This is how the commit might look like:

..  code-block:: shell

    Author: Author <email@example.org>
    Date:   Fri Jun 26 15:50:08 2023 +0200

        [TASK] Subject

        (cherry picked from commit 609493dd8893cbac7ad78aa38a23e02d011bb0c2)
