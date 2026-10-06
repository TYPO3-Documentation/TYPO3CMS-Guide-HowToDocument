:navigation-title: Documentation links
..  include:: /Includes.rst.txt

..  _rest-ref:
..  _intersphinx:

============================
Links to TYPO3 documentation
============================

You can link the following elements in any TYPO3 manual: headlines,
:ref:`confvals <rest-confval>`, and
:ref:`PHP domain definitions <rest-phpdomain>`.
You can also put an :ref:`anchor <link-targets-explanation>` almost anywhere
and link to it.

There are two ways to write such a link:

*   A :ref:`permalink <permalinks>`, written as a normal link with a URL. This
    is the preferred way, also for links inside the same manual.
*   A :ref:`reST reference <rest-ref-role>` with the :rst:`:ref:` text role.

Both ways point to an anchor, not to a file. The link keeps working when the
section moves to another page or its headline is renamed.

..  contents:: Table of contents
    :local:

..  _link-modal:

Copy the link from the link modal
=================================

When you hover over an element that can be linked, a link icon appears:

..  figure:: /_Images/link-headlines.png

    Hover over a headline to see if it is linkable, then click the link icon

Click the link icon. A modal opens that offers the permalink and the reST
reference for this element:

..  figure:: /_Images/link-headlines-box.png

    Copy the permalink or the reST reference

Copy the link from this modal rather than assembling it by hand. Do not copy
the URL from the address bar of your browser: it contains the version and the
path of the page, and it breaks when the page is moved.

..  _permalinks:

Permalinks
==========

A permalink is a plain URL on docs.typo3.org. It names the manual and the
anchor of the element, and it redirects to the current location of the
element in the `main` version of the manual. Use it like any other
:ref:`external link <external-links>`:

..  code-block:: rst
    :caption: A permalink in reST

    Tag the entries with
    `cache tags <https://docs.typo3.org/permalink/t3coreapi:caching-developer-cache-tags>`_
    so that they can be flushed together.

A permalink has the following syntax:

..  code-block:: plaintext
    :caption: Syntax of a permalink

    https://docs.typo3.org/permalink/[interlink]:[anchor]

Permalinks are the preferred way to link TYPO3 documentation, for the
following reasons:

*   You can open a permalink directly from the source file, in an editor, a
    diff, or a review. You do not have to render the manual first to see
    where the link goes.
*   The same link works in reST, in Markdown, in a commit message, in an
    issue, and in a chat.
*   The rendering turns a permalink into a direct link to its target. A
    permalink into the same manual therefore does not leave the rendered
    manual through a redirect.

..  _permalinks-rules:

Rules for permalinks
--------------------

If you write or change a permalink by hand, follow these three rules:

#.  **The interlink shortcode is required.** It is needed even when the anchor
    lives in the manual you are writing in:
    `permalink/t3coreapi:dependency-injection` resolves,
    `permalink/dependency-injection` does not.

#.  **The manual is written with hyphens, not slashes.** This is where a
    permalink differs from a reST reference: :rst:`:ref:` uses
    `friendsoftypo3/content-blocks:`, the permalink uses
    `friendsoftypo3-content-blocks:`.

#.  **Underscores in an anchor become hyphens.** The anchor
    `..  _run_upgrade_wizard:` is published as `run-upgrade-wizard`, so only
    `permalink/t3coreapi:run-upgrade-wizard` resolves.

The rendered page links to the right target even if you break one of these
rules. The URL in the source file, however, returns 404 for everyone who opens
it from there. Since render-guides 0.42.0, the rendering warns about all three
mistakes, so :bash:`make test-docs` fails on them. See
`render-guides issue #1402 <https://github.com/TYPO3-Documentation/render-guides/issues/1402>`_.

..  _rest-ref-role:

reST references
===============

A reST reference uses the :rst:`:ref:` text role:

..  code-block:: rst
    :caption: Reference to another manual

    To keep news URLs short, :ref:`hide the detail page <georgringer/news:hideDetailPage>`.

A reference has the following syntax:

..  code-block:: plaintext
    :caption: Syntax of a reST reference

    :ref:`[link_text] <[interlink]:[anchor]>`

If you link within the same manual, you can omit the `[interlink]:` part,
including the colon:

..  code-block:: rst
    :caption: Reference inside the same manual

    To keep news URLs short, :ref:`hide the detail page <hideDetailPage>`.

Many manuals contain reST references. They keep working, and you do not have
to replace them with permalinks.

..  _rest-doc-role:

Headlines without an anchor
===========================

If the modal shows a warning that the headline has no anchor, it offers a
:rst:`:doc:` link instead:

..  figure:: /_Images/link-headlines-box-warning.png

    Linking to a headline without an anchor

The link then looks like this in reST:

..  code-block:: rst

    :doc:`Some further explanations <georgringer/news:Tutorials/BestPractice/HideDetailPage/Index#some-further-explanations>`

Such a link points to a file and a headline, not to an anchor. It breaks when
the section is moved to another page, and it can point to the wrong section
when another section with the same headline is added.

Add a unique anchor to the headline instead, and link to that anchor with a
permalink. See section :ref:`Link anchors <link-targets-explanation>`.

..  _link-text:

Always give a link text
=======================

Give every permalink and every reference its own link text, written to fit
the sentence it appears in:

..  code-block:: rst

    Tag the entries with
    `cache tags <https://docs.typo3.org/permalink/t3coreapi:caching-developer-cache-tags>`_
    so that they can be flushed together.

    To keep news URLs short, :ref:`hide the detail page <georgringer/news:hideDetailPage>`.

A permalink without a link text shows the bare URL.

A reference without a link text, such as
``:ref:`georgringer/news:hideDetailPage```, uses the headline of the
target section instead. This causes two problems:

*   A headline is written as a title, not as part of your sentence.
    "To keep news URLs short, Hide detail page in URL." does not read well,
    and you cannot adapt the wording to the grammar around it.
*   Headlines change. When a headline is renamed, its anchor
    `stays the same <https://docs.typo3.org/permalink/h2document:anchor-persistence>`_,
    so the link keeps working, but its text changes with the headline. The
    link can then stop fitting your sentence, or stop saying what you meant,
    without anybody touching your page.

The link modal uses the headline of the target as the link text. Reword that
text to fit your sentence before you use it.

..  _check-link-text:

Let the rendering check the link texts
--------------------------------------

A manual can have the rendering warn about every reference that has no link
text of its own. Switch the check on with
`check-link-text <https://docs.typo3.org/permalink/h2document:settings-guides-check-link-text>`_
in :file:`Documentation/guides.xml`:

..  code-block:: xml
    :caption: Documentation/guides.xml

    <extension class="\T3Docs\Typo3DocsTheme\DependencyInjection\Typo3DocsThemeExtension"
               check-link-text="true" />

The check is off by default, because a warning fails a render with
:bash:`--minimal-test` and most manuals still have references without a link
text. Give the references of your manual a link text first, then switch it on
so that the next one cannot slip in unnoticed.

..  _check-link-text-page:

Switching the check for a single page
-------------------------------------

A page can override the setting of its manual with a field above the title:

..  code-block:: rst
    :caption: Documentation/Reference/Menus/NavigationTitle.rst

    :check-link-text: off

    ================
    Navigation title
    ================

Use `off` for a page that shows a reference without a link text on purpose,
for example one that demonstrates what such a reference does. Use `on` while
a manual is being cleaned up page by page and the setting of the manual is
still off.
