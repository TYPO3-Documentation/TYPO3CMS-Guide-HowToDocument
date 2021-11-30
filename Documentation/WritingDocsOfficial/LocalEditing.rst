.. include:: /Includes.rst.txt
.. highlight:: rst
.. index:: Official documentation; Local editing
.. _docs-contribute-git-docker:

======================================================
Workflow #2: "Local editing and rendering with Docker"
======================================================

Using your local machine instead of editing documentation on GitHub has many advantages, it includes
the freedom to choose which IDE you make your changes in (see :ref:`tools-for-editing-rest`) and it also gives you
the ability to experiment and preview your changes locally before submitting them for approval.

.. rst-class:: bignums-xxl

1. Create a GitHub account:

   Visit `Join GitHub <https://github.com/join>`__ and create your account.

   Though not mandatory, the general convention in the TYPO3 community is
   to set your GitHub name (*not* username) as your full name.

2. Find and fork the repository

   In the footer of the documentation you wish to make changes to,
   select the :guilabel:`Repository` link.

   This will take you to the documentations repository in GitHub.

   From here, select the "Fork" button in the upper right corner of the page.

   .. image:: ../images/github-fork.png
      :class: with-shadow

3. Clone the forked repository

   Clone the **forked repository from your workspace** (select *Clone or
   download* to copy the URL).

   In your terminal:

   .. code-block:: bash

      git clone https://github.com/<USERNAME>/<NAME OF REPOSITORY>.git


4. Setup Git Settings and SSH Key

   For this, we refer to the general help on Git and GitHub:

   Setup `username <https://help.github.com/en/articles/setting-your-username-in-git>`__
   and `email <https://help.github.com/en/articles/setting-your-commit-email-address-in-git>`__
   (if not already setup in your global :file:`~/.gitconfig`).

   `Setup your .ssh key for GitHub <https://help.github.com/en/enterprise/2.15/user/articles/adding-a-new-ssh-key-to-your-github-account>`__

5. Create a branch for your changes


   .. important::

      If you did not just fork and clone but are instead using an old local version of this repository:

      #. Make sure the repository is up-to-date by pulling from upstream as described
         in :ref:`contribute-edit-locally-more-changes`.
      #. Always branch from `main` (see also :ref:`tip-branches-main`).
         If you are checked in to a feature branch, switch back to `main`
         first:

         .. code-block:: bash

            git checkout main

   For example, create the branch `feature/changes-in-cgl`:

   .. code-block:: bash

      git checkout -b feature/changes-in-cgl

6. Make your changes

   Using your preferred IDE or editor you can now start making your changes.

   If you are not familiar with reST, you can visit the
   :ref:`reST Introduction <writing-rest-introduction>` to help get you started
   along with the :ref:`rest-cheat-sheet`.

7. Render the documentation

   Render your changes with Docker to preview them locally:

   *  :ref:`render-documenation-with-docker` (works best on Linux)
   *  :ref:`render-with-docker-compose` (should work better on MacOS
      and Windows, but is still in development)

8. Commit

   .. code-block:: bash

      git commit -a

   Write a short, meaningful commit message describing what changes you have made.
   See :ref:`general-conventions-commit-messages` for more information on how to
   word your commit messages.

9. Push changes

   .. code-block:: bash

      git push origin changes-in-cgl

   This will push the change to your forked repository.

10. Create Pull request

    Now, in your browser, visit the forked repository in your `GitHub
    <https://github.com/>`__ workspace. GitHub will already make
    some suggestions for a pull request and will display your pushed
    branch as "Your recently pushed branches".

    Click on the green button "Compare & pull request" and then
    "Create pull request".

    Your change will now be reviewed. A reviewer might
    suggest additional changes. Monitor your notifications (email) from GitHub. If at any
    point, you are not sure what to do, don't hesitate to
    :ref:`ask for help <how-to-get-help>`. When your pull request is accepted,
    it will be merged. You will receive a notification email as soon as this happens.

**Congratulations! You are now a contributor. Welcome and thank you!**


Next steps
==========

*  Look at :ref:`docs-official-how-you-can-help` for more ways to contribute.


.. index:: Official documentation; Fork up-to date
.. _contribute-edit-locally-more-changes:

Keeping your local fork up-to date
===============================

Explanation
-----------

This section describes how to keep your local repository up-to-date. This is
similar to the GitHub documentation in chapter `Keep your fork synced
<https://docs.github.com/en/github/getting-started-with-github/fork-a-repo#keep-your-fork-synced>`__.

If you have already created a patch for a repository, you can reuse your
local repository. This means you do not have to fork and clone for every new patch.

However, if you reuse your local clone, you should make sure it is up-to-date
before you create another branch for a new patch.

You local repository is based on the forked repository in your workspace.

For example,

*  URL of fork:  `git@github.com:<your username>/TYPO3CMS-Guide-HowToDocument.git`
*  original URL: `git@github.com:TYPO3-Documentation/TYPO3CMS-Guide-HowToDocument.git`

So, running the following will not get the latest changes:


.. code-block:: bash

   git pull origin main

because origin points to your fork.


Do it now
---------

You must now do the following:

.. code-block:: bash

   git remote add upstream git@github.com:TYPO3-Documentation/TYPO3CMS-Guide-HowToDocument.git
   git pull upstream main


Replace the URI with the correct URI for the original repository, not your fork!

The URL for upstream has now been written to :file:`.git/config` in your local repository,
so next time it is enough to do:

.. code-block:: bash

   git pull upstream main


Now, continue with step 5 (create branch) in :ref:`edit-locally-quickstart`.


More information
================

For more information in this guide:

*  :ref:`Formatting-with-reST`
*  `Rendering Documentation With Docker <https://github.com/t3docs/docker-render-documentation/blob/main/README.rst>`__


For more information about GitHub see the help pages on GitHub or other
resources, for example:

*  `Creating a pull request from a fork
   <https://help.github.com/articles/creating-a-pull-request-from-a-fork/>`__
*  `How to Create a Pull Request on GitHub
   <https://www.digitalocean.com/community/tutorials/how-to-create-a-pull-request-on-github>`__
*  `Fork a repo <https://help.github.com/en/articles/fork-a-repo>`__


