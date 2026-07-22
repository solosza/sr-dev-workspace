# Hybrid Roles — Design Doc

## Governing Contract

`framework/docs/5-layer-contract.md` — Layer 4 rules. The hybrid Role is a **human persona whose workflow spans interfaces** — the flagship composition (DB discovery → claim injection → UI workup → DB verification) and the platform's differentiation.

## Decision

Canonicalize `SitExaminer` — already exercised end-to-end in the conftest walkthrough dry run and shipped as [[tests-hybrid]]'s canonical test. This doc adds the one rule neither of those states: **identity threading** across interfaces.

## Identity Threading (the rule this doc exists for)

A hybrid workflow touches multiple interfaces, each with its own authentication:

| Leg | Who authenticates | Where it's configured |
|-----|-------------------|----------------------|
| UI actions | **The Role's persona** — self-authenticating login, identity injected via fixture | `credentials["examiner"]` |
| DB queries/writes | The interface-level connection identity (per-user model — e.g. the analyst's own SQL login) | config `database.identity` → session fixture |
| API/SOAP calls | The interface-level client identity | config per interface |

**Two identities coexisting in one workflow is by design, and mirrors reality:** the human examiner clicks in QNXT as themselves while the test harness verifies through its own DB access — exactly how the manual SIT ran (tester in QNXT, analyst queries on the side). The Role's `identity` governs *persona actions only*; interface identities are conftest/config concerns the Role never sees. Per-persona DB authentication (if a client ever requires the DB leg to run *as the persona*) is a function-scoped connection variant — **deferred until demanded**.

## Canonical Example

```python
"""SitExaminer - Layer 4 Role (Hybrid). Persona whose workflow spans interfaces."""

from framework.utilities.trace import trace
from _reference.tasks.claim_discovery_tasks import ClaimDiscoveryTasks
from _reference.tasks.claim_setup_tasks import ClaimSetupTasks
from _reference.tasks.autopend_verification_tasks import AutopendVerificationTasks
from _reference.roles.models.scenario_models import ScenarioResult


class SitExaminer:
    """
    - Constructor: Tasks via DI (three modules) + persona identity
    - Typed result — the workflow computes data the test must see
    - UI legs self-authenticate as the persona; DB/API legs ride interface identities
    """

    @trace("Role Constructor")
    def __init__(self, discovery: ClaimDiscoveryTasks, setup: ClaimSetupTasks,
                 verification: AutopendVerificationTasks, identity: dict):
        self.discovery = discovery
        self.setup = setup
        self.verification = verification
        self.identity = identity

    @trace("Role")
    def run_readmission_scenario(self, scenario: dict) -> ScenarioResult:
        """Full SIT workflow: validate history (DB) → inject + work claim (UI) →
        verify outcome (DB). Returns the typed result the test asserts on."""
        history = self.discovery.validate_history_claim(scenario["history_cid"])
        self.setup.inject_readmission(scenario)                      # 837BT leg
        self.setup.work_claim_as(self.identity, scenario)            # UI leg — persona
        status = self.verification.get_claim_status(scenario["readmission_cid"])
        return ScenarioResult(history_valid=history.eligible,
                              readmission_status=status)
```

Dual assertion downstream (typed result + same-instance L2 state-checks) is [[tests-hybrid]]'s canon — the Role returns what it *computed*; system state that outlives the workflow is asserted via Data Objects.

## Dry Run — TC-001 End-to-End (third pass, new angle)

**Subject:** TC-001 again — deliberately: it was the conftest walkthrough's fixture dry run and tests-hybrid's assertion dry run; this pass checks the **Role seams** specifically.

**Checks:** three Task modules injected (composition rule: comfortably a Role, not a wrapper) ✓; persona identity used in exactly one place (`work_claim_as` — the UI leg) ✓; DB legs (`validate_history_claim`, `get_claim_status`) carry no identity parameters — they ride the session interface identity ✓; typed `ScenarioResult` up, page/DB state observable behind it ✓; the 837BT injection leg remains behind the deferred Phase 1/4 decision — the Role signature is stable regardless of which mechanism lands, because injection is a *Task* (`setup.inject_readmission`), so the open question never reaches Layer 4 ✓ (worth noticing: the layering is *containing* the deferred decision, which is what layers are for). **HOLDS.**

## Contract Compliance

| Rule | Status |
|------|--------|
| Tasks via DI (3 modules) + identity as workflow config | PASS |
| Typed result — data flows up | PASS |
| Identity threading: persona for UI only; interface identities untouched | PASS (documented) |
| Deferred 837BT decision isolated below Layer 4 | PASS |

## What Does NOT Go Here

- No interface knowledge (which SDK the legs use is invisible here)
- No decisions/filtering/retry (L3)
- No cross-persona orchestration (tests sequence Roles — see [[roles-ui]] multi-user)
- No identity values, connection strings, or credential resolution (fixtures/config)
