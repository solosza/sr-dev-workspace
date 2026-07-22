# Step 1: Validate Input

## Purpose

Detect input mode (new build vs rebuild), resolve the command name, and validate the source against command-skill-pattern and tiered-index architecture. This is the corpus validation gate.

## Input

- Source path (command argument) — design doc, skill directory, command file, or bare name
- Completeness checklist: -> `.claude/docs/design/build-command/references/input-contract.md`
- Tiered-index architecture: -> `.claude/docs/design/tiered-index-architecture/index.md`

## Output

- Mode detection: `new_build` or `rebuild`
- Completeness report (presented to user)
- Tiered-index compliance report (presented to user)
- State file initialized at `.claude/state/build-command-state.json`

## Mode Detection

1. If path contains `docs/design` and ends with `index.md` → **new_build** mode
2. If path contains `skills/` → **rebuild** mode, command name = skill folder name
3. If path contains `commands/` → **rebuild** mode, read file → extract Skill Reference path → resolve
4. If bare name (no separators) → **rebuild** mode, resolve to `.claude/skills/[name]/SKILL.md`

In **rebuild** mode:
- Read all existing skill files (SKILL.md, workflow.md, gate-contract.md, steps/*, references/*, contracts/*)
- Check for associated design doc at `.claude/docs/design/[name]/index.md`
- Validate existing files against same checklist as new build
- Report which layers pass and which have gaps

## Acceptance Criteria

- [ ] Input mode detected (new_build or rebuild)
- [ ] Command name extracted from source path
- [ ] All 7 required sections checked (Identity, Philosophy, Vocabulary, Critical Rules, Workflow Summary, Step Specs, File Structure)
- [ ] All 5 optional sections checked (Reference Frontmatter, INDEX.md Structure, Contract Definitions, State Persistence, Hook Specs)
- [ ] Tiered-index Layer 1 compliance checked (see below)
- [ ] Tiered-index Layer 2 compliance checked (see below)
- [ ] Tiered-index Layer 3 compliance checked (see below)
- [ ] Combined report presented to user
- [ ] User confirms: `proceed`, `update`, or `stop`

## Tiered-Index Compliance Checks

### Layer 1: Organization

| Check | How to Verify |
|-------|---------------|
| index.md is pure index | No identity/philosophy/vocabulary/rules inline. Only tables pointing to payloads. |
| All payloads in references/ | No payload files alongside index.md |
| Every file under 200 lines | `wc -l` each .md file |
| No file is both index and payload | Index has tables + links, no substantive content. Payload has content, no navigation tables. |
| Folder structure matches canonical | `[topic]/index.md` + `[topic]/references/*.md` |

### Layer 2: Pre-Generation Checkpoints

| Check | How to Verify |
|-------|---------------|
| Workflow steps have checkpoints | Each step payload that generates output has a "Pre-generation checkpoint" block |
| Checkpoints list specific files | Reading list names exact file paths, not generic "read the references" |
| Checkpoints reference contracts | Steps with contracts point to the contract file |

### Layer 3: Contracts & Dual Gates

| Check | How to Verify |
|-------|---------------|
| Contract definitions exist | `references/contracts.md` or equivalent payload with full JSON definitions |
| Each contract has soft_validation_rules | At least one rule per contract |
| Each contract has mechanical_validations | Array present (may be empty with justification) |
| Contracts reference canonical examples | `canonical_reference` field points to existing file |

## References

- -> `.claude/docs/design/build-command/references/input-contract.md`
- -> `.claude/docs/design/build-command/references/cross-cutting-rules.md`
- -> `.claude/docs/design/tiered-index-architecture/index.md`

## Procedure

1. **Detect mode** from input path (see Mode Detection above)
2. Extract command name from source path
3. Initialize state file at `.claude/state/build-command-state.json` with `mode: "new_build"` or `mode: "rebuild"`
4. **If new_build:** Read the design doc index file, follow wikilinks to all payloads
5. **If rebuild:** Read existing skill files, check for design doc at `.claude/docs/design/[name]/index.md`
6. Check each section against the completeness checklist (7 required + 5 optional)
   - In rebuild mode: check sections exist in skill files (SKILL.md has Identity, Philosophy, etc.)
7. Check tiered-index Layer 1 compliance (index vs payload, 200-line, folder structure)
8. Check tiered-index Layer 2 compliance (checkpoints in workflow steps)
9. Check tiered-index Layer 3 compliance (contract definitions with rules)
10. Present combined report to user
    - In rebuild mode: also report which files exist, which are missing, and which have gaps

## Verification

Report format:
```
DESIGN DOC VALIDATION: [path]

Content (7 required + 5 optional):
  Required: N/7
  Optional: N/5

Tiered-Index Compliance:
  Layer 1 (Organization):  PASS / FAIL — [details]
  Layer 2 (Checkpoints):   PASS / FAIL — [details]
  Layer 3 (Contracts):     PASS / FAIL — [details]

RESULT: PASS | FAIL
```

## Failure Recovery

| Result | User Options |
|--------|-------------|
| All checks pass | `proceed` or `review` |
| Content sections missing | `update` / `proceed anyway` / `stop` |
| Tiered-index Layer 1 fail | `update` (MUST fix before build — index/payload mixing propagates) |
| Tiered-index Layer 2 fail | `update` / `proceed anyway` (checkpoints can be added post-build) |
| Tiered-index Layer 3 fail | `update` / `proceed anyway` (contracts can be added post-build) |
