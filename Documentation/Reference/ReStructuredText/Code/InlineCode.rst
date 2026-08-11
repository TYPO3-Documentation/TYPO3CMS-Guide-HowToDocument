:navigation-title: Inline Code

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

You can also use `text roles <https://docs.typo3.org/permalink/h2document:text-roles>`_ with one of the predefined languages to display more
information to the user. For the most common languages, automatic
detection provides more context for the user.

..  tabs::

    ..  group-tab:: Output

        ..  include:: _snippets/_inline-code-languages.rst.txt

    ..  group-tab:: reST

        ..  literalinclude:: _snippets/_inline-code-languages.rst.txt

All named inline code roles show an icon right after the code that opens
an infobox with details about it — the language, and for a resolvable
PHP class from the TYPO3 Core, its doc comment (if any) and a link to
https://api.typo3.org. The code text itself stays plain, selectable text,
so it can be copied directly instead of accidentally opening the infobox.

..  _inline-code-php:

`:php:` and `:php-short:`
=========================

Use :rst:`:php:` and :rst:`:php-short:` when the text is a real,
resolvable PHP identifier — a class, method, constant, or function — so
the infobox can tell the reader something genuinely useful about it. If
the tooling has nothing to resolve, the "PHP" tag and the infobox button
are just noise, and worse, they promise a lookup that goes nowhere. In
those cases a plain literal reads more honestly:

*   A TCA key, `CType`, array key, or YAML config key looks like it lives
    in PHP because it is often written inside a PHP array, but the key
    itself is just a string, not an identifier the PHP domain can
    resolve. Write it as a plain literal instead:

    ..  code-block:: rst

        The `enablecolumns` key ...

*   When referencing a class, interface, or similar type on its own, pass
    the fully-qualified name (leading backslash, full namespace) to
    :rst:`:php-short:` rather than :rst:`:php:`. It still resolves the
    infobox content from the FQCN, but displays only the short name,
    which reads much better inline than the full namespace:

    ..  code-block:: rst

        :php-short:`\TYPO3\CMS\Core\Security\ContentSecurityPolicy`

    As of this writing, :rst:`:php-short:` only resolves a bare type this
    way, not a type combined with a method, such as `Scope::backend()`.
    For those, use :rst:`:php:` with the full FQCN instead — it reads
    longer, but it is the one that actually resolves:

    ..  code-block:: rst

        :php:`\TYPO3\CMS\Core\Security\ContentSecurityPolicy\Scope::backend()`

*   When you are talking about a concept rather than naming a specific,
    resolvable class — for example "a PreviewRenderer" used generically,
    not `\Vendor\Ext\PreviewRenderer` — a plain literal fits better, since
    there is no single class the infobox could point to.

*   Headlines are the one place to leave roles out entirely, including
    :rst:`:php:`/:rst:`:php-short:` — use plain backticks there even for
    something that would get a role in body text. A role's code styling
    and infobox button do not read well in a heading, and they disappear
    wherever the heading's text gets reused as plain text elsewhere — for
    example a bare :rst:`:ref:` to it falls back to unstyled text instead
    of keeping the code formatting.

..  seealso::

    *   `API links: More information on TYPO3 PHP classes <https://docs.typo3.org/permalink/h2document:links-api>`_
