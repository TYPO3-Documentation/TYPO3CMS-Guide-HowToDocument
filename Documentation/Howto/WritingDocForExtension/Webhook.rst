..  include:: /Includes.rst.txt
..  index:: Webhooks
..  _webhook:

=======
Webhook
=======

This section explains how to configure webhooks for automatic documentation
rendering in a repository.

TYPO3 documentation rendering supports Git as a Version Control System (VCS)
and integrates with the following repository hosts:

*   :ref:`GitHub <webhook-github>`
*   :ref:`Bitbucket Cloud <webhook-bitbucket-cloud>` and Bitbucket self-hosted
*   :ref:`GitLab Cloud <webhook-gitlab>` and :ref:`GitLab self-hosted <webhook-gitlab>`
*   `Forgejo and Gitea <https://docs.typo3.org/permalink/h2document:webhook-forgejo>`_,
    including self-hosted instances

..  contents:: Table of Contents
    :local:

..  index:: Webhooks; Approval
..  _approval-intercept:

Approval
========

Before your documentation is rendered, the TYPO3 Documentation Team must approve
the repository the first time you request rendering.

For approval, ensure the following:

#.  The extension must be published in the TYPO3 Extension Repository (TER)
    under the same extension key specified
    in :ref:`composer.json <t3coreapi:composer-json>`.
#.  The Git repository should be referenced on the TER detail view page.

These steps help prevent misuse of the infrastructure and ensure extension
name consistency.

If the approval process takes too long, request approval via the Slack channel
`#typo3-documentation <https://typo3.slack.com/messages/C028JEPJL>`_. Register
for Slack at `my.typo3.org <https://my.typo3.org/index.php?id=35>`__.

..  _foreign-setups:

Foreign setups
==============

If your repository host is not in the list above, create a mirror on a
supported repository host. Also create a mirror if the structure of your
repository is different from a typical TYPO3 extension. Without a mirror, the
automatic rendering cannot start.

A self-hosted instance of a supported repository host can use any domain. The
Documentation Team approves the domain of your instance one time, together
with the repository approval described above.

..  _webhook-how-webhook-works:

How webhooks work
=================

If you are new to webhooks, refer to
the `GitHub Webhooks Guide <https://developer.github.com/webhooks/>`_.

The webhook setup described below ensures that rendering is triggered only on
push events.

To test the webhook integration, push changes to
the `main` or `documentation-draft` branch (see :ref:`supported branches <migrate-branches>`).

..  note::

    Documentation rendering is triggered only for the version affected by the
    push event, not the entire repository. For example, a push event on
    branch `13.4` will render only that version.

..  _webhook-legacy:

Legacy webhook
==============

If a webhook was previously configured, it may be using a deprecated method.
A compatibility layer is still in place but will be removed in the future.

..  index:: Webhooks; GitHub
..  _webhook-github:

GitHub
======

To enable automatic documentation rendering using GitHub webhooks, follow
these steps:

..  rst-class:: bignums-xxl

#.  Navigate to the :guilabel:`Settings` tab of the repository.

    ..  figure:: /_Images/webhook/github/repository-start.png
        :width: 932

#.  Open the **Webhooks** section.

    ..  figure:: /_Images/webhook/github/settings-tab.png
        :width: 932

#.  Click **Add webhook**.

    ..  figure:: /_Images/webhook/github/webhook-section.png
        :width: 932

#.  Configure the webhook settings:

    *   **Payload URL**: `https://docs-hook.typo3.org`
    *   **Content type**: `application/json`
    *   **SSL verification**: Enabled
    *   **Events**: `Just the push event`
    *   **Active**: Checked

    Click **Add webhook**.

    ..  figure:: /_Images/webhook/github/webhook-add.png
        :width: 932

#.  Verify webhook creation.

    GitHub will confirm that the webhook was successfully added.

    ..  figure:: /_Images/webhook/github/webhook-added.png
        :width: 932

#.  Test the webhook.

    Visit `intercept.typo3.com <https://intercept.typo3.com/admin/docs/deployments>`_
    and check the **Recent actions** section. Push a commit
    to `main` or `documentation-draft` to trigger the webhook.

    ..  figure:: /_Images/webhook/github/intercept-feedback.png
        :width: 932

..  index:: Webhooks; Bitbucket
..  _webhook-bitbucket-cloud:

Bitbucket cloud
===============

To configure a webhook for a Bitbucket repository:

..  rst-class:: bignums-xxl

#.  Open the repository **Settings**.

    ..  figure:: /_Images/webhook/bitbucket/cloud/repository-start.png
        :width: 932

#.  Go to the **Webhooks** section.

    ..  figure:: /_Images/webhook/bitbucket/cloud/settings-tab.png
        :width: 932

#.  Click **Add webhook**.

    ..  figure:: /_Images/webhook/bitbucket/cloud/webhook-section.png
        :width: 932

#.  Configure the webhook:

    *   **Title**: `TYPO3 Docs`
    *   **URL**: `https://docs-hook.typo3.org`
    *   **Active**: Checked
    *   **Triggers**: `Repository push`

    Click **Save**.

    ..  figure:: /_Images/webhook/bitbucket/cloud/webhook-add.png
        :width: 932

#.  Verify webhook creation.

    Bitbucket will confirm webhook addition.

    ..  figure:: /_Images/webhook/bitbucket/cloud/webhook-added.png
        :width: 932

#.  Test the webhook.

    Visit `intercept.typo3.com <https://intercept.typo3.com/admin/docs/deployments>`_
    and check **Recent actions**. Push a commit
    to `main` or `documentation-draft` to trigger the webhook.

    ..  figure:: /_Images/webhook/bitbucket/cloud/intercept-feedback.png
        :width: 932

..  index:: Webhooks; GitLab
..  _webhook-gitlab:

GitLab cloud and Self-Hosted
============================

To set up a GitLab webhook:

..  rst-class:: bignums-xxl

#.  Open the **Integrations** section of the repository.

    ..  figure:: /_Images/webhook/gitlab/repository-start.png
        :width: 932

#.  Add a webhook with the following settings:

    *   **URL**: `https://docs-hook.typo3.org`
    *   **Triggers**: `Push events` and `Tag push events`

    Click **Add webhook**.

    ..  figure:: /_Images/webhook/gitlab/webhook-add.png
        :width: 932

#.  Verify webhook creation.

    The webhook will appear in the list.

    ..  figure:: /_Images/webhook/gitlab/webhook-added.png
        :width: 932

#.  Test the webhook.

    Visit `intercept.typo3.com <https://intercept.typo3.com/admin/docs/deployments>`_
    and check **Recent actions**. Push a commit
    to `main` or `documentation-draft` to trigger the webhook.

    ..  figure:: /_Images/webhook/gitlab/intercept-feedback.png
        :width: 932

..  index:: Webhooks; Forgejo
..  _webhook-forgejo:

Forgejo and Gitea
=================

Forgejo and Gitea instances can use any domain, so a self-hosted instance does
not need a mirror. To set up the webhook:

..  rst-class:: bignums-xxl

#.  Open the repository **Settings**. Go to the **Webhooks** section.

#.  Click **Add Webhook**. Select **Forgejo**, or **Gitea** on a Gitea
    instance.

#.  Configure the webhook:

    *   **Target URL**: `https://docs-hook.typo3.org`
    *   **HTTP Method**: `POST`
    *   **POST Content Type**: `application/json`
    *   **Trigger On**: `Custom Events`, with **Push** selected

    Keep the default value of the branch filter. With this value, the
    webhook sends an event for each push to a branch or a tag. The branches
    include `documentation-draft` and version branches such as `13.4`.

    Select only the push event. The endpoint rejects other events, for
    example the creation or deletion of a branch. These rejected deliveries
    then fill the delivery history of your webhook.

    Click **Add Webhook**.

#.  Test the webhook.

    Push a commit to `main` or `documentation-draft` that changes
    `README.rst`, `README.md`, or a file in :file:`Documentation/`. Then
    open `intercept.typo3.com <https://intercept.typo3.com/admin/docs/deployments>`_.
    Look at the **Recent actions** section.

    ..  note::
        The **Test Delivery** button of Forgejo and the **Test Push Event**
        button of Gitea send a push event without changed files. Forgejo or
        Gitea shows this delivery as successful, but the rendering does not
        start. Only a push with changes to the documentation starts the
        rendering.

..  _webhook-deliveries:

Reading the webhook deliveries on GitHub
========================================

In the GitHub repository settings under :guilabel:`Webhooks > Recent
Deliveries` every delivery shows the response of the documentation server:

*   `200`: ping accepted.
*   `204`: push accepted, a rendering was triggered.
*   `412`: repository not approved yet — expected for the first test
    delivery before the Documentation Team has approved the project.

A branch push and a tag push are separate deliveries. When a new version does
not appear on docs.typo3.org, check the delivery of the **tag** push — the
branch push having succeeded says nothing about the tag. GitLab and Bitbucket
show the corresponding information in their webhook edit views.

..  _webhook-testing:

Testing webhooks
================

To test webhook configurations before integrating with TYPO3, use:

*   `Beeceptor <https://beeceptor.com/>`_ for quick API testing.
*   `Webhook.site <https://webhook.site/>`_ to inspect webhook payloads in real-time.

These tools help debug webhook calls and ensure correct configuration before enabling documentation rendering.
