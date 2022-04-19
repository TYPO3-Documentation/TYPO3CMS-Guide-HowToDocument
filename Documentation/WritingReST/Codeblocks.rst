.. include:: /Includes.rst.txt
.. highlight:: rst
.. index::
   reST; Code blocks
   reST; syntax highlighting
.. _writing-rest-codeblocks-with-syntax-highlighting:

====================================
Code blocks with syntax highlighting
====================================


.. _codeblock-quick-reference:

Quick Reference
===============

A simple code block consists of the directive `code-block` and the actual code indented
by 3 spaces, the standard indentation for ReStructured Text. The TYPO3 source uses 4
spaces instead for consistency with other code.

A code block can have one or more options. To make orientation in code examples easier
try to always add a `:caption:` with the path and name of the file where the example should go:

.. tabs::

   .. group-tab:: Source (rst)

      .. code-block:: rst
         :caption: Documentation/MyDocs.rst

         .. code-block:: php
            :caption: EXT:site_package/Configuration/TCA/Overrides/sys_template.php

            /**
             * Add default TypoScript (constants and setup)
             */
            \TYPO3\CMS\Core\Utility\ExtensionManagementUtility::addStaticFile(
                'site_package',
                'Configuration/TypoScript',
                'Site Package'
            );

   .. group-tab:: Output

      .. code-block:: php
         :caption: EXT:site_package/Configuration/TCA/Overrides/sys_template.php

         /**
          * Add default TypoScript (constants and setup)
          */
         \TYPO3\CMS\Core\Utility\ExtensionManagementUtility::addStaticFile(
             'site_package',
             'Configuration/TypoScript',
             'Site Package'
         );

Always use :ref:`syntactically correct code <codeblocks-syntactically-correct>`
in a code block.

Use :ref:`placeholders <codeblocks-placeholders>` in angle brackets
(`<placeholder-name>`) to refer to a place in the code where you don't care
about the exact value.


.. index:: reST directives; code-block
.. _codeblock-directive:

Code block directive
====================

A code block has the following syntax:

.. code-block:: rst
   :caption: Documentation/MyDocs.rst

   .. code-block:: <language>
      :caption: <caption>
      <options>

      <code>

There must be a newline between the options and the code. There must not be a
newline between the directive line and options or within options. Otherwise the rendering
will fail.

<language>
   The language of the code-block. We commonly use the following: :rst:`php`,
   :rst:`typoscript` (also for tsconfig), :rst:`yaml`, :rst:`javascript`,
   :rst:`html` (also for Fluid), :rst:`shell`, :rst:`xml`, :rst:`none`.

   See all
   :ref:`available lexers <writing-rest-codeblocks-available-lexers>`

<caption>
   To make orientation in code examples easier try to always add
   a caption with the name of the file where the example should go. If the code
   should be entered in the backend explain where it should go there.

<options>
   The following options may be used, all options but :rst:`caption` are
   optional:

   .. code-block:: rst

      .. code-block:: <language>
         :caption: <caption>
         :linenos:
         :lineno-start: <start-number>
         :emphasize-lines: <emphasized-line-numbers>
         :name: <reference-label>

   :rst:`linenos`
      Show line numbers.

   :rst:`lineno-start`
      Start line numbers with <start-number>.

   :rst:`emphasize-lines`
      <emphasized-line-numbers> contains a comma separated list of line numbers
      to be emphasized.

   :rst:`name`
      Set a <reference-label>. This label can be used to link from any given
      text to the specific code-block. The name needs to be unique within one
      manual.

   See also the official
   `sphinx documentation on code-blocks <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-code-block>`__.

Examples
========

A simple code-block with syntax highlighting
--------------------------------------------


.. tabs::

   .. group-tab:: Source (rst)

      .. code-block:: rst
         :caption: Documentation/MyDocs.rst

         .. code-block:: php
            :caption: EXT:site_package/Configuration/TCA/Overrides/sys_template.php

            /**
             * Add default TypoScript (constants and setup)
             */
            \TYPO3\CMS\Core\Utility\ExtensionManagementUtility::addStaticFile(
                'site_package',
                'Configuration/TypoScript',
                'Site Package'
            );

   .. group-tab:: Output

      .. code-block:: php
         :caption: EXT:site_package/Configuration/TCA/Overrides/sys_template.php

         /**
          * Add default TypoScript (constants and setup)
          */
         \TYPO3\CMS\Core\Utility\ExtensionManagementUtility::addStaticFile(
             'site_package',
             'Configuration/TypoScript',
             'Site Package'
         );

Code-block with line numbers and highlighting of one line
---------------------------------------------------------


.. tabs::

   .. group-tab:: Source (rst)

      .. code-block:: rst
         :caption: Documentation/MyDocs.rst

         .. code-block:: php
            :caption: EXT:site_package/Configuration/TCA/Overrides/sys_template.php
            :linenos:
            :emphasize-lines: 4, 7

            /**
             * Add default TypoScript (constants and setup)
             */
            \TYPO3\CMS\Core\Utility\ExtensionManagementUtility::addStaticFile(
                'site_package',
                'Configuration/TypoScript',
                'Site Package'
            );

   .. group-tab:: Output

      .. code-block:: php
         :caption: EXT:site_package/Configuration/TCA/Overrides/sys_template.php
         :linenos:
         :emphasize-lines: 4, 7

         /**
          * Add default TypoScript (constants and setup)
          */
         \TYPO3\CMS\Core\Utility\ExtensionManagementUtility::addStaticFile(
             'site_package',
             'Configuration/TypoScript',
             'Site Package'
         );

Use code-blocks containing diffs
--------------------------------

To emphasize changes that should be made:

.. tabs::

   .. group-tab:: Source (rst)

      .. code-block:: rst
         :caption: Documentation/MyDocs.rst

         .. code-block:: diff
            :caption: ext_localconf.php.diff

             <?php

            -defined('TYPO3_MODE') or die();
            +defined('TYPO3') or die();

   .. group-tab:: Output

      .. code-block:: diff
         :caption: ext_localconf.php.diff

          <?php

         -defined('TYPO3_MODE') or die();
         +defined('TYPO3') or die();

.. hint::
   You can use diff tools such as the
   `bartlweb diff file generator <https://tools.bartlweb.net/diff/>`__. Make
   sure to use the type :code:`unified context`

Show a directory tree
---------------------

.. tabs::

   .. group-tab:: Source (rst)

      .. code-block:: rst
         :caption: Documentation/MyDocs.rst

         .. code-block:: none
            :caption: Page tree of directory :file:`vendor/composer`

            $ tree vendor/composer
            ├── ClassLoader.php
            ├── LICENSE
            ├── autoload_classmap.php
            ├── ...
            └── installed.json


   .. group-tab:: Output

      .. code-block:: none
         :caption: Page tree of directory :file:`vendor/composer`

         $ tree vendor/composer
         ├── ClassLoader.php
         ├── LICENSE
         ├── autoload_classmap.php
         ├── ...
         └── installed.json

.. _writing-rest-codeblocks-syntactically-correct:
.. _codeblocks-syntactically-correct:

Use syntactically correct code
==============================

.. attention::

   **Please: No syntax errors!**

   Syntax highlighting only works if the lexer can parse the code without
   errors. In other words: If there's a syntax error in the code the
   highlighting will not work.

   .. tabs::

      .. group-tab:: Correct


         .. code-block:: rst
            :caption: Documentation/MyDocs.rst

            .. code-block:: php

               $a = array(
                  'one' => 1,
                  // ...
               );


      .. group-tab:: Wrong

         .. code-block:: rst
            :caption: Documentation/MyDocs.rst

            .. code-block:: php

               $a = array(
                  'one' => 1,
                  ...
               );

.. index:: reST directives; highlight
.. _writing-rest-codeblocks-highlight-directive:
.. _codeblocks-highlight-directive:

Highlight directive
===================

You can set the default language with the `highlight` directive. All following
code blocks will use the language as specified in the `highlight` directive for
syntax highlighting.

This language works as fall back for the outdated code-blocks that do not
specify the desired language.

For TYPO3 we have adopted the convention that each reStructuredText source file
imports the :file:`Documentation/Includes.rst.txt` file at the top. And in the
included file - in general - we set PHP as default language for highlighting.
Exception: In the TypoScript manuals we are using `typoscript` as default.

.. index:: reST; Lexers
.. _writing-rest-codeblocks-available-lexers:

Available lexers
================

You can use any of the following names of lexers:


`| bash, sh, ksh, shell |` for example all mean the same lexer:

abap \|
abnf \|
ada, ada95, ada2005 \|
adl \|
agda \|
ahk, autohotkey \|
alloy \|
ampl \|
antlr-as, antlr-actionscript \|
antlr-cpp \|
antlr-csharp, antlr-c# \|
antlr-java \|
antlr-objc \|
antlr-perl \|
antlr-python \|
antlr-ruby, antlr-rb \|
antlr \|
apacheconf, aconf, apache \|
apl \|
applescript \|
arduino \|
as, actionscript \|
as3, actionscript3 \|
aspectj \|
aspx-cs \|
aspx-vb \|
asy, asymptote \|
at, ambienttalk, ambienttalk/2 \|
autoit \|
awk, gawk, mawk, nawk \|
basemake \|
bash, sh, ksh, shell \|
bat, batch, dosbatch, winbatch \|
bbcode \|
bc \|
befunge \|
blitzbasic, b3d, bplus \|
blitzmax, bmax \|
bnf \|
boo \|
boogie \|
brainfuck, bf \|
bro \|
bugs, winbugs, openbugs \|
c-objdump \|
c \|
ca65 \|
cadl \|
camkes, idl4 \|
cbmbas \|
ceylon \|
cfc \|
cfengine3, cf3 \|
cfm \|
cfs \|
chai, chaiscript \|
chapel, chpl \|
cheetah, spitfire \|
cirru \|
clay \|
clean \|
clojure, clj \|
clojurescript, cljs \|
cmake \|
cobol \|
cobolfree \|
coffee-script, coffeescript, coffee \|
common-lisp, cl, lisp \|
componentpascal, cp \|
console, shell-session \|
control, debcontrol \|
coq \|
cpp, c++ \|
cpp-objdump, c++-objdumb, cxx-objdump \|
cpsa \|
crmsh, pcmk \|
croc \|
cryptol, cry \|
csharp, c# \|
csound, csound-orc \|
csound-document, csound-csd \|
csound-score, csound-sco \|
css+django, css+jinja \|
css+erb, css+ruby \|
css+genshitext, css+genshi \|
css+lasso \|
css+mako \|
css+mako \|
css+mozpreproc \|
css+myghty \|
css+php \|
css+smarty \|
css \|
cucumber, gherkin \|
cuda, cu \|
cypher \|
cython, pyx, pyrex \|
d-objdump \|
d \|
dart \|
delphi, pas, pascal, objectpascal \|
dg \|
diff, udiff \|
django, jinja \|
docker, dockerfile \|
doscon \|
dpatch \|
dtd \|
duel, jbst, jsonml+bst \|
dylan-console, dylan-repl \|
dylan-lid, lid \|
dylan \|
earl-grey, earlgrey, eg \|
easytrieve \|
ebnf \|
ec \|
ecl \|
eiffel \|
elixir, ex, exs \|
elm \|
emacs, elisp, emacs-lisp \|
erb \|
erl \|
erlang \|
evoque \|
extempore \|
ezhil \|
factor \|
fan \|
fancy, fy \|
felix, flx \|
fish, fishshell \|
flatline \|
fortran \|
fortranfixed \|
foxpro, vfp, clipper, xbase \|
fsharp \|
gap \|
gas, asm \|
genshi, kid, xml+genshi, xml+kid \|
genshitext \|
glsl \|
gnuplot \|
go \|
golo \|
gooddata-cl \|
gosu \|
groff, nroff, man \|
groovy \|
gst \|
haml \|
handlebars \|
haskell, hs \|
haxeml, hxml \|
hexdump \|
hsail, hsa \|
html+cheetah, html+spitfire, htmlcheetah \|
html+django, html+jinja, htmldjango \|
html+evoque \|
html+genshi, html+kid \|
html+handlebars \|
html+lasso \|
html+mako \|
html+mako \|
html+myghty \|
html+php \|
html+smarty \|
html+twig \|
html+velocity \|
html \|
http \|
hx, haxe, hxsl \|
hybris, hy \|
hylang \|
i6t \|
idl \|
idris, idr \|
iex \|
igor, igorpro \|
inform6, i6 \|
inform7, i7 \|
ini, cfg, dosini \|
io \|
ioke, ik \|
irc \|
isabelle \|
j \|
jade \|
jags \|
jasmin, jasminxt \|
java \|
javascript+mozpreproc \|
jcl \|
jlcon \|
js+cheetah, javascript+cheetah, js+spitfire, javascript+spitfire \|
js+django, javascript+django, js+jinja, javascript+jinja \|
js+erb, javascript+erb, js+ruby, javascript+ruby \|
js+genshitext, js+genshi, javascript+genshitext, javascript+genshi \|
js+lasso, javascript+lasso \|
js+mako, javascript+mako \|
js+mako, javascript+mako \|
js+myghty, javascript+myghty \|
js+php, javascript+php \|
js+smarty, javascript+smarty \|
js, javascript \|
jsgf \|
json \|
jsonld, json-ld \|
jsp \|
julia, jl \|
kal \|
kconfig, menuconfig, linux-config, kernel-config \|
koka \|
kotlin \|
lagda, literate-agda \|
lasso, lassoscript \|
lcry, literate-cryptol, lcryptol \|
lean \|
less \|
lhs, literate-haskell, lhaskell \|
lidr, literate-idris, lidris \|
lighty, lighttpd \|
limbo \|
liquid \|
live-script, livescript \|
llvm \|
logos \|
logtalk \|
lsl \|
lua \|
make, makefile, mf, bsdmake \|
mako \|
mako \|
maql \|
mask \|
mason \|
mathematica, mma, nb \|
matlab \|
matlabsession \|
minid \|
modelica \|
modula2, m2 \|
monkey \|
moocode, moo \|
moon, moonscript \|
mozhashpreproc \|
mozpercentpreproc \|
mql, mq4, mq5, mql4, mql5 \|
mscgen, msc \|
mupad \|
mxml \|
myghty \|
mysql \|
nasm \|
ncl \|
nemerle \|
nesc \|
newlisp \|
newspeak \|
nginx \|
nimrod, nim \|
nit \|
nixos, nix \|
nsis, nsi, nsh \|
numpy \|
objdump-nasm \|
objdump \|
objective-c++, objectivec++, obj-c++, objc++ \|
objective-c, objectivec, obj-c, objc \|
objective-j, objectivej, obj-j, objj \|
ocaml \|
octave \|
odin \|
ooc \|
opa \|
openedge, abl, progress \|
pacmanconf \|
pan \|
parasail \|
pawn \|
perl, pl \|
perl6, pl6 \|
php, php3, php4, php5 \|
pig \|
pike \|
pkgconfig \|
plpgsql \|
postgresql, postgres \|
postscript, postscr \|
pot, po \|
pov \|
powershell, posh, ps1, psm1 \|
praat \|
prolog \|
properties, jproperties \|
protobuf, proto \|
ps1con \|
psql, postgresql-console, postgres-console \|
puppet \|
py3tb \|
pycon \|
pypylog, pypy \|
pytb \|
python, py, sage \|
python3, py3 \|
qbasic, basic \|
qml, qbs \|
qvto, qvt \|
racket, rkt \|
ragel-c \|
ragel-cpp \|
ragel-d \|
ragel-em \|
ragel-java \|
ragel-objc \|
ragel-ruby, ragel-rb \|
ragel \|
raw \|
rb, ruby, duby \|
rbcon, irb \|
rconsole, rout \|
rd \|
rebol \|
red, red/system \|
redcode \|
registry \|
resource, resourcebundle \|
rexx, arexx \|
rhtml, html+erb, html+ruby \|
roboconf-graph \|
roboconf-instances \|
robotframework \|
rql \|
rsl \|
rst, rest, restructuredtext \|
rts, trafficscript \|
rust \|
sass \|
sc, supercollider \|
scala \|
scaml \|
scheme, scm \|
scilab \|
scss \|
shen \|
silver \|
slim \|
smali \|
smalltalk, squeak, st \|
smarty \|
sml \|
snobol \|
sourceslist, sources.list, debsources \|
sp \|
sparql \|
spec \|
splus, s, r \|
sql \|
sqlite3 \|
squidconf, squid.conf, squid \|
ssp \|
stan \|
swift \|
swig \|
systemverilog, sv \|
tads3 \|
tap \|
tcl \|
tcsh, csh \|
tcshcon \|
tea \|
termcap \|
terminfo \|
terraform, tf \|
tex, latex \|
text \|
thrift \|
todotxt \|
trac-wiki, moin \|
treetop \|
ts, typescript \|
turtle \|
twig \|
typoscript \|
typoscriptcssdata \|
typoscripthtmldata \|
urbiscript \|
vala, vapi \|
vb.net, vbnet \|
vcl \|
vclsnippets, vclsnippet \|
vctreestatus \|
velocity \|
verilog, v \|
vgl \|
vhdl \|
vim \|
wdiff \|
x10, xten \|
xml+cheetah, xml+spitfire \|
xml+django, xml+jinja \|
xml+erb, xml+ruby \|
xml+evoque \|
xml+lasso \|
xml+mako \|
xml+mako \|
xml+myghty \|
xml+php \|
xml+smarty \|
xml+velocity \|
xml \|
xquery, xqy, xq, xql, xqm \|
xslt \|
xtend \|
xul+mozpreproc \|
yaml+jinja, salt, sls \|
yaml \|
zephir \|

**Tip:** Try the Pygments Demo at http://pygments.org/


`Sphinx <http://www.sphinx-doc.org/en/stable/>`__ uses `Pygments
<http://pygments.org/>`__ for highlighting. On a machine that has Pygments
installed the command `pygmentize -L` will list all available lexers.

Literalinclude
==============

A draw back of code-blocks is that most editors cannot properly highlight or
indent code within code-blocks. The directive :rst:`literalinclude` enables you
to store longer code blocks in an external file with the proper ending.

The :rst:`literalinclude` directive imports the file and displays its content as
code-block.


.. tabs::

   .. group-tab:: Source (rst)

      .. code-block:: rst
         :caption: Documentation/SiteConfiguration/Index.rst

         .. literalinclude:: /CodeSnippets/LiteralIncludes/example.yaml
            :language: yaml
            :emphasize-lines: 5,10-13
            :linenos:

   .. group-tab:: Output

      .. literalinclude:: /CodeSnippets/LiteralIncludes/example.yaml
         :language: yaml
         :emphasize-lines: 5,10-13
         :linenos:

Literal includes can even be used to render the difference between files,
without having to create a diff file first:

.. tabs::

   .. group-tab:: Source (rst)

      .. code-block:: rst
         :caption: Documentation/SiteConfiguration/Index.rst

         .. literalinclude:: /CodeSnippets/LiteralIncludes/example.yaml
            :diff: /CodeSnippets/LiteralIncludes/example_de.yaml

   .. group-tab:: Output

      .. literalinclude:: /CodeSnippets/LiteralIncludes/example.yaml
         :diff: /CodeSnippets/LiteralIncludes/example_de.yaml


See also `literalinclude directive
<http://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-literalinclude>`__.


.. _codeblocks-placeholders:

Placeholders
============

Placeholders in this context are named tags in code and
:ref:`example URLs <preventing-links>` where the exact value does not matter,
but is referenced in the surrounding documentation.
Use the *Backus-Naur form* `<placeholder-name>` for placeholders in code and
URLs, i.e. use angle brackets to encapsulate the placeholder name.

For example in PHP

.. code-block:: rst

   Set up a controller class to handle user interaction with the entity data
   model:

   .. code-block:: php

      class <Entity>Controller extends ActionController
      {
         ..
      }

   where `<Entity>` corresponds to the entity data model class name.

or on the command line

.. code-block:: rst

   Importing a TYPO3 dump file is as simple as running:

   .. code-block:: bash

      typo3/sysext/core/bin/typo3 impexp:import <file>

   where `<file>` can be the absolute path on the server or the relative path
   in the TYPO3 project folder.

or in an example URL

.. code-block:: rst

   The TYPO3 backend normally appends the session token ID to the URL as
   follows: :samp:`https://example.org/typo3/main?token=<token-id>`.

In the XML and HTML markup languages, which make extensive use of angle
brackets, the comment tag :html:`<!-- placeholder-name -->` is used to insert
placeholders. A `<placeholder-name>` looks like a regular element and would lead to confusion.


Outdated code-block formats
===========================

For historic reasons the :rst:`:caption:` option is missing in many code-blocks.
We try to add them wherever we touch the rst files. Do not add new code-blocks
without a caption stating the file name. It is often very confusing for new
developer where a certain code-snippet should go. The recommended file name
answers many questions.

We recommend to always write the language name after the code-block directive.
This makes it easier for first time contributors to adjust or copy-paste code
blocks. For historic reasons there are code-blocks without an explicit language:

If you do not explicitly set the language, the default language (as set with
the :ref:`codeblocks-highlight-directive`) is used. If no highlight directive
was used, the default set in :file:`Documentation/Includes.rst.txt` is used.

In the past a simplified shorthand directive was widely used: A sentence ending
with two double colon :rst:`::`, followed by a new line and an indented
block of code. This quick syntax has several draw-backs:

*  It is confusing to developers who seldom contribute
*  We cannot give a caption and state the file name where the code should go.
*  The script language is only stated implicitly.
*  Such codeblocks cannot be easily copy-pasted to use them as models for your
   own code-blocks.

Change such code-blocks as follows:

.. code-block:: diff
   :caption: UpdateShorthandCode.diff

    The extension already contains some unit tests that extend `typo3/testing-framework`'s base
   -unit test class in directory :file:`Tests/Unit/Hooks` (stripped)::
   +unit test class:
   +
   +.. code-block:: php
   +   :caption: <extension_key>/Tests/Unit/Hooks/DataHandlerFlushByTagHookTest.php

        <?php
        namespace Lolli\Enetcache\Tests\Unit\Hooks;
