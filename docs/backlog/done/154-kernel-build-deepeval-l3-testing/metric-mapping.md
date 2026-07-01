# Metric Mapping: DeepEval Metrics → Kernel Command Evaluation

## Status
NEW

## Purpose

Map DeepEval's metric library to kernel command evaluation needs. Kernel commands are Agent pipelines — they use tools, follow protocols, produce artifacts. The metric selection must reflect this.

## Pipeline Type: Agent

platform-deepeval's SKILL.md defines pipeline types. Kernel commands are **Agent** pipelines:
- They use tools (Read, Write, Edit, Bash, openpyxl)
- They follow multi-step protocols (SKILL.md → workflow.md → step files)
- They produce structured output (xlsx updates, state files, user-facing displays)

Agent pipeline auto-selects: **ToolCorrectness**, **TaskCompletion**

## Metric Selection

### Auto-Selected (Agent Pipeline)

| Metric | What It Evaluates | Kernel Command Application |
|--------|-------------------|---------------------------|
| ToolCorrectness | Did the agent use the right tools with correct parameters? | Did check-data read the right xlsx cells, write to correct columns, call openpyxl correctly? |
| TaskCompletion | Did the agent complete all required sub-tasks? | Did check-data execute all 10 steps, update all required fields, produce complete output? |

### Custom GEval (Protocol Faithfulness)

DeepEval's GEval metric allows custom evaluation criteria. For kernel commands, protocol faithfulness is critical — the agent must follow its skill instructions, not improvise.

| GEval Criterion | Description | Example |
|-----------------|-------------|---------|
| Rule Compliance | Agent followed all Critical Rules in SKILL.md | "Did the agent verify DRG-to-MDC via lookup table (Rule 5) instead of assuming?" |
| Step Ordering | Agent executed steps in the prescribed sequence | "Did the agent run Step 3 (assign dates) before Step 4 (QNXT changes)?" |
| Constraint Satisfaction | Agent checked all soft validation rules from contract | "Did the agent check SV-305 (clean break per member) before accepting dates?" |
| Output Completeness | Agent displayed all required information per step spec | "Did Step 6 output include history claim ID, member, DRG, MDC, enddate AND readmission details?" |

### Optional Metrics (Per Contract)

| Metric | When to Use | Contract Signal |
|--------|-------------|-----------------|
| Faithfulness | When contract has `context` references (canonical docs) | `soft_validation_rules[].check` references a specific document |
| Hallucination | When agent must not invent data | Any step that reads from xlsx/DB — output must match source |
| AnswerRelevancy | When agent produces user-facing explanations | Step 6 (Output) — displayed info must be relevant to the TC |

## GEval Criteria Generation

GEval criteria are generated from contract JSONs:

```
Contract: soft_validation_rules[]
  → GEval criterion per rule
  → evaluation_params: ["input", "actual_output", "expected_output"]
  → threshold: from contract's confidence_threshold or default 0.7

Contract: success_criteria[]
  → GEval criterion per success condition
  → Used for TaskCompletion scoring
```

### Example: check-data Step 3 Contract → GEval

```json
{
  "name": "SV-301 Compliance",
  "criteria": "Evaluate whether the agent verified that the assigned date pair is unique for this history claim in the date registry before accepting it. The agent should have checked all existing entries for the same history_claim_id and confirmed no duplicate (admit, discharge) pairs exist.",
  "evaluation_params": ["input", "actual_output", "expected_output"],
  "threshold": 0.8
}
```

## Metric Thresholds

| Level | Threshold | Meaning |
|-------|-----------|---------|
| Minimum viable | 0.5 | Agent attempts the right approach but has gaps |
| Acceptable | 0.7 | Agent follows protocol with minor deviations |
| Production ready | 0.85 | Agent consistently follows protocol, correct output |
| Target | 0.95 | Near-perfect protocol adherence and output quality |

Thresholds apply per-metric. Overall pass/fail uses the lowest individual score.

## Dependencies

- platform-deepeval must support GEval with custom criteria
- Contract JSONs must have `soft_validation_rules` for GEval generation
- Agent output capture must provide reasoning traces for faithfulness evaluation
