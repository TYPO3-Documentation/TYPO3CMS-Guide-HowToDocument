..  include:: /Includes.rst.txt
..  highlight:: rst
..  index:: reST; Tabs
..  _rest-tabs:

=====
Tabs
=====

They provide a compact way to present a topic from different perspectives, with
each perspective presented in a tab. When the reader changes tabs, this change
is synchronized in all tab content elements.

For example, if the reader is guided through the TYPO3 installation with text
and five code blocks, they could switch from Bash to Powershell instructions
in the first code block, and all subsequent code blocks would also automatically
switch to Powershell.

..  tabs::

    ..  group-tab:: bash

        ..  code-block:: bash

            composer create-project typo3/cms-base-distribution:^11 example-project-directory

    ..  group-tab:: powershell

        ..  code-block:: powershell

            composer create-project "typo3/cms-base-distribution:^11" example-project-directory

..  tabs::

    ..  group-tab:: bash

        ..  code-block:: bash

            touch example-project-directory/public/FIRST_INSTALL

    ..  group-tab:: powershell

        ..  code-block:: powershell

            echo $null >> public/FIRST_INSTALL

..  code-block:: rst

    ..  tabs::

        ..  group-tab:: bash

            ..  code-block:: bash

                composer create-project typo3/cms-base-distribution:^11 example-project-directory

        ..  group-tab:: powershell

            ..  code-block:: powershell

                composer create-project "typo3/cms-base-distribution:^11" example-project-directory

    ..  tabs::

        ..  group-tab:: bash

            ..  code-block:: bash

                touch example-project-directory/public/FIRST_INSTALL

        ..  group-tab:: powershell

            ..  code-block:: powershell

                echo $null >> public/FIRST_INSTALL

As an example, tabs are used in the Getting Started Guide in the chapter
:ref:`Installation <t3start:install>`.
