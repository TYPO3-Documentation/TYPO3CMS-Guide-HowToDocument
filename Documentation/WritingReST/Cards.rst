.. include:: /Includes.rst.txt
.. highlight:: rst
.. index::
   reST; Cards
.. _restContentCards:

=====
Cards
=====

A content element that nicely supports grouping deep links by category: cards.

It can be used as portal-like overview page in extensive extensive extension
documentation

Simple cards
============

.. code-block:: rst

   .. container:: row m-0 p-0

      .. container:: col-md-6 pl-0 pr-3 py-3 m-0

         .. container:: card px-0 h-100

            .. rst-class:: card-header h3

               .. rubric:: :ref:`Concepts <t3start:Concepts>`

            .. container:: card-body

               Written for new users, this chapter introduces some of TYPO3s
               core concepts including the backend, TYPO3s administration
               interface.

      .. container:: col-md-6 pl-0 pr-3 py-3 m-0

         .. container:: card px-0 h-100

            .. rst-class:: card-header h3

               .. rubric:: :ref:`System Requirements <t3start:System-Requirements>`

            .. container:: card-body

               System requirements for the host operation system, including
               its web server and database and how they should be configured
               prior to installation.

      .. container:: col-md-6 pl-0 pr-3 py-3 m-0

         .. container:: card px-0 h-100

            .. rst-class:: card-header h3

               .. rubric:: :ref:`Installation <t3start:Install>`

            .. container:: card-body

               The installation chapter provides detailed instructions
               about how to install TYPO3, it also contains information about
               how to deploy TYPO3 to a production environment.

Rendered it looks like this:

.. container:: row m-0 p-0

   .. container:: col-md-6 pl-0 pr-3 py-3 m-0

      .. container:: card px-0 h-100

         .. rst-class:: card-header h3

            .. rubric:: :ref:`Concepts <t3start:Concepts>`

         .. container:: card-body

            Written for new users, this chapter introduces some of TYPO3s
            core concepts including the backend, TYPO3s administration
            interface.

   .. container:: col-md-6 pl-0 pr-3 py-3 m-0

      .. container:: card px-0 h-100

         .. rst-class:: card-header h3

            .. rubric:: :ref:`System Requirements <t3start:System-Requirements>`

         .. container:: card-body

            System requirements for the host operation system, including
            its web server and database and how they should be configured
            prior to installation.

   .. container:: col-md-6 pl-0 pr-3 py-3 m-0

      .. container:: card px-0 h-100

         .. rst-class:: card-header h3

            .. rubric:: :ref:`Installation <t3start:Install>`

         .. container:: card-body

            The installation chapter provides detailed instructions
            about how to install TYPO3, it also contains information about
            how to deploy TYPO3 to a production environment.

Cards with buttons in a footer
==============================

.. code-block::rst

   .. container:: row m-0 p-0

      .. container:: col-md-6 pl-0 pr-3 py-3 m-0

         .. container:: card px-0 h-100

            .. rst-class:: card-header h3

               .. rubric:: :ref:`Pages <t3editors:pages>`

            .. container:: card-body

               The Page Management Guide introduces TYPO3's Page Tree and explains how pages are created and managed.

            .. container:: card-footer pb-0

               .. rst-class:: horizbuttons-striking-m

               -  `12-dev <https://docs.typo3.org/m/typo3/tutorial-editors/main/en-us/Pages/Index.html>`__
               -  `11.5 <https://docs.typo3.org/m/typo3/tutorial-editors/11.5/en-us/Pages/Index.html>`__
               -  `10.4 <https://docs.typo3.org/m/typo3/tutorial-editors/10.4/en-us/Pages/Index.html>`__

      .. container:: col-md-6 pl-0 pr-3 py-3 m-0

         .. container:: card px-0 h-100

            .. rst-class:: card-header h3

               .. rubric:: :ref:`Content <t3editors:content-elements>`

            .. container:: card-body

               The Content Creation Guide shows how page content is created in the form of Content Elements.

            .. container:: card-footer pb-0

               .. rst-class:: horizbuttons-striking-m

               -  `12-dev <https://docs.typo3.org/m/typo3/tutorial-editors/main/en-us/ContentElements/Index.html>`__
               -  `11.5 <https://docs.typo3.org/m/typo3/tutorial-editors/11.5/en-us/ContentElements/Index.html>`__
               -  `10.4 <https://docs.typo3.org/m/typo3/tutorial-editors/10.4/en-us/ContentElements/Index.html>`__

Rendered it looks like this:

.. container:: row m-0 p-0

   .. container:: col-md-6 pl-0 pr-3 py-3 m-0

      .. container:: card px-0 h-100

         .. rst-class:: card-header h3

            .. rubric:: :ref:`Pages <t3editors:pages>`

         .. container:: card-body

            The Page Management Guide introduces TYPO3's Page Tree and explains how pages are created and managed.

         .. container:: card-footer pb-0

            .. rst-class:: horizbuttons-striking-m

            -  `12-dev <https://docs.typo3.org/m/typo3/tutorial-editors/main/en-us/Pages/Index.html>`__
            -  `11.5 <https://docs.typo3.org/m/typo3/tutorial-editors/11.5/en-us/Pages/Index.html>`__
            -  `10.4 <https://docs.typo3.org/m/typo3/tutorial-editors/10.4/en-us/Pages/Index.html>`__

   .. container:: col-md-6 pl-0 pr-3 py-3 m-0

      .. container:: card px-0 h-100

         .. rst-class:: card-header h3

            .. rubric:: :ref:`Content <t3editors:content-elements>`

         .. container:: card-body

            The Content Creation Guide shows how page content is created in the form of Content Elements.

         .. container:: card-footer pb-0

            .. rst-class:: horizbuttons-striking-m

            -  `12-dev <https://docs.typo3.org/m/typo3/tutorial-editors/main/en-us/ContentElements/Index.html>`__
            -  `11.5 <https://docs.typo3.org/m/typo3/tutorial-editors/11.5/en-us/ContentElements/Index.html>`__
            -  `10.4 <https://docs.typo3.org/m/typo3/tutorial-editors/10.4/en-us/ContentElements/Index.html>`__

Cards with images
=================

.. code-block:: rst

   .. container:: row m-0 p-0

      .. container:: col-md-6 pl-0 pr-3 py-3 m-0

         .. container:: card px-0 h-100

            .. rst-class:: card-header h3

               .. rubric:: :ref:`Cards <restContentCards>`

            .. container:: card-body

               .. image:: /images/rest/ContendCards.png
                  :alt: Cards, example output
                  :class: with-shadow mb-2

               Card that can be used to shortly introduce topics and generate
               overview pages.

      .. container:: col-md-6 pl-0 pr-3 py-3 m-0

         .. container:: card px-0 h-100

            .. rst-class:: card-header h3

               .. rubric:: :ref:`Tabs <restContentTabs>`

            .. container:: card-body

               .. image:: /images/rest/ContendTabs.png
                  :alt: Tabs, example output
                  :class: with-shadow mb-2

               Tabs with different contend

Rendered it looks like this:

.. container:: row m-0 p-0

   .. container:: col-md-6 pl-0 pr-3 py-3 m-0

      .. container:: card px-0 h-100

         .. rst-class:: card-header h3

            .. rubric:: :ref:`Cards <restContentCards>`

         .. container:: card-body

            .. image:: /images/rest/ContendCards.png
               :alt: Cards, example output
               :class: with-shadow mb-2

            Card that can be used to shortly introduce topics and generate
            overview pages.

   .. container:: col-md-6 pl-0 pr-3 py-3 m-0

      .. container:: card px-0 h-100

         .. rst-class:: card-header h3

            .. rubric:: :ref:`Tabs <restContentTabs>`

         .. container:: card-body

            .. image:: /images/rest/ContendTabs.png
               :alt: Tabs, example output
               :class: with-shadow mb-2

            Tabs with different contend
