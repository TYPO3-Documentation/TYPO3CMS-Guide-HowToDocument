.. include:: ../Includes.txt
.. highlight:: rst

.. _docs-contribute-git-docker:

======================================================
Workflow #2: "Local Editing and Rendering with Docker"
======================================================

This section walks you through contributing to the documentation
with Git and Docker.

If necessary, ask for help as explained in :ref:`how-to-get-help`.


.. _edit-locally-quickstart:

Quick Start
===========


This describes how to create a pull request for the TYPO3 documentation. All
steps described are steps you would usually do for any GitHub pull
request. Only the part about editing (step 6) and rendering (step 7)
are specific to TYPO3 documentation.



.. rst-class:: bignums-xxl

1. Get a `Github <https://github.com>`__ account:

   Fill out the form on `Join Github <https://github.com/join>`__.

   The general convention in the TYPO3 community is to use your full
   real name as name (*not* username), but it is not a requirement.

   Be sure to use an email-address that you will regularly check as
   soon as you upload changes to Github.

2. Find and fork the repository

   Find the repository for the manual you wish to make changes to.
   On the lower left side of the rendered documentation, click on
   the link "Related Links". Then click on the link "Repository".


   This will direct you to the repository on Github.

   There, click on the "Fork" button in the upper right.

   .. image:: ../images/github-fork.png
      :class: with-shadow

   .. note::
      The repository will be forked to your workspace on Github. You can
      delete it later or reuse it for further changes.


3. Clone the forked repository

   Clone the **forked repository from your workspace** (click *Clone or
   download* to copy the URL).

   In your terminal:

   .. code-block:: bash

      git clone https://github.com/<USERNAME>/<NAME OF REPOSITORY>.git


4. Setup Git Settings and SSH Key

   For this, we refer to general help on Git or GitHub:

   Setup `username <https://help.github.com/en/articles/setting-your-username-in-git>`__
   and `email <https://help.github.com/en/articles/setting-your-commit-email-address-in-git>`__
   (if not already setup in your global :file:`~/.gitconfig`).


   `Setup your .ssh key for GitHub <https://help.github.com/en/enterprise/2.15/user/articles/adding-a-new-ssh-key-to-your-github-account>`__

5. Create a branch


   .. important::

      If you did not just fork and clone but are using a local repository, you created a while ago:

      #. Make sure the repository is up-to-date by pulling from upstream as described
         in :ref:`contribute-edit-locally-more-changes`.
      #. Always branch from *master* (see also :ref:`tip-branches-master`).
         If you have still checked out a feature branch, switch back to  *master*
         first:

         .. code-block:: bash

            git checkout master

   For example, create the branch `feature/changes-in-cgl`:

   .. code-block:: bash

      git checkout -b feature/changes-in-cgl

6. Make changes

   Using your preferred IDE or editor, make changes to the files. Make
   sure you adhere to :ref:`format-rest-cgl`, e.g.
   use 3 spaces to indent (not tabs).

   If you are not familier with reST, you might want to check out
   :ref:`reST Introduction <writing-rest-introduction>` first!

   Also, see our :ref:`rest-cheat-sheet` in this guide.


7. Render the documentation

   Render with Docker in order to test the changes:

   * :ref:`render-documenation-with-docker` (works best on Linux)
   * :ref:`render-with-docker-compose` (should work better on MacOS
     or Windows, but is still being tested)

8. Commit

   .. code-block:: bash

      git commit -a

   Write a short commit message, describing what was changed, for example
   "Fix link". See :ref:`general-conventions-commit-messages`, but keep in
   mind that the conventions for commit messages for the documentation are
   not strict.

9. Push changes

   .. code-block:: bash

      git push origin changes-in-cgl

   This will push the change to your forked repository.

10. Create Pull request

   Now, in your browser, visit the forked repository in your `GitHub
   <https://github.com/>`__ workspace. Github will already make
   some suggestions for a pull request and will display your pushed
   branch as "Your recently pushed branches".

   Click on the green button "Compare & pull request" and then
   "Create pull request".



Now, wait for someone to review and merge your pull request


You will receive notifications (email) about this. Once your change is
merged, you can reload the page (which you fixed) in your browser.

**Congratulations! You are now a contributor. Welcome and thank you!**


.. _contribute-edit-locally-more-changes:

Keep Your Local Fork Up-to-date
===============================

Explanation
-----------

This section describes how to keep your local repository up-to-date. This is
similar to the section "Keep your fork synced" on the online resource
`Fork a repo <https://help.github.com/en/articles/fork-a-repo>`__.

If you have already created a patch for a repository, you can reuse your
local repository. This means you do not have to fork and clone for every new patch.

However, if you reuse your local clone, you should make sure it is up-to-date
before you create the another branch for a new patch.

You local repository is based on the forked repository in your workspace.

For example,

* URL of fork:  `git@github.com:<your username>/TYPO3CMS-Guide-HowToDocument.git`
* original URL: `git@github.com:TYPO3-Documentation/TYPO3CMS-Guide-HowToDocument.git`

So, running the following will not get the latest changes:


.. code-block:: bash

   git pull origin master

because origin points to your fork.



Do it Now
---------

You must now do the following:

.. code-block:: bash

   git remote add upstream git@github.com:TYPO3-Documentation/TYPO3CMS-Guide-HowToDocument.git
   git pull upstream master

.. important::

   Some repositories use main branch "latest", not "master". In that case use "latest" instead
   of master.


Replace the URI with the correct URI for the original repository, not your fork!

The URL for upstream has now been written to :file:`.git/config` in your local repository,
so next time it is enough to do:

.. code-block:: bash

   git pull upstream master


Now, continue with step 5 (create branch) in :ref:`edit-locally-quickstart`.


More information
================

For more information in this guide:

* :ref:`Formatting-with-reST`
* `Rendering Documentation With Docker <https://github.com/t3docs/docker-render-documentation/blob/master/README.rst>`__


For more information about GitHub see the help pages on Github or other
resources, for example:

* `Creating a pull request from a fork
  <https://help.github.com/articles/creating-a-pull-request-from-a-fork/>`__
* `How to Create a Pull Request on GitHub
  <https://www.digitalocean.com/community/tutorials/how-to-create-a-pull-request-on-github>`__
* `Fork a repo <https://help.github.com/en/articles/fork-a-repo>`__


