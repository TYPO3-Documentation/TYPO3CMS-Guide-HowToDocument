.. include:: /Includes.rst.txt

.. _user-round-trip:

=================
User's round trip
=================

Once the user is interested in a TYPO3 extension, a Composer package or a
standalone manual, they should be quickly directed to all aspects of the
project: 

*  Rendered documentation
*  Code repository (Github, Gitlab etc)
*  Packagist
*  TYPO3 Extension Repository (TER)
*  Where to report issues

Therefore, set up a convenient
navigation from one aspect to another by using native configuration settings.

.. uml::

   !include <tupadr3/font-awesome-5/typo3>

   skinparam DefaultTextAlignment center
   skinparam RectangleBackgroundColor transparent
   skinparam RectangleBorderColor transparent
   skinparam UsecaseFontColor<< inactive >> #b9b9b9
   skinparam UsecaseBorderColor<< inactive >> #b9b9b9
   skinparam UsecaseBackgroundColor<< inactive >> #FEFEFE

   rectangle "<color:#f49700><$typo3></color>\n Extension / Package / Manual" as typo3actor
   usecase "Packagist" as packagist
   usecase "VCS repository" as vcsRepository
   usecase "Documentation" as documentation
   usecase "TYPO3 Extension Repository" as ter

   typo3actor -left-> packagist
   typo3actor -right-> vcsRepository
   typo3actor -up-> documentation
   typo3actor -down-> ter

   packagist <-up-> documentation
   documentation <-down-> vcsRepository
   vcsRepository <-down-> ter
   ter <-up-> packagist

   hide << inactive >> stereotype

**Table of Contents:**

.. contents::
   :backlinks: top
   :class: compact-list
   :depth: 2
   :local:


.. _user-round-trip-project-aspects:

Project aspects
===============


.. _user-round-trip-documentation-aspect:

Documentation
-------------

Guide the user from the documentation to the other aspects by setting these
Sphinx theme configuration properties at :ref:`settings-cfg`:

.. code-block:: none

   project_home         = <typo3-extension-repository>
   project_repository   = <vcs-repository>
   project_issues       = <vcs-repository-issues>

for example for the *News System* extension:

.. code-block:: none

   project_home         = https://extensions.typo3.org/extension/news/
   project_repository   = https://github.com/georgringer/news
   project_issues       = https://github.com/georgringer/news/issues

and find the links to the other aspects displayed in the footer of the rendered
documentation (see `News System example <https://docs.typo3.org/p/georgringer/news/main/en-us/>`__).

For a Composer package, replace the TER URL with the Packagist URL. For a
standalone manual, replace the TER URL with the documentation URL.

The Packagist URL is linked indirectly from the TER page and is therefore not
specified in this configuration file. The issues URL is considered here because
it is closely related to the VCS repository aspect.


.. _user-round-trip-vcs-repository-aspect:

VCS repository
--------------

Guide the user from the VCS repository page to the other aspects by offering a
table in the :ref:`README file <readme-rst>`:

.. code-block:: md

   |                  | URL                                            |
   |------------------|------------------------------------------------|
   | **Repository:**  | <vcs-repository>                               |
   | **Read online:** | <documentation>                                |
   | **TER:**         | <typo3-extension-repository>                   |

for example for the *Mask* extension:

.. code-block:: md

   |                  | URL                                            |
   |------------------|------------------------------------------------|
   | **Repository:**  | https://github.com/Gernott/mask                |
   | **Read online:** | https://docs.typo3.org/p/mask/mask/main/en-us/ |
   | **TER:**         | https://extensions.typo3.org/extension/mask    |

and find the README file usually displayed by the VCS host below the file list
of the repository (see `Mask example <https://github.com/Gernott/mask>`__).

For a Composer package, replace the TER URL with the Packagist URL and label it
"Packagist:". For a standalone manual, remove the TER entry.

The Packagist URL is linked indirectly from the TER page and is therefore not
included in this configuration file.


.. _user-round-trip-packagist-aspect:

Packagist
---------

Guide the user from the Packagist page to the other aspects by setting these
:file:`composer.json` configuration values:

.. code-block:: none

    "homepage": "<typo3-extension-repository>",
    "support": {
        "docs": "<documentation>",
        "issues": "<vcs-repository-issues>",
        "source": "<vcs-repository>"
    }

for example for the *Address List* extension:

.. code-block:: none

   "homepage": "https://extensions.typo3.org/extension/tt_address",
   "support": {
      "docs": "https://docs.typo3.org/p/friendsoftypo3/tt-address/main/en-us/",
      "issues": "https://github.com/FriendsOfTYPO3/tt_address/issues",
      "source": "https://github.com/FriendsOfTYPO3/tt_address"
   }

and find the links to the other aspects shown in the right column of the
Packagist page (see `Address List example <https://packagist.org/packages/friendsoftypo3/tt-address>`__).

For a Composer package, replace the TER URL with the Packagist URL.

The issues URL is considered here because it is closely related to the VCS
repository aspect.


.. _user-round-trip-ter-aspect:

TYPO3 Extension Repository
--------------------------

Guide the user from the TER page to the other aspects by setting these
configuration values on the
`extension management page <https://extensions.typo3.org/my-extensions>`__:

*  **Published on Packagist:** check
*  **Composer name of extension:** `<package-name>`
*  **Link to issue tracker:** `<vcs-repository-issues>`
*  **Link to repository:** `<vcs-repository>`

for example for the *Static File Cache* extension:

*  **Published on Packagist:** check
*  **Composer name of extension:** lochmueller/staticfilecache
*  **Link to issue tracker:** \https://github.com/lochmueller/staticfilecache/issues
*  **Link to repository:** \https://github.com/lochmueller/staticfilecache

and find the links to the other aspects presented in the right column of the TER
page (see `Static File Cache example <https://extensions.typo3.org/extension/staticfilecache>`__).

The documentation URL is automatically resolved when the documentation is
published on docs.typo3.org. The issues URL is considered here because it is
closely related to the VCS repository aspect.


.. _user-round-trip-project-types:

Project types
=============


.. _user-round-trip-typo3-extension-type:

TYPO3 extension
---------------

.. uml::

   !include <tupadr3/font-awesome-5/typo3>

   skinparam DefaultTextAlignment center
   skinparam RectangleBackgroundColor transparent
   skinparam RectangleBorderColor transparent
   skinparam UsecaseFontColor<< inactive >> #b9b9b9
   skinparam UsecaseBorderColor<< inactive >> #b9b9b9
   skinparam UsecaseBackgroundColor<< inactive >> #FEFEFE

   rectangle "<color:#f49700><$typo3></color>\n TYPO3 extension" as typo3actor
   usecase "Packagist" as packagist
   usecase "VCS repository" as vcsRepository
   usecase "Documentation" as documentation
   usecase "TYPO3 Extension Repository" as ter

   typo3actor -left-> packagist
   typo3actor -right-> vcsRepository
   typo3actor -up-> documentation
   typo3actor -down-> ter

   packagist <-up-> documentation
   documentation <-down-> vcsRepository
   vcsRepository <-down-> ter
   ter <-up-> packagist

   hide << inactive >> stereotype

Guide the user to all four aspects of the TYPO3 extension, which is usually
hosted on both TER and Packagist, by configuring:

#. :ref:`user-round-trip-documentation-aspect`
#. :ref:`user-round-trip-vcs-repository-aspect`
#. :ref:`user-round-trip-ter-aspect`
#. :ref:`user-round-trip-packagist-aspect`

For example, look at the *Apache Solr* extension and try navigating all four
aspects by simply clicking on a redirect link on each page - starting at the
`Apache Solr TER page <https://extensions.typo3.org/extension/solr>`__.


.. _user-round-trip-composer-package-type:

Composer package
----------------

.. uml::

   !include <tupadr3/font-awesome-5/typo3>

   skinparam DefaultTextAlignment center
   skinparam RectangleBackgroundColor transparent
   skinparam RectangleBorderColor transparent
   skinparam UsecaseFontColor<< inactive >> #b9b9b9
   skinparam UsecaseBorderColor<< inactive >> #b9b9b9
   skinparam UsecaseBackgroundColor<< inactive >> #FEFEFE

   rectangle "<color:#f49700><$typo3></color>\n Composer package" as typo3actor
   usecase "Packagist" as packagist
   usecase "VCS repository" as vcsRepository
   usecase "Documentation" as documentation
   usecase "TYPO3 Extension Repository" << inactive >> as ter

   typo3actor -left-> packagist
   typo3actor -right-> vcsRepository
   typo3actor -up-> documentation
   typo3actor -[hidden]down-> ter

   packagist <-up-> documentation
   documentation <-down-> vcsRepository
   vcsRepository <-[hidden]down-> ter
   ter <-[hidden]up-> packagist

   hide << inactive >> stereotype

A Composer package that is not a TYPO3 extension is usually hosted only on
Packagist. Therefore, guide the user to three aspects of the package by
configuring:

#. :ref:`user-round-trip-documentation-aspect`
#. :ref:`user-round-trip-vcs-repository-aspect`
#. :ref:`user-round-trip-packagist-aspect`

For example, examine the *TYPO3 Console* package and try navigating through its
three aspects by just clicking on a redirecting link on each page - starting at
the `TYPO3 Console Packagist page <https://packagist.org/packages/helhum/typo3-console>`__.


.. _user-round-trip-standalone-manual-type:

Standalone manual
-----------------

.. uml::

   !include <tupadr3/font-awesome-5/typo3>

   skinparam DefaultTextAlignment center
   skinparam RectangleBackgroundColor transparent
   skinparam RectangleBorderColor transparent
   skinparam UsecaseFontColor<< inactive >> #b9b9b9
   skinparam UsecaseBorderColor<< inactive >> #b9b9b9
   skinparam UsecaseBackgroundColor<< inactive >> #FEFEFE

   rectangle "<color:#f49700><$typo3></color>\n Standalone manual" as typo3actor
   usecase "Packagist" << inactive >> as packagist
   usecase "VCS repository" as vcsRepository
   usecase "Documentation" as documentation
   usecase "TYPO3 Extension Repository" << inactive >> as ter

   typo3actor -[hidden]left-> packagist
   typo3actor -right-> vcsRepository
   typo3actor -up-> documentation
   typo3actor -[hidden]down-> ter

   packagist <-[hidden]up-> documentation
   documentation <-down-> vcsRepository
   vcsRepository <-[hidden]down-> ter
   ter <-[hidden]up-> packagist

   hide << inactive >> stereotype

A standalone manual, i.e. a tutorial, guide or reference, is usually not
hosted in a store. Therefore, guide the user to two aspects of the manual by
configuring:

#. :ref:`user-round-trip-documentation-aspect`
#. :ref:`user-round-trip-vcs-repository-aspect`

For example, take a look at the *Getting Started* tutorial and try navigating
between the two aspects by simply clicking on a redirecting link on each page -
starting at the
`Getting Started documentation <https://docs.typo3.org/m/typo3/tutorial-getting-started/main/en-us/>`__.
