# Build: JIT Rule Injection — Phase 1

## Status
Open

## Priority
Medium-High — 239 verdict: mechanism live-tested (`additionalContext` renders as system-reminder), 8 soft rules have caused repeat violations JIT would catch; phase 1 is deliberately small (2 rules, 1 hook file).

## Summary
Implement phase 1 of the 239 YAH verdict: a PreToolUse hook that inspects the attempted action and injects ONLY the relevant rule snippet as non-blocking advisory context — the exact rule at the exact moment it can be violated, zero standing context bloat. Phase 1 ships the 2 highest-priority rules from the research's candidate ranking with a rule-map JSON, dedup window, and measurement hook so later phases are driven by observed violation-rate reduction.

## Requirements
- New PreToolUse hook file (advisory — never blocks) + settings.json registration; returns `additionalContext` per the live-tested output schema in `projects/kernel-jit-rule-injection-research/02-injection-capability.md`
- Rule-map JSON: glob/tool-pattern → snippet, seeded with the top 2 rules from `projects/kernel-jit-rule-injection-research/01-rule-inventory.md` candidate ranking (read it — do not pick by memory)
- Payload discipline per `03-rule-map-design.md`: snippet size cap, consecutive-call dedup (same rule not re-injected on back-to-back matching calls)
- Measurement: injection events appended to a lightweight counter/log so phase 2 expansion is evidence-based
- L3 test: live session performs a matching tool call, assert the system-reminder appears and a non-matching call gets nothing; assert the hook never converts to a block
- Complementary, not replacement: no changes to anchor duties or existing blocking gates

## References
- Backlog done: 239; sibling builds 244, 245
- `.claude/hooks/sr_dev-gate-enforcer.py` (existing blocking half), `projects/kernel-jit-rule-injection-research/research-report.md` (phased rollout plan)

## Task Builder Input
- **Deliverable:** Advisory PreToolUse hook + rule-map JSON (2 rules) + injection counter + L3 live-injection test evidence
- **Location:** workspace
- **Scope:** BUILD
- **Constraints:** Hook loads at startup — set `needs_restart: true` on completion. Advisory only: any code path that returns a block is a defect. Phases 2-4 are OUT of scope (future backlogs gated on measured violation reduction).
