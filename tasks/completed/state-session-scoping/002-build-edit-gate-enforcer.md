# 002 — Edit Gate Enforcer: Skip Anchor + Counter Gates for one_shot Agents

## Type
BUILD

## Action
Edit `.claude/hooks/universal-gate-enforcer.py` to skip Gate 3 (anchored check) and Gate 4 (counter check) when `one_shot: true` in session_state.json.

## Change

1. After reading session_state (line ~194), check for one_shot mode:

```python
# One-shot agents (run-task.sh) skip anchor and counter gates
# They execute one task and exit — anchor drift isn't a risk
is_one_shot = session_state.get('one_shot', False)
```

2. Guard Gate 3 (anchored check, ~line 216):

```python
# Gate 3: Anchored? (skip for one-shot agents)
if not is_one_shot:
    domain = session_state.get('domain')
    if domain:
        domain_state = read_state(get_domain_state_file(domain))
        if not domain_state.get('anchored'):
            smart_block(...)
```

3. Guard Gate 4 + counter (check_and_increment_counter call, ~line 247):

```python
# Gate 4 + AUTO-INCREMENT: skip for one-shot agents
if not is_one_shot:
    check_and_increment_counter(session_state, safe_bash)
```

4. Also guard Gate 5 (anchor token) and Gate 6 (protocol hash) with `if not is_one_shot:` — one-shot agents don't anchor, so these don't apply.

## Target File
`.claude/hooks/universal-gate-enforcer.py`

## Acceptance
- [ ] `is_one_shot` variable read from session_state
- [ ] Gate 3 skipped when one_shot is true
- [ ] Counter increment skipped when one_shot is true
- [ ] Gate 5 and Gate 6 skipped when one_shot is true
- [ ] Gate 1 (session_started) and Gate 2 (needs_learn) still enforced for one_shot agents
- [ ] File compiles without errors

## Dependencies
None
