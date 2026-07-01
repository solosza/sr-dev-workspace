# Governance Depth Recommendation Report

**Backlog:** 151 — Governance Depth Over Breadth
**Task:** 005-build-recommendation-report
**Constraint:** All recommendations respect feature freeze. No new commands, hooks, or features.

---

## Source Research

| # | Research File | Key Findings |
|---|--------------|--------------|
| 001 | `loop-optimization.md` | Loop shape is sound; depth needed in anchor Part B (structured table), learn (specificity gate), complete (requirements cross-reference) |
| 002 | `enforcement-depth.md` | 10 failure modes in 4-hook system; 3 drift scenarios; policy embedded in hook code |
| 003 | `domain-setup-and-lessons.md` | Bootstrap quality improvable via structured extraction; lessons compound via tiered promotion; auto-enforcement premature |
| 004 | `external-governance-models.md` | Unix validates primitive minimality; seL4 validates TCB constraint; OTP identifies escalation gap; K8s identifies policy-data separation gap; Ostrom identifies graduated sanctions gap |

---

## Recommendations — High Priority

### H1. Narrow Auto-Approve Scope

**What:** Exclude `.claude/hooks/*.py` and `.claude/settings*.json` from auto-approval in `auto-approve-claude-writes.py`.

**Where:** `.claude/hooks/auto-approve-claude-writes.py` — add exclusion check before returning `approve`.

**Change:** ~4 lines. Check if file path matches hook or settings pattern; if so, return `abstain` (let normal permission flow ask user).

**Expected improvement:** Closes the self-modification bypass vector (enforcement-depth.md failure mode 10, external-governance-models.md K8s no-self-modification pattern). An agent can no longer silently modify its own enforcement hooks.

**Rationale:** Both the enforcement depth analysis and the K8s admission controller model independently identified this as a real bypass risk. The fix is minimal and has no false-positive risk — legitimate hook modifications should go through user approval anyway.

---

### H2. Structured Anchor Part B Output

**What:** Require a table format for action review during anchor Part B, replacing free-text assessment.

**Where:** `.claude/commands/kernel/anchor.md` — Step 7 (review each action against protocol).

**Change:** Command text update. Replace the current checklist with a required table:

```
| # | Action | Protocol Rule | Compliant | Evidence |
|---|--------|--------------|-----------|----------|
```

**Expected improvement:** Makes hand-waving visible during self-review. An empty "Evidence" column is a detectable violation. Addresses the self-assessment weakness identified in loop-optimization.md and the Ostrom monitoring principle from external-governance-models.md.

**Rationale:** The anchor Part B is the kernel's primary monitoring mechanism. Currently free-text, it allows the agent to claim compliance without evidence. A structured table doesn't guarantee honesty, but it makes gaps visible to the user reviewing anchor output.

---

### H3. Block Unsafe Redirection in Safe Bash

**What:** Check for redirection operators (`>`, `>>`, `|` followed by a command) in bash commands currently classified as "safe."

**Where:** `.claude/hooks/universal-gate-enforcer.py` — `is_safe_bash()` function.

**Change:** ~5 lines. After matching a safe prefix, check if the command contains `>`, `>>`. If so, treat as unsafe (increment counter, apply gates).

**Expected improvement:** Prevents `echo "data" > file.txt` from bypassing all gates. Enforcement-depth.md failure mode 2 identified this as medium likelihood.

**Rationale:** The safe bash exemption exists to avoid gating read-only commands (ls, git status). But the prefix check doesn't inspect the full command. A command like `cat file > /dev/null` is safe; `echo payload > target.txt` is not. The simplest fix: any safe-prefix command with `>` or `>>` is treated as unsafe.

---

## Recommendations — Medium Priority

### M1. Requirements Cross-Reference in Complete

**What:** Add a step to `/kernel/complete` that re-reads the task file and maps each requirement to a specific deliverable section.

**Where:** `.claude/commands/kernel/complete.md` — after deliverable verification (Step 2).

**Change:** Command text addition. New substep:

```
Re-read the task file. For each requirement:
| Requirement | Deliverable Section | Addressed? |
|-------------|-------------------|------------|
```

**Expected improvement:** Forces the agent to demonstrate coverage, not just existence. Addresses the semantic quality gap identified in loop-optimization.md (complete is self-assessed) and the principal-agent information asymmetry from external-governance-models.md.

**Rationale:** Gate contracts check existence and grep patterns. This cross-reference adds a protocol-level quality check without modifying gate contracts. The user can quickly verify coverage by scanning the table.

---

### M2. Log Bash Description Field

**What:** Include the `description` field from Bash tool input in actions.jsonl log entries.

**Where:** `.claude/hooks/actions-log-appender.py` — the Bash entry formatting line.

**Change:** ~1 line. Change `entry = f"Bash: {command[:80]}"` to include `tool_input.get('description', '')`.

**Expected improvement:** Makes anchor Part B review meaningful for complex bash commands. Currently, multi-line Python commands are truncated to 80 chars, losing their intent. The description field (e.g., "Compute protocol hash") is already provided by the agent. Enforcement-depth.md failure mode 4.

---

### M3. Lesson Specificity Gate

**What:** Require that every lesson's anti-pattern and quality gate contain a concrete verb (never/always/must) and a checkable condition.

**Where:** `.claude/commands/kernel/learn.md` — after recording the lesson (Step 3).

**Change:** Command text addition. New self-check:

```
Specificity check:
- Does your anti-pattern include a concrete verb (never/always/must)?
- Does your quality gate define a checkable condition (not just "be careful")?
- If either is No, rewrite before recording.
```

**Expected improvement:** Prevents vague lessons ("be more careful with paths") that don't prevent recurrence. Identified in loop-optimization.md and domain-setup-and-lessons.md.

---

### M4. Structured Domain Setup Extraction Output

**What:** Require structured output (table with file:line evidence) during step 4 (extract patterns) of domain setup.

**Where:** `.claude/skills/kernel-domain-setup/references/step-04-extract.md`.

**Change:** Step text addition. Require:

```
| Category | Pattern | Evidence (file:line) |
|----------|---------|---------------------|
```

**Expected improvement:** Grounds extracted patterns in observed code rather than agent assertions. Addresses domain-setup-and-lessons.md weakness 1 (under-specified extraction).

---

### M5. Graduated Sanction Escalation in Learn

**What:** Track lesson recurrence count and escalate visibility at thresholds.

**Where:** `.claude/commands/kernel/learn.md` — recurrence detection (Step 5). `.claude/commands/kernel/complete.md` — completion report.

**Change:** Command text additions:
- 2nd recurrence → promote to RULE ZERO (already happens informally; make explicit)
- 3rd recurrence → set `escalated_violation: true` in session state; anchor must include warning
- 4th+ recurrence → must appear in `/kernel/complete` report

**Expected improvement:** Provides graduated sanctions (Ostrom principle 5, OTP restart intensity). Currently all violations are treated identically regardless of recurrence history.

---

## Recommendations — Low Priority

### L1. Fresh Protocol Hash Per Anchor

**What:** Require the anchor command to compute a fresh hash each time (not compare against stored hash).

**Where:** `.claude/commands/kernel/anchor.md` — Step 1 (read protocol). `.claude/hooks/universal-gate-enforcer.py` — hash comparison logic.

**Change:** Command text update + ~5 lines in hook. The hook stores the protocol hash at anchor time. On next anchor, the agent submits a freshly computed hash. The hook compares submitted vs. stored. Mismatch = protocol changed since last anchor (warning, not block).

**Expected improvement:** Strengthens the anchor ceremony proof. Currently the agent can present a stored hash without re-reading the protocol. Fresh computation proves the file was read. Enforcement-depth.md scenario 4.

---

### L2. Track Reads in Actions Log

**What:** Add Read tool calls to the actions log (track but don't gate or increment counter).

**Where:** `.claude/hooks/actions-log-appender.py` — tool name filter.

**Change:** ~2 lines. Add `"Read"` to the tracked tools list with a flag that skips counter increment.

**Expected improvement:** Makes read-heavy work visible during anchor Part B review. Currently, research tasks that read 30+ files are invisible to enforcement. Enforcement-depth.md scenario 2.

**Caveat:** Increases log volume. May require raising the 200-line retention cap or accepting that read entries are lower priority.

---

### L3. Reduce Actions Limit to 15

**What:** Change `actions_limit` from 30 to 15 in `sr_dev_workflow.json`.

**Where:** `.claude/state/sr_dev_workflow.json` — `actions_limit` field.

**Change:** State value change (one number).

**Expected improvement:** Reduces maximum drift between anchors. The original design specified 10; 30 was set for operational convenience. 15 is a middle ground. Loop-optimization.md section 3.

**Caveat:** Increases anchor frequency. For tasks with many bash commands (pytest runs, git operations), 15 may feel interruptive. The error-weighted interval (M-priority if implemented) would complement this.

---

### L4. Protocol Completeness Check in Domain Setup

**What:** Add a cross-reference check between step 4 extraction output and step 8 protocol to verify no patterns were dropped.

**Where:** `.claude/skills/kernel-domain-setup/references/step-08-protocol.md`.

**Change:** Step text addition. After writing protocol: "For each pattern extracted in Step 4, verify it appears in the protocol reference table."

**Expected improvement:** Prevents silent pattern omission during domain setup. Domain-setup-and-lessons.md weakness 3.

---

## Do Not Do

### DN1. Auto-Generate Hook Rules from Lessons

**Status:** Considered and rejected.

**Reasoning:** Domain-setup-and-lessons.md Part 3 analyzed this in depth. While feasible (most enforceable lessons follow 3 patterns: bash match, path match, state check), the risks outweigh the benefits at current scale:
- False positive risk from auto-generated patterns (e.g., blocking `cd` in `echo "enter cd key"`)
- Hook complexity growth — auto-generated rules erode the 4-hook TCB boundary
- The manual promotion pipeline (learn → user reviews → implements hook) already works
- Premature automation of a judgment call (not all lessons should become hard blocks)

**Future:** Phase approach — enforceability assessment now (M3), pattern library later (when 5+ lessons assessed as enforceable), auto-suggest (not auto-apply) in future.

### DN2. Add a Reviewer Agent for Quality Assurance

**Status:** Considered and rejected under feature freeze.

**Reasoning:** External-governance-models.md identified self-assessment as an unsolvable problem within current constraints. A second agent reviewing the first agent's output would address the principal-agent problem and Ostrom's accountable monitoring principle. However, this is a new feature — it adds a command, a skill, and an execution pattern. The requirements cross-reference (M1) and structured Part B (H2) achieve partial mitigation without a new agent.

### DN3. Implement Error-Weighted Anchor Interval

**Status:** Considered and deferred.

**Reasoning:** Loop-optimization.md proposed reducing the anchor interval by half after a test failure. This is a good idea (one conditional in existing hook code) but introduces coupling between `needs_learn` state and the counter logic. The simpler fix (L3: reduce limit to 15) achieves a similar effect without the complexity. If L3 proves insufficient, error-weighting can be revisited.

### DN4. Add Capability-Per-Operation Granularity

**Status:** Considered and rejected.

**Reasoning:** External-governance-models.md explored scoped tokens (anchor token encodes what was reviewed) and operation-specific capabilities. While architecturally elegant (seL4 model), this is over-engineering for the current scale. The kernel governs one agent in one workspace. Capability granularity matters when multiple principals or multiple untrusted agents compete for resources. The current single-token model is sufficient.

### DN5. Add Proportional Governance (Risk-Weighted Action Limits)

**Status:** Considered and deferred.

**Reasoning:** External-governance-models.md (Ostrom principle) and enforcement-depth.md both noted that all actions face identical governance overhead. A production code write and a `git status` both increment the same counter. Risk-weighting would require classifying actions by risk level — a semantic judgment the hook can't reliably make. The safe-bash exemption is the kernel's crude approximation. More granularity would add complexity without clear benefit at current scale.

---

## Implementation Priority Matrix

| # | Recommendation | Priority | Change Type | LOC | Dependencies |
|---|---------------|----------|-------------|-----|-------------|
| H1 | Narrow auto-approve scope | HIGH | Hook code | ~4 | None |
| H2 | Structured anchor Part B | HIGH | Command text | ~10 | None |
| H3 | Block unsafe redirection | HIGH | Hook code | ~5 | None |
| M1 | Requirements cross-reference | MEDIUM | Command text | ~8 | None |
| M2 | Log bash description | MEDIUM | Hook code | ~1 | None |
| M3 | Lesson specificity gate | MEDIUM | Command text | ~6 | None |
| M4 | Structured extraction output | MEDIUM | Skill step text | ~8 | None |
| M5 | Graduated sanctions | MEDIUM | Command text + state | ~15 | None |
| L1 | Fresh protocol hash | LOW | Command + hook | ~10 | None |
| L2 | Track reads in log | LOW | Hook code | ~2 | None |
| L3 | Reduce actions limit | LOW | State value | 1 | None |
| L4 | Protocol completeness check | LOW | Skill step text | ~5 | M4 |

**No recommendation requires a feature freeze exception.** All changes modify existing hooks (code refinements), command files (text additions), or state values. No new commands, hooks, skills, or features.

**Recommended execution order:** H1 → H3 → H2 → M2 → M1 → M3 → M4 → M5 → L1-L4. Code changes (H1, H3, M2) first because they're smallest and most impactful. Command text changes (H2, M1, M3) next. State/config changes (L3) last.

---

## Meta-Finding

Across all 4 research files and 5 external models, one pattern repeats: **governance depth comes from rigor within a small surface area, not from expanding the surface area.** seL4 is 10,000 lines verified. OTP has 3 restart strategies. K8s admission has 2 phases. Ostrom's principles are 8. The kernel's 5 commands + 4 hooks is the right size. Every recommendation above deepens an existing mechanism. None adds a new one.
