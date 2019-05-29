.. include:: ../Includes.txt
.. highlight:: rst

.. _contribute-to-system-extension:

==============================
Contribute to System Extension
==============================

The documentation for system extensions is maintained inside the TYPO3
source code, so the contribution workflow is a little different.

For more information about the various contribution workflows,
see :ref:`overview-of-types`.

* When it comes to documentation that is contained within the
  core (like system extension documentation and changelog), you would
  use Forge to report **issues**, using the category "Documentation":
  https://forge.typo3.org/projects/typo3cms-core/issues
* The :ref:`t3contribute:start` explains the **contribution workflow** for the core.
  For making a change to the documentation in the core, you would use the
  workflow explained in that guide (using Git and pushing to Gerrit).
* You can also test the change by :ref:`rendering locally <rendering-docs>`
  as in any documentation patch, because all documentation uses a common
  format and :ref:`file structure <general-conventions-dir-and-filenames>`
  and can be rendered with the same Docker container.

.. tip::

   There is an easy shortcut for minor changes: You can use
   the `Edit me on GitHub method <docs-contribute-github-method>`__ for
   minor changes to system extensions and the changelog. Under the hood,
   a patch will get created and pushed to Gerrit and you will find a
   comment in your pull request with information about where to find your patch
   on Gerrit.

   .. image:: ../images/github-gerrit.png
      :class: with-shadow
      :target: https://github.com/TYPO3/TYPO3.CMS/pull/172#issuecomment-494721296

See `System Extensions <https://docs.typo3.org/typo3cms/SystemExtensions/Index.html>`__
for a list of system extension documentation.

Use the `sample extension manual <https://github.com/TYPO3-Documentation/TYPO3CMS-Example-ExtensionManual>`__
if you want to start new system extension documentation from scratch.