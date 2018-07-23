.. include:: ../Includes.txt
.. highlight:: rst

.. _general-conventions-menu-hierarchy:

==============
Menu hierarchy
==============

The file hiearchy on disc does not affect the menu hierarchy in any way. But, as a general
convention, we use the common practice that the file hierarchy reflects the menu
hierarchy.

So, the menu structure  for the files described under
:ref:`general-conventions-dir-and-filenames`

.. code-block:: none

  Documentation/
  |
   --> Index.rst
  |
   --> Topic1/
         |
         -> Index.rst
         -> Subtopic1.rst
         -> Subtopic2.rst


would look something like this:

**Documentation/Index.rst:**

.. code-block:: none

   .. toctree::
      :hidden:

      Topic1/Index


**Documentation/Topic1/Index.rst**

.. code-block:: none

   .. toctree::
      :hidden:

      Subtopic1
      Subtopic2


See :ref:`example-toctree` to see how this is rendered.

.. image:: ../images/toctree.png
   :class: with-shadow

