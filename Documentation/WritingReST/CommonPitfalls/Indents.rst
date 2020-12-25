.. include:: /Includes.rst.txt

.. highlight:: rst


=====================
Problems With Indents
=====================


Common mistake #1: Incorrect indents
====================================

Always indent correctly (3 spaces per level)

Correct Syntax
--------------

::

   .. image:: ../../images/a4.jpg
      :width: 100px
      :class: with-shadow

How it looks:

.. image:: ../../images/a4.jpg
   :width: 100px
   :class: with-shadow

Incorrect Syntax
----------------

Here, `:width:` is indented with only 2 spaces. The image will not be
rendered at all!

::

   .. image:: ../../images/a4.jpg
     :width: 100px
      :class: with-shadow

How it looks:


.. image:: ../../images/a4.jpg
  :width: 100px
   :class: with-shadow
