.. include:: ../Includes.txt
.. highlight:: rst

.. _contribute-to-3rdparty-extension:

================================
Contribute to 3rdparty extension
================================


.. _contribute-to-3rdparty-extension-find-the-source:

Find the source (repository)
============================

First, you need to find out, where the source is maintained. Usually, this will
be a repository on Github. There, you can also check if documentation is already
available. It should be a `Documentation` folder or one of the alternatives
mentioned in :ref:`supported-filenames-and-formats`.

To find the repository, use one of these methods:

Method 1: Find the source with "Related links"
----------------------------------------------

In the page of the rendered docs for the extension, click on "Related links", and
then "Repository"

Method 2: Find the source on https://extensions.typo3.org
---------------------------------------------------------

.. rst-class:: bignums

   1. Go to the `Extension repository <https://extensions.typo3.org/>`__

   2. In the search box, enter the name or extension key

   3. Select the extension


      .. image:: ../images/ter_news2.png
         :alt: Link: Show manual
         :target: https://extensions.typo3.org/?L=0&id=1&tx_solr%5Bq%5D=news
         :class: with-shadow
         :width: 600px

   4. Click take a look in the code

      .. image:: ../images/take-a-look-in-the-code.png
         :alt: Link: Take a look in the code
         :target: https://github.com/georgringer/news
         :class: with-shadow

.. note::

   You cannot find system extensions (extensions that are maintained in 
   the core) on https://extensions.typo3.org. System extensions are for
   example indexed_search, form, impexp, etc. 


Find the rendered manual
========================

You can also find the rendered documentation:

Method 1: Find rendered manual on docs.typo3.org
------------------------------------------------

Is it a system extension? Go to 
`Core extensions <https://docs.typo3.org/typo3cms/SystemExtensions/Index.html>`__

Is it a 3rdparty extension? Go to 
`Extensions by extension key <https://docs.typo3.org/typo3cms/extensions/Index.html>`__

Method 2: Find rendered manual on https://extensions.typo3.org
--------------------------------------------------------------

.. rst-class:: bignums

   1. Go to the `Extension repository <https://extensions.typo3.org/>`__

   2. In the search box, enter the name or extension key

   3. Click on "Show Manual"

      .. image:: ../images/ter_news.png
         :alt: Link: Show manual
         :target: https://docs.typo3.org/typo3cms/extensions/news/
         :class: with-shadow
         :width: 600px

.. note::

   You cannot find system extensions (extensions that are maintained in 
   the core) on https://extensions.typo3.org. 

Follow contribution guide
=========================

Hopefully, the extension has a contribution guide. You can look at the Github
help pages to check for `conventions for contribution guides
<https://help.github.com/articles/setting-guidelines-for-repository-contributors/>`__.

In the Github repository, you should find a file like:

* CONTRIBUTING.md
* .github/CONTRIBUTING.md
* etc.

If no contribution guide exists, follow the general conventions for TYPO3 documentation
and conventions for creating Pull Requests on Github or contact the author.
