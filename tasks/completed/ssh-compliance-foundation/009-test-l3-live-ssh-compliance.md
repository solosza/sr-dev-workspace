# 009 — L3 Live SSH Compliance Test

**Type:** TEST
**Depends on:** 008

## Target
`D:\my_ai_projects\project_test_repos\isagawa-qa\platform-ssh-test`

## Requirements
Run the full compliance foundation test suite against a live SSH target.

Prerequisites:
- Docker container `platform-ssh-test-target` running on port 2222
- If not running, start it: `docker-compose -f _test/docker/docker-compose.yml up -d`

Run:
```bash
pytest framework/_reference/tests/test_compliance_foundation.py -v --rootdir=. --html=_test/compliance-foundation-report.html --self-contained-html
```

This exercises:
- ComplianceValidator unit tests (make_result schema, field types, fixture loading)
- ServiceValidator pgrep fallback (mocked)
- Live SSH compliance check (real connection to Docker container)
- Live batch executor framework grouping

All tests must pass. The HTML report is the L3 deliverable.

## Acceptance Criteria
- [ ] pytest exits 0 (all tests pass)
- [ ] `_test/compliance-foundation-report.html` exists

## Gates
TEST-01, TEST-02
