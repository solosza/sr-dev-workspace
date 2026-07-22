# Hybrid Tests — Design Doc

## Governing Contract

`framework/docs/5-layer-contract.md` — Layer 5 rules with everything at once: acts through a Role (multi-Task orchestration = persona semantics, L5 rule 9), **dual assertion** in full (typed workflow results AND same-instance L2 state-checks across multiple interfaces).

## Decision

The flagship test species — DB setup → UI action → system behavior → DB verify is the platform's differentiation (v2's command-pay and the autopend suite are both this shape). The canonical example is autopend TC-001 end-to-end, already validated as the conftest walkthrough's dry run.

## Canonical Example

```python
"""test_autopend_happy_path.py - Layer 5 (Hybrid). The full dual-assertion pattern."""

import pytest
from framework.utilities.trace import trace


class TestAutopendHappyPath:

    @trace("Test")
    @pytest.mark.autopend
    def test_tc001_readmission_same_mdc_pends(self, sit_examiner, claims_data,
                                              tc001_scenario):
        """TC-001: within 30d, different DRG, same MDC → auto-pend, 30DAYR."""
        # Arrange + Act — ONE workflow through the Role (persona: SIT examiner
        # doing discovery → injection → QNXT workup → verification)
        result = sit_examiner.run_readmission_scenario(tc001_scenario)

        # Assert 1 — typed results: data the workflow computed
        assert result.history_valid, \
            "History claim failed SP eligibility filters"
        assert result.readmission_status == "PEND", \
            f"Expected PEND, got {result.readmission_status}"

        # Assert 2 — same-instance L2 state-checks: system state after the workflow
        claims_data.verify_update_id(
            tc001_scenario["readmission_cid"], tc001_scenario["update_id"])
        assert claims_data.get_count() > 0, \
            "Claim pended but updateid != 30DAYR — wrong pend source"
```

**Which assertion family when:** typed results for what the workflow *computed or observed en route* (the Role passes Task results up); state-checks for *system state that outlives the workflow* (rows, statuses). A hybrid test that uses only one family is usually missing coverage on the other side.

## Dry Run — TC-001 End-to-End (already exercised)

**Subject:** the full TC-001 flow — this exact test was built live during the conftest walkthrough's layer-stack dry run against the real SIT workbook, which is how the same-instance rule, the 7-fixture domain stack, and the 837BT question were all discovered.

**Verdict: HOLDS** (pre-validated). Cross-reference: [docs/walkthroughs/2026-07-13-conftest-design.md](../../../docs/walkthroughs/2026-07-13-conftest-design.md) §8 + tasks-db dry run for the DB leg. The one open dependency is inherited, not new: the claim-injection fixture awaits the 837BT/Phase 4 decision.

## Contract Compliance

| Rule | Status |
|------|--------|
| Acts through a Role (genuine multi-Task persona) | PASS |
| Dual assertion — both families, with the when-to-use rule stated | PASS |
| One AAA block; scenario data carries all domain values | PASS |
| Same-instance verification across the DB leg | PASS |

## What Does NOT Go Here

- No orchestration in the test body (the Role owns the sequence — a hybrid test with six Act steps is a Role that wasn't extracted)
- No interface-specific idioms beyond assertions (faults, screenshots, cleanup all live where their docs put them)
- No wait-for-batch logic (split-session pattern in [[cross-layer-notes]] handles overnight steps)
