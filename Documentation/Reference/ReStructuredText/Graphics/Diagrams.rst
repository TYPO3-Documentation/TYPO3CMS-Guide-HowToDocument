..  include:: /Includes.rst.txt
..  index::
    ! Diagrams
    Diagrams; PlantUML
..  _PlantUML-diagrams:

=================
PlantUML diagrams
=================

In order to render diagrams in the TYPO3 documentation,
`PlantUML <https://plantuml.com/>`_ is integrated into the rendering process.

Basic diagrams can be embedded directly into the reStructuredText markup:

..  code-block:: rst
    :caption: Documentation/SomeFile.rst

    ..  uml::
        :caption: Some Caption

        class -> otherClass : message

This will be rendered as:

..  uml::
    :caption: Some Caption

    class -> otherClass : message

..  _PlantUML-diagrams-included:

Include a PlantUML file
=======================

..  code-block:: rst
    :caption: Documentation/SomeFile.rst

    ..  uml:: _complex_uml.plantuml
        :align: center
        :caption: Figure 1-1: Application flow
        :width: 1000

This will be rendered as:

..  uml:: _complex_uml.plantuml
    :align: center
    :caption: Figure 1-1: Application flow
    :width: 1000

Put a file called :file:`_complex_uml.plantuml` in the same directory as
the reST file:

..  literalinclude:: _complex_uml.plantuml
    :caption: Documentation/_complex_uml.plantuml
    :language: text
