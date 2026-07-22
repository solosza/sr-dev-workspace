# Task 006: L2 - Sort + Cycle Unit Test
**Type:** TEST (L2) | **Gates:** DW-06
## Action
ONE test: build a 3-node graph (A, B independent; C depends_on [A,B]) - assert sort yields wave1={A,B}, wave2={C}. Build a cyclic graph (A->B->A) - assert the sort REJECTS it with a clear error and spawns nothing.
## Acceptance
Both assertions pass, exit 0. Red: fix then /kernel/learn.
