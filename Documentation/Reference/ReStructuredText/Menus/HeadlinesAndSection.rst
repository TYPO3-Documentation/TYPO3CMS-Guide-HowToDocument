:navigation-title: Headlines

..  include:: /Includes.rst.txt
..  index::
    pair: reST; Headlines
    pair: reST; Titles
    pair: reST; Sections
..  _headlines-and-sections:

=====================
Headlines and anchors
=====================

Each reST document must have a title. It is overlined and underlined like this:

..  code-block:: rst

    ..  _rest-cheat-sheet:

    =============================
    Cheat sheet: reStructuredText
    =============================

The anchor is used for permalinks. It should be lowercase with dashes between
words. During rendering special signs are converted into dashes and all letters changed to
lowercase if you ignore this.
Start a new anchor with the anchor of its section, see
`Naming a new anchor <https://docs.typo3.org/permalink/h2document:link-anchor-new>`_.

Use headers to divide your document into sections. Start with h2:

By convention we use the following underlines:

..  literalinclude:: /_CodeSnippets/_Headers.rst.txt
    :caption: Documentation/MyDocs.rst

Further headline levels are possible:

..  code-block:: rst

    ..  _h4-headline:

    H4 headline
    ~~~~~~~~~~~

    ..  _h5-headline:

    H5 headline
    """""""""""

    ..  _h6-headline:

    H6 headline
    '''''''''''

    ..  _another-h2-headline:

    Another H2 headline
    ===================

They look like this:

..  _h2-headline:

H2 headline
===========

..  _h3-headline:

H3 headline
-----------

..  _h4-headline:

H4 headline
~~~~~~~~~~~

..  _h5-headline:

H5 headline
"""""""""""

..  _h6-headline:

H6 headline
'''''''''''

..  _syntax-headlines:

Syntax of headlines
===================

Make the over- and underline as long as the headline. The rendering does not
check this.

Each headline should have an anchor. Otherwise permalinking does not work.

Never delete an anchor. If a concept is removed without substitute, move the
anchor to a special page that says when and why the concept was removed. See
`Keeping anchors working <https://docs.typo3.org/permalink/h2document:anchor-persistence>`_.
