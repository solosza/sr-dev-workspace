# Data Objects — Design Doc

## Governing Contract

`framework/docs/5-layer-contract.md` — Layer 2 rules apply:
- Constructor takes Interface instance(s) — composition, no inheritance
- NO decorators on any methods
- Table/schema config as class-level constants
- SQL owned by the Data Object (inline constants OR co-located `.sql` files)
- One atomic query per method (one business question = one method)
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
- Pydantic models for typed result access
- Parameterized queries only (`?` placeholders — never f-strings, never regex replacement)

## Decision

Rewrite from scratch. The `hmsa-healthcare-qa/_reference/data_objects/work_table.py` shows the concept but has anti-patterns: f-string SQL interpolation, raw list returns, no typing. New pattern uses parameterized queries, pydantic models, and follows the same return-self + state-check structure as Page Objects and API Objects.

## SDK

- `SqlServerInterface` (Layer 1 — wraps `mssql_python.Connection`)
- `pydantic` v2 (result model validation)

## What Is a Data Object?

The DB equivalent of a Page Object. A Page Object knows the page's locators and provides atomic UI actions. A Data Object knows the table's schema and provides atomic queries.

| Page Object | Data Object |
|-------------|-------------|
| Locators as class constants | SQL as constants or `.sql` files |
| One UI action per method | One query per method |
| Returns self for chaining | Returns self for chaining |
| State-check: `is_on_dashboard()` | State-check: `has_results()`, `get_count()` |
| Composes BrowserInterface | Composes SqlServerInterface |

## What Is "Atomic" for a Data Object?

**One business question = one method.** SQL complexity is irrelevant to atomicity.

A single-table `SELECT COUNT(*)` and a 50-line query with 6 subqueries and multiple JOINs are both atomic — each answers one question. What matters is the question boundary, not the query complexity.

| Atomic (one question) | NOT Atomic (multiple operations) |
|----------------------|----------------------------------|
| Count records by status | Count records AND update audit log |
| Find eligible subjects (50-line SQL, 6 joins) | Query subjects THEN insert notification |
| Check for duplicates (subquery + HAVING) | Validate data AND archive failures |
| Verify outcome after SP execution | Run SP AND query results in same method |

**Rule for the agent:** Read requirements or SQL, identify each distinct question being asked, map each question to one method. The SQL behind the method can be any complexity.

## Use Cases for Data Objects

Data Objects serve four purposes in enterprise test automation:

| Purpose | What It Does | Example |
|---------|-------------|---------|
| **Discovery** | Find eligible test subjects from broad criteria | Query all active members matching grade/status filters |
| **Validation** | Check preconditions before proceeding | Verify a record doesn't already exist, check for date conflicts |
| **Setup** | Insert/update test data | Create a test record, update status to trigger condition |
| **Verification** | Confirm outcomes after execution | Check record was created/updated, count output rows |

All four follow the same atomic method pattern. The Data Object doesn't decide WHAT to do with results — it just answers questions and performs writes. Layer 3 Tasks handle decisions, filtering, retry logic.

## SQL Ownership

The Data Object **owns** its queries. Format depends on complexity:

| SQL Length | Storage | Why |
|-----------|---------|-----|
| 1-5 lines | Class constant | Readable inline, no file overhead |
| 6+ lines | `.sql` file in co-located `sql/` folder | Maintainable, syntax-highlighted in IDE, reviewable by DBAs |

Both are parameterized with `?` placeholders. Never f-strings. Never regex replacement on SQL files.

```
framework/_reference/data_objects/
├── __init__.py
├── models/
│   └── order_models.py           ← pydantic models for row types
├── sql/
│   ├── find_eligible_orders.sql  ← complex queries live here
│   └── customer_summary.sql
└── orders_data_object.py         ← Data Object class
```

## Canonical Example: OrdersDataObject

```python
"""
OrdersDataObject - Layer 2 Component (Data Object)

Data Object for the orders table. Provides atomic query methods
for discovery, validation, setup, and verification.
"""

from pathlib import Path
from functools import cached_property
from interfaces.sql_server_interface import SqlServerInterface
from _reference.data_objects.models.order_models import OrderRow, OrderSummary


class OrdersDataObject:
    """
    Data Object for the Orders table.

    - Constructor takes SqlServerInterface — composition, no inheritance
    - NO decorators on any methods
    - SQL owned by this class (constants for short, files for complex)
    - One business question per method
    - Atomic methods return self for fluent chaining
    - State-check methods return bool, int, or typed pydantic models
    - Parameterized queries only (? placeholders, never f-strings)
    """

    def __init__(self, db: SqlServerInterface):
        """Compose SqlServerInterface — NO inheritance."""
        self.db = db
        self.last_results: list = []
        self.last_count: int = 0

    # === TABLE CONFIG (Class Constants) ===

    TABLE = "orders"
    SQL_DIR = Path(__file__).parent / "sql"

    # === SQL (Short queries as constants) ===

    COUNT_BY_STATUS_SQL = """
        SELECT COUNT(*) FROM orders WHERE status = ?
    """

    GET_BY_ID_SQL = """
        SELECT order_id, customer_id, status, total, created_at
        FROM orders WHERE order_id = ?
    """

    INSERT_ORDER_SQL = """
        INSERT INTO orders (order_id, customer_id, status, total, created_at)
        VALUES (?, ?, ?, ?, ?)
    """

    UPDATE_STATUS_SQL = """
        UPDATE orders SET status = ? WHERE order_id = ?
    """

    # === SQL (Complex queries loaded from files) ===

    @cached_property
    def find_eligible_sql(self) -> str:
        """Load complex discovery query from file."""
        return (self.SQL_DIR / "find_eligible_orders.sql").read_text()

    @cached_property
    def customer_summary_sql(self) -> str:
        """Load complex aggregate query from file."""
        return (self.SQL_DIR / "customer_summary.sql").read_text()

    # === DISCOVERY METHODS ===

    def query_eligible(self, status: str, min_total: float) -> "OrdersDataObject":
        """Find orders matching broad eligibility criteria."""
        self.last_results = self.db.execute_query(
            self.find_eligible_sql, (status, min_total)
        )
        return self

    def query_by_status(self, status: str) -> "OrdersDataObject":
        """How many orders have this status?"""
        self.last_count = self.db.execute_scalar(
            self.COUNT_BY_STATUS_SQL, (status,)
        )
        return self

    # === VALIDATION METHODS ===

    def query_by_id(self, order_id: str) -> "OrdersDataObject":
        """Does this order exist? Get its details."""
        self.last_results = self.db.execute_query(
            self.GET_BY_ID_SQL, (order_id,)
        )
        return self

    def query_customer_summary(self, customer_id: str) -> "OrdersDataObject":
        """What's the aggregate picture for this customer?"""
        self.last_results = self.db.execute_query(
            self.customer_summary_sql, (customer_id,)
        )
        return self

    # === SETUP METHODS (writes) ===

    def insert_order(self, order_id: str, customer_id: str, status: str,
                     total: float, created_at: str) -> "OrdersDataObject":
        """Insert a test order record."""
        self.last_count = self.db.execute_non_query(
            self.INSERT_ORDER_SQL, (order_id, customer_id, status, total, created_at)
        )
        return self

    def update_status(self, order_id: str, new_status: str) -> "OrdersDataObject":
        """Update an order's status."""
        self.last_count = self.db.execute_non_query(
            self.UPDATE_STATUS_SQL, (new_status, order_id)
        )
        return self

    # === VERIFICATION METHODS ===

    def verify_status(self, order_id: str, expected_status: str) -> "OrdersDataObject":
        """Verify an order has the expected status (post-execution check)."""
        self.last_count = self.db.execute_scalar(
            "SELECT COUNT(*) FROM orders WHERE order_id = ? AND status = ?",
            (order_id, expected_status)
        )
        return self

    # === STATE-CHECK METHODS ===

    def get_count(self) -> int:
        """Return last scalar count or rows-affected result."""
        return self.last_count

    def has_results(self) -> bool:
        """Check if last query returned any rows."""
        return len(self.last_results) > 0

    def result_count(self) -> int:
        """Count of rows in last result set."""
        return len(self.last_results)

    def get_results_as(self, model: type, columns: list[str] | None = None) -> list:
        """Parse last results into pydantic models.

        Args:
            model: Pydantic model class to validate against
            columns: Column names for positional mapping. If None, uses model field names.
        """
        cols = columns or list(model.model_fields.keys())
        return [model(**dict(zip(cols, row))) for row in self.last_results]

    def get_first_as(self, model: type, columns: list[str] | None = None) -> object:
        """Parse first row of last results into a pydantic model."""
        cols = columns or list(model.model_fields.keys())
        return model(**dict(zip(cols, self.last_results[0])))
```

## Pydantic Models

```python
"""
order_models.py - Pydantic models for order data

Row schemas for typed access to query results.
"""

from pydantic import BaseModel


class OrderRow(BaseModel):
    order_id: str
    customer_id: str
    status: str
    total: float
    created_at: str


class OrderSummary(BaseModel):
    customer_id: str
    name: str
    total_spent: float
    order_count: int
```

## Layer Boundary: What Goes Where

This is critical. The Data Object answers questions and performs writes. It does NOT make decisions, filter results in Python, retry, or orchestrate sequences. That's Layer 3.

| Responsibility | Layer | Example |
|---------------|-------|---------|
| Execute one query | Layer 2 (Data Object) | `query_eligible()` returns all matching rows |
| Filter results by business logic | Layer 3 (Task) | Exclude invalid records, narrow candidates |
| Pick a subject (random, first-match, etc.) | Layer 3 (Task) | `random.choice(eligible)` |
| Retry with different subject | Layer 3 (Task) | Loop: pick → validate → retry if invalid |
| Compose multiple Data Object calls | Layer 3 (Task) | Query eligible → validate → setup → verify |
| Insert/update test data | Layer 2 (Data Object) | `insert_order()`, `update_status()` |
| Decide WHAT to insert based on discovery | Layer 3 (Task) | Use discovered data to compose the write |

### Example: How Discovery Flows Through Layers

```
Layer 2 (Data Object):
  query_eligible(criteria)     → returns broad result set
  validate_precondition(id)    → checks one specific record
  insert_test_record(data)     → creates one row
  verify_outcome(id, expected) → confirms result

Layer 3 (Task):
  1. Call data_object.query_eligible(criteria)
  2. Get results → filter in Python (exclude invalids)
  3. Pick a candidate (random, first-match)
  4. Call data_object.validate_precondition(candidate.id)
  5. If invalid → pick another (retry loop)
  6. Call data_object.insert_test_record(composed_data)
  7. [Trigger action — SP, UI, API]
  8. Call data_object.verify_outcome(id, expected_status)

Layer 5 (Test):
  assert data_object.get_count() > 0
  assert data_object.has_results()
```

## How the Agent Builds Data Objects Dynamically

Given any table, verification SQL, or requirements:

1. **Identify questions** — each SELECT or logical check = one question = one method
2. **Categorize** — is this discovery, validation, setup, or verification?
3. **Determine SQL storage** — short (≤5 lines) → class constant. Long → `.sql` file.
4. **Name the method** — after the question: `query_[what]`, `count_[what]`, `verify_[what]`, `insert_[what]`
5. **Choose Interface method:**
   - Scalar (counts, sums) → `execute_scalar` → store in `self.last_count`
   - Result set (rows) → `execute_query` → store in `self.last_results`
   - Single row → `execute_query_one` → store in `self.last_results`
   - Write (INSERT/UPDATE/DELETE) → `execute_non_query` → store rows-affected in `self.last_count`
   - Batch write → `execute_many` → store rows-affected in `self.last_count`
6. **Define pydantic model** — one model per distinct result shape
7. **Wire state-check** — `get_count()` for scalars, `get_results_as(Model)` for typed rows

## Uniform Layer 2 Pattern

| Layer 2 Type | Constants | Atomic Methods | State-Check Methods |
|-------------|-----------|----------------|-------------------|
| Page Object | Locators (By, selector) | UI action → return self | `is_*()`, `has_*()` → bool |
| API Object | Endpoint paths | HTTP call → return self | `get_last_status()`, `get_last_body_as()` |
| Data Object | SQL (constants + files) | DB query/write → return self | `get_count()`, `get_results_as()`, `has_results()` |

Same structure. Same mental model. Same conventions.

## Contract Compliance

| Rule | Status |
|------|--------|
| Constructor takes Interface — composition | PASS |
| NO decorators | PASS |
| SQL owned by Data Object (constants + files) | PASS |
| One atomic query per method | PASS — one question = one method |
| Returns self for chaining | PASS |
| State-check methods return primitives | PASS |
| Domain vocabulary in method names | PASS |
| No knowledge of upper layers | PASS |
| Parameterized queries only | PASS — ? placeholders, never f-strings |
| Pydantic for typed results | PASS |

## Dependencies

- `SqlServerInterface` (Layer 1)
- `pydantic` v2 (BaseModel)
- `pathlib` (stdlib — SQL file paths)
- `functools` (stdlib — cached_property for SQL file loading)
- `typing` (stdlib)

## What Does NOT Go Here

- No Python filtering of results (Layer 3 Task narrows broad result sets)
- No retry/selection logic (Layer 3 Task picks subjects, retries on failure)
- No multi-Data-Object orchestration (Layer 3 composes multiple Data Objects)
- No connection management (factory, 3.5)
- No assertions (Layer 5 Tests)
- No workflow decisions (Layer 3 decides what to query/write based on prior results)
