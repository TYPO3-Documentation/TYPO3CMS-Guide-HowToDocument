:navigation-title: API links

..  _links-api:

================================================
API links: More information on TYPO3 PHP classes
================================================

At https://api.typo3.org/ all classes and interfaces of the
TYPO3 Core are listed with their public members and descriptions. The API
itself also links to the source code on GitHub. You can use implicit and
explicit links to these:

..  contents::

..  _links-api-explicit:

Explicit links to api.typo3.org
===============================

..  literalinclude:: _Api.rst.txt

The links then look like this:

..  include:: _Api.rst.txt

Explicit links can use the interlink scheme to link to different TYPO3 versions.
If not specified they also link to the :confval:`guides-extension-typo3-core-preferred`.

If you want to link directly to the source files on GitHub, you can use the
:ref:`:t3src: text role <linking-core-source>`.

..  _links-api-fqn:

Implicit links to fully-qualified names
=======================================

Implicit links have the advantage that they show more information about the
class or interface in a popover while they still offer a link to the API.

..  literalinclude:: _ApiImplicit.rst.txt

The links then look like this:

..  include:: _ApiImplicit.rst.txt

As you can see, only links to the namespace `/TYPO3/CMS` can be linked to the
API. We do display general information about some other namespaces that are
commonly used in TYPO3 development. Example namespaces should always start with
`\MyVendor\`. Use `\MyVendor\MyExtension\` for extensions and
`\MyVendor\MySitepackage\` for sitepackages.

Implicit links are always referring to your
:confval:`guides-extension-typo3-core-preferred` as set in the
:ref:`guides.xml <guides-xml>`.

..  _links-api-short:

Links to the API with the short class name
==========================================

Using the text role `php-short` you can display the short name of the class
or interface within the text. Other then that it works just like the
:ref:`:php: <links-api-fqn>` text role.

..  literalinclude:: _ApiShort.rst.txt

The links then look like this:

..  include:: _ApiShort.rst.txt
