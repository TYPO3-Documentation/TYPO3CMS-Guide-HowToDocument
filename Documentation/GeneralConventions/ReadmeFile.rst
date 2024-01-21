
.. index:: File structure; README.rst, README.rst
.. _readme-rst:
.. _about-file:

=======================================
:file:`README.rst` or :file:`README.md`
=======================================

Full documentation contains both a :file:`README.rst` and a :file:`Documentation/Index.rst`
file. To avoid redundancy in both places, the :file:`README.rst` in this case usually
contains only a summary and links to all aspects of the project, i.e. the VCS
repository, the published documentation and - if available - the TYPO3 Extension
Repository (TER) page to guide the reader to the next steps. This could be for
example:

..  tabs::

    ..  group-tab:: With placeholders

        ..  include:: /CodeSnippets/FileStructure/ReadmeRst.rst.txt

    ..  group-tab:: Third party extension

        ..  include:: /CodeSnippets/FileStructure/Examples/IndexRst.rst.txt

    ..  group-tab:: System extension

        ..  include:: /CodeSnippets/FileStructure/Dashboard/IndexRst.rst.txt

    ..  group-tab:: Official manual

        ..  include:: /CodeSnippets/FileStructure/GettingStarted/IndexRst.rst.txt

    ..  group-tab:: Markdown

        ..  include:: /CodeSnippets/FileStructure/ReadmeMd.rst.txt


.. _readme-rst-badges:

Badges
^^^^^^

Point out interesting statistics of your extension or package in the *badges*
placeholder, which should include the latest release version, the total and
monthly download rate and the supported TYPO3 versions:

..  tabs::

    ..  group-tab:: Rest

        ..  include:: /CodeSnippets/FileStructure/Badges.rst.txt

    ..  group-tab:: Markdown

        ..  include:: /CodeSnippets/FileStructure/BadgesMd.rst.txt


Remove this field if the project is no extension or package.


.. _readme-rst-project:

Project
^^^^^^^

The *project* placeholder contains the title of the project.

Common values are in the official TYPO3 manuals

#. `<Topic> Guide`, e.g. "Installation and Upgrade Guide",
   for collections of articles on a specific topic
#. `<Topic> Reference`, e.g. "TCA Reference",
   for a complete encyclopedia
#. `<Topic> Tutorial`, e.g. "Getting Started Tutorial",
   for collections of tutorials on a specific topic

and in TYPO3 system and third-party extensions

*  `TYPO3 extension <extension-key>`, e.g. "TYPO3 extension \`\`extbase\`\`" and
   "TYPO3 extension \`\`mask\`\`".


.. _readme-rst-abstract:

Abstract
^^^^^^^^

The *abstract* placeholder contains a short and precise description of the
project with as many keywords as possible in as few sentences as possible. It
helps the decision maker to quickly decide whether the project is worth
considering and whether or not to read the full documentation. It should be
aligned with the abstract of Index.rst and - if available - the description
fields of :file:`ext_emconf.php` and :file:`composer.json`.
