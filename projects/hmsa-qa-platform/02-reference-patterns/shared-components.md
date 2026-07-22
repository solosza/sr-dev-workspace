# Shared Components — Design Doc

## Governing Contract

`framework/docs/5-layer-contract.md` — Layer 2 rules + Browser addendum rule 4, and the v2.3 constructor clause this design produced: *identifier config and composed L2 components may be injected, never constructed internally.* All decisions settled in [docs/walkthroughs/2026-07-14-shared-components.md](../../../docs/walkthroughs/2026-07-14-shared-components.md) (dry-tested against QNXT TC-001 + the full v2 component inventory).

## Decision

Build from scratch. No clean reference exists: platform-selenium has no components; v2's nine component files are **architecture reference only** (clean-room) — they prove the category's value and its two failure modes (app-specific content mixed in, inheritance for variants).

## Definition & Membership Test

A shared component is **a Layer 2 class encoding the *mechanics* of a recurring UI pattern, whose identifiers are injected rather than owned**, subject to every Layer 2 rule, shipping in `_reference/components/`.

**Membership test (the generating agent applies this to every candidate):**
> Could a different client's app use this class unchanged, given only an identifier config?
> **Yes** → shared component. **No** → app-specific — with two exits:
> 1. Leave it app-specific (its content is genuinely one app's), or
> 2. Extract the mechanics into a generic component + config, then re-test (v2's org-hierarchy fails as written but yields a TreeComponent that passes).

**Genericity scope:** each component declares `universal` (pure HTML mechanics) or `library:<name>` (generic across apps sharing a widget library — e.g. a date-picker). Library-scoped components are legitimate; they just say so.

**The economic line:** shared components are platform IP — built once, reused every engagement. App-specific L2 is client deliverable. Misclassification either gives away custom work or charges for stock.

## The Pattern: Locator-Contract Injection

```python
# SHIPS WITH PLATFORM — framework/_reference/components/grid_component.py
@dataclass(frozen=True)
class GridLocators:                      # the locator CONTRACT — declares needs, holds no values
    root: tuple                          # (By, selector) — grid container
    header_cells: tuple                  # relative to root
    rows: tuple                          # relative to root
    cell_template: str                   # dynamic locator template, instantiated per call

class GridComponent:
    """Mechanics only — knows HOW grids work, never WHICH grid."""
    def __init__(self, browser: BrowserInterface, locators: GridLocators):
        self.browser = browser
        self.loc = locators
    # === STATE-CHECKS ===
    def get_column_names(self) -> list[str]: ...
    def find_row_by_values(self, **column_values) -> int: ...
    # === ATOMIC ===
    def click_row(self, index: int) -> "GridComponent": ...   # returns self
```

```python
# BUILT PER CLIENT — the app-specific page owns the VALUES
class ClaimsSearchPage:
    RESULTS_GRID = GridLocators(
        root=(By.CSS_SELECTOR, "#claimSearchResults"),
        header_cells=(By.CSS_SELECTOR, "thead th"),
        rows=(By.CSS_SELECTOR, "tbody tr"),
        cell_template="td:nth-child({col})",
    )
```

```python
# WIRED BY FIXTURES — no intra-L2 construction, conftest rule 3 absolute
@pytest.fixture
def claims_results_grid(browser):
    return GridComponent(browser, ClaimsSearchPage.RESULTS_GRID)

@pytest.fixture
def claim_workup(claims_search_page, claims_results_grid, claim_page):
    return ClaimWorkupTasks(claims_search_page, claims_results_grid, claim_page)
```

Components are **ordinary fixture-built L2 objects, delivered to Layer 3 side-by-side with pages**. Same-instance assertions work through the component's own fixture.

**Honest limit:** locator contracts fit structurally *similar* widgets. A truly alien widget (canvas grid, virtualized list) gets its own app-specific component against the BrowserInterface — the generic set is an offered toolkit, never a forced abstraction.

## Variants Without Inheritance

| Variant differs in… | Mechanism | v2 case it replaces |
|--------------------|-----------|--------------------|
| Identifiers only | Same class + per-variant config | 3 dashboard subclasses → 1 DashboardComponent + 3 configs |
| Behavior | App component **composes** the generic (has-a, fixture-injected) | `my_work_grid_superclass` → `ApprovalGrid(grid)` delegating to a GridComponent |

```python
class ApprovalGrid:                       # app-specific, client repo
    def __init__(self, grid: GridComponent):    # composed generic, injected by fixture
        self.grid = grid
    def approve_row(self, **criteria) -> "ApprovalGrid":
        row = self.grid.find_row_by_values(**criteria)
        ...
```

## What Ships (v1 Exemplars)

| File | Role | Why this one |
|------|------|--------------|
| `modal_component.py` | **Lead exemplar** | Simplest complete demonstration: small locator contract, config injection, fixture wiring — the file the agent learns the pattern from |
| `grid_component.py` | **Flagship** | Pattern at full stress — most identifiers, most mechanics; dry-tested against QNXT claims grid + platform-selenium employees table (one class, two apps, zero changes); v2's documented duplication failure zone, fixed |

**The set beyond these is DEFERRED — deliberately.** Trigger to extend: Phase 4 harness design or first client onboarding, whichever comes first. Candidates on record: navbar, wizard, file-upload (input-element path only — native OS dialogs are not browser-automatable), date-picker (`library:`-scoped), type-ahead, tree. The set **self-assembles**: when the agent meets a recurring pattern with no component, it builds one per this doc and the membership test — the exemplars are teaching material, not a catalog.

## Dry Runs (kept as permanent worked examples)

1. **GridComponent × two apps:** QNXT claims-search grid (TC-001's `open_claim` flow) and platform-selenium's employees table — same class, two `GridLocators` blocks, zero component changes. Genericity holds.
2. **Membership test × the full v2 inventory:** all nine files sort cleanly (grid/navbar/activity-guide → shared; three dashboards → app-specific; two superclasses → composition rebuilds; org-hierarchy → extract-then-pass). The two sharpenings above came out of this run.

## Contract Compliance

| Rule | Status |
|------|--------|
| L2 rules apply unchanged (chaining, state-checks, no decorators, domain vocabulary) | PASS |
| v2.3 rule 1: config/composed-component injection, never internal construction | PASS (this design motivated the clause) |
| Conftest rule 3: all construction in fixtures | PASS — no intra-L2 construction anywhere |
| No inheritance (global rule 6) | PASS — config variants + has-a |
| Identifiers at Layer 2, owned by app-specific code | PASS — contract declares, page supplies, fixture wires |

## Dependencies

- `BrowserInterface` (Phase 1.1) · `dataclasses` (stdlib) · fixture model per [[fixture-wiring]]

## What Does NOT Go Here

- No app locator values (pages own them)
- No workflow logic (Tasks compose components + pages)
- No speculative components — the deferred-set trigger governs additions
- No inheritance, ever — a "base component" someone wants to subclass is a config or a composition waiting to be recognized
