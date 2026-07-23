#!/bin/bash
# 291 regression — verify_postcondition: a task_done is only true if the declared
# "## Postcondition" deliverable actually exists + is non-empty.
set -uo pipefail
MAIN="$(cd "$(dirname "$0")/.." && pwd)"
source "$MAIN/lib/common.sh"
validate_deps
PASS=0; FAIL=0
ok(){ echo "  [PASS] $1"; PASS=$((PASS+1)); }
no(){ echo "  [FAIL] $1"; FAIL=$((FAIL+1)); }

T=$(mktemp -d); mkdir -p "$T/tasks" "$T/projects/x" "$T/output/y"

cat > "$T/tasks/001.md" <<'EOF'
# Task 1
## Postcondition
- projects/x/report.md
EOF

echo "=== 1. declared deliverable MISSING -> reject ==="
verify_postcondition "$T/tasks/001.md" "$T" >/dev/null 2>&1 && no "missing accepted" || ok "missing deliverable rejected"

echo "=== 2. deliverable EXISTS + non-empty -> accept ==="
echo content > "$T/projects/x/report.md"
verify_postcondition "$T/tasks/001.md" "$T" >/dev/null 2>&1 && ok "present deliverable accepted" || no "present rejected"

echo "=== 3. deliverable EMPTY -> reject ==="
: > "$T/projects/x/report.md"
verify_postcondition "$T/tasks/001.md" "$T" >/dev/null 2>&1 && no "empty accepted" || ok "empty deliverable rejected"

echo "=== 4. NO ## Postcondition -> pass (backward-compat) ==="
printf '# Task 2\njust a task\n' > "$T/tasks/002.md"
verify_postcondition "$T/tasks/002.md" "$T" >/dev/null 2>&1 && ok "no-postcondition passes" || no "no-postcondition rejected"

echo "=== 5. glob deliverable -> matches any non-empty ==="
echo x > "$T/output/y/a.json"
printf '# Task 3\n## Postcondition\n- output/y/*.json\n' > "$T/tasks/003.md"
verify_postcondition "$T/tasks/003.md" "$T" >/dev/null 2>&1 && ok "glob deliverable matched" || no "glob not matched"

echo "=== 6. syntax + wiring ==="
bash -n "$MAIN/run-task.sh" && ok "run-task.sh bash -n OK" || no "run-task.sh syntax error"
bash -n "$MAIN/lib/common.sh" && ok "common.sh bash -n OK" || no "common.sh syntax error"
[ "$(grep -c 'verify_postcondition "$TASK_FILE_PATH" "$REPO"' "$MAIN/run-task.sh")" -ge 2 ] && ok "postcondition wired on both fresh + resume paths" || no "not wired on both paths"

rm -rf "$T"
echo ""
echo "=== 291 RESULT: $PASS pass / $FAIL fail ==="
[ "$FAIL" -eq 0 ] && { echo "291 POSTCONDITION VERIFIED"; exit 0; } || { echo "291 FAILED"; exit 1; }
