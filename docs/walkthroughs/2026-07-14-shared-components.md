# Walkthrough Ledger — shared components design (HMSA QA Platform 2.1.5)

**Date:** 2026-07-14
**Mode/Depth:** loop / plain
**Sources read:** v2 components directory inventory (architecture reference only, clean-room) · platform-selenium `_reference/` structure (no components dir exists) · hmsa-qa-platform README (Shared Components + monolith autopsy) · 5-layer-contract.md (v2.2→v2.3)
**Sections:** 5 settled, 1 consciously deferred
**Contract impact:** v2.3 — L2 constructor rule 1 narrowed (identifier config / composed L2 components may be injected, never constructed internally)

## Decisions

| # | Section | Settled |
|---|---------|---------|
| 1 | **the-locator-problem** | Locator-contract injection: generic component defines a typed identifier config (`GridLocators`: root, header_cells, rows, cell_template) declaring WHAT it needs; app-specific L2 owns the VALUES; **fixtures wire values into components** — no intra-L2 construction, conftest rule 3 absolute. Components are ordinary fixture-built L2 objects injected into L3 side-by-side with pages. Honest limit: locator contracts fit structurally similar widgets; alien widgets get app-specific components — the set is an offered toolkit, not a forced abstraction. *(Dry-tested: one GridComponent, QNXT claims grid + platform-selenium employees table, zero component changes. First model — page constructs its own components — rejected after user challenge.)* |
| 2 | **no-inheritance** | Identifier-only variants → one class + per-variant config (v2's 3 dashboard subclasses → 1 component + 3 configs). Behavior variants → app component COMPOSES the generic (has-a via fixture injection, never is-a). All nine v2 files map onto this with nothing left over. |
| 3 | **what-is-a-shared-component** | Definition: a Layer 2 class encoding the MECHANICS of a recurring UI pattern, identifiers injected not owned, all L2 rules apply, ships in `_reference/components/`. **Membership test:** usable by a different client's app unchanged, given only an identifier config → shared; else app-specific. Economic line: shared = platform IP; app-specific = client deliverable. *(Dry-tested against all 9 v2 files + QNXT cases: clean sort. Two sharpenings: the test classifies CLASSES not PATTERNS — FAIL has two exits, leave or extract-mechanics-and-retest; genericity may be library-scoped — components declare `universal` vs `library:<name>`.)* |
| 4 | **the-generic-set** | **DEFERRED** — trigger: Phase 4 harness design OR first client onboarding. v1 ships only the two exemplars. Candidates on record: navbar, wizard, file-upload, date-picker, type-ahead, tree. The set self-assembles via the membership test + pattern. |
| 5 | **page-component-composition** | Fixture-built components delivered to L3 alongside pages; app L2 owns values; wrappers receive composed generics via fixtures; same-instance assertions preserved. |
| 6 | **reference-examples** | Two exemplars: `modal_component.py` (lead — simplest complete) + `grid_component.py` (flagship — dry-tested worst case). Exemplars are teaching material, not a catalog; agent builds further components on demand. |

## Notes & Deferred

- **Design principle established (generalizes beyond this walkthrough):** *contract-touching decisions early, catalogs on demand.* The classifier, injection pattern, and contract wording were load-bearing (settled now); inventory-picking was speculative (deferred to demand).
- **File-upload constraint on record:** input-element path only — native OS dialogs are not browser-automatable.
- Gap-check B-findings routed: date-picker/type-ahead → deferred-set candidates (here); navigation-return position → contract rationale line when next touched; wait-policy home → Phase 3.1.
