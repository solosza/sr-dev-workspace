# Base ComplianceValidator Class

## Status
NEW

## Location
`framework/_reference/validators/compliance_validator.py`

## What It Does
Abstract base class that all 8 framework validators inherit from. Provides the enhanced result format, fixture loading, and common check patterns.

## Interface
```python
class ComplianceValidator:
    FRAMEWORK = ""        # e.g., "DISA STIG"
    FRAMEWORK_ID = ""     # e.g., "stig"

    def __init__(self, ssh, rules=None):
        self.ssh = ssh
        self.rules = rules or self.default_rules()

    def default_rules(self) -> list:
        """Load from fixture file. Override per framework."""
        ...

    def check_config_value(self, file, directive, expected, rule_id, severity):
        """Check that a config directive has the expected value."""
        ...

    def check_config_absent(self, file, directive, rule_id, severity):
        """Check that a config directive is NOT present."""
        ...

    def check_package_installed(self, package, rule_id, severity):
        """Check that a package is installed."""
        ...

    def check_service_status(self, service, expected_status, rule_id, severity):
        """Check service is active/inactive."""
        ...

    def make_result(self, rule_id, check, passed, expected, actual, evidence, severity, remediation):
        """Produce an enhanced result dict."""
        ...

    def validate(self) -> list:
        """Run all rules. Override per framework."""
        ...
```

## Key Design Decisions
- `check_config_value` does `grep` + parses the actual value, not just presence
- Each framework validator overrides `default_rules()` to load its fixture
- `make_result()` is the single point that produces the enhanced schema
- Rules are data-driven: list of dicts with `{rule_id, check_type, file, directive, expected, severity}`

## Dependencies
- Result schema (must be defined first)
