
.. include:: ../../Includes.txt
.. highlight:: rst

.. _Clever-reST:

====================
Clever reST
====================

Place 'list' in 'empty list item' in 'definition description'
=============================================================

**Goal:**

This is what we want to achieve:

.. code-block:: html

   <dl>
      <dt>
         Message
      </dt>
      <dd>
         <ul>
            <li>
               <!-- WE DON'T WANT ANY OTHER TEXT HERE -->
               <ul>
                  <li>Hello</li>
                  <li>World!</li>
               </ul>
            </li>
         </ul>
      </dd>
   </dl>   
   
**reST source:**

This is the reST code we write. `Message` is going to be the definition term DT
because (1) the next line is NOT empty (2) AND it is indented. That creates a
definition list DL. Then we use the star `*` to open a list item LI of an
unordered list UL. The list item consists of nothing but a nested list for
which we are using the plus sign `+` - just because it looks nice. Any allowed
character would do. As usual the nested list is preceded by (at least) one empty 
line and it is indented. The empty lines 6 and 11 are optional and could be
multiple empty lines:

.. code-block:: rst
   :linenos:
   :emphasize-lines: 6,11

   Message
      *
   
        + Hello
        + World!
        
      *
   
        + Hello
        + World!
        
      *
   
        + Hello
        + World!


**Result:**

And this is how it looks like:

   Message
      *
   
        + Hello
        + World!
      *
   
        + Hello
        + World!
      *
   
        + Hello
        + World!

     
