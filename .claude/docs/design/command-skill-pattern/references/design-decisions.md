# Design Decisions (8 Baseline)

<!-- Payload of: command-skill-pattern/index.md -->

This architecture implements all 8 decisions from SMART-CONTRACTS-DESIGN.md:

| # | Decision | Summary |
|---|----------|---------|
| 1 | Contract Chaining | Downstream declares requires (dbt pattern) |
| 2 | One Artifact Per Step | Each step produces one primary artifact |
| 3 | Canonical Reference Versioning | Hash-based tracking |
| 4 | Dual Validation | Soft (agent) + hard (hook) on same contract |
| 5 | Contract Metadata | Dependencies + staleness + validation timestamps |
| 6 | Learning Integration | Record lessons via /kernel/learn when violations found |
| 7 | Override Handling | Project-scoped exceptions with expiry + audit trail |
| 8 | Soft/Hard Gate Integration | Unified workflow, single source of truth |

---

## Modular Loop Design

This architecture supports two invocation modes:

### Outer Loop (Standalone Command)

```
user -> /command [input]
  |
Skill orchestrates steps 1..N
  |
Results returned to user
```

### Inner Loop (Called by Another Skill)

```
User -> /healthcare-qa (outer skill)
  |-- Step 1..5 (healthcare-qa steps)
  |-- Call -> /create-test-artifacts (inner command/skill)
  |   |-- Steps 1..N (artifact creation)
  |   +-- Returns artifacts
  +-- Steps 6..18 (healthcare-qa continues)
```

Same skill code works in both contexts. Only invocation path differs.

---

## Workflow Phases

Commands typically organize steps into phases with gates:

### Phase 1: Setup
- Steps: 1, 2, ...
- Gate: Verify inputs valid, dependencies met

### Phase 2: Artifact Generation
- Steps: ..., ...
- Gate: All artifacts produced, pass validation

### Phase 3: Verification
- Steps: ..., ...
- Gate: All gates pass, ready for use

Phases are command-specific; this is a template.
