..  include:: /Includes.rst.txt
..  highlight:: rst

..  _docs-official-how-you-can-help:
..  _how-to-contribute:
..  _how-you-can-help:

================
How you can help
================

Everyone can contribute to the TYPO3 documentation and contributions are
very much appreciated.

..  note::
    These are just examples to get you started. As a contributor, you are not
    restricted to this. If you can make useful improvements, do it!
    Some of the best contributions come from starting with something that
    bothers you the most.


Make minor changes
==================

If you see a typo, a broken link, something is outdated or you can make
improvements in any way, do not hesitate to click on :guilabel:`Edit on GitHub`
button and make the change yourself. See :ref:`docs-contribute-github-method`
for a walkthrough.


.. _how-you-can-help-fix-issues:
.. _links-github-issues:

Fix issues
==========

Pick an issue for a topic you are familiar with and try to fix it. Some of the
issues address a problem, some are enhancements where new text needs to be
written.

You can look at the open issues of a manual you are familiar with, pick one
and fix the problem.

For example:

*  `Issues for "TYPO3 Explained"
   <https://github.com/TYPO3-Documentation/TYPO3CMS-Reference-CoreApi/issues>`__
*  `Issues for "Getting Started Tutorial"
   <https://github.com/TYPO3-Documentation/TYPO3CMS-Tutorial-GettingStarted/issues>`__


.. _github-good-first-issue:
.. _useful-links-for-contributors:

Links to GitHub issues
----------------------

Here are some links to GitHub issues in `TYPO3-Documentation <https://github.com/TYPO3-Documentation>`__.

.. important::

   GitHub will show a 404 page if you are not logged in following these links!
   So, remember to log in first!

For new contributors:

*  `Good first issues <https://github.com/issues?q=is%3Aopen%20is%3Aissue%20label%3A%22good%20first%20issue%22%20archived%3Afalse%20user%3ATYPO3-Documentation>`__ (Link to GitHub)

For contributors:

*  `All open, unassigned issues (without team, theme etc.) <https://github.com/issues?utf8=%E2%9C%93&q=is%3Aopen+is%3Aissue+archived%3Afalse+org%3ATYPO3-Documentation+-repo%3ATYPO3-Documentation%2FT3DocTeam+-repo%3ATYPO3-Documentation%2Ft3SphinxThemeRtd+-repo%3ATYPO3-Documentation%2FTYPO3CMS-Guide-HowToDocument+no%3Aassignee>`__ (Link to GitHub)

For team members and advanced contributors:

*  `All open issues
   <https://github.com/issues?q=is%3Aopen+is%3Aissue+archived%3Afalse+org%3ATYPO3-Documentation>`__ (Link to GitHub)
*  `All open, unassigned issues
   <https://github.com/issues?q=is%3Aopen+is%3Aissue+archived%3Afalse+org%3ATYPO3-Documentation+no%3Aassignee>`__ (Link to GitHub)

The Docker image for rendering is in the organization **t3docs** (instead of TYPO3-Documentation):

*  `All open issues in t3docs <https://github.com/issues?utf8=%E2%9C%93&q=is%3Aopen+is%3Aissue+archived%3Afalse+org%3At3docs>`__ (Link to GitHub)


.. _how-you-can-help-review-pr:

Review pull requests
====================

Some pull requests make changes in documentation describing an aspect
of TYPO3 you may know well.
Help in this area is very much appreciated!

.. important::

   GitHub will show a 404 page if you are not logged in following these links!
   So, remember to log in first!


Anyone is welcome to review open pull requests!

In **TYPO3-Documentation**:

*  `Open pull requests <https://github.com/pulls?q=is%3Aopen+is%3Apr+archived%3Afalse+org%3ATYPO3-Documentation+sort%3Acreated-desc>`__ (Link to GitHub)

In **t3docs** (Docker image):

*  `Open pull requests <https://github.com/pulls?q=is%3Aopen+is%3Apr+archived%3Afalse+org%3At3docs+sort%3Acreated-asc>`__ (Link to GitHub)


.. _how-you-can-help-write-new-content:

Write new content
=================

*  :ref:`Write missing content <links-github-issues>`.


.. _how-you-can-help-add-diagrams:

Add diagrams
============

Often things can be conveyed more easily if visual aids like diagrams
are used in conjunction with text.

You can create UML diagrams such as class diagrams, sequence diagrams and
cheat sheets.

Here are some examples:

*   :ref:`Check out sequence diagram on new page about request handling <t3coreapi:request-handling>`

    ..  figure:: /Images/diagram.png
        :alt: Example of a sequence diagram about request handling
        :class: with-shadow

        Example of a sequence diagram about request handling

*  :ref:`System overview in "TYPO3 Explained" contains a diagram <t3coreapi:overview>`

*  :ref:`Get started with PlantUML diagrams <PlantUML-diagrams>`


Replace outdated images and screenshots
=======================================

Replace outdated images, for example, in the :ref:`t3tsconfig:start`
reference.

Look at :ref:`how-to-document-images` for information about how to
embed images with reST.


Add YouTube videos
==================

Add some new YouTube videos from the `TYPO3 YouTube channel`_.

See :ref:`youtube-videos` for information on how to do this.


.. _how-you-can-help-review-manuals:

Review manuals
==============

Pick a manual and start reviewing it. If you find something that needs fixing or
something is missing, either fix it or write an issue for it, if you cannot make
the changes yourself.

More information: :ref:`guidelines-for-reviewing`

..  tip::
    Usually, there is
    :ref:`one branch for each major TYPO3 version <t3home:usage-version-selector>`
    in a manual. Please focus your efforts mostly on the "main" branch, to get
    that up to date and ready! The Documentation Team will then check, if a
    backport to older versions makes sense.

..  tip::
    If you do not have write access to a GitHub repository (which is usually the
    case if you just started), you cannot check off the checkmarks in the review
    list. In that case, just leave a comment in the issue.

Once you start and are confident that you can make progress, you may want to
talk about your intentions in the `#typo3-documentation`_ Slack channel (as this
is a bigger change). You can also mention, if you need help (because reviewing
an entire manual can be quite too much to do for one person).

..  note::
    Instead of reviewing and changing all pages of a chapter in one pull request,
    consider to split them into multiple pull request, for example, one per
    page. This makes the reviewing for the Documentation Team easier
    and you get feedback more quickly.


Teach
=====

If you are already familiar with the workflow, you can help others to get
started. Whenever you are at a `TYPO3 event`_ (sprint, barcamp, etc.), on
`StackOverflow`_ or in a `Slack`_ channel and someone finds something missing or
a problem in the documentation, help them make the necessary changes themselves.

Motivate
========

Thank others for their contributions (for example on `Slack`_, `Mastodon`_ or
personally).


.. _contribute-what-social-media:

Spread the word
===============

Tell others about things in the documentation, that are `new`_,
that you found interesting or that helped you in any way.

Remind people, that everyone can contribute!

Write on `Mastodon`_ (hashtag: `#TYPO3`). Additionally, you can use `#T3Docs`,
`#T3Contribute`, and mention `@documentation@typo3.social`_.


Blog about your contributions
=============================

Telling a real life story may help others to make the decision to
contribute. It's your story, so you decide what is in it, but here
are some ideas to get you started:

*   What gave you the motivation to contribute?
*   How did you benefit from contributing? For example, what did you learn?
*   What advice can you give others?


.. _how-you-can-help-new-content:

Make suggestions for new content
================================

Sometimes you can directly add content in a manual or create an issue for it.

But, what if you are not sure, where the new content should go or if it should
be created at all?

If this is the case, raise the question in the `#typo3-documentation`_ channel
on `Slack`_.


.. _how-you-can-help-changelog:

Add information from the changelog
==================================

Each new or changed changelog from the TYPO3 Core creates an issue in the
`Changelog-to-doc repository`_. The issues are mostly already tagged with the
according manual which has to be changed. If you want to pick up an issue,
check if there is already a person assigned. If not leave a comment in the issue
that you are working on it. This prevents two people working on the same issue.

Regardless of this, if you find something missing, you can add it yourself. Or
ask in the `#typo3-documentation`_ Slack channel, if you can help out.


.. _how-you-can-help-check-spelling:

Check spelling
==============

Check spelling for consistency. For example, compare spelling of title
and headlines to the rules outlined in the :ref:`spelling` chapter.


More ideas?
===========

Do you have more ideas to add to this list? Either add them directly to this
page using one of :ref:`the two workflows <contribute>` or contact us in the
`#typo3-documentation`_ channel on `Slack`_.


..  _@documentation@typo3.social: https://typo3.social/@documentation
..  _#typo3-documentation: https://typo3.slack.com/app_redirect?channel=C028JEPJL
..  _Changelog-to-doc repository: https://github.com/TYPO3-Documentation/Changelog-To-Doc/issues
..  _Mastodon: https://joinmastodon.org/
..  _new: https://docs.typo3.org/News/Index.html
..  _Slack: https://typo3.org/community/meet/chat-slack
..  _StackOverflow: https://stackoverflow.com/questions/tagged/typo3
..  _TYPO3 event: https://typo3.org/community/events/
..  _TYPO3 YouTube channel: https://www.youtube.com/channel/UCwpl8LY9Tr3PB26Kk2FYW_w
