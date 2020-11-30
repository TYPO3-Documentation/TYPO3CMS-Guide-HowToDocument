.. include:: ../Includes.txt
.. highlight:: rst

.. _diagrams:

========
Diagrams
========

In order to render diagrams in the TYPO3 documentation,
`PlantUML <https://plantuml.com/>`_ is integrated into the rendering process.

.. contents:: Types of diagrams:
   :backlinks: top
   :class: compact-list
   :depth: 1
   :local:


Activity diagram
================

.. include:: Diagrams/activity.rst.txt
.. literalinclude:: Diagrams/activity.rst.txt
   :language: rst

Docs: https://plantuml.com/activity-diagram-legacy


Class diagram
=============

.. include:: Diagrams/class.rst.txt
.. literalinclude:: Diagrams/class.rst.txt
   :language: rst

Docs: https://plantuml.com/class-diagram


Component diagram
=================

.. include:: Diagrams/component.rst.txt
.. literalinclude:: Diagrams/component.rst.txt
   :language: rst

Docs: https://plantuml.com/component-diagram


Deployment diagram
==================

.. include:: Diagrams/deployment.rst.txt
.. literalinclude:: Diagrams/deployment.rst.txt
   :language: rst

Docs: https://plantuml.com/deployment-diagram


Icons
=====

There are two ways to integrate icons into your diagrams: Either by using the
supplied *PlantUML Standard Library*, which comes with a suitable set of symbols,
or by using remote font sets. The standard library can be used for offline
rendering, while the remote font sets always contain the latest symbols.

Standard Library
----------------

The PlantUML Standard Library contains dumps of various well-known third-party
font sets such as Font Awesome (v4 and v5), Devicon, etc. The available icons
can best be searched by checking out the `project repository
<https://github.com/plantuml/plantuml-stdlib/tree/e58cee3f88e462e45d9ef0581a517a9e6dd6d69a>`_
with the release date of PlantUML v2018.13, which is used in the current
rendering process of the TYPO3 documentation.

.. include:: Diagrams/icons_stdlib.rst.txt
.. literalinclude:: Diagrams/icons_stdlib.rst.txt
   :language: rst

Remote font sets
----------------

.. note::

   Including icons this way requires an online connection during the rendering
   process.

The latest icons can be integrated directly via remote url.

.. include:: Diagrams/icons_remote.rst.txt
.. literalinclude:: Diagrams/icons_remote.rst.txt
   :language: rst

Docs: https://plantuml.com/stdlib


Maths
=====

.. include:: Diagrams/maths.rst.txt
.. literalinclude:: Diagrams/maths.rst.txt
   :language: rst

Docs: https://plantuml.com/ascii-math


Misc
====

.. include:: Diagrams/misc.rst.txt
.. literalinclude:: Diagrams/misc.rst.txt
   :language: rst

Docs: https://plantuml.com/link | https://plantuml.com/sequence-diagram


Object diagram
==============

.. include:: Diagrams/object.rst.txt
.. literalinclude:: Diagrams/object.rst.txt
   :language: rst

Docs: https://plantuml.com/object-diagram


Sequence diagram
================

.. include:: Diagrams/sequence.rst.txt
.. literalinclude:: Diagrams/sequence.rst.txt
   :language: rst

Docs: https://plantuml.com/sequence-diagram


State diagram
=============

.. include:: Diagrams/state.rst.txt
.. literalinclude:: Diagrams/state.rst.txt
   :language: rst

Docs: https://plantuml.com/state-diagram


Timing diagram
==============

.. include:: Diagrams/timing.rst.txt
.. literalinclude:: Diagrams/timing.rst.txt
   :language: rst

Docs: https://plantuml.com/timing-diagram


Use Case diagram
================

.. include:: Diagrams/use_case.rst.txt
.. literalinclude:: Diagrams/use_case.rst.txt
   :language: rst

Docs: https://plantuml.com/use-case-diagram
