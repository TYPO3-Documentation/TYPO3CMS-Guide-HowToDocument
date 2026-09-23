:navigation-title: Inline code

..  include:: /Includes.rst.txt
..  _inline-code:

=====================================
Inline code with or without infoboxes
=====================================

..  hint::

    Too much inline code can make the information on a page
    unreadable. If this is the case, consider using
    `Code blocks with syntax highlighting <https://docs.typo3.org/permalink/h2document:writing-rest-codeblocks-with-syntax-highlighting>`_.

Any text inside single or double backticks is printed as inline code. Use
single backticks by default; double backticks are only needed when the
code itself contains an unescaped backtick:

..  tabs::

    ..  group-tab:: Output

        ..  include:: _snippets/_inline-code.rst.txt

    ..  group-tab:: reST

        ..  literalinclude:: _snippets/_inline-code.rst.txt

..  _inline-code-language:

Code roles with language information and an infobox
===================================================

You can also use `text roles <https://docs.typo3.org/permalink/h2document:text-roles>`_
that name the language of the code:

..  tabs::

    ..  group-tab:: Output

        ..  include:: _snippets/_inline-code-languages.rst.txt

    ..  group-tab:: reST

        ..  literalinclude:: _snippets/_inline-code-languages.rst.txt

Every code role shows an icon right after the code that opens an infobox.
For most roles, the infobox only names the language, for example "Code
written in SQL". Only :rst:`:php:` and :rst:`:php-short:` can tell the
reader more, see
`PHP classes and interfaces <https://docs.typo3.org/permalink/h2document:inline-code-php>`_.
The code text itself stays plain, selectable text, so it can be copied
directly instead of accidentally opening the infobox.

Two text roles that are not code roles open an infobox as well:
`:composer: <https://docs.typo3.org/permalink/h2document:linking-extensions>`_
always does, with information from Packagist, and
`:file: <https://docs.typo3.org/permalink/h2document:text-roles-file>`_
only does for a file that the same manual documents with the
:rst:`..  typo3:file::` directive.

..  _inline-code-when-to-use-a-role:

When to use a code role for inline code
=======================================

A code role labels its text as code in a language. Use one when the text
is code in that language: a statement, an expression, a keyword, a type,
or an identifier that the rendering can look up.

Everything else is a plain literal in single backticks. On text that is not
code, the language label and the infobox add nothing, and they promise
information that is not there.

..  _inline-code-keys-and-names:

Plain literals for array keys, configuration keys and column names
------------------------------------------------------------------

A TCA key, `CType`, array key, or YAML configuration key looks like PHP
because it is often written inside a PHP array, but the key itself is a
string. Database table and column names such as `tt_content` or `pid` are
often written next to SQL, but they are names, not SQL. Write all of them
as plain literals:

..  code-block:: rst

    The `enablecolumns` key ...

    The `pid` column of the `pages` table ...

Keep :rst:`:sql:` for actual SQL, such as a statement, a keyword like
:sql:`WHERE`, or a column type like :sql:`varchar(255)`.

..  _inline-code-generic-class-names:

Plain literals for class names used generically
-----------------------------------------------

When you talk about a kind of thing rather than one specific class, for
example "a PreviewRenderer" used generically, there is nothing a role
could resolve. Use a plain literal.

A namespace in a plain literal needs doubled backslashes, for example
`\\Vendor\\Ext\\PreviewRenderer`: unlike :rst:`:php:`, a plain literal
drops a single backslash instead of printing it. See
`Backslashes in text roles <https://docs.typo3.org/permalink/h2document:text-roles-backslash>`_.

..  _inline-code-headlines:

No code roles in headlines
--------------------------

Leave code roles out of headlines entirely, including :rst:`:php:` and
:rst:`:php-short:`. Use a plain literal there, even for something that would
get a role in body text:

..  code-block:: rst

    The `GeneralUtility` class
    ==========================

The text of a headline is reused in places that only show plain text: the
menu, the page title in the browser, and a reference without its own link
text. There, the role's styling and infobox are lost, and the text appears
exactly as written in the source, a full namespace included.

..  _inline-code-php:

PHP classes and interfaces with `:php:` and `:php-short:`
=========================================================

These two roles resolve a PHP type, such as a class or an interface, and a
member of one. Always pass the fully qualified name, including the leading
backslash: the namespace is what the roles need to find the class. For a type
of the TYPO3 Core, the infobox then shows its signature, the summary of its
doc comment and a link to https://api.typo3.org. For any other type, for
example one from Symfony, it can only say that the text is a class or
interface name.

:rst:`:php:` also recognizes a path in the global configuration, such as
:php:`$GLOBALS['TYPO3_CONF_VARS']['MAIL']['transport']`, and explains
`$GLOBALS['TYPO3_CONF_VARS']` in its infobox.

..  _inline-code-php-types:

Referencing a PHP class or interface with `:php-short:`
-------------------------------------------------------

Use :rst:`:php-short:`. It resolves the type from the fully qualified name
but shows only the short name, which reads much better inline:

..  code-block:: rst

    :php-short:`\TYPO3\CMS\Core\Security\ContentSecurityPolicy\Scope`

:rst:`:php:` resolves the type the same way but prints the full namespace.

..  _inline-code-php-methods:

Referencing a class member with `:php-short:`
---------------------------------------------

A method, property, constant or enum case resolves as well, as long as you
write it after the fully qualified class, with `::` or `->`:

..  code-block:: rst

    Create a scope with
    :php-short:`\TYPO3\CMS\Core\Security\ContentSecurityPolicy\Scope::backend()`.

The text prints as :php-short:`\TYPO3\CMS\Core\Security\ContentSecurityPolicy\Scope::backend()`.
The infobox names what the member is, for example "PHP function" for a
method, "PHP property", "PHP constant" or "PHP enum case", and describes the
class it belongs to; the link to https://api.typo3.org leads to the member on
the page of its class.

A member written on its own, such as `Scope::backend()`, has nothing to
resolve without its namespace. Introduce the class once with
:rst:`:php-short:`, then write the bare member as a plain literal.

..  seealso::

    *   `When to use a code role for inline code <https://docs.typo3.org/permalink/h2document:inline-code-when-to-use-a-role>`_
    *   `API links: More information on TYPO3 PHP classes <https://docs.typo3.org/permalink/h2document:links-api>`_
