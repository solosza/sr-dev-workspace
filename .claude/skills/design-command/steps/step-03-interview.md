# Step 3: Interview

## Purpose

Extract structured requirements from the user through targeted questions. This step IS the interactive session.

## Input

- Confirmed command name + description from Step 1
- Selected reference design from Step 2
- Interview protocol: `.claude/docs/design/design-command/references/interview-protocol.md`

## Output

- Structured requirements object covering all 7 required sections

## Acceptance Criteria

- [ ] Requirements extracted for: identity, philosophy, vocabulary, critical rules, workflow, steps, file structure
- [ ] Each requirement category meets minimum depth from input-contract
- [ ] User confirmed the extracted requirements

## References

- Design doc: `.claude/docs/design/design-command/references/interview-protocol.md`
- Design doc: `.claude/docs/design/design-command/references/output-contract.md`

## Procedure

1. Present the reference design's workflow summary as a starting point
2. Ask the user to describe their command's workflow in similar terms
3. For each requirement category, extract or confirm:
   - **Steps:** What are the phases? What order?
   - **Inputs:** What does the command take? File paths? Names? Modes?
   - **Outputs:** What does it produce? Files? Reports? State changes?
   - **Constraints:** What must never happen? What are the hard rules?
   - **HITL:** Where does the user need to approve before continuing?
   - **State:** What needs to persist for resume?
4. Organize into structured format matching the completeness checklist

**Rule:** If the user gives a comprehensive description upfront, don't ask redundant questions. Extract what's there, confirm gaps only.

## Verification

Structured requirements include all 7 required sections at minimum depth:
- Identity: 1+ sentence
- Philosophy: 3+ principles
- Vocabulary: 3+ terms
- Critical rules: 2+ rules
- Workflow: 2+ steps with all 4 columns
- Step specs: purpose + procedure per step
- File structure: shows skills/ tree

## Failure Recovery

| Situation | Action |
|-----------|--------|
| User gives vague description | Ask targeted questions per category |
| User can't define philosophy | Propose principles based on constraints, confirm |
| Missing vocabulary | Extract terms from conversation, present for confirmation |
