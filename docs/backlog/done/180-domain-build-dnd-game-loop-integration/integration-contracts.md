# Integration Contracts — Outer/Inner Loop Composition

## Problem

The dnd-game-engine-test orchestration-loop defines routing (DETERMINE phase decision tree) and output validation (DESCRIBE phase 10-step contract). But individual sub-loops don't formally declare their integration interface. The outer loop knows what it expects, but inner loops don't declare what they provide.

This creates a gap: when building or modifying an inner loop, there's no contract to validate against. The developer (agent) must read the orchestration-loop SKILL.md to understand what format to return. This is fragile and doesn't scale.

## Solution: Bidirectional Integration Contracts

Each inner loop declares its integration interface as part of its own contract set:

```json
{
  "integration": {
    "invoked_by": ["orchestration-loop"],
    "receives": {
      "user_action": "object — action type + target + context",
      "campaign_state": "object — full campaign state",
      "resolved_creatures": "array — stat blocks (not IDs)"
    },
    "returns": {
      "result_code": "string — victory|defeat|success|failure|escape|etc",
      "updates": "object — field changes per sub-loop-update-contract",
      "narration": "string — player-facing result text",
      "downstream_calls": "array — optional sub-loops to invoke"
    },
    "downstream_invocations": [
      {
        "loop": "ability-saves",
        "when": "concentration broken or DC save required",
        "mandatory": true
      }
    ]
  }
}
```

The outer loop's routing contract references these inner declarations. Validation is bidirectional:
- Outer loop validates: "did the inner loop return what I expect?"
- Inner loop validates: "did I receive what I need?"

## Application to Game Repo

The orchestration-loop already has `sub-loop-update-contract.json` (field ownership matrix) and `describe-phase-contract.json` (10-step validation). What's missing:

1. **Per-loop input contracts** — What each sub-loop expects to receive
2. **Per-loop output contracts** — What each sub-loop guarantees to return
3. **Downstream invocation contracts** — When a sub-loop MUST invoke another sub-loop
4. **Cross-loop validation** — Outer loop checks inner loop output against its own integration spec

## Generalized Template

Any repo with outer/inner loops uses the same pattern:

```
outer-loop/
  contracts/
    routing-contract.json        # Decision tree: which inner loop for which input
    integration-spec.json        # What all inner loops must return

inner-loop/
  contracts/
    [loop]-input.json            # What this loop receives
    [loop]-output.json           # What this loop returns
    [loop]-integration.json      # How this loop connects to outer loop
    [loop]-downstream.json       # What downstream loops this loop invokes
```
