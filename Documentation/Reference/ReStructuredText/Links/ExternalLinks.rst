:navigation-title: External URLs
..  include:: /Includes.rst.txt

..  index:: reST; External links
..  _external-links:

==============
External links
==============

..  important::

    Do not use this mechanism (external links) for links to sections of
    the TYPO3. Use references as described in the section above:
    :ref:`References to TYPO3 manuals <rest-reference>`.


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
