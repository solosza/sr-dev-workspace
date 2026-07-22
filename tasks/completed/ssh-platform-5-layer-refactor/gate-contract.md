# Gate Contract — SSH Platform 5-Layer Refactor

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| BUILD-01 | autologger.py exists | file_exists | `test -f framework/_reference/utilities/autologger.py` | Create file |
| BUILD-02 | autologger has automation_logger | grep | `grep -q 'def automation_logger' framework/_reference/utilities/autologger.py` | Fix function |
| BUILD-03 | ssh_interface.py has docstrings | grep | `grep -q '"""' framework/_reference/ssh_interface.py` | Add docstrings |
| BUILD-04 | ssh_interface.py has type hints | grep | `grep -q 'def execute_command.*->.*:' framework/_reference/ssh_interface.py` | Add type hints |
| BUILD-05 | ssh_interface.py has logger | grep | `grep -q 'self.logger' framework/_reference/ssh_interface.py` | Add logging |
| BUILD-06 | compliance_validator.py deleted | run_code | `! test -f framework/_reference/validators/compliance_validator.py` | Delete file |
| BUILD-07 | stig_validator.py standalone | grep | `grep -q 'class STIGValidator' framework/_reference/validators/stig_validator.py && ! grep -q 'ComplianceValidator' framework/_reference/validators/stig_validator.py` | Remove inheritance |
| BUILD-08 | stig_validator.py has SSHInterface param | grep | `grep -q 'ssh.*SSHInterface' framework/_reference/validators/stig_validator.py` | Fix constructor |
| BUILD-09 | All 12 validators exist | run_code | `ls framework/_reference/validators/{stig,cis,fips,nist,pci_dss,hipaa,soc2,iso27001,config,kernel,package,service}_validator.py 2>/dev/null \| wc -l` returns 12 | Create missing |
| BUILD-10 | Task layer is class-based | grep | `grep -q 'class ComplianceTask' framework/_reference/tasks/run_ssh_command.py` | Refactor to class |
| BUILD-11 | Task has @automation_logger | grep | `grep -q '@automation_logger' framework/_reference/tasks/run_ssh_command.py` | Add decorator |
| BUILD-12 | Role has @automation_logger | grep | `grep -q '@automation_logger' framework/_reference/roles/ssh_batch_executor.py` | Add decorator |
| BUILD-13 | Role does not store self.ssh | run_code | `! grep -q 'self\.ssh\s*=' framework/_reference/roles/ssh_batch_executor.py` | Remove self.ssh |
| BUILD-14 | conftest has setup fixture | grep | `grep -q 'def setup' framework/_reference/tests/conftest.py` | Add fixture |
| BUILD-15 | test_stig is class-based AAA | grep | `grep -q 'class Test' framework/_reference/tests/test_stig_validator.py` | Refactor to class |
| FUNC-01 | All imports resolve | run_test | `cd framework/_reference && python -c "from utilities.autologger import automation_logger; from ssh_interface import SSHInterface; from validators.stig_validator import STIGValidator"` exits 0 | Fix imports |
| TEST-01 | pytest collects all tests | run_test | `pytest framework/_reference/tests/ --collect-only --rootdir=D:/my_ai_projects/project_test_repos/platform-ssh` exits 0 | Fix collection errors |
| TEST-02 | All tests pass | run_test | `pytest framework/_reference/tests/ -v --rootdir=D:/my_ai_projects/project_test_repos/platform-ssh` exits 0 | Fix failing tests |
