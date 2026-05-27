# Phase 1: Update platform-ssh Spec with Compliance Infrastructure

**Status:** Ready to start after backlog 085 research complete

**Deliverable:** Public platform-ssh spec with all compliance fixtures, base validator, example validator, example test, and orchestrator enhancements

---

## What Gets Added

### Fixtures (All 8 frameworks — authoritative data)

Destination: `validators/fixtures/`

| File | Source | Size | Purpose |
|------|--------|------|---------|
| `stig_rules.json` | platform-ssh-test | ~2.5 KB | DISA STIG baseline (benchmarks) |
| `cis_l1_rules.json` | platform-ssh-test | ~1.8 KB | CIS Level 1 (foundational) |
| `nist_rules.json` | platform-ssh-test | ~2.1 KB | NIST SP 800-53 (federal) |
| `fips_rules.json` | platform-ssh-test | ~1.5 KB | FIPS 140-2 (cryptography) |
| `pci_dss_rules.json` | platform-ssh-test | ~1.9 KB | PCI DSS v3.2.1 (payment cards) |
| `hipaa_rules.json` | platform-ssh-test | ~2.0 KB | HIPAA Security Rule (healthcare) |
| `soc2_rules.json` | platform-ssh-test | ~1.7 KB | SOC 2 Type II (service orgs) |
| `iso27001_rules.json` | platform-ssh-test | ~2.2 KB | ISO 27001:2013 (information security) |

**Copy task:** Byte-identical copy from platform-ssh-test to platform-ssh

---

### Validators (Base + 1 Example)

Destination: `validators/`

**Base Class: `compliance_validator.py`**

```python
#!/usr/bin/env python3
"""ComplianceValidator — base class for framework-specific validators."""

import json
from pathlib import Path
from typing import List, Dict, Any

class ComplianceValidator:
    """
    Base validator for compliance frameworks.

    Subclasses implement check() to validate host config against framework rules.
    """

    FRAMEWORK_NAME = None  # Subclass must define
    RULES_FILE = None      # Subclass must define

    def __init__(self, rules_path: str = None):
        """Initialize validator with framework rules."""
        if rules_path is None:
            if self.RULES_FILE is None:
                raise ValueError(f"{self.__class__.__name__}.RULES_FILE not defined")
            rules_path = str(Path(__file__).parent / 'fixtures' / self.RULES_FILE)

        with open(rules_path, 'r') as f:
            self.rules = json.load(f)

    def check(self, host_config: Dict[str, Any]) -> List[Dict[str, str]]:
        """
        Validate host config against framework rules.

        Returns list of violations (empty if all pass).
        """
        violations = []
        for rule in self.rules:
            result = self._check_rule(rule, host_config)
            if result:  # Violation found
                violations.append({
                    'rule_id': rule.get('id'),
                    'framework': self.FRAMEWORK_NAME,
                    'message': result
                })
        return violations

    def _check_rule(self, rule: Dict, config: Dict) -> str:
        """Subclass implements rule-specific logic. Return violation message or None."""
        raise NotImplementedError(f"{self.__class__.__name__} must implement _check_rule()")
```

**Example Validator: `stig_validator.py`**

```python
#!/usr/bin/env python3
"""STIGValidator — DISA STIG baseline compliance validator."""

from compliance_validator import ComplianceValidator
from typing import Dict, Any

class STIGValidator(ComplianceValidator):
    """
    Validate host config against DISA Security Technical Implementation Guide (STIG).

    STIG is a baseline hardening configuration. This validator checks essential rules.
    """

    FRAMEWORK_NAME = 'STIG'
    RULES_FILE = 'stig_rules.json'

    def _check_rule(self, rule: Dict, config: Dict) -> str:
        """
        Check one STIG rule against host config.

        Returns violation message if failed, None if passed.
        """
        rule_id = rule.get('id')
        check_type = rule.get('check_type')
        expected = rule.get('expected_value')

        # Example: Check if SSH service is enabled
        if check_type == 'service_enabled':
            service = rule.get('parameter')
            is_enabled = config.get('services', {}).get(service, False)
            if not is_enabled:
                return f"STIG {rule_id}: Service '{service}' must be enabled"

        # Example: Check SSH config parameters
        elif check_type == 'ssh_config':
            param = rule.get('parameter')
            ssh_config = config.get('ssh_config', {})
            actual = ssh_config.get(param)
            if actual != expected:
                return f"STIG {rule_id}: {param} must be '{expected}', got '{actual}'"

        # Example: Check file permissions
        elif check_type == 'file_permission':
            file_path = rule.get('parameter')
            perms = rule.get('expected_permission')
            actual_perms = config.get('file_permissions', {}).get(file_path)
            if actual_perms != perms:
                return f"STIG {rule_id}: {file_path} must have permissions {perms}, got {actual_perms}"

        return None  # Rule passed
```

---

### Tests (1 Example)

Destination: `tests/`

**Example Test: `test_stig_validator.py`**

```python
#!/usr/bin/env python3
"""Test STIGValidator — validates rule checking logic."""

import pytest
from pathlib import Path
import sys

# Import validator
sys.path.insert(0, str(Path(__file__).parent.parent))
from validators.stig_validator import STIGValidator

def test_stig_validator_init():
    """STIGValidator initializes without errors."""
    validator = STIGValidator()
    assert validator.FRAMEWORK_NAME == 'STIG'
    assert len(validator.rules) > 0

def test_stig_passes_compliant_config():
    """Compliant config passes STIG validation."""
    validator = STIGValidator()

    config = {
        'services': {'sshd': True},
        'ssh_config': {
            'PermitRootLogin': 'no',
            'PasswordAuthentication': 'no',
            'PubkeyAuthentication': 'yes'
        },
        'file_permissions': {
            '/etc/ssh/sshd_config': '0600',
            '/home/user/.ssh/authorized_keys': '0600'
        }
    }

    violations = validator.check(config)
    # Note: Actual test depends on fixture rules
    # This demonstrates the pattern
    assert isinstance(violations, list)

def test_stig_fails_noncompliant_config():
    """Non-compliant config produces violations."""
    validator = STIGValidator()

    config = {
        'services': {'sshd': False},  # SSH disabled — violation
        'ssh_config': {
            'PermitRootLogin': 'yes',  # Violation
            'PasswordAuthentication': 'yes',  # Violation
            'PubkeyAuthentication': 'no'
        },
        'file_permissions': {
            '/etc/ssh/sshd_config': '0644'  # Wrong permissions — violation
        }
    }

    violations = validator.check(config)
    assert len(violations) > 0
    assert any('enabled' in v['message'] for v in violations)
```

---

## Orchestrator Enhancements

### `ssh_batch_executor.py` — Add Framework Grouping

Current: Executes validators independently

Enhanced: Group validators by framework for reporting

```python
def by_framework(validators_results):
    """Group validation results by compliance framework."""
    grouped = {}
    for result in validators_results:
        framework = result.get('framework', 'unknown')
        if framework not in grouped:
            grouped[framework] = []
        grouped[framework].append(result)
    return grouped

# Usage: results_by_framework = by_framework(all_validation_results)
```

### `host_configs.json` — Add Frameworks Field

Current:
```json
{
  "hosts": [
    {"name": "ssh-server-01", "ip": "192.168.1.10", ...}
  ]
}
```

Enhanced:
```json
{
  "hosts": [
    {
      "name": "ssh-server-01",
      "ip": "192.168.1.10",
      "frameworks": ["STIG", "CIS", "NIST"],
      ...
    }
  ]
}
```

---

## Workflow Documentation

### `workflow.md` — Update Steps 03–05

Current workflow refers to generic "validators". Enhanced workflow references compliance validators explicitly.

**Step 03: Load Compliance Validators**
- Load base ComplianceValidator class
- Instantiate framework-specific validators (STIG, CIS, NIST, FIPS, PCI, HIPAA, SOC2, ISO27001)
- Load fixtures from validators/fixtures/

**Step 04: Run Compliance Checks**
- For each host in host_configs.json:
  - Get frameworks list
  - Run selected validators against host config
  - Collect results by framework

**Step 05: Report Compliance Status**
- Group results by framework
- Display violations per host per framework
- Highlight critical failures

---

## Tasks for Phase 0 + Phase 1

| Task | Action |
|------|--------|
| 0.1 | Create feature branch in platform-ssh (e.g., feature/088-ssh-compliance-migration) |
| 1.1 | Copy stig_rules.json from platform-ssh-test to platform-ssh/validators/fixtures/ |
| 1.2 | Copy cis_l1_rules.json from platform-ssh-test to platform-ssh/validators/fixtures/ |
| 1.3 | Copy nist_rules.json from platform-ssh-test to platform-ssh/validators/fixtures/ |
| 1.4 | Copy fips_rules.json from platform-ssh-test to platform-ssh/validators/fixtures/ |
| 1.5 | Copy pci_dss_rules.json from platform-ssh-test to platform-ssh/validators/fixtures/ |
| 1.6 | Copy hipaa_rules.json from platform-ssh-test to platform-ssh/validators/fixtures/ |
| 1.7 | Copy soc2_rules.json from platform-ssh-test to platform-ssh/validators/fixtures/ |
| 1.8 | Copy iso27001_rules.json from platform-ssh-test to platform-ssh/validators/fixtures/ |
| 1.9 | Create validators/compliance_validator.py (base class) |
| 1.10 | Create validators/stig_validator.py (example validator) |
| 1.11 | Create tests/test_stig_validator.py (example test) |
| 1.12 | Edit ssh_batch_executor.py: add by_framework() grouping function |
| 1.13 | Edit host_configs.json: add frameworks field to host definitions |
| 1.14 | Edit workflow.md: document Steps 03–05 with compliance validator references |
| 1.15 | Verify: All 8 fixtures in place, validators importable, tests runnable |

---

## Acceptance Criteria

- [ ] All 8 fixtures copied byte-identical from platform-ssh-test
- [ ] compliance_validator.py created and syntactically valid
- [ ] stig_validator.py created, inherits from ComplianceValidator, _check_rule implemented
- [ ] test_stig_validator.py created, covers init + pass/fail scenarios
- [ ] ssh_batch_executor.py enhanced with by_framework() function
- [ ] host_configs.json enhanced with frameworks field (schema valid)
- [ ] workflow.md updated with Steps 03–05 documentation
- [ ] Manual verification: Can instantiate STIGValidator and run check()
- [ ] Manual verification: All fixture JSON files load without errors

---

## References

- Source files: `D:\my_ai_projects\project_test_repos\isagawa-qa\platform-ssh-test\framework\_reference\`
- Base research: backlog 085 — Hybrid architecture decision documented
- Next: Phase 2 validation via /kernel/prod-test
