..  include:: /Includes.rst.txt
..  index:: reST; Versions
..  _rest-versions:
..  _version-hints:

========
Versions
========

We have 3 directives to mark versions in the manuals.

The incentive is that information which is important for migration can be marked
and semi-automatically be removed after one or two versions.

..  _rest-versions-versionadded:

Versionadded
============

..  code-block:: rst

    ..  versionadded:: 10.0
        Starting with TYPO3 10.0 hooks and signals have been replaced by a PSR-14 based
        event dispatching system.
        See `Feature: #88770 - PSR-14 based EventDispatcher <https://docs.typo3.org/permalink/changelog:feature-88770>`_.

..  versionadded:: 10.0
    Starting with TYPO3 10.0 hooks and signals have been replaced by a PSR-14 based
    event dispatching system.
    See `Feature: #88770 - PSR-14 based EventDispatcher <https://docs.typo3.org/permalink/changelog:feature-88770>`_.

For emphasis, the directive can also be placed into one of the
:ref:`admonitions <rest-admonitions>`:


..  code-block:: rst

    ..  tip::
        ..  versionadded:: 10.0
            Starting with TYPO3 10.0 hooks and signals have been replaced by a PSR-14 based
            event dispatching system.
            See `Feature: #88770 - PSR-14 based EventDispatcher <https://docs.typo3.org/permalink/changelog:feature-88770>`_.

..  tip::
    ..  versionadded:: 10.0
        Starting with TYPO3 10.0 hooks and signals have been replaced by a PSR-14 based
        event dispatching system.
        See `Feature: #88770 - PSR-14 based EventDispatcher <https://docs.typo3.org/permalink/changelog:feature-88770>`_.

..  _rest-versions-deprecated:

Deprecated
==========

..  code-block:: rst

    ..  deprecated:: 9.5
        The hook :php:`$GLOBALS['TYPO3_CONF_VARS']['SC_OPTIONS']['tslib/class.tslib_fe.php']['tslib_fe-PostProc']`
        is deprecated - use a custom PSR-15 middleware instead.
        See `Deprecation: #86279 - Various Hooks and PSR-15 Middlewares <https://docs.typo3.org/permalink/changelog:deprecation-86279>`_.

..  deprecated:: 9.5
    The hook :php:`$GLOBALS['TYPO3_CONF_VARS']['SC_OPTIONS']['tslib/class.tslib_fe.php']['tslib_fe-PostProc']`
    is deprecated - use a custom PSR-15 middleware instead.
    See `Deprecation: #86279 - Various Hooks and PSR-15 Middlewares <https://docs.typo3.org/permalink/changelog:deprecation-86279>`_.

..  _rest-versions-versionchanged:

Versionchanged
==============

..  code-block:: rst

    ..  versionchanged:: 14.3
        See `Important: #110233 - Search query added to AfterPageTreeItemsPreparedEvent <https://docs.typo3.org/permalink/changelog:important-110233-1787820210>`_.

    The event also provides the current page tree search query via
    :php:`getSearchQuery()`.

..  versionchanged:: 14.3
    See `Important: #110233 - Search query added to AfterPageTreeItemsPreparedEvent <https://docs.typo3.org/permalink/changelog:important-110233-1787820210>`_.

The event also provides the current page tree search query via
:php:`getSearchQuery()`.

..  _rest-versions-what-belongs-in-directive:

What belongs in a version directive
===================================

The directive body can be removed after one or two versions. Avoid putting
information there that is meant to stay in the documentation permanently -
how something works, how to use it - that belongs in the regular text
around the directive instead.

It is fine to put information in the directive body that is itself tied to
the version transition and becomes obsolete once the directive is pruned:
a link to the corresponding Core changelog entry, a link to a migration
section, or a mention of what this replaces (for example, that an event
replaces a previous hook).

..  code-block:: rst

    ..  versionadded:: 12.3
        The event replaces the deprecated hook
        :php:`$GLOBALS['TYPO3_CONF_VARS']['SC_OPTIONS']['t3lib/class.t3lib_userauth.php']['logoff_pre_processing']`.
        See `Feature: #100307 - PSR-14 events for user login & logout <https://docs.typo3.org/permalink/changelog:feature-100307-1679924551>`_.

    The purpose of the PSR-14 event
    :php:`\TYPO3\CMS\Core\Authentication\Event\BeforeUserLogoutEvent` is to
    trigger any kind of action before a user will be logged out.

..  versionadded:: 12.3
    The event replaces the deprecated hook
    :php:`$GLOBALS['TYPO3_CONF_VARS']['SC_OPTIONS']['t3lib/class.t3lib_userauth.php']['logoff_pre_processing']`.
    See `Feature: #100307 - PSR-14 events for user login & logout <https://docs.typo3.org/permalink/changelog:feature-100307-1679924551>`_.

The purpose of the PSR-14 event
:php:`\TYPO3\CMS\Core\Authentication\Event\BeforeUserLogoutEvent` is to
trigger any kind of action before a user will be logged out.

Find a changelog entry's permalink from its own
`.. _<type>-<issue>-<timestamp>:` anchor, for example in the "Added files"
section of the corresponding `Changelog-To-Doc <https://github.com/TYPO3-Documentation/Changelog-To-Doc>`__
issue.
