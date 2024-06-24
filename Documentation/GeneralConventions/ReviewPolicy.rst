..  include:: /Includes.rst.txt
..  index:: ! Review policy
..  _review-policy:

=============================================
Policy for making and reviewing contributions
=============================================

Contributing to the TYPO3 Documentation is much appreciated,
and should be a rewarding and positive experience both for
contributors and maintainers of the documentation.

With this document, we try to set up conventions and best practices.
We welcome constructive feedback to this living document with suggestions
to continuously improve our process.

..  _review-policy-contributors:

Policy for Contributors
=======================

As outlined in the chapter :ref:`docs-contribute`, contributors can
provide so called "Pull Requests" (PRs) to our manual repositories
on GitHub.

When a Pull Request is made, we kindly ask contributors to note
the following:

*   Please ensure that your Pull Request is **made against the appropriate
    version of the documentation**, usually against the `main` branch. If the
    changes you propose apply to specific versions of the documentation,
    you can add a line like `Releases: main, 12.4, 11.5` to note any
    Git branch that your change would apply to. If you are unsure,
    our maintainers will take care of it - this is just a step to make
    their work easier.
*   Please provide a **meaningful title** to your Pull Request.
*   Please provide a **short description** of what your Pull Request
    is about.
*   Please try to **focus your Pull Request on a single issue/topic**. At best,
    a pull request should only affect a single file or chapter, maybe even
    a section. Feel free to contribute multiple Pull Requests for multiple
    topics. This makes our review process quicker and easier.
*   **Be open to feedback** that our maintainers may have about the change,
    and sometimes there will be questions or other comments that will help
    to finalize your contribution.
*   Please **be patient for feedback** to your contribution. Our maintainers
    work on Pull Requests in their spare time.

If you are interested in the work of our maintainers, read on in the
next section.

..  _review-policy-maintainers:

Review policy for maintainers
-----------------------------

This section is intended for current maintainers, but please read on,
if you are interested in maybe becoming one in the future.

**Contributions are very valuable**: Anyone putting in the effort and time
to help us should **feel rewarded** by doing so. We try to adjust our review
policy to making this possible without sacrificing the **quality of our
documentation**.

The review process should have the **same standard** for anyone of the
maintainer team performing the review, and every member of the team
should feel good when **making decisions** on what and how to give feedback on.

Basic work on contributions
~~~~~~~~~~~~~~~~~~~~~~~~~~~

*   **Be kind and understanding**. Even when rejecting a contribution,
    there is a person behind a text, who meant well.
*   Try to **improve and explain changes** made to Pull Requests.
*   The automatic **Code-Checks** must be green (maintainers may need to
    execute them first for first-time contributors - before you do, ensure
    no malicious code is contained in `.github` action code changes or general
    code snippets)
*   Ensure **factual correctness** and **basic spell-checks** of a Pull Request.
*   A maintainer can and should always **directly edit/commit a Pull Request** to
    apply the following changes without the need to first ask for
    feedback of the contributor or other team members:

    *   **Apply spelling fixes**.
    *   **Fix syntax errors** made in code.
    *   **Fix mistakes in reST markup** (indentation, wrong directives, missing headers,
        wrong or missing linebreaks, wrong or bad links/references, ...) - see
        :ref:`format-rest-cgl`.

Workflow and follow-ups to contributions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following more specific checks to be fulfilled, before a Pull Request can be
merged:

*   Ensure the Pull Request is **made against the most recent applicable
    version**. The usual workflow will allow :ref:`backport-changes` from the
    latest to older versions. If this is not aligned, ask the contributor if
    a PR can be made against a different branch.
*   **Apply appropriate labels** to the Pull Request, for example `Backport 12.4`
    or `Needs language rework` or `Needs CodeSnippet` so that possible follow-up
    Pull Requests can be created.
*   A **single maintainer is sufficient to approve** a Pull Request, if all
    merging criteria has been met. No "grace period" must be met before a
    contribution can be merged.
*   **Read all comments by co-maintainers**, before you merge, and ensure no
    concerns are raised.
*   If you feel the Pull Request contains **debatable or problematic parts**,
    please **discuss this //internally//** in the documentation team (Slack channel
    `#documentation-team`). **Negative public feedback can be off-putting** and must only
    be raised after internal discussion, because this can reflect back to
    the TYPO3 project as a whole. Be encouraging in your feedback to give
    the contributor a chance to improve or agree to errors or wrong
    direction.
*   A **single maintainer can also decide to close/dismiss** a pull request.
    There should be a positively worded feedback to the contributor, stating
    factual reasons why a contribution can not be merged at this point.
*   Only apply the "Request Changes" ("-1") action if you feel the Pull Request
    must not be merged by any other maintainer. Ideally, always just comment
    nicely and give feedback on problematic areas of a Pull Request and ask
    the contributor to rephrase or fix errors. Other maintainers will read
    your comment. Discuss problems internally, if they cannot be addressed
    in an encouraging way towards the contributor.
*   If a maintainer sees **additional issues** while reviewing a contribution,
    these should be addressed in a separate Pull Request, as this is **beyond
    scope**.
*   In some areas, **maintainers can be "opinionated"** and may not agree, because
    there is no objective criteria to discuss. Such a discrepancy should be
    discussed internally. We are working on a catalogue of "debatable" topics,
    like for example when to make PHP code "final" or what to make "private/protected".
    All of our manuals should ideally follow the same lead. Whenever we hit
    a debatable topic, we should try to find a common ground and document how we
    decided to deal with this. These decisions are found in :ref:`review-policy-opinionated`.

After a Pull Request has been merged:

*   Check if there were any **labels that require follow-up changes** to the
    Pull Request (like rework of wording, changing code snippets, adding
    screenshots). If applicable, a maintainer can either create the Pull
    Request themself, or maybe ask contributors, if they want to create a follow-up.
*   If a **backport** is needed, see :ref:`backport-changes` on how to perform this.
*   The maintainer who merges a Pull Request can make a decision on the scope
    of the backport. If a backport is too hard or time-consuming to execute,
    a maintainer may decide to not perform it. Any maintainer who feels otherwise
    is free to perform the backport on their own.
*   If a maintainer finds **issues or disagrees with a performed merge** after the fact,
    this must be discussed internally. A revert is always possible, as is a follow-up
    PR addressing mistakes. We are humans, and do make those from time to time.

..  _review-policy-opinionated:

"Opinionated" decisions
=======================

Some decisions can not be made objectively, there may be reasons against and for it.
Like picking "spaces or tabs" for intendation, or how to apply Uppercase Wording.

Here is a list of currently agreed stances:

*   We use "Sentence case" for all headlines, so only uppercase words at the
    beginning of a sentence, and following english language uppercasing rules,
    plus uppercase all special words found in our :ref:`Glossary <spelling-ref>`.
*   Headline levels are used semantically/structurally, not visually. Their levels
    must follow logical rules and leave no levels out (for example, no headline of
    level 4 after a level 1 headline).
*   In PHP code examples, prefer Dependency Injection over `makeInstance` calls,
    whenever possible.
*   PHP Coding Guidelines adhere to the PSR-2 standard, as described in the
    :ref:`TYPO3 Coding Guidelines for PHP files <t3coreapi:cgl-general-requirements-for-php-files>`
*   When acronyms are used, the first usage of that in a chapter must always spell it out.
*   Cross-link to other chapters when named specifically.
*   Always write "for example" instead of "e.g." or "i.e.", generally avoid abbreviations.
*   When referencing PHP class names / object types, spell out their "Fully Qualified Class Name" (FQCN) on first use.
*   See :ref:`format-rest-cgl` for coding guidelines of reST formatting.
*   See :ref:`content-styleguide` for more spelling / writing rules.

..  _review-policy-todo:

TODO
====

A few things still need to be addressed:

*   Unify the GitHub labels for all TYPO3-Documentation projects to have:

    *   Backport 12.4/11.5
    *   Needs language rework
    *   Needs CodeSnippet
    *   Needs more Examples
    *   ...?

*   Create a list of "opinionated" and problematic decisions, aligned with
    the best practices of the TYPO3 Core Team. For example:

    *   What to make "final" in PHP variables/methods/classes
    *   What to make "private" instead of "protected" (and vice versa) variables/methods/classes
    *   Directory names for code examples (for example "Classes/Service/" or "Classes/Services"?)
    *   File names for code examples ("EntryService.php" or "EntriesService.php" or "EntryServices.php")
    *   Exact prefixes for "Vendor" ("MyVendor"?) and Extensions ("MyExtension" or "MySitepackage"?)
    *   Remove redundancy between :ref:`review-policy-opinionated` and :ref:`content-styleguide` (split it up into "technical" and "grammar"?)

