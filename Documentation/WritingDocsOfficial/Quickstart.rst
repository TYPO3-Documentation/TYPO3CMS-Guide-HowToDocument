.. include:: ../Includes.txt
.. highlight:: rst



.. _docs-contribute-quickstart:
.. _docs-contribute-git-docker:

===============================
Quick start with git and docker
===============================


.. important::

   Read the :ref:`general-conventions` first!


The quickstart walks you through contributing to the documenation
with git and docker.

If necessary, ask for help as explained in :ref:`how-to-get-help`.

.. rst-class:: bignums-xxl

1. Get a `Github <https://github.com>`__ account

   The general convention in the TYPO3 community is to use your full
   real name as name (*not* username), but it is not a requirement.

   Be sure to use an email-address that you will regularly check as
   soon as you upload changes to Github.

2. Find and fork the repository

   Find the repository for the manual you wish to make changes to.
   On the lower left side of the rendered documentation, click on
   the link "Related Links". Then click on the link "Repository".


   .. image:: ../images/related-links.png
      :class: with-shadow


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

   for example, use the branch `feature/changes-in-cgl`:

   .. code-block:: bash

      git checkout -b feature/changes-in-cgl

5. Make changes

   Using your preferred IDE or editor, make changes to the files. Make
   sure you adhere to :ref:`format-rest-cgl`, e.g.
   use 3 spaces to indent (not tabs).

   Look up reST format if necessary: :ref:`Formatting-with-reST`.


6. Render the documentation

   Render with docker in order to test the changes (see :ref:`rendering-docs`).

   .. code-block:: bash

      source <(docker run --rm t3docs/render-documentation show-shell-commands)
      dockrun_t3rdf makehtml

7. Commit

   .. code-block:: bash

      git commit -a

   See :ref:`general-conventions-commit-messages`.


8. Push changes

   .. code-block:: bash

      git push origin changes-in-cgl

9. Create Pull request

   Now, in your browser, visit the forked repository in your Github
   workspace. Github will already make some suggestions for a Pull
   Request and will display your pushed branch as "Your recently
   pushed branches".

   Now, click on the green button "Compare & pull request" and then
   "Create pull request".

10. You must now wait for someone to review and merge your Pull Request

   You will receive notifications about this to the email adress you
   used when registering for Github.


More information
================

For more information in this guide:

* :ref:`Formatting-with-reST`
* :ref:`rendering-docs`


For more information about Github see the help pages on Github or other
resources, for example:

* `Creating a pull request from a fork
  <https://help.github.com/articles/creating-a-pull-request-from-a-fork/>`__
* `How to Create a Pull Request on GitHub
  <https://www.digitalocean.com/community/tutorials/how-to-create-a-pull-request-on-github>`__


