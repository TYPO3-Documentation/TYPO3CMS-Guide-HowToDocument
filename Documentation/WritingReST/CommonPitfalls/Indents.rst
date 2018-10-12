. include:: ../../Includes.txt
.. highlight:: rst


=====================
Problems with indents
=====================


Common mistake #1: Incorrect indents
====================================

Always indent correctly (3 spaces per level)

Correct syntax
--------------

::

   .. image:: ../../images/a4.jpg
      :width: 100px
      :class: with-shadow

How it looks:

   .. image:: ../../images/a4.jpg
      :width: 100px
      :class: with-shadow

Incorrect syntax
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