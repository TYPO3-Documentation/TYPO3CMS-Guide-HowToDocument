.. include:: /Includes.rst.txt
.. highlight:: rst
.. index::
   Spelling, Terms, Glossary
.. _preferred-terms:
.. _spelling-ref:
.. _spelling-ref-this-guide:

============================
Spelling, terms and glossary
============================

.. index:: pair: Text role; pn (proper name)

*Very much recommended:* Make use of text role `pn` (proper name) to point out
that some special spelling is applied due to a proper name like
`TYPO3 Core Team`:pn:. The recommended way for markup is:

.. code-block:: rst

   `TYPO3 Core Team`:pn:

Having `:pn:` at then end facilitates reading. In future Sphinx will be able
to automatically create a list of all proper names used in a manual.

Currently the 'pn' textrole is defined in file :file:`Includes.rst.txt`. It is
a derivative of 'emphasis' and rendered in html as `<em class="pn">`. Visual
appearance is italics, but that may changed in future.


Spelling
========

.. default-role:: guilabel

Pick the spelling and recommended terms from this list.


B

`backend`,


C

`code sprint`,
`Composer`,
`Core Team`, `TYPO3 Core Team`,
`Core`, `TYPO3 Core`
`cross-site scripting`,


D

`Data Processor`,
`Docker`,
`Documentation Team`, `TYPO3 Documentation Team`,


E

`Edit on GitHub`,
`Edit on GitHub button`,
`Edit on GitHub workflow`,
`Extbase`
`Extension Manager`
`extension`,


F

`Flexform`,
`Flexforms`,
`Fluid`,
`frontend`,


G

`Git`,
`GitHub`,


I

`Introduction Package`,

M

`mark up the text`,
`markup (the)`,

Q

`quick start`,


R

`reStructuredText`, `reST`,


S

`sitepackage`,
`system extension`,


T

`TCA`,
`textrole`,
`third party extension`,
`TSconfig`,
`TYPO3 Core Team`, `Core Team`,
`TYPO3 Core`, `Core`,
`TYPO3`,
`TypoScript`


V

`ViewHelper`



.. default-role:: php



Terms
=====

Worth knowing about some of the terms:

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

.. glossary::

   third party extension
      …

   TYPO3 CMS
      The TYPO3 content management system.

   TYPO3 Core Team
      This is the team that drives the development of the TYPO3 `Core`:pn:.

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

