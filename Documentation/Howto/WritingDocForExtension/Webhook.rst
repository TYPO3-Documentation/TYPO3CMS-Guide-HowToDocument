.. include:: /Includes.rst.txt
.. index:: Webhooks
.. _webhook:

=======
Webhook
=======

This section explains how to configure webhooks for automatic documentation rendering in a repository.

TYPO3 documentation rendering supports Git as a Version Control System (VCS) and integrates with the following repository hosts:

-  :ref:`webhook-github`
-  :ref:`webhook-bitbucket-cloud` and Bitbucket self-hosted
-  :ref:`GitLab Cloud <webhook-gitlab>` and :ref:`GitLab self-hosted <webhook-gitlab>`

.. contents:: Table of Contents
   :local:

.. index:: Webhooks; Approval
.. _approval-intercept:

Approval
========

Before your documentation is rendered, the TYPO3 Documentation Team must approve the repository the first time you request rendering.

For approval, ensure the following:

#.  The extension must be published in the TYPO3 Extension Repository (TER) under the same extension key specified in :ref:`composer.json <t3coreapi:composer-json>`.
#.  The Git repository should be referenced on the TER detail view page.

These steps help prevent misuse of the infrastructure and ensure extension name consistency.

If the approval process takes too long, request approval via the Slack channel
`#typo3-documentation <https://typo3.slack.com/messages/C028JEPJL>`_. Register for Slack at `my.typo3.org <https://my.typo3.org/index.php?id=35>`__.

.. _foreign-setups:

Foreign setups
==============

If your repository is hosted outside the supported platforms (GitHub, GitLab, Bitbucket) or its structure differs from a typical TYPO3 extension, you must create a mirror on a supported platform. Otherwise, automatic rendering will not be possible.

.. _webhook-how-webhook-works:

How webhooks work
=================

If you are new to webhooks, refer to the `GitHub Webhooks Guide <https://developer.github.com/webhooks/>`_.

The webhook setup described below ensures that rendering is triggered only on push events.

To test the webhook integration, push changes to the `main` or `documentation-draft` branch (see :ref:`migrate-branches`).

.. note::

   Documentation rendering is triggered only for the version affected by the push event, not the entire repository. For example, a push event on branch `13.4` will render only that version.

.. _webhook-legacy:

Legacy webhook
==============

If a webhook was previously configured, it may be using a deprecated method. A compatibility layer is still in place but will be removed in the future.

.. index:: Webhooks; GitHub
.. _webhook-github:

GitHub
======

To enable automatic documentation rendering using GitHub webhooks, follow these steps:

.. rst-class:: bignums-xxl

#.  Navigate to the repositories **Settings** tab.

   .. figure:: /_Images/webhook/github/repository-start.png
      :width: 932

#. Open the **Webhooks** section.

   .. figure:: /_Images/webhook/github/settings-tab.png
      :width: 932

#. Click **Add webhook**.

   .. figure:: /_Images/webhook/github/webhook-section.png
      :width: 932

#. Configure the webhook settings:

    *   **Payload URL**: `https://docs-hook.typo3.org`
    *   **Content type**: `application/json`
    *   **SSL verification**: Enabled
    *   **Events**: `Just the push event`
    *   **Active**: Checked

   Click **Add webhook**.

   .. figure:: /_Images/webhook/github/webhook-add.png
      :width: 932

#. Verify webhook creation.

   GitHub will confirm that the webhook was successfully added.

   .. figure:: /_Images/webhook/github/webhook-added.png
      :width: 932

#. Test the webhook.

   Visit `intercept.typo3.com <https://intercept.typo3.com/admin/docs/deployments>`_ and check the **Recent actions** section. Push a commit to `main` or `documentation-draft` to trigger the webhook.

   .. figure:: /_Images/webhook/github/intercept-feedback.png
      :width: 932

.. index:: Webhooks; Bitbucket
.. _webhook-bitbucket-cloud:

Bitbucket Cloud
===============

To configure a webhook for a Bitbucket repository:

.. rst-class:: bignums-xxl

#. Open the repository **Settings**.

   .. figure:: /_Images/webhook/bitbucket/cloud/repository-start.png
      :width: 932

#. Go to the **Webhooks** section.

   .. figure:: /_Images/webhook/bitbucket/cloud/settings-tab.png
      :width: 932

#. Click **Add webhook**.

   .. figure:: /_Images/webhook/bitbucket/cloud/webhook-section.png
      :width: 932

#. Configure the webhook:

   - **Title**: `TYPO3 Docs`
   - **URL**: `https://docs-hook.typo3.org`
   - **Active**: Checked
   - **Triggers**: `Repository push`

   Click **Save**.

   .. figure:: /_Images/webhook/bitbucket/cloud/webhook-add.png
      :width: 932

#. Verify webhook creation.

   Bitbucket will confirm webhook addition.

   .. figure:: /_Images/webhook/bitbucket/cloud/webhook-added.png
      :width: 932

#. Test the webhook.

   Visit `intercept.typo3.com <https://intercept.typo3.com/admin/docs/deployments>`_ and check **Recent actions**. Push a commit to `main` or `documentation-draft` to trigger the webhook.

   .. figure:: /_Images/webhook/bitbucket/cloud/intercept-feedback.png
      :width: 932

.. index:: Webhooks; GitLab
.. _webhook-gitlab:

GitLab Cloud and Self-Hosted
============================

To set up a GitLab webhook:

.. rst-class:: bignums-xxl

#. Open the **Integrations** section of the repository.

   .. figure:: /_Images/webhook/gitlab/repository-start.png
      :width: 932

#. Add a webhook with the following settings:

   - **URL**: `https://docs-hook.typo3.org`
   - **Triggers**: `Push events` and `Tag push events`

   Click **Add webhook**.

   .. figure:: /_Images/webhook/gitlab/webhook-add.png
      :width: 932

#. Verify webhook creation.

   The webhook will appear in the list.

   .. figure:: /_Images/webhook/gitlab/webhook-added.png
      :width: 932

#. Test the webhook.

   Visit `intercept.typo3.com <https://intercept.typo3.com/admin/docs/deployments>`_ and check **Recent actions**. Push a commit to `main` or `documentation-draft` to trigger the webhook.

   .. figure:: /_Images/webhook/gitlab/intercept-feedback.png
      :width: 932

.. _webhook-testing:

Testing Webhooks
================

To test webhook configurations before integrating with TYPO3, use:

- `Beeceptor <https://beeceptor.com/>`_ for quick API testing.
- `Webhook.site <https://webhook.site/>`_ to inspect webhook payloads in real-time.

These tools help debug webhook calls and ensure correct configuration before enabling documentation rendering.
