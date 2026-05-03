# 005 — L3 Live STIG Validation Test

**Type:** TEST
**Depends on:** 004

## Target
`D:\my_ai_projects\project_test_repos\isagawa-qa\platform-ssh-test`

## Requirements
Run the STIG validator test suite against a live SSH target.

Prerequisites:
- Docker container `platform-ssh-test-target` running on port 2222
- If not running, start it: `docker-compose -f _test/docker/docker-compose.yml up -d`

Run:
```bash
pytest framework/_reference/tests/test_stig_validator.py -v --rootdir=.
```

All tests must pass.

## Acceptance Criteria
- [ ] pytest exits 0 (all tests pass)

## Gates
TEST-01
