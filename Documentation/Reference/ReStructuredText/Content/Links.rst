..  include:: /Includes.rst.txt
..  index::
    reST; Hyperlinks
    reST; Cross referencing
    reST roles; ref
..  _how-to-document-hyperlinks:

========================
Links & cross references
========================

In reStructuredText (reST) there are multiple methods to define links to
different targets. This text describes those most commonly used in TYPO3
manuals.

..  contents::

..  _rest-ref:
..  _intersphinx:

References to TYPO3 manuals
===========================

You can link the following elements in any TYPO3 manual: Headlines,
:ref:`confvals <rest-confval>` and :ref:`phpdomain definitions <rest-phpdomain>`.
It is also possible to put an anchor almost anywhere and then link it.

When an element in a manual can be linked a link symbol will appear when you
hover it:

..  figure:: /Images/link-headlines.png

    Hover over a headline to see if it is linkable, then click the link icon

After you click the link icon you can copy the reST link from the modal that
appears:

..  figure:: /Images/link-headlines-box.png

    Copy the reST reference

The reST code of the reference looks like this:

..  code-block:: rst
    :caption: Reference from another manual

    :ref:`Hide detail page in URL <georgringer/news:hideDetailPage>`

A reference has the following syntax:

..  code-block:: plaintext
    :caption: Syntax of a reST reference

    :ref:`[link_text] <[interlink]:[anchor]>`

If you are linking within the same manual you can omit the `[interlink]:` part,
including the colon.

..  code-block:: rst
    :caption: Reference from inside the same manual

    :ref:`Hide detail page in URL <hideDetailPage>`

If there is a warning box displayed, that the link has no anchor, you can
still link to it using a doc-reference:

..  figure:: /Images/link-headlines-box-warning.png

    Linking to a headline without an anchor

The link then looks like this in reST:

..  code-block:: rst

    :doc:`Some further explanations <georgringer/news:Tutorials/BestPractice/HideDetailPage/Index#some-further-explanations>`

However such a link would not work anymore if the section was moved to another
page or if another section with the same headline was introduced.

We suggest adding a unique link anchor to the headline to be linked to in this
case. See section :ref:`Link anchors <link-targets-explanation>`.

..  index:: reST; External links
..  _external-links:

External links
==============

..  important::

    Do not use this mechanism (external links) for links to sections of
    the TYPO3. Use references as described in the section above:
    :ref:`References to TYPO3 manuals <rest-reference>`.


An URL that is mentioned within a text is automatically linked:

..  code-block:: rst

    Lorem Ipsum Dolor https://example.org dolor sit

The result looks like this:

Lorem Ipsum Dolor https://example.org dolor sit

If you want to also give the URL a distinctive link text you can use the
following syntax:

..  code-block:: rst

    Lorem Ipsum Dolor `Example Page <https://example.org>`__ dolor sit

The result looks like this:

Lorem Ipsum Dolor `Example Page <https://example.org>`__ dolor sit

Sometimes links can get quite long and unruly to use within the text. You can
use so called named links to separate the link definitions from the text:

..  code-block:: rst

    Lorem Ipsum Dolor `Example Page`_ dolor sit

    ..  _Example Page: https://example.org

The result looks like this:

Lorem Ipsum Dolor `Example Page`_ dolor sit

..  _Example Page: https://example.org

..  _linking-extensions:

Linking extensions and Composer packages
========================================

You can use the text role :rst:`:composer:` to create an infobox with information
and links to Packagist. This way you can link to any TYPO3 extension
that is also listed on Packagist like :composer:`georgringer/news` and
:composer:`b13/container`, any TYPO3 system extension like
:composer:`typo3/cms-adminpanel` and any other Composer package like
:composer:`typo3/testing-framework`:

..  code-block:: rst

    This way you can link to any TYPO3 extension
    that is also listed on packagist like :composer:`georgringer/news` and
    :composer:`b13/container`, any TYPO3 system extension like
    :composer:`typo3/cms-adminpanel` and any other Composer package like
    :composer:`typo3/testing-framework`

If you want to link to the TYPO3 Extension Repository (TER) you can use the
text role :rst:`t3ext` instead and link extensions like :t3ext:`news` or
system extensions like :t3ext:`adminpanel`:

..  code-block:: rst

    You can use the text role `t3ext` instead and link extensions like
    :t3ext:`news` or system extensions like :t3ext:`adminpanel`

..  _linking-core-source:

Linking source files of the TYPO3 Core
======================================

Any file within the TYPO3 Core can be linked to their source file on GitHub using 
the text role :rst:`t3src`.

You can link classes like the
:t3src:`typo3/sysext/core/Classes/Pagination/SlidingWindowPagination.php`
and any other file type like
:t3src:`typo3/sysext/core/Resources/Private/Templates/ErrorPage/Error.html`.

..  code-block:: rst

    You can link classes like the
    :t3src:`typo3/sysext/core/Classes/Pagination/SlidingWindowPagination.php`
    and any other file type like
    :t3src:`typo3/sysext/core/Resources/Private/Templates/ErrorPage/Error.html`.

..  index:: reST; Link targets
..  _link-targets-explanation:
..  _explicit-link-targets:

Link anchors
============

Link anchors assign a unique name to a headline and its section. These anchors
can be used in internal references and references between TYPO3 manuals.

As long as the anchor of a section stays the same the section can be moved to
another page or the headline can be renamed and references will still go to the
correct target.

You can define a link anchor with a label for a section.

In the following example, the link target :rst:`columns-inline` is assigned
to the section with the title "Inline columns".

Place the link anchor definition directly before the section header:

..  code-block:: rst

    ..  _columns-inline:

    Inline columns
    ==============

..  index:: reST; Preventing links
..  _preventing-links:

Preventing links
================

Sphinx automatically converts simple URLs into links. This can be unintentional
in certain contexts, for example when using a
:ref:`hypothetical domain <hypothetical-domains>` like "example.org" or
:ref:`placeholders <codeblocks-placeholders>` instead of real query parameters
in a tutorial.
To prevent linking, the TYPO3 documentation uses the :code:`:samp:` directive
to wrap the URL.

For example:

..  code-block:: rst

    The TYPO3 backend can be accessed via :samp:`https://example.org/typo3` ..

is rendered like:

The TYPO3 backend can be accessed via :samp:`https://example.org/typo3` ..

To emphasize parts of the URL, use curly braces:

..  code-block:: rst

    The *route* is the "speaking URL" as a whole without the domain part,
    for example :samp:`https://example.org/<page-path>/{<page-name>}`.

is rendered like:

The *route* is the "speaking URL" as a whole without the domain part,
for example :samp:`https://example.org/<page-path>/{<page-name>}`.


..  index:: reST; Hypothetical domains
..  _hypothetical-domains:

Hypothetical domains
====================

The TYPO3 documentation uses a defined set of dummy domains when describing URLs
where the domain name does not matter, but serves as a placeholder. The defined
set is

1. :samp:`https://example.org`
2. :samp:`https://example.com`
3. :samp:`https://example.net`

– in this order: :samp:`https://example.org` as the preferred domain, and
:samp:`https://example.com` and :samp:`https://example.net` as alternatives if
multiple domains are required in the same context.

Why is :samp:`https://example.com` not preferred, as common sense would have it?
Because the preference for :samp:`.org` over :samp:`.com` fits with the fact
that the TYPO3 documentation is hosted on :samp:`https://typo3.org` and the
TYPO3 Association is owning the TYPO3 GmbH.

For explicit mention of the local development context it uses

4. :samp:`https://example.localhost`.

If you need additional dummy domains, use subdomains of the domains listed
above such as :samp:`https://staging.example.org` and
:samp:`https://production.example.org`.

For example:

..  code-block:: rst

    The class :php:`MailMessage` can be used to generate and send a mail without
    using Fluid:

    ..  code-block:: rst

        $mail = GeneralUtility::makeInstance(\TYPO3\CMS\Core\Mail\MailMessage::class);
        $mail
            ->from(new Address('john.doe@example.org', 'John Doe'))
            ->to(
                new Address('receiver@example.com', 'Max Mustermann'),
                new Address('other@example.net')
            )
