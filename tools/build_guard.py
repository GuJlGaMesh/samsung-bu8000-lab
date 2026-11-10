"""Build an unsigned, local-report-only helper. Does not sign, install or connect."""
import json
import shutil
import subprocess
import zipfile
from pathlib import Path
from generate_cleanup import generate

ROOT = Path(__file__).resolve().parents[1]


def main():
    build = ROOT / 'build/guard'
    build.mkdir(parents=True, exist_ok=True)
    shutil.copytree(ROOT / 'guard', build, dirs_exist_ok=True,
                    ignore=shutil.ignore_patterns('payload-src'))
    profile = json.loads((ROOT / 'profiles/bu8000-1720.7.json').read_text())
    (build / 'service/block-services.sh').write_text(
        generate(profile)['block-services.sh'], encoding='utf-8', newline='\n')
    payload = build / 'payload'
    payload.mkdir(exist_ok=True)
    for name in ('SamsungTvArchiveRoot', 'SamsungTvRootAgent'):
        project = ROOT / 'guard/payload-src' / (name + '.csproj')
        output = ROOT / 'build/payloads' / name
        subprocess.run(['dotnet', 'build', str(project), '-c', 'Release', '-o', str(output)], check=True)
        for suffix in ('.dll', '.deps.json'):
            shutil.copyfile(output / (name + suffix), payload / (name + suffix))
        config = {'runtimeOptions': {'tfm': 'netcoreapp3.1', 'rollForward': 'LatestPatch',
                  'framework': {'name': 'Microsoft.NETCore.App', 'version': '3.1.0'}}}
        (payload / (name + '.runtimeconfig.json')).write_text(json.dumps(config), encoding='utf-8')
    for name in ('Vetro-MIT.txt', 'samsung-tv-root-Unlicense.txt'):
        shutil.copyfile(ROOT / 'LICENSES' / name, build / name)
    (ROOT / 'dist').mkdir(exist_ok=True)
    package = ROOT / 'dist/tv-privacy-guard-unsigned.wgt'
    # Explicit allowlist: old build contents cannot silently enter the package.
    files = [build / n for n in ('config.xml', 'index.html', 'icon.png',
                                 'Vetro-MIT.txt', 'samsung-tv-root-Unlicense.txt')]
    files += [build / 'service' / n for n in ('main.js', 'block-services.sh', 'platform.js',
              'adb.js', 'sdb.js', 'tar.js', 'root-agent.js', 'debloat-commands.js')]
    files += [payload / (name + suffix) for name in ('SamsungTvArchiveRoot', 'SamsungTvRootAgent')
              for suffix in ('.dll', '.deps.json', '.runtimeconfig.json')]
    with zipfile.ZipFile(package, 'w', zipfile.ZIP_DEFLATED) as archive:
        for item in files:
            archive.write(item, item.relative_to(build).as_posix())
    with zipfile.ZipFile(package) as archive:
        if archive.testzip() is not None:
            raise RuntimeError('Corrupt package')
    print(package)


if __name__ == '__main__':
    main()
