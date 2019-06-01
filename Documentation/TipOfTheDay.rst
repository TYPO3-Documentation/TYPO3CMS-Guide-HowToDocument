:orphan:

.. include:: Includes.txt

.. _Tip-of-the-day:

=============
Did you know?
=============

See also: :ref:`tips-extension-authors`

.. --------------------------------------------------------

.. _tip-branches-master:
.. rst-class:: panel panel-default

2019-06-01 - [IMPORTANT] Change Main Branches to master
=======================================================


This is important if you are using the
:ref:`Local Git / Docker workflow <docs-contribute-git-docker>` and
are working on already existing fork / clone.


Each documentation project has a main (or default) branch. This usually
corresponds to the latest released TYPO3 version.
For some official manuals, the main branch had been `latest`.
We now changed this, so that `master` is the main branch for all manuals.

**In the future, you should make sure to always work on master.**

When you create a new fork and clone, this should not be a problem.

But, when you are using a local repository that you cloned a while ago,
make sure to get the latest changes and work on `master` in the future.

.. rst-class:: bignums

   1. Check your branches:

      .. code-block:: bash

         git branch
      or

      .. code-block:: bash

         git branch -a

   2. Setup upstream remote

      This will get you changes from the original repository, not your fork.

      .. code-block:: bash

         git remote add upstream git@github.com:TYPO3-Documentation/<name of repository>.git

   3. Fetch from remote:

      .. code-block:: bash

         git fetch upstream

   4. Checkout master:

      .. code-block:: bash

         git checkout master


.. --------------------------------------------------------

For older, outdated tips, see :ref:`Tip-of-the-day-outdated`.
