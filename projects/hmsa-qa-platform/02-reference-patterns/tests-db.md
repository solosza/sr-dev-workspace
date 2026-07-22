# DB Tests — Design Doc

## Governing Contract

`framework/docs/5-layer-contract.md` — Layer 5 rules; assertion targets for DB: **typed results from Tasks** + same-instance Data Object counts. Parametrize tuples carry **variant keys + expected values only** — identifiers live in the Data Object (ratified 2026-07-13, tasks-db dry run).

## Decision

The SP-as-subject test pattern — the readmissions suite's shape (44+ cases) rebuilt contract-clean. This is the doc where the ratified variant-key refinement becomes visible test code.

## Canonical Example

```python
"""test_reference_pipeline.py - Layer 5 (DB). Parametrized SP-as-subject validation."""

import pytest
from framework.utilities.trace import trace

# === PARAMETRIZE (collection-time, domain conftest) ===
# Variant keys + expected values ONLY — SP/table names live in the Data Object.
ALL_LOAD_VARIANTS = [
    ("apr_mapping",   3),
    ("ms_mapping",    3),
    ("apr_exclusion", 2),
    ("ms_exclusion",  2),
]


class TestReferencePipeline:

    @trace("Test")
    @pytest.mark.db
    @pytest.mark.parametrize("variant,expected_moved", ALL_LOAD_VARIANTS)
    def test_valid_rows_archive(self, reference_pipeline, reference_load,
                                variant, expected_moved):
        """Archive SP moves valid work rows to ref table and writes audit."""
        # Act — typed results from the Task, one operation per call
        report = reference_pipeline.run_error_report(variant)
        assert report.flagged == 0, \
            f"[{variant}] error SP flagged {report.flagged} rows: {report.rows}"

        archive = reference_pipeline.run_archive(variant)
        outcome = reference_pipeline.verify_pipeline_outcome(variant, expected_moved)

        # Assert — typed outcome + same-instance count backup
        assert outcome.work_drained, f"[{variant}] work table not drained"
        assert outcome.ref_matches, \
            f"[{variant}] ref table rows < expected {expected_moved}"
        assert outcome.audit_written, f"[{variant}] no audit trail"
        reference_load.count_ref_rows(variant)
        assert reference_load.get_count() >= expected_moved, \
            f"[{variant}] same-instance recount disagrees with outcome model"
```

One parametrized method = 4 test cases with variant-labeled failures (`[apr_mapping] ...`) — the readmissions economics with contract-clean layers.

## Dry Run — Readmissions Reference Load (real suite, all four variants)

**Subject:** the same real SPs as the tasks-db dry run, now from Layer 5.

**Instantiation:** the canonical example IS the suite: `ALL_LOAD_VARIANTS` replaces the old `ALL_ARCHIVE_SPS` tuples (which carried five raw names per row); each name now resolves inside `ReferenceLoadDataObject`. Failure messages carry the variant key — human-readable without exposing identifiers.

**Verdict: HOLDS.** The refinement survives contact: collection-time rule intact (tuples still module constants), test IDs still meaningful (`test_valid_rows_archive[apr_mapping-3]`), and the tuple shrank from 5 columns to 2 — the identifier columns were pure duplication all along. Nothing further surfaced.

## Contract Compliance

| Rule | Status |
|------|--------|
| Variant keys in tuples; identifiers in Data Object | PASS (ratified refinement) |
| Typed results + same-instance state-checks | PASS |
| One AAA block per (parametrized) method | PASS |
| Run ≠ verify (separate Task calls) | PASS |
| Failure messages with variant context | PASS |

## What Does NOT Go Here

- No SQL, SP names, or table names — anywhere in the test file
- No seeding logic (fixtures + Phase 3.3 data strategy; seeding is an arranged Task call)
- No transaction rollback (explicit-cleanup discipline — walkthrough §7)
