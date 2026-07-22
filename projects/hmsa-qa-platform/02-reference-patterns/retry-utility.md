# Retry Utility — Design Doc

## Governing Contract

`framework/docs/5-layer-contract.md` — error rule 3: Layer 3 retry may catch *transient* exceptions via the shared utility — it retries or re-raises, never swallows. Utilities table: `retry.py` in `framework/resources/utilities/`, used by L3 only.

## Decision

Extract the implementation already drafted in [[hybrid-tasks]] (retry_operation with exponential backoff) into its canonical home, and codify the boundary the dry run sharpened: **transient-failure retry and subject-selection retry are different mechanisms** — only the first belongs here.

## Canonical Implementation

```python
"""retry.py - Layer 3 utility. Transient-failure retry with backoff."""

import time
from typing import Callable, TypeVar

T = TypeVar("T")


def retry_operation(operation: Callable[[], T], max_attempts: int = 3,
                    delay_seconds: float = 1.0, backoff_factor: float = 2.0,
                    exceptions: tuple = (Exception,)) -> T:
    """Retry a zero-arg operation on declared transient exceptions.
    Re-raises the last error after max_attempts — never swallows."""
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

Usage (from hybrid-tasks): `retry_operation(lambda: self.processing_api.trigger(id), exceptions=(ConnectionError, TimeoutError))` — **declared exception types only**; `(Exception,)` default exists for the signature, callers must narrow it.

## The Two Retries (the rule this doc exists for)

| | Transient retry (`retry_operation`) | Subject retry (Task loop) |
|---|---|---|
| Failure means | Infrastructure blinked (timeout, connection) | The *data* was unsuitable (candidate claim invalid) |
| Retry does | The SAME operation again | A DIFFERENT subject |
| Lives in | `retry.py`, wrapped around one L2 call | The Task's own loop (see `find_eligible_order` in [[hybrid-tasks]]) |
| Wrong usage | Retrying a failed assertion or a domain rejection | Wrapping subject selection in retry_operation (same subject re-fails forever) |

## Dry Run — Autopend Discovery Under Both Failure Modes

**Subject:** finding an eligible history claim (real TC discovery: query candidates, validate status still PAID).

**Instantiation:** (1) DB timeout mid-query → `retry_operation` around the Data Object call retries the same query, succeeds on attempt 2 — correct. (2) Candidate claim got grabbed by another process (status changed) → that is NOT an exception to retry; the Task's subject loop picks the next candidate. Wrapping case 2 in `retry_operation` would re-validate the same dead candidate three times and raise — the anti-usage the table forbids.

**Verdict: HOLDS.** The two-retries boundary is the doc's real content; the implementation is 20 proven lines. Nothing surfaced.

## Contract Compliance

| Rule | Status |
|------|--------|
| L3 only; transient exceptions only, declared | PASS |
| Re-raises after exhaustion — never swallows | PASS |
| Identical implementation shipped in every platform (utilities rule) | PASS |

## What Does NOT Go Here

- No subject-selection loops (Task logic)
- No pytest-level rerun policy (`pytest-rerunfailures`, Phase 3.6 — a different layer of the flakiness answer)
- No retry at Layers 1, 2, 4, or 5
