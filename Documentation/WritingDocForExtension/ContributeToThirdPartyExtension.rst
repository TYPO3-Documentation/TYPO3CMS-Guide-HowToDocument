.. include:: /Includes.rst.txt
.. highlight:: rst
.. index:: pair: Documentation; Third-party extensions
.. _contribute-to-3rdparty-extension:

====================================
Contribute to third-party extensions
====================================

This chapter addresses contributing to third party extension documentation.

For system extensions, see :ref:`contribute-to-system-extension`.

You can contribute to the documentation of any publicly available extension,
if the repository is public (for example hosted on GitHub). This does not mean, the
extension author will be willing or is obligated to merge your change. But, most
of the time, useful contributions are welcome.

You can add issues or make changes via patches (for example pull requests on GitHub).

If you can make the change yourself, try to submit it as a patch instead of
just writing an issue. It depends on the policy of the extension author
(see contribution guide for specific repository, if available), but
it is usually not required to write an issue. You can just submit a pull request
(PR) directly.


.. _contribute-to-3rdparty-extension-find-the-source:

Find the Source
===============

First, you need to find out where the source is maintained. Usually, this will
be a repository on GitHub. There, you can also check if documentation is already
available. It should be a `Documentation` folder or one of the alternatives
mentioned in :ref:`file-structure-general`.

To find the repository, use one of these methods:


Method 1: Find the Source on docs.typo3.org
-------------------------------------------

In the page of the rendered docs for the extension, click on :guilabel:`Repository`
in the footer.

Sometimes the metadata in Settings.cfg in a Documentation
project is not filled out and this link is missing. Then, you can use Method 2.


Method 2: Find the Source on https://extensions.typo3.org
---------------------------------------------------------

.. rst-class:: bignums

   1. Go to the `extension repository <https://extensions.typo3.org/>`__

   2. In the search box, enter the name or extension key

   3. Select the extension


      .. image:: /Images/ter_news2.png
         :alt: Link: Show manual
         :target: https://extensions.typo3.org/?L=0&id=1&tx_solr%5Bq%5D=news
         :class: with-shadow
         :width: 600px

   4. Click take a look in the code

      .. image:: /Images/take-a-look-in-the-code.png
         :alt: Link: Take a look in the code
         :target: https://github.com/georgringer/news
         :class: with-shadow

You cannot find system extensions (extensions that are maintained in
the core) on https://extensions.typo3.org. System extensions are for
example indexed_search, form, impexp, etc.


.. index:: Third-party extensions; Find the manual

Find the rendered manual
========================

You can also find the rendered documentation:

Method 1: Find rendered manual on docs.typo3.org
------------------------------------------------

Go to:
`Extensions by extension key <https://docs.typo3.org/typo3cms/extensions/Index.html>`__

Method 2: Find rendered manual on https://extensions.typo3.org
--------------------------------------------------------------

.. rst-class:: bignums

   1. Go to the `Extension repository <https://extensions.typo3.org/>`__

   2. In the search box, enter the name or extension key

   3. Click on "Show Manual"

      .. image:: /Images/ter_news.png
         :alt: Link: Show manual
         :target: https://docs.typo3.org/typo3cms/extensions/news/
         :class: with-shadow
         :width: 600px

.. note::

   You cannot find system extensions (extensions that are maintained in
   the core) on https://extensions.typo3.org.


.. index::
   Third-party extensions; Contribution guide
   Files; CONTRIBUTING.md

Follow the contribution guide
=============================

Hopefully, the extension has a contribution guide. You can look at the GitHub
help pages to check for `conventions for contribution guides
<https://help.github.com/articles/setting-guidelines-for-repository-contributors/>`__.

In the GitHub repository, you should find a file like:

*  CONTRIBUTING.md
*  .github/CONTRIBUTING.md
*  etc.

If no contribution guide exists, follow the general conventions for TYPO3 documentation
and conventions for creating pull requests on GitHub or contact the author.
