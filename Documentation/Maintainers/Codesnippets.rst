..  include:: /Includes.rst.txt
..  _codesnippet-generation:

=======================
Generated code snippets
=======================

Some manuals contain code snippets that the generator
:composer:`t3docs/codesnippet` created from the source code of TYPO3. Such a
snippet shows, for example, the API of a PSR-14 event or an excerpt of the
TCA. The generator is abandoned, and its repository is archived. The
manuals for TYPO3 v13 and newer no longer run it.

The snippet files stay in the manuals. A page includes such a file like any
other file:

..  code-block:: rst

    ..  include:: /CodeSnippets/Events/Core/SomeEvent.rst.txt

..  _codesnippet-add-new:

Document the API of a new type
==============================

Do not add a generated snippet for a new type. To show the API of a type of
the TYPO3 Core, write the
`typo3:api-class directive <https://docs.typo3.org/permalink/h2document:rest-phpdomain-api-class>`_
with the fully qualified name of the type:

..  code-block:: rst

    ..  typo3:api-class:: \TYPO3\CMS\Core\Routing\Event\AfterPageUriGeneratedEvent

The directive reads the API from api.typo3.org when the manual is rendered.
It needs no snippet file and no configuration. Its
`options <https://docs.typo3.org/permalink/h2document:rest-phpdomain-api-class-options>`_
select the members to show, for example:

..  code-block:: rst

    ..  typo3:api-class:: \TYPO3\CMS\Core\Site\Entity\Site
        :members: getIdentifier, getBase, getLanguages
        :no-class-comment:

..  _codesnippet-regeneration:

Change a generated code snippet
===============================

Nothing generates the snippet files again. If the snippet shows the API of
a type, replace its include with the directive. The directive creates the
same anchors as the snippet, so links to the type and its members keep
working:

..  code-block:: diff

    -..  include:: /CodeSnippets/Events/Impexp/BeforeImportEvent.rst.txt
    +..  typo3:api-class:: \TYPO3\CMS\Impexp\Event\BeforeImportEvent

Then delete the snippet file, unless another page still includes it. See
`Replace a generated code snippet <https://docs.typo3.org/permalink/h2document:rest-phpdomain-api-class-snippets>`_
for the differences in the output.

Edit any other snippet file by hand.
