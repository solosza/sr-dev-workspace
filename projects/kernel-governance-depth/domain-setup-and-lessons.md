# Domain Setup and Lessons System Analysis

**Backlog:** 151 — Governance Depth Over Breadth
**Task:** 003-research-domain-setup-and-lessons
**Constraint:** No new commands or hooks proposed.

---

## Part 1: Domain Setup Bootstrapping

### Current Approach: Scan → Extract → Write Protocol

The domain-setup skill follows an 11-step sequence:

```
Prerequisites → Discover repo → Read code → Extract patterns → Understand enforcement
→ Read workflow → Build roadmap → Build protocol → Wrap commands → Update state → Report
```

The protocol it produces is a pure index — pointers to reference files, not duplicated content. The agent reads the actual files during each `/kernel/anchor`.

### Assessment: Is Scan-Repo → Extract → Write-Protocol the Best Bootstrap?

**Yes, with qualifications.**

The current approach has three structural strengths:

1. **Protocol-as-index prevents drift.** When the protocol points to actual code files, changes to the code automatically update what the agent reads during anchor. No sync problem. Duplicated content drifts the moment the source changes — indexing avoids this by design.

2. **Pattern extraction forces the agent to read before prescribing.** Steps 2-4 (discover, read, extract) require the agent to observe the repo's actual patterns before writing the protocol. This produces a protocol that reflects reality rather than imposing generic best practices. The alternative — template-based bootstrapping (stamp a generic protocol) — produces rules disconnected from the codebase.

3. **11 steps are sequential with checkpoints.** Each step produces output the next step consumes. Resume support (`resume_step`) means a failed setup can continue from where it stopped. This is superior to a monolithic "analyze everything and write protocol" approach.

**Qualifications — where bootstrapping quality could deepen without adding steps:**

#### Weakness 1: Step 4 (Extract Patterns) is Under-Specified

Step 4 asks "what layers exist?", "naming conventions?", "error handling?" — but doesn't require structured output. The agent can write a paragraph saying "the code uses snake_case" without providing evidence. Compared to the structured anchor table proposed in loop-optimization.md, step 4's output is free-form.

**Recommendation:** Add a structured output requirement to step-04-extract.md. For each pattern category (architecture, naming, anti-patterns, data), require at least one concrete example with file path and line reference. This is a step-file text change, not a new step.

```
| Category | Pattern | Evidence (file:line) |
|----------|---------|---------------------|
| Naming | snake_case functions | src/validator.py:42 |
| Architecture | 3-layer (config→validator→enforcer) | src/core.py:10-30 |
```

#### Weakness 2: No Initial Gate Tightness Calibration

The protocol bootstrapped by domain-setup has no opinion about gate strictness. The `actions_limit` defaults to whatever the kernel ships (currently 10, but sr_dev has it at 30). Whether the new domain should have a tight loop (10) or loose loop (30) depends on the domain's error rate and complexity — but domain-setup doesn't assess this.

**Recommendation:** Add a calibration note to step-08-protocol.md (build protocol): "Based on Step 4 findings, recommend an initial `actions_limit`. High-complexity domains (many layers, custom patterns) → 10. Low-complexity domains (few files, standard patterns) → 20. The agent states the recommendation and reasoning in the protocol." This is advisory text in an existing step, not a gate or hook.

#### Weakness 3: Protocol Quality Is Not Verified

After step 8 produces the protocol, no step verifies that the protocol actually indexes all the patterns extracted in step 4. A protocol could omit half the extracted patterns and step 9 (wrap commands) would proceed regardless.

**Recommendation:** Add a cross-reference check to step 8 or between steps 8 and 9: "For each pattern extracted in Step 4, verify it appears in the protocol's reference table. List any unindexed patterns." This is a verification substep within existing step flow, not a new step.

### Summary: Bootstrap Quality

| Aspect | Current | Improvement | Change Type |
|--------|---------|-------------|-------------|
| Protocol-as-index | Sound | None needed | — |
| Pattern extraction depth | Under-specified | Structured output table | Step text |
| Initial gate calibration | Missing | Advisory calibration note | Step text |
| Protocol completeness check | Missing | Cross-reference substep | Step text |

---

## Part 2: Lessons System

### Current Format

Each lesson in topic files follows:

```markdown
## [Date] [Issue Name]
- **Issue:** What happened
- **Root Cause:** Why it happened
- **Fix:** How it was resolved
- **Anti-Pattern Added:** What to avoid
- **Quality Gate Added:** What to check
```

The index file (`lessons.md`) has two tiers:
1. **RULE ZERO** — the most critical, recurrent lessons (currently ~40 lines)
2. **Topic index table** — links to 17 topic files with 32 total lessons

### Assessment: Is the Current Format Capturing Enough Signal?

**The format captures the right fields, but signal density varies.**

Strong examples (high signal):
- "NEVER USE `cd` IN BASH COMMANDS" — concrete verb, specific action, recurrence history with dates
- "NEVER BUNDLE ACTIONS INTO ONE TASK" — concrete anti-pattern, explains why, references the user correction count

Weak examples (low signal):
- Some topic-file lessons have vague anti-patterns: "be more careful with X" doesn't prevent recurrence
- Quality gates sometimes restate the fix instead of defining a checkable condition

**Recommendation: Lesson Specificity Gate.** Already proposed in loop-optimization.md (Section 4). The learn command text should require: "Does your anti-pattern contain a concrete verb (never/always/must)? Does your quality gate define a checkable condition (not just 'be careful')? If not, rewrite before recording." This is a command-text addition to learn.md, not a new mechanism.

### Lessons Compounding Strategy

The task asks three questions about compounding:

#### Q1: How should lessons compound over time?

Currently, lessons accumulate linearly. The index grows, topic files grow, RULE ZERO grows. The agent reads all of it during every anchor. This works at 32 lessons. At 100+, it will fail — the agent will skim RULE ZERO instead of internalizing it, defeating the anchor's purpose.

**Proposed compounding model: Tiered Promotion**

```
Tier 1: ACTIVE LESSONS (lessons.md RULE ZERO)
   ↑ Promote when: 2+ recurrences, still being violated
   │
Tier 2: TOPIC LESSONS (topic files)
   ↑ Promote when: first recorded via /kernel/learn
   │
Tier 3: GRADUATED (reference files or hooks)
   ↓ Demote from Tier 1 when: mechanically enforced by hook or codified in reference file
```

**Key insight:** A lesson that has been mechanically enforced (hook added) or codified (reference file updated) no longer needs to occupy RULE ZERO space. It graduated. The agent doesn't need to re-read "never use cd in bash" if the hook blocks cd commands automatically.

**Current state of this pattern:** Some lessons have already graduated partially. The `cd` lesson is in RULE ZERO *and* has a domain enforcer check proposed. Once the hook ships, the RULE ZERO entry can be shortened to: "cd in bash — enforced by hook. See sr_dev-gate-enforcer.py."

**Recommendation:** When a lesson becomes hook-enforced, shrink its RULE ZERO entry to a one-line reference: "[lesson] — GRADUATED to hook/reference. See [file]." This keeps the lesson visible (the agent knows the rule exists) without the multi-paragraph explanation. The explanation lives in the topic file for historical reference. This is a formatting convention, not a feature.

#### Q2: Should old lessons decay?

**No decay. Graduation instead.**

Decay (removing old lessons) is dangerous — a lesson removed might be the one preventing a recurrence. The kernel's own history shows lessons recurring months later (quick-anchor lesson from 2026-02-25 recurred on 2026-05-01 and 2026-05-26).

Instead of decay:
- **Graduate** lessons that are mechanically enforced → shrink to one-line reference
- **Archive** lessons that apply to deprecated features → move to `lessons/archived/`
- **Never delete** — even archived lessons remain readable

#### Q3: Should lessons promote to hard rules?

**They already do, but the pipeline is informal.**

The current learn command (step 4) says "Update hooks if enforceable" — this is the promotion-to-hard-rule path. The lesson "never use cd in bash" was manually identified as hook-enforceable and a domain enforcer check was proposed. But this promotion is ad-hoc — it depends on the agent or user recognizing enforceability.

**Recommendation: Enforceability Assessment in Learn Command.** Add a required substep to learn.md after recording the lesson:

```
Enforceability check:
- Can this failure be detected mechanically? (Y/N)
- If Y: which hook could detect it? (universal / domain / test-failure / actions-log)
- Proposed detection: [pattern match, state check, etc.]
- Effort: [one-line change / conditional / new function]
```

This doesn't auto-generate the hook — it documents whether the lesson *could* be enforced. The user then decides whether to implement the enforcement. This is a text addition to learn.md, not a code change.

---

## Part 3: Auto-Enforcement Feasibility

### The Question: Should lessons auto-generate enforcement (lesson → hook rule)?

**Feasibility: Medium. Recommendation: Not yet.**

#### What Auto-Enforcement Would Look Like

```
Agent records lesson "never use cd in bash"
→ Learn command detects enforceability
→ Auto-generates hook code:
    if 'cd ' in command and not in safe_patterns:
        block("cd detected. Use absolute paths.")
→ Adds to domain enforcer
→ Next session loads updated hook
```

#### Why It's Feasible in Theory

The kernel already has:
- A domain enforcer with a pattern-matching structure (sr_dev-gate-enforcer.py)
- PreToolUse event with full tool input access
- A convention for blocking messages (exit code 2, stderr)
- The learn command already modifies hooks (step 4)

Most enforceable lessons follow one of three patterns:
1. **Bash command pattern match** — block commands containing X (cd, intent.py record)
2. **File path pattern match** — block writes to X path (hooks/, settings)
3. **State condition check** — block when state field Y is Z

Auto-generating any of these three patterns from a structured lesson is mechanically straightforward.

#### Why It's Not Recommended Now

1. **False positive risk.** Auto-generated patterns can block legitimate actions. A pattern that blocks "cd " in bash would also block `echo "enter cd key"`. Human review catches these edge cases; auto-generation doesn't. The current system of human-reviewed hook changes is slower but safer.

2. **Hook complexity growth.** Each auto-generated rule adds conditionals to the enforcer. At 10 rules, the hook is manageable. At 50 auto-generated rules, the hook becomes slow and hard to debug. The current 4-hook constraint implicitly caps complexity — auto-generation would erode this.

3. **The promotion pipeline works manually.** The learn command already says "update hooks if enforceable." The gap isn't automation — it's the enforceability assessment step (proposed above). Once the agent consistently documents enforceability, the user can implement the hook change in a controlled way.

4. **Premature automation of a judgment call.** Deciding whether a lesson should become a hard block requires domain judgment. "Never use cd in bash" is a clear block. "Always verify testing completeness during atomization" is not — it's a protocol discipline, not a pattern match. Auto-enforcement can't distinguish between these.

#### Recommendation

**Phase the approach:**

| Phase | Action | When |
|-------|--------|------|
| Now | Add enforceability assessment to learn.md | Immediately |
| Later | Build a pattern library of common enforcement templates | When 5+ lessons have "enforceable: Y" assessments |
| Future | Auto-suggest (not auto-apply) hook rules from the pattern library | When the pattern library has proven templates |

The key distinction: **auto-suggest vs auto-apply.** The system should eventually suggest enforcement code for the user to review, not silently modify hooks. This preserves human oversight while reducing the effort to implement enforcement.

---

## Summary

| Question | Finding | Recommendation |
|----------|---------|----------------|
| Is scan → extract → write-protocol the best bootstrap? | Yes, protocol-as-index is sound | Deepen with structured extraction output, calibration note, completeness check |
| How can protocol quality improve without adding steps? | Step text changes to existing steps | Structured output in step 4, cross-reference in step 8 |
| Should domain-setup produce tighter initial gates? | Currently no gate calibration | Add advisory calibration note to step 8 |
| Is the lesson format capturing enough signal? | Format is right, signal density varies | Add specificity gate to learn command |
| How should lessons compound? | Linear growth will break at scale | Tiered promotion: active → topic → graduated |
| Should lessons decay? | No — graduate instead of decay | Graduated lessons shrink to one-line references |
| Should lessons auto-generate enforcement? | Feasible but premature | Phase: assess now, library later, suggest future |
