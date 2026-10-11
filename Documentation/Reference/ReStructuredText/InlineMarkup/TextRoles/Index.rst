:navigation-title: Text Roles

..  include:: /Includes.rst.txt
..  _text-roles:

=================================
Supported named inline text roles
=================================

A named inline text role marks up a short piece of text inline, in the
middle of a sentence. Write the role name surrounded by colons
(:rst:`:role-name:`), immediately followed — with no space — by the text
it applies to, enclosed in backticks. Some roles expect that text to
follow a particular syntax, for example a link target, an issue number,
or a fully-qualified class name.

In general we support any text roles in reStructuredText that were
previously supported by Sphinx. The TYPO3 Documentation Rendering
Container also supports the
`Docutils Standard Text Roles <https://docutils.sourceforge.io/docs/ref/rst/roles.html#standard-roles>`_
except for :rst:`:raw:`, as that could pose security issues.

The roles below are the ones most commonly used across TYPO3
documentation that are not already covered on their own page.

..  _text-roles-backslash:

..  attention::

    For most roles, a lone backslash inside the backticks is treated as
    an escape character and silently disappears from the output instead
    of being printed. This trips people up in Windows paths and PHP
    namespaces:

    ..  code-block:: rst

        `\Vendor\Ext\MyClass`        renders as: VendorExtMyClass
        `\\Vendor\\Ext\\MyClass`     renders as: \Vendor\Ext\MyClass

    Double every backslash you want to keep. :rst:`:file:`, :rst:`:php:`,
    :rst:`:php-short:`, and :rst:`:php-namespace:` are exceptions. They
    print a single backslash as it is.

    In these four roles, the text must not end with a backslash. That
    backslash escapes the closing backtick, and the role runs on into the
    text that follows. Doubling it does not help, because these roles then
    print both backslashes. If you are not sure how a given role handles
    a backslash, check the rendered output.

..  index:: reST roles; abbr
..  _text-roles-abbr:

`:abbr:`
========

Marks a piece of text as an abbreviation or acronym. Write the
abbreviation followed by its expansion in parentheses; the expansion is
shown as a tooltip on hover and is not printed inline.

..  code-block:: rst

    :abbr:`LIFO (last-in, first-out)`

How it looks:
    :abbr:`LIFO (last-in, first-out)`

..  index:: reST roles; path
..  _text-roles-path:

`:path:`
========

Refers to a directory or folder path, as opposed to a specific file. Use
:ref:`:file: <text-roles-file>` instead when the path ends in a file name.

..  code-block:: rst

    The extension stores its data in :path:`public/fileadmin`.

How it looks:
    The extension stores its data in :path:`public/fileadmin`.

..  index:: reST roles; file
..  _text-roles-file:

`:file:`
========

Refers to a specific file, including its name and, if helpful, its path.
Use :ref:`:path: <text-roles-path>` instead when referring to a directory
rather than a single file.

..  code-block:: rst

    Edit :file:`config/system/settings.php` to change the setting.

How it looks:
    Edit :file:`config/system/settings.php` to change the setting.

If the file is defined with the directive :rst:`..  typo3:file::`, the role
links to its description. A popup tells the reader where the file is in a
Composer-based installation and in a Classic mode installation. The official
manuals define their files in
`TYPO3 Explained <https://docs.typo3.org/permalink/t3coreapi:start>`_, and
the role finds those files in every manual, in the version that the
interlinks of the manual use:

..  code-block:: rst

    Add the setting to :file:`config/sites/my-site/settings.yaml`.

How it looks:
    Add the setting to :file:`config/sites/my-site/settings.yaml`.

Each definition decides with a regular expression which paths it matches.
A file that neither the manual itself nor TYPO3 Explained defines, or a
path that the expression does not match, prints as plain code.

..  index:: reST roles; issue
..  _text-roles-issue:

`:issue:`
=========

Links to an issue on `TYPO3 Forge <https://forge.typo3.org>`_ by its
number. By default the link text is `forge#<number>`; pass a custom link
text before the number in angle brackets to show different text instead.

..  code-block:: rst

    See also :issue:`102056` or :issue:`this issue <99508>`.

How it looks:
    See also :issue:`102056` or :issue:`this issue <99508>`.

..  _text-roles-elsewhere:

More text roles, documented on their own pages
==============================================

A few text roles are common enough, or involved enough, to have a full
page to themselves rather than a short entry here:

*   :rst:`:guilabel:` for GUI labels — backend modules, tabs, buttons,
    fields — and click paths through them, and :rst:`:kbd:` for keyboard
    shortcuts — see
    `Referring to GUI elements and keystrokes <https://docs.typo3.org/permalink/h2document:rest-refer-to-gui-elements>`_.
*   :rst:`:composer:` and :rst:`:t3ext:` for linking Composer packages and
    TER extensions — see
    `Linking Composer packages and TYPO3 extensions <https://docs.typo3.org/permalink/h2document:linking-extensions>`_.
*   :rst:`:t3src:` for linking source files of the TYPO3 Core — see
    `Linking source files of the TYPO3 Core <https://docs.typo3.org/permalink/h2document:linking-core-source>`_.
*   :rst:`:php:`, :rst:`:php-short:`, :rst:`:php-namespace:`,
    :rst:`:typoscript:`, and other code roles with an infobox — see
    `Inline code with or without infoboxes <https://docs.typo3.org/permalink/h2document:inline-code>`_.

..  seealso::

    *   `Basic inline markup (bold, italic etc.) <https://docs.typo3.org/permalink/h2document:rest-bold-italic>`_
    *   `Links in ReStructured Text <https://docs.typo3.org/permalink/h2document:how-to-document-hyperlinks>`_
    *   `Docutils: Interpreted Text Roles <http://docutils.sourceforge.io/docs/ref/rst/roles.html>`_
