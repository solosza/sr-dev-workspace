# Phase 3: Sync Updated Spec to platform-ssh-test

**Status:** Depends on Phase 1 + Phase 2 completion

**Deliverable:** platform-ssh-test updated with new spec files, integration tests passing, agent can generate remaining validators from pattern

---

## Overview

Phase 1 updates the **public** platform-ssh spec with compliance infrastructure. Phase 3 syncs those updates back to the **test** platform-ssh-test repo to verify:

1. Updated spec still works in test environment
2. Fixtures integrate correctly with existing test framework
3. Agent can generate remaining 7 validators from the base pattern (proof of concept)

---

## Sync Tasks

### Task 1: Pull Updated Spec Files

Source: `D:\my_ai_projects\project_test_repos\platform-ssh` (after Phase 1)

Destination: `D:\my_ai_projects\project_test_repos\isagawa-qa\platform-ssh-test\framework\_reference\`

Files to sync:

| File | From | To | Action |
|------|------|-----|--------|
| `validators/compliance_validator.py` | platform-ssh | platform-ssh-test | Copy/merge |
| `validators/stig_validator.py` | platform-ssh | platform-ssh-test | Copy/merge |
| `tests/test_stig_validator.py` | platform-ssh | platform-ssh-test | Copy/merge |
| `validators/fixtures/` (all 8 JSON) | platform-ssh | platform-ssh-test | Verify byte-identical |
| `ssh_batch_executor.py` enhancements | platform-ssh | platform-ssh-test | Merge by_framework() function |
| `host_configs.json` enhancements | platform-ssh | platform-ssh-test | Merge frameworks field |

### Task 2: Verify Fixture Integrity

For each of the 8 fixtures:

```bash
# Byte-for-byte comparison
cmp platform-ssh/validators/fixtures/STIG_rules.json \
    platform-ssh-test/framework/_reference/fixtures/stig_rules.json
```

Expected: Files identical (no diffs)

### Task 3: Test Spec Integration

Run test suite in platform-ssh-test:

```bash
cd platform-ssh-test
python -m pytest tests/test_stig_validator.py -v
```

Expected: All tests pass

### Task 4: Verify Validator Instantiation

In Python REPL or script:

```python
from framework._reference.validators import STIGValidator

# Can instantiate
validator = STIGValidator()

# Can run check()
config = {...}
violations = validator.check(config)

# Results are correct type
assert isinstance(violations, list)
```

Expected: No errors, validator works

### Task 5: Verify by_framework() Integration

Test the enhanced orchestrator:

```python
from framework._reference.ssh_batch_executor import by_framework

results = [
    {'framework': 'STIG', 'rule_id': 'V-1234', 'message': 'Failed'},
    {'framework': 'CIS', 'rule_id': 'CIS-1.1', 'message': 'Failed'},
    {'framework': 'STIG', 'rule_id': 'V-5678', 'message': 'Passed'}
]

grouped = by_framework(results)
# Expected: {'STIG': [2 items], 'CIS': [1 item]}

assert 'STIG' in grouped
assert len(grouped['STIG']) == 2
assert len(grouped['CIS']) == 1
```

Expected: Grouping correct

### Task 6: Verify Host Config Schema

Load host_configs.json and verify frameworks field is optional:

```python
import json

with open('host_configs.json', 'r') as f:
    config = json.load(f)

# Check: hosts without frameworks still work (backward compat)
for host in config['hosts']:
    frameworks = host.get('frameworks', [])
    assert isinstance(frameworks, list)
```

Expected: Schema valid, backward compatible

### Task 7: Agent Generation Proof of Concept

**Goal:** Demonstrate agent can generate a second validator (e.g., CISValidator) from the STIG pattern

**Process:**

1. Read STIGValidator source code
2. Understand the pattern:
   - Inherit from ComplianceValidator
   - Define FRAMEWORK_NAME and RULES_FILE
   - Implement _check_rule() with framework-specific logic
3. Generate CISValidator as standalone script
4. Test: Instantiate CISValidator, run check()
5. Verify: Results are correct type, violations detected

**Template for generated CISValidator:**

```python
#!/usr/bin/env python3
"""CISValidator — CIS Benchmarks compliance validator."""

from compliance_validator import ComplianceValidator
from typing import Dict, Any

class CISValidator(ComplianceValidator):
    """
    Validate host config against CIS Benchmarks Level 1.

    CIS provides prescriptive hardening guidance. This validator checks essential rules.
    """

    FRAMEWORK_NAME = 'CIS'
    RULES_FILE = 'cis_l1_rules.json'

    def _check_rule(self, rule: Dict, config: Dict) -> str:
        """
        Check one CIS rule against host config.

        Returns violation message if failed, None if passed.
        """
        # Same pattern as STIGValidator, adapted for CIS
        rule_id = rule.get('id')
        check_type = rule.get('check_type')
        expected = rule.get('expected_value')

        if check_type == 'service_enabled':
            service = rule.get('parameter')
            is_enabled = config.get('services', {}).get(service, False)
            if not is_enabled:
                return f"CIS {rule_id}: Service '{service}' must be enabled"

        elif check_type == 'ssh_config':
            param = rule.get('parameter')
            ssh_config = config.get('ssh_config', {})
            actual = ssh_config.get(param)
            if actual != expected:
                return f"CIS {rule_id}: {param} must be '{expected}', got '{actual}'"

        return None

# Test it
if __name__ == '__main__':
    validator = CISValidator()
    print(f"CISValidator loaded with {len(validator.rules)} rules")
```

**Acceptance:** Agent can generate this code from STIGValidator pattern + rule it that generates 7 remaining validators in same manner

---

## Integration Test Plan

After syncing, run comprehensive integration test:

```
Test Suite: Compliance Validator Integration
├─ L1 Sanity (all files present)
├─ L2 Functionality (fixtures load, validators instantiate)
├─ L3 Integration
│  ├─ All validators run without conflicts
│  ├─ Fixtures don't interfere across validators
│  ├─ Results group correctly by framework
│  ├─ Backward compat verified (optional fields work)
│  └─ Generated validator (CIS) works as well as shipped (STIG)
└─ L4 End-to-End (workflow 03-05 simulation with real host config)
```

Expected: All tests pass

---

## Tasks for Phase 3 + Phase 4

| Task | Action |
|------|--------|
| 3.1 | Copy compliance_validator.py from platform-ssh to platform-ssh-test |
| 3.2 | Copy stig_validator.py from platform-ssh to platform-ssh-test |
| 3.3 | Copy test_stig_validator.py from platform-ssh to platform-ssh-test |
| 3.4 | Verify all 8 fixtures are byte-identical (compare platform-ssh ↔ platform-ssh-test) |
| 3.5 | Merge by_framework() function into platform-ssh-test ssh_batch_executor.py |
| 3.6 | Merge frameworks field into platform-ssh-test host_configs.json |
| 3.7 | Run pytest on test_stig_validator.py in platform-ssh-test context |
| 3.8 | Verify STIGValidator instantiates in platform-ssh-test environment |
| 3.9 | Verify by_framework() grouping works in platform-ssh-test context |
| 3.10 | Verify host_configs.json schema is backward compatible |
| 3.11 | Generate CISValidator from STIGValidator pattern (agent proof of concept) |
| 3.12 | Test CISValidator instantiation and check() call |
| 3.13 | Run full integration test suite (L1/L2/L3/L4) |
| 3.14 | Document all test results and any issues |
| 4.1 | Merge feature branch to origin/main in platform-ssh repo (after all testing passes) |

---

## Acceptance Criteria

- [ ] All files synced from platform-ssh to platform-ssh-test
- [ ] All 8 fixtures verified byte-identical
- [ ] test_stig_validator.py passes in platform-ssh-test environment
- [ ] STIGValidator instantiates without errors
- [ ] by_framework() grouping works correctly
- [ ] host_configs.json schema backward compatible
- [ ] Agent can generate CISValidator from pattern (proof of concept)
- [ ] CISValidator instantiates and runs successfully
- [ ] Full integration test suite passes (L1/L2/L3/L4)
- [ ] No cross-validator pollution or conflicts
- [ ] All 8 fixtures load simultaneously without issues

---

## Success Criteria

When Phase 3 completes successfully:

✅ **Hybrid architecture proven in production**
- ✅ 8 fixtures ship as-is (authoritative data)
- ✅ Base class + 1 example shipped (teaches pattern)
- ✅ Agent can generate remaining 7 validators (extensibility proven)
- ✅ All validators work together without conflicts
- ✅ Framework can be easily extended by agent without spec updates

✅ **Ready for next steps:**
- ✅ Backlog 089 (Universal Hook Validator System) can reference this as implementation proof
- ✅ Other domains can adopt pattern for their compliance needs
- ✅ Modular, extensible, and tested

---

## References

- Phase 1: Spec updates to platform-ssh
- Phase 2: Validation via /kernel/prod-test
- Backlog 089: Universal Hook Validator System (references this migration)
- Research: `projects/kernel-architecture/ssh-compliance-spec-decomposition.md`
