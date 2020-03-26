.. include:: ../Includes.txt
.. highlight:: rst

.. _reregister-versions:

=============================
Script to reregister versions
=============================

If there are documentations for some extension version missing they have to
be announced to Intercept again. This can be achieved by triggering a webhook
with the correct version number.

As we all dont wont to loose our tags, this can be worked around by creating
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
              git checkout -b $tag $tags;
              git push origin refs/heads/$tag;
              git push --delete origin refs/heads/$tag;
              git checkout master;
              git branch -D $tag;
              sleep 10;
      done

      rm -rf "/tmp/$EXTENSION"

The script needs to be called with the repository name. If you saved the script
with the name trigger_documentation_push.sh this would be executed like for
example

   .. code-block:: bash

      trigger_documentation_push.sh evoWeb/sf_register

This will create a temporary folder, clones the script into that, creates
branches for each tag, pushes and deletes them to origin, deletes them locally,
takes a nap of 10 seconds and after all work is done removes the cloned folder.

After that the extensions should queued to be approved, which can be check
on https://intercept.typo3.com/admin/docs/deployments . Please be patient,
because they need to be approved manually. As the documentation team has a
lot to do this can take some time.
