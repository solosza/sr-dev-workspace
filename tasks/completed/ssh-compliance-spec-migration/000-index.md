# SSH Compliance Spec Migration — Task Index

**Backlog:** docs/backlog/088-domain-build-ssh-compliance-spec-migration.md
**Type:** BUILD (cross-repo)
**Target:** D:\my_ai_projects\project_test_repos\isagawa-qa\platform-ssh
**Source:** D:\my_ai_projects\project_test_repos\isagawa-qa\platform-ssh-test

## Tasks

| # | Task | Type | Description |
|---|------|------|-------------|
| 001 | Create feature branch | BUILD | Create feature/088-ssh-compliance-migration branch in platform-ssh |
| 002 | Copy stig_rules.json | BUILD | Copy fixture from platform-ssh-test to platform-ssh |
| 003 | Copy cis_l1_rules.json | BUILD | Copy fixture from platform-ssh-test to platform-ssh |
| 004 | Copy nist_rules.json | BUILD | Copy fixture from platform-ssh-test to platform-ssh |
| 005 | Copy fips_rules.json | BUILD | Copy fixture from platform-ssh-test to platform-ssh |
| 006 | Copy pci_dss_rules.json | BUILD | Copy fixture from platform-ssh-test to platform-ssh |
| 007 | Copy hipaa_rules.json | BUILD | Copy fixture from platform-ssh-test to platform-ssh |
| 008 | Copy soc2_rules.json | BUILD | Copy fixture from platform-ssh-test to platform-ssh |
| 009 | Copy iso27001_rules.json | BUILD | Copy fixture from platform-ssh-test to platform-ssh |
| 010 | Copy compliance_validator.py | BUILD | Copy base class from platform-ssh-test to platform-ssh |
| 011 | Copy stig_validator.py | BUILD | Copy example validator from platform-ssh-test to platform-ssh |
| 012 | Copy test_stig_validator.py | BUILD | Copy example test from platform-ssh-test to platform-ssh |
| 013 | Update ssh_batch_executor.py | BUILD | Replace with enhanced version from platform-ssh-test (by_framework grouping) |
| 014 | Update host_configs.json | BUILD | Replace with enhanced version from platform-ssh-test (frameworks field) |
| 015 | Update workflow.md | BUILD | Add compliance validator references to steps 03-05 |
| 016 | Validate spec (L1/L2) | TEST | Verify all files present, importable, validators instantiate |
| 017 | Commit and merge | BUILD | Commit on feature branch, merge to main |
