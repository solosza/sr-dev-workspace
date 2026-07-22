# Hybrid Tasks — Design Doc

## Governing Contract

`framework/docs/5-layer-contract.md` — Layer 3 rules apply:
- Constructor takes Layer 2 object instances — composition, no inheritance
- `@trace("Task")` decorator on every public method
- Makes decisions: filtering, retry, selection, sequencing
- Orchestrates Layer 2 objects (single or multiple interfaces)
- Returns typed results (pydantic models, dicts, named tuples)
- No knowledge of Roles or Tests
- Module-level docstring states file purpose and layer
- Class docstring lists structural rules as bullet points
- Docstring on every method
- Type hints on all parameters and return types

## Decision

Build from scratch. No existing reference in any platform repo. The Task layer is where single-interface and multi-interface orchestration converge — same structure, same pattern, different scope.

## SDK

- Layer 2 objects (Data Objects, Page Objects, API Objects) — injected via constructor
- `trace.py` — `@trace("Task")` decorator for observability
- `pydantic` v2 (result models)
- `random` (stdlib — subject selection)
- `time` (stdlib — retry delays)

## What Is a Task?

The orchestration layer. A Task composes Layer 2 objects to accomplish a domain operation that requires decisions, sequencing, or multi-step logic.

| Single-Interface Task | Multi-Interface (Hybrid) Task |
|----------------------|-------------------------------|
| Composes ONE Layer 2 type | Composes TWO+ Layer 2 types |
| e.g., discovery + validation via DB | e.g., DB setup + UI action + DB verify |
| Same structure, same decorator | Same structure, same decorator |
| Most tests use these | Complex enterprise workflows use these |

**Key insight:** There is no structural difference between single and hybrid tasks. A Task that takes one Data Object and a Task that takes a Data Object + Page Object + API Object follow the identical pattern. The constructor just receives more objects.

## Pattern Structure

```
framework/_reference/tasks/
├── __init__.py
├── discovery_tasks.py         ← single-interface (DB only)
├── workflow_tasks.py          ← multi-interface (DB + UI + API)
└── utilities/
    └── retry.py              ← lightweight retry utility
```

## What a Task Does (Decision Matrix)

| Responsibility | Layer 2 (Object) | Layer 3 (Task) |
|---------------|-------------------|----------------|
| Execute one query/action | YES | NO |
| Filter results in Python | NO | YES |
| Pick a subject (random, first-match) | NO | YES |
| Retry with different subject | NO | YES |
| Sequence multiple operations | NO | YES |
| Compose across interfaces | NO | YES |
| Make business logic decisions | NO | YES |
| Return typed domain results | NO | YES |

## Canonical Example 1: Single-Interface Task (DB Only)

```python
"""
DiscoveryTasks - Layer 3 Task

Orchestrates Data Object queries to find and validate eligible test subjects.
Single-interface: uses only SqlServerInterface via Data Objects.
"""

from framework.utilities.trace import trace
from _reference.data_objects.orders_data_object import OrdersDataObject
from _reference.data_objects.models.order_models import OrderRow

import random


class DiscoveryTasks:
    """
    Task: Find eligible test subjects from the database.

    - Constructor takes Layer 2 Data Object(s) — composition
    - @trace("Task") on every public method
    - Makes decisions: filter, select, retry
    - Returns typed results (pydantic models or primitives)
    - No knowledge of Roles or Tests
    """

    def __init__(self, orders_data: OrdersDataObject):
        """Compose Layer 2 Data Object(s)."""
        self.orders_data = orders_data

    @trace("Task")
    def find_eligible_order(self, status: str, min_total: float,
                            exclusion_list: list[str] | None = None) -> OrderRow:
        """Find a valid test order by querying, filtering, and validating.

        Decision logic:
        1. Broad query via Data Object
        2. Filter in Python (exclude known-bad)
        3. Pick random candidate
        4. Validate preconditions
        5. Retry if invalid
        """
        exclusions = exclusion_list or []

        # Step 1: Broad query
        self.orders_data.query_eligible(status, min_total)

        if not self.orders_data.has_results():
            raise NoEligibleSubjectError(f"No orders with status={status}, min_total={min_total}")

        # Step 2: Get typed results + filter
        candidates = self.orders_data.get_results_as(OrderRow)
        candidates = [c for c in candidates if c.order_id not in exclusions]

        if not candidates:
            raise NoEligibleSubjectError("All candidates excluded")

        # Step 3-5: Pick + validate + retry
        for candidate in random.sample(candidates, min(5, len(candidates))):
            self.orders_data.query_by_id(candidate.order_id)
            order = self.orders_data.get_first_as(OrderRow)

            # Validate: still in expected status (not grabbed by another process)
            if order.status == status:
                return order

        raise NoEligibleSubjectError("All sampled candidates failed validation")

    @trace("Task")
    def count_orders_by_status(self, status: str) -> int:
        """Simple delegation — still a Task because it's a domain operation."""
        self.orders_data.query_by_status(status)
        return self.orders_data.get_count()


class NoEligibleSubjectError(Exception):
    """Raised when no valid test subject can be found."""
    pass
```

## Canonical Example 2: Multi-Interface (Hybrid) Task

```python
"""
WorkflowTasks - Layer 3 Task (Hybrid)

Orchestrates multiple Layer 2 objects across DB, UI, and API interfaces
to execute enterprise test workflows.
"""

from framework.utilities.trace import trace
from _reference.data_objects.orders_data_object import OrdersDataObject
from _reference.pages.admin_page import AdminPage
from _reference.api_objects.processing_api_object import ProcessingApiObject
from _reference.tasks.discovery_tasks import DiscoveryTasks
from _reference.data_objects.models.order_models import OrderRow


class WorkflowTasks:
    """
    Task: Execute multi-interface enterprise workflows.

    - Constructor takes multiple Layer 2 objects — hybrid composition
    - @trace("Task") on every public method
    - Composes single-interface Tasks for reusable sub-operations
    - Sequences operations across interfaces
    - Returns verification results
    """

    def __init__(self, orders_data: OrdersDataObject, admin_page: AdminPage,
                 processing_api: ProcessingApiObject, discovery: DiscoveryTasks):
        """Compose Layer 2 objects + reusable Tasks."""
        self.orders_data = orders_data
        self.admin_page = admin_page
        self.processing_api = processing_api
        self.discovery = discovery

    @trace("Task")
    def setup_and_trigger_processing(self, status: str, min_total: float,
                                     config_value: str) -> OrderRow:
        """Set up preconditions across DB + UI, then trigger processing via API.

        Workflow:
        1. Find eligible order (DB — via reusable Task)
        2. Configure processing settings (UI)
        3. Trigger processing (API)
        4. Return the subject for downstream verification
        """
        # Step 1: Find subject (delegates to single-interface Task)
        order = self.discovery.find_eligible_order(status, min_total)

        # Step 2: UI configuration
        self.admin_page.navigate_to_settings()
        self.admin_page.enter_config_value(config_value)
        self.admin_page.click_save()

        # Step 3: Trigger via API
        self.processing_api.trigger_processing(order.order_id)

        return order

    @trace("Task")
    def verify_processing_outcome(self, order_id: str,
                                  expected_status: str) -> dict:
        """Verify outcomes across multiple interfaces after processing.

        Checks:
        1. DB: order status updated
        2. API: processing record exists
        3. UI: confirmation displayed (optional)
        """
        # DB verification
        self.orders_data.verify_status(order_id, expected_status)
        status_ok = self.orders_data.get_count() > 0

        # API verification
        self.processing_api.get_status(order_id)
        api_ok = self.processing_api.is_last_status_ok()

        return {
            "status_ok": status_ok,
            "api_ok": api_ok,
            "order_id": order_id,
        }
```

## Task Composition: Tasks Calling Tasks

Tasks can compose other Tasks. This is how complex workflows stay readable:

```python
# WorkflowTasks composes DiscoveryTasks
self.discovery = DiscoveryTasks(orders_data)

# Then delegates the discovery sub-operation:
order = self.discovery.find_eligible_order(status, min_total)
```

**Rules for Task composition:**
- A Task can receive another Task via constructor (injected by conftest)
- A Task NEVER instantiates another Task directly — always injected
- Keep the chain shallow: max 2 levels (Task → Task → Layer 2). Deeper = refactor.

## Retry Utility

```python
"""
retry.py - Layer 3 Utility

Lightweight retry with backoff for flaky operations (DB timeouts, network blips).
Used by Tasks when an operation may transiently fail.
"""

import time
from typing import Callable, TypeVar

T = TypeVar("T")


def retry_operation(
    operation: Callable[[], T],
    max_attempts: int = 3,
    delay_seconds: float = 1.0,
    backoff_factor: float = 2.0,
    exceptions: tuple = (Exception,),
) -> T:
    """Retry an operation with exponential backoff.

    Args:
        operation: Zero-arg callable to retry
        max_attempts: Maximum number of attempts
        delay_seconds: Initial delay between retries
        backoff_factor: Multiplier for delay after each failure
        exceptions: Tuple of exception types to catch and retry

    Returns:
        Result of successful operation call

    Raises:
        Last exception if all attempts fail
    """
    last_error = None
    delay = delay_seconds

    for attempt in range(max_attempts):
        try:
            return operation()
        except exceptions as e:
            last_error = e
            if attempt < max_attempts - 1:
                time.sleep(delay)
                delay *= backoff_factor

    raise last_error
```

**Usage in a Task:**
```python
@trace("Task")
def trigger_with_retry(self, order_id: str) -> None:
    """Trigger processing with retry on transient API failures."""
    retry_operation(
        lambda: self.processing_api.trigger_processing(order_id),
        max_attempts=3,
        exceptions=(ConnectionError, TimeoutError),
    )
```

## Fixture Wiring (Conftest)

Tasks receive Layer 2 objects via fixtures. Hybrid tasks receive multiple:

```python
# Layer 2 fixtures
@pytest.fixture
def orders_data(db):
    return OrdersDataObject(db)

@pytest.fixture
def admin_page(browser):
    return AdminPage(browser)

@pytest.fixture
def processing_api(api):
    return ProcessingApiObject(api)

# Layer 3 fixtures (single-interface)
@pytest.fixture
def discovery(orders_data):
    return DiscoveryTasks(orders_data)

# Layer 3 fixtures (hybrid)
@pytest.fixture
def workflow(orders_data, admin_page, processing_api, discovery):
    return WorkflowTasks(orders_data, admin_page, processing_api, discovery)
```

## How Tests Use Tasks

Layer 5 tests receive Tasks (or Roles that wrap Tasks) and assert on results:

```python
class TestOrderProcessing:

    def test_eligible_order_processed(self, workflow):
        """Eligible order should reach COMPLETE status after processing."""
        order = workflow.setup_and_trigger_processing(
            status="PENDING", min_total=100.0, config_value="AUTO"
        )
        result = workflow.verify_processing_outcome(order.order_id, "COMPLETE")

        assert result["status_ok"], "Order not moved to COMPLETE"
        assert result["api_ok"], "Processing API has no record"

    def test_ineligible_order_unchanged(self, discovery, orders_data):
        """Orders below threshold should not be processed."""
        order = discovery.find_eligible_order("PENDING", min_total=0.01)
        # [no processing triggered]
        orders_data.verify_status(order.order_id, "PENDING")

        assert orders_data.get_count() > 0, "Order status changed unexpectedly"
```

## Contract Compliance

| Rule | Status |
|------|--------|
| Constructor takes Layer 2 objects — composition | PASS |
| @trace("Task") on every public method | PASS |
| Makes decisions (filter, retry, select) | PASS |
| Returns typed results | PASS |
| No knowledge of Roles or Tests | PASS |
| Domain vocabulary in method names | PASS |
| Type hints on all parameters/returns | PASS |
| Docstrings on module, class, and methods | PASS |

## Dependencies

- Layer 2 objects (Data Objects, Page Objects, API Objects)
- `trace.py` (framework utility — `@trace("Task")`)
- `pydantic` v2 (result models, shared with Layer 2)
- `random` (stdlib — candidate selection)
- `time` (stdlib — retry delays)
- `typing` (stdlib)

## What Does NOT Go Here

- No direct SDK/Interface calls (that's Layer 2)
- No test assertions (that's Layer 5)
- No user identity/persona (that's Layer 4 Roles)
- No connection management (that's fixtures/conftest)
- No locators, SQL, or endpoint paths (that's Layer 2 constants)
