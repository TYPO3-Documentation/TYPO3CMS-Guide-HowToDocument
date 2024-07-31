:navigation-title: example.org
..  include:: /Includes.rst.txt

..  index:: reST; Preventing links
..  _preventing-links:

===========================
Example domain: example.org
===========================

The renderer automatically converts simple URLs into links. This can be unintentional
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
