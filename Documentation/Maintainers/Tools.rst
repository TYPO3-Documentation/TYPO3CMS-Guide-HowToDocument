.. include:: /Includes.rst.txt
.. highlight:: shell
.. index:: Changes; Backporting
.. _backport-changes:

=====================
Tools of the Doc Team
=====================

api.typo3.org
=============

Landing page
------------

The landing page of https://api.typo3.org is automatically updated when this
file is updated in GitHub:

https://github.com/TYPO3-Documentation/DocsTypo3Org-Homepage/blob/main/WebRootResources-api.typo3.org/index.html

As this is a pure HTML file, we currently keep the content in this page and
then update :file:`WebRootResources-api.typo3.org/index.html` with the
rendered output.

The workflow responsible for replacing the landing page is
https://github.com/TYPO3-Documentation/DocsTypo3Org-Homepage/blob/main/.github/workflows/apihome.yml

Generated API per version
-------------------------

The content per version https://api.typo3.org/main, https://api.typo3.org/12.4
etc is generated with Doxygen. A Doxygen Docker image is maintained by the
TYPO3 GmbH in this repository:
https://github.com/TYPO3GmbH/doxygenapi

The rendering is triggered by this workflow which we in the documentation team
can change:
https://github.com/TYPO3-Documentation/t3docs-ci-deploy/blob/main/.github/workflows/api-typo3-org.yml

..  attention::
    This workflow is running automatically for max 60 days then it has to be
    restarted manually
