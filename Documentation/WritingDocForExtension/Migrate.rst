.. include:: ../Includes.txt

.. _migrate:

=====================
Migrate documentation
=====================

Since May 29th 2019 a new infrastructure is in place at docs.typo3.org. This
requires some migration tasks, in order to keep extension documentation
rendering at docs.typo3.org

.. _migrate-necessary-steps:

Necessary steps
===============

The following section will explain all two necessary steps.

.. rst-class:: bignums-xxl

#. Add necessary :file:`composer.json`, see :ref:`composer-json`

   This file is necessary, in order to determine mandatory information, like
   vendor, package name and supported TYPO3 version.

#. Add new webhook, see :ref:`webhook`

   The legacy webhook is no longer necessary, as explained at
   :ref:`webhook-legacy`.

.. _migrate-info-about-changes:

Info about changes
==================

.. _migrate-extension-release:

Extension release
-----------------

The TER (TYPO3 Extension Repository) will no longer trigger documentation
rendering. Therefore uploading an extension at extensions.typo3.org does not
trigger rendering anymore.

In order to release a new version of an extension:

#. Publish the extension at https://extensions.typo3.org/

#. Add :ref:`webhook` (if not already done).

#. Tag the Git commit with an valid version.

#. Publish the extension at https://packagist.org/ (This is done by Webhook +
   Tagging)

.. _migrate-version-numbers:

Version Numbers
---------------

There is no change necessary. https://docs.typo3.org/ does no longer show three
level version numbers in form of ``Major.Minor.Patch``. Only the first two
levels are shown ``Major.Minor``.

This reduces the amount of documentation while keeping relevant information, as
patch levels should not introduce breaking changes or new features.

.. _migrate-branches:

Supported branches
------------------

The rendering supports two branches within repositories:

``master``
   Should contain the current development state, used for upcoming release.
   Every push to this branch triggers a new rendering, available at
   ``https://docs.typo3.org/p/<vendor>/<package>/master/en-us/``.

``documentation-draft``
   Should contain a draft of the documentation.
   Every push to this branch triggers a new rendering, available at
   ``https://docs.typo3.org/p/<vendor>/<package>/draft/en-us/``.

   This state is not indexed by search engines. This branch can be used to test
   rendering before releasing a new version of an extension.

   In order to test a different rendering, remove the branch, and create it
   again.

.. _migrate-existing-documentation:

Existing Documentation
----------------------

Existing Documentation is kept until end of 2020. Each documentation contains an
information block that it's outdated, together with an link to the necessary
steps.

In order to migrate, follow :ref:`migrate`. The Documentation team can setup
redirects for old documentation to new documentation afterwards. Send an message
within `Slack <https://my.typo3.org/about-mytypo3org/slack>`_
`#typo3-documentation <https://typo3.slack.com/messages/C028JEPJL>`_.

.. _migrate-url-structure:

URL structure
-------------

The URL structure has changed. Redirects are in place.

The URL structure now consists of the following parts:

``type``
   One of:

   ``p``
      Provides documentation for composer packages (TYPO3 third party extensions)

   ``c``
      Provides documentation for TYPO3 core extensions.

   ``m``
      Provides official manuals (guides, tutorials, references).

   ``h``
      Provides the homepage of docs.typo3.org

   ``other``
      Provides further documentation, e.g. for `Surf
      <https://github.com/TYPO3/Surf>`_ or `Fluid
      <https://github.com/TYPO3/Fluid>`_

``vendor``
   Collects all packages of the same vendor, e.g. "typo3" or an company
   providing extensions. Same as on packagist.org.

``package``
   Defines the package. Same as on packagist.org.

``version``
   Defines the concrete version, either in form of "Major.Minor" or ``master`` or
   ``draft``.

``locale``
   Defines the locale, e.g. ``en-us`` or ``fr-fr``.
