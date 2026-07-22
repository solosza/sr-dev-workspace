# Layer 3: Contracts & Dual Gates (Enforcement)

<!-- Payload of: tiered-index-architecture.md -->

Proof the agent read correctly and generated correctly. Two validation gates — one agent-driven, one hook-driven — both reading the same contract.

---

## Why It Exists

Layers 1 and 2 organize files and direct the agent to read them. But without enforcement, the agent can:

- Skip the reading list and generate from memory
- Read the reference but not follow it
- Follow it once, then drift in subsequent steps

**The fix:** Contracts define what "correct" looks like. Gates validate every artifact before it's written. Violations are blocked and recorded.

---

## Dual Gate Validation

### Soft Gate (Agent-Driven)

The agent validates its own output before writing:

1. Read contract `soft_validation_rules` for this step
2. Read the canonical reference (same one from Layer 2 checkpoint)
3. Compare generated artifact to contract rules + reference pattern
4. If violation → log error, invoke `/kernel/learn`, STOP

**What it catches:** Semantic issues — wrong content structure, missing coverage, incorrect logic, patterns that don't match the reference.

### Hard Gate (Hook-Driven)

A hook validates the artifact mechanically at write time:

1. Hook intercepts the Write operation
2. Loads corresponding contract for the artifact type
3. Applies `mechanical_validations` (regex, file checks, counts)
4. If violation → block write, agent must fix and retry

**What it catches:** Structural issues — missing headers, wrong patterns, missing keywords, format violations.

### Why Both

| Gate | Catches | Example |
|------|---------|---------|
| Soft | Content is wrong but formatted correctly | Test case has correct headers but tests the wrong thing |
| Hard | Format is wrong regardless of content | Missing `### TC-` headers, no `UNION ALL` keyword |

Neither gate alone is sufficient. Together they cover both content quality and structural compliance.

---

## Contract Structure

Each step has a contract JSON file. Both gates read the same contract — single source of truth.

```json
{
  "contract_version": "1.0",
  "artifact": "test-cases.md",
  "step": 2,
  "dependencies": ["step-01"],

  "soft_validation_rules": [
    {
      "rule_id": "TC-001",
      "name": "TC count >= AC count",
      "description": "At least one TC per AC (test pyramid)",
      "check": "count(### TC-) >= total_ac_count",
      "reference": "references/step-02/example.md",
      "on_violation": "log error, invoke /kernel/learn, STOP"
    }
  ],

  "mechanical_validations": [
    {
      "rule_id": "MV-001",
      "name": "TC headers present",
      "method": "grep",
      "pattern": "^### TC-\\d{3}:",
      "min_count": 1,
      "on_violation": "block write"
    }
  ],

  "canonical_reference": "references/step-02/example.md",
  "success_criteria": ["TC count >= AC count", "Headers follow pattern"]
}
```

**Key fields:**
- `soft_validation_rules` — agent reads these, compares artifact to reference
- `mechanical_validations` — hook applies these mechanically (grep, file_exists)
- `canonical_reference` — the golden file both gates compare against
- `on_violation` — what happens when a rule fails

---

## Violation Flow

### Soft Gate Violation

```
Agent generates artifact
    → Agent reads contract rules
    → Rule check fails
    → Agent logs: needs_learn: true
    → Agent invokes /kernel/learn
    → Agent records lesson (what went wrong, reference to correct pattern)
    → Lesson clears the block
    → Agent retries generation
```

### Hard Gate Violation

```
Agent attempts to write artifact
    → Hook intercepts write
    → Hook applies mechanical validations
    → Validation fails
    → Write BLOCKED
    → Agent reads error message + canonical reference
    → Agent fixes artifact
    → Agent retries write
    → Hook re-validates → passes → write succeeds
```

---

## Learning Integration

When violations are caught, the lesson is recorded so the same mistake doesn't repeat:

```markdown
Step 2: Test Cases Violation

Rule violated: TC-001 (TC count >= AC count)
Expected: TC count >= 20
Found: TC count = 15

Reference: references/step-02/example.md
Action: Apply test pyramid — each AC needs at least 1 TC

Lesson: Before writing test-cases.md, verify every AC has at least one TC.
```

Lessons feed back into Layer 2 checkpoints — the agent reads lessons as part of the pre-generation checkpoint, preventing repeat violations.

---

## Key Principle

**Contracts are declarative, not procedural.** All validation logic is data-driven (JSON). The agent reads rules and applies them. The hook reads rules and enforces them. No hardcoded validation in code — everything flows from the contract.
