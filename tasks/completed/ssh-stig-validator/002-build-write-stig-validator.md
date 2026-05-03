# 002 — Write STIGValidator Class

**Type:** BUILD
**Depends on:** 001

## Target
`D:\my_ai_projects\project_test_repos\isagawa-qa\platform-ssh-test\framework\_reference\validators\stig_validator.py`

## Requirements
Write a STIG validator that inherits from ComplianceValidator.

```python
class STIGValidator(ComplianceValidator):
    FRAMEWORK = "DISA STIG"
    FRAMEWORK_ID = "stig"

    def default_rules(self):
        # Load from fixtures/stig_rules.json
        import json, os
        fixture_path = os.path.join(os.path.dirname(__file__), '..', 'fixtures', 'stig_rules.json')
        with open(fixture_path) as f:
            return json.load(f)
```

The validate() method is inherited from ComplianceValidator — no override needed since all rules use standard check types.

## Acceptance Criteria
- [ ] `framework/_reference/validators/stig_validator.py` exists
- [ ] File contains `class STIGValidator(ComplianceValidator)`

## Gates
BUILD-03, BUILD-04, BUILD-05
