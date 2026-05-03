# Gate Contract — SSH Compliance Testing Extension

## Verification Methods
→ [[references/verification-methods.md]]

## Structural Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| STRUCT-01 | Interface in correct dir | file_exists | `test -f framework/interfaces/ssh_interface.py` | Move file |
| STRUCT-02 | No interface in _reference | run_code | `! test -f framework/_reference/ssh_interface.py` | Delete old |
| STRUCT-03 | Top-level tests dir | file_exists | `test -d tests/` | Create dir |
| STRUCT-04 | conftest at top level | file_exists | `test -f tests/conftest.py` | Move file |
| STRUCT-05 | No conftest in _reference | run_code | `! test -f framework/_reference/tests/conftest.py` | Delete old |
| STRUCT-06 | Host configs in tests/data | file_exists | `test -f tests/data/host_configs.json` | Move file |
| STRUCT-07 | No fixtures in _reference | run_code | `! test -d framework/_reference/fixtures` | Delete old |
| STRUCT-08 | STIG fixture exists | file_exists | `test -f tests/data/compliance/stig-rocky9.json` | Create file |
| STRUCT-09 | CIS fixture exists | file_exists | `test -f tests/data/compliance/cis-rocky9-l1.json` | Create file |
| STRUCT-10 | NIST 800-171 fixture exists | file_exists | `test -f tests/data/compliance/nist-800-171.json` | Create file |
| STRUCT-11 | FIPS fixture exists | file_exists | `test -f tests/data/compliance/fips-140-3.json` | Create file |
| STRUCT-12 | CIQ RLC Pro client config | file_exists | `test -f tests/data/clients/ciq-rlc-pro.json` | Create file |
| STRUCT-13 | CIQ RLC Pro AI client config | file_exists | `test -f tests/data/clients/ciq-rlc-pro-ai.json` | Create file |
| STRUCT-14 | STIG validator exists | file_exists | `test -f framework/_reference/validators/stig_validator.py` | Create file |
| STRUCT-15 | CIS validator exists | file_exists | `test -f framework/_reference/validators/cis_validator.py` | Create file |
| STRUCT-16 | NIST 800-171 validator exists | file_exists | `test -f framework/_reference/validators/nist_800_171_validator.py` | Create file |
| STRUCT-17 | FIPS validator exists | file_exists | `test -f framework/_reference/validators/fips_validator.py` | Create file |
| STRUCT-18 | Compliance tasks exists | file_exists | `test -f framework/_reference/tasks/compliance_tasks.py` | Create file |
| STRUCT-19 | Compliance auditor exists | file_exists | `test -f framework/_reference/roles/compliance_auditor.py` | Create file |
| STRUCT-20 | Compliance test suite exists | file_exists | `test -f tests/test_compliance.py` | Create file |

## Build Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| BUILD-01 | STIG fixture has rules | grep | `grep -q '"rules"' tests/data/compliance/stig-rocky9.json` | Add rules |
| BUILD-02 | CIS fixture has benchmarks | grep | `grep -q '"benchmarks"' tests/data/compliance/cis-rocky9-l1.json` | Add benchmarks |
| BUILD-03 | NIST fixture has controls | grep | `grep -q '"controls"' tests/data/compliance/nist-800-171.json` | Add controls |
| BUILD-04 | FIPS fixture has checks | grep | `grep -q '"checks"' tests/data/compliance/fips-140-3.json` | Add checks |
| BUILD-05 | Client config has compliance_frameworks | grep | `grep -q '"compliance_frameworks"' tests/data/clients/ciq-rlc-pro.json` | Add field |
| BUILD-06 | STIG validator has validate method | grep | `grep -q 'def validate' framework/_reference/validators/stig_validator.py` | Add method |
| BUILD-07 | CIS validator has validate method | grep | `grep -q 'def validate' framework/_reference/validators/cis_validator.py` | Add method |
| BUILD-08 | NIST validator has validate method | grep | `grep -q 'def validate' framework/_reference/validators/nist_800_171_validator.py` | Add method |
| BUILD-09 | FIPS validator has validate method | grep | `grep -q 'def validate' framework/_reference/validators/fips_validator.py` | Add method |
| BUILD-10 | conftest has compliance_config fixture | grep | `grep -q 'compliance_config' tests/conftest.py` | Add fixture |
| BUILD-11 | conftest has client_config fixture | grep | `grep -q 'client_config' tests/conftest.py` | Add fixture |
| BUILD-12 | AI client config has compliance_frameworks | grep | `grep -q '"compliance_frameworks"' tests/data/clients/ciq-rlc-pro-ai.json` | Add field |
| BUILD-13 | Compliance tasks has entry point | grep | `grep -q 'class ComplianceTasks\|def run' framework/_reference/tasks/compliance_tasks.py` | Add class |
| BUILD-14 | Compliance auditor has entry point | grep | `grep -q 'class ComplianceAuditor\|def audit' framework/_reference/roles/compliance_auditor.py` | Add class |

## Functional Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| FUNC-01 | All JSON fixtures parse | run_code | `python -c "import json,glob; [json.load(open(f)) for f in glob.glob('tests/data/**/*.json',recursive=True)]"` exits 0 | Fix JSON |
| FUNC-02 | Compliance validators import | run_code | `python -c "import sys;sys.path.insert(0,'framework/_reference');from validators.stig_validator import STIGValidator"` exits 0 | Fix imports |
| FUNC-03 | Existing tests still pass | run_test | `pytest framework/_reference/tests/test_ssh_batch.py -v` exits 0 | Fix regression |
| FUNC-04 | Compliance tests pass | run_test | `pytest tests/test_compliance.py -v` exits 0 | Fix tests |

## Test Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| TEST-01 | L3 production test | run_test | Compliance audit against Docker+SSH Rocky target produces results with passed/failed counts | Fix validators |

## Documentation Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| DOC-01 | Validator catalog updated | grep | `grep -q 'stig_validator\|STIGValidator' references/validator-catalog.md` | Add entry |
| DOC-02 | FRAMEWORK.md updated | grep | `grep -q '[Cc]ompliance' FRAMEWORK.md` | Add section |
| DOC-03 | README.md updated | grep | `grep -q '[Cc]ompliance' README.md` | Add section |
