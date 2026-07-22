# UI Tests — Design Doc

## Governing Contract

`framework/docs/5-layer-contract.md` — Layer 5 rules: one AAA block per method; acts through the **highest applicable layer** (Role for persona workflows, Task directly when a Role would be a pass-through); asserts via Page Object state-checks; every assert carries a failure message; `@trace("Test")` + markers; no business logic.

## Decision

Translate `platform-selenium/framework/_reference/tests/` (proven AAA pattern) onto the DI fixture stack. UI tests are the one place where **assertion targets are page state** — the `-> None` Task norm means the page, not return values, carries the evidence.

## Canonical Example

> **Rename note (2026-07-21):** example swept to Orderly commerce vocabulary per the clean-room directive (was a QNXT claim/DRG example — lesson #45 doc-sweep: the directive wins and the doc gets fixed, not followed).

```python
"""test_order_workup.py - Layer 5 (UI). Arrange via fixtures, Act through Task, Assert page state."""

import pytest
from framework.utilities.trace import trace


class TestOrderWorkup:

    @trace("Test")
    @pytest.mark.ui
    @pytest.mark.orders
    def test_status_change_saves(self, order_workup, orders_page, tc001_scenario):
        """Status change persists and Orderly confirms the save."""
        # Arrange — fixtures wired the stack; scenario carries domain values
        order_id = tc001_scenario["workup_order_id"]

        # Act — through the Task (single-Task scenario: Role would be a pass-through)
        order_workup.open_order(order_id)
        order_workup.update_status(tc001_scenario["status_to"])

        # Assert — page state, same-instance orders_page
        assert orders_page.is_save_confirmed(), \
            f"Orderly did not confirm save for order {order_id}"
        assert orders_page.get_displayed_status() == tc001_scenario["status_to"], \
            "Displayed status does not match the update"
```

Multi-persona UI scenarios act through a Role instead (see [[roles-ui]] when designed); the L5 rule 9 test is "would the Role wrap a single Task call?"

## Dry Run — TC-001 UI Slice

**Subject:** the Orderly status-change step of order-workup TC-001 (pending → shipped on order `ORD-2101`).

**Instantiation:** exactly the canonical example — scenario JSON supplies order id + target status; `order_workup` (Task fixture) acts; `orders_page` (same instance the Task used) asserts. On failure, the screenshot hook fires (browser fixture present) — the evidence chain needs nothing from the test body.

**Verdict: HOLDS.** The dual-assertion question resolves cleanly for UI: there are no typed results to assert on (`-> None` norm), so page state-checks carry everything — the UI test is the degenerate case of the dual pattern, which is worth stating so the generating agent doesn't invent return values for Browser Tasks just to have something to assert.

## Contract Compliance

| Rule | Status |
|------|--------|
| One AAA block per method | PASS |
| Acts through highest applicable layer (Task here — Role would be pass-through) | PASS |
| Asserts via same-instance Page Object state-checks | PASS |
| Failure message on every assert | PASS |
| Never calls Interface or L2 action methods to act | PASS |

## What Does NOT Go Here

- No waits/retries in test bodies (Page Objects own waits)
- No data setup (fixtures + scenario data)
- No screenshots (conftest hook)
- No multi-interface verification (that's a hybrid test, [[tests-hybrid]])
