.. include:: ../Includes.txt
.. highlight:: bash

.. _rendering-docs-troubleshooting:

===============
Troubleshooting
===============

If you run into problems, here are some
helpful hints on how to solve them.

Remember, you can always ask questions in the **#typo3-documentation**
channel on Slack! `Register for slack <https://my.typo3.org/index.php?id=35>`__
and join the channel, if you have not done so already.


When you run `dockrun_t3rdf makehtml`, you should see some output. If
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

.. _render-troubleshooting-errors:

Errors That Break the Rendering
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

Scroll back in your terminal to see where the errors occured:

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

Remember, every file includes :file:`Includes.txt` at the top. Check your
latest changes.

.. code-block:: none

   .. include:: ../Includes.txt

Correct the path, so it will point to the existing Includes.txt (which
should be located in the directory :file:`Documentation`.

.. _render-troubleshooting-warnings:

Warnings
========

There may be problems which will not break the rendering but which
should be taken care of. Warnings are listed in the file
:file:`Documentation-GENERATED-temp/Result/project/0.0.0/_buildinfo/warnings.txt`

You can look at them in the browser (or whatever application has been
setup on your system for this file type):

.. code-block:: bash

   open "file:///$(pwd)/Documentation-GENERATED-temp/Result/project/0.0.0/_buildinfo/warnings.txt"

Try `xdg-open` (for Linux) or `start` (for Windows) instead of `open` if this does not work for you.

You can also view the file in the terminal (or in your IDE / editor):

.. code-block:: bash

      less Documentation-GENERATED-temp/Result/project/0.0.0/_buildinfo/warnings.txt

.. tip::

   Create aliases for the commands that work best for you now!


.. _render-troubleshooting-incremental:

Incremental Rendering
=====================

After you make changes, you can initiate rendering again, for example:

.. code-block:: bash

   dockrun_t3rdf makehtml

This will cause .rst files, that have been changed, to be rendered again.

If the menu (toctree) has been changed, the menu may not be correctly
displayed for unchanged files because they will not be rendered again.

If you need a complete rendering, delete the :file:`Documentation-GENERATED-temp`
folder and render again, for example:

.. code-block:: bash

  rm -rf Documentation-GENERATED-temp
  dockrun_t3rdf makehtml
