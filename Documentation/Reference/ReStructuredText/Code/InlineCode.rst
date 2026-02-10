:navigation-title: Inline Code

..  include:: /Includes.rst.txt
..  _inline-code:

====================================
Inline code with or without overlays
====================================

..  hint::

    Too much inline code can make the information on a page
    unreadable. If this is the case, consider using
    `Code blocks with syntax highlighting <https://docs.typo3.org/permalink/h2document:writing-rest-codeblocks-with-syntax-highlighting>`_.

Any text inside single or double backticks is printed as inline code. Double
backticks allow unescaped backticks to be used in the code:

..  tabs::

    ..  group-tab:: Output

        ..  include:: _snippets/_inline-code.rst.txt

    ..  group-tab:: reST

        ..  literalinclude:: _snippets/_inline-code.rst.txt

By convention single backticks are used unless double are needed.

..  _inline-code-language:

Code roles with language information and overlay
================================================

You can also use `text roles <text-roles>`_ with one of the predefined languages to display more
information to the user. For the most common languages, automatic
detection provides more context for the user.

..  tabs::

    ..  group-tab:: Output

        ..  include:: _snippets/_inline-code-languages.rst.txt

    ..  group-tab:: reST

        ..  literalinclude:: _snippets/_inline-code-languages.rst.txt

PHP classes from the TYPO3 Core are automatically linked to https://api.typo3.org
and display the PHP doc comment (if any) in the overlay.

All named inline code roles show an overlay where the code can be conveniently
copied and information on the language of the code.

..  seealso::

    *   `API links: More information on TYPO3 PHP classes <https://docs.typo3.org/permalink/h2document:links-api>`_
