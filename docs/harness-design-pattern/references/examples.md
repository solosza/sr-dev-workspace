# Canonical Examples

## Orchestrator Loop: /reddit-pain/analyze

**Type:** Orchestrator loop (calls 3 skills sequentially)

**Entry point:** `.claude/commands/reddit-pain/analyze.md`

**Skills called:**
1. `reddit-data-pipeline` — Fetch Reddit posts and clean text
2. `ai-analysis-engine` — Identify pain points and generate ideas
3. `results-processor` — Format and export JSON + Markdown

**Deliverables:**
- `results.json` — Structured data (machine-readable)
- `results.md` — Human-readable report

**Use case:** Complex multi-phase analysis requiring sequential skill execution.

**From:** Harness backlog 127

---

## Primitive Loop: /spawn-subagent

**Type:** Primitive loop (self-contained, 4 steps)

**Entry point:** `.claude/commands/spawn-subagent.md`

**Skill:** `.claude/skills/spawn-subagent/SKILL.md`

**Steps:**
1. Parse task description
2. Validate background-safe
3. Invoke Agent tool with `run_in_background=true`
4. Return agent ID immediately (non-blocking)

**Key characteristic:** Non-blocking execution

**Pattern:** `env -u CLAUDECODE` (required for interactive sessions)

**Use case:** Spawn autonomous agents for background work without blocking user.

**Examples:**
- `spawn-subagent Test H3 adventure with 50 monsters`
- `spawn-subagent Build full test suite with 100 scenarios`
- `spawn-subagent Refactor backlog 127 to specification`

**From:** Kernel utility

---

## When to Reference Each

### Use /reddit-pain/analyze as model when:

- Building a multi-phase analysis harness
- Need to orchestrate 3+ skills sequentially
- Each phase is a distinct domain task
- Phases depend on each other's output

**Key files to study:**
- `.claude/commands/reddit-pain/analyze.md` — Command orchestration
- `.claude/skills/reddit-data-pipeline/SKILL.md` — First skill structure
- `.claude/skills/ai-analysis-engine/SKILL.md` — LLM-based skill structure
- `docs/HARNESS-DESIGN-PATTERN.md` — Full design pattern

### Use /spawn-subagent as model when:

- Building a utility loop (reusable component)
- Need non-blocking background execution
- Task is self-contained (doesn't call other skills)
- Want a standalone command that works independently

**Key files to study:**
- `.claude/commands/spawn-subagent.md` — Command entry point
- `.claude/skills/spawn-subagent/SKILL.md` — Primitive loop structure
- `.claude/skills/spawn-subagent/references/step-03-invoke-agent.md` — Background execution pattern
- `.claude/skills/spawn-subagent/references/error-handling.md` — Error recovery

---

## Comparison Table

| Aspect | reddit-pain | spawn-subagent |
|--------|------------|---|
| Type | Orchestrator | Primitive |
| Skills | 3 (sequential) | 1 (self-contained) |
| Complexity | High | Low |
| State output | .json + .md | agent_id |
| Duration | 3-5 minutes | 1-2 seconds |
| Blocking | No (async skills) | No (background agent) |
| Reusability | Called as unit | Can be called by other loops |
| Typical use | Domain analysis | Utility function |

---

*Both examples follow the same architecture and validation patterns. They differ only in scope and complexity.*
