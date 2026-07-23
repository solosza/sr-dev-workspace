# Gate Contract — 273 Gate Integrity Enforcement

| Gate | Check | Method | Task | Pass |
|------|-------|--------|------|------|
| GI-01 | Gate-evidence classifier: a helper classifies a GATE/L3 task's evidence as live | simulated | empty. A gate whose evidence is a simulation or a 0-byte log is a DEFECT, never a pass (reaffirms #39/#49). Composes with 276's completion oracle, does not re-implement it | grep + read; unit sim | 001 | classifier returns live/simulated/empty |
| GI-02 | Fixture-portability linter: scans live test tasks/fixtures for relative DATABASE_URL (non-absolute/non-env) and missing explicit PYTHONPATH declarations, and flags them (222/#47 class). Encodes 223's already-portable pattern as the enforced standard | grep + read; unit sim | 002 | relative-DB + missing-PYTHONPATH flagged |
| GI-03 | Shared strip_markup_then_grep helper: strips <style>/<script> blocks, then greps, then reports surrounding context. All HTML/source semantics gates call it — eliminates the CSS max-width:100% false-positive class. Retrofit the portfolio absolute-claims gate to use it | grep + read; unit sim | 003 | helper strips markup + context; no CSS-100% FP |
| GI-04 | Regression: (a) a simulated/empty gate-evidence is REJECTED by the classifier; (b) a relative-DATABASE_URL fixture is FLAGGED by the linter; (c) the grep helper does NOT fire on CSS `max-width:100%` but DOES fire on a real absolute claim in body text | live pytest/bash | 004 | 3/3 regression cases pass live |

## Rules
- READ 276's lib/observability.py (completion oracle) + the eval/prod-test gate-contract patterns + lesson #47 (PYTHONPATH) FIRST (RULE ZERO) — COMPOSE, do not duplicate 276
- Helpers go in lib/ and are CALLED from gate contracts/verification — not duplicated per pipeline
- Encode EXISTING lessons as enforcement (#39, #47, #49, the CSS-100% FP) — do not re-derive them
- Must not weaken any existing passing gate. One action per task. Any RED -> fix -> /kernel/learn.
