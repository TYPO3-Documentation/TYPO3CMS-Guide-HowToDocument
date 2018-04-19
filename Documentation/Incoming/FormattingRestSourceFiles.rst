.. include:: ../Includes.txt
.. highlight:: none

.. _Formatting-reST-Source-Files:

============================
Formatting reST Source Files
============================

((to be written))

For your own texts you can use any style you want to and that
technically works

For "official" manuals this holds::

   - use utf-8

   - the only way to include "special" characters is to use them directly
   
   - remove white space from the end of lines (= no trailing tabs or spaces)

   - don't use tabs

   - one indentenation level consists of three spaces

   - code examples use three spaces as indentation level as well
   
   - if in doubt about the length: use short lines!
     - then reST is readable as source as well
     - can be easily edited directly at Github
     - can be compared in a diff view

   - if possible, keep lines shorter than 80 characters. So lines should have
     0..79 characters, followed by newline characters.

   - if lines need to be longer for some reason add multiples of three
     since we are using indenting and outdenting by three:
        0 to 79       = strongly recommended
        0 to 91       = if something around 90 seems useful
        0 to 121      = if something around 120 seems useful

     these can be set in sublime for example.
     add screen shots (Jetbrains, Sublime, ...)

