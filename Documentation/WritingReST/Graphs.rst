.. include:: /Includes.rst.txt
.. highlight:: rst
.. index::
   ! Graphs
   Graphs; Graphviz
.. _graphviz-graphs:

===============
Graphviz graphs
===============

In order to render graphs in the TYPO3 documentation,
`Graphviz <https://graphviz.org/>`_ is integrated into the rendering process.

.. contents::
   :backlinks: top
   :class: compact-list
   :depth: 2
   :local:

.. _graphviz-graphs-graph-types:

Graph types
===========

There are two types of graphs to choose from: The directed and the undirected
graph, which are declared by the keywords `digraph` and `graph` respectively.

.. index:: Graphs types; Undirected graph
.. _graphviz-graphs-undirected-graph:

Undirected graph
----------------

.. graphviz::
   :caption: The MVC pattern divides the application into three global layers.

   graph {
      user [
         shape=plaintext;
         width=4;
         label="User";
         style="";
         # Image is currently not supported due to a bug in Sphinx
         # see https://github.com/sphinx-doc/sphinx/issues/8232#issuecomment-992711887
         # image="typo3-logo.svg";
      ]
      view [
         shape=box;
         width=4;
         label=<<B>View</B><BR/>Displaying the data>;
      ]
      controller [
         shape=box;
         width=4;
         label=<<B>Controller</B><BR/>Control of functionality>;
      ]
      model [
         shape=box;
         width=4;
         label=<<B>Model</B><BR/>Domain model and domain logic>;
      ]
      user -- view -- controller -- model;
   }

.. code-block:: rest

   .. graphviz::
      :caption: The MVC pattern divides the application into three global layers.

      graph {
         user [
            shape=plaintext;
            width=4;
            label="User";
            style="";
            # Image is currently not supported due to a bug in Sphinx
            # see https://github.com/sphinx-doc/sphinx/issues/8232#issuecomment-992711887
            # image="typo3-logo.svg";
         ]
         view [
            shape=box;
            width=4;
            label=<<B>View</B><BR/>Displaying the data>;
         ]
         controller [
            shape=box;
            width=4;
            label=<<B>Controller</B><BR/>Control of functionality>;
         ]
         model [
            shape=box;
            width=4;
            label=<<B>Model</B><BR/>Domain model and domain logic>;
         ]
         user -- view -- controller -- model;
      }

Examples: https://graphviz.org/Gallery/undirected/

.. index:: Graphs types; Directed graph
.. _graphviz-graphs-directed-graph:

Directed graph
--------------

.. graphviz::
   :caption: In this request, a list of blog posts is displayed.

   digraph {
      graph [rankdir=BT;splines=ortho];
      node [shape=box;width=1];

      user [label="User";shape=plaintext;style="";margin="0.36,0.055"];

      subgraph cluster_view {
         label="View";
         style="filled,dashed";
         v1 [label="V1"];
         v2 [label="V2";color=grey70;fillcolor=grey90;fontcolor=grey70];
      }

      subgraph cluster_controller {
         label="Controller";
         style="filled,dashed";
         rankdir=LR;

         subgraph cluster_post_controller {
            label="PostController";
            style=filled;
            list [];
            show [color=grey70;fillcolor=grey90;fontcolor=grey70];
         }

         subgraph cluster_comment_controller {
            label="CommentController";
            style=filled;
            color=grey70;
            fillcolor=grey90;
            fontcolor=grey70;
            new [color=grey70;fillcolor=grey90;fontcolor=grey70];
         }
      }

      subgraph cluster_model {
         label="Model";
         rankdir=LR;
         style="filled,dashed";
         blog_entity [label="";shape=ellipse];
         post_entity [label="";shape=ellipse];
      }

      blog_entity -> list [label="③ Array of blog posts"];
      list -> v1 [label="④ Array of blog posts for display"];
      v1 -> user [label="⑤ Response"];
      user -> list [label="① Request";constraint=false];
      list -> blog_entity [label="② Retrieve all blog posts";constraint=false];
   }

.. code-block:: rest

   .. graphviz::
      :caption: In this request, a list of blog posts is displayed.

      digraph {
         graph [rankdir=BT;splines=ortho];
         node [shape=box;width=1];

         user [label="User";shape=plaintext;style="";margin="0.36,0.055"];

         subgraph cluster_view {
            label="View";
            style="filled,dashed";
            v1 [label="V1"];
            v2 [label="";style="";shape=plaintext];
         }

         subgraph cluster_controller {
            label="Controller";
            style="filled,dashed";
            rankdir=LR;

            subgraph cluster_post_controller {
               label="PostController";
               style=filled;
               list [];
               show [color=grey70;fillcolor=grey90;fontcolor=grey70];
            }

            subgraph cluster_comment_controller {
               label="CommentController";
               style=filled;
               color=grey70;
               fillcolor=grey90;
               fontcolor=grey70;
               new [color=grey70;fillcolor=grey90;fontcolor=grey70];
            }
         }

         subgraph cluster_model {
            label="Model";
            rankdir=LR;
            style="filled,dashed";
            blog_entity [label="";shape=ellipse];
            post_entity [label="";shape=ellipse];
         }

         blog_entity -> list [label="③ Array of blog posts"];
         list -> v1 [label="④ Array of blog posts for display"];
         v1 -> user [label="⑤ Response"];
         user -> list [label="① Request";constraint=false];
         list -> blog_entity [label="② Retrieve all blog posts";constraint=false];
      }

Examples: https://graphviz.org/Gallery/directed/

.. _graphviz-graphs-layout-engines:

Layout engines
==============

The graphs can be rendered using different engines, where the default is
*Dot*, which is the most popular for directed graphs.
The engine is defined by the attribute `layout` with the available values

-  :ref:`dot <graphviz-graphs-dot-layout-engine>` (default)
-  :ref:`neato <graphviz-graphs-neato-layout-engine>`
-  :ref:`twopi <graphviz-graphs-twopi-layout-engine>`
-  :ref:`circo <graphviz-graphs-circo-layout-engine>`
-  :ref:`fdp <graphviz-graphs-fdp-layout-engine>`
-  :ref:`osage <graphviz-graphs-osage-layout-engine>`
-  :ref:`patchwork <graphviz-graphs-patchwork-layout-engine>` and
-  :ref:`sfdp <graphviz-graphs-sfdp-layout-engine>`.

Below you will find some examples of graphs rendered by the available engines.

.. index:: Graphs engines; Dot layout engine
.. _graphviz-graphs-dot-layout-engine:

Dot layout engine
-----------------

.. graphviz::

   digraph G {
      subgraph cluster_0 {
         style=filled;
         color=lightgrey;
         fillcolor=lightgrey;
         node [color=white;fillcolor=white];
         a0 -> a1 -> a2 -> a3;
         label = "process #1";
      }

      subgraph cluster_1 {
         b0 -> b1 -> b2 -> b3;
         label="process #2";
         color=blue;
      }

      start -> a0;
      start -> b0;
      a1 -> b3;
      b2 -> a3;
      a3 -> a0;
      a3 -> end;
      b3 -> end;

      start [shape=Mdiamond];
      end [shape=Msquare];
   }

.. code-block:: rest

   .. graphviz::

      digraph G {
         subgraph cluster_0 {
            style=filled;
            color=lightgrey;
            fillcolor=lightgrey;
            node [color=white;fillcolor=white];
            a0 -> a1 -> a2 -> a3;
            label = "process #1";
         }

         subgraph cluster_1 {
            b0 -> b1 -> b2 -> b3;
            label="process #2";
            color=blue;
         }

         start -> a0;
         start -> b0;
         a1 -> b3;
         b2 -> a3;
         a3 -> a0;
         a3 -> end;
         b3 -> end;

         start [shape=Mdiamond];
         end [shape=Msquare];
      }

Documentation: https://graphviz.org/docs/layouts/dot/

.. index:: Graphs engines; Neato layout engine
.. _graphviz-graphs-neato-layout-engine:

Neato layout engine
-------------------

.. graphviz::

   graph ER {
      layout=neato;

      node [shape=box]; course; institute; student;
      node [shape=ellipse]; {node [label="name"] name0; name1; name2;}
         code; grade; number;
      node [shape=diamond,color=lightgrey,fillcolor=lightgrey]; "C-I"; "S-C"; "S-I";

      name0 -- course;
      code -- course;
      course -- "C-I" [label="n",len=1.00];
      "C-I" -- institute [label="1",len=1.00];
      institute -- name1;
      institute -- "S-I" [label="1",len=1.00];
      "S-I" -- student [label="n",len=1.00];
      student -- grade;
      student -- name2;
      student -- number;
      student -- "S-C" [label="m",len=1.00];
      "S-C" -- course [label="n",len=1.00];

      label="\n\nEntity Relation Diagram\ndrawn by NEATO";
      fontsize=20;
   }

.. code-block:: rest

   .. graphviz::

      graph ER {
         layout=neato;

         node [shape=box]; course; institute; student;
         node [shape=ellipse]; {node [label="name"] name0; name1; name2;}
            code; grade; number;
         node [shape=diamond,color=lightgrey,fillcolor=lightgrey]; "C-I"; "S-C"; "S-I";

         name0 -- course;
         code -- course;
         course -- "C-I" [label="n",len=1.00];
         "C-I" -- institute [label="1",len=1.00];
         institute -- name1;
         institute -- "S-I" [label="1",len=1.00];
         "S-I" -- student [label="n",len=1.00];
         student -- grade;
         student -- name2;
         student -- number;
         student -- "S-C" [label="m",len=1.00];
         "S-C" -- course [label="n",len=1.00];

         label="\n\nEntity Relation Diagram\ndrawn by NEATO";
         fontsize=20;
      }

Documentation: https://graphviz.org/docs/layouts/neato/

.. index:: Graphs engines; Twopi layout engine
.. _graphviz-graphs-twopi-layout-engine:

Twopi layout engine
-------------------

The given examples of the Graphviz gallery are too large for inclusion here.
In case you can contribute one, feel encouraged to get in contact with us.
Navigate to the below URLs to get further insights.

*  Documentation: https://graphviz.org/docs/layouts/twopi/
*  Example: https://graphviz.org/Gallery/undirected/networkmap_twopi.html

.. index:: Graphs engines; Circo layout engine
.. _graphviz-graphs-circo-layout-engine:

Circo layout engine
-------------------

No examples provided at the Graphviz gallery for this layout engine.
In case you can contribute one, feel encouraged to get in contact with us.
Navigate to the below URL to get further insights.

Documentation: https://graphviz.org/docs/layouts/circo/

.. index:: Graphs engines; Fdp layout engine
.. _graphviz-graphs-fdp-layout-engine:

Fdp layout engine
-----------------

.. graphviz::

   graph G {
      layout=fdp;

      e;

      subgraph clusterA {
         a -- b;
         subgraph clusterC {
            C -- D;
         }
      }

      subgraph clusterB {
         d -- f;
      }

      d -- D;
      e -- clusterB;
      clusterC -- clusterB;
   }

.. code-block:: rest

   .. graphviz::

      graph G {
         layout=fdp;

         e;

         subgraph clusterA {
            a -- b;
            subgraph clusterC {
               C -- D;
            }
         }

         subgraph clusterB {
            d -- f;
         }

         d -- D;
         e -- clusterB;
         clusterC -- clusterB;
      }

.. index:: Graphs engines; Osage layout engine
.. _graphviz-graphs-osage-layout-engine:

Osage layout engine
-------------------

No examples provided at the Graphviz gallery for this layout engine.
In case you can contribute one, feel encouraged to get in contact with us.
Navigate to the below URL to get further insights.

Documentation: https://graphviz.org/docs/layouts/osage/

.. index:: Graphs engines; Patchwork layout engine
.. _graphviz-graphs-patchwork-layout-engine:

Patchwork layout engine
-----------------------

No examples provided at the Graphviz gallery for this layout engine.
In case you can contribute one, feel encouraged to get in contact with us.
Navigate to the below URL to get further insights.

Documentation: https://graphviz.org/docs/layouts/patchwork/

.. index:: Graphs engines; Sfdp layout engine
.. _graphviz-graphs-sfdp-layout-engine:

Sfdp layout engine
------------------

No examples provided at the Graphviz gallery for this layout engine.
In case you can contribute one, feel encouraged to get in contact with us.
Navigate to the below URL to get further insights.

Documentation: https://graphviz.org/docs/layouts/sfdp/
