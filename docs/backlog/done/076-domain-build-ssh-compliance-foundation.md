# Build SSH Compliance Foundation

## Status
Open

## Priority
High — blocks all 8 framework validators (077-084)

## Summary
Enhance the platform-ssh domain spec with a compliance-ready foundation: enhanced result schema with rule IDs, severity, and remediation; a base `ComplianceValidator` class; ServiceValidator systemd fallback for containers; host config `frameworks` field; and updated batch executor for framework-aware reporting.

## Design Documents

| Document | Purpose |
|----------|---------|
| [[076-domain-build-ssh-compliance-foundation/result-schema]] | Enhanced result format with rule_id, framework, severity, remediation |
| [[076-domain-build-ssh-compliance-foundation/base-compliance-validator]] | Abstract base class all 8 framework validators inherit from |
| [[076-domain-build-ssh-compliance-foundation/service-validator-fix]] | Systemd fallback for container environments |
| [[076-domain-build-ssh-compliance-foundation/host-config-update]] | Add frameworks field to host_configs.json |
| [[076-domain-build-ssh-compliance-foundation/batch-executor-update]] | Framework-aware reporting in SSHBatchExecutor |

## Requirements
- All changes go into the test repo `isagawa-qa/platform-ssh-test`
- Must not break existing 4 validators (Package, Kernel, Service, Config)
- Existing pytest suite must still pass
- Foundation must be complete before any framework validator (077-084) can start

## References
- Source repo: `isagawa-qa/platform-ssh` (original — don't touch until tested)
- Test repo: `D:\my_ai_projects\project_test_repos\isagawa-qa\platform-ssh-test`
- Prod-test report: `platform-ssh-test/_test/prod-test-report.html`
- Showcase page: `isagawa-co.github.io/ssh-compliance.html`
- Depends on: nothing
- Blocks: 077, 078, 079, 080, 081, 082, 083, 084

## Task Builder Input
- **Deliverable:** Enhanced result schema, ComplianceValidator base class, ServiceValidator fix, host config update, batch executor update
- **Location:** `new-repo:D:\my_ai_projects\project_test_repos\isagawa-qa\platform-ssh-test`
- **Scope:** BUILD
- **Constraints:** Must preserve backward compatibility with existing validators and tests
