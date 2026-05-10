..  include:: /Includes.rst.txt
..  _new-major-core-versions:

==================================
New major Core version is released
==================================

..  content::


..  _new-major-core-versions-api:

Update api.typo3.org for a new major version
============================================

*  Add the new TYPO3 LTS version for rendering into 
   https://github.com/TYPO3-Documentation/t3docs-ci-deploy/blob/main/.github/workflows/api-typo3-org.yml#L13
*  Add the new TYPO3 Version to the sidebar of api.typo3.org: 
   https://github.com/TYPO3-Documentation/render-guides/blob/main/packages/typo3-api/template/components/sidebar.html.twig#L9
*  Trigger rendering of the api, by triggering above workflow
*  Add the new version to the api.typo3.org startpage: https://github.com/TYPO3-Documentation/DocsTypo3Org-Homepage/blob/main/WebRootResources-api.typo3.org/index.html
*  Add the new Version to the main Menu: http://github.com/TYPO3-Documentation/DocsTypo3Org-Homepage/blob/main/Documentation/_mainMenu.rst.txt
