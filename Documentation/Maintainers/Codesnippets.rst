..  include:: /Includes.rst.txt
..  _codesnippet-generation:

=======================
Code snippet generation
=======================

..  _codesnippet-add-new:

Add a code snippet for a new class
==================================

The API section of a manual page (for example a PSR-14 event page) is
usually not written by hand: it is generated from the class's own PHP
doc-comments and method signatures by `t3docs-codesnippets
<https://github.com/TYPO3-Documentation/t3docs-codesnippets>`__, and then
included into the page with:

..  code-block:: rst

    ..  include:: /CodeSnippets/Events/Core/SomeEvent.rst.txt

To make the generator pick up a new class, register it in the manual's
:file:`Documentation/CodeSnippets/Config/` tree. For events this is one PHP
file per category, for example
:file:`Documentation/CodeSnippets/Config/Api/Events/EventsCore.php` for
:composer:`typo3/cms-core`, returning an array of entries:

..  code-block:: php
    :caption: Documentation/CodeSnippets/Config/Api/Events/EventsCore.php

    [
        'action' => 'createPhpClassDocs',
        'class' => \TYPO3\CMS\Core\Routing\Event\AfterPageUriGeneratedEvent::class,
        'targetFileName' => 'CodeSnippets/Events/Core/AfterPageUriGeneratedEvent.rst.txt',
        'withCode' => false,
    ],

..  attention::
    :file:`targetFileName` is flat per top-level category
    (:file:`CodeSnippets/Events/Core/...`), regardless of any subfolder the
    corresponding manual page itself lives in (for example
    :file:`ApiOverview/Events/Events/Core/Routing/...`). Match the existing
    files in the same category rather than mirroring the page's own path.

If there is no config file for the class's category yet, create one
following the pattern above and add it to that tree's :file:`All.php`
aggregator so it is picked up.

After adding the entry, run the class through the generator (see
:ref:`Regenerate existing code snippets <codesnippet-regeneration>` below)
to create the actual :file:`.rst.txt` file. If you cannot run the generator
locally, you can write the file by hand in the same format so the page
renders correctly in the meantime - the next real generator run will
overwrite it with equivalent content, so this is not destructive.

..  _codesnippet-regeneration:

Regenerate existing code snippets
=================================

To regenerate the existing code snippets in a manual or extension clone
the repository of that manual.

..  code-block:: bash

    git clone git@github.com:TYPO3-Documentation/TYPO3CMS-Reference-CoreApi.git


Use composer to install all dependencies,
including dev-dependencies. In official manuals we have a make command for
your convenience.

..  tabs::

    ..  tab:: Make

        ..  code-block:: bash

            make install

    ..  tab:: composer

        ..  code-block:: bash

            # in repositories with composer.lock in version control
            composer install

            # in repositories where the composer.lock is not in version control
            # to prevent outdated packages due to a local composer.lock from earlier install-runs
            composer update

Then regenerate the code snippets. Official manuals should have a make command
for that.

..  tabs::

    ..  tab:: Make

        ..  code-block:: bash

            make codesnippets

    ..  tab:: TYPO3 console command

        ..  code-block:: bash

            # Paths depends on where the vendor binaries are installed
            # And where the configuration file codesnippets.php is located

            vendor/bin/typo3 codesnippet:create Documentation/
