# Task 006: Copy pci_dss_rules.json

**Type:** BUILD
**Action:** Copy fixture from platform-ssh-test to platform-ssh

## What

```bash
cp "D:/my_ai_projects/project_test_repos/isagawa-qa/platform-ssh-test/framework/_reference/fixtures/pci_dss_rules.json" "D:/my_ai_projects/project_test_repos/isagawa-qa/platform-ssh/framework/_reference/fixtures/pci_dss_rules.json"
```

## Acceptance Criteria

- [ ] File exists at `platform-ssh/framework/_reference/fixtures/pci_dss_rules.json`
- [ ] File is byte-identical to source: `cmp` exits 0
