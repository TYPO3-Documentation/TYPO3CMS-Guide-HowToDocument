:navigation-title: Navigation title

..  _navigation-title:

=================================================
Navigation title: A page title displayed in menus
=================================================

It is possible to define a different, usually shorter, title for a page to be
displayed in menus.

While the title of a page is a very important tool to pass information to
both the readers and search engines including our internal elastic search,
elaborate titles usually take up to much space within the menu, the breadcrumb
etc.

For example, the title of the page you are currently reading is quite long:
`Navigation title: A page title displayed in menus`. This title is also used
as automatic title in references, unless otherwise specified:
:ref:`navigation-title`.

However in the main menu and in the breadcrumb the shorter navigation title
is displayed.

A navigation title can be defined as follows:

..  code-block:: rst
    :capition: SomePage.rst

    :navigation-title: Navigation title

    ..  include:: /Includes.rst.txt
    ..  _navigation-title:

    =================================================
    Navigation title: A page title displayed in menus
    =================================================

    [...]

    For example, the title of the page you are currently reading is quite long:
    `Navigation title: A page title displayed in menus`. This title is also used
    as automatic title in references, unless otherwise specified:
    :ref:`navigation-title`.
