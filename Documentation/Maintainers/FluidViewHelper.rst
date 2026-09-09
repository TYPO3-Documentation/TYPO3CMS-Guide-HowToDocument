..  include:: /Includes.rst.txt
..  _fluid-viewhelper-reference-generation:

=====================================
Fluid ViewHelper reference generation
=====================================

The :ref:`Fluid ViewHelper Reference <t3viewhelper:start>` is assembled from
two sources: the PHP classes of the ViewHelpers themselves, and hand-written
reStructuredText in the repository `TYPO3CMS-Reference-ViewHelper
<https://github.com/TYPO3-Documentation/TYPO3CMS-Reference-ViewHelper>`_.
This page describes how that pipeline fits together, for the maintainers who
keep it running.

..  seealso::
    Contributors who want to improve a single ViewHelper page do not need any
    of this. See :ref:`t3viewhelper:contribution` instead.

..  contents::

..  _fluid-viewhelper-reference-generation-sources:

What is taken from the PHP sources
==================================

The generator reads the ViewHelper classes of the
`TYPO3 Core <https://github.com/TYPO3/typo3>`__ and of the package
`Fluid Rendering Engine <https://github.com/TYPO3/Fluid>`__. From each class it
takes the phpDoc-style comment above the class and the arguments registered in
its :php:`initializeArguments()` method.

Only that short description and the argument list come from PHP. Everything
else on a ViewHelper page — the explanations, the examples and the page
structure — is written by hand in the reference repository, and that is where
it should stay. See :ref:`Hand-written documentation is preferred
<t3viewhelper:contribution-hand-written>`.

Fixing a wrong or missing short description is therefore a change to the PHP
doc-comment, and follows the :ref:`TYPO3 Contribution Guide - Core Development
<t3contribute:recommended-reading>`.
Adding an example is a change to the manual, through a pull request against the
reference repository.

..  _fluid-viewhelper-reference-generation-rst:

Generation of the reStructuredText files and JSON files
=======================================================

The `Fluid ViewHelper Documentation Generator
<https://github.com/TYPO3-Documentation/fluid-documentation-generator>`__
produces, for each documented Fluid namespace, a directory of
:abbr:`rST (reStructuredText)` files and one JSON file.

The namespaces are configured in JSON files in the generator repository, below
:file:`config/`. A configuration may combine several namespaces into one —
this is how `f:*` in TYPO3 ends up covering both the ViewHelpers of
`EXT:fluid` and those of Fluid Standalone.

..  _fluid-viewhelper-reference-generation-html:

Rendering the ViewHelper reference to HTML
==========================================

The generated files are copied into `TYPO3CMS-Reference-ViewHelper`_ by the
:ref:`GitHub action <fluid-viewhelper-reference-generation-github-action>`,
under two different rules:

reStructuredText files
    Copied only if no file of that name exists yet. An existing page is never
    overwritten, so hand-written content is safe. A ViewHelper that is removed
    from the Core keeps its page until somebody deletes it by hand.

JSON files
    Always overwritten. This is what keeps descriptions and argument tables
    current: the :rst:`typo3:viewhelper` directive on a page reads the JSON at
    render time, so a changed doc-comment reaches the published page without
    the page itself being touched.

:file:`Documentation/Index.rst` is explicitly restored after the copy and is
maintained by hand, as are the :ref:`guides.xml <settings-guides-xml>` and
everything else outside the generated namespace directories.
`TYPO3CMS-Reference-ViewHelper`_ is then rendered by the standard rendering
process.

..  _fluid-viewhelper-reference-generation-github-action:

GitHub action "Fluid ViewHelper documentation"
==============================================

All of the above is combined into the workflow
:file:`.github/workflows/fluid-viewhelper.yml` in the repository
`t3docs-ci-deploy <https://github.com/TYPO3-Documentation/t3docs-ci-deploy>`__.
It runs once a day and can also be started manually through the GitHub UI by
the TYPO3 Documentation team.

The workflow runs once per documented TYPO3 version. Each run installs a slim
TYPO3 setup for that version, defined in
:file:`Build/fluid-viewhelpers/<version>/composer.json`, and pushes its result
to the branch of the same name in the reference repository. Adding a version
therefore means adding both the directory and an entry in the workflow's
matrix, which also pins the PHP version that version of TYPO3 needs.

The resulting commits are titled
`[BOT][TASK] Only add new ViewHelper documentation files`. There are none on
days when no ViewHelper was added and no description changed.

Maintainers need to occasionally watch for failed or stuck `workflow runs
<https://github.com/TYPO3-Documentation/t3docs-ci-deploy/actions>`__, because
the pipeline can stop without anything looking wrong:

*   GitHub disables a scheduled workflow after 60 days without a commit to
    its repository. The daily runs then simply stop, and there is no failed
    run to notice. Re-enable the workflow on the :guilabel:`Actions` tab, or
    start it once manually, and the schedule resumes.
*   The step that writes to the reference repository is marked
    `continue-on-error`, so a failure there does not turn the run red.

In both cases the symptom is the same: the reference stops receiving commits
while every run still looks fine.
