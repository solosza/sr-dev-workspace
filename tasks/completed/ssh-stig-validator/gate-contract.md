# Gate Contract — SSH STIG Validator

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| BUILD-01 | STIG fixture exists | file_exists | `test -f framework/_reference/fixtures/stig_rules.json` | Create file |
| BUILD-02 | STIG fixture is valid JSON | run_code | `python -c "import json; json.load(open('framework/_reference/fixtures/stig_rules.json'))"` exits 0 | Fix JSON |
| BUILD-03 | STIG validator exists | file_exists | `test -f framework/_reference/validators/stig_validator.py` | Create file |
| BUILD-04 | STIG validator has class | grep | `grep -q 'class STIGValidator' framework/_reference/validators/stig_validator.py` | Add class |
| BUILD-05 | STIG validator inherits ComplianceValidator | grep | `grep -q 'ComplianceValidator' framework/_reference/validators/stig_validator.py` | Fix inheritance |
| BUILD-06 | STIG test file exists | file_exists | `test -f framework/_reference/tests/test_stig_validator.py` | Create file |
| FUNC-01 | STIG validator imports | run_code | `python -c "import sys; sys.path.insert(0,'framework/_reference'); from validators.stig_validator import STIGValidator"` exits 0 | Fix imports |
| TEST-01 | STIG tests pass | run_test | `pytest framework/_reference/tests/test_stig_validator.py -v --rootdir=.` exits 0 | Fix tests |
