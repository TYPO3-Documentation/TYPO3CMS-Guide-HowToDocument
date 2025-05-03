:navigation-title: CGL for ReST files

..  include:: /Includes.rst.txt
..  _cgl:

=============================================
Coding guidelines for reStructured text files
=============================================

In the official documentation files we try to follow the following coding
guidelines:

*   Indentation of 4 spaces, this includes
    `lists <https://docs.typo3.org/permalink/h2document:rest-lists>`_, directives,
    `Code blocks <https://docs.typo3.org/permalink/h2document:writing-rest-codeblocks-with-syntax-highlighting>`_,
    and other blocks that need to be indented in ReST.
*   Wrap lines at 80 chars where possible
*   We avoid abbreviations and colloquial language. When we use abbreviations
    they should be introduced in the same section.
*   Each ReST file must have a main header.
*   Each ReST file must include `..  include:: /Includes.rst.txt` to display
    global messages, for example for outdated versions.
*   It is highly recommended to use `:navigation-title: My Title` at the top
    of each file to provide a shorter title to be displayed in the menu.
    See `Navigation title: A page title displayed in menus <https://docs.typo3.org/permalink/h2document:navigation-title>`_.

..  literalinclude:: _general.rst.txt
    :caption: Documentation/Introduction.rst

..  _cgl-code:

Rules for code examples
=======================

*   Wrap code examples at 80 chars where possible to avoid horizontal scrolling.
*   Code examples longer then a few lines should go in external files to be
    included.
*   All code examples should lint. They should demonstrate best practices.
    Where best practices would over complicate things, mention that this is not
    a best practice but used for demonstration.

..  literalinclude:: _code.rst.txt
    :caption: Documentation/Installation.rst

..  _cgl-headlines:

Rules headlines
===============

*   Headlines are in sentence case.
*   Each headline should be possible to understand without context. This improves
    search results in the internal search and search engines.
*   Use the official order for marking headlines. The page title is overlined
    and underlined with `=`, headlines of level 2 are underlined with `=`,
    level 3 with `-` and level 4 with `~`.
*   Each headline should have a unique anchor so that permalinks to the headline
    can be generated.

..  literalinclude:: _headlines.rst.txt
    :caption: Documentation/HeaderDemo.rst

See `Headlines and Anchors <https://docs.typo3.org/permalink/h2document:headlines-and-sections>`_
for more headline levels.
