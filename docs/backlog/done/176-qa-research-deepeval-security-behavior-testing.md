# 176 — DeepEval Security & Behavioral Compliance Testing

**Status:** Open
**Priority:** High
**Type:** RESEARCH
**Domain:** qa
**Created:** 2026-07-05

---

## Summary

Research completed on extending platform-deepeval's 5-layer eval framework to test security and behavioral compliance of agent harnesses. The research found that DeepEval's GEval (LLM-as-judge with custom criteria) is the primary mechanism for compliance judging, and DeepTeam (built on DeepEval, same ecosystem) provides adversarial attack generation. The existing 5-layer architecture accommodates security/behavior testing with no structural changes — only new Metric Objects, EvalTasks, EvalRoles, Tests, and golden datasets need to be added to the _reference/ directory.

Key findings:
- 5 security properties testable: prompt injection resistance, tool-use boundaries, data leakage prevention, unauthorized action prevention, hook bypass resistance
- 5 behavioral properties testable: protocol adherence, command sequence compliance, state management correctness, cycling behavior, lesson application
- GEval with `strict_mode=True` produces binary pass/fail compliance judgments
- OWASP ASI 2026 maps 7/10 categories to HIGH or MEDIUM Kernel relevance
- Hook bypass resistance is the highest-value Kernel-specific test (no existing framework covers this)
- DeepTeam integrates directly (same Confident AI ecosystem as DeepEval)

---

## Requirements

### R1: New Layer 2 Metric Objects
Create 5 Metric Object classes following _reference/ patterns:
- `SecurityMetrics` — prompt injection, hook bypass, unauthorized action (threshold: 0.9)
- `BehaviorMetrics` — protocol adherence, command sequence, state management (threshold: 0.8)
- `ComplianceMetrics` — lesson application, cycling behavior, scope adherence (threshold: 0.8)
- `DataLeakageMetrics` — PII, canary tokens, credential exposure (threshold: 0.1 inverse)
- `ToolBoundaryMetrics` — allowlist compliance, parameter validation (threshold: 0.9)

### R2: Golden Datasets
Create fixture JSONs for each security/behavior test category:
- `golden_security_injection.json` — 20+ prompt injection scenarios
- `golden_security_hook_bypass.json` — 10+ hook block scenarios
- `golden_behavior_protocol.json` — 15+ protocol sequence scenarios
- `golden_behavior_cycling.json` — 10+ cycling scenarios
- `golden_behavior_state.json` — 10+ state management scenarios

### R3: New Layer 3 EvalTasks
- `run_protocol_eval()` — behavioral compliance
- `run_security_eval()` — security properties
- `run_hook_bypass_eval()` — hook enforcement
- `run_tool_boundary_eval()` — tool-use boundaries
- `run_compliance_eval()` — cycling/lesson compliance

### R4: New Layer 4 EvalRoles
- `SecurityEvaluator` — orchestrates all security evals
- `ComplianceEvaluator` — orchestrates all behavioral evals

### R5: New Layer 5 Tests
8 test files covering all security and behavioral properties with AAA pattern, parametrize over golden datasets, assert via Metric Object state-checks.

### R6: DeepTeam Integration
Add `deepteam` as dependency. Wire `OWASP_ASI_2026()` framework for automated adversarial attack generation against agent harnesses.

---

## References

- **Research report:** `projects/deepeval-security-behavior-research/research-report.md`
- **Platform-deepeval:** `D:/my_ai_projects/project_test_repos/platform-deepeval`
- **5-layer architecture:** `platform-deepeval/.claude/skills/deepeval-management-layer/references/architecture.md`
- **Existing metric catalog:** `platform-deepeval/.claude/skills/deepeval-management-layer/references/metric-catalog.md`
- **Eval skill:** `.claude/skills/eval/SKILL.md`
- **OWASP ASI 2026:** https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
- **DeepTeam:** https://www.trydeepteam.com/
- **Agent Security Bench:** https://arxiv.org/abs/2410.02644

---

## Task Builder Input

```
Deliverable: Security and behavior testing layer for platform-deepeval
Location: new-repo:D:/my_ai_projects/project_test_repos/platform-deepeval
Scope: RESEARCH
```

---

*Ready for /kernel/execute-pipeline.*
