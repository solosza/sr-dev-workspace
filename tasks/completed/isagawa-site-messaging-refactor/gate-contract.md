# Gate Contract: Isagawa.co Site Messaging Refactor

## BUILD Gates

| Gate | Check | Type | Verification | Status |
|------|-------|------|--------------|--------|
| BUILD-001 | index.html hero title updated | structural | grep -c "SDD architecture for governed agents" index.html | PASS if count ≥ 1 |
| BUILD-002 | index.html hero subtitle updated | structural | grep -c "Isagawa turns repeatable workflows" index.html | PASS if count ≥ 1 |
| BUILD-003 | Growth subtitle updated | structural | grep -c "SDD architecture:" index.html | PASS if count ≥ 2 |
| BUILD-004 | Growth narrative updated | structural | grep -c "compile specifications into structured agents" index.html | PASS if count ≥ 1 |
| BUILD-005 | Self-extension card 1 updated | structural | grep -c "Every capability begins as intent" index.html | PASS if count ≥ 1 |
| BUILD-006 | Self-extension card 2 updated | structural | grep -c "Autonomous for deterministic execution; HITL" index.html | PASS if count ≥ 1 |
| BUILD-007 | kernel.html references updated | structural | grep -c "SDD architecture" kernel.html | PASS if count ≥ 1 |

## TEST Gates

| Gate | Check | Type | Verification | Status |
|------|-------|------|--------------|--------|
| TEST-001 | No "natural language" claims remain | functional | ! grep -q "natural language" index.html | PASS if grep returns nothing |
| TEST-002 | No absolute claims remain | functional | ! grep -q "mechanically can't\|physically cannot\|no human intervention" index.html | PASS if grep returns nothing |
| TEST-003 | HTML syntax valid | structural | grep -c "</html>" index.html | PASS if count = 1 |

## Acceptance Criteria
- All BUILD gates PASS
- All TEST gates PASS
- Changes committed to feature branch (not merged)
- User validation on local branch before merge decision
