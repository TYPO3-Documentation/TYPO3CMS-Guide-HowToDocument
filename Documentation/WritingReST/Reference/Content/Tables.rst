..  include:: /Includes.rst.txt
..  highlight:: rst
..  index:: reST; Tables
..  _rest-tables:

======
Tables
======

There are several ways to create tables in reST.

It is recommended that you do not use large tables as they are not
responsive.

..  index:: reST; Grid table

Grid table
==========

..  code-block:: rst

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


..  index:: reST; Simple table

Simple table
============


..  code-block:: rst

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


..  index:: reST; CSV table

CSV table
=========

..  code-block:: rst

    ..  csv-table:: Numbers
        :header: "Header 1", "Header 2"
        :widths: 15, 15

        1, "one"
        2, "two"


..  csv-table:: Numbers
    :header: "Header 1", "Header 2"
    :widths: 15, 15

    1, "one"
    2, "two"


https://docutils.sourceforge.io/docs/ref/rst/directives.html#csv-table-1


..  index::
    reST directives; t3-field-list-table

t3-field-list-table tables
==========================

`t3-field-list-table` is a custom directive, created by the t3SphinxThemeRtd
template. If you want your .rst file to be correctly rendered on other
platforms as well (for example GitHub), you should not use this.


..  code-block:: rst

    ..  t3-field-list-table::
        :header-rows: 1

        -   :Header1:   Header1
            :Header2:   Header2

        -   :Header1:   1
            :Header2:   one

        -   :Header1:   2
            :Header2:   two



..  t3-field-list-table::
    :header-rows: 1

    -   :Header1:   Header1
        :Header2:   Header2

    -   :Header1:   1
        :Header2:   one

    -   :Header1:   2
        :Header2:   two


Example: https://docs.typo3.org/typo3cms/GuidesAndTutorials/Index.html


