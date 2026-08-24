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

    Double every backslash you want to keep. :rst:`:file:`, :rst:`:php:`
    and :rst:`:php-short:` are exceptions -- they take the text verbatim,
    so a single backslash there already prints as-is. If you are not
    sure how a given role handles it, check the rendered output rather
    than assuming.

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
*   :rst:`:php:`, :rst:`:php-short:`, :rst:`:typoscript:` and other code
    roles with an infobox — see
    `Inline code with or without infoboxes <https://docs.typo3.org/permalink/h2document:inline-code>`_.

..  seealso::

    *   `Basic inline markup (bold, italic etc.) <https://docs.typo3.org/permalink/h2document:rest-bold-italic>`_
    *   `Links in ReStructured Text <https://docs.typo3.org/permalink/h2document:how-to-document-hyperlinks>`_
    *   `Docutils: Interpreted Text Roles <http://docutils.sourceforge.io/docs/ref/rst/roles.html>`_
