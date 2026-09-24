:navigation-title: Rendered artifacts

..  include:: /Includes.rst.txt

..  _rendered-artifacts:

==========================================
What a render publishes beside the pages
==========================================

Rendering a manual produces more than the HTML pages a reader sees. Beside
them it writes a handful of files that describe the manual itself: its
inventory, its table of contents, the classes it speaks of, and every page a
second time as Markdown. They are published with the manual, at the same URL
as its pages, and they are what other manuals, the search and machine clients
read.

You never write these files, and nothing in your sources refers to them. They
are worth knowing about all the same: they are the reason an anchor and a
headline are not only decoration, and they answer questions about a manual
that reading its pages one by one cannot.

..  _rendered-artifacts-markdown:

Every page as Markdown
======================

Every page is published a second time as Markdown, at its own URL with `.md`
instead of `.html`:

..  code-block:: text

    https://docs.typo3.org/m/typo3/reference-coreapi/main/en-us/Index.md

It holds the content of the page without navigation, theme or markup, and it
is a fraction of the size. Each rendered page announces it in its `<head>`
with a `<link rel="alternate" type="text/markdown">` tag.

The Markdown is produced from the same build as the HTML, after includes are
resolved and generated directives are expanded, so it holds what the page
holds — unlike the reST source below.

..  _rendered-artifacts-inventory:

The inventory
=============

The inventory lists everything a manual can be linked to: every page,
headline, anchor and named entity, with its title and its URL. It is written
twice, as JSON and in the Sphinx format:

..  code-block:: text

    https://docs.typo3.org/m/typo3/reference-coreapi/main/en-us/objects.inv.json
    https://docs.typo3.org/m/typo3/reference-coreapi/main/en-us/objects.inv

This is what an interlink resolves against. When you write
:rst:`:ref:`Link text <t3coreapi:some-anchor>``, the rendering of your manual
downloads the inventory of that manual and looks the anchor up in it. An
anchor that is not in the inventory is what a "could not be resolved" warning
is about, and an anchor that is only added later is why a reference can start
working after a re-render.

See
`Interlink inventories <https://docs.typo3.org/permalink/t3renderguides:interlinkrepositories>`_
for the format.

..  _rendered-artifacts-toc:

The table of contents
=====================

..  code-block:: text

    https://docs.typo3.org/m/typo3/reference-coreapi/main/en-us/toc.json

The pages of a manual in the order its table of contents puts them, nested the
way it nests them, each with its title and the anchor its permalink is built
from. Pages no toctree leads to are marked as orphans, which makes this the
quickest way to find a page that has fallen out of the menu.

See
`Table of contents as JSON <https://docs.typo3.org/permalink/t3renderguides:tableofcontentsjson>`_
for the format.

..  _rendered-artifacts-classes:

The class index
===============

..  code-block:: text

    https://docs.typo3.org/m/typo3/reference-coreapi/main/en-us/classes.json

Every PHP class a manual speaks of, with the places that speak of it: where
the text names the class, where a code example uses it, and where the manual
documents the class itself. It answers what the inventory cannot, namely where
a class is explained and what else mentions it at all — the inventory lists
what a manual documents, which is the definitions alone.

This is also what makes the difference between :rst:`:php:` and a plain
literal visible from outside a page: a class written as a code role is found,
a class written as ordinary text is not. See
`PHP classes and interfaces <https://docs.typo3.org/permalink/h2document:inline-code-php>`_.

See
`Class index as JSON <https://docs.typo3.org/permalink/t3renderguides:classindexjson>`_
for the format, which is still settling.

..  _rendered-artifacts-changelog:

The changelog index
===================

..  code-block:: text

    https://docs.typo3.org/c/typo3/cms-core/main/en-us/Changelog-14.json

Published for the TYPO3 Core Changelog only, one file per major release. Each
entry carries its permalink, title, the kind of change, the Forge issue and
its tags, so the changes of a release can be read without walking the overview
page. See
`Changelog index <https://docs.typo3.org/permalink/t3renderguides:changelogindex>`_.

..  _rendered-artifacts-sources:

The reST source
===============

The source of every page is published as well, under `_sources`:

..  code-block:: text

    https://docs.typo3.org/m/typo3/reference-coreapi/main/en-us/_sources/Index.rst.txt

It is the file as you wrote it, which means it is smaller than the page and
sometimes says less: an `include` is not resolved in it, and a directive that
generates its content, such as the arguments of a ViewHelper, has nothing in
it at all. Use the Markdown above where the complete content matters.

..  _rendered-artifacts-no-singlehtml:

The single file of a whole manual
=================================

Until render-guides 0.44.0 every manual was also published as one large HTML
page under `singlehtml/`. It is no longer produced, and it disappears from a
manual with that manual's next render.

You can still make one locally, from your own sources:

..  code-block:: bash

    docker run --rm --pull always -v "$(pwd)":/project -t \
      ghcr.io/typo3-documentation/render-guides:latest --config=Documentation --single-markdown

`--single-markdown` writes the whole manual into :file:`singlemd/Index.md`,
`--single-html` into :file:`singlehtml/Index.html`. Both render that one file
and nothing else, which makes them a quick way to read or search a whole
manual at once.

..  _rendered-artifacts-crawling:

Who reads these files
=====================

`llms.txt <https://docs.typo3.org/llms.txt>`_ describes the artifacts above
for AI clients and tells them to start from the inventory or the table of
contents rather than crawling the pages, and
`robots.txt <https://docs.typo3.org/robots.txt>`_ allows all of them for every
client. Both files are maintained in the
`homepage repository <https://github.com/TYPO3-Documentation/DocsTypo3Org-Homepage>`_.
