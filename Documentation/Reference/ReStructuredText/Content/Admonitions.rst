..  include:: /Includes.rst.txt
..  index:: reST; Admonitions
..  _rest-admonitions:

===============================================
Admonitions: Tip, Note, Warning, See also,  etc
===============================================

The following directives are called Admonitions. You
can use them to point out additional or important
information.

..  _rest-admonitions-examples:

Examples
========

..  index:: reST directives; seealso

..  _rest-admonitions-examples-see:

See also
--------

..  code-block:: rst

    ..  seealso::
        `Admonitions <http://docutils.sourceforge.net/0.7/docs/ref/rst/directives.html#admonitions>`__

..  seealso::
    `Admonitions <http://docutils.sourceforge.net/0.7/docs/ref/rst/directives.html#admonitions>`__


..  index:: reST directives; note

..  _rest-admonitions-examples-note:

Note
----

..  code-block:: rst

    ..  note::
        A note

..  note::
    A note


..  index:: reST directives; tip

..  _rest-admonitions-examples-tip:

Tip
---

..  code-block:: rst

    ..  tip::
        A tip

..  tip::
    A tip

You may also use the admonition **hint**, but this is very similar
and **tip** is more commonly used in the documentation.

..  index:: reST directives; warning

..  _rest-admonitions-examples-warning:

Warning
-------

..  code-block:: rst

    ..  warning::
        Some text pointing out something that people should be warned about.

..  warning::
    Some text pointing out something that people should be warned about.

You may also use the admonitions **caution** or even **danger** if the
severity of the warning must be stressed.


..  index:: reST directives; attention

..  _rest-admonitions-examples-attention:

Attention
---------

..  code-block:: rst

    ..  attention::
        An attention

..  attention::
    An attention


..  _rest-admonitions-information:

More Information
================

The admonitions listed here are the most commonly used in the TYPO3 documentation.

For more see `reStructuredText directives in docutils documentation <http://docutils.sourceforge.net/docs/ref/rst/directives.html#specific-admonitions>`__.
