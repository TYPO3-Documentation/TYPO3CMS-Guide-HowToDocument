.. include:: /Includes.rst.txt
.. highlight:: bash
.. index:: Rendering; Troubleshooting
.. _rendering-docs-troubleshooting:

===========================================
Troubleshooting local rendering with Docker
===========================================

If you run into problems, here are some
helpful hints on how to solve them.

Remember, you can always ask questions in the **#typo3-documentation**
channel on Slack! `Register for slack <https://my.typo3.org/index.php?id=35>`__
and join the channel, if you have not done so already.


.. index:: Rendering; Problems with `source < (docker run ...`
.. _render-troubleshooting-source:

Problems with `source < (docker run ...`
========================================


.. code-block:: bash

   source <(docker run --rm t3docs/render-documentation show-shell-commands)
   dockrun_t3rd makehtml

If these commands do not work on your platform, try this instead:

.. code-block:: bash

    mkdir -p ~/bin
    docker run --rm t3docs/render-documentation show-shell-commands > ~/bin/t3docs
    source ~/bin/t3docs


.. _docker-troubleshoot-sample-output-ok:

Sample output without errors
============================

When you run render, you should see some output. If
everything works correctly, the final output should look like this:

.. code-block:: none

   ...

   We saw these exitcodes (code, count):
   {
      "0": 86
   }
   exiting with exitcode 0

   ...

Relevant is the exitcode 0. It indicates that everything executed
smoothly.


.. index:: Rendering; Errors
.. _render-troubleshooting-errors:

Errors that break the rendering
===============================

If there are errors which break the rendering, you may see something like:

.. code-block:: none

    We saw these exitcodes (code, count):
    {
      "0": 53,
      "3": 1,
      "22": 7
    }
   exiting with exitcode 0

Do not let the message *"exiting with exitcode 0"* mislead you. You've
definitely got a problem that needs to be taken care of.

.. important::

   If the rendering is not executed correctly, the files in
   :file:`Documentation-GENERATED-temp` will still contain
   the last rendered results (which are now no longer up to
   date) !

Scroll back in your terminal to see where the errors occurred:

.. code-block:: none

    ==================================================
       18-Make-and-build/run_Check-requirements.py
       exitcode: 22

    ==================================================
       20-Postprocess/run_00-Check-requirements.py
       exitcode: 22

    ==================================================
       22-Assemble-results/run_01-Assemble-html-pdf-and-more.py
       exitcode: 22

    ==================================================
       26-Collect-buildinfo/run_Check-requirements.py
       exitcode: 22

Everything with exitcode != 0 is relevant. Here, we see a problem
with the requirements. This is usually caused by an incorrect path
for including a file.

Remember, every file includes :file:`Includes.rst.txt` at the top. Check your
latest changes.

.. code-block:: none

   .. include:: /Includes.rst.txt

Correct the path, so it will point to the existing Includes.rst.txt (which
should be located in the directory :file:`Documentation`.


.. index:: Rendering; Warnings
.. _render-troubleshooting-warnings:

Warnings
========

There may be problems which will not break the rendering but which
should be taken care of. Warnings are listed in the file
:file:`Documentation-GENERATED-temp/Result/project/0.0.0/_buildinfo/warnings.txt`


.. index:: Rendering; Incremental
.. _render-troubleshooting-incremental:

Incremental Rendering
=====================

After you make changes, you can initiate rendering again.

This will cause .rst files, that has been changed, to be rendered again.

If the menu (toctree) has been changed, the menu may not be correctly
displayed for unchanged files because they will not be rendered again.

If you need a complete rendering, delete the :file:`Documentation-GENERATED-temp`
folder and render again, for example:

.. code-block:: bash

  rm -rf Documentation-GENERATED-temp


Get detailed information
========================

If you create a directory :file:`tmp-GENERATED-temp` before you start the rendering,
the toolchain will not remove this directory when it is done. Usually
it cleans up after itself and this directory will be created and then removed.

The directory contains some additional information for the individual scripts
that have been run. In case of cryptic error messages which you have trouble
interpreting, you may check these files for more information.

Look for files with ending :file:`err.txt` that are not empty.

Example output:

:file:`tmp-GENERATED-temp/RenderDocumentation/2019-05-19_06-37-50_072139/18-Make-and-build/40-Html/xeq-40-Make-html-1-err.txt`

.. code-block:: bash

   Traceback (most recent call last):
     File "/usr/local/lib/python2.7/site-packages/sphinx/cmdline.py", line 303, in main
       args.warningiserror, args.tags, args.verbosity, args.jobs)
     File "/usr/local/lib/python2.7/site-packages/sphinx/application.py", line 191, in __init__
       self.setup_extension(extension)
     File "/usr/local/lib/python2.7/site-packages/sphinx/application.py", line 411, in setup_extension
       self.registry.load_extension(self, extname)
     File "/usr/local/lib/python2.7/site-packages/sphinx/registry.py", line 318, in load_extension
       raise ExtensionError(__('Could not import extension %s') % extname, err)
   ExtensionError: Could not import extension sphinxcontrib.googlechart (exception: cannot import name Directive)

   Extension error:
   Could not import extension sphinxcontrib.googlechart (exception: cannot import name Directive)
