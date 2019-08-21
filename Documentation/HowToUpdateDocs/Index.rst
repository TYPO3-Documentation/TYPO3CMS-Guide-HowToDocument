.. include:: ../Includes.txt
.. highlight:: rst

.. _update-docs:

===========================
How to Update Documentation
===========================

Once a new TYPO3 release comes out, the main documentation (e.g. :ref:`t3coreapi:start`,
:ref:`t3tca:start` etc.) must be updated.

Here, we describe some best practices for updating the official documentation
for a new TYPO3 release. We stick to the core conventions as much as possible because that
makes it easier for everyone.

* Once a feature is deprecated in the core, it is removed from the main documentation
  in the respective version branches where the feature is deprecated.
* It is not necessary to create an issue for every change
* The commit message can point out the releases to which the change should apply
  (as in the core commits), e.g. `Releases: master, 9.5`, see :ref:`general-conventions-commit-messages`.
* The person merging the commit should take care of merging into other branches as well
  (in case that is necessary)
* The commit can have a subject such as `[TASK] Update with changes from 9.5.3`. 

