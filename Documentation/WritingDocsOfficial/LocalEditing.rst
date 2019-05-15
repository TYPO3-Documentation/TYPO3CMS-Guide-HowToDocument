.. include:: ../Includes.txt
.. highlight:: rst

.. _docs-contribute-git-docker:

=======================================
Local Editing and Rendering with Docker
=======================================

This section walks you through contributing to the documentation
with Git and Docker.

If necessary, ask for help as explained in :ref:`how-to-get-help`.


Quick Start
===========

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

   Clone the forked repository **from your workspace** (click *Clone or
   download* to copy the URL).

   In your terminal:

   .. code-block:: bash

      git clone https://github.com/<USERNAME>/<NAME OF REPOSITORY>.git


4. Create a branch

   For example, use the branch `feature/changes-in-cgl`:

   .. code-block:: bash

      git checkout -b feature/changes-in-cgl

5. Make changes

   Using your preferred IDE or editor, make changes to the files. Make
   sure you adhere to :ref:`format-rest-cgl`, e.g.
   use 3 spaces to indent (not tabs).

   If you are not familier with reST, you might want to check out
   :ref:`reST Introduction <writing-rest-introduction>` first!


6. Render the documentation

   Render with Docker in order to test the changes
   (see `Rendering Documentation With Docker <https://github.com/t3docs/docker-render-documentation/blob/master/README.rst>`__).

   .. code-block:: bash

      # this does a docker run and makes the
      # command dockrun_t3rdf available in your current terminal
      source <(docker run --rm t3docs/render-documentation show-shell-commands)

      # build documentation, will create directory Documentation-GENERATED-temp
      dockrun_t3rdf makehtml

      # open result in Browser
      # on MacOS:
      open "file:///$(pwd)/Documentation-GENERATED-temp/Result/project/0.0.0/Index.html"
      # on Linux:
      xdg-open "file:///$(pwd)/Documentation-GENERATED-temp/Result/project/0.0.0/Index.html"


7. Commit

   .. code-block:: bash

      git commit -a

   Write a short commit message, describing what was changed, for example
   "Fix link". See :ref:`general-conventions-commit-messages`, but keep in
   mind that the conventions for commit messages for the documentation are
   not strict.

8. Push changes

   .. code-block:: bash

      git push origin changes-in-cgl

   This will push the change to your forked repository.

9. Create Pull request

   Now, in your browser, visit the forked repository in your `GitHub
   <https://github.com/>`__ workspace. Github will already make
   some suggestions for a pull request and will display your pushed
   branch as "Your recently pushed branches".

   Click on the green button "Compare & pull request" and then
   "Create pull request".

10. Wait for someone to review and merge your pull request


You will receive notifications (email) about this. Once your change is
merged, you can reload the page (which you fixed) in your browser.

**Congratulations! You are now a contributor. Welcome and thank you!**


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


