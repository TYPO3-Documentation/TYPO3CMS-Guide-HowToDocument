# AGENTS.md — my_extension

## Repository structure

```
Classes/          # PHP code of the extension
Configuration/    # TCA, site set, and services
Documentation/    # the manual, reST source published to docs.typo3.org
Resources/        # templates, language files, and assets
composer.json     # the supported TYPO3 versions
```

## Commands

Render the manual and fail on every warning:

```bash
mkdir -p Documentation-GENERATED-temp
docker run --rm --pull always -v $(pwd):/project \
  ghcr.io/typo3-documentation/render-guides:latest \
  --config=Documentation --no-progress --minimal-test
```

Run it before every commit that changes `Documentation/`.

## Documentation rules

The manual follows the TYPO3 "How to document" guide. Read the rules
there instead of writing from memory:

- Writing style: https://docs.typo3.org/permalink/h2document:content-styleguide
- reST formatting: https://docs.typo3.org/permalink/h2document:format-rest-cgl
- Anchors: https://docs.typo3.org/permalink/h2document:link-anchor
- Links: https://docs.typo3.org/permalink/h2document:permalinks

If the skill `typo3-docs-writing` is installed, use it for every change
in `Documentation/`.

Rules of this repository:

- Check every fact about this extension against `Classes/` and
  `Configuration/` of the branch you work on.
- Check every fact about the TYPO3 Core against the lowest and the
  highest TYPO3 version that `composer.json` allows.
- Never remove an anchor, also not when you delete a section.

## Commits

- Never commit or push without being asked.
- Write the summary line in the imperative, and explain in the body
  why the change is needed.
- Add an `Assisted-by: <tool/model name> <contact>` trailer if you used
  AI assistance for more than a basic spelling or grammar check.
