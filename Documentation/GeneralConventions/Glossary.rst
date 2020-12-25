.. include:: /Includes.rst.txt
.. highlight:: rst
.. index::
   Spelling; Reference
   Preferred terms
   Glossary
.. _preferred-terms:
.. _spelling-ref:
.. _spelling-ref-this-guide:

==============================================
Spelling reference, preferred terms & glossary
==============================================

This section has 3 goals:

*  Define the **spelling**. You can use this list to check how a special TYPO3 term is
   spelled
*  **Preferred terms**: Sometimes there are more terms for one thing, which basically
   mean the same thing, such as "third party extension" and "community extension.
   Here, we define the preferred term.
*  **Glossary**: Sometimes a term may have several different meanings. Here we also
   define the meaning for some difficult edge cases.

In this list, the terms in the header are spelled **exactly** as they should be spelled.
This means that the first word is sometimes lowercased. This is something you should not
usually do in the documentation. Always uppercase the first word in a title, header
or sentence.


.. important::

   The goal of this page is to give guidance for people editing the documentation
   (and other content, e.g. in the TYPO3 backend). It is not intended as a glossary
   for beginners.

backend (noun)
--------------

Spelling:
   Usually not capitalized. This is not specific to TYPO3. Fluid is capitalized, like
   Docker (see :ref:`spelling-proper-names`). Backend is a general thing, like any backend,
   any extension, any plugin or any car and not a 1953 Chevy Corvette.

   Example: "when you log in to the backend ..."

   Note: Outside of the TYPO3 context, you will also encounter spellings like back-end
   or back end. These are not wrong, but in the context of TYPO3, we try to use consistent
   spelling, so stick to backend.
   

cross-site scripting
--------------------

Spelling:
   Commonly written in lowercase with one dash between cross and site. See `Wikipedia: 
   Cross-site scripting <https://en.wikipedia.org/wiki/Cross-site_scripting>`__


code sprint
-----------

Spelling:
   Commonly written in lowercase. See `Wikipedia: Hackathon
   <https://en.wikipedia.org/wiki/Hackathon#Code_sprints>`__

(the TYPO3) Core
----------------

Spelling:
   Example: "The TYPO3 Core comes with a number of icons that may be used in your extension."

Composer
--------

Spelling:
   Use Composer unless you explicitly mean the command `composer` (see Docker for explanation).

(the TYPO3) Core Team
---------------------

Spelling:
   Capitalized.

Data Processor
--------------

Spelling:
   Capitalized: The Data Processor as used in FLUIDTEMPLATE is a common name, specific
   to TYPO3 and not just any old generic data processor.

(the TYPO3) Documentation Team
------------------------------

Spelling:
   Capitalized, unless it means *any* documentation team.

Docker
------

Spelling:
   The product Docker is a brand name and therefore capitalized, so use that
   unless you explicitly mean the command `docker` (see `Use the Docker command line
   <https://docs.docker.com/engine/reference/commandline/cli/>`__).

Edit on GitHub workflow
-----------------------

Preferred term:
   Use this to describe the workflow which involves editing on GitHub as
   opposed to "local editing and rendering with Docker".

Extbase
-------

Spelling:
   Capitalized. Adhering to the rule set of :ref:`spelling-proper-names`.

extension
---------

Spelling:
   See description for backend for an explanation of why we use lowercase.

   Examples:

   *  "When you create the documentation for your extension, make sure ..."
   *  "... includes all TYPO3 extensions that are uploaded to TER"

Extension Manager
-----------------

Spelling:
   Capitalized. Example: "Use the Extension Manager to activate an extension."

Flexform
--------

Spelling
   Flexform (singular), Flexforms (plural)


Fluid
-----

Spelling:
   Capitalized. The rule set of :ref:`spelling-proper-names`.

frontend
--------

Spelling:
   Usually not capitalized. See backend for an explanation.

Git
---

spelling:
   The same applies as for Docker. Use Git unless you explicitly mean the command
   line command `git`.

GitHub
------

Spelling:
   Exception: This is the official spelling.

Introduction Package
--------------------

Spelling:
   Example: “The official TYPO3 Introduction Package is a great place to start”

local editing and rendering with Docker
---------------------------------------

Preferred term:
   This phrase is used to describe the workflow of editing locally.

quick start
-----------


reStructuredText
----------------

Preferred term:
   This is the official spelling. Alternate word: **reST**, but this may be confused
   with REST(ful). We commonly use reST within this document, because it is shorter and
   we assume you know we are not talking about REST here, but elsewhere, reStructuredText
   should be preferred.

sitepackage
-----------

Preferred term:
   In the context of a TYPO3 sitepackage, a TYPO3 sitepackage extension or the sitepackage
   builder, we use the spelling sitepackage and not site package.

system extension
----------------

Preferred term:
   "system extension" is commonly used to describe an extension shipped with the
   core and located in the directory sysext in the file system. The alternate term
   "core extension" is discouraged
   (see `Issue on GitHub <https://github.com/TYPO3-Documentation/TYPO3CMS-Guide-HowToDocument/issues/47>`__).

TCA
----

Spelling
   TCA is an :ref:`acronym <spelling-acronyms>`. We capitalize it.

third party extension
---------------------

Preferred term:
   It is preferred to use "third party extension" and not "3rd party extension" (see
   `Issue on GitHub <https://github.com/TYPO3-Documentation/TYPO3CMS-Guide-HowToDocument/issues/38>`__
   for discussion).

Definition:
   Not a system extension maintained in the core, an extension publicly
   available.

TSconfig
--------

Spelling:
   :ref:`TYPO3 exception <spelling-typo3>`. Note the lowercase "c" after TS! Spelling TSConfig is sometimes
   used, but it should be **TSconfig!**

TYPO3
-----

Spelling:
   :ref:`TYPO3 exception <spelling-typo3>`: TYPO3 is always spelled TYPO3.

TypoScript
----------

Spelling:
   :ref:`TYPO3 exception <spelling-typo3>`

ViewHelper
----------


Spelling:
   :ref:`TYPO3 exception <spelling-typo3>`


More information
----------------

*  See `Issue on GitHub <https://github.com/TYPO3-Documentation/TYPO3CMS-Guide-HowToDocument/issues/36>`__
   for discussion about spelling.
*  See open issue about `Clarifying terms <https://github.com/TYPO3-Documentation/T3DocTeam/issues/77>`__
*  Open related issue
   `Several changes for making TYPO3 concepts easier to understand for new users <https://github.com/TYPO3-Documentation/T3DocTeam/issues/120>`__
