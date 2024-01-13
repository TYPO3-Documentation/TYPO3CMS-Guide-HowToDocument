.. include:: /Includes.rst.txt
.. index:: reST; Hyperlinks
.. highlight:: rst

===================
Problems with links
===================

There are several ways to write links, here we assume you are
using external links with the following syntax. For more information
see the :ref:`references <common-pitfalls-links-more-information>`
at the bottom on this page.

Correct syntax
==============

..  code-block:: rst

    `anchor text <url>`__


Example:

..  code-block:: rst

   `T3O <https://typo3.org>`__

How this looks:

`T3O <https://typo3.org>`__


Common mistake #1: Missing space
================================

Make sure there is a space between the anchor text and the
opening `<`.


Wrong syntax
------------

..  code-block:: rst

    Wrong: `T3O<https://typo3.org>`__

    Correct: `T3O <https://typo3.org>`__


Common mistake #2: Missing underscore (_)
=========================================

Missing `_` or `__` at the end:


Wrong Syntax
------------

..  code-block:: rst

   Wrong: `T3O <https://typo3.org>`

   Correct: `T3O <https://typo3.org>`__


.. _common-pitfalls-links-more-information:

Additional information
======================

*  :ref:`external-links`
