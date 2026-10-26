..  include:: /Includes.rst.txt
..  index:: reST; PHP domain
..  _rest-phpdomain:

==========
PHP domain
==========

In order to describe PHP code in TYPO3's documentation,
our toolchain has an integrated extension inspired by the
`PHP domain <https://pypi.org/project/sphinxcontrib-phpdomain/>`__
of the Sphinx project.

The source code of the PHP domain extension is located on GitHub:

https://github.com/TYPO3-Documentation/guides-php-domain

..  _rest-phpdomain-quick-example:

Quick example
=============

..  php:namespace::  Vendor\Extension

..  php:class:: DateTime

    Datetime class

    ..  php:method:: setDate($year, $month, $day)

        Set the date.

        :param int $year: The year.
        :param int $month: The month.
        :param int $day: The day.
        :returns: Either false on failure, or the datetime object for method chaining.

    ..  php:method:: setTime($hour, $minute[, $second])

        Set the time.

        :param int $hour: The hour
        :param int $minute: The minute
        :param int $second: The second
        :returns: Either false on failure, or the datetime object for method chaining.

    ..  php:const:: ATOM

        Y-m-d\TH:i:sP

..  code-block:: rst

    ..  php:namespace::  Vendor\Extension

    ..  php:class:: DateTime

        Datetime class

        ..  php:method:: setDate($year, $month, $day)

            Set the date.

            :param int $year: The year.
            :param int $month: The month.
            :param int $day: The day.
            :returns: Either false on failure, or the datetime object for method chaining.

        ..  php:method:: setTime($hour, $minute[, $second])

            Set the time.

            :param int $hour: The hour
            :param int $minute: The minute
            :param int $second: The second
            :returns: Either false on failure, or the datetime object for method chaining.

        ..  php:const:: ATOM

            Y-m-d\TH:i:sP

..  _rest-phpdomain-best-practices:

Best practices
==============

*   Use :ref:`namespaces <rest-phpdomain-namespaces>` wherever they apply.
*   Show a type of the TYPO3 Core with the
    `typo3:api-class directive <https://docs.typo3.org/permalink/h2document:rest-phpdomain-api-class>`_
    instead of writing it by hand. The directive keeps the type up to date.
*   Document only public, not internal entities,
    as developers must not depend on the internal API.
*   Configuration values stored in PHP arrays should be documented
    using the :ref:`confval directive <rest-confval>`.
    The PHP domain does not have directives to document nested PHP arrays.

..  _rest-phpdomain-namespaces:

Namespaces
==========

Use namespaces wherever they are applicable.

Create a namespace once per document that becomes the link target:

..  code-block:: rst

    ..  php:namespace::  Vendor\Extension

..  _rest-phpdomain-examples:

Examples
========

..  _rest-phpdomain-events:

Events
------

PSR-14 events are - technically - PHP classes. So they can be documented
just like PHP classes.

..  php:namespace:: TYPO3\CMS\Seo\Event

..  php:class:: ModifyUrlForCanonicalTagEvent

    PSR-14 to alter (or empty) a canonical URL for the href="" attribute of a canonical URL.

    ..  php:method:: getUrl()

        :returntype: string

    ..  php:method:: setUrl(string url)

        :param string $url: the url

..  code-block:: rst

    ..  php:namespace::  TYPO3\CMS\Seo\Event

    ..  php:class:: ModifyUrlForCanonicalTagEvent

        PSR-14 to alter (or empty) a canonical URL for the href="" attribute of a canonical URL.

        ..  php:method:: getUrl()

            :returntype: string

        ..  php:method:: setUrl(string url)

            :param string $url: the url

..  _rest-phpdomain-interfaces:

Interfaces
----------

..  php:namespace:: TYPO3\CMS\Core\Error

..  php:interface:: ErrorHandlerInterface

    ..  php:method:: setExceptionalErrors($exceptionalErrors)

        Defines which error levels should result in an exception thrown.

        :param int $exceptionalErrors: The integer representing the E_* error level to handle as exceptions

    ..  php:method:: handleError($errorLevel, $errorMessage, $errorFile, $errorLine)

        Handles an error.
        If the error is registered as exceptionalError it will be converted into
        an exception, to be handled by the configured exception handler.

        Additionally the error message is written to the configured logs.
        If application is backend, the error message is also added to the
        flashMessageQueue, in frontend the error message is displayed in the
        admin panel (as TsLog message).

        :param int $errorLevel: The error level - one of the E_* constants
        :param string $errorMessage: The error message
        :param string $errorFile: Name of the file the error occurred in
        :param int $errorLine: Line number where the error occurred
        :returntype: bool
        :throws: :php:`TYPO3\CMS\Core\Error\Exception`

    ..  php:const:: ERROR_HANDLED

        true

    ..  php:attr:: testattr

        Value of some attribute.

..  code-block:: rst

    ..  php:namespace:: TYPO3\CMS\Core\Error

    ..  php:interface:: ErrorHandlerInterface

        ..  php:method:: setExceptionalErrors($exceptionalErrors)

            Defines which error levels should result in an exception thrown.

            :param int $exceptionalErrors: The integer representing the E_* error level to handle as exceptions

        ..  php:method:: handleError($errorLevel, $errorMessage, $errorFile, $errorLine)

            Handles an error.
            If the error is registered as exceptionalError it will be converted into
            an exception, to be handled by the configured exception handler.

            Additionally the error message is written to the configured logs.
            If application is backend, the error message is also added to the
            flashMessageQueue, in frontend the error message is displayed in the
            admin panel (as TsLog message).

            :param int $errorLevel: The error level - one of the E_* constants
            :param string $errorMessage: The error message
            :param string $errorFile: Name of the file the error occurred in
            :param int $errorLine: Line number where the error occurred
            :returntype: bool
            :throws: :php:class:`TYPO3\\CMS\\Core\\Error\\Exception`

        ..  php:const:: ERROR_HANDLED

            true

        ..  php:attr:: testattr

            Value of some attribute.

..  _rest-phpdomain-exceptions:

Exceptions
----------

..  php:namespace:: TYPO3\CMS\Core\Exception\Page

..  php:exception:: BrokenRootLineException

    Exception for root line traversal when a page within the root line traversal
    is missing / cannot be resolved.

..  code-block:: rst

    ..  php:namespace:: TYPO3\CMS\Core\Exception\Page

    ..  php:exception:: BrokenRootLineException

        Exception for root line traversal when a page within the root line traversal
        is missing / cannot be resolved.

..  _rest-phpdomain-traits:

Traits
------

..  php:namespace:: TYPO3\CMS\Core\Context

..  php:trait:: ContextAwareTrait

    ..  php:attr:: $context

    ..  php:method:: setContext(Context $context)

        :param TYPO3\\CMS\\Core\\Context\\Context $context: The context

    ..  php:method:: getContext()

        :returntype: TYPO3\\CMS\\Core\\Context\\Context

..  code-block:: rst

    ..  php:namespace:: TYPO3\CMS\Core\Context

    ..  php:trait:: ContextAwareTrait

        ..  php:attr:: $context

        ..  php:method:: setContext(Context $context)

            :param TYPO3\\CMS\\Core\\Context\\Context $context: The context

        ..  php:method:: getContext()

            :returntype: TYPO3\\CMS\\Core\\Context\\Context

..  _rest-phpdomain-links:

Linking to PHP entities
=======================

..  note::
    Backslashes have to be escaped by :rst:`\\`.

*   :php:exc:`TYPO3\\CMS\\Core\\Exception\\Page\\BrokenRootLineException`
*   :php:ns:`TYPO3\\CMS\\Core\\Exception\\Page`
*   :php:class:`Vendor\\Extension\\DateTime`
*   :php:class:`TYPO3\\CMS\\Seo\\Event\\ModifyUrlForCanonicalTagEvent`
*   :php:interface:`TYPO3\\CMS\\Core\\Error\\ErrorHandlerInterface`
*   :php:func:`Vendor\\Extension\\DateTime::setTime()`
*   :php:const:`Vendor\\Extension\\DateTime::ATOM`

..  code-block:: rst

    *   :php:exc:`TYPO3\\CMS\\Core\\Exception\\Page\\BrokenRootLineException`
    *   :php:ns:`TYPO3\\CMS\\Core\\Exception\\Page`
    *   :php:class:`Vendor\\Extension\\DateTime`
    *   :php:class:`TYPO3\\CMS\\Seo\\Event\\ModifyUrlForCanonicalTagEvent`
    *   :php:interface:`TYPO3\\CMS\\Core\\Error\\ErrorHandlerInterface`
    *   :php:func:`Vendor\\Extension\\DateTime::setTime()`
    *   :php:const:`Vendor\\Extension\\DateTime::ATOM`

With the :rst:`:any:` text role you can link to any PHP domain entity:

*   :any:`Vendor\\Extension\\DateTime`
*   :any:`Vendor\\Extension\\DateTime::setTime()`

..  code-block:: rst

    *   :any:`Vendor\\Extension\\DateTime`
    *   :any:`Vendor\\Extension\\DateTime::setTime()`

..  _rest-phpdomain-autogenerate:
..  _rest-phpdomain-api-class:

Show a type of the TYPO3 API
============================

The :rst:`typo3:api-class` directive shows a class, an interface, a trait,
or an enum of the TYPO3 Core with its members. Write the fully qualified
name of the type after the directive:

..  code-block:: rst

    ..  typo3:api-class:: \TYPO3\CMS\Impexp\Event\BeforeImportEvent

The directive reads the type from `api.typo3.org <https://api.typo3.org/>`__
when the manual is rendered. The manual itself contains no generated
reStructuredText, and the type stays up to date with the TYPO3 API.

The directive writes the type with the directives of the PHP domain, such as
:rst:`php:class`, :rst:`php:method`, and :rst:`php:const`. Link to the type
and its members like to a type that you documented by hand, see
`Linking to PHP entities <https://docs.typo3.org/permalink/h2document:rest-phpdomain-links>`_.
In the rendered page, the fully qualified name of the type opens a modal.
It shows the signature, the summary, and a link to the type on
api.typo3.org.

..  _rest-phpdomain-api-class-version:

TYPO3 version
-------------

The directive reads the type for the TYPO3 version that
`typo3-core-preferred <https://docs.typo3.org/permalink/h2document:confval-guides-extension-typo3-core-preferred>`_
in :file:`guides.xml` names:

*   `stable`, the default, is the latest LTS version.
*   `oldstable` is the LTS version before it.
*   `main` and `dev` both name the version in development.
*   A major version, such as `13`, is the LTS version of that major
    version, here 13.4.
*   A version such as `12.4` is used as it is.

If that version of TYPO3 does not have the type, the directive shows
nothing and the rendering writes a warning.

..  _rest-phpdomain-api-class-left-out:

Types the directive leaves out
------------------------------

The directive shows nothing and writes a warning in these cases:

*   The type is marked `@internal`. Use the option `:include-internal:` to
    show it anyway.
*   The TYPO3 API does not document the type. This is the case for a type
    of a third party package, such as
    :php:`\Psr\Http\Server\MiddlewareInterface`, and for a misspelled name.

..  _rest-phpdomain-api-class-options:

Options
-------

Without an option, the directive shows the type with its public constants,
properties, and methods, except `__construct()`, and the cases of an enum.

`:members:`
    Shows only these constants, properties, methods, and cases, in this
    order. Separate the names with commas. A method name is not case
    sensitive, as in PHP. The rendering warns about a name that the type does
    not have.

`:visibility:`
    The visibilities to show, separated by commas, by default `public`.
    For example, `public, protected` also shows the protected members.

`:include-internal:`
    Also shows a type or a member that is marked `@internal`.

`:exclude-deprecated:`
    Leaves out a deprecated method. By default, a deprecated method is shown
    with a notice.

`:include-constructor:`
    Also shows `__construct()`.

`:no-class-comment:`
    Leaves out the description of the type.

`:no-member-comment:`
    Leaves out the descriptions of the members.

`:no-parameters:`
    Leaves out the descriptions of the parameters and of the return value.

`:noindex:`
    Does not register the type for links and the index. Use it when a page
    shows a type a second time.

`:noindex-members:`
    Does not register the members.

The following example shows four methods of a class, without the
description of the class:

..  code-block:: rst

    ..  typo3:api-class:: \TYPO3\CMS\Core\Site\Entity\Site
        :members: getIdentifier, getBase, getLanguages, getLanguageById
        :no-class-comment:

..  _rest-phpdomain-api-class-snippets:

Replace a generated code snippet
--------------------------------

Some manuals include the API of a type as a snippet that the abandoned
generator :composer:`t3docs/codesnippet` created, see
`Generated code snippets <https://docs.typo3.org/permalink/h2document:codesnippet-generation>`_.
The options of the directive are the settings of the `createPhpClassDocs`
action of that generator.

The directive creates the same anchors and the same entries in
:file:`objects.inv.json` as such a snippet. A page can thus replace the
include of the snippet with the directive, and links to the type and its
members keep working:

..  code-block:: diff

    -..  include:: /CodeSnippets/Events/Impexp/BeforeImportEvent.rst.txt
    +..  typo3:api-class:: \TYPO3\CMS\Impexp\Event\BeforeImportEvent

The output is close to that of the snippet, but not identical. For example,
the directive marks a class as :php:`final` and :php:`readonly`. It also
shows the type from the doc comment where that type is more precise than
the one in the signature, such as :php:`string[]` instead of :php:`array`.
