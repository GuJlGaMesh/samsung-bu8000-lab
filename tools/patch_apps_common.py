"""Offline, exact-hash patch. Never connects to a TV."""
import argparse
import hashlib
import json
from pathlib import Path

MANIFEST = Path(__file__).resolve().parents[1] / 'profiles/installed-only-patch.json'


def transform(data, reverse=False):
    spec = json.loads(MANIFEST.read_text(encoding='utf-8'))
    source = spec['patchedSha256'] if reverse else spec['originalSha256']
    target = spec['originalSha256'] if reverse else spec['patchedSha256']
    if hashlib.sha256(data).hexdigest() != source:
        raise ValueError('Unsupported input hash: do not patch another firmware or an already modified DLL')
    offset = int(spec['fileOffset'], 16)
    before = bytes.fromhex(spec['after'] if reverse else spec['before'])
    after = bytes.fromhex(spec['before'] if reverse else spec['after'])
    if data[offset:offset + len(before)] != before:
        raise ValueError('Instruction bytes do not match the manifest')
    result = data[:offset] + after + data[offset + len(before):]
    if hashlib.sha256(result).hexdigest() != target:
        raise ValueError('Unexpected output hash')
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', type=Path)
    parser.add_argument('output', type=Path)
    parser.add_argument('--reverse', action='store_true')
    args = parser.parse_args()
    result = transform(args.input.read_bytes(), args.reverse)
    # Exclusive creation: preserve an existing output or the input itself.
    with args.output.open('xb') as output:
        output.write(result)
    print(hashlib.sha256(result).hexdigest())


if __name__ == '__main__':
    main()
