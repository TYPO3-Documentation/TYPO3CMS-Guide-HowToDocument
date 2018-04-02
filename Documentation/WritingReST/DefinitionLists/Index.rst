
.. include:: ../../Includes.txt
.. highlight:: rst

.. _Styled-Definition-Lists:

=======================
Styled Definition Lists
=======================


List style "dl-parameters"
==========================

This list style is used in TYPO3 documentation to style the explanation
and description of parameters. The general markup we use is that of a "definition list".

Example 1: No extra styling
---------------------------

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


Example 2: Nicely styled
------------------------

Source::

   .. rst-class:: dl-parameters

   parameterAbc
      :sep:`|` :aspect:`Condition:` required
      :sep:`|` :aspect:`Type:` string
      :sep:`|` :aspect:`Default:` ''
      :sep:`|`

      Text describing parameterAbc ...

   parameterBcd
      :sep:`|` :aspect:`Condition:` optional
      :sep:`|` :aspect:`Type:` boolean
      :sep:`|` :aspect:`Default:` false
      :sep:`|`

      Text describing parameterBcd ...


Rendering result:

   .. rst-class:: dl-parameters

   parameterAbc
      :sep:`|` :aspect:`Condition:` required
      :sep:`|` :aspect:`Type:` string
      :sep:`|` :aspect:`Default:` ''
      :sep:`|`

      Text describing parameterAbc ...

   parameterBcd
      :sep:`|` :aspect:`Condition:` optional
      :sep:`|` :aspect:`Type:` boolean
      :sep:`|` :aspect:`Default:` false
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
`<span class="sep">|</span>`. The "keyword:" part is marked up specially
as well just to give it the ":aspect:" textrole Our css uses the classes to
give the whole construct a nice styling.

Attention:

The textroles `ascpect` and `sep` (for separator) need to be defined. The usual
way of defining them is by having these lines in the
:file:`Documentation/Includes.txt` file. Add these lines::

   .. role:: aspect (emphasis)
   .. role:: sep (strong)

Sphinx already comes with standard textroles 'emphasis' and 'strong'. 'aspect'
and 'sep' inherit their properties and are further specialized.

Example 3: Nicely styled though labels interfere
------------------------------------------------

Let's say you want to place labels in front of each definition list
item. This creates anchors you can link to symbolically with the
Sphinx "instersphinx" procedure. A downside is that this will
intercept the list. Instead, many lists are created. This isn't
a problem, if you repeat the 'rst-class' line.


Source::

   .. _label-parameterAbc:
   .. rst-class:: dl-parameters

   parameterAbc
      :sep:`|` :aspect:`Condition:` required
      :sep:`|` :aspect:`Type:` string
      :sep:`|` :aspect:`Default:` ''
      :sep:`|`

      Text describing parameterAbc ...

   .. _label-parameterBcd:
   .. rst-class:: dl-parameters

   parameterBcd
      :sep:`|` :aspect:`Condition:` optional
      :sep:`|` :aspect:`Type:` boolean
      :sep:`|` :aspect:`Default:` false
      :sep:`|`

      Text describing parameterBcd ...


Rendering result:

   .. _label-parameterAbc:
   .. rst-class:: dl-parameters

   parameterAbc
      :sep:`|` :aspect:`Condition:` required
      :sep:`|` :aspect:`Type:` string
      :sep:`|` :aspect:`Default:` ''
      :sep:`|`

      Text describing parameterAbc ...

   .. _label-parameterBcd:
   .. rst-class:: dl-parameters

   parameterBcd
      :sep:`|` :aspect:`Condition:` optional
      :sep:`|` :aspect:`Type:` boolean
      :sep:`|` :aspect:`Default:` false
      :sep:`|`

      Text describing parameterBcd ...

Link example:

Source::

   Here we link to :ref:`A link text for parameterAbc <label-parameterAbc>`.

   Here we link to :ref:`A link text for parameterBcd <label-parameterAbc>`.

Result:

   Here we link to :ref:`A link text for parameterAbc <label-parameterAbc>`.

   Here we link to :ref:`A link text for parameterBcd <label-parameterAbc>`.

