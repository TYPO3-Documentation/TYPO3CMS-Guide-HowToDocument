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

.. _title-case:

Rules for Title Case
--------------------

Summary of basic rules:

#. First and last word of title is always capitalized.
#. Capitalize all important words (nouns, `pronouns <https://en.wikipedia.org/wiki/Pronoun>`__, 
   adjectives, verbs, adverbs, and subordinate conjunctions).
#. Lowercase `articles <https://en.wikipedia.org/wiki/Article_(grammar)>`__ (e.g. a, an, the)
  `prepositions <https://en.wikipedia.org/wiki/Preposition_and_postposition>`__
  (e.g. in, from, with) and `conjunctions <https://en.wikipedia.org/wiki/Conjunction_(grammar)>`__
  (e.g. and, or) **with fewer than 4 letters**. These types of words with 4 or more letters are capitalized.
#. Exceptions: Words with special spelling like TYPO3, PHP, stdWrap etc. are written the
  way they are commonly written.

Capitalize means: The first letter of a word  is a capital letter. Example: **England** is capitalized, 
**the** is not.

The rules for title case are based on the TYPO3 Style guide. The title capitalization rules
in the TYPO3 Style Guide are based on common other style guides like Chicago Manual of Style. 

You can use the tool https://capitalizemytitle.com/ to check the title. Choose "Default" and
"Title Case" for correct spelling in title. The result may slightly deviate from our rules
only for the above mentioned articles, prepositions or conjunctions with 4 letters and more
and for the exceptions (e.g. TYPO3).

Examples:
* *Is* is a verb. Though it is short, do capitalize it (rule 2), as in "This Is the End"
* *With* is a preposition with 4 letters, so it must be capitalized (rule 3): "Install With Composer"
* The first word is always capitalized (see rule 1), so *in* is capitalized here: "In the End"
* *In* is a preposition with fewer than 4 letters, so it is usually lowercased (rule 3): "Rules in the Style Guide"
* TYPO3 is always spelled TYPO3 (rule 4): "TYPO3 is always spelled TYPO3", "stdWrap", "Programming with PHP"

Words capitalized in title (most words are capitalized, these are only some examples):
* With (rule 3, 4 characters or more)
* Throughout
* Is (verb, rule 2)
* It (pronoun, rule 2)
* He
* She

Words lowercased in title (except if it is the first or last word):
* a (article with less than 4 characters, rule 3)
* an
* the
* in (preposition with less than 4 characters, rule 3)
* and
* or

*"We capitalize all principal words of a title, including the first and
the last words. We do not capitalize articles, prepositions or conjunctions
that have* **fewer than four letters**, *such as a, an, and ..."*
(`Style Guide: Title Case <https://typo3.org/community/teams/content/writing-style-guide/#c8486>`__)


This applies to **all headers** on a page, not just the top level header (title).

In reST, headers are created by underlined / overlining with (`====`, `----`, etc.)
as described in :ref:`Headlines-and-sections`::

   =================
   This Is the Title
   =================

   This Is the Subheader
   =====================

Additional Information:
   * `Style Guide: Title Case <https://typo3.org/community/teams/content/writing-style-guide/#c8486>`__


.. _buttons:

Rules for Buttons
-----------------


The same rules as in the title apply to buttons: `Style Guide: Buttons
<https://typo3.org/community/teams/content/writing-style-guide/#c8487>`__


Rules for plain text
--------------------



Proper Names, Brand Names
~~~~~~~~~~~~~~~~~~~~~~~~~

General rules of the English language apply here:

* If `proper names <https://en.wikipedia.org/wiki/Proper_names>`__  or brand names are used in
  normal text (not headlines), they are capitalized.

Proper Noun:
   *"A proper noun is a noun directly associated with an entity and primarily used to refer to
   that entity, such as London, Jupiter, Sharon, or Microsoft, as distinguished from a common
   noun, which is a noun directly associated with a class of entities (city, planet, person, 
   corporation) and primarily used to refer to instances of a specific class (a city, another 
   planet, these persons, our corporation)"* (quote from `Wikipedia: Proper Noun 
   <https://en.wikipedia.org/wiki/Proper_noun>`__)
Proper Name:
   *"...  proper nouns are limited to single words only (possibly with the), while proper names
   include all proper nouns (in their primary applications) as well as noun phrases such as the
   United Kingdom, North Carolina"* (quote from `Wikipedia: Proper Names 
   <https://en.wikipedia.org/wiki/Proper_noun#Proper_names>`__)
Brand Name:
   This is the name of a brand, e.g. the car model **Corvette**, VW **Volkswagen**, Renault **Clio** or 
   Toyota **Prius**.


Examples: 

* "This manual is designed to be readable by someone with basic UNIX command-line skills, but no
  previous knowledge of **Git**.": because it is a brand name (quote from `Git User Manual <https://mirrors.edge.kernel.org/pub/software/scm/git/docs/user-manual.html>`__)
* **Wikipedia**: brand name
* **English**: because it is derived from the proper name England (a country)

Additional information:

* `Wikipedia: English capitalization of proper nouns <https://en.wikipedia.org/wiki/Proper_noun#English_capitalization_of_proper_nouns>`__

Tools with Executables
~~~~~~~~~~~~~~~~~~~~~~

Some tools have a program, which you can run. For example, **Git** has the command line
tool git. In this case, we use the correct spelling of the command (lowercase), when
we are explicitly referring to the command git. In all other cases, we use capital
spelling Git, because it is a proper noun. 

The same goes for **Docker**, **Composer**, etc.

Additional Information:

* `StackOverflow: Spelling for Git <https://stackoverflow.com/a/37418911/2444812>`__


.. _spelling-acronyms:

Acronyms
~~~~~~~~

Often, acronyms are written with capital letters only. If terms are commonly spelled that
way, this is how we spell them as well, for example HTML, CMS, PHP or LTS.

Additional information:

* `Stackexchange: Proper capitalization of commonly used acronyms 
  <https://english.stackexchange.com/questions/51924/proper-capitalization-of-commonly-used-acronyms>`__



.. _styleguide-spelling-ref:

Spelling Reference
==================

Here we list some terms that are often used in the documentation and might easily
be misspelled.

The spelling here is how they will be used in normal text (not headlines).

backend
   Example: "when you log in to the backend ..."
Composer
   The product Composer is a proper noun and is capitalized, so use that unless you
   explicitly mean the command composer.
(the) Core Team
   Should be capitalized.
(the) Documentation Team
   Should be capitalized, unless it means *any* documentation team.
Docker
   The product Docker is a proper noun and is capitalized, so use that
   unless you explicitly mean the command docker (see `Use the Docker command line
   <https://docs.docker.com/engine/reference/commandline/cli/>`__).
extension
   Example: "When you create documentation for your extension, make sure ..."
Git
   The same applies as for docker. Use Git unless you explicitly mean the command
   line command git.
reST
   This is the official abbreviation for reStructuredText
TYPO3
   TYPO3 is always spelled TYPO3.


This may be different from what some spellcheckers say, because they do not know
these terms (e.g. TYPO3).




