:navigation-title: External URLs
..  include:: /Includes.rst.txt

..  index:: reST; External links
..  _external-links:

==============
External links
==============

..  tip::

    To link TYPO3 documentation, use a permalink with this syntax rather than
    the URL from the address bar of your browser. See
    :ref:`Permalinks <permalinks>`.

An URL that is mentioned within a text is automatically linked:

..  code-block:: rst

    Lorem Ipsum Dolor https://example.org dolor sit

The result looks like this:

Lorem Ipsum Dolor https://example.org dolor sit

If you want to also give the URL a distinctive link text you can use the
following syntax:

..  code-block:: rst

    Lorem Ipsum Dolor `Example Page <https://example.org>`__ dolor sit

The result looks like this:

Lorem Ipsum Dolor `Example Page <https://example.org>`__ dolor sit

Sometimes links can get quite long and unruly to use within the text. You can
use so called named links to separate the link definitions from the text:

..  code-block:: rst

    Lorem Ipsum Dolor `Example Page`_ dolor sit

    ..  _Example Page: https://example.org

The result looks like this:

Lorem Ipsum Dolor `Example Page`_ dolor sit

..  _Example Page: https://example.org
