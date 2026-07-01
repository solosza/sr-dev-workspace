# Build TDD Discipline Reference for Code-Heavy Domain Repos

## Status
Open

## Priority
Low-Medium — the kernel's gate contracts verify test existence but don't enforce test-before-code ordering. For code-heavy domains (QA platforms, RT automation, any application repo), TDD provides design-driving discipline and proof that tests actually test the right thing (watching fail). Not applicable to kernel itself or research work.

## Summary
Research (backlog 118, superpowers-research/tdd-assessment.md) assessed Superpowers' TDD skill against the kernel's existing test patterns. Recommendation: CONDITIONAL ADOPT — add TDD as a domain-specific protocol reference for repos with testable code. RED-GREEN-REFACTOR adapted to the kernel's atomicity constraint: combine RED+GREEN into a single "implement with TDD" task rather than splitting into 5 micro-tasks. Skip for kernel core and research work (gate contracts already sufficient). The anti-pattern reference (no mocking without understanding dependencies, no test-only methods in production classes) is the most directly applicable piece.

## Requirements
- Create `.claude/references/tdd-discipline.md` — canonical TDD reference document: RED-GREEN-REFACTOR cycle adapted for kernel atomicity, iron law (no production code without failing test first), anti-patterns reference (mocking, test-only methods, over-engineering), verification checklist
- Update `/kernel/domain-setup` step 8 (protocol building): when the domain has testable code (Python, TypeScript, SQL), reference tdd-discipline.md and add a protocol rule: "BUILD tasks that produce code MUST follow RED-GREEN-REFACTOR"
- Add hook warning (not block): when a test file creation timestamp is later than its corresponding production file, warn "Possible TDD violation — test created after code." Block is too aggressive; warning surfaces the pattern.
- Document the adaptation: in tdd-discipline.md, explain how the 5-step TDD cycle (write test, watch fail, write code, watch pass, refactor) maps to kernel task atomicity (one task covers write test + write minimal code together, a second task covers refactor)

## References
- Research assessment: `projects/superpowers-research/tdd-assessment.md`
- Superpowers source: `https://github.com/obra/superpowers`
- Domain setup step 8: `.claude/skills/kernel-domain-setup/references/step-08-protocol.md`
- Existing gate contracts: `.claude/skills/task-builder/references/verification-methods.md`
- Target repos: QA platforms (isagawa-qa), RT automation (projects/rt-automation), any BUILD domain

## Task Builder Input
- **Deliverable:** `.claude/references/tdd-discipline.md` reference document + updated domain-setup step 8 to reference it for code-heavy domains + hook warning for test-after-code detection
- **Location:** `workspace:.claude/references/`, `workspace:.claude/skills/kernel-domain-setup/references/`
- **Scope:** BUILD
- **Constraints:** Do NOT add to kernel core CLAUDE.md — this is domain-specific only. Domain-setup must detect whether the domain has testable code before wiring TDD. Hook must be a WARNING not a block (timing false positives are likely). TDD reference must adapt the 5-step cycle to kernel atomicity — do not prescribe 5 micro-tasks per behavior.
