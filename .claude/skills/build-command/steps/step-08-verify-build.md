# Step 8: Verify Build

## Purpose

Check all generated files against command-skill-pattern requirements AND tiered-index architecture compliance. This is the final quality gate. A build that violates tiered-index fails.

## Input

- `files_written` list from state file
- Command-skill-pattern: -> `.claude/docs/design/command-skill-pattern/design.md`
- Tiered-index-architecture: -> `.claude/docs/design/tiered-index-architecture/index.md`

## Output

- Verification report (pass/fail per layer + tiered-index compliance)
- State file deleted on success, kept on failure

## Acceptance Criteria

- [ ] All per-layer checks pass (see Procedure)
- [ ] Every generated file <= 200 lines
- [ ] Design doc hash computed and written to SKILL.md frontmatter
- [ ] Tiered-index Layer 1 compliance verified on generated output
- [ ] Tiered-index Layer 2 compliance verified on generated output
- [ ] Tiered-index Layer 3 compliance verified on generated output
- [ ] State file deleted (success) or kept with failure details (failure)

## References

- -> `.claude/docs/design/command-skill-pattern/design.md`
- -> `.claude/docs/design/tiered-index-architecture/index.md`

## Procedure

1. List all generated files (from `files_written` in state)
2. **Per-layer checks:**
   - **L1 Command:** Has Usage, Examples, Design Reference link
   - **L2 Skill:** Has Identity, Philosophy, Vocabulary, Critical Rules, File Index
   - **L2 Workflow:** Has Phases, State Persistence
   - **L3 Steps:** Count matches design doc. Each has Purpose + Procedure
   - **L4 References:** INDEX.md wikilinks resolve to existing files
   - **L5 Contracts:** JSON is valid. Has soft_validation_rules + mechanical_validations
   - **L6 Hooks:** Only if design doc specified (otherwise skipped)
3. **200-line threshold:** Check every .md file
4. **Staleness hash:** Compute sha256 of design doc index -> verify matches SKILL.md frontmatter
5. **Tiered-index Layer 1 checks on generated output:**
   - SKILL.md is pure index (points to workflow, references, contracts -- no inline step content)
   - workflow.md is index or under 200 lines
   - Step files are pure payloads (content only, no navigation to siblings)
   - All payloads in correct folders (steps/, references/, contracts/)
   - No file is both index and payload
6. **Tiered-index Layer 2 checks on generated output:**
   - Every output-producing step in workflow.md has a "Pre-generation checkpoint" block
   - Checkpoints list specific file paths (not generic references)
   - Checkpoints include canonical reference + contract + prior step input
7. **Tiered-index Layer 3 checks on generated output:**
   - Contract JSON files exist for steps that the design doc specifies contracts for
   - Each contract has soft_validation_rules array with at least one rule
   - Each contract has mechanical_validations array (may be empty with justification)
   - canonical_reference fields point to existing files
8. All pass -> delete state file. Any fail -> report + keep state

## Verification

Report format:
```
BUILD COMPLETE: /[command-name]
Design doc: [path] (hash: [sha256])
Files created: N

Content checks:
  L1 Command ✓ | L2 Skill ✓ | L3 Steps ✓ | L4 Refs ✓ | L5 Contracts ✓ | L6 Hooks ✓/skipped

Tiered-Index compliance:
  Layer 1 (Organization):  PASS / FAIL — [details]
  Layer 2 (Checkpoints):   PASS / FAIL — [N/M steps have checkpoints]
  Layer 3 (Contracts):     PASS / FAIL — [N contracts, all valid]

200-line check: PASS / FAIL — [details]
Warnings: [count]
```

## Failure Recovery

Any check fails -> report which layer and which check. Keep state file for re-run.

**Tiered-index failures are blockers.** The build cannot pass with:
- A file that is both index and payload
- A workflow with no checkpoints on output-producing steps
- Missing contract definitions that the design doc specifies
