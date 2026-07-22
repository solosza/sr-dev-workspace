# JIT Rule Injection Research Report

## Verdict: YAH

JIT rule injection at the PreToolUse boundary should be added to the kernel as a complementary layer alongside the N-action anchor. It is technically feasible, architecturally sound, and addresses a real gap in the current enforcement model.

---

## Research Summary

### 01 — Rule Inventory (Task 002)

Catalogued 16 hard-enforced rules (H1–H16) across the universal gate enforcer, domain gate enforcer, code quality validator, and PostToolUse hooks. Identified 22 soft rules (S1–S22) from RULE ZERO and lessons that are currently protocol-only (agent self-enforcement).

Of the 22 soft rules:
- **2 are high JIT candidates** (S1: verify before write, S12: no unnecessary agents)
- **6 are medium candidates** (S3: wikilink tiering, S6: use kernel commands, S14: pytest rootdir, S17: AST semantics, S18/S22: vocab check, S19: PYTHONPATH)
- **14 are low/already enforced** (too abstract, too narrow, or already mechanical)

The 8 actionable candidates represent rules that have caused repeated violations documented in lessons.md, where a timely reminder at the tool boundary would have prevented the violation.

### 02 — Injection Capability (Task 003)

**Live-tested and confirmed:** Claude Code 2.1.207 PreToolUse hooks support non-blocking advisory context injection via `hookSpecificOutput.additionalContext` with `permissionDecision: "allow"` and exit 0.

The injected text appears as a `<system-reminder>` tag in the agent's context, formatted as `PreToolUse:[ToolName] hook additional context: [text]`. It renders with system-level authority, between the agent's tool call and the tool result, at the exact moment of relevance.

Key technical parameters:
- 10,000 character limit per injection (generous for rule snippets)
- Non-blocking: tool call proceeds, action counter unaffected by the advisory itself
- JSON schema: `hookSpecificOutput.additionalContext` field, requires `permissionDecision: "allow"`
- No fallback design needed — the primary mechanism works as intended

### 03 — Rule-Map Design (Task 004)

Designed a JSON rule-map schema with 5 trigger types (path_glob, content_match, command_match, session_state, always) and worked 6 examples covering the high and medium candidates.

Payload discipline:
- 500 chars per rule, max 5 rules per injection, 2,500 chars total
- 60-second dedup window per (rule, file) pair
- Priority-based ordering (safety > quality > convention > architecture)

Explicitly bounded JIT's coverage: it handles known per-action rules but cannot cover task-direction drift, cross-file architecture, protocol refresh, context recovery, violation self-correction, or re-centering cadence. These remain the anchor's irreducible duties.

---

## Trade-Off Analysis: JIT vs Current N-Action Anchor

### What the Current System Does Well

The N-action anchor (currently 30 actions) forces a full protocol re-read, lessons internalization, holistic work review, and context recovery. It catches violations retroactively in Part B and triggers the learn cycle. It's battle-tested through 46 lessons and has prevented countless regressions.

### What the Current System Misses

The anchor operates **retroactively**. It reviews work that already happened. If the agent violates a soft rule at action 3, the violation isn't caught until the anchor at action 30 — by then, the agent may have compounded the violation across 27 more actions. Examples from the lessons log:

- `cd` was used 7 times across two anchors before mechanical enforcement was added (lesson: RULE ZERO)
- Vocab leaks shipped through an entire pipeline because the check was structural, not content-aware (lesson #45)
- Agent spawning for research happened repeatedly despite the rule (lesson: RULE ZERO)

JIT catches these **at the boundary**, before the action executes. It's prevention vs. detection.

### Head-to-Head

| Dimension | N-Action Anchor | JIT Injection | Both Together |
|-----------|----------------|---------------|---------------|
| **Timing** | Retroactive (every N actions) | Preventive (every action) | Preventive + periodic review |
| **Scope** | Holistic (all work, all context) | Single-action (one tool call) | Full coverage |
| **Protocol refresh** | Full re-read | Snippet only | JIT keeps rules top-of-mind between anchors |
| **Drift detection** | Yes (Part B review) | No | Anchor catches what JIT can't |
| **Violation prevention** | No (catches after) | Yes (warns before) | Defense in depth |
| **Agent disruption** | Medium (pause for ceremony) | Zero (non-blocking) | Anchor cadence unchanged |
| **Maintenance cost** | Low (lessons.md is the source) | Medium (rule-map JSON must sync with lessons) | Acceptable if rule-map auto-derives |
| **False positive risk** | Low (human review) | Medium (pattern matching) | JIT false positives are advisory, not blocking |

### Net Assessment

JIT injection reduces the **rate** of per-action violations between anchors. It doesn't reduce anchor frequency — the anchor's irreducible duties (drift, architecture, refresh, recovery) are unaffected. The anchor catches what JIT misses; JIT prevents what the anchor would otherwise catch retroactively. Defense in depth.

The risk is maintenance overhead: the rule-map must stay synchronized with lessons.md. Mitigation: derive the rule-map from a structured section of lessons.md (or a companion file) rather than maintaining it separately. When `/kernel/learn` records a new lesson, it updates the rule-map if the lesson has a JIT-actionable trigger.

---

## Integration Design

### Architecture

```
PreToolUse event
    │
    ├── universal-gate-enforcer.py  (existing: gates, counter)
    ├── sr_dev-gate-enforcer.py     (existing: cd, intent, code quality, ceremony)
    └── jit-rule-injector.py        (NEW: advisory context injection)
                │
                ├── Load rule-map.json
                ├── Match tool_name + tool_input against triggers
                ├── Dedup against recent injections
                ├── Select top 5 by priority
                └── Return JSON with additionalContext
```

### Hook Registration

Add to `settings.local.json` PreToolUse:

```json
{
  "matcher": "Edit|Write|Bash|Agent",
  "hooks": [
    {
      "type": "command",
      "command": "python .claude/hooks/jit-rule-injector.py"
    }
  ]
}
```

Registered AFTER the gate enforcers so it fires only for allowed actions.

### Rule-Map Location

`.claude/rules/rule-map.json` — loaded by the JIT hook at each invocation. The file is derived from lessons.md quality gates and updated by `/kernel/learn` when a new JIT-actionable lesson is recorded.

### Implementation Phases

| Phase | Scope | Effort |
|-------|-------|--------|
| **Phase 1** | High-priority rules only (S1, S12) — 2 rules, simple triggers | Small (1 backlog) |
| **Phase 2** | Medium-priority rules (S3, S6, S14, S19, S22) — pattern matching | Medium (1 backlog) |
| **Phase 3** | Session-state tracking (Read history for S1) + dedup logic | Medium (1 backlog) |
| **Phase 4** | Auto-derivation from lessons.md + `/kernel/learn` integration | Large (1-2 backlogs) |

### Anchor Interaction

- **Anchor frequency unchanged.** The N-action limit remains at 30. JIT doesn't reduce it.
- **Anchor Part B simplified.** With JIT preventing common violations, Part B finds fewer violations, making the anchor faster and its output cleaner.
- **Learn cycle enriched.** When `/kernel/learn` records a lesson with a clear per-action trigger, it can auto-generate a rule-map entry, closing the loop from violation → lesson → JIT prevention.

---

## Risks and Mitigations

| Risk | Severity | Mitigation |
|------|----------|------------|
| Rule-map diverges from lessons | Medium | Auto-derive from lessons.md; `/kernel/learn` updates rule-map |
| False positives cause noise | Low | Advisory only (non-blocking); dedup window; priority cap at 5 rules |
| Hook latency per action | Low | JSON file load + pattern match is <50ms; no network calls |
| Agent ignores advisory context | Medium | Track compliance in anchor Part B; escalate to hard block if recurrent |
| Maintenance burden | Medium | Phase 1 starts with only 2 rules; grow organically with lessons |

---

## Verdict Rationale

**YAH** because:

1. **The mechanism exists and is proven.** Live test confirmed `additionalContext` works in PreToolUse, rendering as a system-reminder visible to the agent.
2. **The gap is real.** 8 soft rules have caused repeated violations that JIT would have prevented at the boundary.
3. **The design is complementary.** JIT doesn't replace the anchor — it reduces per-action violations between anchors while the anchor retains its irreducible duties.
4. **The cost is bounded.** Phase 1 is 2 rules and 1 hook file. Growth is organic, tied to new lessons.
5. **The risk is low.** Advisory injection is non-blocking; worst case is the agent ignores the reminder (same as current state without JIT).

**Not YAH because it replaces the anchor.** The anchor is still needed for drift, architecture, refresh, recovery, and violation self-correction. JIT is a complementary layer, not a replacement.
