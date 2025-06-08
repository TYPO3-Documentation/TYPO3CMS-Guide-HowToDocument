:navigation-title: Text Roles

..  include:: /Includes.rst.txt
..  _text-roles:

=================================
Supported named inline text roles
=================================

In general we support any text roles in reStructuredText that were previously
supported by Sphinx.

The TYPO3 Documentation Rendering Container also supports the
`Docutils Standard Text Roles <https://docutils.sourceforge.io/docs/ref/rst/roles.html#standard-roles>`_
except for `:raw:`, as that could pose security issues.

..  seealso::

    *   `Basic inline markup (bold, italic etc.) <https://docs.typo3.org/permalink/h2document:rest-bold-italic>`_
    *   `Inline code with or without overlays <https://docs.typo3.org/permalink/h2document:inline-code>`_
        for roles like `:php:`, `:typoscript:`, etc.
    *   `Links in ReStructured Text <https://docs.typo3.org/permalink/h2document:how-to-document-hyperlinks>`_

..  tabs::

    ..  group-tab:: Output

        ..  include:: _snippets/_text-roles.rst.txt

    ..  group-tab:: reST

        ..  literalinclude:: _snippets/_text-roles.rst.txt
