:navigation-title: ViewHelper
..  include:: /Includes.rst.txt
..  _viewhelper:

=============================================
Display Fluid ViewHelpers in ReStructuredText
=============================================

The special `..  typo3:viewhelper::` directive can be used to display the
information about a Fluid ViewHelper, including all arguments.

The information on the available arguments is included from a `.json` file.
See also https://github.com/TYPO3-Documentation/fluid-documentation-generator
on how to generate the input file.

..  warning::
    Usage of the viewhelper directive outside of the
    :ref:`Fluid ViewHelper Reference <t3viewhelper:start>` is still considered
    experimental.

..  _viewhelper-example:

Example: Display a ViewHelper from a JSON include
=================================================

..  code-block:: rst
    :caption: Documentation/MyViewHelper.rst

    ..  typo3:viewhelper:: link.external
        :source: /resources/global_viewhelpers_demo.json

..  literalinclude:: _ViewHelper/_global_viewhelpers_demo.json
    :language: json
    :caption: Documentation/resources/global_viewhelpers_demo.json


..  _viewhelper-properties:

Properties of the `viewhelper` directive
========================================

..  confval-menu::
    :display: table
    :type:

    ..  include:: _ViewHelper/_Content.rst.txt
        :show-buttons:

    ..  include:: _ViewHelper/_Source.rst.txt
        :show-buttons:

    ..  include:: _ViewHelper/_SortBy.rst.txt
        :show-buttons:

    ..  include:: _ViewHelper/_NoIndex.rst.txt
        :show-buttons:
