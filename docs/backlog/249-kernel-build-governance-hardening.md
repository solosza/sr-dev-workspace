# Build: Governance Hardening — Policy/State Separation + Integrity Verification

## Status
Open

## Priority
High — answers the external review's most serious finding (#20 STRONG NAY: "if the agent can freely modify the hook code, policy files, or state files that govern it, the mechanical cage is self-modifiable"). Worktree + review-queue already gate hook CODE changes; this extends protection to integrity verification and state writes.

## Summary
Formalize the boundary between immutable policy (hooks, commands, protocol, CLAUDE.md, lessons) and mutable state (`.claude/state/*`), and mechanically verify it. Extend the existing protocol-hash mechanism to a policy manifest covering hooks and commands, verified at session entry (consistent with the validation-at-entry lesson). State writes go through the schema-validated atomic helper 244 introduces. Document `/kernel/review-queue accept` as the privileged human approval gate for any governance change.

## Requirements
- Policy manifest: `lib/attestation/policy-manifest.json` — SHA-256 per file over `.claude/hooks/*.py`, `.claude/commands/kernel/*.md`, `.claude/protocols/*.md`, `CLAUDE.md`; regenerated ONLY via a sanctioned regen script invoked at review-queue accept time
- Session-entry verification: `/kernel/session-start` verifies the manifest (entry-only, NOT per-action — lesson: protocol validation at entry, not execution, or concurrent agents deadlock); mismatch → report to user and STOP, never self-repair
- Policy-vs-state separation reference doc: which paths are policy (require review-queue accept to change) vs state (agent-writable via the 244 atomic helper only); wikilink from protocol References
- Gate enforcer: block Write/Edit to policy paths unless a sanctioned pipeline flag is set (worktree pipelines building hooks set it; interactive direct edits blocked with FIX pointing to the loop)
- Reframe the intent marker honestly: document `KERNEL_BACKLOG_INTENT` as an accident tripwire, not security (external review: "hidden env var as security — STRONG NAY"); no code change required beyond the doc
- Context-sensitive debug-statement gate (external review #28): `print()` block applies to framework/kernel source paths only — scratchpad, tools/, and generated report scripts exempt (live false positive 2026-07-21: build script blocked)
- L2/L3 tests: tamper a hook copy → session-start detects; attempt interactive policy edit → blocked; sanctioned pipeline edit → allowed; print() in tools/ → allowed, in hooks/ → blocked

## References
- External review 2026-07-21 (items 20, 21, 26, 28); backlogs 244 (atomic helper — prerequisite), 245/246 (hook-building pipelines this must not break)
- `.claude/hooks/universal-gate-enforcer.py` (protocol_hash precedent), `lib/attestation/` (existing intent chain), `.claude/state/review-status.json`

## Task Builder Input
- **Deliverable:** Policy manifest + regen script + session-start verification + separation reference doc + policy-path write gate + context-scoped print gate + L2/L3 tamper tests
- **Location:** workspace
- **Scope:** BUILD
- **Constraints:** Run AFTER 246 (it gates the very files 245/246 modify — sequencing avoids blocking those pipelines). Depends on 244's atomic write helper. Hook changes → needs_restart flow. Verification at session entry ONLY — never per-action.
