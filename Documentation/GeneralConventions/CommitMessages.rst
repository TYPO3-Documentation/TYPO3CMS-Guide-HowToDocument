.. include:: ../Includes.txt
.. highlight:: rst

.. _general-conventions-commit-messages:

===============
Commit Messages
===============

The Documentation Team currently does not have strict "rules" for commit messages. These
are recommendations.
  
Commit Message Recommendations
==============================

* Write commit messages that are **clear**, **concise** and **meaningful**
* Use imperative form: "Fix typo" (instead of "Fixed typo"). This is
  seen from the person, that is going to apply your patch: What will the patch do?
  Fix typo!
* As in the TYPO3 core commit message rules, keep lines below 52 characters
  if possible, but below 80 in any case.
* A commit message for the docs should consists of a subject line. More lines
  are optional.
* If an issue exists, link to it.


Examples
========

Example commit message with issue
---------------------------------

.. code-block:: none

   Add chapter for commit message rules

   Resolves: #4
   
This consists of the following parts:

.. code-block:: none

   <subject>

   Resolves: #<issue number>
   
The issue number is optional. Github will automatically create a link to
the issue.


If you are editing online with GitHub, this may look like this:

.. image:: ../images/commit-msg.png
   :class: with-shadow



Using "Resolves", will automatically close the issue. You can use "Related" instead of
"Resolves" if you do not want this.

You can refer to more than one issue.


Using TYPO3 Core Commit Message Rules
=====================================

If you wish, you can use the prefixes [BUGFIX],[FEATURE],[TASK] etc. as is customary in core development
(see :ref:`t3contribute:commitmessage`).
However, this is not mandatory. If possible, use the conventions, that are being used in
the manual in which you are working, e.g. `TYPO3 Explained commits <https://github.com/TYPO3-Documentation/TYPO3CMS-Reference-CoreApi/commits/latest>`__
typically use these conventions.

Additional Information
======================

* `How to write a git commit message <https://chris.beams.io/posts/git-commit/>`__
* :ref:`t3contribute:commitmessage` in TYPO3 Contribution Guide - Core Development


