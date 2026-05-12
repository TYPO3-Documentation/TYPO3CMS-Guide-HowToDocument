..  include:: /Includes.rst.txt
..  _new-major-core-versions:

=================================================
Branching of the docs for a new major LTS version
=================================================

..  contents::

Create branches for the new LTS version in all versioned official repositories
==============================================================================

This includes all manuals in the "All Documentation" menu with version hints,
excluding the System extension manuals. The System extension manuals will
receive their new versions automatically via webhook in the release. This might
take a few days.

*   Create a new branch. `14.3` in this example.
*   Limit the composer.json to that version. For example `"typo3/cms-core": "^14.3"`
    instead of `"typo3/cms-core": "dev-main as 14.3"` and make sure `composer update`
    works.
*   Set the release and version to the new minor version, for example

    ..  code-block:: xml
        :caption: Documentation/guides.xml

        <project title="TYPO3 Explained"
                 release="14.3"
                 version="14.3"
                 copyright="since 2012 by the TYPO3 contributors"
        />

**After all the new LTS branches have been created and rendered** for all repositories,
revisit the guides.xml in all new LTS branches and raise to the preferred typo3 version:

..  code-block:: xml
    :caption: Documentation/guides.xml
    :emphasize-lines: 9

    <extension
        class="\T3Docs\Typo3DocsTheme\DependencyInjection\Typo3DocsThemeExtension"
        project-home="https://docs.typo3.org/m/typo3/reference-coreapi/main/en-us/"
        project-contact="https://typo3.slack.com/archives/C028JEPJL"
        project-repository="https://github.com/TYPO3-Documentation/TYPO3CMS-Reference-CoreApi"
        project-issues="https://github.com/TYPO3-Documentation/TYPO3CMS-Reference-CoreApi/issues"
        edit-on-github-branch="main"
        edit-on-github="TYPO3-Documentation/TYPO3CMS-Reference-CoreApi"
        typo3-core-preferred="14.3"
        interlink-shortcode="t3coreapi"
    />

We usually leave the `edit-on-github-branch` on main to avoid people making PRs
against the LTS branch and to avoid confusion in our backport workflows.

..  _new-major-core-versions-elts:

Add new eLTS warnings to the newly created eLTS version
=======================================================

Add a warning to the `Documentation/Includes.rst.txt` of the branch for the
new eLTS versions of all repositories:

..  code-block:: rst
    :caption: Documentation/Includes.rst.txt

    ..  You can put central messages to display on all pages here
    
    ..  attention::
        TYPO3 v12 has reached end-of-life as of April 30th 2026 and
        is no longer being maintained. Use the version switcher on the top
        left of this page to select documentation for a supported version of TYPO3.
    
        Need more time before upgrading?
        You can purchase Extended Long Term Support (ELTS) for TYPO3 v12 here:
        `TYPO3 ELTS <https://typo3.com/services/extended-support-elts>`__.

..  _new-major-core-versions-startpage:

Update the start page docs.typo3.org for a new major version
============================================================

*   Add the new major version to the main menu:
    https://github.com/TYPO3-Documentation/DocsTypo3Org-Homepage/blob/main/Documentation/_mainMenu.rst.txt
    Remove the versions that are now ELTS.
*   Add the new API version to the main menu
*   Require the latest LTS version in
    https://github.com/TYPO3-Documentation/DocsTypo3Org-Homepage/blob/main/composer.json

..  _new-major-core-versions-api:

Update api.typo3.org for a new major version
============================================

*  Add the new TYPO3 LTS version for rendering into
   https://github.com/TYPO3-Documentation/t3docs-ci-deploy/blob/main/.github/workflows/api-typo3-org.yml#L13
*  Add the new TYPO3 version to the sidebar of api.typo3.org:
   https://github.com/TYPO3-Documentation/render-guides/blob/main/packages/typo3-api/template/components/sidebar.html.twig#L9
*  Trigger rendering of the API by running the workflow above
*  Add the new version to the api.typo3.org start page: https://github.com/TYPO3-Documentation/DocsTypo3Org-Homepage/blob/main/WebRootResources-api.typo3.org/index.html
*  Add the new version to the main menu: http://github.com/TYPO3-Documentation/DocsTypo3Org-Homepage/blob/main/Documentation/_mainMenu.rst.txt

..  _new-major-core-versions-renderguides:

Set the "stable" version for links to the new LTS version in renderguides
=========================================================================

You should only do this after all versioned repositories exist in the new LTS
version and have been rendered; otherwise, rendering links will fail in all
manuals that are newly rendered. Then create a new renderguides release by
creating a tag for the version. See https://github.com/TYPO3-Documentation/render-guides/pull/1246
for an example.

..  _new-major-core-versions-search:

Make the new LTS version the preferred result in the docs search
================================================================

Require the newly created version of `t3docs/typo3-version-handling`
(created by the renderguides release in https://github.com/TYPO3-Documentation/t3docs-search-indexer)
and make a new release of the search.
