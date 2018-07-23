.. include:: Includes.txt
.. highlight:: rst

.. _basic-principles:

=======================================
Basic principles of TYPO3 documentation
=======================================


Introduction to TYPO3 documentation
===================================

For an excellent introduction, please see the 3 part series on Marcus
Schwemer's blog TYPO3 Worx:

* `GUIDE TO TYPO3 DOCUMENTATION – PART 1: THE USER-INTERFACE <https://typo3worx.eu/2017/01/guide-to-typo3-documentation-part-1-the-ui/>`__
* `GUIDE TO TYPO3 DOCUMENTATION – PART 2: CONTENT STRUCTURE <https://typo3worx.eu/2017/01/guide-to-typo3-documentation-content-structure/>`__
.. * `GUIDE TO TYPO3 DOCUMENTATION – PART 3: CONTRIBUTION AND REST HELPERS! <https://typo3worx.eu/2017/02/guide-to-typo3-documentation-part-3-contribute/>`__


.. important::

   Please note that the section "CONVERT REST TO “READABLE” FORMATS" in part 3 is
   slightly outdated. Currently, using the docker container for :ref:`rendering
   <rendering-docs>` is the recommended approach.

What's TYPO3 documentation?
==========================================

TYPO3 documentation may be one of the following:

* It can be one of the `official manuals <https://docs.typo3.org/>`__
  like :ref:`t3coreapi:start`.
  `system extension <https://docs.typo3.org/typo3cms/SystemExtensions/Index.html>`__.
* It can be the documentation of a
  `3rdparty extension <https://docs.typo3.org/typo3cms/extensions/Index.html>`__.
* TYPO3 documentation can also be a
  `Changelog <https://docs.typo3.org/typo3cms/extensions/core/latest/>`__
  entry for the core, for example a documented breaking change or new feature.

Common characteristics of TYPO3 documentation
=============================================

All of these examples have a few things in common:

* The documentation is rendered and found on https://docs.typo3.org
* The documentation has a **common theme**, all pages look similar and use the same styles
* Most of the documentation can be directly **edited by the community**. For third party
  extensions, this depends on where and how the source-code is hosted and maintained.
* The source of the documentation is written (mostly) in reStructuredText (**reST**)
* All documentation is rendered using the **same rendering toolchain**.
* The documentation source files adhere to :ref:`general-conventions` and
  share a **common structure** (e.g. all documentation files in a
  :file:`Documentation` subdirectory).
* Due to the conventions, the rendering of documentation can be automated and
  every documentation project only requires a minimum of setup.

Specific characteristics
========================


The things that are different for various kinds of documentation are:

* Where the source code is kept
* The workflow for making changes to the documentation


Overview
--------

.. t3-field-list-table::
 :header-rows: 1

 - :Type:         Type of documentation
   :Source:       Source Code (git repository)
   :Workflow:     Workflow for making changes

 - :Type:         Official `guides, tutorials <https://docs.typo3.org/typo3cms/GuidesAndTutorials/Index.html>`__,
                  `references <https://docs.typo3.org/typo3cms/References/Index.html>`__,
                  etc.
   :Source:       Github: `TYPO3-Documentation <https://github.com/TYPO3-Documentation>`__
   :Workflow:     Create Github Pull Request

 - :Type:         `TYPO3 Core Changelog <https://docs.typo3.org/typo3cms/extensions/core/latest/>`__
   :Source:       Inside TYPO3 source code: `git.typo3.org <git://git.typo3.org/Packages/TYPO3.CMS>`__,
                  `Github <https://github.com/TYPO3/TYPO3.CMS>`__ as mirror
   :Workflow:     Same as for Core development, see :ref:`Contribution Guide <t3contribute:Bugfixing-Adding-documentation>`

 - :Type:         `System extensions <https://docs.typo3.org/typo3cms/SystemExtensions/Index.html>`__
   :Source:       Same as for Changelog, inside TYPO3 source code: `git.typo3.org <git://git.typo3.org/Packages/TYPO3.CMS>`__,
                  `Github <https://github.com/TYPO3/TYPO3.CMS>`__ as mirror
   :Workflow:     Same as for Core development, see :ref:`Contribution Guide <t3contribute:start>`

 - :Type:         `3rdparty extensions <https://docs.typo3.org/typo3cms/extensions/Index.html>`__
   :Source:       it depends, see :ref:`contribute-to-3rdparty-extension`
   :Workflow:     it depends, see :ref:`contribute-to-3rdparty-extension`


Official TYPO3 manuals
----------------------

The official TYPO3 manuals are hosted on Github. Editing the documentation
requires a Github account and involves creating a Pull Request on Github.

Find out more about how to contribute: :ref:`docs-contribute`.

Documentation for the core
--------------------------

The documentation for the core (Changelog and system extensions) is added
to the TYPO3 source code. For this reason, the workflow of changing
something in the core documentation is very similar to adding a patch
to the core.

Find out more about the :ref:`Core contribution workflow <t3contribute:Start>`
in general.

Documentation for 3rdparty extensions
-------------------------------------

The documentation for a 3rdparty extension is maintained within the
source-code of this extensions. If and where it is edited depends
on where the extension is hosted and maintained.

To find out how to contribute documentation for a specific extension:
:ref:`contribute-to-3rdparty-extension`


