# 003 — Edit Host Configs: Add frameworks Field

**Type:** BUILD
**Depends on:** —

## Target
`D:\my_ai_projects\project_test_repos\isagawa-qa\platform-ssh-test\framework\_reference\fixtures\host_configs.json`

## Requirements
Add `frameworks` array to each host config entry. This field lists which compliance framework IDs to validate against.

For `rlc_pro`: `"frameworks": ["stig", "cis_l1", "fips", "nist"]`
For `rlc_pro_ai`: `"frameworks": ["stig", "cis_l1", "fips", "nist"]`

Empty or missing `frameworks` = run generic validators only (backward compatible).

## Acceptance Criteria
- [ ] `host_configs.json` contains `"frameworks"` field in both entries
- [ ] File is valid JSON

## Gates
BUILD-07
