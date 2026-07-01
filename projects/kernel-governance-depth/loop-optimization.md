# Loop Optimization Analysis

**Backlog:** 151 — Governance Depth Over Breadth
**Task:** 001-research-loop-optimization
**Constraint:** No new features, commands, or hooks. Improvements deepen existing mechanisms only.

---

## The Current Loop

```
session-start → anchor → WORK → complete
                  ↑         ↓
                  └── every N actions (hook-enforced)
                           ↓
                  failure? → fix → learn
```

Five components analyzed below: session-start, anchor, work phase, learn, complete.

---

## 1. Session-Start

### Current Behavior
- Reads `session_state.json` for context recovery
- Checks `needs_restart` for domain-setup resume
- Checks for existing domain (persistence rule)
- Forces `anchored: false` on fresh start (unless one_shot)
- Reports state summary

### Strengths
- Structured context object (`current_task`, `progress`, `next_step`) enables deterministic resume after context compaction
- One-shot guard prevents sub-agents from resetting parent anchor state
- Domain persistence rule prevents accidental domain recreation

### Weaknesses
- No validation of context staleness — if `session_state.json` has a context from 3 days ago, agent internalizes it without questioning whether it's still relevant
- No integrity check on the state file itself — if another agent corrupted it (shared mutable state issue), session-start proceeds with bad data

### Recommendation: TIGHTEN

**Context age check:** Add a soft warning (not a block) when context timestamp is >24h old. The agent should still internalize the context but flag it: "Context is N days old — verify before acting." This is a protocol-level rule, not a new hook — the session-start command text can include it.

**State integrity assertion:** Session-start should verify that `domain` in session_state matches any existing `[domain]_workflow.json`. If they disagree, report the mismatch before proceeding. Again, a protocol-level check — no new code needed.

---

## 2. Anchor

### Current Behavior
- **Part A:** Re-read protocol + lessons, compute protocol hash, apply rules to next action with concrete verbs, restore context from session_state
- **Part B:** Review all inter-anchor work from actions.jsonl against protocol, flag violations
- **Part C:** Archive actions log, update state, confirm anchor token

### Strengths
- Full re-read requirement (not "already read this session") prevents protocol drift — the most battle-tested rule in the kernel
- Action review against protocol catches violations that the agent would otherwise rationalize away
- Anchor token mechanism prevents quick-anchoring (just flipping `anchored: true`)
- "Apply rules to next action" with concrete verbs forces the agent to commit to specific behavior, not generic acknowledgments

### Weaknesses
- Part B review is qualitative ("does this match protocol?") — the agent rates its own work. When the agent caused the violation, it's also the reviewer. Self-review has a known blindspot (see lessons: cycling-run-2, anchor missed violation)
- The "apply rules to next action" step produces varying quality — sometimes genuinely specific ("I will test one allow rule in isolation"), sometimes procedurally correct but shallow ("I will use absolute paths")
- No structured output format for Part B — the review is free-text, making it harder to detect when the agent is hand-waving

### Recommendation: TIGHTEN

**Structured Part B output:** Require a table format for every action reviewed:

```
| # | Action | Protocol Rule | Compliant | Evidence |
|---|--------|--------------|-----------|----------|
| 1 | Edit: hook.py | Naming conventions | Yes | snake_case used |
| 2 | Bash: pytest ... | Test before commit | Yes | exit 0 |
```

This is a command format change (anchor.md), not a new feature. The structured format makes hand-waving visible — an empty "Evidence" column is a violation.

**Rule application depth score:** After stating concrete verbs, the agent self-rates: "3 rules applied, 2 skipped with reason." If 0 rules applied, that's a signal the agent isn't engaging with lessons. This is a soft metric within the existing anchor output, not a gate.

---

## 3. Anchor Interval (Work Phase)

### Current Behavior
- Default: every 10 actions (configurable via `actions_limit`)
- Hook auto-increments counter for Write, Edit, Bash
- .claude/ writes don't increment (infrastructure)
- Safe bash commands (ls, git status, etc.) increment but don't trigger blocks
- One-shot agents skip counter entirely

### Strengths
- Automatic counting removes agent responsibility for tracking
- Configurable limit allows tuning per domain
- Infrastructure writes excluded — prevents anchor spam during state updates
- One-shot bypass is correct — single-task agents don't need mid-task anchoring

### Weaknesses
- Fixed interval doesn't account for task complexity or error rate. A 10-action anchor during a simple file write is overhead; a 10-action anchor during complex multi-file refactoring might be too late
- The current limit of 30 (`actions_limit: 30` in sr_dev_workflow.json) is very generous — the original design was 10. At 30 actions between anchors, significant drift can accumulate
- No distinction between "10 successful actions" and "10 actions including 5 failures" — error-dense work should re-center more frequently

### Recommendation: ADAPT

**Error-weighted interval:** When `needs_learn` has been triggered since the last anchor (i.e., a test failure occurred), reduce the effective limit by half for the next interval. This doesn't require a new hook — the existing `check_and_increment_counter` function can read `needs_learn` from session_state and use `actions_limit / 2` when it's been recently set. One conditional in existing code.

**Review the 30-action limit:** The current `actions_limit: 30` should be evaluated. The original design specified 10. If 30 was set for operational convenience (fewer interruptions), the tradeoff is more drift between anchors. Recommend resetting to 15 as a middle ground — still fewer interruptions than 10, but catches drift earlier than 30. This is a state value change, not code.

---

## 4. Learn

### Current Behavior
- Records lesson in `lessons.md` with structured format (Issue, Root Cause, Fix, Anti-Pattern, Quality Gate)
- Updates reference files if pattern is worth codifying
- Updates hooks if failure is mechanically enforceable
- Recurrence detection pipeline (fingerprint, threshold, escalation)
- Clears `needs_learn` block in state
- Two triggers: test failure (hook-set) and anchor violation (self-set)

### Strengths
- Mandatory invocation after failure — hook blocks all writes until learn is completed
- Two-tier enforcement: hook sets `needs_learn` on test failure, protocol requires self-enforcement even if hook doesn't fire
- Lesson-to-hook pipeline: if a failure can be mechanically prevented, the learn step adds it to the hook — failures compound into enforcement
- Recurrence tracking with escalation prevents the same lesson from being recorded without noticing the pattern

### Weaknesses
- Lesson quality varies — some lessons are precise ("never use cd in bash"), others are vague ("be more careful with paths"). The command doesn't enforce specificity
- The recurrence detection pipeline (Step 5) references imports (`lessons.schema`, `lessons.recurrence`, `lessons.alerts`) that may not exist in all deployments — this is aspirational code in the command definition
- No lesson pruning or consolidation — `lessons.md` grows monotonically. RULE ZERO is already 40+ lines. Eventually the anchor re-read becomes noise because the agent skims rather than internalizes

### Recommendation: TIGHTEN + LEAVE AS-IS

**Lesson specificity gate (TIGHTEN):** The learn command should require that every lesson includes at least one concrete verb in the Anti-Pattern or Quality Gate field. "Be careful" is not a lesson. "Never use cd in bash commands" is. This is a command-text change — add a self-check step: "Does your anti-pattern include a concrete verb (never/always/must)? If not, rewrite it."

**Lesson pruning (LEAVE AS-IS for now):** The growth concern is real but premature. The current 32 lessons are manageable. Pruning introduces risk (removing a lesson that's still relevant). When lessons.md exceeds ~100 entries, revisit with a consolidation strategy. Don't solve this now.

**Recurrence pipeline (LEAVE AS-IS):** The aspirational imports are fine as a design target. They don't cause failures — the command works without them. When the infrastructure exists, they'll activate.

---

## 5. Complete

### Current Behavior
- Checks protocol_created and anchored gates
- Verifies deliverables (read files, confirm content matches requirements)
- Verifies gate contract if task folder has one
- Three modes: one-shot (exit), cycling (next task), single (done)
- Saves final context for resume

### Strengths
- Gate contract verification is mechanical — the agent can't self-report completion without its gates passing
- Deliverable verification table forces the agent to actually read what it produced, not just report "tool call succeeded"
- Three-mode design handles all execution contexts cleanly
- One-shot state preservation (don't reset anchored, don't reset counter) prevents sub-agent interference

### Weaknesses
- Deliverable verification is self-assessed — the agent reads its own output and decides if it's good. For research tasks especially, the agent can write shallow analysis and mark it complete
- No cross-reference with task requirements — the complete command verifies "deliverables exist" but doesn't mechanically verify "deliverables address all requirements listed in the task file"
- Gate contract only checks existence/grep/run — no semantic quality gate (e.g., "file has analysis of all 5 components")

### Recommendation: TIGHTEN

**Requirements cross-reference (TIGHTEN):** The complete command should include a step: "Re-read the task file. List each requirement. For each, state which part of your deliverable addresses it." This makes gaps visible — if a requirement has no corresponding deliverable section, the agent must either fill it or explain why it's not applicable. This is a command-text addition to Step 2, not a new mechanism.

**Semantic gate in gate-contract (LEAVE AS-IS):** Adding semantic quality checks to gate-contract.md (e.g., "file contains analysis of 5 components") would require a new verification method. This crosses the feature freeze boundary. The requirements cross-reference above achieves a similar effect without new code.

---

## Summary

| Component | Current State | Recommendation | Change Type |
|-----------|--------------|----------------|-------------|
| Session-Start | Functional, no staleness check | TIGHTEN — add context age warning + state integrity assertion | Command text |
| Anchor | Strong, Part B is qualitative | TIGHTEN — structured Part B table, rule application depth score | Command text |
| Anchor Interval | Fixed at 30, no error weighting | ADAPT — error-weighted interval, reduce limit to 15 | One conditional + state value |
| Learn | Strong enforcement, quality varies | TIGHTEN — lesson specificity gate (concrete verb required) | Command text |
| Complete | Gate contract works, self-assessed | TIGHTEN — requirements cross-reference step | Command text |

**Key finding:** Most improvements are command-text changes (deepening existing instructions), not new code. The loop shape is sound — the depth is in how rigorously each step is executed, not in adding new steps.
