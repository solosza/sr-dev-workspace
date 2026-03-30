# Gate Contract — SSH Image Testing Platform

## Verification Methods
→ [[.claude/skills/task-builder/references/verification-methods.md]]

## Structural Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| BUILD-01 | Research doc exists | file_exists | `test -f docs/research/ciq-product-analysis.md` | Create doc |
| BUILD-02 | Research covers RLC Pro AI packages | grep | `grep -q 'CUDA\|PyTorch' docs/research/ciq-product-analysis.md` | Add content |
| BUILD-03 | requirements.txt has paramiko | grep | `grep -q 'paramiko' requirements.txt` | Add dep |
| BUILD-04 | FRAMEWORK.md exists | file_exists | `test -f FRAMEWORK.md` | Create file |
| BUILD-05 | SSH Interface file exists | file_exists | `test -f framework/_reference/ssh_interface.py` | Create file |
| BUILD-06 | SSHInterface class defined | grep | `grep -q 'class SSHInterface' framework/_reference/ssh_interface.py` | Add class |
| BUILD-07 | Retry logic present | grep | `grep -q 'retry' framework/_reference/ssh_interface.py` | Add retry |
| BUILD-08 | Validators directory exists | file_exists | `test -d framework/_reference/validators/` | Create dir |
| BUILD-09 | Package validator exists | file_exists | `test -f framework/_reference/validators/package_validator.py` | Create file |
| BUILD-10 | Kernel validator exists | file_exists | `test -f framework/_reference/validators/kernel_validator.py` | Create file |
| BUILD-11 | Service validator exists | file_exists | `test -f framework/_reference/validators/service_validator.py` | Create file |
| BUILD-12 | Config validator exists | file_exists | `test -f framework/_reference/validators/config_validator.py` | Create file |
| BUILD-13 | Task file exists | file_exists | `test -f framework/_reference/tasks/run_ssh_command.py` | Create file |
| BUILD-14 | Role file exists | file_exists | `test -f framework/_reference/roles/ssh_batch_executor.py` | Create file |
| BUILD-15 | Test file exists | file_exists | `test -f framework/_reference/tests/test_ssh_batch.py` | Create file |
| BUILD-16 | Conftest exists | file_exists | `test -f framework/_reference/tests/conftest.py` | Create file |
| BUILD-17 | Fixtures exist | file_exists | `test -f framework/_reference/fixtures/host_configs.json` | Create file |
| BUILD-18 | SKILL.md exists | file_exists | `test -f .claude/skills/ssh-management-layer/SKILL.md` | Create file |
| BUILD-19 | workflow.md exists | file_exists | `test -f .claude/skills/ssh-management-layer/workflow.md` | Create file |
| BUILD-20 | Spec gate contract exists | file_exists | `test -f .claude/skills/ssh-management-layer/gate-contract.md` | Create file |

## Functional Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| FUNC-01 | SSHInterface imports | run_code | `python -c "from framework._reference.ssh_interface import SSHInterface"` exits 0 | Fix imports |
| FUNC-02 | PackageValidator imports | run_code | `python -c "from framework._reference.validators.package_validator import PackageValidator"` exits 0 | Fix imports |
| FUNC-03 | Task imports | run_code | `python -c "from framework._reference.tasks.run_ssh_command import run_ssh_command"` exits 0 | Fix imports |
| FUNC-04 | Role imports | run_code | `python -c "from framework._reference.roles.ssh_batch_executor import SSHBatchExecutor"` exits 0 | Fix imports |
| FUNC-05 | Host config JSON valid | json_valid | `python -c "import json; json.load(open('framework/_reference/fixtures/host_configs.json'))"` | Fix JSON |
| TEST-01 | All unit tests pass | run_test | `pytest framework/_reference/tests/ -v` exits 0 | Fix tests |

## Integration Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| INT-01 | Kernel domain-setup discovers spec | run_code | Protocol file created after domain-setup in test workspace | Fix SKILL.md |
| INT-02 | Hooks fire in test workspace | run_code | actions_since_anchor increments after action | Fix hooks |
| INT-03 | Task completes under enforcement | run_code | Task cycling produces completed_tasks entry | Fix cycling |

## Documentation Gates

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| DOC-01 | README has install flow | grep | `grep -q 'install\|setup\|pip' README.md` | Add install |
| DOC-02 | FRAMEWORK explains 5 layers | grep | `grep -q 'Layer 1\|Interface\|Layer 5\|Test' FRAMEWORK.md` | Add layers |

## Summary
- Structural: 20 gates
- Functional: 6 gates
- Integration: 3 gates
- Documentation: 2 gates
- **Total: 31 gates**
