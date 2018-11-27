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

Refer to the resources, which the style guide suggests, or Merriam Webster as last resort:
`https://m-w.com <https://www.merriam-webster.com/>`__


.. _title-case:

Title Case
==========

*"We capitalize all principal words of a title, including the first and
the last words. We do not capitalize articles, prepositions or conjunctions
that have* **fewer than four letters**, *such as a, an, and ..."*
(`Style Guide: Title Case <https://typo3.org/community/teams/content/writing-style-guide/#c8486>`__)

The first word is always capitalized, as in "**A** Good Thing".

Capitalize
   This means: The first letter of a word  is capitalized. Example: "**Not** now, not **Never**".

Principal word
   This means: Words with meaning, that don't just glue other words together (e.g. "a" is not
   a principal word, "walk" is)

This applies to all headers on a page, not just the top level header (title).

In reST, headers are created by underlined / overlining with (`====`, `----`, etc.)
as described in :ref:`Headlines-and-sections`::

   =================
   This is the Title
   =================

   This is the Subheader
   =====================

Tools:

* https://titlecaseconverter.com/
* https://capitalizemytitle.com/


.. _buttons:

Buttons
=======


The same rules as in the title apply to buttons: `Style Guide: Buttons
<https://typo3.org/community/teams/content/writing-style-guide/#c8487>`__


Spelling of proper nouns
========================

If `proper nouns <https://en.wikipedia.org/wiki/Proper_noun>`__ are used in
normal text (not headlines), they are capitalized.

Sometimes, it is not so easy to determine, how to spell something, e.g. is it
a style guide, or **the** Style Guide? Is it an extension or *the* TYPO3
bootstrap_package Extension? Is the backend? Or the Backend? Or a Backend user
or a backend user?

If in doubt, ask in Slack channel #typo3-documentation (see
:ref:`how-to-get-help` or contact
`The Content Group <https://typo3.org/community/teams/content/>`__).

If you found something missing here and you have researched the answer, please
add that information yourself. See "Edit me on Github", see :ref:`docs-contribute`
for more information about how to make changes to the documenation.

Here we list some proper nouns (we often use in documentation) and how they are
used in normal text (not headlines).

CMS
   As in content management system.
(the) Documentation Team
    Should be capitalized, unless it means *any* documentation team.
reST
   This is the official abbreviation for reStructuredText
TYPO3
   TYPO3 is always spelled TYPO3.


This may be the opposite of what some spellcheckers say, because they do not know
these proper nouns, e.g. try to use TYPO3 or reST on  https://capitalizemytitle.com/.

Tools with executables
----------------------

Some tools have a program, which you can run. For example, **Git** has the command line
tool git. In this case, we use the correct spelling of the command (lowercase), when
we are explicitly referring to the command git. In all other cases, we use capital
spelling Git. The same goes for **Docker**, **Composer**, etc.


Composer
    The product Composer is a proper noun and is capitalized, so use that unless you explicitly mean the command composer.
Docker
   The product Docker is a proper noun and is capitalized, so use that
   unless you explicitly mean the command docker (see `Use the Docker command line
   <https://docs.docker.com/engine/reference/commandline/cli/>`__).
Git
   The same applies as for docker. Use Git unless you explicitly mean the command
   line command git.
