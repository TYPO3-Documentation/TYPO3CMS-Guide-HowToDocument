.. include:: /Includes.rst.txt
.. highlight:: rst


.. _docs-official-how-you-can-help:
.. _how-to-contribute:


================
How You Can Help
================


Everyone can contribute to the TYPO3 documentation and contributions are
very much appreciated.


.. important::

   These are just examples to get you started. As a contributor, you are not
   restricted to this. If you can make useful improvements, do it!
   Some of the best contributions come from starting with something that bothers you
   the most.



Make Minor Changes
==================

If you see a typo, a broken link, something is outdated or you can make improvements in
any way, do not hesitate to click on "Edit on GitHub" and make
the change yourself. See :ref:`docs-contribute-github-method` for
a walkthrough.


.. _how-you-can-help-fix-issues:

Fix Issues
==========

See :ref:`links-github-issues`. As a new contributor, specifically look at issues
with the label :ref:`good first issue <github-good-first-issue>`.



.. _how-you-can-help-review-pr:

Review Pull Requests
====================

*--* **new**, *added August 10, 2019*

:ref:`Find an open pull request <github-pull-requests>` and review it.

Some pull requests make changes in documentation describing an aspect
of TYPO3 you may know well.
Help in this area is very much appreciated!


.. _how-you-can-help-write-new-content:

Write New Content
=================

*--* **new**, *added August 10, 2019*

*  :ref:`Write missing content <links-github-issues>`.



.. _how-you-can-help-add-diagrams:

Add Diagrams
============

*updated December 18, 2021*

Often things can be conveyed more easily if visual aids like diagrams
are used in conjunction with text.

You can create UML diagrams such as class diagrams, sequence diagrams and
cheat sheets.

Here are some examples:

*  :ref:`Check out sequence diagram on new page about request handling <t3coreapi:request-handling>`
*  :ref:`System Overview in "TYPO3 Explained" contains a diagram <overview>`


.. figure:: ../images/diagram.png
   :class: with-shadow
   :target: https://docs.typo3.org/m/typo3/reference-coreapi/main/en-us/ApiOverview/RequestHandling/Index.html#typo3-implementation

   Page in the documentation with a diagram

*  :ref:`Get started with PlantUML diagrams <PlantUML-diagrams>`


.. _how-you-can-help:

Create Cheat Sheets
===================

*--* **new**, *added August 11, 2019*

Look at the existing cheat sheets and check if they are up to date:

*  `List of cheat sheets <https://docs.typo3.org/Home/CheatSheets.html>`__

You can create further cheat sheets and add them to this list.



Replace Outdated Images
=======================

Replace outdated images, for example in the :doc:`t3tsconfig:Index`
reference.

Look at :ref:`how-to-document-images` for information about how to
embed images with reST.


Add YouTube Videos
==================

Add some new YouTube videos from the  `TYPO3 YouTube channel
<https://www.youtube.com/channel/UCwpl8LY9Tr3PB26Kk2FYW_w>`__.

See :ref:`youtube-videos` for information on how to do this.


.. _how-you-can-help-review-manuals:

Review Manuals
==============

*--* **new**, *added August 9, 2019*

Pick a manual and start reviewing it.
If you find something that needs fixing or something is missing, either fix it or write an
issue for it, if you cannot make the changes yourself.

.. tip::

   Usually, there is :ref:`one branch for each major TYPO3 version <t3home:usage-version-selector>`
   in a manual. Please focus your
   efforts mostly on the latest `main` branch, to get that up to date and ready!

You can for example start with:

*  :doc:`t3extbasebook:Index` : This currently needs some work in all branches. Check if the text
   is up to date and technically correct. Also, the text needs to be shortened in some parts and
   language improvements are necessary (grammar, style). For the `main` branch, you can
   `check off this review list <https://github.com/TYPO3-Documentation/TYPO3CMS-Book-ExtbaseFluid/issues/296>`__
   once you have started reviewing. This makes it easier for other reviewers to just skip the parts
   that are already ok.
*  :doc:`t3coreapi:Index`: The same applies as for :doc:`t3extbasebook:Index` except that
   "TYPO3 Explained" is generally in much better shape. Still, you can help by reviewing and
   `checking off this review list <https://github.com/TYPO3-Documentation/TYPO3CMS-Reference-CoreApi/issues/537>`__

.. tip::

   If you don't have write access to a GitHub repository (which is usually the case if you
   just started), you cannot check off the checkmarks in the review list. In that case, just leave a comment
   in the issue.

Once you start and are confident that you can make progress, you may want to talk about
your intentions in the #typo3-documentation Slack channel (as this is a bigger change).
You can also mention if you need help (because reviewing an entire manual can be quite
too much to do for one person).

You can check here to see the current review status of each manual:

*  :ref:`t3docteam:overview-of-manuals-review`



Teach
=========================

If you are already familiar with the workflow, you can help others
to get started. Whenever you are at a `TYPO3 event <https://typo3.org/community/events/>`__
(Sprint, Barcamp, etc.), on `StackOverflow <https://stackoverflow.com/questions/tagged/typo3>`__
or in a `Slack <https://my.typo3.org/index.php?id=35>`__ channel and someone finds
something missing or a problem in the documentation, help them make the
necessary changes themselves.

Motivate
===============

Thank others for their contributions (for example on Slack, Twitter or personally).


.. _contribute-what-social-media:

Spread the Word
===============

Tell others about things in the documentation, that are
`new <https://docs.typo3.org/News/Index.html>`__,
that you found interesting or that helped you in any way.

Remind people, that everyone can contribute!

*  `Tweet <https://twitter.com/>`__
   (hashtag: `#TYPO3 <https://twitter.com/search?q=%23TYPO3>`__).
   Additionally, you can use `#T3Docs <https://twitter.com/search?q=%23T3Docs>`__,
   `#T3Contribute <https://twitter.com/search?q=%23T3Contribute>`__,
   and `@T3DocTeam <https://twitter.com/T3docTeam>`__.

Review documentation
====================

Pick a manual and start reviewing it.

If you find something that needs fixing or something is missing, either fix it or write an
issue for it and add a warning.

More information: :ref:`guidelines-for-reviewing`

Blog About Your Contributions
=============================

Telling a real life story may help others to make the decision to
contribute. It's your story, so you decide what's in it, but here
are some ideas to get you started:

*  What gave you the motivation to contribute?
*  How did you benefit from contributing? For example, what did you learn?
*  What advice can you give others?

.. _how-you-can-help-new-content:

Make Suggestions for New Content
================================

Sometimes you can directly add content in a manual or create an issue for it.

But, what if you are not sure, where the new content should go or if it should
be created at all?

If this is the case, either:

*  Raise the question in the #typo3-documentation channel on Slack
*  Or, add a comment with your suggestion to this general issue:
   `What content is missing in the documentation? <https://github.com/TYPO3-Documentation/T3DocTeam/issues/85>`__


.. _how-you-can-help-changelog:

Add Information from the ChangeLog
==================================

.. important::

   This is already being taken care of by the TYPO3 Core Team. For each release,
   the Changelogs are checked and official documentation is updated. This mostly
   concerns TYPO3 Explained and the references.

Regardless of this, if you find something missing, you can add it yourself. Or
ask in Slack #typo3-documentation if you can help out.

.. _how-you-can-help-check-spelling:

Check Spelling
==============

Check spelling for consistency. For example, compare spelling of title
and headlines to `The TYPO3 Writing Style Guide
<https://typo3.org/community/teams/content/writing-style-guide/>`__ on typo3.org.

Is spelling of proper nouns correct?

See :ref:`content-styleguide` for more information, use the online tool
https://capitalizemytitle.com/ to check title spelling.


More Ideas?
===========

Do you have more ideas to add to this list? Either add them directly to this page using one of
:ref:`the two workflows <contribute>`
or `contact us
<https://typo3.org/community/teams/documentation/#c9886>`__ and make your suggestions.
