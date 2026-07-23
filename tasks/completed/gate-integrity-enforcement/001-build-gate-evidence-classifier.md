# Task 001: Gate-Evidence Classifier
**Type:** BUILD | **Gates:** GI-01
## Action
Add a helper (lib/gate_integrity.py or extend lib/observability.py) that classifies a GATE/L3 task's evidence as live / simulated / empty.
## Spec
READ lib/observability.py (276 completion-truth oracle) FIRST — COMPOSE with it, do not re-implement. Given a gate/L3 task's evidence (its iteration log + any recorded command/output artifact), classify: LIVE (a re-runnable command + captured non-empty real output), SIMULATED (evidence describes a simulation / 'would run' / no real execution), or EMPTY (0-byte log / no output). A gate whose evidence is simulated or empty is a DEFECT — the classifier returns that verdict so the orchestrator/runner can reject it (reaffirms lessons #39, #49). Detect the '247 L3 was a simulation not a live swarm' + '208 UT-04 0-byte log' shapes.
## Acceptance
A helper that returns live/simulated/empty for a gate task's evidence; simulated+empty flagged as defects; composes with 276.
