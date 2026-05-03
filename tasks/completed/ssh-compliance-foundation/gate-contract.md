# Gate Contract — SSH Compliance Foundation

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| BUILD-01 | ComplianceValidator base class exists | file_exists | `test -f framework/_reference/validators/compliance_validator.py` | Create file |
| BUILD-02 | Base class has FRAMEWORK attribute | grep | `grep -q 'FRAMEWORK =' framework/_reference/validators/compliance_validator.py` | Add attribute |
| BUILD-03 | Base class has make_result method | grep | `grep -q 'def make_result' framework/_reference/validators/compliance_validator.py` | Add method |
| BUILD-04 | Base class has check_config_value method | grep | `grep -q 'def check_config_value' framework/_reference/validators/compliance_validator.py` | Add method |
| BUILD-05 | Base class has validate method | grep | `grep -q 'def validate' framework/_reference/validators/compliance_validator.py` | Add method |
| BUILD-06 | ServiceValidator has pgrep fallback | grep | `grep -q 'pgrep' framework/_reference/validators/service_validator.py` | Add fallback |
| BUILD-07 | Host configs have frameworks field | grep | `grep -q 'frameworks' framework/_reference/fixtures/host_configs.json` | Add field |
| BUILD-08 | Batch executor has by_framework grouping | grep | `grep -q 'by_framework' framework/_reference/roles/ssh_batch_executor.py` | Add grouping |
| BUILD-09 | Test fixture exists | file_exists | `test -f framework/_reference/fixtures/compliance_rules_test.json` | Create file |
| BUILD-10 | Compliance test file exists | file_exists | `test -f framework/_reference/tests/test_compliance_foundation.py` | Create file |
| FUNC-01 | ComplianceValidator imports cleanly | run_code | `python -c "import sys; sys.path.insert(0,'framework/_reference'); from validators.compliance_validator import ComplianceValidator"` exits 0 | Fix imports |
| FUNC-02 | ServiceValidator imports cleanly | run_code | `python -c "import sys; sys.path.insert(0,'framework/_reference'); from validators.service_validator import ServiceValidator"` exits 0 | Fix imports |
| FUNC-03 | Batch executor imports cleanly | run_code | `python -c "import sys; sys.path.insert(0,'framework/_reference'); from roles.ssh_batch_executor import SSHBatchExecutor"` exits 0 | Fix imports |
| FUNC-04 | Test fixture is valid JSON | run_code | `python -c "import json; json.load(open('framework/_reference/fixtures/compliance_rules_test.json'))"` exits 0 | Fix JSON |
| TEST-01 | Compliance foundation tests pass | run_test | `pytest framework/_reference/tests/test_compliance_foundation.py -v --rootdir=.` exits 0 | Fix tests |
| TEST-02 | Live SSH compliance check passes | run_test | `pytest framework/_reference/tests/test_compliance_foundation.py -v -k live --rootdir=.` exits 0 | Fix live tests |
