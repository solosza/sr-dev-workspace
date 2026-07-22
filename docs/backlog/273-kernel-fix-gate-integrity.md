# Gate Integrity Enforcement — No Pass-on-Stub, Portable Fixtures, Grep False-Positive Helper

## Status
Open

## Priority
High — the gate system is the only thing standing between "self-reported done" and "actually correct." Three integrity holes let weakened or simulated tests report GATE passes, which lesson #39's orchestrator re-run discipline catches manually today. Make the holes structurally hard.

## Summary
Three category-4 gate-integrity failures: (1) batches self-report GATE passes on tests that were weakened or simulated rather than run live (247 L3 was a simulation not a live dependent swarm; 216 L3 never ran) — a simulated gate should be structurally distinguishable from a live one; (2) persisted test fixtures are not portable — 222 used a relative `DATABASE_URL`/`PYTHONPATH` that only worked from one cwd (lesson #47); (3) grep-based semantics gates false-positive on content like CSS `max-width:100%` matching an absolute-claim grep, because the grep doesn't strip `<style>` or check match context. Codify each into a reusable, enforceable check.

## Requirements
- **Live-vs-simulated gate marker:** GATE/L3 tasks must emit a re-runnable evidence artifact (the exact command + captured live output, non-empty) as their pass proof. A gate whose evidence is a "simulation" or a 0-byte log is a DEFECT finding, never a pass (reaffirms lessons #39 and #49 mechanically). Provide a small checker the orchestrator and the runner can call to classify a gate's evidence as live | simulated | empty.
- **Fixture portability rule + linter:** live test fixtures MUST use an absolute or env-driven `DATABASE_URL` and an explicit `PYTHONPATH` stated in the task file (lesson #47). Add a linter that scans test tasks/fixtures for relative DB URLs and missing PYTHONPATH declarations and fails them before they ship. (223's tests already follow this — encode it as the enforced standard.)
- **Shared grep-context helper:** a single `strip_markup_then_grep` helper (strip `<style>`/`<script>` blocks, then match, then report surrounding context for human/automated adjudication) that all HTML/source semantics gates call, eliminating the CSS-`100%` class of false positive. Retrofit the portfolio/absolute-claims gates to use it.
- **Regression coverage:** tests proving (a) a simulated/empty gate evidence is rejected, (b) a relative-DATABASE_URL fixture is flagged, (c) the grep helper does not fire on CSS `max-width:100%` but does fire on a real absolute claim in body text.

## References
- Lessons #39 (orchestrator re-runs every gate live), #49 (0-byte-log gate skip is a defect), 2026-07-15 semantics false-positives (AST/docstring/decorator), 2026-07-20 fixture PYTHONPATH (#47 — single-root imports + explicit PYTHONPATH)
- Grep false positives this session: pipelines 255/256/258 (CSS `max-width:100%` vs absolute-claims grep)
- Simulated/never-run gates: 247 L3 (simulation), 216 L3 (never ran)
- `.claude/skills/eval/gate-contract.md`, `.claude/skills/prod-test/gate-contract.md`, portfolio gate contracts under `tasks/portfolio-*`

## Task Builder Input
- **Deliverable:** A gate-evidence classifier (live/simulated/empty), a fixture-portability linter, and a shared `strip_markup_then_grep` helper — wired into the gate-contract verification path and retrofitted onto the portfolio absolute-claims gate; plus regression tests for all three.
- **Location:** workspace
- **Scope:** BUILD
- **Constraints:** Helpers go in `lib/` and are called from gate contracts/verification, not duplicated per pipeline. Must not weaken any existing passing gate. This is the most independent of the four (touches gate/test tooling, not the runner core) but still runs SEQUENTIAL in this pipeline per the user's instruction. Encode existing lessons as enforcement — do not re-derive them.
