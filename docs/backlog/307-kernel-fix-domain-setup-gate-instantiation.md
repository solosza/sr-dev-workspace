# Fix kernel-domain-setup to instantiate + register the domain gate enforcer

## Status
Open

## Priority
High - every domain bootstrapped by the kernel ships without a domain-specific write-time gate, so layer-boundary / vocab / contract violations go unenforced until someone hand-builds the enforcer.

## Summary
`kernel-domain-setup` ships a `domain-gate-enforcer.template.py` (present in the platform-multi-interface spec) but its 11-step workflow has no step that instantiates the template into an active `{domain}-gate-enforcer.py` or registers it as a PreToolUse hook. Bootstrapped domains therefore wire only the generic `universal-gate-enforcer.py` and get no domain-specific write-time enforcement. The sr_dev workspace has a hand-built `sr_dev-gate-enforcer.py` proving the pattern is real, but domain-setup does not reproduce it. Separately, `CLAUDE.md` over-claims that `/kernel/domain-setup` "creates protocol + hooks" (plural) when it only wires the universal enforcer.

## Root Cause
- Skill step table (SKILL.md steps 1-11): step 5 "Understand enforcement" and step 10 "Update state" register `universal-gate-enforcer.py` only; no step reads the template, writes the instance, or registers a second PreToolUse entry.
- The template is shipped but orphaned - nothing consumes it during bootstrap.

## Evidence (Phase 2 prod-test, platform-multi-interface domain spec)
- Spec repo `platform-multi-interface/.claude/hooks/` contains `domain-gate-enforcer.template.py` + `universal-gate-enforcer.py`.
- After domain-setup bootstrapped domain `multi_interface_qa`: protocol + state + qa-workflow all wired, framework smoke green - but no instantiated `multi_interface_qa-gate-enforcer.py` and no PreToolUse registration for it.
- Contrast: `sr_dev_workspace/.claude/hooks/sr_dev-gate-enforcer.py` exists (hand-built), demonstrating the intended end state domain-setup fails to produce.

## Requirements
- Add a step to `kernel-domain-setup` that: (a) reads `domain-gate-enforcer.template.py`, (b) instantiates it as `{domain}-gate-enforcer.py` with the domain name substituted, (c) registers it as a PreToolUse hook in `.claude/settings.local.json` alongside the universal enforcer.
- Correct `CLAUDE.md` so its description of `/kernel/domain-setup` matches what it actually wires (do not over-claim "hooks" if only the universal enforcer is registered by default; state the domain gate is now instantiated too once this ships).
- Fix in the master kernel at `D:/my_ai_projects/isagawa-kernel` first, then propagate to the platform-multi-interface spec's copy of `kernel-domain-setup` (and any other spec that carries the skill).
- Re-test on a FRESH git clone: run domain-setup, then verify the domain gate IS instantiated + registered and the framework smoke is still green.

## References
- `.claude/skills/kernel-domain-setup/SKILL.md` (step table)
- `.claude/skills/kernel-domain-setup/references/step-05-enforcement.md`, `step-10-state.md`
- `.claude/hooks/sr_dev-gate-enforcer.py` (the hand-built reference instance)
- `platform-multi-interface/.claude/hooks/domain-gate-enforcer.template.py` (the orphaned template)
- Master kernel: `D:/my_ai_projects/isagawa-kernel`
- Related: the multi_interface_qa domain gate being built in this session (spec-side counterpart of this kernel fix)

## Task Builder Input
- **Deliverable:** A `kernel-domain-setup` skill that instantiates + registers a domain-specific gate enforcer during bootstrap, corrected `CLAUDE.md` claim, verified on a fresh clone.
- **Location:** `new-repo:D:\my_ai_projects\isagawa-kernel` (master kernel; propagate to spec copies afterward)
- **Scope:** BUILD
- **Constraints:** Fix master kernel first, then propagate. Must not break existing universal-enforcer registration. Re-test bootstrap on a fresh clone. Keep the instantiated enforcer consistent with the existing `sr_dev-gate-enforcer.py` thin-orchestrator pattern (uses shared `lib/validators`).
