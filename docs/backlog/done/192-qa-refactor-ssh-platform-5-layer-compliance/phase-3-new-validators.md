# Phase 3: Build 7 Missing Compliance Validators

## Status
NEW — rule fixture JSON files exist on `feature/088-ssh-compliance-migration` branch, Python classes do not

## Location
`platform-ssh/framework/_reference/validators/`

## Validators to Build

| Validator | Fixture File | Framework |
|-----------|-------------|-----------|
| `cis_validator.py` | `cis_rules.json` | CIS Benchmarks |
| `fips_validator.py` | `fips_rules.json` | FIPS 140-3 |
| `nist_validator.py` | `nist_rules.json` | NIST 800-171 |
| `pci_dss_validator.py` | `pci_dss_rules.json` | PCI DSS |
| `hipaa_validator.py` | `hipaa_rules.json` | HIPAA |
| `soc2_validator.py` | `soc2_rules.json` | SOC 2 |
| `iso27001_validator.py` | `iso27001_rules.json` | ISO 27001 |

## What Needs to Happen

### For Each Validator
- Same structure as refactored STIGValidator (Phase 2 output)
- Constructor takes SSHInterface, loads rules from fixture JSON
- Module docstring, class docstring with layer rules
- Identifiers loaded from fixture in constructor
- Atomic check methods per rule category
- State-check methods: `is_compliant()`, `get_score()`, `get_findings()`
- Action methods return `self`
- Type hints, section headers, no decorators

### Fixture Files
- Pull from `feature/088-ssh-compliance-migration` branch
- Place in `framework/_reference/fixtures/`
- Each JSON has rule definitions with check commands, expected values, severity

## Dependencies
- Phase 2 (STIGValidator pattern established first)
- Feature branch `feature/088-ssh-compliance-migration` for fixture JSONs

## Contract Rules
- Layer 2, all rules
- Layer 2 Rule #3: fixture file externalization clause
