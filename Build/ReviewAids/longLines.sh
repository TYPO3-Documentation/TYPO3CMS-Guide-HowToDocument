#!/usr/bin/env bash
#
# Report the lines a change adds that reach the 80 character limit the style
# guide sets for reStructuredText:
#
#   https://docs.typo3.org/m/typo3/docs-how-to-document/main/en-us/Advanced/CodingGuidelines.html
#
# Usage, from the repository whose change is under review:
#
#   ../guide-h2d/Build/ReviewAids/longLines.sh [<base>] [<pathspec>...]
#
# <base> defaults to origin/main, the pathspec to reST and PHP files.
#
# Only added lines are looked at, because the rule is younger than the
# manuals: a single manual carries thousands of lines that were already too
# long, so a full-tree run reports the past instead of the change. URLs are
# skipped as well — a link that does not fit still has to stay on one line.
#
# This is a review aid, not a test: it always exits 0, and whether a long line
# is worth rewrapping is an editorial decision. See README.md.

set -euo pipefail

base="${1:-origin/main}"
[ "$#" -gt 0 ] && shift
[ "$#" -eq 0 ] && set -- '*.rst' '*.rst.txt' '*.php'

git diff "${base}...HEAD" -- "$@" | awk '
    /^\+\+\+ b\// {
        file = substr($0, 7)
        next
    }
    /^@@ / {
        match($0, /\+[0-9]+/)
        line = substr($0, RSTART + 1, RLENGTH - 1) + 0
        next
    }
    /^ / {
        line++
        next
    }
    /^\+/ {
        text = substr($0, 2)
        if (length(text) >= 80 && text !~ /https?:\/\//) {
            printf "%s:%d  (%d chars)\n    %s\n", file, line, length(text), text
            found++
        }
        line++
    }
    END {
        if (found) {
            printf "\n%d added line(s) reach 80 characters.\n", found
        } else {
            print "No added line reaches 80 characters."
        }
    }
'
