# Test Scanner

## Type
TEST

## Phase Gate
Task 004 must be complete.

## Deliverable
Test verification output confirming scanner works.

## Instructions
1. Verify all deliverables exist:
   - `.claude/skills/reference-scanner/scanner.py` (from 001)
   - `.claude/skills/reference-scanner/state-schema.md` (from 003)
   - `.claude/skills/reference-scanner/SKILL.md` (from 004)
2. Run: `python -c "from pathlib import Path; assert Path('.claude/skills/reference-scanner/scanner.py').exists()"`
3. Run: `python -c "from pathlib import Path; assert Path('.claude/skills/reference-scanner/SKILL.md').exists()"`
4. Verify scanner.py imports and parses without syntax errors:
   `python -c "import ast; ast.parse(open('.claude/skills/reference-scanner/scanner.py').read()); print('OK')"`
5. Verify scanner.py contains required functions:
   `python -c "import ast; t=ast.parse(open('.claude/skills/reference-scanner/scanner.py').read()); fns=[n.name for n in ast.walk(t) if isinstance(n, ast.FunctionDef)]; assert 'scan_index' in fns; assert 'match_payloads_to_steps' in fns; print('Functions OK:', fns)"`

## Verification
- All assertions pass with exit code 0
- scanner.py contains scan_index and match_payloads_to_steps
