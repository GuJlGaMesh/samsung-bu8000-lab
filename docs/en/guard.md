# Read the Privacy Guard boot report

[README](../../README.en.md) · [Prepare the TV and computer](setup.md) · [Hide recommendations in Samsung Apps](smart-hub.md) · [Disable components and restore their original state](cleanup.md) · **Read the Privacy Guard boot report** · [Validation results](validation.md)

Temporary service masks disappear on restart. The helper reapplies seven masks, checks the services, writes a local report and exits. It expects the public profile’s baseline and four stop markers. Older backups have a different layout.

The cold-boot test used `Host PC IP = 127.0.0.1`. The report arrived about 85 seconds after startup. With the computer’s address the owner could use PC diagnostics, but automatic cleanup after a cold boot was not verified. The final configuration used the computer’s address.

Read `/home/owner/share/tvprivacyguard-status.json` and check its timestamp. `ok=true` describes the state at that instant. Save the report before manually starting the helper. Switching the host address to read it from a PC may require another restart. The public build stores reports on the TV, checks all 37 apps and cleans its own temporary files. It has been checked on a PC. For rollback use `restore.sh`, which disables `tvprivgrd1.svc` and restores flags and markers.
