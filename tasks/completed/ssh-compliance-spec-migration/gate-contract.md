# Gate Contract — SSH Compliance Spec Migration

## Gates

| Gate | Criteria | Verification |
|------|----------|--------------|
| G1 | Feature branch exists in platform-ssh | `git -C [target] branch --list feature/088*` returns non-empty |
| G2 | All 8 fixture JSONs present | `ls [target]/framework/_reference/fixtures/*.json` shows 9 files (8 compliance + host_configs) |
| G3 | compliance_validator.py exists | `python -c "exec(open('[target]/framework/_reference/validators/compliance_validator.py').read())"` exits 0 |
| G4 | stig_validator.py exists | File present in validators/ |
| G5 | test_stig_validator.py exists | File present in tests/ |
| G6 | ssh_batch_executor.py has by_framework | `grep -q 'by_framework' [target]/framework/_reference/roles/ssh_batch_executor.py` exits 0 |
| G7 | host_configs.json has frameworks field | `grep -q 'frameworks' [target]/framework/_reference/fixtures/host_configs.json` exits 0 |
| G8 | All files byte-identical to source | `cmp` each file against platform-ssh-test source |
| G9 | Feature branch merged to main | `git -C [target] log --oneline -1` shows merge commit |

## Paths

- **Target repo:** `D:\my_ai_projects\project_test_repos\isagawa-qa\platform-ssh`
- **Source repo:** `D:\my_ai_projects\project_test_repos\isagawa-qa\platform-ssh-test`
- **Target validators:** `[target]/framework/_reference/validators/`
- **Target fixtures:** `[target]/framework/_reference/fixtures/`
- **Target tests:** `[target]/framework/_reference/tests/`
- **Source validators:** `[source]/framework/_reference/validators/`
- **Source fixtures:** `[source]/framework/_reference/fixtures/`
- **Source tests:** `[source]/framework/_reference/tests/`
