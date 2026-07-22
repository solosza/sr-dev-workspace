# Task 001: Research Existing Infrastructure

## Type
RESEARCH

## Objective
Audit what persona-like infrastructure already exists in the Isagawa kernel ecosystem. Map current capabilities to the 5 target personas (Developer, QA, PM, Sales, Marketing).

## Steps
1. Read and catalog existing harness repos and skills:
   - Developer: kernel commands, skills, hooks
   - QA: prod-test, gap-check, review-queue, eval
   - Sales: job-application-spec
2. Read Pulsia research (`projects/pulsia-research/`) for scale benchmarks
3. Read loop composability research (`projects/loop-composability-research/`)
4. Read agent orchestration framework (`docs/backlog/done/127-kernel-build-agent-orchestration-framework.md`)
5. Read harness design pattern docs (`docs/harness-design-pattern/`)
6. Produce inventory table: persona → existing commands/skills → gaps

## Deliverable
`projects/multi-persona-architecture/01-existing-infrastructure.md` — inventory of current capabilities mapped to personas

## Acceptance Criteria
- All 5 personas listed with existing vs missing capabilities
- References to actual file paths for existing infrastructure
- Gap analysis identifying what each persona needs
