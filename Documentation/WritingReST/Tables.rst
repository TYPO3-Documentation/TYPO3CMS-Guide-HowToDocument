.. include:: /Includes.rst.txt
.. highlight:: rst



.. _rest-tables:

======
Tables
======

There are several ways to create tables in reST. Use what works best for your use case.


Grid Table
==========


.. code-block:: rest


   +----------+----------+
   | Header 1 | Header 2 |
   +==========+==========+
   | 1        | one      |
   +----------+----------+
   | 2        | two      |
   +----------+----------+



+----------+----------+
| Header 1 | Header 2 |
+==========+==========+
| 1        | one      |
+----------+----------+
| 2        | two      |
+----------+----------+


http://docutils.sourceforge.net/docs/user/rst/quickref.html#tables

You can use this `table generator <https://www.tablesgenerator.com/text_tables>`__ to
create a grid table.

Simple Table
============


.. code-block:: rest

   ========  ========
   Header 1  Header 2
   ========  ========
   1         one
   2         two
   ========  ========


========  ========
Header 1  Header 2
========  ========
1         one
2         two
========  ========

http://docutils.sourceforge.net/docs/user/rst/quickref.html#tables


Csv Tables
==========

.. code-block:: rest

   .. csv-table:: Numbers
      :header: "Header 1", "Header 2"
      :widths: 15, 15

      1, "one"
      2, "two"


.. csv-table:: Numbers
   :header: "Header 1", "Header 2"
   :widths: 15, 15

   1, "one"
   2, "two"


http://docutils.sourceforge.net/docs/ref/rst/directives.html#id4


t3-field-list-table Tables
==========================

`t3-field-list-table` is a custom directive, created by the t3SphinxThemeRtd
template. If you want your .rst file to be correctly rendered on other
platforms as well (e.g. GitHub), you should not use this.


.. code-block:: rest

   .. t3-field-list-table::
      :header-rows: 1

      -  :Header1:   Header1
         :Header2:   Header2

      -  :Header1:   1
         :Header2:   one

      -  :Header1:   2
         :Header2:   two



.. t3-field-list-table::
   :header-rows: 1

   -  :Header1:   Header1
      :Header2:   Header2

   -  :Header1:   1
      :Header2:   one

   -  :Header1:   2
      :Header2:   two


Example: https://docs.typo3.org/typo3cms/GuidesAndTutorials/Index.html


