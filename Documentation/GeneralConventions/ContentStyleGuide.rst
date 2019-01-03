.. include:: ../Includes.txt
.. highlight:: rst

.. _content-styleguide:

==============================
Content Style Guide & Spelling
==============================

The authoritative style guide for writing official text for TYPO3 is `The TYPO3 Writing Style Guide
<https://typo3.org/community/teams/content/writing-style-guide/>`__ on typo3.org.

Please use the conventions defined in the style guide.

If the style guide does not define something specifically, use correct spelling in English language,
or rather American (US) language (see `Style Guide: Spelling
<https://typo3.org/community/teams/content/writing-style-guide/#c8483>`__).

Refer to the resources, which the style guide suggests, or use
`Merriam Webster (https://m-w.com) <https://www.merriam-webster.com/>`__ as last resort.

If in doubt, ask in Slack channel #typo3-documentation (see
:ref:`how-to-get-help` or contact
`the Content Group <https://typo3.org/community/teams/content/>`__).

If you found something missing here and you have researched the answer, please
add that information yourself. See "Edit me on Github", see :ref:`docs-contribute`
for more information about how to make changes to the documentation.

Menu and Clickpath Style
========================

If you describe something that needs to be selected from a menu or clicked one
after the other, use *>* as separator and style the text in italics:

Example: Select *File > Open*

Spelling Rules
==============

.. _spelling-title-case:

Rules for Title Case
--------------------

Basic rules (read in this order, use the first rule that applies):

#. Exceptions: Words with special spelling like TYPO3, TypoScript, PHP, stdWrap etc. are written the
   way they are commonly written.
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
   for the exceptions (e.g. TYPO3).

The rules for title case are based on the `TYPO3 Content Style Guide
<https://typo3.org/community/teams/content/writing-style-guide/#c8486>`__:

*"We capitalize all principal words of a title, including the first and
the last words. We do not capitalize articles, prepositions or conjunctions
that have* **fewer than four letters**, *such as a, an, and ..."*

Examples:

* *Is* is a verb. Though it is short, do capitalize it (rule #4), as in "This Is the End"
* *With* is a preposition with 4 letters, so it must be capitalized (rule #4): "Install With Composer"
* The first word is always capitalized (see rule #2), so *in* is capitalized here: "In the End"
* *In* is a preposition with fewer than 4 letters, so it is lowercased (rule #5): "Rules in the Style Guide"
* TYPO3 is always spelled TYPO3 (rule #1): "TYPO3 is Always Spelled TYPO3", "stdWrap", "Programming With PHP"


This applies to **all headers** on a page, not just the top level header (title).

In reST, headers are created by underlined / overlining with (`====`, `----`, etc.)
as described in :ref:`Headlines-and-sections`::

   =================
   This Is the Title
   =================

   This Is the Subheader
   =====================



.. _buttons:

Rules for Buttons
-----------------


The same rules as in the title apply to buttons: `Style Guide: Buttons
<https://typo3.org/community/teams/content/writing-style-guide/#c8487>`__


Rules for plain text
--------------------

Some exceptions to rules:

#. If the text refers to terms used in the GUI (e.g. a clickpath for selecting
   something from the menu is described, the spelling used in the GUI can be
   used, e.g. *File* -> *Open*

Common rules of the English language are applied:

#. If a word has special spelling, e.g. an acronym like PHP, this spelling is applied.
#. Special words like proper nouns and brand names are capitalized, e.g. Docker
#. Most other words are lowercased.

There are some edge cases and some terms are not spelled consistently in the same way
everywhere. Sometimes it also depends on the context. Capitalization may change over
the course of time, for example see `The Associated Press style guide will no longer capitalize 'internet'
<https://www.theverge.com/2016/4/2/11352744/ap-style-guide-will-no-longer-capitalize-internet>`__
In other texts, "internet" is still capitalized.

For this reason, we have put together a :ref:`spelling reference <styleguide-spelling-ref-plaintext>`
to mention some common
terms that may be difficult to spell or that are spelled differently in the TYPO3 context.


Proper Names, Brand Names
~~~~~~~~~~~~~~~~~~~~~~~~~

General rules of the English language apply here:

If `proper names <https://en.wikipedia.org/wiki/Proper_names>`__  or brand names are used in
normal text (not headlines), they are capitalized. These can be countries, names of people,
corporations or brand names.

Examples:

* "This manual is designed to be readable by someone with basic UNIX command-line skills, but no
  previous knowledge of **Git**.": because it is a brand name (quote from
  `Git User Manual <https://mirrors.edge.kernel.org/pub/software/scm/git/docs/user-manual.html>`__)
* **Wikipedia**
* **Europe**



Tools with Executables
~~~~~~~~~~~~~~~~~~~~~~

Some tools have a program, which you can run. For example, **Git** has the command line
tool `git`. In this case, we use the correct spelling of the command (lowercase), when
we are explicitly referring to the command `git`. In all other cases, we use capital
spelling Git, because it is a proper noun. 

The same goes for **Docker**, **Composer**, etc.


.. _spelling-acronyms:

Acronyms
~~~~~~~~

Often, acronyms are written with capital letters only. If terms are commonly spelled that
way, this is how we spell them as well, for example HTML, CMS, PHP or LTS.


.. _styleguide-preferred-terms:

Reference of Preferred Terms
============================

Here we list some common terms that are specifically used in TYPO3, almost like brand names.
We add it to this list if a specific term is to be preferred as opposed to one with very
similar, but not the same meaning.


system extension
    "System extension" is commonly used in core as opposed to "core extension"
    (see `Issue on GitHub <https://github.com/TYPO3-Documentation/TYPO3CMS-Guide-HowToDocument/issues/47>`__).

Pending decision:

* `"third party extension" or "community extension"
  <https://github.com/TYPO3-Documentation/TYPO3CMS-Guide-HowToDocument/issues/38>`__


.. _styleguide-spelling-ref:

Spelling Reference
==================

Here we list some terms that are often used in the documentation and might easily
be misspelled.

.. _styleguide-spelling-ref-plaintext:

Plain Text Spelling Reference
-----------------------------

The spelling here is how the terms will be used in normal text (not headlines).

Some spelling may be context specific. For example, when we are referring to
GUI elements, we usually spell them in the way, they are used in the GUI.

Additionally, there may be more than one term with the same meaning. Here, we list
the preferred term.


backend
   Example: "when you log in to the backend ..."
Composer
   The product Composer is a proper noun and is capitalized, so use that unless you
   explicitly mean the command `composer`.
(the) Core Team
   Should be capitalized.
(the) Documentation Team
   Should be capitalized, unless it means *any* documentation team.
Docker
   The product Docker is a proper noun and is capitalized, so use that
   unless you explicitly mean the command `docker` (see `Use the Docker command line
   <https://docs.docker.com/engine/reference/commandline/cli/>`__).
extension
   Examples:

   *  "When you create documentation for your extension, make sure ..."
   * "... includes all TYPO3 extensions that are uploaded to TER"
Git
   The same applies as for Docker. Use Git unless you explicitly mean the command
   line command `git`.
GitHub
   Exception: This is the official spelling.
reST
   Exception: This is an official spelling for reStructuredText
TYPO3
   Exception: TYPO3 is always spelled TYPO3.


See also `Issue on GitHub <https://github.com/TYPO3-Documentation/TYPO3CMS-Guide-HowToDocument/issues/36>`__
for terms pending a decision.

.. _styleguide-spelling-ref-title:

Title Spelling Reference
------------------------

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


Additionally Used Resources
===========================

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
* "When referring to GUI elements, match the capitalization used in the interface.", see
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
