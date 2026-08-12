:navigation-title: Redirects

..  include:: /Includes.rst.txt
..  index:: ! Redirects; Renaming pages; Deleting pages
..  _redirects:

====================================
Redirecting renamed or deleted pages
====================================

Each `.rst` file published to docs.typo3.org is a page with its own URL.
Unlike an anchor within a page (see :ref:`link anchors <link-anchor>`),
there is no in-repo mechanism to keep an old file's URL working after it is
renamed or deleted.

This page describes a rule for the **official TYPO3 documentation
repositories** (maintained under the `TYPO3-Documentation
<https://github.com/TYPO3-Documentation>`__ organization — this manual,
the Core API reference, and similar), not for third-party extension
documentation — the process goes through a repository maintained by TYPO3
GmbH, and does not scale to a pull request per extension for every rename.

Within those official repositories, whenever a change renames or deletes a
page — an actual change to the file's path, not just moving an anchor to a
different heading within another page — a redirect for the old URL
**must** be added, per the process below. Reviewers should ask for this on
any PR that renames or deletes a page and does not already include it.
This is not a courtesy: we have had real, concrete complaints from users
who followed an old bookmarked or search-indexed link and landed on a hard
404 with no explanation.

..  _redirects-adding:

Adding a redirect
=================

Redirects are configured in a **separate repository**,
`TYPO3GmbH/site-intercept <https://github.com/TYPO3GmbH/site-intercept>`__,
in the file :file:`config/nginx/redirects.conf`. Anyone can open a pull
request there against the `develop` branch — you do not need to be a
maintainer of this or any other documentation repository to do so.

Add an nginx `location` rule for the old path, using your own repository's
package name in place of `<repo-package>` below (for this manual, that is
`docs-how-to-document`):

*   **Renamed or moved to a different existing page** — redirect straight
    to the new path:

    ..  code-block:: nginx

        location ~ ^/m/typo3/<repo-package>/(main|14.3)/en-us/Old/Path/Index.html$ {
            return 303 /m/typo3/<repo-package>/$1/en-us/New/Path/Index.html;
        }

*   **Deleted, with no replacement** — redirect to a page that still
    explains what happened, rather than to an unrelated page. A common
    pattern is a dedicated :file:`Documentation/404.rst` page, with one
    section per removed concept, that the redirect can link an anchor
    within — see the `TYPO3 Core API reference's 404.rst
    <https://github.com/TYPO3-Documentation/TYPO3CMS-Reference-CoreApi/blob/main/Documentation/404.rst>`__
    for a real example: :rst:`:orphan:` at the top (it is only ever
    reached via a redirect, not linked from the table of contents), then
    one section per TYPO3 version, each removed concept as its own
    heading with the anchor(s) that used to point to it, a
    :rst:`..  deprecated::` or :rst:`..  versionchanged::` directive
    linking the changelog entry, and a short note on what to do instead.
    Most repos won't need this from the start — create it the first time
    you need to redirect removed content somewhere:

    ..  code-block:: nginx

        location ~ ^/m/typo3/<repo-package>/(main|14.3)/en-us/Old/Path/Index.html$ {
            return 303 /m/typo3/<repo-package>/$1/en-us/404.html#old-concept-anchor;
        }

Scope the version group (`(main|14.3)`, `(main|14.3|13.4)`, ...) to the
versions where the old path actually existed. Use `303` for a redirect to
different content, `301` if it is genuinely permanent and the same content
just moved.

..  important::

    :file:`redirects.conf` is shared production infrastructure for the whole of
    docs.typo3.org. A syntax error in this file will take the whole site down.
