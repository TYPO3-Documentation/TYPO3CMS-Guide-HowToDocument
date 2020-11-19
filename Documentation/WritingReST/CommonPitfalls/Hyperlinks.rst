.. include:: ../../Includes.txt
.. highlight:: rst


===================
Problems With Links
===================

There are several ways to write links, here we assume you are
using external links with the following syntax. For more information
see the :ref:`references <common-pitfalls-links-more-information>`
at the bottom on this page.

Correct Syntax
==============

::

   `anchor text <url>`__


Example:

::

   `T3O <https://typo3.org>`__

How this looks:

`T3O <https://typo3.org>`__


Common Mistake #1: Missing Space
================================

Make sure there is a space between the anchor text and the
opening `<`.

.. tip::

   To test this yourself right now, click on "Edit on GitHub" in the top right corner
   of this page, fix the errors, then use "Preview changes" to view the changes
   (you need a GitHub account for this, if you do not
   have an account, go to `https://github.com/join <https://github.com/join>`__).



Wrong Syntax
------------

::

   `T3O<https://typo3.org>`__


How this looks:


`T3O<https://typo3.org>`__


Common Mistake #2: Missing Undercore (_)
========================================

Missing `_` or `__` at the end:


Wrong Syntax
------------

::

   `T3O <https://typo3.org>`


How this looks:


`T3O <https://typo3.org>`


.. _common-pitfalls-links-more-information:

Additional Information
======================

*  :ref:`external-links`
