.. include:: /Includes.rst.txt
.. highlight:: rst

.. _content-styleguide:
.. _spelling:

========
Spelling
========



General information
===================

The authoritative style guide for writing official text for TYPO3 is `The TYPO3 Writing Style Guide
<https://typo3.org/community/teams/content/writing-style-guide/>`__ on typo3.org.

.. important::

   We use different **title capitalization** from the content style guide, to ease contribution.
   The main differences are explained below in :ref:`spelling-title-case`.

This section aims to add some additional explanations and more examples for rules
already defined in the style guide. It also explains how to apply the rules in
the documentation (e.g. format with reST).

Since the English language is not always specific and there may be more than one correct spelling
for some words, we have added a :ref:`spelling-ref`. If something is not
mentioned here specifically, use correct spelling in English language
or rather American (US) language. Refer to the resources, which the style guide suggests, or use
`Merriam Webster (https://m-w.com) <https://www.merriam-webster.com/>`__ as last resort.
If in doubt, ask in Slack channel #typo3-documentation (see :ref:`how-to-get-help`).

.. _spelling-title-case:
.. _spelling-ref-title:

Rules for titles & section headers
==================================

We use "sentence case" for title case:

*  The first word is capitalized.
*  All other words are spelled as they would be spelled elsewhere: Proper nouns are capitalized,
   all other words written in lowercase.

This is different from the content style guide where more words are capitalized (first
and last word, all words with 4 letters and more, all principal words).

This was changed on February 4, 2020 for the following reasons:

*  Sentence case is easier to follow for occasional contributors and developers
*  It is already being used intuitively by contributors most of the time. If
   the other title capitalization were enforced, a number of PR would have
   to be corrected as they come in.
*  Most of the documentation is spelled this way

This means, the same rules as in :ref:`spelling-plain-text` apply to the titles.

For discussion, see `Title capitalization in the docs (revisited) <https://decisions.typo3.org/t/title-capitalization-in-the-docs-revisited/562>`__

Examples:

*  "TYPO3 is always spelled TYPO3"
*  "Using TypoScript"

.. important::

   This applies to **all headers** on a page, not just the top level header (title).

In reST, headers are created by underlining / overlining with (`====`, `----`, etc.)
as described in :ref:`Headlines-and-sections`::

   =================
   This is the title
   =================

   This is the subheader
   =====================



.. _spelling-buttons:
.. _spelling-anchor-text:

Rules for buttons & links
=========================

The same spelling rules as in the title apply to buttons and links.


.. _spelling-refer-to-gui-elements:

Rules for referring to GUI elements
===================================

If the text refers to terms used in the GUI (e.g. a clickpath for selecting
something from the menu is described), the spelling used in the GUI should be
used, e.g. "*File > Open*" or "click on "*ADMIN TOOLS > Extensions*".

See :ref:`rest-refer-to-gui-elements` for information about how to use reST
markup for this.

.. _spelling-plain-text:

Rules for plain text
====================


.. _spelling-compound-words:

Rules for compound words
------------------------

Compound words (or compounds) are words that have been glued together from one or more separate
words to create a new term with a new meaning as in backyard (back and yard) or
New Age (new and age).

But how should they be spelled? Backend, back-end or back end? Site package or sitepackage?

All these spellings for backend are currently correct spellings (at least according to
`some sources <https://ell.stackexchange.com/questions/117383/what-is-the-correct-term-back-end-back-end-or-backend>`__.

.. important::

   **In the TYPO3 context** we have defined **backend** to be the preferred spelling,
   as well as **sitepackage**.

   If a spelling has been explicitly defined in the :ref:`spelling-ref`, please
   use that spelling.

How can you decide for yourself in other edge cases?

.. tip::

   If in doubt, use what is commonly used in the documentation. If you see inconsistencies between
   documentation and English dictionaries or within the documentation, raise
   the issue in Slack.



.. _spelling-plain-text-capitalization:

Capitalization rules (plain text)
---------------------------------

#. If a word has special spelling, e.g. a :ref:`special TYPO3 word <spelling-typo3>`
   like TypoScript or an :ref:`acronym <spelling-acronyms>` like PHP,
   this spelling is applied.
#. :ref:`Proper nouns and brand names <spelling-proper-names>` are
   capitalized, e.g. Docker.
#. Most other words begin with a lowercase letter.

There are some edge cases and some terms are not spelled consistently throughout various
resources. Often it also depends on the context. Capitalization may change over the course of
time, for example see `The Associated Press style guide will no longer capitalize 'internet'
<https://www.theverge.com/2016/4/2/11352744/ap-style-guide-will-no-longer-capitalize-internet>`__.
In other texts, "internet" is still capitalized.

For this reason we have put together a :ref:`spelling reference <spelling-ref>`
to list some common terms that may be difficult to spell or that are spelled differently in the TYPO3 context.

.. _spelling-typo3:

Exceptions for specific TYPO3 spellings
---------------------------------------

There are some specific TYPO3 spellings like TypoScript, TSconfig, stdWrap, ViewHelper,
TYPO3, etc. These should be used! See :ref:`spelling-ref` for more examples.

.. _spelling-source-code:

Exceptions for words taken from source code
-------------------------------------------

If you are using class names, function names, databases tables or fields, configuration
options etc, use the spelling that is used in the source code.

Examples:

*  function names in :ref:`t3coreapi:database-connection`
*  configuration options in :ref:`t3coreapi:soft-references-default-parsers-substitute`


.. _spelling-acronyms:

Acronyms
--------

Often acronyms are written with capital letters only. If terms are commonly spelled that
way, this is how we spell them as well, for example HTML, CMS, PHP or LTS.


.. _spelling-proper-names:

Proper names, brand names
-------------------------

General rules of the English language apply here:

If `proper names <https://en.wikipedia.org/wiki/Proper_names>`__ or brand names (e.g. Coca-Cola)
are used in normal text (not headlines), they are capitalized.

These can be countries, names of people, corporations or brand names.

Examples:

*  "This manual is designed to be readable by someone with basic UNIX command-line skills, but no
  previous knowledge of **Git**.": Git is capitalized, because it is a brand name (quote from
  `Git User Manual <https://mirrors.edge.kernel.org/pub/software/scm/git/docs/user-manual.html>`__)
*  **Wikipedia**
*  **Europe**

.. _spelling-executables:

Tools With executables
~~~~~~~~~~~~~~~~~~~~~~

Some tools have a program, which you can run. For example, **Git** has the command line
tool `git`. When the documentation explicitly refers to the command `git`, its appropriate
spelling is used, which is lowercase. In all other cases, we use capital
spelling for Git, because it applies to the rules for :ref:`spelling-proper-names`.

The same goes for **Docker**, **Composer**, etc.



Spelling & preferred terms reference
====================================

The content was moved to :ref:`spelling-ref`.

.. _spelling-ref-title:



Used resources
==============

In addition to the TYPO3 Content Style Guide, some other resources have been used:

*  `Microsoft Writing Style Guide <https://docs.microsoft.com/en-us/style-guide/welcome/>`__
*  "Don't use the same word for 2 different meanings", see `RACKSPACE DEVELOPER DOCS:
   Use consistent terminology
   <https://developer.rackspace.com/docs/style-guide/terminology/general-term-guidelines/use-consistent-terms/>`__
*  `Microsoft style guide <https://docs.microsoft.com/de-de/style-guide/welcome/>`__

Capitalization:

*  *"The tendency towards lowercase, which in part reflects a less formal, less deferential society, has
   been accelerated by the explosion of the internet."*,
   `Guardian and Observer Styleguide <https://www.theguardian.com/guardian-observer-style-guide-c>`__,
   look under "capital".
   Note that these are British publications and we use American spelling.
*  *"When referring to GUI elements, match the capitalization used in the interface."*, see
   `IBM developerWorks editorial style guide
   <https://www.ibm.com/developerworks/library/styleguidelines/index.html>`__
*  `Stackexchange: Proper capitalization of commonly used acronyms
   <https://english.stackexchange.com/questions/51924/proper-capitalization-of-commonly-used-acronyms>`__
*  `The Associated Press style guide will no longer capitalize 'internet'
   <https://www.theverge.com/2016/4/2/11352744/ap-style-guide-will-no-longer-capitalize-internet>`__
*  `Wikipedia: English capitalization of proper nouns <https://en.wikipedia.org/wiki/Proper_noun#English_capitalization_of_proper_nouns>`__
*  *"A proper noun is a noun directly associated with an entity and primarily used to refer to
   that entity, such as London, Jupiter, Sharon, or Microsoft, as distinguished from a common
   noun, which is a noun directly associated with a class of entities (city, planet, person,
   corporation) and primarily used to refer to instances of a specific class (a city, another
   planet, these persons, our corporation)"* (quote from `Wikipedia: Proper Noun
   <https://en.wikipedia.org/wiki/Proper_noun>`__)
*  *"[...]  proper nouns are limited to single words only (possibly with the), while proper names
   include all proper nouns (in their primary applications) as well as noun phrases such as the
   United Kingdom, North Carolina"* (quote from `Wikipedia: Proper Names
   <https://en.wikipedia.org/wiki/Proper_noun#Proper_names>`__)

Compound words:

*  `Wikipedia: English compound <https://en.wikipedia.org/wiki/English_compound>`__
