# Contract Definitions — /walkthrough

Parent: [[../index.md]]

Gate contracts for the generated skill. Soft rules are judgment checks the agent self-verifies; mechanical validations are hook/script-checkable.

## Step 3 Contract (Decompose) — `contracts/step-03-contract.json`

```json
{
  "step": "03-decompose",
  "soft_validation_rules": [
    "Section map is dependency-ordered (no section requires a later one)",
    "Each section is one-sitting sized (split too-big, merge trivial)",
    "Section names use domain vocabulary, meaningful standalone in the ledger",
    "User explicitly approved the map before the loop started"
  ],
  "mechanical_validations": [
    {"check": "file_exists", "target": ".claude/state/walkthrough-state.json"},
    {"check": "json_field_nonempty", "target": "sections"},
    {"check": "json_field_equals", "target": "cursor", "value": 0},
    {"check": "json_field_nonempty", "target": "sources_read"}
  ]
}
```

## Step 4/5/6 Contract (Loop Iteration)

```json
{
  "step": "04-06-iteration",
  "soft_validation_rules": [
    "Exactly one section rendered this turn (format-contract hard rule 1)",
    "All required format parts present for current depth (7 plain / 3 terse)",
    "Grounding part cites files actually present in sources_read",
    "Explanation ended with a settle prompt",
    "Ledger entry 'settled' field is self-contained full sentences"
  ],
  "mechanical_validations": [
    {"check": "json_field_length_equals", "target": "ledger", "value": "cursor",
     "note": "ledger length == cursor after each Record — append-before-advance invariant"}
  ]
}
```

## Step 7 Contract (Exit)

```json
{
  "step": "07-exit",
  "soft_validation_rules": [
    "No section left DEFERRED without a revisit offer",
    "Handoff options presented (feed /design, fold into doc, stop)"
  ],
  "mechanical_validations": [
    {"check": "file_exists", "target": "docs/walkthroughs/*[artifact-slug].md"},
    {"check": "json_field_equals", "target": "status", "value": "complete"},
    {"check": "json_field_nonempty", "target": "ledger_file"}
  ]
}
```

## Global Invariants

| Invariant | Enforcement |
|-----------|-------------|
| Never invoked from run-task.sh / autonomous cycling | Soft (SKILL.md critical rule); optionally hook-blockable via `one_shot` state detection |
| One-shot writes no state | Soft — step-01 branches around state init |
| State overwrite of an active walkthrough requires explicit user confirmation | Soft (step-01 resume check) |
