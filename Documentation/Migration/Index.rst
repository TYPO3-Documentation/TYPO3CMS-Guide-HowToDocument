..  include:: /Includes.rst.txt
..  index::
    Documentation; Migration
    docs.typo3.org
..  _migrate:

=============================================
Migration: From Sphinx to PHP-based rendering
=============================================

..  note::

    Since the beginning of 2024 you can switch to the new, PHP-based reStructured
    Text rendering to try it out. The new rendering will become mandatory in
    August 2024.

The main difference compared to the Sphinx rendering is that the PHP-based rendering
requires a file called :file:`Documentation/guides.xml` for configuration.
The Sphinx rendering required a file called :file:`Documentation/Settings.cfg`.
In the transition period the GitHub action of the official rendering process detects if a file called
:file:`Documentation/guides.xml` is present and then automatically switches to the
PHP-based rendering.

..  _migrate_guides_xml:

Create the settings file :file:`Documentation/guides.xml`
=========================================================

The Docker container for the PHP-based rendering additionally consists out of
a migration tool. This tool can be used to automatically create a
:file:`Documentation/guides.xml` based on the information contained in your
:file:`Documentation/Settings.cfg`.

`Docker <https://docs.docker.com/install/>`__ (or a drop-in replacement like
`Podman <https://podman.io>`__) needs to be installed on your
operating system for the tool to work:

..  tabs::

    ..  group-tab:: Docker

        ..  code-block:: bash

            docker run --rm --pull always \
              -v $(pwd):/project \
              -it ghcr.io/typo3-documentation/render-guides:latest \
              migrate Documentation

    .. group-tab:: Podman

        ..  code-block:: bash

            podman run --rm --pull always \
              -v $(pwd):/project \
              -it ghcr.io/typo3-documentation/render-guides:latest \
              migrate Documentation


The last parameter (:bash:`Documentation`) is the name of the directory, where your
:file:`Settings.cfg` is currently placed in.

After the migration is performed, you will see some output in the terminal about which settings were
converted, if some old settings were discarded, or errors occurred. When you see this:

..  code-block:: text
    :caption: Output of the command

    Note: Some of your settings could not be converted:
        * html_theme_options
        * project_discussions
        * use_opensearch

everything went well. They can be ignored since these files are usually files that
not need to be converted. You can now delete :file:`Settings.cfg`. If you ever should need it again it is still in the Git history. Also delete
file :file:`genindex.rst` in your Documentation directory (if available).

Try out the rendering locally
=============================

Use our Docker container to render your documentation locally. Read more about it in
:ref:`local rendering <rendering-docs>`.

..  _migrate-detailed-steps:

Further steps to adapt to the PHP-based rendering
=================================================

You should perform the following tasks to conclude the migration to the
PHP-based rendering tool:

..  rst-class:: bignums

#.  Manual modifications of the :file:`guides.yml`

    You have to manually change the following: in the :xml:`<extension>` tag add the attribute

        ..  code-block:: text
            :caption: Changes in your :file:`guides.yml`

            interlink-shortcode="my-vendor/my-extension"

    You can find the package name in your :file:`composer.json` file under "name".
    For example, :json:`my-vendor/my-extension`.
    We recommend to reformat the code, for example in PhpStorm, using the Mac shortcut
    :kbd:`cmd (⌘)` + :kbd:`option/alt (⌥)` + :kbd:`L`, or :kbd:`Ctrl` + :kbd:`Alt` + :kbd:`L`
    on Windows/Linux and to use for every attribute one line.


#.  Improve your documentation to render without warning

    Rendering your documentation should not yield any warnings or errors.

    If you get error messages, often they refer to wrong indentation, missing
    :ref:`interlinks <settings-guides-interlink-mapping>`, orphaned files or
    outdated ReST identifiers.

    If you are unable to address a warning/error with changes in your documentation
    feel free to ask in Slack channel #typo3-documentation (see :ref:`how-to-get-help`).

    If you believe you found a specific bug in the PHP-based rendering, please open
    an `issue on GitHub <https://github.com/TYPO3-Documentation/render-guides/issues>`__.

#.  Remove outdated files

    After the :file:`guides.xml` file has been created, you can remove the old
    :file:`Settings.cfg` file.

    You can also delete the :file:`genindex.rst` file which was previously used
    to generate an index.

#.  Adapt :file:`Includes.rst.txt`

    The main documentation directory can contain a file :file:`Includes.rst.txt`
    to include any fixed text, which will be placed on every page of your rendered
    documentation.

    Previously, it was also used to define a list of utilized directives/roles.

    You can either remove that file, or add your fixed text to it. If you remove
    the file, remember to also remove all references pointing to that file, like:

    ..  code-block:: text
        :caption: Documentation/Index.rst

        ..  include:: /Includes.rst.txt

    Most official documentation uses this as the stub of the file:

    ..  code-block:: text
        :caption: Documentation/Includes.rst.txt

        ..  You can put central messages to display on all pages here

#.  Remove the entry `genindex` from :file:`Index.rst` (Index/Glossary)

    If you previously had a :file:`genindex.rst` file, this optional index
    (or glossary) was rendered as a page through an entry in the file :file:`Index.rst`
    like this:

    ..  code-block:: diff
        :caption: Documentation/Index.rst

         .. toctree::
            :hidden:

            Sitemap
        -   genindex

    Remove the entry `genindex` from the list.

    ..  hint::

        See :ref:`migrate-glossary` for details about the future of the
        index (glossary) generation.

#.  Avoid code snippets with :file:`.rst` extension

    All files with the extension :file:`.rst` will be interpreted by the PHP-based
    rendering, and every file that is just a code snippet placed in an external file
    should be renamed to use a :file:`.rst.txt` extension instead.

Recommendations
===============

The following list is not a requirement to utilize the PHP-based rendering, but
follows "best practice" to make the most of your documentation project.

..  _migrate-to-makefile:

Add a :file:`Makefile` to your project
--------------------------------------

A :file:`Makefile` is a simple command line runner configuration file, which requires
the utility `GNU make <https://www.gnu.org/software/make/manual/make.html>`_
to be available on your Unix-based operating system (Linux, macOS, WSL on Windows,
for example).

This allows you to perform shortcuts to render your documentation instead
of typing a long :bash:`docker run...` or :bash:`podman run...` command:

..  code-block:: shell

    make docs

You should see something like this

.. code-block:: text

    Successfully placed 7 rendered HTML, SINGLEPAGE, and INTERLINK files into /project/Documentation-GENERATED-temp

..  _migrate-possible-errors:

Possible errors using `make docs`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We provide four example errors to guide you through the fixes.

..  _migrate-interlink-inventory-not-found:

Interlink inventory not found: HTTP/2 404
"""""""""""""""""""""""""""""""""""""""""

.. code-block:: text

    [2024-03-13T12:22:50.661532+00:00] app.WARNING: Interlink inventory not found: HTTP/2 404
    returned for "https://docs.typo3.org/m/typo3/book-extbasefluid/11.5/en-us/objects.inv.json". [] []

Here you see that the link `https://docs.typo3.org/m/typo3/book-extbasefluid/11.5/en-us` is not found (404 page).
We can now check via Google if there is another link to book Extbasefluid. We found this site `https://docs.typo3.org/m/typo3/book-extbasefluid/10.4/en-us/`
We can find the hint: `This manual is no longer being maintained for TYPO3 versions 11.5 and above.`. This tells us that the Documentation Team abandoned this
manual. We can, for example, link to the last existing version. Which is 10.4. To do this we have to change the :file:`guides.xml`. Search for the

.. code-block:: xml

    <inventory id="t3extbasebook"
           url="https://docs.typo3.org/m/typo3/book-extbasefluid/11.5/en-us/"
    />

and change `11.5` to `10.4`. Generate files again. Keep in mind, that this is a
workaround to avoid warnings temporarily. References to outdated manuals should be adjusted
as soon as possible.


..  _migrate-inventory-link-with-key-not-found:

Inventory link with key ... not found
"""""""""""""""""""""""""""""""""""""

.. code-block:: text

    [2024-03-13T12:26:40.940930+00:00] app.WARNING: Inventory link with key "h2document:rest-common-pitfalls"
    (rest-common-pitfalls) not found.  {"rst-file":"GeneratedExtension/Index","type":"ref","targetRef

We see already that we have to go to file :file:`GeneratedExtension/Index` in the directory "Documentation".
In there we have to delete the line which contains

.. code-block:: text

    * :ref:`h2document:rest-common-pitfalls`

But whether we should delete the reference or not depends on the special case. In this case the whole section was removed.
So here it is useful to delete the reference.
We conclude: In general it depends on the case itself what the best solution is.

..  _migrate-nested-php-domain-components-not-supported:

Nested PHP domain components (php:class, php:interface, php:enum etc) are not supported
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

.. code-block:: text

    [2024-03-25T13:26:11.600367+00:00] app.WARNING: Nested PHP domain components
    (php:class, php:interface, php:enum etc) are not supported.
    Found php:\Vendor\MyExtension\Interfaces\RequireJsModuleInterface inside
    \Vendor\MyExtension\Interfaces\AnotherImportantInterface {"rst-file":"Developer/Index.rst"} []

The file :file:`Index.rst` in :file:`Documentation/Developer/` has a wrong indentation. A class must not belong to another class.
Here is the wrong rst code.

.. code-block:: rst

    ..  php:class:: AnotherImportantInterface

        Used for ...

        ..  php:class:: RequireJsModuleInterface

        Widgets implementing this interface will add the provided RequireJS modules.
        Those modules will be loaded in dashboard view if the widget is added at least once.

Additionally regarding the name it has to be interfaces and not classes.
:rst:`..  php:class:: ExampleInterface` has to be changed to :rst:`..  php:interface:: ExampleInterface`.


..  _migrate-reference-could-not-be-resolved:

Reference sitehandling-addinglanguages could not be resolved in LocalizedContent/Index {"rst-file":"LocalizedContent/Index"} []
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

The next step is to visit the site which was rendered with the Sphinx rendering, in our example
`https://docs.typo3.org/m/typo3/guide-frontendlocalization/main/en-us/LocalizedContent/Index.html`.
There we can search for `sitehandling-addinglanguages` in the restructured text code by clicking the button "`</> View Source`".
We have found this:

.. code-block:: rst

    ..  tip::
        For more information on how to add languages and configure their
        behaviour in the site configuration, see
        :ref:`Adding Languages <sitehandling-addinglanguages>`.

The link is leading to
`https://docs.typo3.org/m/typo3/reference-coreapi/main/en-us/ApiOverview/SiteHandling/AddLanguages.html#sitehandling-addinglanguages`.
We have to click the symbol next to the heading and copy the correct link
which is the one for restructured text

.. image:: /Images/get_link.png
    :class: with-shadow
    :width: 600px

.. code-block:: rst

    :ref:`Adding Languages <t3coreapi:sitehandling-addingLanguages>`

You have to replace the correct link in, for example, :file:`Documentation/LocalizedContent/Index.rst` to
fix the error. Note: Since we already migrated the Frontend Localization Guide
(`https://docs.typo3.org/m/typo3/guide-frontendlocalization/main/en-us/LocalizedContent/Index.html`)
to use the PHP-based rendering you cannot find the state that we have shown above anymore.

..  _migrate-makefile-example-code:

Makefile example
~~~~~~~~~~~~~~~~

For inspiration, check out the :file:`Makefile` of the main PHP-based rendering
repository:

https://github.com/TYPO3-Documentation/render-guides/blob/main/Makefile

A small example :file:`Makefile`:

..  literalinclude:: /CodeSnippets/_Makefile
    :language: plaintext
    :caption: Makefile

..  hint::

    Makefile blocks need to be indented with a TAB character, not spaces.
    If your project comes with an :ref:`editorconfig` definition for
    code formatting, you should add the following:

    ..  code-block:: text

        [Makefile]
        # Use tabs for indentation (Makefiles require tabs)
        indent_style = tab


..  _migrate-to-testing-workflow:

Activate automatic testing in your project
------------------------------------------

It is recommended to use an automatic workflow on GitHub Or GitLab to
ensure the extension's documentation renders without warnings.

An example workflow on GitHub would be established via this file in
:file:`.github/workflows/documentation.yml`:

..  literalinclude:: /CodeSnippets/_documentation.yml
    :caption: .github/workflows/documentation.yml


This creates a workflow entry `Test documentation`, so that on every push to your
repository, and every pull request, the rendering is executed. A commit will then
not be possible, if the rendering fails. The workflow run will be marked with an error,
and shown on pull requests.

..  _migrate-glossary:

To be discussed: Index generation (glossary)
============================================

The Sphinx rendering allowed to utilize a syntax like the following to
add indexes to your documentation:

..  code-block:: plaintext
    :caption: Documentation/Index.rst

    ..  index::
        XLIFF; Files
        File; XLIFF

The automatically generated file :file:`genindex.html` would show a
two-column layout of all indexes, with the pages that they were used on.

The PHP-based rendering does not (yet) support this indexing.

The current recommendation is to only remove the :file:`genindex.rst` file
from your documentation directory, but keep all the placed `..  index`
directives. If at some point the automatic index generation is re-introduced,
your old indexes will be able to show up again.
