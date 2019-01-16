.. include:: ../Includes.txt
.. highlight:: rst

.. _content-styleguide:
.. _spelling:

========
Spelling
========



The same applies to TYPO3 documentation!

General Information
===================

The authoritative style guide for writing official text for TYPO3 is `The TYPO3 Writing Style Guide
<https://typo3.org/community/teams/content/writing-style-guide/>`__ on typo3.org.

This section aims to add some additional explanations and more examples for rules
already defined in the style guide. It also explains how to apply the rules in
the documentation (e.g. format with reST).

Since English language is not always specific and there may be several correct spellings
for some words, we have added a :ref:`spelling-ref`. If somethings is not
mentioned here specifically, use correct spelling in English language,
or rather American (US) language. Refer to the resources, which the style guide suggests, or use
`Merriam Webster (https://m-w.com) <https://www.merriam-webster.com/>`__ as last resort.
If in doubt, ask in Slack channel #typo3-documentation (see
:ref:`how-to-get-help`) or contact
`the Content Group <https://typo3.org/community/teams/content/>`__.

If you found something missing here and you have researched the answer, please
add that information yourself. See "Edit me on Github", see :ref:`docs-contribute`
for more information about how to make changes to the documentation.


.. _spelling-title-case:

Rules for Titles & Section Headers
==================================

Basic rules (read in this order, use the first rule that applies and skip the rest):

#. Exceptions: Words with special spelling like TYPO3, TypoScript, PHP, stdWrap etc. are written the
   way they are commonly written (see :ref:`spelling-typo3`, :ref:`spelling-acronyms`).
#. First and last word of title is always capitalized.
#. Capitalize all words with 4 or more letters.
#. Capitalize all important words (nouns, `pronouns <https://en.wikipedia.org/wiki/Pronoun>`__,
   adjectives, verbs, adverbs), for example "Is", "Are", "Has".
#. Lowercase `articles <https://www.merriam-webster.com/dictionary/article>`__ (e.g. a, an, the)
   `prepositions <https://www.merriam-webster.com/dictionary/preposition>`__
   (e.g. in) and `conjunctions <https://www.merriam-webster.com/dictionary/conjunction>`__
   (e.g. and, or) **with fewer than 4 letters**.

Capitalize means: The first letter of a word  is a capital letter. Example: **England** is capitalized,
**the** is not.

.. tip::

   You can use the tool https://capitalizemytitle.com/ to check the title. Choose "AP" and
   "Title Case" for correct spelling in title. The result may slightly deviate from our rules
   for the exceptions (e.g. TYPO3). For a spelling reference, see :ref:`spelling-ref-title`
   on this page.

The rules for title case are based on the `TYPO3 Content Style Guide
<https://typo3.org/community/teams/content/writing-style-guide/#c8486>`__:

Examples:

* TYPO3 is always spelled TYPO3 (rule #1): "TYPO3 is Always Spelled TYPO3", "stdWrap", "Programming With PHP"
* The first word is always capitalized (see rule #2), so *in* is capitalized here: "**In** the End"
* *With* is a preposition with 4 letters, so it must be capitalized (rule #3): "Install **With** Composer"
* *Is* is a verb. Though it is short, do capitalize it (rule #4), as in "This **Is** the End"
* *In* is a preposition with fewer than 4 letters, so first letter is lowercase (rule #5): "Rules **in** the Style Guide"

.. important::

   This applies to **all headers** on a page, not just the top level header (title).

In reST, headers are created by underlined / overlining with (`====`, `----`, etc.)
as described in :ref:`Headlines-and-sections`::

   =================
   This Is the Title
   =================

   This Is the Subheader
   =====================



.. _spelling-buttons:

Rules for Buttons
=================


The same rules as in the title apply to buttons: `Style Guide: Buttons
<https://typo3.org/community/teams/content/writing-style-guide/#c8487>`__

.. _spelling-anchor-text:

Rules for Links
===============

If you refer to another document, chapter or section of another manual in the docs
and use the title of that as anchor text, use title capitalization.

This has an additional advantage: If you do not specifically supply an anchor text with
the `:ref:` directive, the title from the referred to page will automatically be
used as anchor text (which will hopefully already be spelled correctly using
title capitalization).

Example:

.. code-block:: rest

   Please see :ref:`t3coreapi:start` to get a good understanding of ...

How this looks:
   Please see :ref:`t3coreapi:start` to get a good understanding of ...


If you refer to another page outside of the docs, you may use the title
capitalization and spelling that is used on that external page (preferred),
but using our title capitalization will also be correct.

Example:

.. code-block:: rest

   See `Test Docker installation  <https://docs.docker.com/get-started/#test-docker-installation>`__

In our spelling, this would be "Test Docker Installation".


How this looks:
   See `Test Docker installation  <https://docs.docker.com/get-started/#test-docker-installation>`__

.. _spelling-refer-to-gui-elements:

Rules for Referring to GUI Elements
===================================

If the text refers to terms used in the GUI (e.g. a clickpath for selecting
something from the menu is described), the spelling used in the GUI should be
used, e.g. "*File > Open*" or "click on "*ADMIN TOOLS > Extensions*".

See :ref:`rest-refer-to-gui-elements` for information about how to use reST
markup for this.

.. _spelling-plain-text:

Rules for Plain Text
====================

As already mentioned: If the text is used in :ref:`titles, subheaders <spelling-title-case>`,
:ref:`anchor text <spelling-anchor-text>` or a text is :ref:`referring to
GUI elements <spelling-refer-to-gui-elements>`, use the correct spelling for that.

For all else (plain text), common rules of the English language are applied.


.. _spelling-compound-words:

Rules for Compound Words
------------------------

Compound words (or compounds) are words that have been glued together from one or more separate
words to create a new term with a new meaning as in backyard (back and yard) or
New Age (new and age).

But, how will they be spelled? Backend, back-end or back end? Site package or sitepackage?

All these spellings for backend are currently correct spellings (at least according to
`some sources <https://ell.stackexchange.com/questions/117383/what-is-the-correct-term-back-end-back-end-or-backend>`__.

.. important::

   **In the TYPO3 context** we have defined **backend** to be the preferred spelling,
   as well as **sitepackage**.

   If a spelling has been explicitly defined in the :ref:`spelling-ref`, please
   use that spelling.

How can you decide for other edge cases yourself?


.. tip::

   If in doubt, use what is commonly used in the documentation. If you see inconsistencies between
   documentation and English dictionaries or within the documentation, raise
   the issue in Slack.



.. _spelling-plain-text-capitalization:

Capitalization Rules (plain text)
---------------------------------

#. If a word has special spelling, e.g. a :ref:`special TYPO3 word <spelling-typo3>`
   like TypoScript or an :ref:`acronym <spelling-acronyms>` like PHP,
   this spelling is applied.
#. :ref:`Proper nouns and brand names <spelling-proper-names>` are
   capitalized, e.g. Docker
#. Most other words begin with a lowercase letter.

There are some edge cases and some terms are not spelled consistently in the same way
everywhere. Sometimes it also depends on the context. Capitalization may change over
the course of time, for example see `The Associated Press style guide will no longer capitalize 'internet'
<https://www.theverge.com/2016/4/2/11352744/ap-style-guide-will-no-longer-capitalize-internet>`__
In other texts, "internet" is still capitalized.

For this reason, we have put together a :ref:`spelling reference <spelling-ref>`
to list some common
terms that may be difficult to spell or that are spelled differently in the TYPO3 context.

.. _spelling-typo3:

Exceptions: Specific TYPO3 spellings
------------------------------------

There are some specific TYPO3 spellings like TypoScript, TSconfig, stdWrap, ViewHelper,
TYPO3, etc. These should be used! See :ref:`spelling-ref` for more examples.

.. _spelling-acronyms:

Acronyms
~~~~~~~~

Often, acronyms are written with capital letters only. If terms are commonly spelled that
way, this is how we spell them as well, for example HTML, CMS, PHP or LTS.


.. _spelling-proper-names:

Proper Names, Brand Names
~~~~~~~~~~~~~~~~~~~~~~~~~

General rules of the English language apply here:

If `proper names <https://en.wikipedia.org/wiki/Proper_names>`__ or brand names (e.g. Coca-Cola)
are used in normal text (not headlines), they are capitalized.

These can be countries, names of people, corporations or brand names.

Examples:

* "This manual is designed to be readable by someone with basic UNIX command-line skills, but no
  previous knowledge of **Git**.": Git is capitalized because it is a brand name (quote from
  `Git User Manual <https://mirrors.edge.kernel.org/pub/software/scm/git/docs/user-manual.html>`__)
* **Wikipedia**
* **Europe**

.. _spelling-executables:

Tools With Executables
~~~~~~~~~~~~~~~~~~~~~~

Some tools have a program, which you can run. For example, **Git** has the command line
tool `git`. In this case, we use the correct spelling of the command (lowercase), when
we are explicitly referring to the command `git`. In all other cases, we use capital
spelling Git, because it applies to the rules for :ref:`spelling-proper-names`.

The same goes for **Docker**, **Composer**, etc.




.. _preferred-terms:
.. _spelling-ref:
.. _spelling-ref-this-guide:

Spelling & Preferred Terms Reference
====================================

The spelling here is how the terms will be used in normal text (not headlines).

Some spelling may be context specific. For example, when we are referring to
GUI elements, we usually spell them in the way, they are used in the GUI.

Additionally, there may be more than one term with the same meaning. Here, we list
the preferred term.

backend (noun)
   We usually do not capitalize this. This is not a specific TYPO3 thing.
   Fluid is capitalized, like Docker (see :ref:`spelling-proper-names`). Backend
   is a general thing, like any backend, any extension, any plugin or any car and not a 1953
   Chevy Corvette.

   Example: "when you log in to the backend ..."

   Note: Outside of the TYPO3 context, you will commonly also see spelling back-end
   or back end. These are not wrong,
   but in the TYPO3 context, we try to use consistent spelling, so stick to backend.

code sprint
   is commonly written in lowercase, see `Wikipedia: Hackathon
   <https://en.wikipedia.org/wiki/Hackathon#Code_sprints>`__

(the TYPO3) Core
   Example: "The TYPO3 Core comes with a number of icons that may be used in your extension."

Composer
   The same applies as for Docker. Use Composer unless you
   explicitly mean the command `composer`.

(the TYPO3) Core Team
   Should be capitalized.

(the TYPO3) Documentation Team
   Should be capitalized, unless it means *any* documentation team.

Docker
   The product Docker is a brand name and is capitalized, so use that
   unless you explicitly mean the command `docker` (see `Use the Docker command line
   <https://docs.docker.com/engine/reference/commandline/cli/>`__).

Edit me on GitHub workflow
   Use this to describe the workflow which involves editing on GitHub as
   opposed to "local editing and rendering with Docker".

extension
   See description for backend for explanation of why we use lowercase.

   Examples:

   *  "When you create documentation for your extension, make sure ..."
   * "... includes all TYPO3 extensions that are uploaded to TER"

Extension Manager
   Example: "Use the Extension Manager to activate an extension."

frontend
   See backend for explanation.

Git
   The same applies as for Docker. Use Git unless you explicitly mean the command
   line command `git`.

GitHub
   Exception: This is the official spelling.

Introduction Package
   Example: “The official TYPO3 Introduction Package is a great place to start”

Local editing and rendering with Docker
   is used to describe the workflow of editing locally.

reStructuredText
   This is an official spelling. Alternate word: **reST**, but this may be confused
   with REST. We commonly use reST within this document, because it is shorter and
   we assume you
   know we are not talking about REST here, but elsewhere, reStructuredText should
   be preferred.

sitepackage
   In the context of a TYPO3 sitepackage, a TYPO3 sitepackage extension or the sitepackage
   builder, we use the spelling sitepackage and not site package. 

system extension
   "system extension" is commonly used to describe an extension shipped with the
   core and located in the directory sysext in the file system. Alternate term
   "core extension" is discouraged
   (see `Issue on GitHub <https://github.com/TYPO3-Documentation/TYPO3CMS-Guide-HowToDocument/issues/47>`__).

TCA
   is an :ref:`acronym <spelling-acronyms>`.

third party extension
   Not a system extension maintained in the core, an extension publicly
   available. It is preferred to use "third party extension" and not "3rd party extension" (see
   `Issue on GitHub <https://github.com/TYPO3-Documentation/TYPO3CMS-Guide-HowToDocument/issues/38>`__
   for discussion).

TSconfig
   :ref:`TYPO3 exception <spelling-typo3>`

TYPO3
   :ref:`TYPO3 exception <spelling-typo3>`: TYPO3 is always spelled TYPO3.

TypoScript
   :ref:`TYPO3 exception <spelling-typo3>`

ViewHelper
   :ref:`TYPO3 exception <spelling-typo3>`


See also `Issue on GitHub <https://github.com/TYPO3-Documentation/TYPO3CMS-Guide-HowToDocument/issues/36>`__
for terms pending a decision.



.. _spelling-ref-title:

Title Spelling Reference
========================

This is a list of words and how they should be used in the title.

Most words are capitalized in the title. Exceptions are **articles,
prepositions** and **conjunctions** with less than 4 letters and a few
exceptions like acronyms (all caps) or words that use capital
letters within a word (e.g. stdWrap, TypoScript).


See :ref:`rules for title case <spelling-title-case>`.

These are only some examples,
more examples for lowercase spelling, see `TYPO3 Content Style Guide
<https://typo3.org/community/teams/content/writing-style-guide/#c8483>`__.

**Even if a word is lowercased in this list, it is always capitalized
if used as first or last word in title!**

a
   Rule #5: Article with less than 4 letters (lowercase)
Always
   Rule #3 and #4: 4 letters or more and adverb
an
   Rule #5: Article with less than 4 letters (lowercase)
and
   Rule #5: Conjunction with less than 4 letters (lowercase)
but
   Rule #5: Conjunction with less than 4 letters (lowercase)
for
   Rule #5: Preposition with less than 4 letters (lowercase)
He
   Rule #4: Pronoun
in
   Rule #5: Preposition with less than 4 letters (lowercase)
Is
   Rule #4: Verb
It
   Rule #4: Pronoun
Me
   Rule #4: Pronoun
or
   Rule #5: Conjunction with less than 4 letters (lowercase)
PHP
   Rule #1: Exception
She
   Rule #4: Pronoun
stdWrap
   Rule #1: Exception
the
   Rule #5: Article with less than 4 letters (lowercase)
Throughout
   Rule #3: 4 letters or more
TYPO3
   Rule #1: Exception: TYPO3 is always spelled TYPO3
TypoScript
   Rule #1: Exception
With
   Rule #3: 4 letters or more. Capitalized even though preposition.
Within
   Rule #3: 4 letters or more. Capitalized even though preposition.
Without
   Rule #3: 4 letters or more. Capitalized even though preposition.


Used Resources
==============

In addition to the TYPO3 Content Style Guide, some other resources have been used:

* "Don't use same word for 2 different meanings", see `RACKSPACE DEVELOPER DOCS:
  Use consistent terminology
  <https://developer.rackspace.com/docs/style-guide/terminology/general-term-guidelines/use-consistent-terms/>`__

capitalization

* *"The tendency towards lowercase, which in part reflects a less formal, less deferential society, has
  been accelerated by the explosion of the internet"*
  `Guardian and Observer Styleguide <https://www.theguardian.com/guardian-observer-style-guide-c>`__,
  look under capital.
  Note that these are British publications and we use American spelling.
* *"When referring to GUI elements, match the capitalization used in the interface."*, see
  `IBM developerWorks editorial style guide
  <https://www.ibm.com/developerworks/library/styleguidelines/index.html>`__
* `Stackexchange: Proper capitalization of commonly used acronyms
  <https://english.stackexchange.com/questions/51924/proper-capitalization-of-commonly-used-acronyms>`__
* `The Associated Press style guide will no longer capitalize 'internet'
  <https://www.theverge.com/2016/4/2/11352744/ap-style-guide-will-no-longer-capitalize-internet>`__
* `Wikipedia: English capitalization of proper nouns <https://en.wikipedia.org/wiki/Proper_noun#English_capitalization_of_proper_nouns>`__
* *"A proper noun is a noun directly associated with an entity and primarily used to refer to
  that entity, such as London, Jupiter, Sharon, or Microsoft, as distinguished from a common
  noun, which is a noun directly associated with a class of entities (city, planet, person,
  corporation) and primarily used to refer to instances of a specific class (a city, another
  planet, these persons, our corporation)"* (quote from `Wikipedia: Proper Noun
  <https://en.wikipedia.org/wiki/Proper_noun>`__)
* *"...  proper nouns are limited to single words only (possibly with the), while proper names
  include all proper nouns (in their primary applications) as well as noun phrases such as the
  United Kingdom, North Carolina"* (quote from `Wikipedia: Proper Names
  <https://en.wikipedia.org/wiki/Proper_noun#Proper_names>`__)

compound words

* `Wikipedia: English compound <https://en.wikipedia.org/wiki/English_compound>`__
