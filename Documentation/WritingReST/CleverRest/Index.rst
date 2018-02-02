
.. include:: ../../Includes.txt
.. highlight:: rst

.. _Clever-reST:

====================
Clever reST
====================

Place LIST in EMPTY LIST ITEM in DEFINITION DESCRIPTION
=======================================================

This is what we want to achieve:

.. code-block:: html

   <dl>
      <dt>
         Message
      </dt>
      <dd>
         <ul>
            <li>
               <!-- WE DON'T WANT OTHER TEXT HERE -->
               <ul>
                  <li>Hello</li>
                  <li>World!</li>
               </ul>
            </li>
         </ul>
      </dd>
   </dl>   
   
This is the reST code we write. `Message` is going to be the definition term DT
because (1) the next line is NOT empty (2) and it is indented. That creates a
definition list DL. Then we use the star `*` to open a list item LI of an
unorder list UL. The list item consists of nothing but a nested list for
which we are using the plus sign `+`. As usual the nested list is preceded
by (at least) one empty line and it is indented. The empty lines 6 and 11
are optional.

.. code-block:: rst
   :lineos:
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

     

