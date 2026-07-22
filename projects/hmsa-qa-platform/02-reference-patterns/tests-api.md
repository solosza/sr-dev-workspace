# API Tests — Design Doc

## Governing Contract

`framework/docs/5-layer-contract.md` — Layer 5 rules; assertion targets for REST: **typed results returned by Tasks** (the norm) plus API Object state-checks (status, response time) on the same instance.

## Decision

Mirror of tests-ui with the assertion polarity flipped: REST Tasks return validated models, so tests assert on data first and transport state (status codes) second.

## Canonical Example

```python
"""test_user_management.py - Layer 5 (API). Assert typed results + same-instance transport state."""

import pytest
from framework.utilities.trace import trace


class TestUserManagement:

    @trace("Test")
    @pytest.mark.api
    def test_created_user_is_retrievable(self, user_management, users_api):
        """Created user comes back with server-assigned identity intact."""
        # Arrange / Act — typed result from the Task
        created = user_management.create_user("Ana Ignacio", "ana@example.com")

        # Assert — the model first (pydantic already validated the shape)...
        assert created.id > 0, "Server did not assign an id"
        assert created.email == "ana@example.com", "Email mutated in flight"

        # ...then transport state on the SAME API Object instance the Task used
        assert users_api.is_last_status_ok(), \
            f"Create returned HTTP {users_api.get_last_status()}"
        assert users_api.get_last_response_time() < 2.0, \
            "Create exceeded the 2s response budget"

        # Cleanup — explicit-cleanup discipline, API flavor
        assert user_management.ensure_user_absent(created.id), \
            "Cleanup failed — user persists"
```

**Schema breaks never reach asserts:** `get_last_body_as(Model)` inside the Task raises `ValidationError` naming the missing/wrong field — the test fails at the layer boundary with a precise message, which is the pydantic decision (2.1.2) paying off at Layer 5.

## Dry Run — Users CRUD (platform-playwright pattern, own repo)

**Subject:** the same CRUD chain as the tasks-rest-api dry run, now from the test's seat.

**Instantiation:** the canonical example verbatim. Both assertion families exercised: typed (`created.id`, `created.email`) and same-instance transport (`is_last_status_ok`, response time). Cleanup runs *inside* the test as a final assert — failed cleanup is a test failure, not a silent leak (explicit-cleanup discipline).

**Verdict: HOLDS.** One note kept: the response-time assert shows where non-functional budgets live (test body, per scenario) — NOT in the Interface as global timeouts. Nothing surfaced.

## Contract Compliance

| Rule | Status |
|------|--------|
| One AAA block; acts through Task | PASS |
| Dual assertion: typed result + same-instance state-checks | PASS |
| Cleanup as asserted step (explicit-cleanup discipline) | PASS |
| Failure messages throughout | PASS |

## What Does NOT Go Here

- No raw `requests` calls or endpoint strings (L1/L2 own transport)
- No schema definitions or manual field-presence checks (pydantic at L2/L3 boundary)
- No retry loops (shared retry utility at L3 when transient)
