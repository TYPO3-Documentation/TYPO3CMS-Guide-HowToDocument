..  include:: /Includes.rst.txt
..  index:: reST; Versions
..  _rest-versions:

========
Versions
========

We have 3 directives to mark versions in the manuals.

The incentive is that information which is important for migration can be marked
and semi-automatically be removed after one or two versions.

..  seealso::

    *   :ref:`update-docs`
    *   :ref:`version-hints`
    *   `The version directives in the Sphinx Docu <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-versionadded>`__

Versionadded
============

..  code-block:: rest

    ..  versionadded:: 10.2
        Starting with TYPO3 10.2 hooks and signals have been replaced by a PSR-14 based
        event dispatching system.

..  versionadded:: 10.2
    Starting with TYPO3 10.2 hooks and signals have been replaced by a PSR-14 based
    event dispatching system.

For emphasis, the directive can also be placed into one of the
:ref:`admonitions <rest-admonitions>`:


..  code-block:: rest

    ..  tip::
        ..  versionadded:: 10.2
            Starting with TYPO3 10.2 hooks and signals have been replaced by a PSR-14 based
            event dispatching system.

..  tip::
    ..  versionadded:: 10.2
        Starting with TYPO3 10.2 hooks and signals have been replaced by a PSR-14 based
        event dispatching system.

Deprecated
==========

..  code-block:: rest

    ..  deprecated:: 10.2
        The hook shown here is deprecated since TYPO3 10.2 - use a custom
        :ref:`PSR-15 middleware<request-handling>` instead.

..  deprecated:: 10.2
    The hook shown here is deprecated since TYPO3 10.2 - use a custom
    :ref:`PSR-15 middleware<request-handling>` instead.

Versionchanged
==============

..  code-block:: rest

    ..  versionchanged:: 10.4.34
        The bug ... was fixed with version 10.4.23 ...

..  versionchanged:: 10.4.34
    The bug ... was fixed with version 10.4.23 ...
