.. include:: ../Includes.txt
.. highlight:: rst

.. _writing-doc-for-ext-from-scratch:


=================================
Create documentation from scratch
=================================

If necessary, ask for help as explained in :ref:`how-to-get-help`.

.. rst-class:: bignums-xxl

1. Clone sample extension manual

   In a temporary directory, clone the Github project
   `sample extension manual <https://github.com/TYPO3-Documentation/TYPO3CMS-Example-ExtensionManual>`__

   .. code-block:: bash

      git clone https://github.com/TYPO3-Documentation/TYPO3CMS-Example-ExtensionManual.git

   Move or copy the files so that the Documentation folder is a direct
   subfolder of your extension, e.g.

   .. code-block:: bash

      cp -r TYPO3CMS-Example-ExtensionManual/Documentation <extension-directory>/
      # cp .gitignore (make sure you don't accidentally overwrite existing one though!)
      cp -n TYPO3CMS-Example-ExtensionManual/.gitignore <extension-directory>/.gitignore

2. Edit the documentation

   Start editing away. Use the existing text to guide you, look at other
   extension manuals for inspiration. Checkout the section on
   :ref:`reST <Formatting-with-reST>` to see how to format headlines,
   code-blocks, images etc.

3. Render the documentation (locally)

   Before you want to publish your changes, make sure the documentation is rendered
   correctly.

   Look at :ref:`rendering-docs-quickstart` for a quick start.

4. When you are done, publish your changes

   If you are working on your own 3rdparty extension, make it publicly available.
   The documentation will then automatically be rendered on docs.typo3.org.

   If you are working on the documentation for a 3rdparty extension, create
   a patch or pull request depending on where it is hosted. Creating a Pull
   Requests for projects hosted on Github is very well documented. Also, take
   a look at the contribution guidelines of the extension, if available.

