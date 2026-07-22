# SOAP Tests — Design Doc

## Governing Contract

`framework/docs/5-layer-contract.md` — Layer 5 rules; assertion targets for SOAP identical to REST: typed models from Tasks + same-instance SOAP Object state-checks. SOAP-specific: fault expectations are tested as raised exceptions, never parsed XML.

## Decision

Thin by design — structurally the REST test doc with the fault case added. Exists so the generating agent has a SOAP-labeled canonical home and the fault-testing idiom is stated once.

## Canonical Example

```python
"""test_member_eligibility.py - Layer 5 (SOAP)."""

import pytest
from framework.utilities.trace import trace
from zeep.exceptions import Fault


class TestMemberEligibility:

    @trace("Test")
    @pytest.mark.soap
    def test_active_member_is_eligible_on_dos(self, member_eligibility, tc_scenario):
        """Member with active coverage on DOS reports eligible."""
        eligible = member_eligibility.is_eligible_on(
            tc_scenario["member_id"], tc_scenario["dos_admit"])

        assert eligible, \
            f"Member {tc_scenario['member_id']} not eligible on {tc_scenario['dos_admit']}"

    @trace("Test")
    @pytest.mark.soap
    def test_unknown_member_raises_fault(self, member_eligibility):
        """Service faults on unknown member — fault propagates as exception."""
        with pytest.raises(Fault):
            member_eligibility.get_eligibility("R00000000000000")
```

The fault test is the SOAP-specific idiom: the Interface catch-log-reraises (error rule 1), layers above never swallow, so `pytest.raises` at Layer 5 sees the original fault — the entire error-handling chain verified in three lines.

## Dry Run — Eligibility Check with Real Scenario Values

**Subject:** the mid-workflow eligibility shape (v2 command-pay, architecture reference only) with TC-001's real member `R00002117738102` and DOS `05/16/2026` as scenario values.

**Instantiation:** the canonical example with those values via scenario JSON. Positive path asserts the Task's typed `bool`; fault path asserts propagation semantics.

**Verdict: HOLDS.** Confirms the tasks-soap finding from the test seat: Layer 5 cannot tell SOAP from REST except by fixture names and the fault idiom — which is the architecture working as intended. Nothing surfaced.

## Contract Compliance

| Rule | Status |
|------|--------|
| Typed results asserted; no XML anywhere | PASS |
| Fault testing via pytest.raises (propagation chain) | PASS |
| One AAA block per method | PASS |
| Domain values from scenario data | PASS |

## What Does NOT Go Here

- No fault-XML inspection (if a test needs fault *content*, the SOAP Object grows a state-check)
- No WSDL/binding assertions (Interface config, Phase 3.1)
- No envelope construction (L2 `create_object`)
