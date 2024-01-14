.. include:: /Includes.rst.txt
.. highlight:: rst
.. index::
   Documentation; Update
   Documentation; New releases
.. _howto-update-docs:
.. _update-docs:

===================================
Apply changelog entries to the docs
===================================

Whenever a change to the TYPO3 Core potentially affects the users a changelog
entry is created or edited, for example:

..  deprecated:: 12.3
    The hook shown here is deprecated since TYPO3 12.3, use the event XYZ
    instead.

Each Core change affecting the changelog automatically creates an
`Issue in the repository Changelog-To-Doc <https://github.com/TYPO3-Documentation/Changelog-To-Doc/issues>`.
New issues here should be treated with priority.

.. index:: pair: Updates; Commit messages

Commit messages
===============

All changes that are related to such an issue should contain a reference in
their commit message to the issue, for example

..  code-block:: text
    :caption: Example commit message

    [FEATURE] Add ApplicationContext to TypoScript data

    resolves: https://github.com/TYPO3-Documentation/Changelog-To-Doc/issues/790
    Releases: main

See also: :ref:`general-conventions-commit-messages`.

..  index::
    Documentation; Deprecations
    reST directives; deprecated
..  _changelog-deprecations:

Deprecations in the changelog
=============================

All information about deprecations should be marked with the :rst:`..  deprecated::`
directive and the version of deprecation.

..  deprecated:: 12.3
    The hook shown here is deprecated since TYPO3 12.3, use the event XYZ
    instead.

..  code-block:: rst

    ..  deprecated:: 12.3
        The hook shown here is deprecated since TYPO3 12.3, use the event XYZ
        instead.

In the ideal workflow a deprecation option will be removed with a breaking
change in the next major version. We can then just remove the deprecated section.

Using the correct directive will help the documentation team to find and remove
deprecation hints in later versions.

.. index::
    Documentation; Breaking changes
    reST directives; versionchanged
..  _changelog-breaking-changes:

Breaking changes in the changelog
=================================

Ideally a breaking change was prepared by a :ref:`deprecation <changelog-deprecations>`
in the previous version. In this case we can just remove the deprecated section.

When important concepts changed that might confuse the users we sometimes leave
a :rst:`.. versionchanged::` directive to inform users where to head now.

..  versionchanged:: 11.5
    The widely used :php:`->execute()` method has been split into:
    php:`->executeQuery()`  and :php:`->executeStatement()`. Read more.

..  code-block:: rst

    ..  versionchanged:: 11.5
        The widely used :php:`->execute()` method has been split into:
        php:`->executeQuery()`  and :php:`->executeStatement()`. Read more.

For emphasis you can also put the version changed directive into a warning or
info box:

..  warning::
    ..  versionchanged:: 11.5
        The widely used :php:`->execute()` method has been split into:
        php:`->executeQuery()`  and :php:`->executeStatement()`. Read more.

..  code-block:: rst

    ..  warning::
        ..  versionchanged:: 11.5
            The widely used :php:`->execute()` method has been split into:
            php:`->executeQuery()`  and :php:`->executeStatement()`. Read more.

Using the correct directive will help us to track down and remove these hints
in later versions.

.. index::
   reST directives; versionadded
..  _changelog-feature:

New features in the changelog
=============================

When adding a new feature to the docs that is not yet availible in all supported
TYPO3 versions, it can be helpfull to mark it with the :rst:`..  versionadded::`
directive:

..  versionadded:: 13.0
    A PHP attribute :php:`\TYPO3\CMS\Core\Attribute\AsEventListener` is
    available to autoconfigure a class as an event listener...

This directive not only highlights new features but also assists users who
are reading the manual in a version that does not align with their installation,
ensuring clarity in cases where feature compatibility may differ.

The documentation team removes these directives when the feature is present in
all supported TYPO3 versions.
