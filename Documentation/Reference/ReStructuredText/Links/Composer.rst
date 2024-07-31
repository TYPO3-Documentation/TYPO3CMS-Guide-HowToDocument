:navigation-title: Composer / Extensions
..  include:: /Includes.rst.txt

..  _linking-extensions:

==============================================
Linking Composer packages and TYPO3 extensions
==============================================

You can use the text role :rst:`:composer:` to create an infobox with information
and links to Packagist. This way you can link to any TYPO3 extension
that is also listed on Packagist like :composer:`georgringer/news` and
:composer:`b13/container`, any TYPO3 system extension like
:composer:`typo3/cms-adminpanel` and any other Composer package like
:composer:`typo3/testing-framework`:

..  code-block:: rst

    This way you can link to any TYPO3 extension
    that is also listed on packagist like :composer:`georgringer/news` and
    :composer:`b13/container`, any TYPO3 system extension like
    :composer:`typo3/cms-adminpanel` and any other Composer package like
    :composer:`typo3/testing-framework`

If you want to link to the TYPO3 Extension Repository (TER) you can use the
text role :rst:`t3ext` instead and link extensions like :t3ext:`news` or
system extensions like :t3ext:`adminpanel`:

..  code-block:: rst

    You can use the text role `t3ext` instead and link extensions like
    :t3ext:`news` or system extensions like :t3ext:`adminpanel`
