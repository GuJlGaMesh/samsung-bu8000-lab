"""Build an isolated MSX shortcut from an upstream WGT supplied by its owner."""
import argparse
import hashlib
import re
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urlencode


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--upstream', type=Path, required=True)
    parser.add_argument('--package', required=True, help='Unique ten-character package ID')
    parser.add_argument('--name', required=True)
    parser.add_argument('--start', required=True, help='Start parameter for the new shortcut')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if not re.fullmatch(r'[A-Za-z0-9]{10}', args.package):
        parser.error('Package ID must be ten alphanumeric characters')
    if args.package in ('l2UWJoWHQN', 'xV5oTMtg6G'):
        parser.error('Refusing to reuse an original MSX package ID')
    with zipfile.ZipFile(args.upstream) as source:
        if source.testzip() is not None:
            raise ValueError('Corrupt source WGT')
        files = {n: source.read(n) for n in source.namelist()
                 if n in ('config.xml', 'index.html') or n.startswith('img/') and not n.endswith('/')}
    # Known official distribution loader: reject silent upstream changes.
    expected = '6c632b6a331e758f7712687d0c2a0bd9099faeea67c248c7550d67dd4735ae0e'
    if hashlib.sha256(files['index.html']).hexdigest() != expected:
        raise ValueError('Unreviewed MSX loader version; review it before updating the accepted hash')
    widget = 'http://www.w3.org/ns/widgets'
    tizen = 'http://tizen.org/ns/widgets'
    ET.register_namespace('', widget)
    ET.register_namespace('tizen', tizen)
    config = ET.fromstring(files['config.xml'])
    app = config.find('{' + tizen + '}application')
    app.set('id', args.package + '.App')
    app.set('package', args.package)
    config.set('id', 'https://local.invalid/' + args.package)
    config.set('version', '1.0.0')
    config.find('{' + widget + '}name').text = args.name
    config.find('{' + widget + '}content').set('src', 'start.html')
    files['config.xml'] = ET.tostring(config, encoding='utf-8', xml_declaration=True)
    query = urlencode({'start': args.start, 'init': '1'})
    files['start.html'] = ('<!doctype html><meta charset="utf-8"><script>location.replace("index.html?'
                           + query + '");</script>').encode()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(args.output, 'x', zipfile.ZIP_DEFLATED) as target:
        for name, data in files.items():
            target.writestr(name, data)
    print(f'{args.output}: {args.package}.App (unsigned)')


if __name__ == '__main__':
    main()
