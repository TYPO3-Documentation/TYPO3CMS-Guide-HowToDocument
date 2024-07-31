:navigation-title: Documentation references
..  include:: /Includes.rst.txt

..  _rest-ref:
..  _intersphinx:

=================================
References to TYPO3 documentation
=================================

You can link the following elements in any TYPO3 manual: Headlines,
:ref:`confvals <rest-confval>` and :ref:`phpdomain definitions <rest-phpdomain>`.
It is also possible to put an anchor almost anywhere and then link it.

When an element in a manual can be linked a link symbol will appear when you
hover it:

..  figure:: /_Images/link-headlines.png

    Hover over a headline to see if it is linkable, then click the link icon

After you click the link icon you can copy the reST link from the modal that
appears:

..  figure:: /_Images/link-headlines-box.png

    Copy the reST reference

The reST code of the reference looks like this:

..  code-block:: rst
    :caption: Reference from another manual

    :ref:`Hide detail page in URL <georgringer/news:hideDetailPage>`

A reference has the following syntax:

..  code-block:: plaintext
    :caption: Syntax of a reST reference

    :ref:`[link_text] <[interlink]:[anchor]>`

If you are linking within the same manual you can omit the `[interlink]:` part,
including the colon.

..  code-block:: rst
    :caption: Reference from inside the same manual

    :ref:`Hide detail page in URL <hideDetailPage>`

If there is a warning box displayed, that the link has no anchor, you can
still link to it using a doc-reference:

..  figure:: /_Images/link-headlines-box-warning.png

    Linking to a headline without an anchor

The link then looks like this in reST:

..  code-block:: rst

    :doc:`Some further explanations <georgringer/news:Tutorials/BestPractice/HideDetailPage/Index#some-further-explanations>`

However such a link would not work anymore if the section was moved to another
page or if another section with the same headline was introduced.

We suggest adding a unique link anchor to the headline to be linked to in this
case. See section :ref:`Link anchors <link-targets-explanation>`.
