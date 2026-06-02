# Research: Candidate Kernel Capabilities for MCP Exposure

## Context
With MCP development effort understood, assess which kernel capabilities are worth exposing as MCP tools and what workflows they would enable that aren't possible today.

## Type
RESEARCH

## Execution
inline

## Dependencies
- 002-kernel-research-mcp-spec-and-frameworks.md

## Phase Gate
- [ ] `projects/mcp-server-research/mcp-frameworks-summary.md` exists

## Requirements
- Survey kernel capabilities: `lib/attestation/attest.py`, pipeline state queries, backlog management
- For each candidate capability, assess:
  - What MCP tool would it expose? (name, inputs, outputs)
  - Who would call it? (other Claude sessions, VS Code extension, web UI)
  - What workflow becomes possible that isn't possible with the current run-task.sh + execute-pipeline architecture?
- Rank candidates by value: which single capability would provide the most value if exposed as an MCP tool?
- Assess: does MCP exposure complement or compete with run-task.sh?
- Write to `projects/mcp-server-research/capabilities-assessment.md`

## Acceptance Criteria
- [ ] `projects/mcp-server-research/capabilities-assessment.md` exists
- [ ] File covers attestation as a candidate
- [ ] File assesses at least 3 kernel capabilities
- [ ] File has ranked list of candidates

## Gates Satisfied
- DOC-04, DOC-05

## Completion Signal
When ALL acceptance criteria are met, invoke `/kernel/complete`.
