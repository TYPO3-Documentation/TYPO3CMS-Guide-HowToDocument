.. include:: ../Includes.txt

.. _migrate:

=====================
Migrate Documentation
=====================

Since May 29th 2019 a new infrastructure is in place at docs.typo3.org. This
requires some migration tasks, in order to ensure that extension documentation
is rendered on docs.typo3.org

.. _migrate-necessary-steps:

Necessary Steps
===============

The necessary steps are:

.. rst-class:: bignums-xxl

#. Add mandatory :file:`composer.json`, see :ref:`composer-json`

   This file is necessary, in order to determine required information, like
   vendor, package name and supported TYPO3 version.

#. Add :file:`Documentation/Settings.cfg`, see :ref:`settings-cfg`

   If this file does not exist, your documentation will get rendered, but
   the title will not be displayed in the left sidebar.

   .. tip::

      We may drop this requirement in the future, but for now it is
      recommended to at least add a minimal :file:`Documentation/Settings.cfg`

      Example for (very) minimal Settings.cfg (for full example see :ref:`settings-cfg`):

      .. code-block:: none

         [general]

         project     = Extension name
         release     = latest



#. Add new webhook, see :ref:`webhook`

   The legacy webhook is no longer necessary, as explained in
   :ref:`webhook-legacy`.

#. Check if your documentation rendered

   You can got to `intercept <https://intercept.typo3.com/admin/docs/deployments>`__.

   In the overview you can see recently rendered documentation.

   Click on the link in the column :guilabel:`"Branch"` to go to the rendered documentation.

   .. image:: ../images/intercept2.png
      :class: with-shadow

   You can find the log by clicking on the link in the column :guilabel:`"Last rendered"`.

#. Request redirects

   Inform the TYPO3 Documentation Team, within `#typo3-documentation
   <https://typo3.slack.com/messages/C028JEPJL>`_ Slack channel (you must
   `register for Slack <https://my.typo3.org/index.php?id=35>`__ first).
   Alternatively, you can request a redirect by commenting in  
   `this GitHub issue <https://github.com/TYPO3-Documentation/T3DocTeam/issues/92>`__
   The team will setup the redirects from existing legacy rendering to current
   rendering:
   
   * legacy URL: `https://docs.typo3.org/typo3cms/extensions/<extkey>/<version>/`
   * new URL: `https://docs.typo3.org/p/<vendor>/<package>/<branch>/<locale>`

.. tip::

   Contact us on Slack (#typo3-documentation)
   if there are :ref:`problems you cannot fix yourself <migrate-common-errors>`.

.. _migrate-info-about-changes:

Info About Changes
==================

.. _migrate-extension-release:

Extension Release
-----------------

The TER (TYPO3 Extension Repository) will no longer trigger documentation
rendering. Therefore uploading an extension at extensions.typo3.org does not
automatically trigger rendering anymore.

In order to release a new version of an extension:

#. Publish the extension at https://extensions.typo3.org/

#. Add :ref:`webhook` (if not already done).

#. Tag the Git commit with a valid version.

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
   ``https://docs.typo3.org/p/<vendor>/<package>/draft/en-us/``
   (same URL as master, except *master* is replaced by *draft*).

   This is not indexed by search engines. This branch can be used to test
   rendering before releasing a new version of an extension.

   In order to test a different rendering, remove the branch, and create it
   again.

.. _migrate-existing-documentation:

Existing Documentation
----------------------

Existing legacy documentation is kept until end of 2020. Each documentation contains an
information block that it's outdated, together with a link to the necessary
steps.



In order to migrate, follow :ref:`migrate`. The Documentation Team can setup
redirects for old documentation to new documentation afterwards. Send a message
within `Slack <https://my.typo3.org/about-mytypo3org/slack>`_
`#typo3-documentation <https://typo3.slack.com/messages/C028JEPJL>`_.

.. _migrate-url-structure:

URL Structure
-------------

The URL structure has changed. Redirects are in place.

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


.. _migrate-known-problems:

Known Problems
==============

* Currently, the project cannot be rendered if the :ref:`start-file` is :file:`README.rst`
  (or .md) and not :file:`Documentation/Index.rst`. This is a
  `known problem <https://github.com/t3docs/docker-render-documentation/issues/31>`__
  and already fixed in
  the development version of our Docker container. We will update this on the
  server shortly. You can use the v2.1.0 version of the Docker container locally.
* A single-file solution (without toctree) may have problems with
  the menu. This is also a `known problem <https://github.com/t3docs/docker-render-documentation/issues/64>`__
  and already fixed in development version.

.. _migrate-common-errors:

Common Errors
=============

Here we show some common errors you can and should fix yourself.

Contact us on Slack, if you need help!

.. tip::

   We also made some changes to the
   `example extension manual <https://github.com/TYPO3-Documentation/TYPO3CMS-Example-ExtensionManual>`__.

   Make sure to use the updated version if you want to
   :ref:`start an extension from scratch <doc-for-ext-from-example>`!

Missing Title
-------------

.. image:: ../images/missing-title.png
   :class: with-shadow

**Solution:** :ref:`settings-cfg` should contain the title
(`project`) and release (`release`).

Example:

.. code-block:: none

   [general]

   project     = Your title
   release     = 2.0.0




FAQ for Extension Authors
=========================

How Do I Find My New Rendered Documentation?
--------------------------------------------

**Answer:** Several possibilities:

#. Search for your extension on https://docs.typo3.org/Home/Extensions.html
#. Or, construct the URL yourself from the rules above: `https://docs.typo3.org/p/<vendor>/<package>/<version>/<en-us>`
#. Or, if you just triggered rendering, look on https://intercept.typo3.com/admin/docs/deployments.
   The column **Branch** contains a link.


Is it Possible to Highjack Extension Documentation?
---------------------------------------------------

How do you make sure only the author of the extension publishes the documentation?

**Answer:**  Documentation rendering is restricted to one repository per package.

I.e. if someone triggers documentation rendering with a repository with vendor *myVendor* and
package *myPackage*, then nobody else will be able to trigger documentation from
a different repository with that exact vendor/package name combination. You
could say this works on a first come first served basis. However, if someone
with malicious intent registers a package first from a fake or wrong repository,
we will have to correct this by hand. The original author should in that case
notify us.

Is There a Way to Manually Trigger Docs Rendering Aside From a Git Repository Push?
-----------------------------------------------------------------------------------

**Answer:** Yes and no. Regular users do not have this option at the moment. However,
as a member of the Documentation Team you can go to https://intercept.typo3.com
and log in with your typo3.org account. Then in the menu you can navigate to
:guilabel:`Documentation > Deployments`. At the top right hand side you will see a button
:guilabel:`Add Configuration`. By clicking this button and going through the form,
you can add a repository manually without the hook. Nevertheless we strongly
recommend the usage of the webhook.

Is Documentation Independant of TER?
------------------------------------

Does the new workflow also mean that the documentation and the extension at
TER (https://extensions.typo3.org) are two separate, independent entities?

**Answer:** Yes. In theory you could have the documentation in GitHub (for example)
and the extension (code) somewhere else (or not in Git at all). You just
need to fire the webhook from GitHub/GitLab/Bitbucket to trigger the
documentation rendering.

Can I use a README.rst (or README.md) instead?
----------------------------------------------

GitHub (or Gitlab, bitbucket) etc. automatically render a :file:`README.rst` (or .md)
on the repository homepage.

For TYPO3 documentation I am required to have extra documentation in a :file:`Documentation`
folder. This means I have to maintain 2 documentations. Or not?


**Answer:** No. You have these 2 options:

#. Use a :file:`README.rst` (or .md) **and** a :file:`Documentation/Index.rst` (for example).
   This is done in our official manuals. The :file:`README.rst` is not used as documentation,
   it is used as an :ref:`about the repo file <about-file>`. The README is mostly
   used to direct users who come via GitHub (or Gitlab, Bitbucket etc.) to the rendered
   documentation on docs.typo3.org
#. Or, use :file:`README.rst` (or .md) as main documentation (:ref:`start-file`) and
   put everything in the :file:`README.rst`. The :file:`Documentation/Settings.cfg` file
   must also exist, but that is all that needs to be in the `Documentation`
   directory.

.. important::

   About using method 2) There are currently still :ref:`2 open issues <migrate-known-problems>`,
   but this is already resolved in a
   "development" version.

Actually, you have more options, but we do not want to make things too complicated.

Which one should you choose? That is up to you.

We recommend: Use method 1) for extensive documentation with several chapters,
use method 2) for minimal documentation which can be maintained in one file.

Further Questions?
==================

Get in touch with us, if you have problems, would like to ask questions or make suggestions.

Our `team page <https://typo3.org/community/teams/documentation/#c9886>`__ contains
information about how to contact us.

In most cases, the `Slack channel #typo3-documentation <https://typo3.slack.com/messages/C028JEPJL>`__
is the preferred method of communication (you must `register first <https://my.typo3.org/index.php?id=35>`__).



