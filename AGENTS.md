# AGENTS.md — TYPO3 "How to Document" Guide

## Repo structure

```
Documentation/                   # the actual manual (reST source, published to docs.typo3.org)
├── Advanced/ContentStyleGuide.rst   # official writing style guide (sentence case, spelling, capitalization)
├── Advanced/CodingGuidelines.rst    # reST formatting conventions (indentation, markers)
├── Reference/ReStructuredText/      # reST syntax reference (roles, directives, anchors, code blocks, ...)
└── ...
CONTRIBUTING.rst                 # how to contribute (issues, branching, PRs)
Build/ReviewAids/                # scripts that help review a change in any manual
```

## Commands

- `make docs` — render the manual locally with Docker
- `make test-docs` — render in minimal-test mode (the same validation CI runs); use this to validate any change before committing

## Reviewing a change

`Build/ReviewAids/` holds scripts that report what is worth a second look in
a documentation change — in this repository or in any other manual, since the
rules they check are the ones defined here. They report and never edit, and
none of them is a test: see [Build/ReviewAids/README.md](Build/ReviewAids/README.md)
for what each one is blind to before trusting a clean run.

## Rules

1. **reST, not Markdown** — everything under `Documentation/` is reStructuredText.
2. **Sentence case headlines** — first word and proper nouns only; see `Documentation/Advanced/ContentStyleGuide.rst`.
3. **4-space indentation** for directive bodies, 2 spaces after `..` markers; see `Documentation/Advanced/CodingGuidelines.rst`.
4. **Single backticks over double**, unless the content needs a literal
   backtick; see `Documentation/Reference/ReStructuredText/Code/InlineCode.rst`.
5. **Every headline needs a `..  _anchor:` target** directly above it; see
   `Documentation/Reference/ReStructuredText/Links/Anchors.rst`.
6. **Validate before committing** — run `make test-docs`.
7. **Never commit or push without being asked.**
8. **Commit message**: follow [Documentation/Advanced/CommitMessages.rst](Documentation/Advanced/CommitMessages.rst).
   This repo has only `main` (no LTS branches), so skip `Releases:`/`Resolves:`.

## References

- [Build/ReviewAids/README.md](Build/ReviewAids/README.md) — review aids, and why they are not tests
- [CONTRIBUTING.rst](CONTRIBUTING.rst) — contribution workflow
- [Documentation/Advanced/CommitMessages.rst](Documentation/Advanced/CommitMessages.rst) — commit message conventions
- [Documentation/Advanced/ContentStyleGuide.rst](Documentation/Advanced/ContentStyleGuide.rst) — official writing style guide
- [Documentation/Advanced/CodingGuidelines.rst](Documentation/Advanced/CodingGuidelines.rst) — reST formatting conventions
- [Documentation/Reference/ReStructuredText/](Documentation/Reference/ReStructuredText/) — reST syntax reference (roles, directives, anchors, code blocks, ...)
