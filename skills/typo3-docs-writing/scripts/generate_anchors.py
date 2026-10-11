#!/usr/bin/env python3
"""
Insert an anchor above every reST headline that has none.

A new anchor is the anchor of the section the headline is in, plus the
headline in kebab case: "With make" on the page "migration" becomes
"migration-with-make". If that is longer than MAX_LENGTH characters, the
suffix leaves out stopwords, then words the prefix already contains. A page
title without an anchor gets one from its file path. A name that is taken
gets "-2", "-3", and so on.

Existing anchors are never changed. Without --apply, the script only prints
the plan; check it, then run it again with --apply.

Usage:
    python3 generate_anchors.py [DOC_ROOT] [--apply] [--plan-json OUT.json]

DOC_ROOT defaults to "Documentation" in the current directory.
"""

import os
import re
import sys
import json
import argparse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from find_missing_anchors import (
    is_underline, parse_headlines, tight_block_above, ANCHOR_RE,
    anchors_for_heading, find_malformed_anchor_lines, normalize,
)

MAX_LENGTH = 50

STOPWORDS = {
    'a', 'an', 'the', 'of', 'and', 'or', 'in', 'on', 'for', 'with', 'to',
    'from', 'is', 'are', 'this', 'that', 'as', 'by', 'into', 'at', 'your',
    'you', 'be', 'can', 'will', 'using', 'use', 'via', 'not', 'it', 'its',
    'their', 'when', 'how', 'what', 'if', 'so', 'do', 'does', 'did', 'was',
    'were', 'been', 'being', 'than', 'then', 'there', 'these', 'those',
    'which', 'who', 'whom', 'about', 'after', 'before', 'between', 'during',
    'over', 'again', 'once', 'here', 'all', 'any', 'both', 'each', 'more',
    'most', 'other', 'some', 'such', 'no', 'nor', 'only', 'own', 'same',
    'too', 'very', 'just', 'also', 'up', 'out', 'off', 'have', 'has', 'had',
}

def strip_markup(text):
    def role_repl(m):
        inner = m.group(1)
        inner = re.sub(r'\s*<[^>]*>\s*$', '', inner)
        return inner
    text = re.sub(r':[A-Za-z0-9_-]+:`([^`]*)`', role_repl, text)
    text = re.sub(r'`([^`]*)`', r'\1', text)
    text = text.replace('\\', '')
    text = re.sub(r'\*\*([^*]*)\*\*', r'\1', text)
    text = re.sub(r'\*([^*]*)\*', r'\1', text)
    return text


def to_kebab(s):
    """Convert an existing anchor string (possibly camelCase, snake_case, or
    otherwise non-kebab) into pure kebab-case, for use as the base of a
    newly-minted anchor. Never applied to anchors that already exist in the
    file -- those are left untouched -- only to the string we build a new
    child anchor on top of."""
    s = re.sub(r'([a-z0-9])([A-Z])', r'\1-\2', s)
    s = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1-\2', s)
    s = s.replace('_', '-')
    s = s.lower()
    s = re.sub(r'[^a-z0-9-]+', '-', s)
    s = re.sub(r'-+', '-', s).strip('-')
    return s


def headline_words(text):
    return re.findall(r"[a-z0-9]+", strip_markup(text).lower()) or ['section']


def child_anchor(prefix, text):
    """The prefix plus the whole headline, shortened only when it is long."""
    words = headline_words(text)
    candidate = f"{prefix}-{'-'.join(words)}"
    if len(candidate) <= MAX_LENGTH:
        return candidate
    words = [w for w in words if w not in STOPWORDS] or words
    candidate = f"{prefix}-{'-'.join(words)}"
    if len(candidate) <= MAX_LENGTH:
        return candidate
    in_prefix = set(prefix.split('-'))
    words = [w for w in words if w not in in_prefix] or words
    return f"{prefix}-{'-'.join(words)}"


def path_base(path, doc_root):
    rel = os.path.relpath(path, doc_root)
    rel = rel[:-4]
    parts = rel.split(os.sep)
    if parts[-1].lower() == 'index':
        parts = parts[:-1]
    slug_parts = []
    for p in parts:
        words = re.findall(r'[A-Za-z0-9]+', p)
        out = []
        for w in words:
            sub = re.findall(r'[A-Z]+(?=[A-Z][a-z])|[A-Z]?[a-z]+|[0-9]+|[A-Z]+', w)
            out.extend(sub if sub else [w])
        slug_parts.append('-'.join(x.lower() for x in out))
    return '-'.join(slug_parts) if slug_parts else 'index'


def build_plan(doc_root, existing_anchor_names):
    # Compare normalized forms: "Setup_Docker" already takes "setup-docker".
    global_set = {normalize(name) for name in existing_anchor_names}

    def unique(name):
        if normalize(name) not in global_set:
            global_set.add(normalize(name))
            return name
        i = 2
        while normalize(f"{name}-{i}") in global_set:
            i += 1
        final = f"{name}-{i}"
        global_set.add(normalize(final))
        return final

    rst_files = []
    for root, _dirs, files in os.walk(doc_root):
        for f in files:
            if f.endswith('.rst'):
                rst_files.append(os.path.join(root, f))
    rst_files.sort()

    plan = []
    warnings = []
    for path in rst_files:
        with open(path, encoding='utf-8') as fh:
            lines = fh.readlines()
        rel_for_warn = os.path.relpath(path, doc_root)
        for m in find_malformed_anchor_lines(lines):
            warnings.append(f"{rel_for_warn}:{m['line']}: looks like a broken anchor, left untouched: {m['text']!r}")
        headlines = parse_headlines(lines)
        level_of_char = {}
        stack = []
        insertions = []
        rel = os.path.relpath(path, doc_root)
        for hi, h in enumerate(headlines):
            anchor_pos = h['overline_line'] if h['overline_line'] is not None else h['title_line']
            anchor_names = anchors_for_heading(lines, anchor_pos)
            is_title = (hi == 0)
            if is_title:
                level = 0
            else:
                if h['char'] not in level_of_char:
                    level_of_char[h['char']] = len(level_of_char) + 1
                level = level_of_char[h['char']]
            while stack and stack[-1][0] >= level:
                stack.pop()
            parent_base = stack[-1][1] if stack else None

            if anchor_names:
                if parent_base:
                    matches = [a for a in anchor_names if a == parent_base or a.startswith(parent_base + '-')]
                    canonical = matches[0] if matches else anchor_names[0]
                else:
                    canonical = anchor_names[0]
            else:
                if parent_base:
                    candidate = child_anchor(to_kebab(parent_base), h['text'])
                else:
                    base = path_base(path, doc_root)
                    candidate = base if is_title else child_anchor(base, h['text'])
                canonical = unique(candidate)
                if len(canonical) > MAX_LENGTH:
                    warnings.append(f"{rel}:{h['title_line'] + 1}: {canonical!r} is {len(canonical)} characters; shorten it by hand")
                insertions.append({'anchor_pos': anchor_pos, 'anchor': canonical, 'text': h['text'], 'line': h['title_line'] + 1})

            stack.append((level, canonical))

        if insertions:
            plan.append({'file': rel, 'insertions': insertions})

    return plan, warnings


def apply_plan(doc_root, plan):
    total = 0
    for entry in plan:
        path = os.path.join(doc_root, entry['file'])
        with open(path, encoding='utf-8') as fh:
            lines = fh.readlines()
        for ins in sorted(entry['insertions'], key=lambda x: -x['anchor_pos']):
            pos = ins['anchor_pos']
            new_lines = [f"..  _{ins['anchor']}:\n", "\n"]
            lines[pos:pos] = new_lines
            total += 1
        with open(path, 'w', encoding='utf-8') as fh:
            fh.writelines(lines)
    return total


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('doc_root', nargs='?', default='Documentation')
    ap.add_argument('--apply', action='store_true', help='Actually write the anchors into files')
    ap.add_argument('--plan-json', default=None)
    args = ap.parse_args()

    # gather all currently-existing anchor names project-wide, for uniqueness
    existing = set()
    for root, _dirs, files in os.walk(args.doc_root):
        for f in files:
            if f.endswith('.rst'):
                path = os.path.join(root, f)
                with open(path, encoding='utf-8') as fh:
                    for line in fh:
                        m = ANCHOR_RE.match(line.rstrip('\n'))
                        if m:
                            existing.add(m.group(1))

    plan, warnings = build_plan(args.doc_root, existing)
    total = sum(len(e['insertions']) for e in plan)

    for entry in plan:
        print(entry['file'])
        for ins in entry['insertions']:
            print(f"    line {ins['line']:>5}  ..  _{ins['anchor']}:  ({ins['text']})")
    print()

    if warnings:
        print(f"WARNING: {len(warnings)} finding(s) to check by hand. A line that looks")
        print("like a broken anchor is not recognized as an anchor, so its headline may")
        print("get a new anchor beside the broken one. Fix these yourself:")
        for w in warnings:
            print(f"    {w}")
        print()

    print(f"Plan: {total} new anchors across {len(plan)} files")

    if args.plan_json:
        with open(args.plan_json, 'w') as f:
            json.dump(plan, f, indent=1)
        print(f"Plan written to {args.plan_json}")

    if args.apply:
        n = apply_plan(args.doc_root, plan)
        print(f"Applied {n} insertions.")
    else:
        print("Dry run only. Re-run with --apply to write changes.")


if __name__ == '__main__':
    main()
