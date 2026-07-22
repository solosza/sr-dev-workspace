# DB Tasks — Design Doc

## Governing Contract

`framework/docs/5-layer-contract.md` — Layer 3 rules + SQL Server addendum apply:
- Constructor takes Layer 2 Data Object(s) via DI — never an Interface, never constructs internally
- `@trace("Task")` on all public methods, NOT on constructor
- One domain operation per method (run-SP and verify are SEPARATE methods — SQL addendum atomicity)
- Makes the decisions: filtering, selection, retry, sequencing
- Returns **typed results** (pydantic models, primitives) — nothing is page-observable in DB work
- Method parameters are domain values — no identifiers (SQL, SP names) at Layer 3
- No knowledge of Roles or Tests

## Decision

Build from scratch. `hybrid-tasks.md` already covers discovery-style DB tasks (broad query → filter → pick → validate → retry). This doc adds the second DB task species: **pipeline execution tasks** — run a stored procedure, then verify its outcome across output tables. Derived from the real readmissions SIT suite (44+ cases), which is exactly this shape.

## SDK

- Layer 2 Data Objects (injected) · `trace.py` · `pydantic` v2 (result models) · stdlib only

## The Two DB Task Species

| Species | Shape | Canonical example |
|---------|-------|-------------------|
| **Discovery** | broad query → filter in Python → pick → validate → retry | `find_eligible_order` in [[hybrid-tasks]] |
| **Pipeline execution** | setup rows → run SP → verify outputs → archive/advance → verify again | this doc |

Same structure, same decorator, same typed returns — the split is what the domain operation *is*, not how the class is built.

## Canonical Example: SP Pipeline Tasks

```python
"""
ReferencePipelineTasks - Layer 3 Task

Orchestrates a Data Object through a stored-procedure pipeline:
error-report pass, archive pass, outcome verification.
"""

from framework.utilities.trace import trace
from _reference.data_objects.reference_load_data_object import ReferenceLoadDataObject
from _reference.data_objects.models.reference_load_models import (
    ErrorReportResult, ArchiveResult, PipelineOutcome
)


class ReferencePipelineTasks:
    """
    Task: Execute and verify a reference-load SP pipeline.

    - Constructor takes Layer 2 Data Object — composition via DI
    - @trace("Task") on every public method
    - One domain operation per method: run and verify are SEPARATE
    - Variant keys (domain values) select the SP — the Data Object owns SP names
    - Returns typed results
    """

    def __init__(self, reference_load: ReferenceLoadDataObject):
        self.reference_load = reference_load

    @trace("Task")
    def run_error_report(self, variant: str) -> ErrorReportResult:
        """Run the error-report SP for a load variant; return what it flagged."""
        self.reference_load.execute_error_sp(variant)
        self.reference_load.query_flagged_rows(variant)
        return ErrorReportResult(
            variant=variant,
            flagged=self.reference_load.get_count(),
            rows=self.reference_load.get_results_as(FlaggedRow),
        )

    @trace("Task")
    def run_archive(self, variant: str) -> ArchiveResult:
        """Run the archive SP: valid work rows move to the reference table."""
        self.reference_load.execute_archive_sp(variant)
        return ArchiveResult(variant=variant,
                             rows_moved=self.reference_load.get_count())

    @trace("Task")
    def verify_pipeline_outcome(self, variant: str,
                                expected_moved: int) -> PipelineOutcome:
        """Verify post-archive state: work drained, ref populated, audit written."""
        self.reference_load.count_work_rows(variant)
        work_remaining = self.reference_load.get_count()
        self.reference_load.count_ref_rows(variant)
        ref_rows = self.reference_load.get_count()
        self.reference_load.count_audit_rows(variant)
        audit_rows = self.reference_load.get_count()
        return PipelineOutcome(
            variant=variant,
            work_drained=(work_remaining == 0),
            ref_matches=(ref_rows >= expected_moved),
            audit_written=(audit_rows > 0),
        )
```

**Where the SP names live:** the Data Object — as a variant→name map in its class constants (or fixture JSON per contract L2 rule 3). Layer 3 passes only the **variant key** (`"apr_mapping"`), a domain value. See Dry Run for why.

## Dry Run — Readmissions Reference-Load Pipeline (real SIT suite)

**Subject:** the hmsa readmissions suite — 4 parametrized variants (`apr/ms` × `mapping/exclusion`), each with an error-report SP, an archive SP, a work table, shared ref + audit tables (real names: `hmsa_com_readmiss_apr_drg_to_mdc_error_rpt_sp`, `hmsa_com_imp_readmiss_apr_drg_to_mdc_ref_wrk_tbl`, …).

**Instantiation:** the canonical example above IS the readmissions flow with variant `"apr_mapping"`. Test parametrizes over 4 variants; each run: seed work rows → `run_error_report` → assert flagged set → `run_archive` → `verify_pipeline_outcome` → assert all three checks. One Task class, one Data Object, 4 variants — pattern covers all 44+ SIT cases.

**Verdict: HOLDS, with one SURFACED conflict — resolved in this doc, needs user ratification:**

> **SURFACED:** the real readmissions conftest keeps raw SP/table names in parametrize tuples, which flow through the test into task calls. Under contract v2.2 that violates TWO rules: L3 rule 10 (no identifiers at Layer 3 — an SP name transiting a Task method is an identifier at L3) and the SQL addendum (the Data Object owns its SQL — SP names included).
>
> **Resolution adopted here:** parametrize tuples carry **variant keys + expected values only** (`("apr_mapping", 3)`) — still module-level constants per the collection-time rule. The Data Object owns the variant→SP/table name maps as its class constants. Names appear in exactly one file; tests and Tasks speak pure domain vocabulary.
>
> **Ledger refinement implied:** the domain-conftest decision ("SP names, table names in domain conftest") narrows to: *test-shaping values* (variant keys, expected outcomes) in conftest; *identifiers* (SP/table names) in the Data Object. The readmissions conftest is the right pattern with the wrong contents.

## Contract Compliance

| Rule | Status |
|------|--------|
| Constructor takes Data Object via DI | PASS |
| @trace("Task") on public methods only | PASS |
| One domain operation per method (run ≠ verify) | PASS |
| Typed results (pydantic) — data flows up | PASS |
| Domain-value parameters (variant keys, not SP names) | PASS — via surfaced resolution |
| No identifiers at L3 | PASS — Data Object owns name maps |
| Decisions at L3 (sequencing, expected-vs-actual assembly) | PASS |
| No knowledge of Roles/Tests | PASS |

## Dependencies

- Layer 2 Data Object with `execute_sproc` support (SqlServerInterface, Phase 1.3)
- `trace.py`, `pydantic` v2

## What Does NOT Go Here

- No SQL, SP names, or table names (Data Object constants — the dry run's whole finding)
- No assertions (Layer 5 asserts on the typed results + same-instance state-checks)
- No test data seeding content (Phase 3.3 / domain `data/`)
- No discovery-with-retry logic (already canonical in [[hybrid-tasks]])
