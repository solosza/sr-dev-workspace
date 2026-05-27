# Task 015: Update workflow.md

**Type:** BUILD
**Action:** Add compliance validator references to workflow.md steps 03-05

## What

Edit `D:/my_ai_projects/project_test_repos/isagawa-qa/platform-ssh/.claude/skills/ssh-management-layer/workflow.md`

Add to the Key Classes section at the bottom:
- **ComplianceValidator** — Abstract base class for framework-specific validators
- **STIGValidator** — DISA STIG baseline validator (example pattern for agent generation)

Update Step 3 (Plan) description to include: "Select compliance validators (STIG, CIS, NIST, FIPS, PCI, HIPAA, SOC2, ISO27001) based on host frameworks config."

Update Step 4 (Execute) description to include: "Run compliance validators via SSHBatchExecutor. Results grouped by framework."

Update Step 5 (Report) description to include: "Report includes per-framework compliance status with by_framework grouping."

## Acceptance Criteria

- [ ] workflow.md references ComplianceValidator and STIGValidator in Key Classes
- [ ] Steps 3-5 reference compliance validators
