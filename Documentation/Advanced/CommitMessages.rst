..  include:: /Includes.rst.txt
..  index:: ! Commit messages
..  _commit-messages:

================
Commit messages
================

These conventions apply to every contribution, no matter whether you make
your change :ref:`directly on GitHub <docs-contribute-github-method>` or
:ref:`locally with Docker <docs-contribute-git-docker>`.

..  literalinclude:: /_CodeSnippets/_CommitMessageExample.txt
    :caption: Example commit message
    :language: text

If the change is related to a changelog entry, a Gerrit change, or an
issue, mention it too:

..  literalinclude:: /_CodeSnippets/_ChangelogCommitMessageExample.txt
    :caption: Example commit message referencing a changelog issue
    :language: text

..  _commit-messages-format:

Format
======

*   Prefix the summary line with the type of change -- `[TASK]`,
    `[BUGFIX]` or `[FEATURE]` -- followed by a short, imperative summary.

*   Explain *why* the change is needed in the body. The diff already shows
    what changed; the body should cover what the diff cannot.

*   End with a `Signed-off-by: Your Name` trailer. Add an
    `Assisted-by: <tool/model name> <contact>` trailer too, if you used AI
    assistance for more than a basic spelling or grammar check.

*   If the change is related to a changelog entry, mention that changelog
    entry. If it is related to a Gerrit change that had no changelog
    entry, mention that Gerrit change instead. If it is related to an
    issue, mention the issue number.

*   If the manual has branches per version, add a line like
    `Releases: main, 14.3` to note which versions your change applies to
    (see :ref:`review policy <review-policy>`). Backporting to those
    branches then happens automatically (see :ref:`backport changes
    <backport-changes>`) -- manual backporting is only needed if the
    automatic backport hits a conflict or the content needs to be
    adjusted per version.
