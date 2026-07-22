# Layer 2: Pre-Generation Checkpoints (Directed Reading)

<!-- Payload of: tiered-index-architecture.md -->

When to read which files. Each step has an explicit reading list the agent must complete before writing anything.

---

## Why It Exists

Layer 1 organizes files into small, focused payloads. But organization alone doesn't tell the agent which files to read for a given task. Without directed reading, the agent either:

- **Reads everything** — wastes context window, increases noise
- **Guesses** — picks wrong files, misses critical references
- **Reads from memory** — hallucinates details that don't match the actual file

**The fix:** Each step declares exactly which payloads the agent must read before generating output.

---

## The Checkpoint

Before writing any artifact, the agent MUST:

1. **Read** the canonical reference for this step (use Read tool — not from memory)
2. **Read** the contract validation rules for this step
3. **Read** domain lessons (patterns learned from prior runs)
4. **Read** input content relevant to this step (corpus, prior step output)
5. **Generate** artifact matching reference pattern exactly

This is not optional. Skipping the checkpoint means the agent generates from memory, which drifts.

---

## Checkpoint Format in Workflow

Each step in a workflow document includes a checkpoint block:

```markdown
### Step N: [Step Name]

**Pre-generation checkpoint:**
- Read canonical reference: `references/step-N/[example-file]`
- Read contract: `contracts/step-N-[artifact]-contract.json`
- Read [input from prior step]
- If [optional corpus] available: read it for enrichment

**How agent uses the reference:**
1. Agent reads reference — sees the exact format
2. Agent reads input — knows what content to generate
3. Agent generates artifact matching reference format with input content
```

The checkpoint is the bridge between Layer 1 (where files live) and the agent's working context (what it actually reads).

---

## What Each Checkpoint Item Provides

| Item | What It Gives the Agent | Without It |
|------|------------------------|------------|
| Canonical reference | The correct output pattern to match | Agent invents its own format → inconsistent |
| Contract | Validation rules to self-check before writing | Agent doesn't know what "correct" looks like |
| Domain lessons | Mistakes to avoid (from prior runs) | Agent repeats the same errors |
| Input content | Data to populate the pattern with | Agent generates placeholder/generic content |

---

## Example: Multi-Step Pipeline

```
Step 1: Extract metadata
  Checkpoint: Read corpus files → extract structure
  Output: metadata.json

Step 2: Generate test cases
  Checkpoint: Read references/step-02/example.md
              Read contracts/step-02-contract.json
              Read metadata.json from Step 1
  Output: test-cases.md

Step 5: Generate queries
  Checkpoint: Read references/step-05/example.sql
              Read contracts/step-05-contract.json
              Read test-cases.md from Step 2
              Read SP code (if available)
  Output: tc-queries.sql
```

Each step reads only the payloads it needs. The index structure (Layer 1) makes them findable. The checkpoint (Layer 2) makes the reading explicit.

---

## Key Principle

**The checkpoint is a reading list, not a suggestion.** If the agent doesn't read the canonical reference, it cannot generate correct output. The contract (Layer 3) will catch the violation, but the goal is to prevent it by directing the agent to the right files upfront.
