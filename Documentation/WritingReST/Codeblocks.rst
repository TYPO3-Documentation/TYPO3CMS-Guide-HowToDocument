.. include:: ../Includes.txt
.. highlight:: rst

.. _writing-rest-codeblocks-with-syntax-highlighting:

===================================
Codeblocks with Syntax Highlighting
===================================



.. _codeblock-quick-reference:

Quick Reference
===============

* To insert a snippet as code with syntax highlighting, use the `code-block`
  directive or the shorthand `::`.
* You can explicitly set the language in the `code-block` or not. 
* If you do not explicitly set the language, the default language (as set with
  the :ref:`codeblocks-highlight-directive`) is used.
* It is recommended to use the short form (`::`). 
* Always use :ref:`syntactically correct code <codeblocks-syntactically-correct>`
  in a code block.

The following examples all do the same thing:

.. rst-class:: bignums

   1. Use the shorthand `::` (recommended)::

         See following example::

            $a='b';
            
      You can use this, if you already set the language PHP with the :ref:`highlight
      directive <codeblocks-highlight-directive>` in the current file (or in Includes.txt).


   2. Set the language (PHP) in the `code-block`::

         See following example:

         .. code-block:: php

            $a = 'b';


   3. Use `code-block` without setting the language::
    

         .. highlight:: php

         See following example:

         .. code-block::

            $a = 'b';
            
      You can use this, if you already set the language PHP with the :ref:`highlight
      directive <codeblocks-highlight-directive>`.      


   
.. _codeblock-shorthand:

Using the '::' Notation (Recommended)
=====================================

It's nice to use this notation and the preferred way to create a code block in
case the highlighting is preset as desired (with the :ref:`codeblocks-highlight-directive`)
and you don't need the special options of the :ref:`codeblock-directive`.

However, the behavior of the '::' notation is "sort of intelligent". So let's
explain it here. *Background:* "Sphinx" is based on "Docutils". Docutils
handles the basic *parse*, *transform* and *create output* process for single
files. Sphinx builds on this and adds the ability to handle multi file
documentation projects. The '::' notation is already part of Docutil's `reST
specification for creating "literal blocks"
<http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#literal-blocks>`__.

Quoting the important part of the specification:

   The paragraph containing only "::" will be completely removed from the
   output; no empty paragraph will remain.

   As a convenience, the "::" is recognized at the end of any paragraph. If
   immediately preceded by whitespace, both colons will be removed from the
   output (this is the "partially minimized" form). When text immediately
   precedes the "::", one colon will be removed from the output, leaving only
   one colon visible (i.e., "::" will be replaced by ":"; this is the "fully
   minimized" form).


Example of Form 1: Expanded
---------------------------

Source::

   Paragraph ...

   ::

      Literal Block

Result:

   Paragraph ...

   ::

      Literal Block

In words: The paragraph will appear as written. The code block just follows.
*Both colons* and one empty line will be removed and not lead to any special
output.


Example of Form 2: Partially Minimized
--------------------------------------

Source::

   Paragraph ... ::

      Literal Block

Result:

   Paragraph ... ::

      Literal Block

In words: The paragraph will appear as written after *both colons* together
with the preceding whitespace (!) have been removed from the end of the line.
The code block then just follows.


Example of Form 3: Fully Minimized
----------------------------------

Source::

   Paragraph::

      Literal Block

Result:

   Paragraph::

      Literal Block

In words: The source of the paragraph has TWO colons at the end which are NOT
preceded by whitespace. In the output just one of the colons will be removed.
The code block then follows normally.


.. _codeblock-directive:

Codeblock Directive
===================

Use codeblock with language PHP::

   .. code-block:: php

      $a = 'b';

Use codeblock without specifying language::

   .. code-block::
   
      $a = 'b';

This uses whatever language has last been set with the :ref:`hightlight-directive` in the current file or in Includes.txt.

.. _writing-rest-codeblocks-syntactically-correct:
.. _codeblocks-syntactically-correct:

Use Syntactically Correct Code
==============================

.. attention::

   **Please: No syntax errors!**

   Syntax highlighting only works if the lexer can parse the code without
   errors. In other words: If there's a syntax error in the code the
   highlighting will not work.


   **Wrong:** ::

      .. code-block:: php

         $a = array(
            'one' => 1,
            ...
         );

   **Correct:** ::

      .. code-block:: php

         $a = array(
            'one' => 1,
            // ...
         );


`Sphinx <http://www.sphinx-doc.org/en/stable/>`__ uses `Pygments
<http://pygments.org/>`__ for highlighting. On a machine that has Pygments
installed the command `pygmentize -L` will list all available lexers.


.. _writing-rest-codeblocks-highlight-directive:
.. _codeblocks-highlight-directive:

Highlight Directive
===================

You can set the default language with the `highlight` directive. All following
codeblocks will use the language as specified in the `highlight` directive for
syntax highlighting.

If all of your codeblocks in one file have the same language, it is easier to just set this
once at the beginning of the file.

This way, you don't need to set the language for each code-block (`..
code-block:: LANG`) explicitly and can use the :ref:`shorthand notation
<codeblock-shorthand>`. 

Use reStructuredText highlighting::

   .. highlight:: rst


Use PHP highlighting::

   .. highlight:: php

For TYPO3 we have adopted the convention that each reStructuredText source file
imports the :file:`Documentation/Includes.txt` file at the top. And in the
included file - in general - we set PHP as default language for highlighting.
Exception: In the TypoScript manuals we are using `typoscript` as default.

You can use the `..highlight:: LANG` directive as often as you want. Each one
remains valid up to the next or up to the end of the *single file* it is used
in.


Highlight Language 'guess'
--------------------------

Note that there is a - pseudo - language 'guess' as well. This should use the
highlighter for the first language that Pygments finds to have no syntax error.


Highlight Language 'none'
-------------------------

The pseudo language 'none' is recognized as well. In this case no highlighting
will occur.


.. _writing-rest-codeblocks-some-more-examples:

Some More Examples
==================

Add Line Numbers to Code Snippet
--------------------------------


Source
~~~~~~

::

   .. code-block:: php
      :linenos:

          $GLOBALS['TYPO3_CONF_VARS']['FE']['addRootLineFields'] .= ',tx_realurl_pathsegment';

          // Adjust to your needs
          $domain = 'www.example.com';
          $rootPageUid = 123;
          $rssFeedPageType = 9818; // pageType of your RSS feed page



Result
~~~~~~

.. code-block:: php
   :linenos:

       <?php

       $GLOBALS['TYPO3_CONF_VARS']['FE']['addRootLineFields'] .= ',tx_realurl_pathsegment';

       // Adjust to your needs
       $domain = 'www.example.com';
       $rootPageUid = 123;
       $rssFeedPageType = 9818; // pageType of your RSS feed page


Turn off Highlighting: Method 1
-------------------------------

Source:
~~~~~~~

.. code-block:: rst

   A description:

   .. code-block:: none

      $ tree vendor/composer
      ├── ClassLoader.php
      ├── LICENSE
      ├── autoload_classmap.php
      ├── ...
      └── installed.json

Result
~~~~~~

A description:

.. code-block:: none

   $ tree vendor/composer
   ├── ClassLoader.php
   ├── LICENSE
   ├── autoload_classmap.php
   ├── ...
   └── installed.json


Turn off Highlighting: Method 2
-------------------------------

Source:
~~~~~~~

.. code-block:: rst

   .. highlight:: none

   A description::

      $ tree vendor/composer
      ├── ClassLoader.php
      ├── LICENSE
      ├── autoload_classmap.php
      ├── ...
      └── installed.json

Result
~~~~~~

.. highlight:: none

A description::

   $ tree vendor/composer
   ├── ClassLoader.php
   ├── LICENSE
   ├── autoload_classmap.php
   ├── ...
   └── installed.json


.. _writing-rest-codeblocks-available-lexers:

Available Lexers
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


Literalinclude
==============

There also is a `literalinclude directive
<http://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-literalinclude>`__.
