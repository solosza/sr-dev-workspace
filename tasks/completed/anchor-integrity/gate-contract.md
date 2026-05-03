# Gate Contract — Anchor Integrity

## L1: Structural Gates

| ID | Check | Method |
|----|-------|--------|
| STRUCT-01 | anchor.md contains `hashlib` or `hash` instruction | grep |
| STRUCT-02 | anchor.md references `protocol_hash` field | grep |
| STRUCT-03 | universal-gate-enforcer.py contains hash verification function | grep |
| STRUCT-04 | universal-gate-enforcer.py imports hashlib | grep |

## L2: Functional Gates

| ID | Check | Method |
|----|-------|--------|
| FUNC-01 | universal-gate-enforcer.py runs without syntax errors | python -c "import" |
| FUNC-02 | Hook processes valid stdin JSON without crashing | echo JSON \| python hook |

## L3: Integration Gates

| ID | Check | Method |
|----|-------|--------|
| INTEG-01 | After anchor, session_state.json contains protocol_hash field | anchor + grep |
| INTEG-02 | protocol_hash matches SHA-256 of current protocol file | python hash compare |
| INTEG-03 | Hook allows action when hash is valid | echo JSON \| python hook (exit 0) |
