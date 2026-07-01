# Cross-Document Consistency Verification

## Context
L3 semantic verification -- confirms all 7 design documents are internally consistent. Design documents produced in parallel can drift on shared decisions (tech stack, BYOK approach, pricing tiers, security model). This test reads all documents and checks for contradictions.

## Type
TEST

## Execution
agent

## Dependencies
- 010 (structural verification passed)

## Phase Gate
- [ ] Task 010 passed (all 7 documents exist and are non-empty)

## Requirements
Read all 7 design documents in `projects/eval-platform-design/` and verify consistency across these dimensions:

**Check 1: Tech stack consistency**
All documents should reference the same tech stack decisions without contradictions:
- Container orchestration: Google Cloud Run (MVP)
- Backend: FastAPI (Python)
- Frontend: Next.js
- Agent execution: Claude Agent SDK
- Sandbox: gVisor (MVP), Firecracker (enterprise)
- Database: PostgreSQL
- Job queue: Google Cloud Tasks
Documents to cross-check: `execution-pipeline.md`, `api-and-frontend.md`, `vertical-plugin-system.md`, `multi-tenancy-isolation.md`

**Check 2: BYOK model consistency**
The BYOK approach must be described identically across documents:
- Session-scoped in-memory key injection (MVP)
- Keys never in env vars, never on disk, never logged
- Container death = key destruction
Documents to cross-check: `byok-key-management.md`, `execution-pipeline.md`, `multi-tenancy-isolation.md`

**Check 3: GO (Conditional) conditions carried forward**
The conditions from 158's GO (Conditional) recommendation must appear as explicit constraints in the relevant design documents:
- Single vertical first (LLM Eval) -- should appear in `vertical-plugin-system.md`
- Validate flywheel before expanding -- should appear in `component-curation-pipeline.md`
- Cold start mitigation -- should appear in `component-curation-pipeline.md`
- Curation bottleneck risk -- should appear in `component-curation-pipeline.md`
Documents to cross-check: `prerequisite-gate.md` conditions vs all other documents

**Check 4: Rate limiting and tier consistency**
Rate limits, pricing tiers, and concurrent job limits must be consistent:
- Free: 1 concurrent, 50 runs/mo
- Pro: 3 concurrent, 500 runs/mo
- Enterprise: 10 concurrent, unlimited
Documents to cross-check: `multi-tenancy-isolation.md`, `api-and-frontend.md`

**Check 5: Timeout values consistency**
Timeout values must match across documents:
- Soft timeout: 8 minutes
- Hard timeout: 10 minutes
Documents to cross-check: `execution-pipeline.md`, `multi-tenancy-isolation.md`

Report for each check: PASS with evidence, or FAIL with the specific contradiction found.

## Acceptance Criteria
- [ ] Tech stack consistent across all documents (no contradictions)
- [ ] BYOK model described identically in byok, execution, and multi-tenancy docs
- [ ] All GO (Conditional) conditions appear as constraints in relevant docs
- [ ] Rate limiting tiers consistent between multi-tenancy and API docs
- [ ] Timeout values match between execution-pipeline and multi-tenancy docs

## Gates Satisfied
- TEST-01, TEST-02, TEST-03

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
