

.. highlight:: rst

=======================
Styled Definition Lists
=======================


List style "dl-parameters"
==========================

This list style is used in TYPO3 documentation to style the explanation
and description of parameters. The general markup we use is that of a "definition list". 

Example with standard styling
-----------------------------

An example with a standard styling would look like this:

Source::

   parameterAbc
      Condition: required, Type: string, Default: ''
      
      Text describing parameterAbc ...
    
   parameterBcd
      Condition: optional, Type: boolean, Default: false
      
      Text describing parameterBcd ...
      
Rendering result:

parameterAbc
   Condition: required, Type: string, Default: ''
      
   Text describing parameterAbc ...
    
parameterBcd
   Condition: optional, Type: boolean, Default: false
      
   Text describing parameterBcd ...

This markup works but isn't very readable due to the lack of styling.

The improved and styled example
-------------------------------

Source::

   .. rst-class:: dl-parameters

   parameterAbc
      :sep:`|` Condition: required
      :sep:`|` Type: string
      :sep:`|` Default: ''
      :sep:`|` 
      
      Text describing parameterAbc ...
    
   parameterBcd
      :sep:`|` Condition: optional
      :sep:`|` Type: boolean
      :sep:`|` Default: false
      :sep:`|` 
      
      Text describing parameterBcd ...


Rendering result:

   .. rst-class:: dl-parameters

   parameterAbc
      :sep:`|` Condition: required
      :sep:`|` Type: string
      :sep:`|` Default: ''
      :sep:`|` 
      
      Text describing parameterAbc ...
    
   parameterBcd
      :sep:`|` Condition: optional
      :sep:`|` Type: boolean
      :sep:`|` Default: false
      :sep:`|` 
      
      Text describing parameterBcd ...

Explanation:

Right in front of the definition list we place an 'rst-class' directive
with 'dl-parameters', meaning a definition list style for parameters.
As a result the rendered html construct will look like 
`<dl class="dl-parameters">...</dl>`. The first line of the description
is used for multiple "keyword: value" explanations. As a separator
we are using the vertical bar. And we are using a special textrole
"sep" (for separator) for it. As a result it will be rendered as
`<span class="sep">|</span>`. Our css uses the classes to give the
whole construct a nice styling.


