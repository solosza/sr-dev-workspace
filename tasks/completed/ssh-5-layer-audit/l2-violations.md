# L2 Metrics Compliance — Violations Report

**Platform:** SSH (`D:/my_ai_projects/project_test_repos/isagawa-qa/platform-ssh/`)
**Audited against:** platform-deepeval 5-layer reference checklist
**Date:** 2026-07-06

## L2 Layer Status

**The L2 (Metrics) layer is entirely absent.** No `metrics/` directory exists in the SSH platform.

## Closest Equivalent: `validators/`

The SSH platform has a `validators/` directory with 6 classes that perform validation logic — functionally similar to metrics but structurally non-conformant.

| Validator Class | File | Has `evaluate()` | Has `is_above_threshold()` | Has `get_score()` |
|----------------|------|:-:|:-:|:-:|
| ComplianceValidator (ABC) | `compliance_validator.py` | NO | NO | NO |
| STIGValidator | `stig_validator.py` | NO | NO | NO |
| KernelValidator | `kernel_validator.py` | NO | NO | NO |
| PackageValidator | `package_validator.py` | NO | NO | NO |
| ServiceValidator | `service_validator.py` | NO | NO | NO |
| ConfigValidator | `config_validator.py` | NO | NO | NO |

**All validators use `validate()` instead of L2 required methods.** None implement `evaluate()`, `is_above_threshold()`, `get_score()`, or `get_detail()`.

## Method Pattern Comparison

| L2 Reference Pattern | SSH Validator Pattern | Status |
|---------------------|----------------------|--------|
| `evaluate()` → returns self (fluent) | `validate()` → returns `List[Dict]` | FAIL — different name, return type, no fluent chaining |
| `is_above_threshold()` → bool | Not present | FAIL — no threshold checking |
| `get_score()` → numeric | Not present | FAIL — no scoring |
| `get_detail()` → dict | Not present | FAIL — no detail accessor |
| Module-level `METRIC_CRITERIA` dict | Not present | FAIL — no criteria constants |
| Module-level `METRIC_THRESHOLDS` dict | Not present | FAIL — no threshold constants |

## Import Direction Audit

| Check | Result |
|-------|--------|
| Validators import paramiko SDK directly? | NO — PASS |
| Validators import L1 (ssh_interface)? | NO — PASS (validators receive `ssh` object via constructor, don't import the module) |
| Validators import from higher layers (L3-L5)? | NO — PASS |
| Internal validator imports? | `stig_validator → compliance_validator` (intra-layer) — PASS |

**Import direction is clean** — no upward imports, no SDK leakage.

## Structural Violations

### V1: L2 layer completely missing

- **Expected:** `framework/_reference/metrics/` directory with metric classes
- **Actual:** No `metrics/` directory exists
- **Severity:** High (entire layer absent)
- **Remediation:** Create `metrics/` directory with metric classes wrapping validator logic, exposing `evaluate()`, `is_above_threshold()`, `get_score()`, `get_detail()`

### V2: Validators lack L2 method signatures

- **Expected:** `evaluate()`, `is_above_threshold()`, `get_score()`, `get_detail()` per class
- **Actual:** All 6 classes use only `validate()` returning `List[Dict]`
- **Severity:** High (no API conformance to L2 contract)
- **Remediation:** Either (a) add L2 methods to existing validators, or (b) create L2 metric wrappers that compose validators internally

### V3: No criteria or threshold constants

- **Expected:** Module-level `METRIC_CRITERIA` and `METRIC_THRESHOLDS` dicts
- **Actual:** No criteria/threshold constants anywhere in validators
- **Severity:** Medium (no declarative metric configuration)
- **Remediation:** Define threshold constants (e.g., minimum pass rate per validator type)

## Summary

| Check | Status | Details |
|-------|--------|---------|
| `metrics/` directory exists | FAIL | Entirely absent (V1) |
| Metric classes have `evaluate()` | FAIL | Validators use `validate()` instead (V2) |
| Metric classes have `is_above_threshold()` | FAIL | Not present (V2) |
| Metric classes have `get_score()` | FAIL | Not present (V2) |
| Criteria/threshold constants | FAIL | Not present (V3) |
| Import direction (L2 → L1 only) | PASS | No SDK or L1 imports in validators |
| No upward imports (L2 → L3+) | PASS | Clean import direction |

**Total violations: 3** (2 high, 1 medium)
**Import compliance: PASS** (despite structural non-conformance, import direction is correct)
