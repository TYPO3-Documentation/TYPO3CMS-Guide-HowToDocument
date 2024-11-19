..  include:: /Includes.rst.txt
..  index:: reST; PHP domain
..  _rest-phpdomain:

==========
PHP domain
==========

In order to describe PHP code in TYPO3's documentation,
our toolchain has an integrated extension inspired by the
`PHP domain<https://pypi.org/project/sphinxcontrib-phpdomain/>`__
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
*   When possible :ref:`autogenerate <rest-phpdomain-autogenerate>`
    the reST code, this helps keep it up-to-date.
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

Reuse a namespace, but prevent it from becoming a link target:

..  code-block:: rst

    ..  php:currentnamespace:: Vendor\Extension

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
        an exception, to be handled by the configured exceptionhandler.

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
            an exception, to be handled by the configured exceptionhandler.

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
    is missing / can not be resolved.

..  code-block:: rst

    ..  php:namespace:: TYPO3\CMS\Core\Exception\Page

    ..  php:exception:: BrokenRootLineException

        Exception for root line traversal when a page within the root line traversal
        is missing / can not be resolved.

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
    *   :php:const:`Vendor\\Extension\\DateTime\\ATOM`

With the :rst:`:any:` directive you can link to any PHP domain entity:

*   :any:`Vendor\\Extension\\DateTime`
*   :any:`Vendor\\Extension\\DateTime::setTime()`

..  code-block:: rst

    *   :any:`Vendor\\Extension\\DateTime`
    *   :any:`Vendor\\Extension\\DateTime::setTime()`

..  _rest-phpdomain-autogenerate:

Autogenerate PHP domain syntax
==============================

We are currently working on the automatic generation of PHP domain syntax
from PHP classes within the
`TYPO3 Screenshots <https://github.com/TYPO3-Documentation/t3docs-screenshots/pull/234>`__
tool.
