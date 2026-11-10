"""Explicit owner-authorized script execution through a pinned upstream transport."""
import argparse
import asyncio
import base64
import ipaddress
import json
import os
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--tv', required=True)
    parser.add_argument('--pc', required=True)
    parser.add_argument('--upstream', type=Path, required=True)
    parser.add_argument('--sdb', type=Path, required=True)
    parser.add_argument('--script', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--root', action='store_true')
    parser.add_argument('--timeout', type=int, default=90)
    args = parser.parse_args()
    for address in (args.tv, args.pc):
        ipaddress.ip_address(address)
    os.environ['PATH'] = str(args.sdb.resolve().parent) + os.pathsep + os.environ['PATH']
    sys.path.insert(0, str(args.upstream.resolve() / 'src'))
    script = args.script.read_text(encoding='utf-8-sig').strip()
    if args.root:
        from samsung_tv_root.archive_root import probe
        command = 'printf %s ' + base64.b64encode(script.encode()).decode() + ' | base64 -d | sh'
        payload = Path(__file__).resolve().parents[1] / 'build/guard/payload'
        result = asyncio.run(probe(args.tv, model='UE55BU8000UCCE', callback_host=args.pc,
            commands=(command,), payloads=payload, command_timeout=args.timeout))
        commands = result.get('commands', [])
        ok = result.get('authenticated') is True and result.get('uid') == 0 and len(commands) == 1
        ok = ok and all(c.get('exit_code') == 0 and not c.get('timed_out') for c in commands)
    else:
        from samsung_tv_root.sdb import SdbClient
        client = SdbClient(args.sdb, args.tv)
        client.require_device()
        capture = client.capture(script, callback_host=args.pc, timeout=args.timeout)
        result = {'output': capture.output}
        ok = capture.output.rstrip().endswith('[exit:0]')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    # Result can contain private identifiers: save locally, never dump or upload automatically.
    print(f'Result saved to {args.output}; success={ok}')
    return 0 if ok else 1


if __name__ == '__main__':
    raise SystemExit(main())
