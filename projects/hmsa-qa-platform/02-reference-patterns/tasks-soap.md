# SOAP Tasks — Design Doc

## Governing Contract

`framework/docs/5-layer-contract.md` — Layer 3 rules + SOAP addendum:
- Constructor takes SOAP Objects via DI
- `@trace("Task")` on public methods
- **Typed returns** — zeep gives dicts, pydantic validates them, Tasks return models
- No operation names, WSDL details, or raw XML at L3

## Decision

Build from scratch — no clean reference exists (v2's SOAP usage in the command-pay flow is **architecture reference only**, per the clean-room rule: the *shape* — mid-workflow member/assignment lookups feeding UI steps — is what we keep; no code, no naming). Structurally identical to REST Tasks; this doc exists so the SOAP-specific seams (fault semantics, payload factories) have a canonical home.

## Canonical Example

```python
"""MemberEligibilityTasks - Layer 3 Task (SOAP). Typed results flow up."""

from framework.utilities.trace import trace
from _reference.soap_objects.member_service_object import MemberServiceObject
from _reference.soap_objects.models.member_models import MemberEligibility


class MemberEligibilityTasks:
    """
    - Constructor takes SOAP Object via DI
    - @trace("Task") on public methods
    - Returns validated pydantic models from zeep dicts
    """

    def __init__(self, member_service: MemberServiceObject):
        self.member_service = member_service

    @trace("Task")
    def get_eligibility(self, member_id: str) -> MemberEligibility:
        """Fetch and validate a member's eligibility snapshot."""
        self.member_service.get_member(member_id)
        return self.member_service.get_last_body_as(MemberEligibility)

    @trace("Task")
    def is_eligible_on(self, member_id: str, date_of_service: str) -> bool:
        """Decision: was the member eligible on the DOS? (Feeds hybrid flows.)"""
        eligibility = self.get_eligibility(member_id)
        return any(span.covers(date_of_service) for span in eligibility.coverage_spans)
```

SOAP faults propagate as exceptions from the Interface (catch-log-reraise, contract error rule 1) — Tasks never interpret fault XML. Complex request payloads are composed by the SOAP Object via `create_object`; Tasks pass domain values only.

## Dry Run — Mid-Workflow Eligibility Check (v2 command-pay shape, architecture reference)

**Subject:** the hybrid-flow step where a UI workflow needs a member's service data before proceeding (v2's DB→UI→**SOAP**→UI→DB command-pay shape — shape only, clean-room).

**Instantiation:** hybrid Task receives `MemberEligibilityTasks` via DI (task-composition rule, max depth 2) and calls `is_eligible_on(member_id, dos)` between the UI setup and submission steps — a typed `bool` gating the workflow's branch. Member ID and DOS arrive from scenario data (TC-001's real member `R00002117738102`, DOS `05/16/2026` would slot straight in).

**Verdict: HOLDS.** Structurally indistinguishable from REST Tasks — which is itself the finding: the SOAP addendum's divergences (faults, `create_object`, dict validation) all land at Layers 1–2, leaving Layer 3 identical across API-shaped interfaces. Nothing surfaced.

## Contract Compliance

| Rule | Status |
|------|--------|
| DI constructor (SOAP Object) | PASS |
| Typed pydantic returns from zeep dicts | PASS |
| Task-in-Task via DI, depth ≤ 2 | PASS |
| No operation names / raw XML at L3 | PASS |
| Faults propagate — never interpreted at L3 | PASS |

## What Does NOT Go Here

- No payload construction (SOAP Object + `create_object`)
- No WSDL/binding config (Interface + environment config)
- No fault-XML parsing anywhere above Layer 1
- No assertions (L5)
