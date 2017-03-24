
.. include:: ../../Includes.txt
.. highlight:: rst

==============
Special Styles
==============

((to be written))

On this page:

.. contents::
   :local:
   :backlinks: top


With theme **t3SphinxThemeRtd**:

classes::

   .. rst-class:: with-border
   .. rst-class:: with-shadow
   .. rst-class:: compact-list (?)

   
Demo docs
=========

- https://docs.typo3.org/typo3cms/drafts/github/TYPO3-Documentation/t3SphinxThemeRtdDemoDocs/

More
====
   
...

Lists as Buttons
================

((to be written))

((...))
-------

To have an unordered list appear as sequence of buttons you may specify
one of the following CSS classes immediately before the list:
`.horizbuttons-typo3-xxxl` ("typo3" means TYPO3 color),
`.horizbuttons-typo3-xxl`,
`.horizbuttons-typo3-xl`,
`.horizbuttons-green-xxxl`, 
`.horizbuttons-green-xxl`,
`.horizbuttons-green-xl`,

.. note::

   With pure Docutils the directive for specifying CSS classes is `class`.
   With Sphinx you have to use `.. rst-class:: ...` instead because `class`
   is already used in the Sphinx-Python-domain.
  
   
.horizbuttons-typo3-xxxl
~~~~~~~~~~~~~~~~~~~~~~~~

Source
""""""
.. code-block:: rst

   .. rst-class:: horizbuttons-typo3-xxxl

   - Go to `ONE <#>`__
   - Go to `TWO <#>`__
   - Go to `THREE <#>`__

Result
""""""
.. rst-class:: horizbuttons-typo3-xxxl

- Go to `ONE <#>`__
- Go to `TWO <#>`__
- Go to `THREE <#>`__

.horizbuttons-typo3-xxl
~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: horizbuttons-typo3-xxl

- Go to `ONE <#>`__
- Go to `TWO <#>`__
- Go to `THREE <#>`__

.horizbuttons-typo3-xl
~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: horizbuttons-typo3-xl

- Go to `ONE <#>`__
- Go to `TWO <#>`__
- Go to `THREE <#>`__

.horizbuttons-green-xxxl
~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: horizbuttons-green-xxxl

- Go to `ONE <#>`__
- Go to `TWO <#>`__
- Go to `THREE <#>`__

.horizbuttons-green-xxl
~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: horizbuttons-green-xxl

- Go to `ONE <#>`__
- Go to `TWO <#>`__
- Go to `THREE <#>`__

.horizbuttons-green-xl
~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: horizbuttons-green-xl

- Go to `ONE <#>`__
- Go to `TWO <#>`__
- Go to `THREE <#>`__


