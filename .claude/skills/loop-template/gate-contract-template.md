---
name: [LOOP-NAME]-gates
type: gate-contract
parent: [LOOP-NAME]
---

# [LOOP-NAME] Loop — Gate Contract

## Verification Methods

| Method | How to check |
|--------|-------------|
| `file_exists` | `test -f {{path}}` — does the file exist? |
| `grep` | Search file content for a specific pattern |
| `json_validate` | Validate JSON against schema (python -m json.tool) |
| `manual` | Review content and judge against criteria (LLM-evaluated) |

---

## Pre-conditions

What must be true BEFORE the [LOOP-NAME] loop runs:

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| PRE-01 | SKILL.md exists | `file_exists` | [DOMAIN-SPECIFIC] SKILL.md exists at expected path | Create SKILL.md |
| PRE-02 | Input contract exists | `file_exists` | [DOMAIN-SPECIFIC] input contract file exists | Create input contract |
| PRE-03 | Input contract valid | `json_validate` | Input contract parses without errors | Fix JSON syntax |
| PRE-04 | Required input fields present | `grep` | [DOMAIN-SPECIFIC] all required input fields defined | Add missing fields |
| PRE-05 | Dependencies available | `manual` | [DOMAIN-SPECIFIC] upstream loops/services accessible | Verify dependency chain |

---

## Post-conditions

What must be true AFTER the [LOOP-NAME] loop completes:

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| POST-01 | Output contract satisfied | `json_validate` | Output matches output contract schema | Fix output generation |
| POST-02 | Required output fields present | `grep` | [DOMAIN-SPECIFIC] all required output fields populated | Add missing output fields |
| POST-03 | State updated | `manual` | [DOMAIN-SPECIFIC] downstream state reflects loop outcome | Fix state mutation |
| POST-04 | No partial mutations | `manual` | Either all state changes applied or none (atomic) | Implement rollback |

---

## Contract Validation

Input/output contract adherence:

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| CV-01 | Input matches schema | `json_validate` | Every invocation input passes input contract validation | Reject malformed input |
| CV-02 | Output matches schema | `json_validate` | Every invocation output passes output contract validation | Fix output generation |
| CV-03 | Enum values valid | `grep` | [DOMAIN-SPECIFIC] all enum fields use declared values only | Restrict to declared enums |
| CV-04 | Required vs optional | `manual` | Required fields never null/missing, optional fields have defaults | Add defaults or enforce required |

---

## State Integrity

No corruption during or after loop execution:

| ID | Check | Method | Pass Criteria | Fail Action |
|----|-------|--------|---------------|-------------|
| SI-01 | No orphaned state | `manual` | [DOMAIN-SPECIFIC] no dangling references after loop completes | Clean up orphaned state |
| SI-02 | Idempotent re-entry | `manual` | Running the loop twice with same input produces same output | Fix non-deterministic behavior |
| SI-03 | Error state clean | `manual` | Failed loop leaves state in pre-invocation condition | Implement cleanup on failure |
| SI-04 | Downstream notified | `manual` | [DOMAIN-SPECIFIC] downstream loops receive expected signals | Fix integration handoff |

---

## Gate Execution Sequence

1. **Pre-condition Gates** (PRE-01 through PRE-05): Verify loop is ready to run
2. **Contract Validation Gates** (CV-01 through CV-04): Verify input/output adherence
3. **Post-condition Gates** (POST-01 through POST-04): Verify loop completed correctly
4. **State Integrity Gates** (SI-01 through SI-04): Verify no corruption

---

## Gate State Machine

```
PRE-01..PRE-05 (verify ready)
  |
CV-01..CV-04 (verify contracts)
  |
POST-01..POST-04 (verify completion)
  |
SI-01..SI-04 (verify integrity)
  |
ALL_GATES_PASS
```
