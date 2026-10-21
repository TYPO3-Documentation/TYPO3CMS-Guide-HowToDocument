:navigation-title: Writing with AI

..  include:: /Includes.rst.txt
..  index:: AI assistance; Writing documentation
..  _ai-assistance:

======================================
Write documentation with AI assistance
======================================

You can use an AI assistant to write or change TYPO3 documentation, for
example a coding agent in your editor or terminal. The same rules apply as
for every other contribution. This page shows how to give the assistant
these rules, and how to check its work.

..  contents::
    :local:

..  _ai-assistance-responsibility:

You are responsible for the result
==================================

The assistant writes a draft. You submit the change, so check it as if you
had written it yourself:

*   Read every line of the diff before you commit it.
*   Verify every technical fact against the source code: class names,
    method signatures, option names, defaults, and the version that added
    or removed something. An assistant often writes a fact from memory, and
    that memory can be out of date.
*   Check the facts against the TYPO3 version of the branch that you write
    on. On the `main` branch of a manual, this is the `main` branch of the
    TYPO3 Core, the version in development.
*   Make sure that no anchor was deleted. See
    `Keeping anchors working <https://docs.typo3.org/permalink/h2document:anchor-persistence>`_.

..  _ai-assistance-commit-message:

The commit message in official documentation
============================================

A change to the official TYPO3 documentation follows the
`rules for commit messages <https://docs.typo3.org/permalink/h2document:commit-messages-format>`_,
also when an assistant wrote it. One of these rules is about AI
assistance:

*   End with a `Signed-off-by: Your Name` trailer. Add an
    `Assisted-by: <tool/model name> <contact>` trailer too, if you used AI
    assistance for more than a basic spelling or grammar check.

The `Signed-off-by` trailer names you, the contributor. The `Assisted-by`
trailer names the tool or the model:

..  literalinclude:: /_CodeSnippets/_CommitMessageExample.txt
    :caption: Example commit message
    :language: text

The :file:`AGENTS.md` of a repository can add trailers of its own, such as
`Releases:` in a manual with a branch per TYPO3 version.

..  _ai-assistance-agents-md:

Instructions in the repository
==============================

Most official TYPO3 manuals have a file :file:`AGENTS.md` at the root of
their repository. Most coding agents read this file by themselves when they
start to work in the repository. It names the structure of the repository,
the commands to render and test it, its branches, and its commit trailers.
For the writing rules, it links to this guide and does not copy them.

Some repositories also have a file :file:`CLAUDE.md`. It only points to
:file:`AGENTS.md`, because Claude Code looks for this file name.

You can add an :file:`AGENTS.md` to the repository of your extension in the
same way. See
`Instructions for AI assistants <https://docs.typo3.org/permalink/h2document:write-doc-extensions-agents-md>`_
for an example.

..  _ai-assistance-skills:

Skills for TYPO3 documentation
==============================

This guide provides the following skills in the folder
`skills/ <https://github.com/TYPO3-Documentation/TYPO3CMS-Guide-HowToDocument/tree/main/skills>`_
of its repository:

`typo3-docs-writing`
    Makes the assistant read the rules of this guide for the content that it
    is about to write. The skill names the page and the anchor for each kind
    of content. After writing, the assistant checks the result with
    :bash:`make test-docs` and reads the rendered pages.

`typo3-docs-style-check`
    Checks changed files against the rules of this guide and reports each
    violation with the rule and a fix. It does not change the files.

`typo3-docs-screenshot-review`
    Compares changed screenshots with their previous version and shows the
    old image, the new one, and the changed pixels on a page. You decide
    which images go into the commit, so images that differ only by chance
    do not make the repository bigger.

`typo3-docs-changelog-triage`
    Goes through new issues of the
    `Changelog-To-Doc <https://github.com/TYPO3-Documentation/Changelog-To-Doc/issues>`__
    repository. For each Core change, it reads the diff, searches the
    manuals, and drafts the labels and a comment that names the pages to
    change. You approve each issue before anything is posted.

The skills do not copy the rules. They read them from the current version
of this guide: from a local clone of the guide, or from GitHub if there is
none. A change to a rule therefore reaches the skills without an update of
the skills.

The skills follow the open
`Agent Skills <https://agentskills.io/>`_ format. Every tool that supports
this format can use them.

..  _ai-assistance-skills-claude-code:

Install the skills in Claude Code
---------------------------------

Run the following commands in Claude Code:

..  code-block:: text
    :caption: Install the skills as the plugin typo3-docs

    /plugin marketplace add TYPO3-Documentation/TYPO3CMS-Guide-HowToDocument
    /plugin install typo3-docs@typo3-docs-guide

Claude Code then uses the skill `typo3-docs-writing` when a task changes
reST files of a TYPO3 manual or of an extension. You can also ask for a
skill by its name.

..  _ai-assistance-skills-other-tools:

Use the skills in other tools
-----------------------------

Each tool reads skills from a folder of its own. See the documentation of
your tool for this folder.

#.  Clone the repository of this guide:

    ..  code-block:: bash

        git clone https://github.com/TYPO3-Documentation/TYPO3CMS-Guide-HowToDocument.git

#.  Link each folder in :path:`skills/` into the skills folder of your
    tool.

A link instead of a copy keeps the skills up to date when you pull the
clone. The skills can also read the rules from this clone.

..  _ai-assistance-reading:

Let the assistant read the documentation
========================================

An assistant that needs a fact from a TYPO3 manual should read the page,
not answer from memory. Give it the permalink of the section. Every page on
docs.typo3.org is also published as Markdown, and every manual has an
:file:`llms.txt` that lists its pages. See
`What a render publishes beside the pages <https://docs.typo3.org/permalink/h2document:rendered-artifacts>`_.

..  _ai-assistance-check:

Check the result
================

Check every change of an assistant before you commit it:

#.  Run :bash:`make test-docs` and fix every warning.
#.  Read the rendered pages that changed. The render does not catch
    everything, for example a role that runs on into the following text.
#.  Run the skill `typo3-docs-style-check` on the changed files, or check
    them against the rules yourself. The render does not check the line
    length, sentence case, the serial comma, or the wording.
#.  Read the diff once more, see
    `You are responsible for the result <https://docs.typo3.org/permalink/h2document:ai-assistance-responsibility>`_.
