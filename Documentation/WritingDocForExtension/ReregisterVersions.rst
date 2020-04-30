.. include:: ../Includes.txt
.. highlight:: rst

.. _reregister-versions:

===================
Reregister versions
===================

If there are documentations for some extension version missing they have to be announced to Intercept again.
This can be achieved by triggering the :ref:`webhook` with the correct version number.
Therefore please register webhook first, if not already done.

As we all don't want to loose our tags, this can be worked around by creating
branches with the same version number and push them to the repository and
remove them directly after that.

With a lot of versions release this task can get very tedious. To get over it
in an efficient way, the follow script can help with the task.

.. code-block:: bash

   #!/bin/sh

   EXTENSION="$1"

   mkdir -p "/tmp/$EXTENSION"
   git clone "git@github.com:$EXTENSION.git" "/tmp/$EXTENSION"

   cd "/tmp/$EXTENSION"
   for tag in $(git tag)
   do
           git checkout -b $tag $tag;
           git push origin refs/heads/$tag;
           git push --delete origin refs/heads/$tag;
           git checkout master;
           git branch -D $tag;
           sleep 10;
   done

   rm -rf "/tmp/$EXTENSION"

The script needs to be called with the repository name. If you saved the script
with the name :file:`trigger_documentation_push.sh` this would be executed like for
example

.. code-block:: bash

   sh trigger_documentation_push.sh evoWeb/sf_register

This will:

#. Create a temporary folder

#. Clones the extension into that

#. Create branches for each tag

#. Pushes and deletes them to origin

#. Deletes them locally

#. Takes a nap of 10 seconds and after all work is done removes the cloned folder

All versions should now be queued for the extension.
This can be checked at https://intercept.typo3.com/admin/docs/deployments.
