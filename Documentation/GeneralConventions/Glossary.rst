.. include:: /Includes.rst.txt
.. highlight:: rst
.. index::
   Spelling; Reference
   Preferred terms
   Glossary
.. _preferred-terms:
.. _spelling-ref:
.. _spelling-ref-this-guide:

============================
Spelling, terms and glossary
============================

.. index:: pair: Text role; pn (proper name)

Feel free to use the `pn` (proper name) text role to mark up special names
like `TYPO3 Core Team`:pn: when it's desirable to make them clearly visible.
The recommended reST source for this is:

.. code-block:: rst

   `TYPO3 Core Team`:pn:

Put `:pn:` to the end of the text. This facilitates reading the source.
Currently the 'pn' text role is defined in file :file:`Includes.rst.txt`. It is
a derivative of 'emphasis' and shown in italics. We are free to change that in
our theme. A future Sphinx will be able to automatically create a sorted list
of all proper names used.


Spelling
========

.. default-role:: guilabel

Pick the spelling and recommended terms from this list.


A

`Apache`,
`API`,


B

`backend`,
`blog post`, `blogger`, `blogging`,


C

`code sprint`,
`Composer`,
`Core Team`, `TYPO3 Core Team`,
`Core`, `TYPO3 Core`
`cross-site scripting`,
`Crowdin`,
`CSV`, `comma separated values`,


D

`Data Processor`,
`DBAL`
`Docker`,
`Docker Compose`,
`Doctrine`
`Documentation Team`, `TYPO3 Documentation Team`,
`DataHandler`,


E

`Edit on GitHub`,
`Edit on GitHub button`,
`Edit on GitHub workflow`,
`Extbase`
`Extension Manager`
`extension`,


F

`FlexForm`,
`Fluid`,
`FormEngine`,
`frontend`,
`frontend rendering`,


G

`Git`,
`GitHub`,


H

`how to document`,
`how-to`, `a how-to video`,


I

`InnoDB`,
`Introduction Package`,

L

`LinkHandler`,
`Linux`,

M

`Markdown`,
`mark up the text`,
`markup (the)`,
`MariaDB`,
`MySQL`,
`MacOs`, outdated: `Mac`, `Mac OS X`,
`model-view-controller`,
`MVC`,

N

`nginx`

O

`Open Source`,

P

`page TSconfig`,
`PNG`,
`PostgreSQL`

Q

`quick start`,


R

`reStructuredText`, `reST`,


S

`sitepackage`,
`Sphinx`
`style guide (en)`, `Styleguide (de)`, 
`SVG`,
`system extension`, not: 'sys extension', `core extension`


T

`TCA`,
`TCE`,
`TCEforms`,
`TCEmain`,
`textrole`,
`third party extension`,
`toctree`,
`TSconfig`,
`TYPO3`,
`TYPO3 Core`, `Core`,
`TYPO3 Core Engine`, 
`TYPO3 Core Team`, `Core Team`,
`TYPO3 Core Engine`
`TypoScript`,

U

`UNIX`,

V

`ViewHelper`

W

`Windows`, `Microsoft Windows`,
`windows`, `modal windows`,



.. default-role:: php



Terms
=====

How to use these terms:

reStructuredText
   Use 'reST' as abbreviation.

TYPO3
   Always and everywhere written with capital letters.

third party extension
   Do not write "3rd party extension".

ViewHelper
   Our community agreed on this spelling.



Glossary
========

.. https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#glossary
.. Creating a glossary with terms that you can refer to - obtaining a link.

What terms mean:

.. glossary::

   third party extension
      Any extension that is not part of the `TYPO3 Core`:pn:

   TYPO3 CMS
      The TYPO3 content management system.

   TYPO3 Core Team
      This is the team that drives the development of the `TYPO3 Core`:pn:.


.. Example usage of :term:
..
..    The :term:`TYPO3 Core Team` is very busy but is not responsible for
      any :term:`third party extension`.


.. See `Issue on GitHub
   <https://github.com/TYPO3-Documentation/TYPO3CMS-Guide-HowToDocument/issues/36>`__
   for discussion about spelling.

.. See open issue about `Clarifying terms
   <https://github.com/TYPO3-Documentation/T3DocTeam/issues/77>`__

.. Open related issue `Several changes for making TYPO3 concepts easier
   to understand for new users
   <https://github.com/TYPO3-Documentation/T3DocTeam/issues/120>`__

