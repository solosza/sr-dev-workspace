# Test: trace.py Imports and Wraps (L1/L2)

## Context
Backlog 199 (V-BASE): verify the utility exists AND runs — import it, decorate a function, call it.

## Type
TEST

## Execution
inline

## Dependencies
- 002

## Phase Gate
- [ ] trace.py exists on the feature branch (TRC-02)

## Requirements
- Run a python one-liner/script (absolute paths, PYTHONPATH to target `framework/`): import the trace module, apply `@trace("Task")` to a sample function, call it, assert the return value passes through unchanged
- Non-zero exit = failure → fix trace.py → /kernel/learn per protocol

## Acceptance Criteria
- [ ] Script exits 0 (import + wrap + call + passthrough verified)

## Gates Satisfied
- TRC-04

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
