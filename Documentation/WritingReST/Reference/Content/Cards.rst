..  include:: /Includes.rst.txt
..  highlight:: rst
..  index:: reST; Cards
..  _rest-cards:

=====
Cards
=====

Cards are used to group content together and provide a brief introduction on a given subject.

..  deprecated:: 0.2.40

    Cards where previously created by using nested :rst:`.. container::`
    directives with manually applied classes. The largest disadvantages were
    a large number of nested blocks and having to apply many classes.

    We discourage using containers for cards and suggest to switch to the
    cards directive.

Simple cards
============

..  card-grid::
    :columns: 1
    :columns-md: 2
    :gap: 4
    :card-height: 100

    ..  card:: :ref:`Concepts <t3start:Concepts>`

        Written for new users, this chapter introduces some of TYPO3s
        core concepts including the backend, TYPO3s administration
        interface.

    ..  card:: :ref:`System Requirements <t3start:System-Requirements>`

        System requirements for the host operation system, including
        its web server and database and how they should be configured
        prior to installation.


    ..  card:: :ref:`Concepts <t3start:Concepts>`

        Written for new users, this chapter introduces some of TYPO3s
        core concepts including the backend, TYPO3s administration
        interface.

    ..  card:: :ref:`System Requirements <t3start:System-Requirements>`

        System requirements for the host operation system, including
        its web server and database and how they should be configured
        prior to installation.

Cards with buttons in the footer
================================

..  card-grid::
    :columns: 1
    :columns-md: 2
    :gap: 4
    :card-height: 100

    ..  card:: :ref:`Pages <t3editors:pages>`

        The Page Management Guide introduces TYPO3's Page Tree and explains how pages are created and managed.

        ..  card-footer:: `12-dev <https://docs.typo3.org/m/typo3/tutorial-editors/main/en-us/Pages/Index.html>`__ `11.5 <https://docs.typo3.org/m/typo3/tutorial-editors/11.5/en-us/ContentElements/Index.html>`__ `10.4 <https://docs.typo3.org/m/typo3/tutorial-editors/10.4/en-us/ContentElements/Index.html>`__
            :button-style: btn btn-primary

    ..  card:: :ref:`Content <t3editors:content-elements>`

        The Content Creation Guide shows how page content is created in the form of Content Elements.

        ..  card-footer:: `12-dev <https://docs.typo3.org/m/typo3/tutorial-editors/main/en-us/ContentElements/Index.html>`__ `11.5 <https://docs.typo3.org/m/typo3/tutorial-editors/11.5/en-us/ContentElements/Index.html>`__ `10.4 <https://docs.typo3.org/m/typo3/tutorial-editors/10.4/en-us/ContentElements/Index.html>`__
            :button-style: btn btn-secondary

    ..  card:: :ref:`Pages <t3editors:pages>`

        The Page Management Guide introduces TYPO3's Page Tree and explains how pages are created and managed.

        ..  card-footer:: `12-dev <https://docs.typo3.org/m/typo3/tutorial-editors/main/en-us/Pages/Index.html>`__ `11.5 <https://docs.typo3.org/m/typo3/tutorial-editors/11.5/en-us/Pages/Index.html>`__  `10.4 <https://docs.typo3.org/m/typo3/tutorial-editors/10.4/en-us/Pages/Index.html>`__
            :button-style: btn btn-link

    ..  card:: :ref:`Content <t3editors:content-elements>`

        The Content Creation Guide shows how page content is created in the form of Content Elements.

        ..  card-footer::

            ..  rst-class:: horizbuttons-striking-m

                *   `12-dev <https://docs.typo3.org/m/typo3/tutorial-editors/main/en-us/ContentElements/Index.html>`__
                *   `11.5 <https://docs.typo3.org/m/typo3/tutorial-editors/11.5/en-us/ContentElements/Index.html>`__
                *   `10.4 <https://docs.typo3.org/m/typo3/tutorial-editors/10.4/en-us/ContentElements/Index.html>`__


    ..  card:: Stretched link

        The complete card can be linked if you use exactly one stretched link.

        ..  card-footer:: :ref:`Read more <t3editors:content-elements>`
            :button-style: btn btn-secondary stretched-link


Cards with images
=================

..  card-grid::
    :columns: 1
    :columns-md: 2
    :gap: 4
    :card-height: 100

    ..  card:: :ref:`Cards <rest-cards>`

        ..  card-image:: /Images/cards.png
            :alt: Cards, example output

        Cards can be used to shortly introduce topics and generate
        overview pages.

    ..  card:: :ref:`Tabs <rest-tabs>`

        ..  card-image:: /Images/tabs.png
            :alt: Tabs, example output

        Tabs can be used to present a topic from different perspectives.

    ..  card:: :ref:`Cards <rest-cards>`

        ..  card-image:: /Images/cards.png
            :alt: Cards, example output

        Cards can be used to shortly introduce topics and generate
        overview pages.


    ..  card:: :ref:`Tabs <rest-tabs>`

        ..  card-image:: /Images/tabs.png
            :alt: Tabs, example output
            :position: bottom

        This card has the image at the bottom
