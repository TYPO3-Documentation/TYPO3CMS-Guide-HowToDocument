:navigation-title: Inline code

..  include:: /Includes.rst.txt
..  _inline-code:
..  _inline-code-headlines:

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
written in SQL". Some roles can tell the reader more:

*   :rst:`:php:` and :rst:`:php-short:`, see
    `PHP classes and interfaces <https://docs.typo3.org/permalink/h2document:inline-code-php>`_.
*   :rst:`:typoscript:` and :rst:`:tsconfig:`, see
    `TypoScript and TSconfig <https://docs.typo3.org/permalink/h2document:inline-code-typoscript>`_.
*   :rst:`:fluid:`, for a ViewHelper, see
    `Fluid ViewHelpers <https://docs.typo3.org/permalink/h2document:inline-code-fluid>`_.

The code text itself stays plain, selectable text, so it can be copied
directly instead of accidentally opening the infobox.

Two text roles that are not code roles open an infobox as well:
`:composer: <https://docs.typo3.org/permalink/h2document:linking-extensions>`_
always does, with information from Packagist, and
`:file: <https://docs.typo3.org/permalink/h2document:text-roles-file>`_
does for a file that TYPO3 Explained or the same manual defines.

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

..  _inline-code-php-namespace:

Referencing a PHP namespace with `:php-namespace:`
--------------------------------------------------

Use :rst:`:php-namespace:` for a namespace. Pass the fully qualified
namespace, including the leading backslash:

..  code-block:: rst

    The classes of :php-namespace:`\TYPO3\CMS\Core\Http` handle requests
    and responses.

Write the namespace without a trailing backslash. A backslash in front of
the closing backtick escapes the backtick, and the role runs on into the
text that follows.

The text prints as :php-namespace:`\TYPO3\CMS\Core\Http`. The role always
prints the full namespace, because the last segment alone says too little.
The infobox calls it a PHP namespace. For a namespace of the TYPO3 Core, the
infobox also links to the page of the namespace on https://api.typo3.org.
The `class index <https://docs.typo3.org/permalink/h2document:rendered-artifacts-classes>`_
does not list a namespace.

A namespace that starts with :php-namespace:`\MyVendor` or
:php-namespace:`\Vendor` is an example namespace. Its infobox asks the
reader to replace it with their own vendor and namespace. See
`Example names for extensions and site packages <https://docs.typo3.org/permalink/h2document:codeblocks-example-names>`_.

The rendering does not check if a namespace exists. A misspelled namespace
renders without a warning. If the infobox of a TYPO3 Core namespace has no
link to the API, check the namespace for a typo.

:rst:`:php:` and :rst:`:php-short:` also recognize a namespace that the TYPO3
API knows, and print it in full. A :php:`use` statement in a code example
that imports such a namespace is recognized too.

Some names are a class and a namespace at the same time, for example
`\\TYPO3\\CMS\\Core\\Exception`. :rst:`:php:` and :rst:`:php-short:` treat
such a name as the class. If you mean the namespace, use
:rst:`:php-namespace:`.

..  _inline-code-typoscript:

TypoScript and TSconfig with `:typoscript:` and `:tsconfig:`
============================================================

The infobox of :rst:`:typoscript:` and :rst:`:tsconfig:` says what the code
is and links to its description. The rendering reads this from the
configuration values of the
`TypoScript reference <https://docs.typo3.org/permalink/t3tsref:start>`_.
This works in every manual, in the version of the TypoScript reference
that its interlinks use.

The roles find the following:

*   A full path to an option, for example :typoscript:`stdWrap.parseFunc`,
    :typoscript:`page.includeJS`, or
    :tsconfig:`options.pageTree.doktypesToShowInNewPageDragArea`.
*   An object type, a function, or a top-level object on its own, for
    example `USER`, `COA_INT`, `PAGE`, `stdWrap`, `typolink`, `config`, or
    `module`.

A name that several options share, such as `wrap` or `current`, gets no
description. A wrong description is worse than none. Write the full path
instead, for example :typoscript:`stdWrap.current` rather than `current`.

..  _inline-code-typoscript-key:

Naming the configuration value in angle brackets
------------------------------------------------

If the code alone does not tell which option it is, name the configuration
value in angle brackets, as in :rst:`:confval:`:

..  code-block:: rst

    Use :typoscript:`current <t3tsref:stdwrap-current>` to ...

The text prints as :typoscript:`current <t3tsref:stdwrap-current>`. The
page shows only the code before the angle brackets.

*   The key is the `:name:` of the
    `confval <https://docs.typo3.org/permalink/h2document:rest-confval>`_.
    Put an interlink key in front of it, such as `t3tsref:` or `t3coreapi:`,
    for a configuration value of another manual. Without an interlink key,
    the key names a configuration value of the same manual.
*   Any configuration value works, not only a TypoScript one. For
    example, you can name a TCA option.
*   The text before the angle brackets must be a path or a name. The
    rendering never reads code such as an HTML wrap, `<div> | </div>`, or
    `<INCLUDE_TYPOSCRIPT: ...>` as a key.

If the named manual does not document the key, the rendering shows a
warning, and :bash:`make test-docs` fails. If the rendering cannot reach
the manual, it shows no warning.

..  _inline-code-fluid:

Fluid ViewHelpers with `:fluid:`
================================

If the code of :rst:`:fluid:` starts with a ViewHelper, the infobox says
what the ViewHelper does and links to its description. The code stays as
you wrote it:

..  code-block:: rst

    Wrap the text in :fluid:`<f:format.html>{record.bodytext}</f:format.html>`.

The text prints as
:fluid:`<f:format.html>{record.bodytext}</f:format.html>`.

The role finds a ViewHelper in any of these forms:

*   As a tag, for example :fluid:`<f:format.html>` or
    :fluid:`</f:format.html>`.
*   As an inline call, for example :fluid:`{f:translate(key: 'title')}`.
*   By its name alone, for example :fluid:`f:uri.image`.

The rendering looks up the ViewHelper in the
`Fluid ViewHelper Reference <https://docs.typo3.org/permalink/t3viewhelper:start>`_,
in the version that the interlinks of your manual use. If your manual
documents the ViewHelper itself, the infobox links to that description
instead.

The role does not find a ViewHelper that is not at the start of the code,
such as in :fluid:`{record.bodytext -> f:format.html()}`. A ViewHelper that
the reference does not document, such as one of your own extension, and
Fluid that names no ViewHelper, such as :fluid:`{page.uid}`, stay Fluid
code. The rendering shows no warning for them.

..  seealso::

    *   `When to use a code role for inline code <https://docs.typo3.org/permalink/h2document:inline-code-when-to-use-a-role>`_
    *   `API links: More information on TYPO3 PHP classes <https://docs.typo3.org/permalink/h2document:links-api>`_
