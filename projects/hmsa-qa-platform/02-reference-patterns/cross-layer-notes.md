# Cross-Layer Notes — Enterprise Test Workflow Pattern

## Purpose

Documents how enterprise test workflows flow through all 5 layers. Derived from proven production patterns (v2 assignment-based pays, HMSA readmission autopend). Reference this when building any project-specific test suite.

## The Enterprise Test Workflow

Enterprise tests follow a common lifecycle regardless of domain:

```
DISCOVER → VALIDATE → SETUP → EXECUTE → VERIFY
```

| Phase | What Happens | Layer |
|-------|-------------|-------|
| **Discover** | Find eligible test subjects from DB | L2 Data Object → L3 Task (filters/selects) |
| **Validate** | Check preconditions, ensure subject is usable | L2 Data Object → L3 Task (retry if invalid) |
| **Setup** | Create/modify test data, configure preconditions | L2 Data Object (writes) + L2 Page/API Object (UI/API config) |
| **Execute** | Perform the action under test | L3 Task (orchestrates) → L4 Role (multi-user) |
| **Verify** | Confirm outcomes match expectations | L2 Data Object (queries) → L5 Test (asserts) |

## Layer Responsibilities Per Phase

### Layer 1 — Interface (SDK Wrapper)

Does not know about test phases. Executes one SDK call per method.

- **DB:** `execute_query`, `execute_scalar`, `execute_non_query`, `execute_sproc`
- **UI:** `click`, `type`, `wait_for_element_visible`
- **API:** `get`, `post`, `put`, `delete`
- **SOAP:** `call_operation`, `create_object`

No decisions. No filtering. No retry. Just SDK calls.

### Layer 2 — Components (Page / API / Data Objects)

Answers one question per method. Returns self for chaining. State-check for assertions.

- **Data Object (Discovery):** `query_eligible_subjects()` — returns broad result set
- **Data Object (Validation):** `verify_no_conflicts()` — checks one precondition
- **Data Object (Setup):** `insert_test_record()` — creates one row
- **Data Object (Verification):** `verify_outcome()` — checks post-execution state
- **Page Object:** `enter_field()`, `click_submit()`, `is_toast_displayed()`
- **API Object:** `create_resource()`, `get_last_status()`

No filtering logic. No retry. No subject selection. No multi-step orchestration.

### Layer 3 — Tasks (Domain Operations)

Orchestrates Layer 2 objects. Makes decisions. Filters. Retries. Composes.

**Discovery + Selection:**
```python
@trace("Task")
def find_test_subject(self, criteria: dict) -> SubjectModel:
    """Find and validate an eligible test subject."""
    # Broad query via Data Object
    self.subjects_data.query_eligible(criteria)
    candidates = self.subjects_data.get_results_as(SubjectModel)

    # Filter in Python (business logic)
    candidates = [c for c in candidates if c.id not in self.exclusion_list]

    # Pick + validate (retry loop)
    for candidate in random.sample(candidates, min(5, len(candidates))):
        self.subjects_data.validate_precondition(candidate.id)
        if self.subjects_data.get_count() == 0:  # no conflicts
            return candidate

    raise NoEligibleSubjectError("All candidates failed validation")
```

**Setup (multi-interface):**
```python
@trace("Task")
def configure_preconditions(self, subject: SubjectModel, config: dict) -> None:
    """Set up all preconditions for the test subject."""
    # DB setup
    self.data_object.insert_test_record(subject.id, config["status"])

    # UI setup (if needed — configure settings via browser)
    self.page_object.navigate_to_settings()
    self.page_object.enter_config_value(config["setting"])
    self.page_object.click_save()

    # API setup (if needed — trigger background process)
    self.api_object.trigger_process(subject.id)
```

**Verification:**
```python
@trace("Task")
def verify_outcome(self, subject_id: str, expected: dict) -> VerificationResult:
    """Verify all expected outcomes after execution."""
    self.data_object.verify_status(subject_id, expected["status"])
    status_ok = self.data_object.get_count() > 0

    self.data_object.verify_record_created(subject_id, expected["record_type"])
    record_ok = self.data_object.get_count() > 0

    return VerificationResult(status_ok=status_ok, record_ok=record_ok)
```

### Layer 4 — Roles (Who)

Wraps Tasks with identity. Represents a user persona performing actions.

```python
class SystemValidator:
    """Role: automated system that runs SP and validates output."""

    @trace("Role Constructor")
    def __init__(self, discovery: DiscoveryTasks, verification: VerificationTasks):
        """Compose Tasks via DI — Roles never instantiate Tasks (conftest wires them)."""
        self.discovery = discovery
        self.verification = verification

    @trace("Role")
    def validate_sp_execution(self, params: dict) -> dict:
        subject = self.discovery.find_test_subject(params["criteria"])
        # [execution happens — SP runs, batch processes, etc.]
        return self.verification.verify_outcome(subject.id, params["expected"])
```

```python
class ConfigAdmin:
    """Role: admin user who sets up preconditions via UI."""

    @trace("Role Constructor")
    def __init__(self, setup: SetupTasks):
        """Compose Tasks via DI — Roles never instantiate Tasks (conftest wires them)."""
        self.setup = setup

    @trace("Role")
    def configure_test_environment(self, subject: SubjectModel, config: dict) -> None:
        self.setup.configure_preconditions(subject, config)
```

### Layer 5 — Tests (Assertions)

AAA pattern. Receives Roles via fixtures. Asserts on typed results.

```python
class TestOrderProcessing:

    def test_eligible_order_gets_processed(self, system_validator, run_params):
        """Eligible orders should be processed to COMPLETE status."""
        results = system_validator.validate_sp_execution(run_params)

        assert results["status_ok"], "Order was not moved to expected status"
        assert results["record_ok"], "Processing record was not created"

    def test_ineligible_order_not_processed(self, system_validator, ineligible_params):
        """Ineligible orders should remain unchanged."""
        results = system_validator.validate_sp_execution(ineligible_params)

        assert not results["status_ok"], "Ineligible order was incorrectly processed"
```

## Fixture Wiring (Conftest)

Fixtures build the layer stack:

```python
# Layer 1 — Interface
@pytest.fixture(scope="session")
def db_connection(config):
    conn = mssql_python.connect(config["connection_string"])
    yield conn
    conn.close()

@pytest.fixture(scope="session")
def db(db_connection, config, logger):
    return SqlServerInterface(db_connection, config, logger)

# Layer 2 — Data Objects
@pytest.fixture
def orders_data(db):
    return OrdersDataObject(db)

# Layer 3 — Tasks
@pytest.fixture
def discovery_tasks(orders_data):
    return DiscoveryTasks(orders_data)

@pytest.fixture
def verification_tasks(orders_data):
    return VerificationTasks(orders_data)

# Layer 4 — Roles (receive Tasks via DI — never an Interface)
@pytest.fixture
def system_validator(discovery_tasks, verification_tasks):
    return SystemValidator(discovery_tasks, verification_tasks)
```

## Key Principle: Data Flows DOWN, Decisions Flow UP

```
Layer 5 (Test)   → passes params DOWN to Role
Layer 4 (Role)   → orchestrates Tasks, returns results UP
Layer 3 (Task)   → calls Data Objects, makes decisions, returns UP
Layer 2 (Object) → queries/writes, stores results, returns self
Layer 1 (Interface) → executes SDK call, returns primitive
```

- **Down:** Configuration, parameters, criteria
- **Up:** Results, typed models, verification outcomes
- **Decisions (filtering, retry, selection):** Layer 3 only
- **Assertions:** Layer 5 only

## Handling "Wait" Steps

Enterprise workflows often have human/batch steps that can't be automated:

```
SETUP → [WAIT: batch job runs overnight] → VERIFY
```

The test handles this by splitting into phases:

| Pattern | How |
|---------|-----|
| **Same-session** | SP call is automated — execute and verify in one test |
| **Split-session** | Setup in one run, verify in next run after batch completes |
| **Mock the wait** | Trigger the SP/batch directly in test (if accessible) |

For split-session, test data (subject IDs, expected outcomes) persists in fixtures/JSON between runs. The verification test reads the fixture and checks outcomes.

## Anti-Patterns to Avoid

| Anti-Pattern | Correct Pattern |
|-------------|-----------------|
| SQL regex replacement on files | Parameterized queries with `?` |
| Re-creating DB connection mid-test | Session-scoped connection fixture |
| Filtering results inside Data Object | Data Object returns broad set, Task filters |
| Multi-step orchestration in Data Object | Single query per method, Task orchestrates |
| Hardcoded test subjects | Discovery query finds eligible subjects dynamically |
| Business logic in Layer 5 (test) | Push logic to Layer 3 Task, test only asserts |
