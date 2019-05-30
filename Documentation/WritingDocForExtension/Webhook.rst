.. include:: ../Includes.txt

.. _webhook:

=======
Webhook
=======

This section describes how to add webhooks for auto rendering to a repository.

The system currently supports the following git systems:

  - GitHub
  - Bitbucket (cloud)
  - GitLab (cloud and self-hosted)

The following chapters provide illustrated walkthrough tutorials on how to add the necessary hook in those systems.

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

   #. Enable "Activate".

   #. Click on "Add webhook"

   .. figure:: /images/webhook/github/webhook-add.png
      :width: 932

#. Webhook was added

   GitHub should show a notice that creation of webhook was successful.

   .. figure:: /images/webhook/github/webhook-added.png
      :width: 932

#. (Optional) visit intercept and check request

   If curious, visit https://intercept.typo3.com/admin/docs/deployments and
   check "Recent actions" (scroll down). The repository should have created a
   "Docs hook ping from github repository".

   .. figure:: /images/webhook/github/intercept-feedback.png
      :width: 932



Bitbucket
=========

Add auto rendering for a repository via Bitbucket webhook in two steps:

.. rst-class:: bignums-xxl

#. Go to "Settings" and "Webhooks" section within the repository

   .. figure:: /images/webhook/bitbucket/bitbucket-settings-webhooks.jpg
      :width: 740

#. Click the "Add webhook" button

#. Fill in webhook configuration

   #. Choose a title for this hook: e.g. "TYPO3 Docs".

   #. Fill URL fields with ``https://docs-hook.typo3.org``.

   #. Click on "Save"
   
   .. figure:: /images/webhook/bitbucket/bitbucket-add-webhook.jpg
      :width: 570
