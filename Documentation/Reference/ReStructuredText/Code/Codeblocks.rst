..  include:: /Includes.rst.txt
..  index::
    reST; Code blocks
    reST; syntax highlighting
..  _writing-rest-codeblocks-with-syntax-highlighting:

====================================
Code blocks with syntax highlighting
====================================


..  _codeblock-quick-reference:

Quick Reference
===============

A code block consists of a `code-block` directive and the actual code indented
by four spaces for consistency with other code bases.

A code block can have one or more options. To make orientation in code examples easier
try to always add a `:caption:` with the path and name of the file where the example should go:

..  tabs::

    ..  group-tab:: Source (rst)

        ..  code-block:: rst
            :caption: Documentation/MyDocs.rst

            ..  code-block:: php
                :caption: EXT:site_package/Configuration/TCA/Overrides/sys_template.php

                /**
                 * Add default TypoScript (constants and setup)
                 */
                \TYPO3\CMS\Core\Utility\ExtensionManagementUtility::addStaticFile(
                     'site_package',
                     'Configuration/TypoScript',
                     'Site Package'
                );

    ..  group-tab:: Output

        ..  code-block:: php
            :caption: EXT:site_package/Configuration/TCA/Overrides/sys_template.php

            /**
             * Add default TypoScript (constants and setup)
             */
            \TYPO3\CMS\Core\Utility\ExtensionManagementUtility::addStaticFile(
                 'site_package',
                 'Configuration/TypoScript',
                 'Site Package'
            );

Always use :ref:`syntactically correct code <codeblocks-syntactically-correct>`
in a code block.

Use :ref:`placeholders <codeblocks-placeholders>` in angle brackets
(`<placeholder-name>`) to refer to a place in the code where the exact
value is not important.


..  index:: reST directives; code-block
..  _codeblock-directive:

Code block directive
====================

A code block has the following syntax:

..  code-block:: rst
    :caption: Documentation/MyDocs.rst

    ..  code-block:: <language>
        :caption: <caption>
        <options>

        <code>

There must be a newline between the options and the code. There must not be a
newline between the directive line and options or within options. Otherwise the rendering
will fail.

<language>
    The language of the code-block. We commonly use the following: :rst:`php`,
    :rst:`typoscript` (also for TSconfig), :rst:`yaml`, :rst:`javascript`,
    :rst:`html` (also for Fluid), :rst:`shell`, :rst:`xml`, :rst:`plaintext`.

    See all
    :ref:`available languages <writing-rest-codeblocks-available-languages>`

<caption>
    To make orientation in code examples easier try to always add
    a caption with the name of the file where the example should go. If the code
    should be manually entered in the TYPO3 backend explain where it should go there.

<options>
    The following options may be used, all options are optional,
    but :rst:`caption` is highly recommended:

    ..  code-block:: rst

        ..  code-block:: <language>
            :caption: <caption>
            :linenos:
            :lineno-start: <start-number>
            :emphasize-lines: <emphasized-line-numbers>
            :name: <reference-label>

    :rst:`linenos`
        Show line numbers.

    :rst:`lineno-start`
        Start line numbers with <start-number>.

    :rst:`emphasize-lines`
        <emphasized-line-numbers> contains a comma separated list of line numbers
        to be emphasized.

    :rst:`name`
        Set a <reference-label>. This label can be used to link from any given
        text to the specific code block. The name needs to be unique within one
        manual.

    See also the official
    `sphinx documentation on code-blocks <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-code-block>`__.

Examples
========

A simple code block with syntax highlighting
--------------------------------------------

..  tabs::

    ..  group-tab:: Source (rst)

        ..  code-block:: rst
            :caption: Documentation/MyDocs.rst

            ..  code-block:: php
                :caption: EXT:site_package/Configuration/TCA/Overrides/sys_template.php

                /**
                 * Add default TypoScript (constants and setup)
                 */
                \TYPO3\CMS\Core\Utility\ExtensionManagementUtility::addStaticFile(
                     'site_package',
                     'Configuration/TypoScript',
                     'Site Package'
                );

    ..  group-tab:: Output

        ..  code-block:: php
            :caption: EXT:site_package/Configuration/TCA/Overrides/sys_template.php

            /**
             * Add default TypoScript (constants and setup)
             */
            \TYPO3\CMS\Core\Utility\ExtensionManagementUtility::addStaticFile(
                 'site_package',
                 'Configuration/TypoScript',
                 'Site Package'
            );

Code block with line numbers and highlighting of one line
---------------------------------------------------------


..  tabs::

    ..  group-tab:: Source (rst)

        ..  code-block:: rst
            :caption: Documentation/MyDocs.rst

            ..  code-block:: php
                :caption: EXT:site_package/Configuration/TCA/Overrides/sys_template.php
                :linenos:
                :emphasize-lines: 4, 7

                /**
                 * Add default TypoScript (constants and setup)
                 */
                \TYPO3\CMS\Core\Utility\ExtensionManagementUtility::addStaticFile(
                     'site_package',
                     'Configuration/TypoScript',
                     'Site Package'
                );

    ..  group-tab:: Output

        ..  code-block:: php
            :caption: EXT:site_package/Configuration/TCA/Overrides/sys_template.php
            :linenos:
            :emphasize-lines: 4, 7

            /**
             * Add default TypoScript (constants and setup)
             */
            \TYPO3\CMS\Core\Utility\ExtensionManagementUtility::addStaticFile(
                 'site_package',
                 'Configuration/TypoScript',
                 'Site Package'
            );

Use code blocks containing diffs
--------------------------------

To emphasize changes that should be made:

..  tabs::

    ..  group-tab:: Source (rst)

        ..  code-block:: rst
            :caption: Documentation/MyDocs.rst

            ..  code-block:: diff
                :caption: ext_localconf.php.diff

                 <?php

                -defined('TYPO3_MODE') or die();
                +defined('TYPO3') or die();

    ..  group-tab:: Output

        ..  code-block:: diff
            :caption: ext_localconf.php.diff

             <?php

            -defined('TYPO3_MODE') or die();
            +defined('TYPO3') or die();

..  hint::
    You can use diff tools such as the
    `bartlweb diff file generator <https://tools.bartlweb.net/diff/>`__. Make
    sure to use the type :code:`unified context`

Show a directory tree
---------------------

To display an expandable directory tree, use the
:ref:`directive '.. directory-tree::' <writing-rest-directory-tree>`.

..  tabs::

    ..  group-tab:: Source (rst)

        ..  code-block:: rst
            :caption: Documentation/MyDocs.rst

            ..  code-block:: none
                :caption: Page tree of directory :file:`vendor/composer`

                $ tree vendor/composer
                ├── ClassLoader.php
                ├── LICENSE
                ├── autoload_classmap.php
                ├── ...
                └── installed.json


    ..  group-tab:: Output

        ..  code-block:: none
            :caption: Page tree of directory :file:`vendor/composer`

            $ tree vendor/composer
            ├── ClassLoader.php
            ├── LICENSE
            ├── autoload_classmap.php
            ├── ...
            └── installed.json

..  _writing-rest-codeblocks-syntactically-correct:
..  _codeblocks-syntactically-correct:

Use syntactically correct code
==============================

..  attention::

    **Please: No syntax errors!**

    Syntax highlighting only works if the lexer can parse the code without
    errors. In other words: If there's a syntax error in the code the
    highlighting will not work.

    ..  tabs::

        ..  group-tab:: Correct


            ..  code-block:: rst
                :caption: Documentation/MyDocs.rst

                ..  code-block:: php

                    $a = array(
                        'one' => 1,
                        // ...
                    );


        ..  group-tab:: Wrong

            ..  code-block:: rst
                :caption: Documentation/MyDocs.rst

                ..  code-block:: php

                    $a = array(
                        'one' => 1,
                        ...
                    );

..  index:: reST directives; highlight
..  _writing-rest-codeblocks-highlight-directive:
..  _codeblocks-highlight-directive:

Highlight directive
===================

You can set the default language with the `highlight` directive. All following
code blocks will use the language as specified in the `highlight` directive for
syntax highlighting.

This language works as fall back for the outdated code blocks that do not
specify the desired language.

For TYPO3 we have adopted the convention that each reStructuredText source file
imports the :file:`Documentation/Includes.rst.txt` file at the top. And in the
included file - in general - we set PHP as default language for highlighting.
Exception: In the TypoScript manuals we are using `typoscript` as default.

..  index:: reST; Languages
..  _writing-rest-codeblocks-available-languages:
..  _writing-rest-codeblocks-available-lexers:

Available languages
===================

The following languages are supported. They can be used in a :rst:`code-block`
and a :rst:`literalinclude` directive.

..  guides:codeblock-languages::


Literalinclude
==============

A drawback of code blocks is that most editors cannot properly highlight or
indent code within code blocks. The directive :rst:`literalinclude` enables you
to store longer code blocks in an external file with the proper file extension.

The :rst:`literalinclude` directive imports the file and displays its content as
code block.


..  tabs::

    ..  group-tab:: Source (rst)

        ..  code-block:: rst
            :caption: Documentation/SiteConfiguration/Index.rst

            ..  literalinclude:: /CodeSnippets/LiteralIncludes/example.yaml
                :language: yaml
                :emphasize-lines: 5,10-13
                :linenos:

    ..  group-tab:: Output

        ..  literalinclude:: /CodeSnippets/LiteralIncludes/example.yaml
            :language: yaml
            :emphasize-lines: 5,10-13
            :linenos:

Literal includes can even be used to render the difference between files,
without having to create a diff file first:

..  tabs::

    ..  group-tab:: Source (rst)

        ..  code-block:: rst
            :caption: Documentation/SiteConfiguration/Index.rst

            ..  literalinclude:: /CodeSnippets/LiteralIncludes/example.yaml
                :diff: /CodeSnippets/LiteralIncludes/example_de.yaml

    ..  group-tab:: Output

        ..  literalinclude:: /CodeSnippets/LiteralIncludes/example.yaml
            :diff: /CodeSnippets/LiteralIncludes/example_de.yaml


See also `literalinclude directive
<http://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-literalinclude>`__.


..  _codeblocks-placeholders:

Placeholders
============

Placeholders in this context are named tags in code and
:ref:`example URLs <preventing-links>` where the exact value does not matter,
but is referenced in the surrounding documentation.
Use the *Backus-Naur form* `<placeholder-name>` for placeholders in code and
URLs, i.e. use angle brackets to encapsulate the placeholder name.

For example in PHP

..  code-block:: rst

    Set up a controller class to handle user interaction with the entity data
    model:

    ..  code-block:: php

        class <Entity>Controller extends ActionController
        {
            ..
        }

    where `<Entity>` corresponds to the entity data model class name.

or on the command line

..  code-block:: rst

    Importing a TYPO3 dump file is as simple as running:

    ..  code-block:: bash

        typo3/sysext/core/bin/typo3 impexp:import <file>

    where `<file>` can be the absolute path on the server or the relative path
    in the TYPO3 project folder.

or in an example URL

..  code-block:: rst

    The TYPO3 backend normally appends the session token ID to the URL as
    follows: :samp:`https://example.org/typo3/main?token=<token-id>`.

In the XML and HTML markup languages, which make extensive use of angle
brackets, the comment tag :html:`<!-- placeholder-name -->` is used to insert
placeholders. A `<placeholder-name>` looks like a regular element and would lead to confusion.


Outdated code block formats
===========================

For historic reasons the :rst:`:caption:` option is missing in many code blocks.
Try to add them whenever you touch the RST files. Do not add new code blocks
without a caption stating the file name. It is often very confusing for new
developers where a certain code snippet should go. The recommended file name
can help to clear this up.

We recommend that you always write the language name after the code block directive.
This makes it easier for first time contributors to adjust or copy-paste code
blocks. For historic reasons there are code blocks without an explicit language.

If you do not explicitly set the language, the default language (as set with
the :ref:`codeblocks-highlight-directive`) is used. If no highlight directive
was used, the default set in :file:`Documentation/Includes.rst.txt` is used.

In the past a simplified shorthand directive was widely used: A sentence ending
with two double colon :rst:`::`, followed by a new line and an indented
block of code. This quick syntax has several drawbacks:

*   It is confusing to developers who seldom contribute
*   We cannot give a caption and state the file name where the code should go.
*   The script language is only stated implicitly.
*   Such code blocks cannot be easily copy-pasted to use them as a foundation for your
    own code blocks.

You can change these code blocks like this:

..  code-block:: diff
    :caption: UpdateShorthandCode.diff

     The extension already contains some unit tests that extend `typo3/testing-framework`'s base
    -unit test class in directory :file:`Tests/Unit/Hooks` (stripped):

    ..  code-block:: php
        :caption: <extension_key>/Tests/Unit/Hooks/DataHandlerFlushByTagHookTest.php

          <?php
          namespace Lolli\Enetcache\Tests\Unit\Hooks;
