# Refactor SSH Platform to 5-Layer Compliance

## Status
Open

## Priority
High — platform-ssh has 0 PASS / 8 FAIL files against the 5-layer contract. Every layer has structural violations.

## Summary
The SSH compliance platform (`platform-ssh`) was built before the 5-layer contract was codified. A `/check-5-layer` audit found zero compliant files. This backlog covers a full structural refactor: rewriting every layer to match the contract, refactoring ABC inheritance to composition, building 7 missing validator Components, and rewriting tests to class-based AAA.

## Requirements
- Rewrite `ssh_interface.py` with docstrings, type hints, logging, constructor contract (SDK + config + logger)
- Add `autologger.py` utility (same implementation as all platforms)
- Refactor `ComplianceValidator` from ABC inheritance to composition — each validator standalone
- Build 7 missing validator Components (CIS, FIPS, NIST 800-171, PCI DSS, HIPAA, SOC 2, ISO 27001) — rule fixture JSON files exist on `feature/088-ssh-compliance-migration` branch
- Refactor existing thin validators (config, kernel, package, service) to full Components with docstrings, type hints, identifiers as class constants
- Refactor `run_ssh_command.py` from function to class-based Task with `@automation_logger("Task")` decorator
- Refactor `SSHBatchExecutor` Role with decorators, `None` returns, no `self.ssh` store (pass-through only)
- Rewrite tests to class-based AAA with `@pytest.fixture(autouse=True)` setup, `@automation_logger("Test")`, `@pytest.mark` tags
- Run `/check-5-layer` after refactor to verify compliance

## Design Documents

| Document | Purpose |
|----------|---------|
| [[192-qa-refactor-ssh-platform-5-layer-compliance/phase-1-interface-autologger]] | Rewrite Interface + add autologger utility |
| [[192-qa-refactor-ssh-platform-5-layer-compliance/phase-2-validators-composition]] | Refactor ComplianceValidator ABC to composition, fix existing validators |
| [[192-qa-refactor-ssh-platform-5-layer-compliance/phase-3-new-validators]] | Build 7 missing compliance validator Components |
| [[192-qa-refactor-ssh-platform-5-layer-compliance/phase-4-task-role]] | Refactor Task + Role layers |
| [[192-qa-refactor-ssh-platform-5-layer-compliance/phase-5-tests]] | Rewrite tests to class-based AAA |

## Architecture

```
Layer 1: SSHInterface (wraps Paramiko — execute_command, upload_file, download_file)
    ↑
Layer 2: STIGValidator, CISValidator, FIPSValidator, NISTValidator,
         PCIDSSValidator, HIPAAValidator, SOC2Validator, ISO27001Validator,
         ConfigValidator, KernelValidator, PackageValidator, ServiceValidator
         (each standalone, takes SSHInterface, loads fixture JSON for identifiers)
    ↑
Layer 3: ComplianceTask (runs one validator scan), SSHCommandTask (runs one command)
    ↑
Layer 4: SSHBatchExecutor (orchestrates multiple Tasks across validators)
    ↑
Layer 5: Tests (class-based AAA, fixtures wire SSHInterface + config)
```

## References
- `/check-5-layer` compliance report from this session (8 FAIL, 0 PASS)
- 5-layer-contract.md v1.0 (`.claude/docs/design/check-5-layer/references/5-layer-contract.md`)
- `feature/088-ssh-compliance-migration` branch has all 8 rule fixture JSON files
- platform-selenium `_reference/` as the gold standard for 5-layer compliance

## Task Builder Input
- **Deliverable:** Fully 5-layer compliant SSH platform (`_reference/` directory)
- **Location:** `new-repo:D:\my_ai_projects\project_test_repos\platform-ssh`
- **Scope:** REFACTOR
- **Constraints:** Must pass `/check-5-layer` audit. Rule fixture JSONs on feature branch. MockSSH in conftest for testing. Composition only — no ABC inheritance.
