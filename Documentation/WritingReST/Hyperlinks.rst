.. include:: /Includes.rst.txt
.. highlight:: rst
.. index::
   reST; Hyperlinks
   reST; Cross referencing
   reST roles; ref
.. _how-to-document-hyperlinks:

==============================
Hyperlinks & cross referencing
==============================


Quick Reference
===============

In Sphinx you can use several types of links:

:ref:`external-links`
   for linking to other sources outside of the reST docs on docs.typo3.org.

   .. code-block:: rest

      `anchor text <url>`__

   (with one or two underscores at the end, if in doubt, use two)

:ref:`Cross-Referencing <cross-referencing>` (`:ref:`)
   for linking to other sections of the same manual on docs.typo3.org with Intersphinx mechanism

   .. code-block:: rest

      :ref:`anchor text <link-target>`


:ref:`Cross-Referencing <cross-referencing>` with intersphinx (`:ref:`)
   for linking to other sections of a different manual on docs.typo3.org

   If your link target is in another manual (for example "Getting Started Tutorial", you must
   add the shortcut (here: `t3start`) for the other manual:

   .. code-block:: rest

      :ref:`anchor text <t3start:link-target>`

   The shortcut must be defined in :ref:`settings-cfg`


Whenever you use the cross-referencing mechanism, you should create a
:ref:`link target <explicit-link-targets>` for a section chapter,
by adding a label before the section header::

      .. _link-target:

      Headline
      ========


How to create links is described in more detail in the next sections.

:ref:`Preventing links <preventing-links>`
   being automatically generated from simple URLs – mostly used in connection
   with hypothetical domains.

   .. code-block:: rest

      :samp:`<url>`


:ref:`Hypothetical domains <hypothetical-domains>`
   are domains for use in URLs where the domain does not matter, but serves as a
   placeholder. The TYPO3 documentation uses a defined set of them.

   .. code-block:: rest

      :samp:`https://example.org/news/`


.. index:: reST; External links
.. _external-links:

External links
==============

.. important::

   Do not use this mechanism (external links) for links to sections of
   the official documentation. Use the Intersphinx mechanism as described
   in :ref:`intersphinx`. See :ref:`intersphinx-benefits` for an explanation
   of why you should do this.


You can use one or more underscores (`_`) for the link. The difference is as follows:

*  One underscore creates a :ref:`named reference <external-links-named-reference>`
*  Two underscores create an :ref:`anonymous URL <external-links-anonymous>`

For further explanation of the difference between these 2, please see
`Stackoverflow <https://stackoverflow.com/questions/27420317/restructured-text-rst-http-links-underscore-vs-use>`__.


If in doubt, just use 2 underscores as explained in the next section :ref:`external-links-anonymous`.


.. index:: reST; Anonymous URL
.. _external-links-anonymous:

External link as anonymous URL
------------------------------

Syntax
~~~~~~

::

   `Anchor text <URL>`__

*  There must always be a space between the anchor text and the URL

Example
~~~~~~~

::

   `Sphinx hyperlinks <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#hyperlinks>`__


How it looks
~~~~~~~~~~~~

`Sphinx hyperlinks <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#hyperlinks>`__


.. index:: reST; Named references
.. _external-links-named-reference:

External link as named reference
--------------------------------

Syntax
~~~~~~

Same as :ref:`anonymous URL <external-links-anonymous>`, but with one
underscore instead of 2.

::

   `Anchor text <URL>`_

*  There must always be a space between the anchor text and the URL



.. index:: reST; Link targets
.. _link-targets-explanation:

Link targets
============

When using the :ref:`intersphinx` mechanism (as described in the next section), you
will link to link targets.


.. index:: reST; Link targets, explicit
.. _explicit-link-targets:

Explicit link targets (Labels for cross referencing)
----------------------------------------------------

You can define an explicit link target with a label for a section (or chapter):

A section label of the name `columns-inline` is set::

   .. _columns-inline:


Here, the link target *columns-inline* will be defined.

*  Place the link target definition directly before the section header:

.. code-block:: rest

   .. _columns-inline:

   Inline columns
   ==============

*  You can define more than one link target definition (for example if
   you want to keep some for historical reasons to not break links but
   the name has changed considerably)


.. index:: reST; Link targets, implicit
.. _implicit-link-targets:

Implicit link targets
---------------------

For every section (or chapter), an implicit link target is created from the
header.

However, there are some disadvantages in using these, so we will not go into
that further.


.. index::
   reST; Link targets, Cross referencing
   reST roles; ref
.. _intersphinx:
.. _cross-referencing:

Cross referencing (`:ref:`)
===========================

This section describes how to link to sections of the current or other
manuals correctly.


Additional information: See the `Sphinx documentation
<https://www.sphinx-doc.org/en/1.6/markup/inline.html#cross-referencing-arbitrary-locations>`__.

For an overview of the link types, see :ref:`cheat-sheet-intersphinx` in
the "ReST & Sphinx Cheat Sheet".

In the same manual
------------------

A :ref:`section label <explicit-link-targets>` of the name `columns-inline` has been set somewhere::

   .. _columns-inline:

   Inline Columns
   ==============


You can then link to it like this **from the same manual**::

  :ref:`columns-inline`

This will use the header of the section as anchor text.

You can also explicitly set an anchor text::

   :ref:`Inline columns <columns-inline>`


From one manual to another
--------------------------

Example 1: Use text of headline as anchor text
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Again, we want to link to the labels `columns-inline` and `This-is-ABC`.

But since the labels are now in a different manuals, we
need to prefix the names of that manuals:

.. code-block:: rest

   :ref:`t3tca:columns-inline`
   :ref:`t3install:This-is-ABC`


The name `t3tca` is the name we have given it in the :file:`Settings.cfg` file: .
`This-is-ABC` is just an example wording.

.. code-block:: none

   t3tca         = https://docs.typo3.org/m/typo3/reference-tca/master/en-us/
   t3install     = https://docs.typo3.org/m/typo3/guide-installation/master/en-us/


.. important::

   Check the Settings.cfg file for the manual you are working on to
   make sure the manual shortcuts for intersphinx linking are available
   in the section `[intersphinx_mapping]`.
   You may need to remove the comment marker `#` at the beginning of the line.


This is called cross-referencing with the *intersphinx* mechanism.

In this example, the linktext shown will be whatever the text
of the headline is that follows the label *in the manual we link to*, in this case
the TCA manual.


Example 2: Specify anchor text
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


If we want to control the anchor text ourselves, we can do so by
writing:

.. code-block:: rest

   :ref:`this is our linktext <t3tca:columns-inline>`

.. _intersphinx-benefits:

Understanding the benefits
--------------------------

Imagine that the TCA manual has been restructured. Text and maybe urls changed, but the - purely -
symbolic label has been kept. As a result the links (= intersphinx references) in foreign
manuals will work again as soon they are rebuilt.

Tips
----

1. For convenience many manuals already have a page "Linktargets" where you can easily
   see what linktargets are available. Example: https://docs.typo3.org/m/typo3/reference-tca/master/en-us/Targets.html

2. As an editor you should not change or remove labels once they have been published.
   If you feel that a label (= linktarget) should be changed you should keep the old one
   and add the new one on a separate line. You cannot know whether some other manual in
   the world links to the label you would like to remove.

3. You still CAN remove that label. The only problem that may arise is that foreign links
   aren't generated any more.


.. index:: reST; Preventing links
.. _preventing-links:

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

.. code-block:: rest

   The TYPO3 backend can be accessed via :samp:`https://example.org/typo3` ..

is rendered like:

The TYPO3 backend can be accessed via :samp:`https://example.org/typo3` ..

To emphasize parts of the URL, use curly braces:

.. code-block:: rest

   The *route* is the "speaking URL" as a whole without the domain part,
   for example :samp:`https://example.org/<page-path>/{<page-name>}`.

is rendered like:

The *route* is the "speaking URL" as a whole without the domain part,
for example :samp:`https://example.org/<page-path>/{<page-name>}`.


.. index:: reST; Hypothetical domains
.. _hypothetical-domains:

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

.. code-block:: rest

   The class :php:`MailMessage` can be used to generate and send a mail without
   using Fluid:

   ::

      $mail = GeneralUtility::makeInstance(\TYPO3\CMS\Core\Mail\MailMessage::class);
      $mail
         ->from(new Address('john.doe@example.org', 'John Doe'))
         ->to(
            new Address('receiver@example.com', 'Max Mustermann'),
            new Address('other@example.net')
         )
