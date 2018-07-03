
.. include:: ../../Includes.txt


.. _Intersphinx-How-to-link-to-topics-of-other-manuals:

===================================================
Intersphinx: How to link to topics of other manuals
===================================================


Cross-referencing
=================

See the `Sphinx documentation 
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

Example:

We are linking to a label ```:ref:`columns-inline` ``` (= referencing a target in an 
arbitrary file of the same manual). But since this belongs to a different manual, we 
need to prefix the name of that manual: ```:ref:`t3tca:columns-inline` ``` That name 
`t3tca` is the name we have given it ourselves in the Settings.cfg in the FAL manual. 
This is called cross-referencing with the intersphinx mechanism.

With ```:ref:`t3tca:columns-inline` ``` the linktext shown will be whatever the text 
of the headline is that follows the label *in the manual we link to*, in this case 
the TCA manual. Since we want to control the linktext ourselves in the FAL manual 
we can do so by writing ```this is our linktext <:ref:`t3tca:columns-inline>` ```.

Understanding the benefits
--------------------------
The TCA manual has been reworked. Text and maybe urls changed, but the - purely - 
symbolic label has been kept. As a result the links (= intersphinx references) in foreign
manuals will work again as soon they are rebuild.

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
