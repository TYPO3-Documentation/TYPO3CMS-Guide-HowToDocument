
..  include:: /Includes.rst.txt
..  index::
    pair: reST; Headlines
    pair: reST; Titles
    pair: reST; Sections
..  _headlines-and-sections:

======================
Headlines and Anchors
======================


..  contents::

Each reST document must have a title. It is overlined and underlined like this:

..  code-block:: rst

    ..  _rest-cheat-sheet:

    =============================
    Cheat sheet: reStructuredText
    =============================

The anchor is used for permalinks. It should be lowercase with dashes between
words. During rendering special signs are converted into dashes and all letters changed to
lowercase if you ignore this.

Use headers to divide your document into sections. Start with h2:

By convention we use the following underlines:

..  code-block:: rst

    ..  _h2-headline:

    H2 Headline
    ===========

    ..  _h3-headline:

    H3 Headline
    -----------

    ..  _h4-headline:

    H4 Headline
    ~~~~~~~~~~~

    ..  _h5-headline:

    H5 Headline
    """""""""""

    ..  _h6-headline:

    H6 Headline
    '''''''''''

    ..  _another-h2-headline:

    Another H2 Headline
    ===================

They look like this:

..  _h2-headline:

H2 Headline
===========

..  _h3-headline:

H3 Headline
-----------

..  _h4-headline:

H4 Headline
~~~~~~~~~~~

..  _h5-headline:

H5 Headline
"""""""""""

..  _h6-headline:

H6 Headline
'''''''''''

..  _syntax-headlines:

Syntax of headlines
===================

The underlining special signs should be as long as the line but this is not
enforced.

Each headline should have an anchor. Otherwise permalinking does not work.

Keep anchors unless a concept is completely removed.
