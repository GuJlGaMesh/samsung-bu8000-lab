# Third-party code and assets

The repository's MIT license covers original documentation and tools. Upstream files retain their respective licenses. Samsung, Tizen and application names belong to their respective owners; this project is independent.

## Vetro — MIT

- Source: https://github.com/andrearicci93/vetro
- Pinned revision: `b05a374ac8396220795fe44321d415b26718a4fa`
- Included: `guard/service/adb.js`, `sdb.js`, `tar.js`, `root-agent.js`, `platform.js`, `debloat-commands.js`, and `guard/icon.png`.
- License: [LICENSES/Vetro-MIT.txt](LICENSES/Vetro-MIT.txt).
- Local adaptations include a separate log, avoiding cleanup of other tools' staging directories, and cleanup of the helper's own staging. The full launcher UI and Home replacement are not included.

## samsung-tv-root — Unlicense

- Source: https://github.com/chris-ritsen/samsung-tv-root
- Pinned revision: `3b97edf3762db7670585d73e29623dc56195bf98`
- Included: `guard/payload-src/SamsungTvArchiveRoot.cs` and `SamsungTvRootAgent.cs`.
- License: [LICENSES/samsung-tv-root-Unlicense.txt](LICENSES/samsung-tv-root-Unlicense.txt).
- Project files target the tested TV's .NET Core 3.1 runtime. `patches/sdb-windows.patch` adjusts script staging and LF handling in the separately cloned Python transport. The Python package and its dependencies are not vendored.

## Media Station X and Samsung files

The MSX shortcut builder consumes the owner's separately downloaded official WGT. The MSX loader, icons, signed packages and remote catalog contents are not distributed here. Their licenses are not replaced by this repository's MIT license.

The AppsCommon patch consumes the owner's exact-version Samsung DLL. Neither original nor modified Samsung DLLs or native images are distributed. Only the patch recipe and hashes are included.

SDB, Apps2Samsung, certificate tooling, Python, Node.js, .NET SDK and build dependencies are separate prerequisites. Private certificates and keys must never be committed.
