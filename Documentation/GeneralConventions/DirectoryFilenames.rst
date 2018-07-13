.. include:: ../Includes.txt
.. highlight:: rst

.. _general-conventions-dir-and-filenames:

========================
Directory and file names
========================

* All documentation resides in a :file:`Documentation` subfolder
* This folder contains the files Settings.cfg, Includes.txt and Index.rst
* Use CamelCase for file and directory names.
* reSt files have ending .rst
* Included files have ending .rst.txt


.. code-block:: none

  Documentation/
  |
   --> Settings.cfg
  |
   --> Includes.txt
  |
   --> Index.rst
  |
   --> Topic1/
         |
         -> Index.rst
         -> Subtopic1.rst
         -> Subtopic2.rst

If the documentation follows these conventions, the documentation rendering toolchain
automatically detects the documentation and renders it correctly on the documentation
server.
