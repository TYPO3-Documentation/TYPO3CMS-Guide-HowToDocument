.. include:: ../Includes.txt

.. _webhook:

=======
Webhook
=======

This section describes how to add webhooks for auto rendering to a repository.

The system supports Git as VCS (Version Control System),
and the following hosters:

- :ref:`webhook-github`
- :ref:`webhook-bitbucket-cloud` and Bitbucket self-hosted
- :ref:`GitLab Cloud <webhook-gitlab>` and :ref:`GitLab self-hosted <webhook-gitlab>`

.. contents:: Table of Contents
   :local:

.. _approval-intercept:

Approval
========

In order to render documentation, the TYPO3 Documentation Team needs to approve
each new extension when requesting rendering for the first time.

In order to approve an extension, the following things need to apply:

#. The extension needs to be published in TER under the same extension key as
   claimed by :ref:`composer.json <composer-json>`.

#. The Git Repository is referenced from TER detail view page.

This is necessary to prevent misuse of the infrastructure and extension names.

In case the approval takes to long,
request the approval within the Slack channel
`#typo3-documentation <https://typo3.slack.com/messages/C028JEPJL>`_.
Registration for Slack is available at `my.typo3.org
<https://my.typo3.org/index.php?id=35>`__.

.. _foreign-setups:

Foreign setups
==============

In some cases one might use a different hoster then mentioned above.
Or the file structure does not match the structure of an TYPO3 extension.

In such cases a mirror to one of the supported hosters must be setup.
Otherwise it is not possible to enable documentation rendering on docs.typo3.org.

.. _webhook-how-webhook-works:

How Webhooks Work
=================

If it's your first time working with webhooks, take a look at `GitHub developer
<https://developer.github.com/webhooks/>`_. The configuration below triggers
rendering only on push events.

In order to test the integration, a push to `master` branch or
`documentation-draft` branch can be used, see :ref:`migrate-branches`.

.. note::

   Documentation rendering is only triggered for versions affected by push event.
   Not the whole repository will be rendered each time.
   If a push event for branch 7.8 is triggered, only this version will be rendered.

.. _webhook-legacy:

Legacy Webhook
==============

If the repository already had a hook, this is considered deprecated. A
compatibility layer is still in place, but will be removed in the future.

.. _webhook-github:

GitHub
======

Add auto rendering for a repository via GitHub webhook in five steps:

.. rst-class:: bignums-xxl

#. Go to "Settings" tab within the repository

   .. figure:: /images/webhook/github/repository-start.png
      :width: 932

#. Go to "Webhooks" section within the repository settings

   .. figure:: /images/webhook/github/settings-tab.png
      :width: 932

#. Add webhook

   .. figure:: /images/webhook/github/webhook-section.png
      :width: 932

#. Fill in webhook configuration

   #. Configure URL ``https://docs-hook.typo3.org`` for field "Payload URL".

   #. Select ``application/json`` as "Content type".

   #. Enable "SSL verification".

   #. Select ``Just the push event.`` for "Which events would you like to trigger this webhook?".

   #. Enable "Active".

   #. Click on "Add webhook"

   .. figure:: /images/webhook/github/webhook-add.png
      :width: 932

#. Webhook was added

   GitHub should show a notice that creation of webhook was successful.

   .. figure:: /images/webhook/github/webhook-added.png
      :width: 932

#. Trigger webhook and visit to check request

   Visit `intercept.typo3.com <https://intercept.typo3.com/admin/docs/deployments>`_ and
   check "Recent actions" (scroll down). The repository should have created a
   "Docs hook ping from github repository".

   For the documentation to be rendered, the hook needs to be triggered: Either push to the
   branch ``master``. Or push to a new branch ``documentation-draft``.

   .. figure:: /images/webhook/github/intercept-feedback.png
      :width: 932


.. _webhook-bitbucket-cloud:

Bitbucket Cloud
===============

Add auto rendering for a repository via Bitbucket webhook in five steps:

.. rst-class:: bignums-xxl

#. Go to "Settings" section within the repository

   .. figure:: /images/webhook/bitbucket/cloud/repository-start.png
      :width: 932

#. Go to "Webhooks" section within the repository settings

   .. figure:: /images/webhook/bitbucket/cloud/settings-tab.png
      :width: 932

#. Add webhook

   .. figure:: /images/webhook/bitbucket/cloud/webhook-section.png
      :width: 932

#. Fill in webhook configuration

   #. Choose a title for this hook: e.g. "TYPO3 Docs".

   #. Fill URL field with ``https://docs-hook.typo3.org``.

   #. Enable "Active" Status.

   #. Select ``Repository push`` for "Triggers".

   #. Click on "Save"

   .. figure:: /images/webhook/bitbucket/cloud/webhook-add.png
      :width: 932

#. Webhook was added

   Bitbucket should show a notice, which disappears after some seconds, that
   creation of webhook was successful. Also the webhook should be shown in the
   list.

   .. figure:: /images/webhook/bitbucket/cloud/webhook-added.png
      :width: 932

#. Trigger webhook and visit to check request

   Visit `intercept.typo3.com <https://intercept.typo3.com/admin/docs/deployments>`_ and
   check "Recent actions" (scroll down).

   For the documentation to be rendered, the hook needs to be triggered: Either push to the
   branch ``master``. Or push to a new branch ``documentation-draft``.

   .. figure:: /images/webhook/bitbucket/cloud/intercept-feedback.png
      :width: 932

.. _webhook-gitlab:

GitLab Cloud and GitLab Self-hosted
===================================

Add auto rendering for a repository via GitLab webhook in four steps:

.. rst-class:: bignums-xxl

#. Go to "Integrations" section within the repository

   .. figure:: /images/webhook/gitlab/repository-start.png
      :width: 932

#. Add webhook by filling in webhook configuration

   #. Fill URL field with ``https://docs-hook.typo3.org``.

   #. Select ``Push events`` and ``Tag push events`` for "Trigger".

   #. Click on "Add webhook"

   .. figure:: /images/webhook/gitlab/webhook-add.png
      :width: 932

#. Webhook was added

   The webhook should be shown in the list (scroll down).

   .. figure:: /images/webhook/gitlab/webhook-added.png
      :width: 932

#. Trigger webhook and visit to check request

   Visit `intercept.typo3.com <https://intercept.typo3.com/admin/docs/deployments>`_ and
   check "Recent actions" (scroll down).

   For the documentation to be rendered, the hook needs to be triggered: Either push to the
   branch ``master``. Or push to a new branch ``documentation-draft``.

   .. figure:: /images/webhook/gitlab/intercept-feedback.png
      :width: 932
