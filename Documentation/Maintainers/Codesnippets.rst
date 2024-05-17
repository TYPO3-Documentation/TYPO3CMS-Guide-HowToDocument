..  include:: /Includes.rst.txt
..  _codesnippet-generation:

=======================
Code snippet generation
=======================

..  todo: Document how to create additional code snippets

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

            # in repositories where the composer.lock is not in version control
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
