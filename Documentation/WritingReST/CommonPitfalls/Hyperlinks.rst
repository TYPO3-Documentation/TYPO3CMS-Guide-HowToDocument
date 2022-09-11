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

..  code-block:: rest

   `anchor text <url>`__


Example:

..  code-block:: rest

   `T3O <https://typo3.org>`__

How this looks:

`T3O <https://typo3.org>`__


Common mistake #1: Missing space
================================

Make sure there is a space between the anchor text and the
opening `<`.

.. tip::

   To test this yourself right now, click on "Edit on GitHub" in the top right corner
   of this page, fix the errors, then use "Preview changes" to view the changes
   (you need a GitHub account for this, if you do not
   have an account, go to https://github.com/join).



Wrong syntax
------------

..  code-block:: rest

   `T3O<https://typo3.org>`__


How this looks:


`T3O<https://typo3.org>`__


Common mistake #2: Missing underscore (_)
=========================================

Missing `_` or `__` at the end:


Wrong Syntax
------------

..  code-block:: rest

   `T3O <https://typo3.org>`


How this looks:


`T3O <https://typo3.org>`


.. _common-pitfalls-links-more-information:

Additional information
======================

*  :ref:`external-links`
