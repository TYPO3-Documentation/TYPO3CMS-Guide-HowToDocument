.. include:: ../Includes.txt
.. highlight:: rst



.. _docs-contribute-github-method:

=================================
Contribute with the Github method
=================================

Basic considerations
====================

In any case, you will need a Github account, go to
https://github.com/.

You can contribute to the documentation by editing directly on Github
by clicking on "Edit me on Github" in the top right corner of any page.

.. image:: ../images/edit_me_on_github.png
   :class: with-shadow

This can be used for minor changes.

If you wish to make extensive changes or use sphinx specific markup
(.e.g. intersphinx linking) it is recommended to use the :ref:`git/docker
<docs-contribute-git-docker>` method because via local rendering with
docker, you will get the best results and can detect errors before you
submit your pull request. The docker container uses the
same toolchain as on the documentation server.

With the Github Preview, you will not see how the menu is rendered,
you will not see some specific markup in action and it will not show
all errors correctly.

That being said, we recommend to try out the Github method, because it is
a way to quickly make changes, but use the :ref:`git/docker
<docs-contribute-git-docker>` method in the long run for larger
changes.


Getting started
===============

.. _github-method-youtube:

Youtube Tutorial - Github method
--------------------------------

Watch the official YouTube video `Tutorial - Contribute to
docs.typo3.org <https://www.youtube.com/watch?v=wNxO-aXY5Yw>`__
to get started.



2018-01-19 by Mathias Schreiber

.. youtube:: wNxO-aXY5Yw

Additional information
----------------------

Even though you can make minor changes very easily and do not need
to know everything about reST formatting, it is a good idea to go
back to this manual from time to time and familiarize
yourself with the basics:

* It is recommended to read the :ref:`writing-rest-introduction`
  and the general :ref:`format-rest-cgl` first.
* Look up specific reST format (e.g. embed images, embed YouTube
  Videos, use lists, headers, bold etc.): :ref:`Formatting-with-reST`.
