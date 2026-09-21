# Review aids

Small scripts that help a reviewer — human or AI — look at a documentation
change. They are kept here, in the repository that also holds the rules they
check, so that every manual can use the same ones instead of each repository
growing its own copy.

## What belongs here, and what does not

A review aid **reports, it never edits**, and it is **not a test**. It points
at lines worth a second look; deciding whether a line is actually wrong stays
with the reviewer.

That is the difference to a manual's own `Build/Scripts/`: a check that can
decide a violation on its own belongs there, wired into `runTests.sh` and a
`make test-*` target, so that CI gates it. A check belongs here instead when

*   it cannot separate a violation from a legitimate exception, so a gate
    would report noise, or
*   the rule is only enforceable for the lines a change adds, because the
    existing corpus predates it.

Every aid documents, in its own header, what it cannot see and which findings
are expected to be false positives. An aid whose false positives disappear has
outgrown this folder and should move into the manuals as a real check.

## Using them

The aids are run from the repository whose change is under review, with the
path to this folder — in a workspace where the manuals are checked out side by
side that is `../guide-h2d`:

```bash
cd ../coreapi
../guide-h2d/Build/ReviewAids/longLines.sh origin/main
../guide-h2d/Build/ReviewAids/missingImports.php Documentation
```

They need nothing installed in this repository. `missingImports.php` uses the
PHP parser from the Composer installation of the manual it is pointed at, so
that manual needs its `make install` to have run.

## The aids

### `longLines.sh`

Reports the reST and PHP lines a change **adds** that reach the 80 character
limit.

Blind to lines that were already too long — the rule is younger than the
manuals, so only added lines can be judged — and to URLs, which stay on one
line whatever their length.

### `missingImports.php`

Reports the class names a PHP snippet uses without importing them, which a
reader copying the example into an extension would have to add by hand.

Blind to names in doc comments, because it reads code and not text, and
unable to tell a missing import from a class that legitimately lives in the
same namespace as the snippet — so expect most of its findings to be fine.
`CodeSnippets/` is skipped entirely: a generator writes those files, as
excerpts without a namespace.
