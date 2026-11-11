# Validation results

[README](../../README.en.md) · [Prepare the TV and computer](setup.md) · [Hide recommendations in Samsung Apps](smart-hub.md) · [Disable components and restore their original state](cleanup.md) · [Read the Privacy Guard boot report](guard.md) · **Validation results**

On 10 November 2026, three Python tests passed on the PC. Unknown binaries were rejected in both directions, protected apps could not enter the disable list and shell metacharacters were rejected in profile identifiers. Applying and reversing the Apps patch reproduced the original DLL byte for byte.

The Windows transport patch matched the pinned source. Both .NET payloads built successfully. The unsigned package passed ZIP and XML checks. The .NET Core 3.1 support warning corresponds to the runtime on this TV.

CI runs the Python tests, generates scripts, checks shell and JavaScript syntax and scans published files. Local links were checked and the publication tree was reviewed for private data. The device record below comes from the earlier cold boot. The published tools were checked locally.

[cold-boot-sanitized.json](../../evidence/cold-boot-sanitized.json)
