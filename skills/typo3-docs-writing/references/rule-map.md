# Which page holds the rule

Each page is named by its path without a file extension. Read it as
published Markdown, `<page>.md` on docs.typo3.org, or as the source
`Documentation/<page>.rst`, see step 1 of the skill. In the Markdown, an
anchor ends a heading as `{#anchor}`, or stands before it as
`<a id="anchor"></a>` if the heading has several. In the source, it is the
`..  _anchor:` target. An anchor of the guide never goes away, so a search
for it always finds the current section, even after the page has moved.

Read the page for every kind of content that your text contains.

## Words and sentences

| Content | Path | Anchor |
|---|---|---|
| Sentences, paragraphs, terms, the imperative | `Advanced/ContentStyleGuide` | `content-styleguide-sentences` |
| Serial comma | `Advanced/ContentStyleGuide` | `content-styleguide-serial-comma` |
| Words that call a task easy | `Advanced/ContentStyleGuide` | `content-styleguide-difficulty` |
| Capitalization of headlines | `Advanced/ContentStyleGuide` | `spelling-ref-title` |
| Capitalization in text, TYPO3 spellings, acronyms | `Advanced/ContentStyleGuide` | `spelling-plain-text` |
| Buttons, links, and GUI elements | `Advanced/ContentStyleGuide` | `spelling-anchor-text`, `spelling-refer-to-gui-elements` |
| Preferred spelling of a term | `Advanced/Glossary` | `preferred-terms` |
| GUI elements and keystrokes in reST | `Advanced/CodingGuidelines` | `rest-refer-to-gui-elements`, `format-rest-cgl-refering-keystrokes` |

## Structure of the source

| Content | Path | Anchor |
|---|---|---|
| Indentation, line length, special characters | `Advanced/CodingGuidelines` | `format-rest-cgl-basic-formatting-rules` |
| Headline levels and underlines | `Advanced/CodingGuidelines` | `rest-cgl-headline-underlines` |
| Headlines and their anchors | `Reference/ReStructuredText/Menus/HeadlinesAndSection` | `headlines-and-sections` |
| Anchors, and keeping them working | `Reference/ReStructuredText/Links/Anchors` | `link-anchor`, `anchor-persistence` |
| Renaming, moving, or deleting a page | `Advanced/Redirects` | `redirects` |
| Files and folders of a manual | `Reference/FileStructure` | `file-structure` |
| Menus, toctree, and orphan pages | `Reference/ReStructuredText/Menus/MenuHierarchy` | `toctree` |
| Short title in the menu | `Reference/ReStructuredText/Menus/NavigationTitle` | `navigation-title` |
| Including a file | `Reference/ReStructuredText/Menus/IncludingFiles` | `including-files` |
| Settings of the manual in `guides.xml` | `Reference/GuidesXml` | `guides-xml` |
| `README` of an extension | `Advanced/ReadmeFile` | `readme-rst` |

## Links

| Content | Path | Anchor |
|---|---|---|
| Links to TYPO3 documentation, permalinks, link texts | `Reference/ReStructuredText/Links/Documentation` | `permalinks`, `permalinks-rules`, `link-text` |
| Composer packages and TYPO3 extensions | `Reference/ReStructuredText/Links/Composer` | `linking-extensions` |
| The TYPO3 API | `Reference/ReStructuredText/Links/Api` | `links-api` |
| Source code of the TYPO3 Core | `Reference/ReStructuredText/Links/CoreSource` | `linking-core-source` |
| External links | `Reference/ReStructuredText/Links/ExternalLinks` | `external-links` |
| Example domains | `Reference/ReStructuredText/Links/ExampleLinks` | `preventing-links` |

## Code

| Content | Path | Anchor |
|---|---|---|
| Inline code, and when to use a code role | `Reference/ReStructuredText/Code/InlineCode` | `inline-code`, `inline-code-when-to-use-a-role` |
| PHP classes, members, and namespaces | `Reference/ReStructuredText/Code/InlineCode` | `inline-code-php` |
| TypoScript and TSconfig | `Reference/ReStructuredText/Code/InlineCode` | `inline-code-typoscript` |
| Fluid ViewHelpers in text | `Reference/ReStructuredText/Code/InlineCode` | `inline-code-fluid` |
| Other text roles, backslashes in roles | `Reference/ReStructuredText/InlineMarkup/TextRoles/Index` | `text-roles` |
| Code blocks, captions, literalinclude | `Reference/ReStructuredText/Code/Codeblocks` | `writing-rest-codeblocks-with-syntax-highlighting` |
| Example names, namespaces, and sets | `Reference/ReStructuredText/Code/Codeblocks` | `codeblocks-example-names` |
| Placeholders in code | `Reference/ReStructuredText/Code/Codeblocks` | `codeblocks-placeholders` |
| Code that must be syntactically correct | `Reference/ReStructuredText/Code/Codeblocks` | `codeblocks-syntactically-correct` |
| Configuration values (confval) | `Reference/ReStructuredText/Code/Confval` | `rest-confval` |
| Site settings | `Reference/ReStructuredText/Code/SiteSettings` | `reference-site-settings` |
| PHP domain | `Reference/ReStructuredText/Code/Phpdomain` | `rest-phpdomain` |
| Fluid ViewHelper reference | `Reference/ReStructuredText/Content/ViewHelper` | `viewhelper` |
| Directory trees | `Reference/ReStructuredText/Lists/DirectoryTree` | `writing-rest-directory-tree` |

## Content elements

| Content | Path | Anchor |
|---|---|---|
| Added, changed, deprecated, removed | `Reference/ReStructuredText/Content/Versions` | `rest-versions` |
| Version hints and changelog links | `Advanced/CodingGuidelines` | `format-rest-cgl-add-version-hints`, `link-to-changelog` |
| Notes, tips, warnings | `Reference/ReStructuredText/Content/Admonitions` | `rest-admonitions` |
| Tables | `Reference/ReStructuredText/Content/Tables` | `rest-tables` |
| Tabs | `Reference/ReStructuredText/Content/Tabs` | `rest-tabs` |
| Cards | `Reference/ReStructuredText/Content/Cards` | `rest-cards` |
| Accordions | `Reference/ReStructuredText/Content/Accordion` | `rest-accordion` |
| Comments in the source | `Reference/ReStructuredText/Content/Comments` | `writing-rest-comments` |
| Special characters | `Reference/ReStructuredText/Content/SpecialCharacters` | `reference-re-structured-text-content-special-characters` |
| Bullet, numbered, and definition lists | `Reference/ReStructuredText/Lists/Index` | `rest-lists` |
| Bold and italic | `Reference/ReStructuredText/InlineMarkup/InlineMarkup/Index` | `rest-bold-italic` |

## Images

| Content | Path | Anchor |
|---|---|---|
| Images and figures in reST | `Reference/ReStructuredText/Graphics/Images` | `how-to-document-images` |
| Formats and screenshots | `Advanced/GuidelinesForImages` | `guidelines-for-images` |
| Alignment | `Reference/ReStructuredText/Graphics/ImageAlignment` | `image-float-alignment` |
| Zoom | `Reference/ReStructuredText/Graphics/ImageZoom` | `image-zoom` |
| Diagrams | `Reference/ReStructuredText/Graphics/Diagrams` | `plantuml-diagrams` |

## Commits and pull requests

| Content | Path | Anchor |
|---|---|---|
| Commit message | `Advanced/CommitMessages` | `commit-messages` |
| Pull requests and review | `Advanced/ReviewPolicy` | `review-policy` |
