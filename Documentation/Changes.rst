:orphan:
.. include:: /Includes.rst.txt
.. index:: ! Changes
.. _changes:

=======
Changes
=======


.. index::
   Changes; Master branches to main
   Git; Branch main
   Git; Branch master (outdated)
.. _tip-branches-main:
.. rst-class:: panel panel-default

[IMPORTANT] Change master branches to main
==========================================


This is important if you are using the
:ref:`Local Git / Docker workflow <docs-contribute-git-docker>` and
are working on already existing fork / clone.

Each documentation project has a main (or default) branch. This usually
corresponds to the latest released TYPO3 version.
For some official manuals, the main branch had been `master`.
We now changed this, so that `main` is the main branch for all manuals.

**In the future, you should make sure to always work on branch main.**

When you create a new fork and clone, this should not be a problem.

But, when you are using a local repository that you cloned a while ago,
make sure to get the latest changes and work on `main` in the future.

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

   4. Checkout main branch:

      .. code-block:: bash

         git checkout main


.. index::
   Changes; Extension manual migration
   Extensions; Manual migration
.. _tip-ext-new-doc-server:
.. rst-class:: panel panel-default

[IMPORTANT] Extension manual migration to the new infrastructure
================================================================

Because of the
`move to the new documentation server <https://typo3.org/article/docstypo3org-gets-new-infrastructure/>`__,
a valid composer.json
and a webhook is now mandatory for extensions, in order to automatically be
rendered on the documentation server.

Read more: :ref:`migrate`

If you see the following on the rendered page of your extension, it has not
yet been rendered with the new mechanism:

.. figure:: images/docs_deprecation.png
   :class: with-shadow
   :alt: Deprecation message on rendered extension documentation page

   Deprecation message on rendered extension documentation page
