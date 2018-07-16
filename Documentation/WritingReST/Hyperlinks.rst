.. include:: ../Includes.txt
.. highlight:: rst


.. _how-to-document-hyperlinks:

==============================
Hyperlinks & Cross-referencing
==============================

.. _external-links:

External links
==============

.. important::

   Do not use this mechanism (absolute URLs) for links to sections of
   the official documentation. Use the Intersphinx mechanism as described
   :ref:`intersphinx`.


Source
------

::

   `Sphinx hyperlinks <http://www.sphinx-doc.org/en/stable/rest.html#hyperlinks>`__


Result
------

`Sphinx hyperlinks <http://www.sphinx-doc.org/en/stable/rest.html#hyperlinks>`__





.. _intersphinx:


Cross-Referencing
=================

This section describes how to link to sections of the current or other
manuals correctly.


Additional information: See the `Sphinx documentation
<http://www.sphinx-doc.org/en/stable/markup/inline.html#cross-referencing-arbitrary-locations>`__.


In the same manual
------------------

Using `:ref:` is the recommended way to create links in a manual because it works across files.


A section label of the name `columns-inline` has been set somewhere::

   .. _columns-inline:

   Inline Columns
   ==============

You can then link to it like this **from the same manual**::

  :ref:`columns-inline`



From one manual to another
--------------------------

Example 1: Use text of headline as linktext
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Again, we want to link to the label `columns-inline`.

But since the label is now in a different manual, we
need to prefix the name of that manual:

.. code-block:: rest

   :ref:`t3tca:columns-inline`


The name `t3tca` is the name we have given it in the :ref:`Settings.cfg` file:

.. code-block:: none

   t3tca = https://docs.typo3.org/typo3cms/TCAReference/



This is called cross-referencing with the *intersphinx* mechanism.

In this example, the linktext shown will be whatever the text
of the headline is that follows the label *in the manual we link to*, in this case
the TCA manual.


Example 2: Specify linktext
~~~~~~~~~~~~~~~~~~~~~~~~~~~


If we want to control the linktext ourselves, we can do so by
writing:

.. code-block:: rest

   :ref:`this is our linktext <t3tca:columns-inline>`

Understanding the benefits
--------------------------
Imagine that the TCA manual has been restructured. Text and maybe urls changed, but the - purely -
symbolic label has been kept. As a result the links (= intersphinx references) in foreign
manuals will work again as soon they are rebuilt.

Tips
----

1. For convenience many manuals already have a page "Linktargets" where you can easily
   see what linktargets are available. Example: https://docs.typo3.org/typo3cms/TCAReference/Targets.html

2. As an editor you should not change or remove labels once they have been published.
   If you feel that a label (= linktarget) should be changed you should keep the old one
   and add the new one on a separate line. You cannot know whether some other manual in
   the world links to the label you would like to remove.

3. You still CAN remove that label. The only problem that may arise is that foreign links
   aren't generated any more.


