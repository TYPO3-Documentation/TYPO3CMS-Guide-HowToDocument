.. include:: /Includes.rst.txt
.. highlight:: rst
.. index:: Documentation; Translation
.. _add-translation:

=======================
How to add translations
=======================

If you want to add a translation to official documentation or to
your extension documentation, please keep in mind that it must be updated
and maintained long term.

.. important::

   Before adding a translation to an official manual
   `contact the Documentation Team <https://typo3.org/community/teams/documentation/#c9886>`__.

In general, it is a good idea to keep the structure of the original
language. That way, it is possible to switch the language on each page and
wind up on the corresponding translated page.

.. rst-class:: bignums-xxl

#. Create a localization directory

   e.g. `Documentation/Localization.de_DE`, `Documentation/Localization.fr_FR`.
   This directory contains a complete documentation project. So, you can effectively
   copy the original :file:`Documentation` directory.

   .. code-block:: none

         Documentation
         └──  Localization.de_DE
              ├── Index.rst
              └── Settings.cfg


#. Update the file :ref:`settings-cfg`.

#. Translate the texts

#. Check the rendering

   :ref:`Render the documentation locally with Docker <rendering-docs>`

   The result will be in :file:`/Documentation-GENERATED-temp/Result/project/<locale>/0.0.0/`,
   for example :file:`/Documentation-GENERATED-temp/Result/project/de-de/0.0.0/Index.html`


Once the documentation has been rerendered on the documentation server, you can
switch the language using the version selector.
