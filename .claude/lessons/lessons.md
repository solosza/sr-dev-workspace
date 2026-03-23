# Lessons Learned — Index

<!-- Updated by /kernel/learn after failures -->
<!-- Tiered: this file is the index. Details in topic files. -->

## RULE ZERO — Read this every anchor

**NEVER ASSUME. ALWAYS VERIFY.** Read the actual files before acting. Don't guess what a file contains, what a config looks like, or what's wired up. Open it and read it. This applies to hooks, state, settings, code — everything. Assumptions caused: missing hooks (settings.local.json never created), stale counters (27 actions untracked), wrong backlog location, wrong naming conventions. Verify first, act second.

**NEVER QUICK-ANCHOR.** When the counter hits the limit, do a FULL anchor — Read protocol, Read lessons, apply rules to next action with concrete verbs, review inter-anchor work. Skipping any part is a violation. The anchor exists to re-center, not to reset a counter. This violation recurred 2026-03-22 even after the lesson was already recorded and read earlier in the same session.

**NEVER USE `cd` IN BASH COMMANDS.** Hooks resolve relative to cwd. Any `cd` shifts cwd for the rest of the session and breaks hook path resolution (`python .claude/hooks/...` fails). Use absolute paths in all Bash commands. If you must reference another directory, use the full path — never `cd` into it. This broke hooks twice in one session (2026-03-22).

---

| Topic | File | Lessons |
|-------|------|---------|
| Kernel Compliance | `kernel-compliance.md` | Hook bypass, quick anchor, dismissing work, words ≠ actions |
| Git & Branching | `git-and-branching.md` | Golden master, feature branches, branch strategy per repo type, repo reset |
| Infrastructure & Setup | `infrastructure-setup.md` | Playwright MCP setup, hook registration |
| Repo Topology | `repo-topology.md` | Kernel repo map, sync rules |
| Cycling Run 1 | `cycling-run.md` | Learn self-enforcement, complete gate, dual state, redundant specs, uncommitted output |
| Cycling Run 2 | `cycling-run-2.md` | Recreated existing files, CSS over role selectors, anchor missed violation, fix priorities |
| Cycling Run 3 | `cycling-run-3.md` | BI compliance blind spot, counter reset mechanism (use Write not Edit for anchor reset) |
| Domain Decomposition | `domain-decomposition.md` | 3 spec types (BUILD/WORKSPACE/OPERATE), decompose before research, anatomy mapping, factory orchestration, SDD connection |
| Meta-Spec Validation | `meta-spec-validation.md` | Gate-contract-driven validation, no validation skill, orchestrator reads gate-contract.md, builder never validates itself |
