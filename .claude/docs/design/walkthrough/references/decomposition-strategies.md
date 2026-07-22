# Decomposition Strategies — Sections per Input Type

Parent: [[../index.md]]

The core loop is artifact-agnostic; ONLY this file knows input types. Adding a new input type = adding a row here + a strategy section, nothing else changes.

## Strategy Table

| Input type | Sections come from | Typical count |
|-----------|-------------------|---------------|
| `file` (code) | Logical regions: bootstrap/imports, then each functional block (options, fixtures by group, hooks) | 5–10 |
| `design-doc` / contract | Its headings (H2 level), merging trivially small ones | 4–10 |
| `command` / skill | Its workflow steps, plus one section for state/gates if present | steps + 1–2 |
| `concept` | Agent-proposed subtopics, ordered dependency-first (what must be understood before what) | 3–8 |
| `plan` / pipeline | Its phases; large phases split by component | phases ± merge/split |
| `error` / log | The causal chain: symptom → immediate cause → root cause → fix options | 3–5 |

## Rules

1. **Dependency order.** Sections are ordered so no section depends on a later one (format-contract rule 3 depends on this).
2. **Section = one sitting.** A section should be explainable in one message and discussable in a few turns. Too big → split; trivial → merge into a neighbor.
3. **The map is a proposal.** Step 3 presents it; the user reorders/adds/removes before the loop starts, and can still say "add a section on X" mid-loop (inserted after the cursor).
4. **Name sections in domain vocabulary** ("credentials", "report hooks") — the names appear in the ledger and must be meaningful standalone.
5. **Cap at ~10.** Beyond that, propose splitting into multiple walkthroughs (the artifact is probably multiple artifacts).

## Worked Example (from the originating session)

Input: "conftest design" (`concept`, grounded in 3 real conftest files) →

```
1. bootstrap        — sys.path, .env loading
2. cli-options      — pytest_addoption knobs
3. config           — environment JSON → session fixture
4. credentials      — users + secrets resolution
5. logging          — handlers, formatters
6. interfaces       — driver/db/api/soap fixtures + scopes
7. layer-stack      — L2/L3/L4 DI wiring
8. report-hooks     — screenshot-on-failure, HTML metadata
9. markers          — dynamic registration
(10. domain-conftest — constants + parametrize, lives in subdirs)
```
