# 002 — Edit Universal Gate Enforcer to Verify Protocol Hash

## Type
BUILD

## Action
Edit `.claude/hooks/universal-gate-enforcer.py` to add a Gate 6 that verifies the protocol hash in session_state.json matches the current protocol file content.

## What to Do

1. Add `import hashlib` to the imports section

2. Add a new function `verify_protocol_hash`:
   ```python
   def verify_protocol_hash(session_state: dict) -> bool:
       """Verify that protocol_hash in state matches actual protocol file content."""
       domain = session_state.get('domain')
       if not domain:
           return True  # No domain = no protocol to verify
       protocol_hash = session_state.get('protocol_hash')
       if not protocol_hash:
           return True  # No hash stored yet = first anchor hasn't run with new code
       protocol_path = _WORKSPACE_ROOT / '.claude' / 'protocols' / f'{domain}-protocol.md'
       if not protocol_path.exists():
           return True  # No protocol file = skip
       actual_hash = hashlib.sha256(protocol_path.read_bytes()).hexdigest()
       return actual_hash == protocol_hash
   ```

3. Add Gate 6 in the `main()` function, after Gate 5 (anchor token check) and before the counter check:
   ```python
   # Gate 6: Protocol hash valid?
   # If protocol changed since last anchor, force re-anchor
   if not verify_protocol_hash(session_state):
       smart_block(
           missing="Protocol file changed since last anchor (hash mismatch)",
           fix_command="/kernel/anchor",
           fix_description="Protocol was modified — re-anchor to re-read and update hash"
       )
   ```

4. Update the docstring at the top of the file to include Gate 6:
   ```
   6. protocol_hash matches current protocol file (if set)
   ```

## Target File
`.claude/hooks/universal-gate-enforcer.py`

## Acceptance
- [ ] `import hashlib` is present
- [ ] `verify_protocol_hash` function exists
- [ ] Gate 6 block exists in main() after Gate 5
- [ ] Docstring updated to list Gate 6

## Dependencies
None
