# AGENTS.md — TYPO3 "How to Document" Guide

## Repo structure

```
Documentation/                   # the actual manual (reST source, published to docs.typo3.org)
├── Advanced/ContentStyleGuide.rst   # official writing style guide (sentence case, spelling, capitalization)
├── Advanced/CodingGuidelines.rst    # reST formatting conventions (indentation, markers)
├── Reference/ReStructuredText/      # reST syntax reference (roles, directives, anchors, code blocks, ...)
└── ...
CONTRIBUTING.rst                 # how to contribute (issues, branching, PRs)
```

## Commands

- `make docs` — render the manual locally with Docker
- `make test-docs` — render in minimal-test mode; use this to validate any change before committing

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
8. **Commit message**: short body explaining why, ending with
   `Assisted-by: <tool/model name> <contact>` and
   `Signed-off-by: <actual committer name>` trailers. This repo has only
   `main` (no LTS branches), so skip `Releases:`/`Resolves:`.

## References

- [CONTRIBUTING.rst](CONTRIBUTING.rst) — contribution workflow
- [Documentation/Advanced/ContentStyleGuide.rst](Documentation/Advanced/ContentStyleGuide.rst) — official writing style guide
- [Documentation/Advanced/CodingGuidelines.rst](Documentation/Advanced/CodingGuidelines.rst) — reST formatting conventions
- [Documentation/Reference/ReStructuredText/](Documentation/Reference/ReStructuredText/) — reST syntax reference (roles, directives, anchors, code blocks, ...)
