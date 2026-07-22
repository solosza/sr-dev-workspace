# UI Roles — Design Doc

## Governing Contract

`framework/docs/5-layer-contract.md` — Layer 4 rules: constructor takes **Tasks via DI + workflow config (credentials = the persona's identity)**; `@trace("Role")` on workflow methods, `@trace("Role Constructor")` on `__init__`; workflow methods call MULTIPLE Tasks; a Role wrapping a single Task call shouldn't exist (composition rule); no Interface receipt, no knowledge of Tests.

## Decision

Translate `platform-selenium/framework/_reference/roles/employee_manager.py` (proven persona shape) to the DI constructor + credentials-fixture identity. The reference already demonstrates the two load-bearing habits: identity stored on `self` as workflow config, and **every workflow method self-authenticates as step 1** — which is what makes multi-user scenarios work.

## Canonical Example

```python
"""ClaimsExaminer - Layer 4 Role (UI). A persona: identity + tasks + workflows."""

from framework.utilities.trace import trace
from _reference.tasks.common_tasks import CommonTasks          # login/logout/nav
from _reference.tasks.claim_workup_tasks import ClaimWorkupTasks


class ClaimsExaminer:
    """
    - Constructor: Tasks via DI + identity (a credentials dict entry)
    - @trace("Role") / @trace("Role Constructor")
    - Workflow methods orchestrate MULTIPLE Task modules
    - -> None norm (UI outcomes page-observable); typed only when data flows up
    """

    @trace("Role Constructor")
    def __init__(self, common: CommonTasks, claim_workup: ClaimWorkupTasks,
                 identity: dict):
        self.common = common
        self.claim_workup = claim_workup
        self.identity = identity            # {"username": ..., "password": ...}

    @trace("Role")
    def work_claim_drg_change(self, pcn: str, drg_to: str) -> None:
        """Complete workflow: authenticate as self, open the claim, change DRG.

        Self-authentication as step 1 is the multi-user mechanism — sequential
        Roles in one browser each begin by logging in as themselves."""
        self.common.login(self.identity["username"], self.identity["password"])
        self.claim_workup.open_claim(pcn)
        self.claim_workup.update_drg(drg_to)
```

```python
# fixtures — persona = tasks + WHICH identity
@pytest.fixture
def claims_examiner(common_tasks, claim_workup, credentials):
    return ClaimsExaminer(common_tasks, claim_workup, credentials["examiner"])

@pytest.fixture
def claims_supervisor(common_tasks, claim_adjust, credentials):
    return ClaimsSupervisor(common_tasks, claim_adjust, credentials["supervisor"])
```

## Multi-User Workflows

Roles never know about each other — **the test sequences personas**, and each Role's self-authenticating workflow handles the identity switch in the shared function-scoped browser:

```python
def test_examiner_pends_supervisor_pays(self, claims_examiner, claims_supervisor,
                                        claim_page, tc_scenario):
    claims_examiner.work_claim_drg_change(tc_scenario["pcn"], tc_scenario["drg_to"])
    claims_supervisor.adjust_claim_to_pay(tc_scenario["pcn"])      # re-login inside
    assert claim_page.get_claim_status() == "PAY", "Supervisor adjustment not applied"
```

No logout choreography in tests; `common.login` owns the session switch (logout-if-needed is login-task mechanics).

## Dry Run

**1. EmployeeManager translation (real reference, own repo):** all five v1.0 traits map — `(browser, url, email, password)` constructor → `(tasks..., identity)` DI; internal `EmployeeManagementTasks(browser)` construction → fixture-injected; `autologger` → `@trace`; login-first workflow → unchanged (it was right all along); `-> None` → unchanged (UI norm). Nothing in the persona shape resists the translation. **HOLDS.**

**2. Multi-user against a real scenario (POST Drop 2 sheet):** the recorded manual flow "I worked the claim and now it's pay" is two personas — examiner workup, then supervisor adjustment. The test above is that flow: two role fixtures, two identities from the same credentials dict, sequential self-authenticating workflows in one browser, assertions via same-instance page state. No role-to-role reference anywhere. **HOLDS.**

## Contract Compliance

| Rule | Status |
|------|--------|
| Tasks via DI + identity as workflow config | PASS |
| Multiple Task modules per workflow (common + domain) | PASS |
| `-> None` norm; page-observable outcomes | PASS |
| No Interface receipt; no test knowledge | PASS |
| Composition rule: login+workup spans two modules — not a pass-through | PASS |

## What Does NOT Go Here

- No locators, waits, or page mechanics (L2)
- No decisions/filtering (L3)
- No assertions (L5)
- No cross-Role orchestration (tests sequence personas)
- No identity values (fixtures inject from the credentials fixture)
