
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
   
This is the reST code we write::

   Message
      *
   
        + Hello
        + World!

And this is how it looks like:

   Message
      *
   
        + Hello
        + World!

     

