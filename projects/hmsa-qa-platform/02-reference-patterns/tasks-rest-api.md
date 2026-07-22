# REST API Tasks — Design Doc

## Governing Contract

`framework/docs/5-layer-contract.md` — Layer 3 rules + REST addendum:
- Constructor takes API Objects via DI
- `@trace("Task")` on public methods
- **Typed returns are the norm** — no page to observe; results flow up as pydantic models
- One domain operation per method; retry via shared `retry.py` only; no endpoints at L3

## Decision

Build on the API Object pattern already designed in [[api-objects]] (UsersApiObject + pydantic models). The Task layer adds what the API Object must not do: sequencing, decisions, and response-to-domain translation.

## Canonical Example

```python
"""UserManagementTasks - Layer 3 Task (REST). Typed results flow up."""

from framework.utilities.trace import trace
from _reference.api_objects.users_api_object import UsersApiObject
from _reference.api_objects.models.user_models import (
    CreateUserRequest, UserResponse
)


class UserManagementTasks:
    """
    - Constructor takes API Object via DI
    - @trace("Task") on public methods
    - Returns validated pydantic models — API contract breaks fail loudly here
    """

    def __init__(self, users_api: UsersApiObject):
        self.users_api = users_api

    @trace("Task")
    def create_user(self, name: str, email: str, role: str = "default") -> UserResponse:
        """Create a user; return the validated created entity."""
        request = CreateUserRequest(name=name, email=email, role=role)
        self.users_api.create(request)
        if not self.users_api.is_last_status_ok():
            raise UserOperationError(
                f"Create failed: HTTP {self.users_api.get_last_status()}")
        return self.users_api.get_last_body_as(UserResponse)

    @trace("Task")
    def ensure_user_absent(self, user_id: int) -> bool:
        """Idempotent cleanup: delete if present. Decision logic lives here."""
        self.users_api.get_by_id(user_id)
        if self.users_api.get_last_status() == 404:
            return False
        self.users_api.delete(user_id)
        return self.users_api.is_last_status_ok()


class UserOperationError(Exception):
    """Domain exception — raised when an API operation cannot proceed."""
```

Status-code checking is a *decision* (proceed vs raise) → Layer 3. The raw check (`is_last_status_ok`) is a state-read → Layer 2. Domain exceptions defined here per contract error rule 4.

## Dry Run — Users CRUD Chain (platform-playwright pattern, own repo)

**Subject:** the create → fetch → update → delete flow the UsersApiObject design was translated from.

**Instantiation:** `create_user("Ana","ana@x.com")` → typed `UserResponse` with real `id` → `ensure_user_absent(user.id)` for cleanup. Each hop re-validates via pydantic — a missing response field fails at the Task boundary with a `ValidationError` naming the field, not three layers later.

**Verdict: HOLDS.** One note worth keeping (not a conflict): idempotent-cleanup tasks like `ensure_user_absent` are the API-side implementation of the **explicit-cleanup discipline** settled for DB writes (conftest walkthrough §7) — same principle, second interface. The pattern generalizes.

## Contract Compliance

| Rule | Status |
|------|--------|
| DI constructor (API Object, not Interface) | PASS |
| Typed pydantic returns | PASS |
| Decisions at L3 (status → proceed/raise), state-reads at L2 | PASS |
| Domain exception per error rule 4 | PASS |
| No endpoints/paths at L3 | PASS |

## What Does NOT Go Here

- No pagination loops as hidden state (a paginated fetch is its own explicit method)
- No auth handling (Interface/conftest)
- No response schema definitions (L2 `models/`)
- No assertions (L5 asserts on the returned models)
