.. include:: ../Includes.txt
.. highlight:: bash

.. _reregister-versions:

===================
Reregister versions
===================

If there are documentations for some extension version missing, they have to be announced to Intercept again.
This can be achieved by triggering the :ref:`webhook` with the correct version number.
Therefore please register webhook first, if not already done.

As no new releases should be created, branches can be created for each existing release.
Those branches need to match the release version.
The created branches can be pushed, to trigger the webhook.
Once done, those branches can be removed again, to keep the repository clean.

With a lot of versions release this task can get very tedious.
To get over it in an efficient way, the following script can help with the task::

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

The script needs to be called with the repository name.
If the script is saved with the name :file:`trigger_documentation_push.sh` this would be executed like for example::

   sh trigger_documentation_push.sh evoWeb/sf_register

This will:

#. Create a temporary folder

#. Clones the extension into that

#. Create branches for each tag

#. Pushes and deletes them to origin

#. Deletes them locally

#. Takes a nap of 10 seconds and after all work is done removes the cloned folder

All versions should now be queued for the extension.
This can be checked as described at :ref:`webhook` last step.
