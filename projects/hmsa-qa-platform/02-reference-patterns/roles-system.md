# System Roles — Design Doc

## Governing Contract

`framework/docs/5-layer-contract.md` — Layer 4 rules. A System Role is a **non-human actor** — "the nightly batch," "the validation service" — with workflows but no login. Typed returns are the norm (nothing page-observable).

## Decision

Canonicalize the `SystemValidator` shape from [[cross-layer-notes]] with one hard scoping rule the dry run produced: **System Roles are the rarest Role and most candidates shouldn't exist.** DB/API test suites usually act through Tasks directly (L5 rule 9) — a System Role earns existence only when a workflow genuinely orchestrates ACROSS Task modules.

## When NOT to Create One (the rule that matters most)

| Candidate | Verdict |
|-----------|---------|
| Wraps one Task module's methods (run SP → verify, same module) | **NO ROLE** — the test consumes the Task directly; a Role here is a pass-through (composition rule). This is exactly why [[tests-db]]'s canonical test uses `reference_pipeline` directly. |
| Orchestrates discovery + execution + verification across modules as one named actor's workflow | **ROLE** — the actor ("the batch validator") is real domain vocabulary and the sequence is a workflow, not a wrapper |

## Canonical Example

```python
"""BatchValidator - Layer 4 Role (System). Non-human actor, typed results."""

from framework.utilities.trace import trace
from _reference.tasks.discovery_tasks import DiscoveryTasks
from _reference.tasks.reference_pipeline_tasks import ReferencePipelineTasks
from _reference.roles.models.validation_models import BatchValidationResult


class BatchValidator:
    """
    - Non-human persona: no identity dict, no login — its 'identity' is the
      interface-level connection identity (per-user model, configured in 3.1)
    - Constructor: Tasks via DI (two modules — earns Role status)
    - Typed results — everything flows up
    """

    @trace("Role Constructor")
    def __init__(self, discovery: DiscoveryTasks,
                 pipeline: ReferencePipelineTasks):
        self.discovery = discovery
        self.pipeline = pipeline

    @trace("Role")
    def validate_reference_load(self, variant: str,
                                expected_moved: int) -> BatchValidationResult:
        """The batch validator's full workflow: precondition → execute → verify."""
        subjects_ready = self.discovery.count_pending_work_rows(variant)
        report = self.pipeline.run_error_report(variant)
        self.pipeline.run_archive(variant)
        outcome = self.pipeline.verify_pipeline_outcome(variant, expected_moved)
        return BatchValidationResult(
            variant=variant, subjects_ready=subjects_ready,
            flagged=report.flagged, outcome=outcome,
        )
```

**Identity note:** the System Role's DB/API access rides the interface-level identity (session-scoped, per-user model from the conftest design). If a client ever requires per-persona DB authentication mid-suite, that becomes a function-scoped connection variant — **deferred until a client demands it** (catalogs on demand).

## Dry Run — Readmissions Suite as the Scoping Test

**Subject:** the real 4-variant SP suite, asked the question: does it need a System Role?

**Result:** the plain SP-validation path (run error SP → archive → verify, one Task module) **correctly produces NO Role** — tests-db.md already ships its canonical test consuming `reference_pipeline` directly, and this dry run confirms that was right, not an omission. The Role appears only in the composed flow (discovery precondition + pipeline + typed aggregation across two modules) — the `BatchValidator` above. The scoping rule survives contact with the suite most likely to tempt someone into a pass-through Role. **HOLDS — and the corpus is already consistent with it.**

## Contract Compliance

| Rule | Status |
|------|--------|
| Tasks via DI, two+ modules | PASS |
| Typed results (pydantic) | PASS |
| No identity dict — interface identity governs access | PASS (documented) |
| Composition rule enforced via the when-NOT table | PASS |

## What Does NOT Go Here

- No pass-through Roles over single Task modules — the test uses the Task
- No SQL/SP knowledge (L2 owns identifiers, L3 owns operations)
- No login/user identity (that's UI/hybrid Roles)
- No assertions (L5 asserts on the typed result)
