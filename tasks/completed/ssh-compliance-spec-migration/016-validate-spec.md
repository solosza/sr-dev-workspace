# Task 016: Validate Spec (L1/L2)

**Type:** TEST
**Action:** Verify all files present, importable, validators instantiate

## What

### L1: Sanity — files exist

```bash
# All 8 compliance fixtures present
for f in stig_rules cis_l1_rules nist_rules fips_rules pci_dss_rules hipaa_rules soc2_rules iso27001_rules; do
  test -f "D:/my_ai_projects/project_test_repos/isagawa-qa/platform-ssh/framework/_reference/fixtures/${f}.json" && echo "OK: ${f}.json" || echo "FAIL: ${f}.json"
done

# Validators present
test -f "D:/my_ai_projects/project_test_repos/isagawa-qa/platform-ssh/framework/_reference/validators/compliance_validator.py" && echo "OK: compliance_validator.py" || echo "FAIL"
test -f "D:/my_ai_projects/project_test_repos/isagawa-qa/platform-ssh/framework/_reference/validators/stig_validator.py" && echo "OK: stig_validator.py" || echo "FAIL"

# Test present
test -f "D:/my_ai_projects/project_test_repos/isagawa-qa/platform-ssh/framework/_reference/tests/test_stig_validator.py" && echo "OK: test_stig_validator.py" || echo "FAIL"
```

### L2: Functionality — files are valid

```bash
# Python files compile
python -c "exec(open('D:/my_ai_projects/project_test_repos/isagawa-qa/platform-ssh/framework/_reference/validators/compliance_validator.py').read())" && echo "OK: compiles" || echo "FAIL: syntax error"

# JSON files parse
for f in stig_rules cis_l1_rules nist_rules fips_rules pci_dss_rules hipaa_rules soc2_rules iso27001_rules; do
  python -c "import json; json.load(open('D:/my_ai_projects/project_test_repos/isagawa-qa/platform-ssh/framework/_reference/fixtures/${f}.json'))" && echo "OK: ${f}.json" || echo "FAIL: ${f}.json"
done

# by_framework present in batch executor
grep -q 'by_framework' "D:/my_ai_projects/project_test_repos/isagawa-qa/platform-ssh/framework/_reference/roles/ssh_batch_executor.py" && echo "OK: by_framework" || echo "FAIL"

# frameworks field in host_configs
grep -q 'frameworks' "D:/my_ai_projects/project_test_repos/isagawa-qa/platform-ssh/framework/_reference/fixtures/host_configs.json" && echo "OK: frameworks" || echo "FAIL"
```

## Acceptance Criteria

- [ ] All 8 fixture JSONs present and valid
- [ ] compliance_validator.py and stig_validator.py compile without errors
- [ ] test_stig_validator.py present
- [ ] ssh_batch_executor.py has by_framework
- [ ] host_configs.json has frameworks field
