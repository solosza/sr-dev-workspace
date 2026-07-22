# API Objects — Design Doc

## Governing Contract

`framework/docs/5-layer-contract.md` — Layer 2 rules apply:
- Constructor takes Interface instance(s) — composition, no inheritance
- NO decorators on any methods
- Endpoint paths as class-level constants
- One atomic API operation per method
- Atomic methods return `self` for fluent chaining
- State-check methods return `bool` or primitive for assertions
- Method names use domain vocabulary
- Only imports from Interface layer or utilities
- No knowledge of Tasks, Roles, or Tests
- Module-level docstring states file purpose and layer
- Class docstring lists structural rules as bullet points
- Docstring on every method
- Methods organized by category with section headers (`# === CATEGORY ===`)
- Type hints on all parameters and return types

## Decision

Translate from `platform-playwright/framework/_reference/apis/users-api.ts` (207 lines TypeScript). Already 5-layer compliant. Add pydantic models for response validation (industry standard for Python API testing, not in the TS version).

## SDK

- `ApiInterface` (Layer 1 — wraps `requests.Session`)
- `pydantic` v2 (response model validation — `BaseModel`, `model_validate`)

## Pattern Structure

```
framework/_reference/api_objects/
├── __init__.py
├── models/
│   └── user_models.py       ← pydantic request/response models
└── users_api_object.py      ← API Object class
```

## What Changes from platform-playwright

| Aspect | platform-playwright (TS) | HMSA QA Platform (Python) | Why |
|--------|--------------------------|--------------------------|-----|
| Language | TypeScript interfaces for types | Pydantic BaseModel | Runtime validation, auto-coercion, schema generation |
| Async | `async/await` | Synchronous | requests is sync — matches ApiInterface |
| Generic types | `<T>` on methods | `model_validate(ModelClass)` | Python pattern for typed parsing |
| Response access | `this.lastResponse` | `self.last_response` | Same pattern, Python naming |
| Validation | Manual — caller checks fields | Automatic — pydantic raises `ValidationError` | Catches API contract breaks without explicit asserts |

## Canonical Example: UsersApiObject

```python
"""
UsersApiObject - Layer 2 Component (API Object)

API Object representing the Users REST resource.
Provides atomic API interactions via ApiInterface composition.
"""

from interfaces.api_interface import ApiInterface, ApiResponse
from _reference.api_objects.models.user_models import (
    CreateUserRequest, UpdateUserRequest, UserResponse, UserListResponse
)


class UsersApiObject:
    """
    API Object for the Users REST resource.

    - Constructor takes ApiInterface — composition, no inheritance
    - NO decorators on any methods
    - Endpoint paths as class constants
    - One atomic API operation per method
    - Atomic methods return self for fluent chaining
    - State-check methods return bool or primitive
    - Pydantic models for request/response typing
    """

    def __init__(self, api: ApiInterface):
        """Compose ApiInterface — NO inheritance."""
        self.api = api
        self.last_response: ApiResponse | None = None

    # === ENDPOINT CONFIG (Class Constants) ===

    BASE_PATH = "/api/users"

    @staticmethod
    def single_path(user_id: int) -> str:
        return f"/api/users/{user_id}"

    # === CRUD METHODS (One API Operation) ===

    def get_all(self, page: int = 1, per_page: int = 20) -> "UsersApiObject":
        """Get all users with pagination."""
        self.last_response = self.api.get(
            self.BASE_PATH, params={"page": page, "perPage": per_page}
        )
        return self

    def get_by_id(self, user_id: int) -> "UsersApiObject":
        """Get a single user by ID."""
        self.last_response = self.api.get(self.single_path(user_id))
        return self

    def create(self, data: CreateUserRequest) -> "UsersApiObject":
        """Create a new user."""
        self.last_response = self.api.post(
            self.BASE_PATH, json=data.model_dump()
        )
        return self

    def update(self, user_id: int, data: UpdateUserRequest) -> "UsersApiObject":
        """Update a user by ID (full replacement)."""
        self.last_response = self.api.put(
            self.single_path(user_id), json=data.model_dump(exclude_unset=True)
        )
        return self

    def patch(self, user_id: int, data: UpdateUserRequest) -> "UsersApiObject":
        """Partially update a user by ID."""
        self.last_response = self.api.patch(
            self.single_path(user_id), json=data.model_dump(exclude_unset=True)
        )
        return self

    def delete(self, user_id: int) -> "UsersApiObject":
        """Delete a user by ID."""
        self.last_response = self.api.delete(self.single_path(user_id))
        return self

    # === STATE-CHECK METHODS (For Assertions) ===

    def get_last_status(self) -> int:
        """Get HTTP status code of last response."""
        return self.last_response.status

    def get_last_body(self) -> dict:
        """Get raw response body as dict."""
        return self.last_response.body

    def get_last_body_as(self, model: type) -> object:
        """Validate and parse last response body into a pydantic model."""
        return model.model_validate(self.last_response.body)

    def get_last_response_time(self) -> float:
        """Get response time of last call in seconds."""
        return self.last_response.response_time

    def is_last_status_ok(self) -> bool:
        """Check if last response was 2xx."""
        return 200 <= self.last_response.status < 300
```

## Pydantic Models

```python
"""
user_models.py - Pydantic models for Users API

Request and response schemas. Provides runtime validation,
auto-coercion, and clear documentation of API contracts.
"""

from pydantic import BaseModel


class CreateUserRequest(BaseModel):
    name: str
    email: str
    role: str = "default"


class UpdateUserRequest(BaseModel):
    name: str | None = None
    email: str | None = None
    role: str | None = None


class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    role: str
    created_at: str


class UserListResponse(BaseModel):
    users: list[UserResponse]
    total: int
    page: int
    per_page: int
```

## How Pydantic Fits

| Concern | Without Pydantic | With Pydantic |
|---------|-----------------|---------------|
| Response structure check | Manual asserts in every test | Automatic — `model_validate` raises `ValidationError` |
| Type coercion | Manual casting | Auto — string "123" → int 123 |
| Missing fields | Silent `None` or KeyError | Immediate `ValidationError` with field name |
| Schema documentation | Comments or external docs | Model IS the documentation |
| Test data generation | Manual fixtures | `ModelClass(**factory_data)` validates on creation |

**Key rule:** Pydantic models live in `models/` subfolder within each API Object directory. They're shared by the API Object and by test fixtures. Layer 3+ imports them for typing but never defines them.

## SOAP API Objects — Same Pattern

SOAP API Objects follow the identical pattern — the only difference is the interface:

```python
class CustomerServiceObject:
    def __init__(self, soap: SoapInterface):
        self.soap = soap
        self.last_response = None

    def get_customer(self, customer_id: str) -> "CustomerServiceObject":
        self.last_response = self.soap.call_operation("GetCustomer", CustomerID=customer_id)
        return self

    def get_order_status(self, order_id: str) -> "CustomerServiceObject":
        self.last_response = self.soap.call_operation("GetOrderStatus", OrderID=order_id)
        return self

    def get_last_body_as(self, model: type) -> object:
        # zeep returns dicts — pydantic validates them identically
        return model.model_validate(self.last_response)
```

<!-- Renamed 2026-07-17 (was MemberServiceObject/GetMemberInfo — pre-Orderly healthcare vocabulary; caught by 211 orchestrator gates). Operations now match harness-app.md V4: GetCustomer, GetOrderStatus. -->


zeep deserializes XML → dict. Pydantic validates dict → typed model. Same flow as REST.

## Contract Compliance

| Rule | Status |
|------|--------|
| Constructor takes Interface — composition | PASS |
| NO decorators | PASS |
| Endpoint config as class constants | PASS |
| One atomic operation per method | PASS |
| Returns self for chaining | PASS |
| State-check methods return primitives | PASS |
| Domain vocabulary in method names | PASS |
| No knowledge of upper layers | PASS |
| Type hints on all parameters/returns | PASS |

## Dependencies

- `ApiInterface` (Layer 1)
- `pydantic` v2 (BaseModel, model_validate)
- `typing` (stdlib)

## What Does NOT Go Here

- No multi-endpoint workflows (Layer 3 Tasks)
- No auth token management (handled by Interface or conftest fixture)
- No retry logic (conftest plugin or Layer 2 utility)
- No test assertions (Layer 5 Tests)
- No pagination orchestration (separate PaginationComponent if needed)
