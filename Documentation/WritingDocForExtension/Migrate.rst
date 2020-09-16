.. include:: ../Includes.txt

.. _migrate:
.. _register-for-rendering:

===========================
Register for docs.typo3.org
===========================

Follow the :ref:`register-necessary-steps` in order to have extension
documentation rendered on docs.typo3.org out of the box.
When migrating existing documentation, :ref:`migrate-info-about-changes` might be interesting as well.

.. contents:: Table of Contents
   :local:

.. _migrate-necessary-steps:
.. _register-necessary-steps:

Necessary Steps
===============

Walk through the following steps in defined order. Proceed with next step only
if the previous step was successful.

.. rst-class:: bignums-xxl

#. Add mandatory :file:`composer.json`, see :ref:`composer-json`

   This file is necessary, in order to determine required information, like
   vendor, package name and supported TYPO3 version.

#. Add :file:`Documentation/Settings.cfg`, see :ref:`settings-cfg`

   If this file does not exist, documentation will get rendered, but title will
   not be displayed in the left sidebar.

   This requirement may be dropped in the future.For now it is necessary to at
   least add a minimal :file:`Documentation/Settings.cfg`.

   Example for very minimal Settings.cfg, for full example see
   :ref:`settings-cfg`:

   .. code-block:: cfg

      [general]

      project = Extension name

#. Add new webhook, see :ref:`webhook`

   The legacy webhook is no longer necessary, as explained in
   :ref:`webhook-legacy`. Instead the new webhook has to be added as described
   at :ref:`webhook`.

   In case the old hook is in play, remove it first, and add the new one
   instead.

#. Trigger webhook for released versions,
   see :ref:`reregister-versions` (optional)

   In case documentation for already released versions should be rendered again,
   follow :ref:`reregister-versions`.

   It will explain how the process of rendering
   can be triggered once more for already released versions.

#. Request redirects (optional)

   This step adds work load to a small team.
   Please check whether there is a need to request redirects.

   Inform the TYPO3 Documentation Team, within `#typo3-documentation
   <https://typo3.slack.com/messages/C028JEPJL>`_ Slack channel. Registration
   for Slack is available at `my.typo3.org
   <https://my.typo3.org/index.php?id=35>`__.
   Alternatively, a redirect can be requested by commenting in `this GitHub
   issue <https://github.com/TYPO3-Documentation/T3DocTeam/issues/92>`__.

   The team will setup the redirects from existing legacy rendering to current
   rendering:

   * legacy URL: `https://docs.typo3.org/typo3cms/extensions/<extkey>/<version>/`
   * new URL: `https://docs.typo3.org/p/<vendor>/<package>/<branch>/<locale>`

All future versions will now be rendered, see :ref:`workflow-extension-release`.
Also some branches will be rendered, see :ref:`supported-branches`.

.. _migrate-extension-release:
.. _workflow-extension-release:

Workflow of Extension Release
=============================

For full information about publishing extensions check :ref:`t3coreapi:publish-extension`.

The following steps only describe what's necessary to publish documentation to show up on extensions.typo3.org:

#. Add :ref:`webhook` (if not already done).

#. Tag the Git commit with a valid version: :ref:`supported-version-numbers`.

#. Push (publish) the Git tag.

Publishing a tag will trigger rendering of documentation for that tag.
The result will be published on docs.typo3.org.
Furthermore a JSON file will provide info about the new available documentation.

This file is used by extensions.typo3.org to find matching documentation.
extensions.typo3.org will only provide a link for latest available version.
This has to match the released version on docs.typo3.org.
No fallback is in place (e.g. master will not be linked by default).

Please note that it might take some time until extensions.typo3.org displays changed URLs to docs.typo3.org.
The information needs to be picked up by a command.
Caches for detail page need to be invalidated, and SOLR index needs to be updated.

.. _migrate-version-numbers:
.. _supported-version-numbers:

Version Numbers
===============

docs.typo3.org does no longer show three level version numbers in form of ``Major.Minor.Patch``.
Only the first two levels are shown ``Major.Minor``.

This reduces the amount of documentation while keeping relevant information,
as patch levels should not introduce breaking changes or new features.

.. _migrate-branches:
.. _supported-branches:

Supported Branches
==================

The rendering supports two branches within repositories:

``master``
   Should contain the current development state, used for upcoming release.
   Every push to this branch triggers a new rendering, available at
   ``https://docs.typo3.org/p/<vendor>/<package>/master/en-us/``.

``documentation-draft``
   Should contain a draft of the documentation.
   Every push to this branch triggers a new rendering, available at
   ``https://docs.typo3.org/p/<vendor>/<package>/draft/en-us/``
   (same URL as master, except *master* is replaced by *draft*).

   This is not indexed by search engines. This branch can be used to test
   rendering before releasing a new version of an extension.

   In order to test a different rendering, remove the branch, and create it
   again.

.. _migrate-url-structure:
.. _url-structure:

URL Structure
=============

The URL structure now consists of the following parts:

`https://docs.typo3.org/<type>/<vendor>/<package>/<version>/<locale>`

Example: https://docs.typo3.org/p/helhum/typo3-console/master/en-us/

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
   Collects all packages of the same vendor, e.g. "typo3" or a company
   providing extensions. Same as on packagist.org.

``package``
   Defines the package. Same as on packagist.org.

``version``
   Defines the version, either in form of "Major.Minor" or ``master`` or
   ``draft``.

``locale``
   Defines the locale, e.g. ``en-us`` or ``fr-fr``.

.. _migrate-info-about-changes:
.. _migrate-existing-documentation:

Info About Changes
==================

Since May 29th 2019 a new infrastructure is in place at docs.typo3.org.
This requires some migration tasks, in order to ensure that extension documentation
is rendered on docs.typo3.org.

Existing legacy documentation is kept until end of 2020.
Each documentation contains an information block that it's outdated,
together with a link to the necessary steps.

In order to migrate, follow :ref:`migrate-necessary-steps`.
