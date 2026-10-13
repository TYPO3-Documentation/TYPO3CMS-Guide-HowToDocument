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
    --repo <manual> --out <scratch dir>/screenshot-review.html [PATH ...]
```

*   Without `--commit`, it compares the PNG files that changed in the
    working tree with `HEAD`, including new and deleted ones.
*   With `--commit <rev>`, it compares the PNG files that this commit
    changed with its parent. Use this to check a commit that is already
    made, also one of a merged pull request.
*   `PATH` limits the comparison to files or folders, such as
    `Documentation/Images`.

Write the page into a scratch directory, never into the repository. The
script prints one line per image to stderr: the number of changed pixels
and the mean error, or why it could not compare the image (added, deleted,
size changed, a PNG format it cannot read).

## 2. Show the page and let the user decide

The page lists the images by how much changed: added, deleted, and resized
ones first, then the largest change. For every image, it shows the old
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
    `git restore -- <path>`, or delete it if it is new. Stage the images marked **Commit** by their path. Never stage the
    images of a screenshot run with `git add -A` or `git add .`.
*   **Existing commit:** propose a new commit that takes the old version of
    each image marked **Restore** back with
    `git checkout <rev>^ -- <path>`. Make it only after the user agrees,
    with the commit rules of the repository.

An image that changed because of the task, but in a chapter that the task
did not touch, is a side effect. Point it out instead of restoring it, so
the cause can be fixed.
