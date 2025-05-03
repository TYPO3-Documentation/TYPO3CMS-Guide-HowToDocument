:navigation-title: Document extensions

.. include:: /Includes.rst.txt
.. index:: Documentation; Extension
.. _writing-doc-for-ext-start:
.. _extension-documentation-files:
.. _write-doc-extensions-intro:

============================
How to document an extension
============================

This chapter explains how to write documentation for a new extension.

This guide uses the `example extension manual <https://github.com/TYPO3-Documentation/TYPO3CMS-Example-ExtensionManual>`__
as a template for starting out.

.. _write-doc-extensions-intro-rendering:

Rendering the documentation locally
===================================

Use the following Docker command to render your documentation guide locally:

..  include:: /_Includes/_LocalRendering.rst.txt

The :ref:`render-documentation-with-docker` has more information.

.. _how-to-start-docs-extension:

Use the init command to create the Documentation folder
=======================================================

The following Docker command helps you to create some basic documentation
including the required configuration file :file:`Documentation/guides.xml`:

..  include:: /_Includes/_InitCommand.rst.txt

The command creates a folder :path:`Documentation` in the directory it is called
from. This should be the root directory of your extension containing the
`composer.json <https://docs.typo3.org/permalink/t3coreapi:files-composer-json>`_.

Follow the interactive dialoge. We suggest to use the option ReStructuredText (rst)
as this format provides the full power of the TYPO3 documentation theme. Using
Markdown (md) is an option for simple and quick one page documentation.

If your extension offers a main `Site set <https://docs.typo3.org/permalink/t3coreapi:site-sets>`_
enter its name and path when prompted. This will regenerate ready to use
documentation about configuration for you. If you have more then one set you
can document the other sets manually. If you have no set, you need to write
the chapter your self.

Make changes and try :ref:`rendering <rendering-docs>` the new documentation.

To publish your documentation to https://docs.typo3.org
a :ref:`webhook needs to be added <webhook>` on GitHub, Bitbucket or GitLab.
A member of the Documentation Team has to approve your new documentation guide
for publishing. In case the Team has questions, please follow the thread
generated for your extension in the `TYPO3 slack organization <https://typo3.org/community/meet/chat-slack>`_
in channel `#typo3-documentation <https://typo3.slack.com/archives/C028JEPJL>`_.

Version numbers
===============

docs.typo3.org does no longer show three level version numbers in form of ``Major.Minor.Patch``.
Only the first two levels are shown ``Major.Minor``.

This reduces the amount of documentation while keeping relevant information,
as patch levels should not introduce breaking changes or new features.

.. index:: Rendering; Branches
.. _migrate-branches:
.. _supported-branches:

Supported branches
==================

The rendering supports two branches within repositories:

``main`` / ``master``
   Should contain the current development state, used for upcoming release.
   Every push to these branches triggers a new rendering, available at
   :samp:`https://docs.typo3.org/p/<vendor>/<package>/main/en-us/`.

   Both branch names are supported, but result in the same URL.
   Please use ``main``, ``master`` is only supported for backward compatibility.

``documentation-draft``
   Should contain a draft of the documentation.
   Every push to this branch triggers a new rendering, available at
   :samp:`https://docs.typo3.org/p/<vendor>/<package>/draft/en-us/`
   (same URL as main, except *main* is replaced by *draft*).


   This is not indexed by search engines. This branch can be used to test
   rendering before releasing a new version of an extension.

   In order to test a different rendering, remove the branch, and create it
   again.


.. toctree::
   :maxdepth: 1
   :hidden:

   Webhook
   ReregisterVersions
   FAQ
   ContributeToSystemExtension
   ContributeToThirdPartyExtension
