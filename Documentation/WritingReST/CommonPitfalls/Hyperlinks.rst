.. include:: ../../Includes.txt
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

::

   `anchor text <url>`__


Example:

::

   `T3O <https://typo3.org>`__

How this looks:

   `T3O <https://typo3.org>`__


Common mistake #1: Missing space
================================

Make sure there is an extra space between the anchor text and the
opening `<`.

.. tip::

   To test this yourself right now, click on "Edit me on Github" in the top right corner
   of this page, fix the errors, then use "Preview changes" to view the changes
   (you need a Github account for this, if you do not
   have an account, go to `https://github.com/join <https://github.com/join>`__).



Wrong syntax
------------

::

   `T3O<https://typo3.org>`__


How this looks:


   `T3O<https://typo3.org>`__


Common mistake #2: Missing undercore (_)
========================================

Missing `_` or `__` at the end:


Wrong syntax
------------

::

   `T3O <https://typo3.org>`


How this looks:


   `T3O <https://typo3.org>`


.. _common-pitfalls-links-more-information:

More information
================

* :ref:`external-links`
