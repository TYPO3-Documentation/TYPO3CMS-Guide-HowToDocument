.. include:: ../Includes.txt

.. _faq-for-extension-authors:

=========================
FAQ for Extension Authors
=========================

Why does the documentation not provide a title?
===============================================

.. image:: ../images/missing-title.png
   :class: with-shadow

Refer to :ref:`migrate-necessary-steps` in order to fix this issue.
:ref:`settings-cfg` provides detail information.


How Do I Find My New Rendered Documentation?
============================================

**Answer:** Several possibilities:

#. Search for for extension on https://docs.typo3.org/Home/Extensions.html.
#. Or, create URL manually, see :ref:`migrate-url-structure`.
#. Or, rendering was done right now the URL will be referenced from https://intercept.typo3.com/admin/docs/deployments.
   The column **Branch** contains the link.

Is it Possible to Highjack Extension Documentation?
===================================================

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
===================================================================================

**Answer:** Yes and no. Regular users do not have this option at the moment. However,
as a member of the Documentation Team you can go to https://intercept.typo3.com
and log in with your typo3.org account. Then in the menu you can navigate to
:guilabel:`Documentation > Deployments`. At the top right hand side you will see a button
:guilabel:`Add Configuration`. By clicking this button and going through the form,
you can add a repository manually without the hook. Nevertheless we strongly
recommend the usage of the webhook.

Is Documentation Independant of TER?
====================================

Does the new workflow also mean that the documentation and the extension at
TER (https://extensions.typo3.org) are two separate, independent entities?

**Answer:** Yes. In theory you could have the documentation in GitHub (for example)
and the extension (code) somewhere else (or not in Git at all). You just
need to fire the webhook from GitHub/GitLab/Bitbucket to trigger the
documentation rendering.

.. _faq-can-i-use-a-readmerst-or-readmemd-instead:

Can I use a README.rst (or README.md) instead?
==============================================

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
