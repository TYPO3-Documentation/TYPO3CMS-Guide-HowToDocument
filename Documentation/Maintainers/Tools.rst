.. include:: /Includes.rst.txt
.. index:: Changes; Backporting
.. _tools_of_the_documentation_team:

===============================
Tools of the Documentation Team
===============================

api.typo3.org
=============

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

Rendering the API locally
-------------------------

..  code-block: bash

    git clone git@github.com:TYPO3-Documentation/render-guides.git
    cd render-guides
    make clone-typo3 # puts TYPO3 core into .Build/TYPO3
    make api-docs # puts result into .phpdoc/build
