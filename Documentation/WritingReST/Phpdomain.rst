.. include:: /Includes.rst.txt
.. highlight:: rst
.. index:: reST; PHP domain
.. _rest-phpdomain:

==========
PHP domain
==========

About Sphinx extension `sphinxcontrib-phpdomain
<https://pypi.org/project/sphinxcontrib-phpdomain/>`__.

.. _rest-phpdomain-quick-example:

Quick example
=============

This is source:

.. code-block:: rst

   .. php:namespace::  Vendor\Extension

   .. php:class:: DateTime

      Datetime class

      .. php:method:: setDate($year, $month, $day)

         Set the date.

         :param int $year: The year.
         :param int $month: The month.
         :param int $day: The day.
         :returns: Either false on failure, or the datetime object for method chaining.


      .. php:method:: setTime($hour, $minute[, $second])

         Set the time.

         :param int $hour: The hour
         :param int $minute: The minute
         :param int $second: The second
         :returns: Either false on failure, or the datetime object for method chaining.

      .. php:const:: ATOM

         Y-m-d\TH:i:sP


.. php:namespace::  Vendor\Extension

.. php:class:: DateTime

   Datetime class

   .. php:method:: setDate($year, $month, $day)

      Set the date.

      :param int $year: The year.
      :param int $month: The month.
      :param int $day: The day.
      :returns: Either false on failure, or the datetime object for method chaining.


   .. php:method:: setTime($hour, $minute[, $second])

      Set the time.

      :param int $hour: The hour
      :param int $minute: The minute
      :param int $second: The second
      :returns: Either false on failure, or the datetime object for method chaining.

   .. php:const:: ATOM

      Y-m-d\TH:i:sP

.. _rest-phpdomain-best-practices:

Best practices
==============

*  Use :ref:`namespaces <rest-phpdomain-namespaces>` wherever they apply.
*  If possible :ref:`autogenerate <rest-phpdomain-autogenerate>` the rst code,
   this helps keeping it up to date
*  Only document public, non internal entities, as developers cannot depend
   on internal API.
*  Configuration values stored in PHP arrays should be documented with
   the :ref:`confval directive <rest-confval>`. Phpdomain has no
   features to document nested PHP arrays.

.. _rest-phpdomain-namespaces:

Namespaces
==========

Use namespaces where ever they apply.

Create a namespace (once per document)::

   .. php:namespace::  Vendor\Extension

Add something to an existing namespace from other where in the document::

   .. php:currentnamespace:: Vendor\Extension

.. _rest-phpdomain-examples:

Examples
========

.. _rest-phpdomain-events:

Documenting an event:
---------------------

PSR-14 events are - technically - PHP classes. So they can be documented
just like a php class.

.. code-block:: rst

   .. php:namespace::  TYPO3\CMS\Seo\Event

   .. php:class:: ModifyUrlForCanonicalTagEvent

      PSR-14 to alter (or empty) a canonical URL for the href="" attribute of a canonical URL.

      .. php:method:: getUrl()

         :returntype: string

      .. php:method:: setUrl(string url)

         :param string $url: the url

.. php:namespace:: TYPO3\CMS\Seo\Event

.. php:class:: ModifyUrlForCanonicalTagEvent

   PSR-14 to alter (or empty) a canonical URL for the href="" attribute of a canonical URL.

   .. php:method:: getUrl()

      :returntype: string

   .. php:method:: setUrl(string url)

      :param string $url: the url

.. _rest-phpdomain-interfaces:

Documenting interfaces:
-----------------------

.. php:namespace:: TYPO3\CMS\Core\Error

.. php:interface:: ErrorHandlerInterface

   .. php:method:: setExceptionalErrors($exceptionalErrors)

      Defines which error levels should result in an exception thrown.

      :param int $exceptionalErrors: The integer representing the E_* error level to handle as exceptions

   .. php:method:: handleError($errorLevel, $errorMessage, $errorFile, $errorLine)

      Handles an error.
      If the error is registered as exceptionalError it will by converted into
      an exception, to be handledby the configured exceptionhandler.

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

   .. php:const:: ERROR_HANDLED

      true

   .. php:attr:: testattr

      Value of some attribute

Document the class so we can link to it:

.. php:class:: Exception

   An exception which represents a PHP error.

.. _rest-phpdomain-exceptions:

Documenting exceptions
----------------------

.. code-block:: rst

   .. php:namespace:: TYPO3\CMS\Core\Exception\Page

   .. php:exception:: BrokenRootLineException

      Exception for root line traversal when a page within the root line traversal
      is missing / can not be resolved

.. php:namespace:: TYPO3\CMS\Core\Exception\Page

.. php:exception:: BrokenRootLineException

   Exception for root line traversal when a page within the root line traversal
   is missing / can not be resolved

.. _rest-phpdomain-traits:

Documenting traits
------------------

.. code-block:: rst

   .. php:namespace:: TYPO3\CMS\Core\Context

   .. php:trait:: ContextAwareTrait

      .. php:attr:: $context

      .. php:method:: setContext(Context $context)

         :param TYPO3\\CMS\\Core\\Context\\Context $context: The context

      .. php:method:: getContext()

         :returntype: TYPO3\\CMS\\Core\\Context\\Context

.. php:namespace:: TYPO3\CMS\Core\Context

.. php:trait:: ContextAwareTrait

   .. php:attr:: $context

   .. php:method:: setContext(Context $context)

      :param TYPO3\\CMS\\Core\\Context\\Context $context: The context

   .. php:method:: getContext()

      :returntype: TYPO3\\CMS\\Core\\Context\\Context

Document class so we can link to it

.. php:class:: Context

.. _rest-phpdomain-links:

Linking to PHP entities
=======================

.. code-block:: rst

   *  :php:exc:`TYPO3\\CMS\\Core\\Exception\\Page\\BrokenRootLineException`
   *  :php:ns:`TYPO3\\CMS\\Core\\Exception\\Page`
   *  :php:class:`Vendor\\Extension\\DateTime`
   *  :php:class:`TYPO3\\CMS\\Seo\\Event\\ModifyUrlForCanonicalTagEvent`
   *  :php:func:`Vendor\\Extension\\DateTime::setTime()`
   *  :php:const:`Vendor\\Extension\\DateTime\\ATOM`

*  :php:exc:`TYPO3\\CMS\\Core\\Exception\\Page\\BrokenRootLineException`
*  :php:ns:`TYPO3\\CMS\\Core\\Exception\\Page`
*  :php:class:`Vendor\\Extension\\DateTime`
*  :php:class:`TYPO3\\CMS\\Seo\\Event\\ModifyUrlForCanonicalTagEvent`
*  :php:func:`Vendor\\Extension\\DateTime::setTime()`
*  :php:const:`Vendor\\Extension\\DateTime::ATOM`

You can link to any PHP domain entity by using directive :rst:`:any:`::

   *  :any:`Vendor\\Extension\\DateTime`
   *  :any:`Vendor\\Extension\\DateTime::setTime()`


*  :any:`Vendor\\Extension\\DateTime`
*  :any:`Vendor\\Extension\\DateTime::setTime()`


.. note::
   Backslashes have to be escaped by :rst:`\\`.

.. _rest-phpdomain-autogenerate:

Autogenerate PHP domain syntax
==============================

We are currently working on auto-generating the PHP domain syntax from
PHPDoc comments within the
`TYPO3 docs screenshot tool <https://github.com/TYPO3-Documentation/t3docs-screenshots/pull/234>`__.
