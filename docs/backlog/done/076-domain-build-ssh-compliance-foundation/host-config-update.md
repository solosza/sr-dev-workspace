# Host Config Frameworks Field

## Status
EXISTS — needs enhancement

## Location
`framework/_reference/fixtures/host_configs.json`

## Current Format
```json
{
  "rlc_pro": {
    "host": "192.168.1.100",
    "port": 22,
    "username": "admin",
    "key_path": "/key",
    "variant": "rlc-pro",
    "expected_packages": ["bash", "rocky-release"],
    "expected_services": ["sshd", "chronyd"]
  }
}
```

## Enhanced Format
```json
{
  "rlc_pro": {
    "host": "192.168.1.100",
    "port": 22,
    "username": "admin",
    "key_path": "/key",
    "variant": "rlc-pro",
    "frameworks": ["stig", "cis_l1", "fips", "nist"],
    "expected_packages": ["bash", "rocky-release"],
    "expected_services": ["sshd", "chronyd"]
  }
}
```

## What Changes
- Add `frameworks` array — list of framework IDs to validate against
- Batch executor reads this to select which compliance validators to run
- Empty or missing `frameworks` = run generic validators only (backward compatible)

## Dependencies
- Batch executor update (must read the new field)
