
.. include:: ../../Includes.txt
.. highlight:: rst

========================
Codeblocks
========================

((to be written))

On this page:

.. contents::
   :local:
   :backlinks: top


++++++++++++++++++++++++++
Syntax highlighting
++++++++++++++++++++++++++

((to be written))

.. tip::

   See all kinds of highlighting in the
   
   .. rst-class:: horizbuttons-green-xxl
   - `DemoDocs <https://docs.typo3.org/typo3cms/drafts/github/TYPO3-Documentation/t3SphinxThemeRtdDemoDocs/Highlighting/>`__

At the moment syntax highlight takes place only in *codeblocks*.

Pygments
========

::

   Weil "pygments", der Syntax-Highlighter das kennt:
   ```(venv)➜  tct git:(master) ✗ pygmentize -L | grep -i yaml
   * yaml+jinja, salt, sls:
       YAML+Jinja (filenames *.sls)
   * yaml:
       YAML (filenames *.yaml, *.yml)
   ```


Auf der Seite http://pygments.org/ gibt's weitere Informationen, und man kann online ausprobieren,
was es so gibt an Languages. Interessant sind vor allem auch `none` und `guess`. Bei
`guess` probiert er die paar tausend Varianten aus und nimmt die erste, die keinen Lexer-Fehler hat.


The 'highlight' directive
=========================

::

   Du hast auch die Möglichkeit, innerhalb eines *.rst Files den Standard umzustellen:
   ```
   .. nimm ab jetzt Yaml
   .. highlight:: yaml

   Hier ist der Yaml-Code::

      type: form
      identifier: example-form-gridcontainer

   .. nimm ab jetzt PHP
   .. highlight:: php

   In PHP schreibt man::

      <?php
      phpinfo();
      ?>

   ```

Was ich damit zeigen will ist, dass man so auf `.. code-block:: LANG` verzichten kann. Liest sich netter.


Example: Turn off highlighting (1)
----------------------------------

Source:
~~~~~~~

.. code-block:: rst

   Example:

   .. code-block:: none

      $ tree vendor/composer
      ├── ClassLoader.php
      ├── LICENSE
      ├── autoload_classmap.php
      ├── ...
      └── installed.json

Result
~~~~~~

Example:

.. code-block:: none

   $ tree vendor/composer
   ├── ClassLoader.php
   ├── LICENSE
   ├── autoload_classmap.php
   ├── ...
   └── installed.json


Example: Turn off highlighting (2)
----------------------------------

Source:
~~~~~~~

.. code-block:: rst

   .. highlight:: none
   
   Example::

      $ tree vendor/composer
      ├── ClassLoader.php
      ├── LICENSE
      ├── autoload_classmap.php
      ├── ...
      └── installed.json

Result
~~~~~~

.. highlight:: none

Example::

   $ tree vendor/composer
   ├── ClassLoader.php
   ├── LICENSE
   ├── autoload_classmap.php
   ├── ...
   └── installed.json
