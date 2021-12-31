.. include:: /Includes.rst.txt
.. highlight:: rst
.. index::
   reST; Tabs
.. _restContentTabs:

=====
Tabs
=====

They provide a compact way to present a topic from different perspectives, with
each perspective presented in a tab. When the reader changes tabs, this change
is synchronized in all tab content elements.

For example, if the reader is guided through the TYPO3 installation with text
and five code blocks, they could switch from Bash to DDEV instructions in the
first code block, and all subsequent code blocks would also automatically
switch to DDEV.

.. code-block:: rst

   .. tabs::

   .. group-tab:: bash

       .. code-block:: bash

         touch example-project-directory/public/FIRST_INSTALL

   .. group-tab:: powershell

       .. code-block:: powershell

         echo $null >> public/FIRST_INSTALL

   .. group-tab:: ddev

       .. code-block:: bash

         ddev exec touch public/FIRST_INSTALL

Looks like this rendered:

.. tabs::

   .. group-tab:: bash

       .. code-block:: bash

         touch example-project-directory/public/FIRST_INSTALL

   .. group-tab:: powershell

       .. code-block:: powershell

         echo $null >> public/FIRST_INSTALL

   .. group-tab:: ddev

       .. code-block:: bash

         ddev exec touch public/FIRST_INSTALL

As an example, tabs are used in the Getting Started Guide in the chapter
:ref:`Installation <t3start:install>`.
