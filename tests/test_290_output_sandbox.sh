#!/bin/bash
# 290 regression — subagent output-sandbox hook. exit 2 = block, exit 0 = allow.
set -uo pipefail
MAIN="$(cd "$(dirname "$0")/.." && pwd)"
HOOK="$MAIN/.claude/hooks/subagent-output-sandbox.py"
PASS=0; FAIL=0
ok(){ echo "  [PASS] $1"; PASS=$((PASS+1)); }
no(){ echo "  [FAIL] $1"; FAIL=$((FAIL+1)); }

W='{"tool_name":"Write","tool_input":{"file_path":"D:/x/kernel/.claude/skills/foo/SKILL.md"}}'
WIN='{"tool_name":"Write","tool_input":{"file_path":"D:/x/output/gdpr/report.md"}}'
FS='{"tool_name":"Write","tool_input":{"file_path":"D:/x/research/gdpr_factory_state.json"}}'
BASH='{"tool_name":"Bash","tool_input":{"command":"echo hi"}}'

echo "=== 1. interactive session (no agent) -> always pass ==="
( unset KERNEL_AGENT_ID KERNEL_SUBAGENT KERNEL_AGENT_OUTPUT_ROOT; printf '%s' "$W" | python "$HOOK" ); rc=$?
[ "$rc" -eq 0 ] && ok "interactive write passes (exit $rc)" || no "interactive blocked, got $rc want 0"

echo "=== 2. subagent write to *_factory_state.json -> BLOCK ==="
( export KERNEL_SUBAGENT=1; unset KERNEL_AGENT_OUTPUT_ROOT KERNEL_SANDBOX_ALLOW; printf '%s' "$FS" | python "$HOOK" ); rc=$?
[ "$rc" -eq 2 ] && ok "factory_state write blocked (exit $rc)" || no "factory_state not blocked, got $rc want 2"

echo "=== 3. subagent write OUTSIDE output root -> BLOCK ==="
( export KERNEL_SUBAGENT=1 KERNEL_AGENT_OUTPUT_ROOT="D:/x/output/gdpr"; unset KERNEL_SANDBOX_ALLOW; printf '%s' "$W" | python "$HOOK" ); rc=$?
[ "$rc" -eq 2 ] && ok "outside-root write blocked (exit $rc)" || no "outside-root not blocked, got $rc want 2"

echo "=== 4. subagent write INSIDE output root -> pass ==="
( export KERNEL_SUBAGENT=1 KERNEL_AGENT_OUTPUT_ROOT="D:/x/output/gdpr"; unset KERNEL_SANDBOX_ALLOW; printf '%s' "$WIN" | python "$HOOK" ); rc=$?
[ "$rc" -eq 0 ] && ok "inside-root write passes (exit $rc)" || no "inside-root blocked, got $rc want 0"

echo "=== 5. escape hatch KERNEL_SANDBOX_ALLOW=1 -> pass ==="
( export KERNEL_SUBAGENT=1 KERNEL_AGENT_OUTPUT_ROOT="D:/x/output/gdpr" KERNEL_SANDBOX_ALLOW=1; printf '%s' "$W" | python "$HOOK" ); rc=$?
[ "$rc" -eq 0 ] && ok "escape hatch passes (exit $rc)" || no "escape hatch blocked, got $rc want 0"

echo "=== 6. non-Write tool -> pass ==="
( export KERNEL_SUBAGENT=1; printf '%s' "$BASH" | python "$HOOK" ); rc=$?
[ "$rc" -eq 0 ] && ok "bash tool passes (exit $rc)" || no "bash blocked, got $rc want 0"

echo "=== 7. wiring: hook registered + runner propagates output root ==="
grep -q 'subagent-output-sandbox.py' "$MAIN/.claude/settings.local.json" && ok "hook registered in settings.local.json" || no "hook NOT registered — it would never fire"
[ "$(grep -c 'KERNEL_AGENT_OUTPUT_ROOT' "$MAIN/run-task.sh")" -ge 2 ] && ok "run-task.sh propagates KERNEL_AGENT_OUTPUT_ROOT" || no "run-task.sh does not propagate output root"
bash -n "$MAIN/run-task.sh" && ok "run-task.sh bash -n OK" || no "run-task.sh syntax error"

echo ""
echo "=== 290 RESULT: $PASS pass / $FAIL fail ==="
[ "$FAIL" -eq 0 ] && { echo "290 SANDBOX VERIFIED"; exit 0; } || { echo "290 FAILED"; exit 1; }
