
.. include:: ../../Includes.txt
.. highlight:: rst

========================
Codeblocks
========================

((to be written))


Highlighting in codeblocks
==========================

((to be written))

Pygments
--------

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


Know the 'highlight' directive
------------------------------

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

.. highlight:: none

Example::

   $ tree vendor/composer
   ├── ClassLoader.php
   ├── LICENSE
   ├── autoload_classmap.php
   ├── ...
   └── installed.json

