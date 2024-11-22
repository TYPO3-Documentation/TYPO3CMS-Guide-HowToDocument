..  include:: /Includes.rst.txt
..  index:: reST; Versions
..  _rest-versions:
.. _version-hints:

========
Versions
========

We have 3 directives to mark versions in the manuals.

The incentive is that information which is important for migration can be marked
and semi-automatically be removed after one or two versions.

Versionadded
============

..  code-block:: rst

    ..  versionadded:: 10.2
        Starting with TYPO3 10.2 hooks and signals have been replaced by a PSR-14 based
        event dispatching system.

..  versionadded:: 10.2
    Starting with TYPO3 10.2 hooks and signals have been replaced by a PSR-14 based
    event dispatching system.

For emphasis, the directive can also be placed into one of the
:ref:`admonitions <rest-admonitions>`:


..  code-block:: rst

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

..  code-block:: rst

    ..  deprecated:: 10.2
        The hook shown here is deprecated since TYPO3 10.2 - use a custom
        PSR-15 middleware instead.

..  deprecated:: 10.2
    The hook shown here is deprecated since TYPO3 10.2 - use a custom
    PSR-15 middleware instead.

Versionchanged
==============

..  code-block:: rst

    ..  versionchanged:: 10.4.34
        The bug ... was fixed with version 10.4.23 ...

..  versionchanged:: 10.4.34
    The bug ... was fixed with version 10.4.23 ...
