..  include:: /Includes.rst.txt
..  index::
    Documentation; Update
    Documentation; New releases
..  _howto-update-docs:
..  _update-docs:

===================================
Apply Changelog entries to the docs
===================================

Whenever a change to the TYPO3 Core potentially affects the users a changelog
entry is created or edited, for example:

..  deprecated:: 12.3
    The hook :php:`$GLOBALS['TYPO3_CONF_VARS']['SC_OPTIONS']['t3lib/class.t3lib_userauth.php']['logoff_pre_processing']`
    is deprecated since TYPO3 12.3, use the event
    :php-short:`\TYPO3\CMS\Core\Authentication\Event\BeforeUserLogoutEvent` instead.
    See `Deprecation: #100307 - Various hooks related to authentication users <https://docs.typo3.org/permalink/changelog:deprecation-100307-1679924603>`_.

..  seealso::
    See :ref:`What belongs in a version directive <rest-versions-what-belongs-in-directive>`
    for what belongs in the directive body versus the regular text around it.

Each Core change affecting the changelog automatically creates an
`Issue in the repository Changelog-To-Doc <https://github.com/TYPO3-Documentation/Changelog-To-Doc/issues>`_.
New issues here should be treated with priority.

..  index:: pair: Updates; Commit messages

..  _howto-update-docs-commit-messages:

Commit messages
===============

All changes that are related to such an issue should contain a reference in
their commit message to the issue (see :ref:`commit message conventions
<commit-messages>` for the full picture), for example:

..  literalinclude:: /_CodeSnippets/_ChangelogCommitMessageExample.txt
    :caption: Example commit message
    :language: text

..  index::
    Documentation; Deprecations
    reST directives; deprecated
..  _changelog-deprecations:

Deprecations in the Changelog
=============================

All information about deprecations should be marked with the :rst:`..  deprecated::`
directive and the version of deprecation.

..  deprecated:: 12.3
    The hook :php:`$GLOBALS['TYPO3_CONF_VARS']['SC_OPTIONS']['t3lib/class.t3lib_userauth.php']['logoff_pre_processing']`
    is deprecated since TYPO3 12.3, use the event
    :php-short:`\TYPO3\CMS\Core\Authentication\Event\BeforeUserLogoutEvent` instead.
    See `Deprecation: #100307 - Various hooks related to authentication users <https://docs.typo3.org/permalink/changelog:deprecation-100307-1679924603>`_.

..  code-block:: rst

    ..  deprecated:: 12.3
        The hook :php:`$GLOBALS['TYPO3_CONF_VARS']['SC_OPTIONS']['t3lib/class.t3lib_userauth.php']['logoff_pre_processing']`
        is deprecated since TYPO3 12.3, use the event
        :php-short:`\TYPO3\CMS\Core\Authentication\Event\BeforeUserLogoutEvent` instead.
        See `Deprecation: #100307 - Various hooks related to authentication users <https://docs.typo3.org/permalink/changelog:deprecation-100307-1679924603>`_.

In the ideal workflow a deprecation option will be removed with a breaking
change in the next major version. We can then just remove the deprecated section.

Using the correct directive will help the documentation team to find and remove
deprecation hints in later versions.

..  index::
    Documentation; Breaking changes
    reST directives; versionchanged
..  _changelog-breaking-changes:

Breaking changes in the Changelog
=================================

Ideally a breaking change was prepared by a :ref:`deprecation <changelog-deprecations>`
in the previous version. In this case we can just remove the deprecated section.

When important concepts changed that might confuse the users we sometimes leave
a :rst:`.. versionchanged::` directive to inform users where to head now.

..  versionchanged:: 12.0
    The widely used :php:`->execute()` method has been split into
    :php:`->executeQuery()` and :php:`->executeStatement()`.
    See `Deprecation: #96972 - Deprecate QueryBuilder::execute() <https://docs.typo3.org/permalink/changelog:deprecation-96972>`_.

..  code-block:: rst

    ..  versionchanged:: 12.0
        The widely used :php:`->execute()` method has been split into
        :php:`->executeQuery()` and :php:`->executeStatement()`.
        See `Deprecation: #96972 - Deprecate QueryBuilder::execute() <https://docs.typo3.org/permalink/changelog:deprecation-96972>`_.

For emphasis you can also put the version changed directive into a warning or
info box:

..  warning::
    ..  versionchanged:: 12.0
        The widely used :php:`->execute()` method has been split into
        :php:`->executeQuery()` and :php:`->executeStatement()`.
        See `Deprecation: #96972 - Deprecate QueryBuilder::execute() <https://docs.typo3.org/permalink/changelog:deprecation-96972>`_.

..  code-block:: rst

    ..  warning::
        ..  versionchanged:: 12.0
            The widely used :php:`->execute()` method has been split into
            :php:`->executeQuery()` and :php:`->executeStatement()`.
            See `Deprecation: #96972 - Deprecate QueryBuilder::execute() <https://docs.typo3.org/permalink/changelog:deprecation-96972>`_.

Using the correct directive will help us to track down and remove these hints
in later versions.

..  index::
    reST directives; versionadded
..  _changelog-feature:

New features in the Changelog
=============================

When adding a new feature to the docs that is not yet available in all supported
TYPO3 versions, it can be helpful to mark it with the :rst:`..  versionadded::`
directive:

..  versionadded:: 13.0
    A PHP attribute :php:`\TYPO3\CMS\Core\Attribute\AsEventListener` is
    available to autoconfigure a class as an event listener.
    See `Feature: #101544 - Introduce PHP attribute to autoconfigure event listeners <https://docs.typo3.org/permalink/changelog:feature-101544-1691063522>`_.

This directive not only highlights new features but also assists users who
are reading the manual in a version that does not align with their installation,
ensuring clarity in cases where feature compatibility may differ.

The documentation team removes these directives when the feature is present in
all supported TYPO3 versions.
