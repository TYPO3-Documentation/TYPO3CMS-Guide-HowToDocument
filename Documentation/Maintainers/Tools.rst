..  include:: /Includes.rst.txt
..  index:: Changes; Backporting
..  _tools-of-the-documentation-team:

===============================
Tools of the Documentation Team
===============================

..  contents:: Table of contents

..  _tools-of-the-documentation-team-search-indexer:

Search indexer
==============

The search indexer code can be found in repository
https://github.com/TYPO3-Documentation/t3docs-search-indexer

It can be deployed by running
https://github.com/TYPO3-Documentation/t3docs-search-indexer/blob/main/.github/workflows/docs-search.yml

A general reindexing can only be triggered by employees of the TYPO3 GmbH at the
time of writing.

Preferred TYPO3 versions can be updated by requiring a new version of
`t3docs/typo3-version-handling` via composer.

The assets for the search result page can be updated by setting the latest
renderguides version in https://github.com/TYPO3-Documentation/t3docs-search-indexer/blob/main/config/services.yaml#L19
ff.

..  _tools-of-the-documentation-team-api:

api.typo3.org
=============

..  _tools-of-the-documentation-team-api-landing:

Landing page
------------

The landing page of https://api.typo3.org/ is automatically updated when this
file is updated in GitHub:

https://github.com/TYPO3-Documentation/DocsTypo3Org-Homepage/blob/main/WebRootResources-api.typo3.org/index.html

As this is a pure HTML file, we currently keep the content in this rst file:
https://github.com/TYPO3-Documentation/DocsTypo3Org-Homepage/blob/main/Documentation/Home/ApiTypo3Org.rst
locally render it,
then update :file:`WebRootResources-api.typo3.org/index.html` with the
rendered output.

The workflow responsible for replacing the landing page is
https://github.com/TYPO3-Documentation/DocsTypo3Org-Homepage/blob/main/.github/workflows/apihome.yml

..  _tools-of-the-documentation-team-api-landing-generation:

Generated API per version
-------------------------

The content per version https://api.typo3.org/main, https://api.typo3.org/12.4
etc is generated with phpDocumentor. The theme is defined in this repository:
https://github.com/TYPO3-Documentation/render-guides/tree/main/packages/typo3-api

The rendering is triggered by this workflow which we in the documentation team
can change:
https://github.com/TYPO3-Documentation/t3docs-ci-deploy/blob/main/.github/workflows/api-typo3-org.yml

..  attention::
    This workflow is running automatically for max 60 days then it has to be
    restarted manually
