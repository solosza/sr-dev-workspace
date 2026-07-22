# Step 4: Draft Design Doc

## Purpose

Generate the complete design doc content from structured requirements.

## Input

- Structured requirements from Step 3
- Selected reference design from Step 2 (structural template)
- Completeness checklist from input-contract

## Output

- Draft content for all design doc files (index.md + payload files)

## Acceptance Criteria

- [ ] index.md has YAML frontmatter (name, type, version, date_created, status, purpose)
- [ ] All 7 required sections present in draft (index or payloads)
- [ ] index.md stays under 200 lines (overflow → extract to payload)
- [ ] Tiered format: index links to payloads, no monolithic files
- [ ] Design Documents table present with wikilinks to all payloads

## References

- Design doc: `.claude/docs/design/design-command/references/workflow.md` (Step 4)
- Design doc: `.claude/docs/design/design-command/references/output-contract.md`

## Procedure

1. Read the reference design's index.md — use as structural template
2. Read command-skill-pattern completeness checklist
3. For each required section, generate content from interview results:
   - **Skill Identity:** One sentence from description + interview
   - **Philosophy:** 3-5 principles from constraints + user values
   - **Vocabulary:** Terms that emerged during interview
   - **Critical Rules:** Hard constraints from interview
   - **Workflow Summary:** Steps table from interview
   - **Step Specs:** Per-step Purpose + Procedure (in workflow.md payload)
   - **File Structure:** Derive from step count + whether contracts/hooks needed
4. For optional sections, generate if requirements exist:
   - Contract definitions (if user specified validation rules)
   - State persistence (if resume needed)
   - Hook specs (if mechanical gates needed)
5. Split into index.md (overview, tables, links) + references/ payloads (details)

## Verification

- Draft index.md under 200 lines
- All 7 required sections present
- Tiered structure (index + payloads, not monolith)

## Failure Recovery

| Situation | Action |
|-----------|--------|
| Index exceeds 200 lines | Extract largest section to payload, replace with wikilink |
| Required section missing from requirements | Loop back to Step 3 to fill gap |
