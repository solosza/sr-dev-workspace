# [DOMAIN-SPECIFIC] Loop — Skill Definition

## Identity

| Key | Value |
|-----|-------|
| Skill | [DOMAIN-SPECIFIC] |
| Type | [DOMAIN-SPECIFIC: root-loop | sub-loop | leaf-loop] |
| Parent | [DOMAIN-SPECIFIC: invoked by X, Y, Z — or "none" if root] |
| Purpose | [DOMAIN-SPECIFIC: one-line description of what this loop resolves] |

## Vocabulary

| Term | Definition |
|------|-----------|
| [DOMAIN-SPECIFIC] | [DOMAIN-SPECIFIC: define domain terms used in this loop] |

## Contracts

| Contract | File |
|----------|------|
| Input | -> [[contracts/input-contract.json]] |
| Output | -> [[contracts/output-contract.json]] |
| Rules | -> [[contracts/rules-contract.md]] |
| Integration | -> [[contracts/integration-contract.md]] |
| Gate | -> [[contracts/gate-contract.md]] |

## Resolution Flow (DDD Phases)

### DECLARE Phase
1. Receive request from invoking loop (or user if root)
2. Load context: [DOMAIN-SPECIFIC: what state/data to retrieve]
3. Validate input against -> [[contracts/input-contract.json]]
4. Present current state to agent

**Contract fields consumed:** [DOMAIN-SPECIFIC: list input fields used]

### DETERMINE Phase
1. Apply rules from -> [[contracts/rules-contract.md]]
2. Route to sub-loops if needed: [DOMAIN-SPECIFIC: which inner loops to invoke]
3. Compute outcome: [DOMAIN-SPECIFIC: what calculation or decision occurs]
4. Classify result via code paths (see below)

**Atomic transaction pattern:** No state mutation occurs during DETERMINE. The phase computes the outcome as a pure calculation. State changes happen only after the invoking loop receives the complete output and validates. This ensures rollback safety.

**Contract fields consumed:** [DOMAIN-SPECIFIC: list input/rules fields used]
**Contract fields produced:** [DOMAIN-SPECIFIC: list output fields generated]

### DESCRIBE Phase
1. **Assemble outcome object** from DETERMINE results
2. **Generate narration** using templates -> [[references/narration-templates.md]]
3. **Validate state** via state-check [DOMAIN-SPECIFIC: validation method]
4. **Return full output** to invoking loop — invoking loop handles state updates

**Contract fields produced:** [DOMAIN-SPECIFIC: list all output fields]

## Code Paths

| Path | Condition | Effect |
|------|-----------|--------|
| [DOMAIN-SPECIFIC] | [DOMAIN-SPECIFIC: condition] | [DOMAIN-SPECIFIC: what happens] |

## Special Rules

[DOMAIN-SPECIFIC: edge cases, exceptions, domain-specific constraints]

## Composition

### As Inner Loop (receives/returns)
- **Receives:** Input contract from parent loop
- **Returns:** Output contract to parent loop
- **Contract:** Parent builds input per -> [[contracts/input-contract.json]], receives output per -> [[contracts/output-contract.json]]
- **State mutation:** This loop does NOT mutate state — parent handles all mutations after receiving output

### As Outer Loop (invokes inner loops)
- **Invokes:** [DOMAIN-SPECIFIC: list inner loops this loop calls, or "none" if leaf]
- **Contract:** Builds input per inner loop's input contract, receives output per inner loop's output contract
- **Orchestration:** [DOMAIN-SPECIFIC: sequential or parallel invocation pattern]

## Integration Points

**Invoked by:**
- [DOMAIN-SPECIFIC: list parent loops that call this loop]

**Invokes:**
- [DOMAIN-SPECIFIC: list child loops this loop calls, or "none (leaf loop)"]

## Agent Execution

When resolving [DOMAIN-SPECIFIC]:

1. **Receive request** — extract fields from input contract
2. **Load context** — [DOMAIN-SPECIFIC: what to look up]
3. **Validate input** — check against -> [[contracts/input-contract.json]]
4. **Apply rules** — evaluate per -> [[contracts/rules-contract.md]]
5. **Route to sub-loops** — [DOMAIN-SPECIFIC: invoke inner loops if needed]
6. **Compute outcome** — [DOMAIN-SPECIFIC: core logic]
7. **Classify result** — determine code path
8. **Assemble output** — build per -> [[contracts/output-contract.json]]
9. **Generate narration** — fill template from -> [[references/narration-templates.md]]
10. **Validate state** — confirm integrity before returning
11. **Return outcome** to invoking loop

## Testing Checklist

- [ ] [DOMAIN-SPECIFIC: each code path tested]
- [ ] Input contract validation (reject malformed input)
- [ ] Output contract completeness (all fields present)
- [ ] Sub-loop integration (if applicable)
- [ ] Narration generated correctly
- [ ] State unchanged after DETERMINE (atomic transaction)
