---
name: typo3-docs-screenshot-review
description: Compare changed PNG screenshots of a TYPO3 manual with their previous version, show the old image, the new one, and the changed pixels on a page, and let the user decide which images go into the commit. Use after a run that regenerates screenshots and before staging or committing PNG files, or when asked whether a commit or pull request holds screenshots that did not really change.
---

# Reviewing changed screenshots

A run that generates screenshots changes more images than the task did.
Fonts, animations, and images that load late make some screenshots differ
a little on every run. Git stores every version of a binary file in full,
so each image that is committed without a real change makes the repository
bigger for good. The user decides which images go into a commit. This
skill shows them what changed, so they can decide quickly.

## 1. Compare the images

Run the script of this skill with Python 3. It needs only the standard
library:

```bash
python3 -I <skill dir>/scripts/compare_screenshots.py \
    --repo <manual> --session <session name> [--flaky <list>] \
    --out <scratch dir>/screenshot-review.html [PATH ...]
```

*   Without `--commit`, it compares the PNG files that changed in the
    working tree with `HEAD`, including new and deleted ones.
*   With `--commit <rev>`, it compares the PNG files that this commit
    changed with its parent. Use this to check a commit that is already
    made, also one of a merged pull request.
*   `PATH` limits the comparison to files or folders, such as
    `Documentation/Images`.
*   `--session` names the session at the top of the page, in its title,
    and in the copied decisions. Pass the name that the user knows the
    session by: a user who runs several sessions at the same time sees
    which one a page belongs to.
*   `--flaky` names a file of the manual that lists the screenshots that
    change on every run, one path or glob per line, with `#` for comments.
    The page shows these images in a section of their own, with
    **Restore** chosen. Pass the list whenever the manual has one.
*   A new image that replaces a deleted one is compared with it, as one
    entry. The script finds the pair in the changed `.rst` files, where a
    `figure`, `image`, or `include` directive switches from the old image
    to the new one. `--pair <old> <new>` adds a pair that the `.rst` files
    do not show.

Write the page into a scratch directory, never into the repository. The
script prints one line per image to stderr: the number of changed pixels
and the mean error, or why it could not compare the image (added, deleted,
size changed, a PNG format it cannot read), and the image that a new one
replaces.

## 2. Show the page and let the user decide

The page lists the images by how much changed: added, deleted, replaced,
and resized ones first, then the largest change, then the images of the
flaky list. For every image, it shows the old
version, the new one, and the changes in red with a frame around them. The
user marks each image as **Commit** or **Restore** and copies the
decisions.

*   If the session can publish a private page, such as an artifact on
    claude.ai, publish the file there and give the user the link.
*   Otherwise give the user the path of the file to open in a browser.

Do not decide for the user, and do not take the numbers as the answer. A
large change can be noise, such as a picture that loaded with a different
crop, and a small change can be real, such as one renamed label in a
screenshot of the whole window. Images that change on every run are noise
for the task at hand, unless the task was to fix them. If the user asks for
a recommendation, name the images that the task meant to change and the
ones that it did not touch.

## 3. Apply the decisions

*   **Working tree:** restore every image marked **Restore** with
    `git restore -- <path>`, or delete it if it is new. The decision on a
    replacement covers both images: the copied decisions list the deleted
    image below the new one, marked `(replaced)`. Stage the images marked **Commit** by their path. Never stage the
    images of a screenshot run with `git add -A` or `git add .`.
*   **Existing commit:** propose a new commit that takes the old version of
    each image marked **Restore** back with
    `git checkout <rev>^ -- <path>`. Make it only after the user agrees,
    with the commit rules of the repository.

An image that changed because of the task, but in a chapter that the task
did not touch, is a side effect. Point it out instead of restoring it, so
the cause can be fixed.
