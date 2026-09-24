..  include:: /Includes.rst.txt
..  index:: reST; Tables
..  _rest-tables:

======
Tables
======

There are several ways to create tables in reST.

It is recommended that you do not use large tables as they are not
responsive.

..  index:: reST; Grid table

..  _rest-tables-grid-table:

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

..  _rest-tables-simple-table:

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

..  _rest-tables-csv-table:

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

..  _rest-tables-t3-field-list:

`t3-field-list-table` tables
============================

`t3-field-list-table` is a custom directive of the TYPO3 rendering. If you
want your .rst file to be correctly rendered on other platforms as well (for
example GitHub), you should not use this.

Each item of the list is one row, and the field names are the columns.
:rst:`:header-rows:` says how many of the first items are header rows, as it
does in a `list-table`: `1` for the usual single header row, `2` for two, and
`0` for a table without a header. Without the option the first row is the
header.

..  note::
    Before render-guides 0.44.0 the option was read but never used: the first
    row was always the header. A table written with :rst:`:header-rows: 0` or
    :rst:`:header-rows: 2` therefore changes its appearance once it is
    rendered again.


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
