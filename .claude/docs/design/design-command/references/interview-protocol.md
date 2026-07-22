# Interview Protocol

How the agent extracts requirements from the user during Step 3.

---

## Principle: Extract, Don't Interrogate

If the user provides a comprehensive description upfront, extract everything possible from it first. Only ask about gaps. Never re-ask what the user already stated.

## Question Categories

### 1. Workflow (Required)

**Goal:** Determine the steps, their order, and dependencies.

**Questions:**
- "What are the main phases of this command? (e.g., setup → process → verify)"
- "Walk me through what happens from input to output."
- "Are any steps dependent on others, or can some run in parallel?"

**Extract from description:** Verbs indicate steps (validate, generate, check, report).

### 2. Input/Output (Required)

**Goal:** Determine what goes in and what comes out.

**Questions:**
- "What does the user pass as arguments?"
- "What files or artifacts does this produce?"
- "Are there multiple input modes? (e.g., file path vs name vs natural language)"

### 3. Constraints (Required)

**Goal:** Determine hard rules and critical behaviors.

**Questions:**
- "What must this command NEVER do?"
- "Are there safety constraints? (e.g., never overwrite without confirmation)"
- "What are the failure modes? What happens when X goes wrong?"

### 4. HITL Points (Required)

**Goal:** Determine where human approval is needed.

**Questions:**
- "Where should the command pause for your approval?"
- "Are there any steps where wrong output would be costly to fix?"
- "Should the command be fully autonomous, or checkpoint at key moments?"

**Default:** If user doesn't specify, propose HITL at:
- Input validation (confirm what was parsed)
- First major output (confirm direction before generating the rest)

### 5. Domain Terms (Extract from conversation)

**Goal:** Build the vocabulary table.

**Method:** As the user describes the command, note domain-specific terms they use. Don't ask "what terms should I define?" — instead, present the terms you noticed and ask if the definitions are correct.

### 6. State & Resume (Optional)

**Goal:** Determine if the command needs to resume after interruption.

**Questions:**
- "Should this command be resumable if interrupted mid-run?"
- "What state needs to persist between steps?"

**Default:** If the command has 5+ steps, propose state persistence.

## When to Infer vs Ask

| Signal | Action |
|--------|--------|
| User gave detailed step-by-step description | Infer steps, confirm |
| User gave vague "it should do X" | Ask for specifics |
| User mentioned constraints explicitly | Extract as critical rules |
| User didn't mention HITL | Propose defaults, confirm |
| User referenced existing commands | Read those commands for pattern |

## Interview Output Format

After the interview, organize into:

```json
{
  "command_name": "...",
  "identity": "You are a ...",
  "philosophy": ["principle 1", "principle 2", "..."],
  "vocabulary": [{"term": "...", "meaning": "..."}],
  "critical_rules": ["rule 1", "rule 2"],
  "steps": [
    {"name": "...", "purpose": "...", "output": "...", "hitl": "none|checkpoint|full_stop"}
  ],
  "input": {"args": "...", "modes": ["..."]},
  "output": {"files": ["..."], "reports": ["..."]},
  "state": {"needed": true, "fields": ["..."]}
}
```

This structured format feeds directly into Step 4 (Draft Design Doc).
