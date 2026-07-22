# Browser Tasks — Design Doc

## Governing Contract

`framework/docs/5-layer-contract.md` — Layer 3 rules + Browser addendum:
- Constructor takes Page Objects/Components via DI (the UI-only simplification of platform-selenium remains valid there; HMSA uses DI everywhere)
- `@trace("Task")` on public methods
- **`-> None` is the norm** — UI outcomes are page-observable; Tests assert via Page Object state-checks (contract L3 rule 2 as the default, not the exception)
- Typed return ONLY when the Task produces data a downstream step needs
- One domain operation per method; fluent Layer 2 chaining inside; no locators at L3

## Decision

Translate `platform-selenium/framework/_reference/tasks/` (proven, UI-only style) to the DI constructor. Two canonical methods: a pure `-> None` operation and one typed-return exception, so the generating agent sees both cases side by side.

## Canonical Example

```python
"""ClaimWorkupTasks - Layer 3 Task (Browser). One domain operation per method."""

from framework.utilities.trace import trace
from _reference.pages.qnxt_claim_page import QnxtClaimPage
from _reference.pages.qnxt_nav_page import QnxtNavPage


class ClaimWorkupTasks:
    """
    - Constructor takes Page Objects via DI — composition
    - @trace("Task") on public methods
    - -> None: outcomes observable on the page
    - Typed return only when data must flow downstream
    """

    def __init__(self, nav_page: QnxtNavPage, claim_page: QnxtClaimPage):
        self.nav_page = nav_page
        self.claim_page = claim_page

    @trace("Task")
    def open_claim(self, patient_control_number: str) -> None:
        """Navigate to a claim by PCN. Page-observable — returns None."""
        self.nav_page.open_claims_search()
        self.claim_page.enter_pcn(patient_control_number) \
                       .click_search() \
                       .click_first_result()

    @trace("Task")
    def update_drg(self, drg_code: str) -> None:
        """Change the claim's DRG and save. Page-observable — returns None."""
        self.claim_page.open_coding_tab() \
                       .enter_drg(drg_code) \
                       .click_save()

    @trace("Task")
    def capture_claim_id(self) -> str:
        """The typed-return exception: scrape the claim ID for downstream DB verify."""
        return self.claim_page.get_claim_id()
```

Navigation and form submission are SEPARATE methods even in one flow (operation boundary rule). Waits live in Page Object methods, never baked into Task sequencing.

## Dry Run — TC-001 QNXT DRG Change (real autopend SIT step)

**Subject:** TC-001's QNXT workup: open claim `SIT-D2-01R` (PCN), change DRG 065 → 287, save — the manual step the SIT sheet records under "Changes Made to Prod Claim."

**Instantiation:** `open_claim("SIT-D2-01R")` → `update_drg("287")`; test asserts `claim_page.is_save_confirmed()` (state-check) — no return values needed, page shows everything. Downstream DB verification (claim re-adjudication → pend) needs the claim ID → `capture_claim_id()` is the typed exception feeding the hybrid flow.

**Verdict: HOLDS.** `-> None` norm fits every step; the one data handoff maps cleanly to the typed exception; no identifiers above Layer 2 (PCN and DRG codes are domain values from scenario data). Nothing surfaced.

## Contract Compliance

| Rule | Status |
|------|--------|
| DI constructor (Page Objects, not Interface) | PASS |
| `-> None` norm + typed exception documented | PASS |
| One operation per method; nav ≠ submit | PASS |
| Domain-value params (PCN, DRG code from scenario data) | PASS |
| No locators/identifiers at L3 | PASS |

## What Does NOT Go Here

- No waits (Page Object methods own them)
- No assertions (L5 via page state-checks)
- No multi-Task workflows (Roles, 2.3)
- No scraping-heavy data extraction pipelines — if a Browser Task returns more than a scalar or small model, the data probably belongs to a DB/API check instead
