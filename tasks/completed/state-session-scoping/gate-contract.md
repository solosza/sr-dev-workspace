# Gate Contract — State Session Scoping

## L1: Structural Gates

| ID | Check | Method |
|----|-------|--------|
| STRUCT-01 | session-start.md contains one_shot guard in step 6 | grep |
| STRUCT-02 | universal-gate-enforcer.py contains one_shot bypass logic | grep |

## L2: Functional Gates

| ID | Check | Method |
|----|-------|--------|
| FUNC-01 | universal-gate-enforcer.py compiles without errors | py_compile |
| FUNC-02 | gate enforcer accepts stdin JSON without crashing | echo + python |

## L3: Integration Gates

| ID | Check | Method |
|----|-------|--------|
| INTEG-01 | With one_shot=true and anchored=false, gate enforcer does NOT block | simulate |
| INTEG-02 | With one_shot=false and anchored=false, gate enforcer DOES block | simulate |
| INTEG-03 | Session-start with one_shot=true preserves anchored=true in workflow state | simulate |
