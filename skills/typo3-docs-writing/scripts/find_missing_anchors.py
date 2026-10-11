#!/usr/bin/env python3
"""
Find reST headlines that have no anchor (a "..  _some-anchor:" target)
directly above them, lines that look like a broken anchor, and labels that
are the same anchor written twice.

Usage:
    python3 find_missing_anchors.py [DOC_ROOT] [--json OUT.json]

DOC_ROOT defaults to "Documentation" in the current directory.

The rendering normalizes a label before it uses it: it lowercases it and
turns every run of other characters than a-z and 0-9 into "-". So
"Building" and "building", or "Setup_Docker" and "setup-docker", are one
anchor. Two such labels side by side add nothing; keep the lowercase one.
"""

import os
import re
import sys
import json
import argparse

ADORNMENT_CHARS = set('=-~^"\'`#*+.:_')
ANCHOR_RE = re.compile(r'^\.\.\s+_([^:]+):\s*$')
# Anything that looks like someone was trying to write an anchor (leading
# dot(s), underscore, a name) but doesn't match ANCHOR_RE above -- catches
# typos like a single leading '.' instead of '..', a missing trailing ':',
# extra dots, or missing whitespace, without matching valid hyperlink
# targets (".. _name: https://...") which have real content after the ':'.
ANCHOR_ISH_RE = re.compile(r'^\.+\s*_[^:\s][^:]*:?\s*$')


def is_underline(line):
    s = line.rstrip('\n')
    if len(s) < 3:
        return None
    c = s[0]
    if c not in ADORNMENT_CHARS:
        return None
    if all(ch == c for ch in s):
        return c
    return None


def parse_headlines(lines):
    """Return a list of headline dicts, in document order.

    Detects both:
      Title
      =====
    and:
      =====
      Title
      =====
    """
    headlines = []
    n = len(lines)
    i = 0
    while i < n:
        oc = is_underline(lines[i])
        if oc is not None and i + 2 < n:
            text = lines[i + 1].rstrip('\n')
            uc = is_underline(lines[i + 2])
            if uc == oc and text.strip() and not text.strip().startswith('..'):
                headlines.append({
                    'title_line': i + 1, 'text': text.strip(), 'char': oc,
                    'overline_line': i, 'underline_line': i + 2,
                })
                i += 3
                continue
        if i + 1 < n:
            text = lines[i].rstrip('\n')
            uc = is_underline(lines[i + 1])
            if uc is not None and text.strip() and not text.strip().startswith('..'):
                # underline must be roughly as long as the title text (docutils requirement)
                if len(lines[i + 1].rstrip('\n')) >= len(text.strip()) - 2:
                    headlines.append({
                        'title_line': i, 'text': text.strip(), 'char': uc,
                        'overline_line': None, 'underline_line': i + 1,
                    })
                    i += 2
                    continue
        i += 1
    return headlines


def tight_block_above(lines, idx):
    """Collect the "front matter" block attached to the heading at `idx`.

    RST requires a blank line between the preceding content and a section
    title, so first skip that gap. What sits directly above it is a run of
    non-blank lines -- normally just the anchor, but sometimes an anchor
    stacked with other directives (e.g. ``.. index::``) with no blank line
    between them. Collect that whole contiguous non-blank run and search it
    for anchors, rather than only checking the single nearest line.
    """
    j = idx - 1
    while j >= 0 and lines[j].strip() == '':
        j -= 1
    block = []
    while j >= 0 and lines[j].strip() != '':
        block.append((j, lines[j].rstrip('\n')))
        j -= 1
    block.reverse()
    return block


def anchors_for_heading(lines, anchor_pos):
    """Return the list of anchor names found in the tight block of non-blank
    lines directly above this heading."""
    block = tight_block_above(lines, anchor_pos)
    anchors = []
    for _line_idx, text in block:
        m = ANCHOR_RE.match(text)
        if m:
            anchors.append(m.group(1))
    return anchors


def find_malformed_anchor_lines(lines):
    """Scan every line in the file (not just ones adjacent to a heading) for
    anything that looks like a botched attempt at an anchor: a leading dot
    typo, a missing trailing colon, extra dots, missing whitespace, etc."""
    malformed = []
    for line_idx, raw in enumerate(lines):
        text = raw.rstrip('\n')
        if ANCHOR_ISH_RE.match(text) and not ANCHOR_RE.match(text):
            malformed.append({'line': line_idx + 1, 'text': text})
    return malformed


def normalize(label):
    """The anchor a label stands for, as the rendering derives it."""
    return re.sub(r'[^a-z0-9]+', '-', label.lower()).strip('-')


def find_duplicate_labels(rst_files, doc_root):
    """Labels in the whole manual that normalize to the same anchor."""
    seen = {}
    for path in rst_files:
        with open(path, encoding='utf-8') as fh:
            for line_idx, raw in enumerate(fh):
                m = ANCHOR_RE.match(raw.rstrip('\n'))
                if m:
                    seen.setdefault(normalize(m.group(1)), []).append(
                        {'file': os.path.relpath(path, doc_root), 'line': line_idx + 1, 'label': m.group(1)})
    return {anchor: labels for anchor, labels in seen.items() if len(labels) > 1}


def scan_file(path):
    with open(path, encoding='utf-8') as fh:
        lines = fh.readlines()
    headlines = parse_headlines(lines)
    missing = []
    for h in headlines:
        anchor_pos = h['overline_line'] if h['overline_line'] is not None else h['title_line']
        anchors = anchors_for_heading(lines, anchor_pos)
        if not anchors:
            missing.append({'line': h['title_line'] + 1, 'text': h['text'], 'char': h['char']})
    malformed_found = find_malformed_anchor_lines(lines)
    return headlines, missing, malformed_found


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('doc_root', nargs='?', default='Documentation', help='Documentation root to scan')
    ap.add_argument('--json', metavar='OUT.json', help='Write full results as JSON to this path')
    ap.add_argument('--quiet', action='store_true', help='Only print the summary, not every finding')
    args = ap.parse_args()

    rst_files = []
    for root, _dirs, files in os.walk(args.doc_root):
        for f in files:
            if f.endswith('.rst'):
                rst_files.append(os.path.join(root, f))
    rst_files.sort()

    results = []
    total_headlines = 0
    total_missing = 0
    total_malformed = 0

    for path in rst_files:
        headlines, missing, malformed = scan_file(path)
        total_headlines += len(headlines)
        total_missing += len(missing)
        total_malformed += len(malformed)
        if missing or malformed:
            rel = os.path.relpath(path, args.doc_root)
            results.append({'file': rel, 'missing': missing, 'malformed': malformed,
                             'total_headlines_in_file': len(headlines)})
            if not args.quiet:
                print(rel)
                for m in missing:
                    print(f"    missing   line {m['line']:>5}  ({m['char']!r})  {m['text']}")
                for m in malformed:
                    print(f"    MALFORMED line {m['line']:>5}  {m['text']!r}  (looks like a broken anchor)")

    duplicates = find_duplicate_labels(rst_files, args.doc_root)
    if duplicates and not args.quiet:
        print('Labels that are the same anchor:')
        for anchor, labels in sorted(duplicates.items()):
            where = ', '.join(f"{l['file']}:{l['line']} {l['label']}" for l in labels)
            print(f"    {anchor}: {where}")

    print()
    print(f"Scanned {len(rst_files)} .rst files under {args.doc_root}")
    print(f"Total headlines found:        {total_headlines}")
    print(f"Headlines missing an anchor:  {total_missing}")
    print(f"Malformed anchor-like lines:  {total_malformed}")
    print(f"Anchors written twice:        {len(duplicates)}")
    print(f"Files with findings:          {len(results)}")

    if args.json:
        with open(args.json, 'w') as f:
            json.dump({
                'doc_root': args.doc_root,
                'total_headlines': total_headlines,
                'total_missing': total_missing,
                'total_malformed': total_malformed,
                'duplicates': duplicates,
                'files': results,
            }, f, indent=1)
        print(f"Full results written to {args.json}")


if __name__ == '__main__':
    main()
