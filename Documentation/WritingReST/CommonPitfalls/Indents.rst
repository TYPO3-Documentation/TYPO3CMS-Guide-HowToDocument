.. include:: /Includes.rst.txt
.. highlight:: rst
.. index:: reST; Indentation

=====================
Problems with indents
=====================


Common mistake #1: Incorrect indents
====================================

Always indent correctly (4 spaces per level)


Correct syntax
--------------

..  code-block:: rst

   .. image:: /Images/a4.jpg
      :width: 100px
      :class: with-shadow

How it looks:

.. image:: /Images/a4.jpg
   :width: 100px
   :class: with-shadow


Incorrect syntax
----------------

Here, `:width:` is indented with only 2 spaces. The image will not be
rendered at all!

..  code-block:: rst

   .. image:: /Images/a4.jpg
      :width: 100px
      :class: with-shadow

How it looks:


.. image:: /Images/a4.jpg
   :width: 100px
   :class: with-shadow
