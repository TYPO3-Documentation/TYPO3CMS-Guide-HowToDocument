#!/usr/bin/env python3
"""Compares changed PNG screenshots of a git repository with their previous
version and writes an HTML page that shows the old image, the new image and
the changed pixels next to each other, sorted by how much changed.

Usage:
    compare_screenshots.py [--repo DIR] [--commit REV] [--out FILE] [PATH ...]

Without --commit, the images that changed in the working tree are compared
with HEAD. With --commit, the images that the commit changed are compared
with its parent. PATH limits the comparison to these files or folders.

Needs only the Python standard library. Uses Pillow when it is installed,
which decodes large images faster.
"""

import argparse
import base64
import html
import json
import struct
import subprocess
import sys
import zlib
from pathlib import Path

# A pixel counts as changed when the sum of the differences of its red,
# green and blue values is above this, as in the screenshot tooling of the
# Editors Tutorial. Smaller differences come from anti-aliasing.
PIXEL_TOLERANCE = 30


def git(repo, *args, binary=False):
    result = subprocess.run(['git', '-C', repo, *args], capture_output=True, check=False)
    if result.returncode != 0:
        return None
    return result.stdout if binary else result.stdout.decode()


def changed_images(repo, commit, paths):
    """Yields (status, path) of the PNG files that changed."""
    spec = ['--', *(paths or ['.'])]
    if commit:
        output = git(repo, 'diff', '--name-status', '--no-renames', f'{commit}^', commit, *spec)
    else:
        output = git(repo, 'status', '--porcelain', '--untracked-files=all', '--no-renames', *spec)
    for line in (output or '').splitlines():
        if commit:
            status, path = line.split('\t', 1)
        else:
            status, path = line[:2].strip(), line[3:]
        if path.lower().endswith('.png'):
            yield status[0], path


def old_and_new(repo, commit, path):
    base = f'{commit}^' if commit else 'HEAD'
    old = git(repo, 'show', f'{base}:{path}', binary=True)
    if commit:
        new = git(repo, 'show', f'{commit}:{path}', binary=True)
    else:
        file = Path(repo) / path
        new = file.read_bytes() if file.exists() else None
    return old, new


def decode_png(data):
    """Returns (width, height, rgb bytes), or None for a PNG this decoder
    does not support."""
    try:
        from io import BytesIO
        from PIL import Image
        image = Image.open(BytesIO(data)).convert('RGB')
        return image.width, image.height, image.tobytes()
    except ImportError:
        pass
    except Exception:
        return None
    if data[:8] != b'\x89PNG\r\n\x1a\n':
        return None
    position, chunks, palette = 8, [], None
    while position < len(data):
        length, kind = struct.unpack('>I4s', data[position:position + 8])
        body = data[position + 8:position + 8 + length]
        if kind == b'IHDR':
            width, height, depth, color, _, _, interlace = struct.unpack('>IIBBBBB', body)
        elif kind == b'PLTE':
            palette = body
        elif kind == b'IDAT':
            chunks.append(body)
        position += 12 + length
    channels = {0: 1, 2: 3, 3: 1, 4: 2, 6: 4}.get(color)
    if depth != 8 or interlace or channels is None:
        return None
    raw = zlib.decompress(b''.join(chunks))
    stride = width * channels
    rows, previous = [], bytearray(stride)
    for y in range(height):
        start = y * (stride + 1)
        kind, row = raw[start], bytearray(raw[start + 1:start + 1 + stride])
        if kind == 1:
            for i in range(channels, stride):
                row[i] = (row[i] + row[i - channels]) & 255
        elif kind == 2:
            row = bytearray((a + b) & 255 for a, b in zip(row, previous))
        elif kind == 3:
            for i in range(stride):
                left = row[i - channels] if i >= channels else 0
                row[i] = (row[i] + ((left + previous[i]) >> 1)) & 255
        elif kind == 4:
            for i in range(stride):
                a = row[i - channels] if i >= channels else 0
                b, c = previous[i], previous[i - channels] if i >= channels else 0
                p = a + b - c
                pa, pb, pc = abs(p - a), abs(p - b), abs(p - c)
                row[i] = (row[i] + (a if pa <= pb and pa <= pc else b if pb <= pc else c)) & 255
        rows.append(row)
        previous = row
    pixels = b''.join(rows)
    if color == 2:
        return width, height, pixels
    rgb = bytearray(width * height * 3)
    for i in range(width * height):
        if color == 6:
            rgb[i * 3:i * 3 + 3] = pixels[i * 4:i * 4 + 3]
        elif color == 3:
            rgb[i * 3:i * 3 + 3] = palette[pixels[i] * 3:pixels[i] * 3 + 3]
        else:
            rgb[i * 3:i * 3 + 3] = bytes([pixels[i * channels]]) * 3
    return width, height, bytes(rgb)


def encode_png(width, height, rgb):
    def chunk(kind, body):
        return struct.pack('>I', len(body)) + kind + body + struct.pack('>I', zlib.crc32(kind + body))
    stride = width * 3
    raw = b''.join(b'\x00' + rgb[y * stride:(y + 1) * stride] for y in range(height))
    return (b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', struct.pack('>IIBBBBB', width, height, 8, 2, 0, 0, 0))
            + chunk(b'IDAT', zlib.compress(raw, 9)) + chunk(b'IEND', b''))


def compare(old, new):
    """Returns the measures of the difference and the image that shows it:
    the new image faded, with the changed pixels in red."""
    (width, height, a), (_, _, b) = old, new
    changed, total = 0, 0
    box = [width, height, -1, -1]
    diff = bytearray(len(b))
    stride = width * 3
    for y in range(height):
        row = slice(y * stride, (y + 1) * stride)
        if a[row] == b[row]:
            diff[row] = bytes(255 - (255 - v) // 4 for v in b[row])
            continue
        for x in range(width):
            i = y * stride + x * 3
            delta = abs(a[i] - b[i]) + abs(a[i + 1] - b[i + 1]) + abs(a[i + 2] - b[i + 2])
            total += delta
            if delta > PIXEL_TOLERANCE:
                changed += 1
                diff[i:i + 3] = b'\xe0\x1b\x24'
                box = [min(box[0], x), min(box[1], y), max(box[2], x), max(box[3], y)]
            else:
                diff[i:i + 3] = bytes(255 - (255 - v) // 4 for v in b[i:i + 3])
    measures = {
        'changedPixels': changed,
        'changedShare': changed / (width * height),
        # The mean absolute error, as ImageMagick computes it: 0 is the same
        # image, 1 is black against white everywhere
        'meanError': total / (width * height * 3 * 255),
        'box': None if box[2] < 0 else [box[0], box[1], box[2] - box[0] + 1, box[3] - box[1] + 1],
    }
    return measures, encode_png(width, height, bytes(diff))


def data_uri(png):
    return 'data:image/png;base64,' + base64.b64encode(png).decode() if png else ''


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--repo', default='.')
    parser.add_argument('--commit')
    parser.add_argument('--out', default='screenshot-review.html')
    parser.add_argument('paths', nargs='*')
    arguments = parser.parse_args()
    repo = git(arguments.repo, 'rev-parse', '--show-toplevel')
    if repo is None:
        sys.exit(f'{arguments.repo} is not a git repository')
    repo = repo.strip()

    entries = []
    for status, path in changed_images(repo, arguments.commit, arguments.paths):
        old, new = old_and_new(repo, arguments.commit, path)
        entry = {'path': path, 'status': status, 'old': data_uri(old), 'new': data_uri(new), 'diff': ''}
        decoded = [decode_png(image) if image else None for image in (old, new)]
        if old is None or new is None:
            entry['note'] = 'added' if old is None else 'deleted'
        elif None in decoded:
            entry['note'] = 'not comparable: a PNG format the script cannot read'
        elif decoded[0][:2] != decoded[1][:2]:
            entry['note'] = 'size changed from {}×{} to {}×{}'.format(*decoded[0][:2], *decoded[1][:2])
        else:
            measures, diff = compare(*decoded)
            entry.update(measures, diff=data_uri(diff))
        print('{}: {}'.format(path, entry.get('note') or '{changedPixels} px changed, mean error {meanError:.6f}'.format(**entry)),
              file=sys.stderr)
        entries.append(entry)

    # Added, deleted and resized images first, then the biggest changes
    entries.sort(key=lambda e: (0, 0) if 'note' in e else (1, -e['meanError']))
    template = (Path(__file__).parent / 'review-page.html').read_text()
    source = f'commit {arguments.commit}' if arguments.commit else 'working tree compared with HEAD'
    page = (template
            .replace('{{SOURCE}}', html.escape(f'{Path(repo).name}, {source}'))
            .replace('{{ENTRIES}}', json.dumps(entries).replace('</', '<\\/')))
    Path(arguments.out).parent.mkdir(parents=True, exist_ok=True)
    Path(arguments.out).write_text(page)
    print(f'{len(entries)} images, {len(page) / 1e6:.1f} MB: {arguments.out}', file=sys.stderr)


if __name__ == '__main__':
    main()
