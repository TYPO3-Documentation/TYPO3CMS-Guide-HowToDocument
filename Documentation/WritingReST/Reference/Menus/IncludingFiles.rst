..  include:: /Includes.rst.txt
..  index::
    reST; Including files
    reST directives; include
..  _including-files:

===============
Including files
===============

Includes can be used for two use cases in the documentation: Repeating text
snippets used in several places or breaking up long pages into easier to edit
subparts.

Some documentation projects have the same snippet of text appear in several
places. This text can be maintained once and included in many places.

In this case it may make sense to *include* text snippets. The `..  include:: someFile.rst.txt`
directive does this.

Files to be included **cannot** lie outside the :path:`Documentation` folder.
They **may not** end on `.rst`. By convention they **should** end on `.rst.txt`.

..  contents::
    :caption: Table of contents

..  _including-files-example-simple:

Example of a simple include:
============================

Include the same text asking for contributions in all Events that do not
have an example yet:

..  code-block:: rst
    :caption: Documentation/Events/Event1.rst

    Example
    =======

    ..  include:: /_includes/EventsContributeNote.rst.txt


..  code-block:: rst
    :caption: Documentation/Events/SomeOtherEvent.rst

    Example
    =======

    ..  include:: /_includes/EventsContributeNote.rst.txt

The file to be included:

..  code-block:: rst
    :caption: Documentation/_includes/EventsContributeNote.rst.txt

    ..  note::
        Currently, we do not have an example for this event. If you can provide a
        useful one, please open an issue ...

These rst definitions will be included in all places the include is used as if
they had been written directly into the rst file. All markup is respected.


..  _including-files-example-advanced:

Example: Break up a large file into manageable pieces
=====================================================

In places like the TSconfig reference or TCA reference it is helpful to display
all properties of an element on one page. However this gives the contributors
very large rst files to maintain. Such files can be broken into pieces that
contain only the definition and maybe example of one parameter each.

..  code-block:: rst
    :caption: Documentation/ColumnsConfig/Type/Category/Index.rst

    Properties of the TCA column type `category`
    ============================================

    ..  confval-menu::
        :display: table
        :type:
        :Scope:

        ..  include:: _Properties/_Default.rst.txt
            :show-buttons:

        ..  include:: _Properties/_ExclusiveKeys.rst.txt
            :show-buttons:

        ..  include:: _Properties/_ForeignTable.rst.txt
            :show-buttons:

Each include file in turn contains the complete data for one property, for
example:

..  code-block:: rst
    :caption: Documentation/ColumnsConfig/Type/Category/_Properties/_ExclusiveKeys.rst.txt

    ..  _columns-category-properties-exclusivekeys:

    ..  confval:: exclusiveKeys
        :name: category-exclusiveKeys
        :type: string (list of)

        List of keys that exclude any other keys ...

The option `:show-buttons:` display a special "Edit on GitHub" button only for
the section contained within include:

..  figure:: /Images/include-with-button.png

    The edit on GitHub button of an included section


..  _include-properties:

Properties
==========

..  confval-menu::
    :display: table
    :type:
    :Scope:

    ..  include:: _Include/_Content.rst.txt
        :show-buttons:

    ..  include:: _Include/_ShowButtons.rst.txt
        :show-buttons:
