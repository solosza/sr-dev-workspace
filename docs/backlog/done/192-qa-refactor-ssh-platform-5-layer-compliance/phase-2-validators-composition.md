# Phase 2: Refactor Existing Validators to Composition

## Status
EXISTS — needs refactor (ABC inheritance → composition)

## Location
`platform-ssh/framework/_reference/validators/`

## Current State
- `compliance_validator.py` — 358-line ABC base class with `validate()`, `check_config_value()`, `check_service_status()`, etc.
- `stig_validator.py` — thin subclass of ComplianceValidator (19 lines)
- `config_validator.py` — 11 lines, compressed one-liner
- `kernel_validator.py` — 7 lines, compressed
- `package_validator.py` — 6 lines, compressed
- `service_validator.py` — 6 lines, compressed

## What Needs to Happen

### 2.1 Delete ComplianceValidator ABC
- Remove `compliance_validator.py` entirely
- No ABC, no inheritance — composition only

### 2.2 Refactor STIGValidator to Standalone
- Constructor takes SSHInterface only (composition)
- Load rule fixtures from JSON in constructor (externalized identifiers)
- Atomic methods: one check per method (`check_protocol()`, `check_key_exchange()`, etc.)
- State-check methods return bool/primitive (`is_compliant()`, `get_score()`)
- Action methods return `self` for chaining
- Full docstrings, type hints, section headers
- No decorators (Layer 2 rule)

### 2.3 Refactor ConfigValidator, KernelValidator, PackageValidator, ServiceValidator
- Same pattern as STIGValidator
- Each standalone, takes SSHInterface
- Identifiers as class-level constants (these have few enough to be inline)
- One atomic operation per method
- Domain vocabulary in method names

## Dependencies
- Phase 1 (SSHInterface must exist first)

## Contract Rules
- Layer 2, Rules 1-7
- Global Rule #6: composition over inheritance
- Layer 2 Rule #3: identifiers as class-level constants or externalized fixtures
