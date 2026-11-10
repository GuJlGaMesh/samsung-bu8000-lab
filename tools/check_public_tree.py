"""Check the Git publication tree, excluding ignored local build/private files."""
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FORBIDDEN_SUFFIXES = {'.p12', '.pfx', '.pem', '.key', '.token', '.wgt', '.tpk', '.dll', '.so', '.exe'}


def main():
    names = subprocess.check_output(['git', 'ls-files', '-z', '--cached', '--others', '--exclude-standard'],
                                    cwd=ROOT).decode().split('\0')
    errors = []
    patterns = [r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',
                r'gh[pousr]_[A-Za-z0-9]{30,}', r'github_pat_[A-Za-z0-9_]{40,}',
                r'(?i)(?:[0-9a-f]{2}:){5}[0-9a-f]{2}',
                r'(?i)[A-Z]:[\\/]Users[\\/][^\s"\x27]+',
                r'\b192\.168\.\d+\.\d+\b', r'\b10\.\d+\.\d+\.\d+\b']
    for name in set(filter(None, names)):
        path = ROOT / name
        if path.suffix.lower() in FORBIDDEN_SUFFIXES:
            errors.append(name + ': disallowed artifact')
        if path.suffix.lower() == '.png':
            continue
        try:
            value = path.read_text(encoding='utf-8-sig')
        except (UnicodeError, OSError):
            errors.append(name + ': unexpected binary or missing file')
            continue
        for pattern in patterns:
            if re.search(pattern, value):
                errors.append(name + ': possible private data; inspect locally')
    if errors:
        raise SystemExit('\n'.join(sorted(set(errors))))
    print('Publication tree checks passed; manual review is still required.')


if __name__ == '__main__':
    main()
