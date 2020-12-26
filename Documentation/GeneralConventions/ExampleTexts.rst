.. include:: /Includes.rst.txt
.. highlight:: rst

.. todo:: Add more boilerplate texts for other content types, e.g. tutorials, guides ...

.. _exampleTexts:

========
Examples
========

This is information about example texts and structure for **official
documentation** on the start page, in the menu etc. Extension
authors are free to do it differently, but using the same conventions
across all documentation on docs.typo3.org should make it easier for
users to find things quickly.

.. contents:: On this page:
   :local:
   :depth: 1


.. _example-start-page:

Start page
==========

For an example start page, see :ref:`t3tca:start`.

The following should be on the start page, typically in this order:

*  *required*: Title
*  *optional*: Quick links (as button style)
*  *required*: Description
*  *required*: Meta information, including language, author, license
   (required) and status, target audience etc. (optional)

   *  The author can contain a link to a section "Credits". If the
      author is "Documentation Team", it should be a link to the
      docs team page on typo3.org, not a link to the email address.

*  *required*: Link to sitemap (as button style)

*  *required*: (in sidebar with title "Contributors:") Link to
   information about contribution, link targets and the shortcut.

*  *required*: Official documentation.
*  *required*: Manual type, e.g. "Core Manual", "Tutorial", etc.
*  *optional*: Credits section and link to contributors on GitHub
*  *optional*: Short information about contribution (this should be
   very general so we do not have to change it often). This can be
   omitted as we already have the link to information about
   contribution in the sidebar.

Example texts
-------------

Author
~~~~~~

"Core Team and TYPO3 Community (see credits)"

* credits is link to credits section

License
~~~~~~~

"Open Publication License available from http://www.opencontent.org/openpub/"

*  This is the *old* license which should be maintained for the manuals that
   already use it.

"Creative Commons (`CC BY-NC-SA 4.0 <https://creativecommons.org/licenses/by-nc-sa/4.0/>`__)"

.. seealso::

   * :ref:`licenses`

Official documentation
~~~~~~~~~~~~~~~~~~~~~~

"This document is included as part of the official TYPO3 documentation."

Core Manual
~~~~~~~~~~~

"This document is a Core Manual. Core Manuals address the built in functionality
of TYPO3 and are designed to provide the reader with in- depth information.
Each Core Manual addresses a particular process or function and how it is
implemented within the TYPO3 source code. These may include information on
available APIs, specific configuration options, etc.

Core Manuals are written as reference manuals. The reader should rely on the
Sitemap to identify what particular section will best address the task at hand."


Credits
~~~~~~~

"The original ... was written by ....
Subsequent versions have been updated by ....
... maintained this document over time,
see the `list of contributors <https://github.com/TYPO3-Documentation/TYPO3CMS-Guide-HowToDocument/graphs/contributors>`__
on GitHub.

A big “Thank You!” goes to every single one of them."

Contribution
~~~~~~~~~~~~

"For general questions about the documentation get in touch with the
`Documentation Team <https://typo3.org/community/teams/documentation>`__.

If you find a bug in this manual, please do not be afraid to suggest a fix,
e.g. by using the “Edit on GitHub” button in the top right corner.
Alternatively you can file an issue."


Change history
--------------

These are some changes that we made for the following reasons:

*  **description** is now above the metadata and not within it because
   it very easily got overlooked there and shouuld stand out more
*  **Last rendered**, **version**, **copyright** and some others
   have been removed because they are already displayed in the footer
*  **Link to Link targets** is now on the start page because it has
   been removed in the menu. It should be in a box (sidebar) with
   title "Contributors"

See `decision: Proposal for documentation manual start page <https://decisions.typo3.org/t/proposal-for-documentation-manual-start-page/668>`__

.. index:: 
   Documentation; Link targets
   Files; Targets.rst

Link targets
============

Official documentation manuals should contain a file :file:`Documentation/Targets.rst`
with the following content:

.. literalinclude:: ../Targets.rst
   :language: rst


.. exapmle-menu::

Menu
====

*  *required*: Should contain "Sitemap", typically as last item
*  Should not contain "Linktargets". There should be a link to the link targets
   on the start page as described above. The filename should be
   :file:`Documentation/Targets.rst`.
