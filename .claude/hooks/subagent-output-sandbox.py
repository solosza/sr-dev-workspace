#!/usr/bin/env python3
"""290 — Subagent output-sandbox (PreToolUse).

Confines a SUBAGENT's Write/Edit to its assigned output directory and blocks writes to
runner-owned state files. Prevents the exact failures seen live this session:
  - an agent writing SKILL.md to the kernel's own .claude/skills/ instead of output/{domain}/
  - an agent writing factory_state.json (runner-owned) and clobbering the completion record.

Prevention-by-hook (unbypassable), not prompt hope. ONLY active for subagent/one-shot sessions
(KERNEL_AGENT_ID set, or KERNEL_SUBAGENT=1) — the interactive session + orchestrator are untouched.
Marked escape hatch: KERNEL_SANDBOX_ALLOW=1 for the rare legitimate cross-dir write.
"""
import json
import os
import sys
import fnmatch


def block(lines):
    sys.stderr.write("\n".join(lines) + "\n")
    sys.exit(2)  # PreToolUse: non-zero (2) blocks the tool call; stderr is shown to the agent


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        sys.exit(0)

    if data.get('tool_name', '') not in ('Write', 'Edit', 'MultiEdit'):
        sys.exit(0)

    fp = (data.get('tool_input', {}).get('file_path') or '').replace('\\', '/')
    if not fp:
        sys.exit(0)

    # Only enforce for subagent (one-shot) sessions. Interactive/orchestrator unaffected.
    if not os.environ.get('KERNEL_AGENT_ID') and os.environ.get('KERNEL_SUBAGENT') != '1':
        sys.exit(0)

    # Marked escape hatch for a legitimate cross-dir write.
    if os.environ.get('KERNEL_SANDBOX_ALLOW') == '1':
        sys.exit(0)

    norm = fp.rstrip('/')
    base = os.path.basename(norm)

    # (a) runner-owned state files: an agent must NEVER write these.
    for pat in ('*_factory_state.json',):
        if fnmatch.fnmatch(base, pat):
            block([
                "BLOCKED (290 output-sandbox): agent write to a runner-owned state file.",
                "  target: " + fp,
                "  factory_state.json is written ONLY by the runner. Produce your deliverable artifact instead.",
                "  (legitimate exception: set KERNEL_SANDBOX_ALLOW=1)",
            ])

    # (b) output confinement: if the runner declared the agent's output root, block writes outside it.
    root = os.environ.get('KERNEL_AGENT_OUTPUT_ROOT')
    if root:
        root = root.replace('\\', '/').rstrip('/')
        try:
            rp = os.path.realpath(fp)
            rr = os.path.realpath(root)
            inside = rp == rr or rp.startswith(rr + os.sep)
        except Exception:
            inside = False
        # also accept a plain string-prefix match (covers not-yet-existing paths / mixed separators)
        if not inside and not norm.startswith(root + '/') and norm != root:
            block([
                "BLOCKED (290 output-sandbox): write outside the agent's assigned output directory.",
                "  target : " + fp,
                "  allowed: " + root + "/  (your assigned output dir)",
                "  Write your deliverable under the allowed dir — this prevents wrong-path writes",
                "  (e.g. SKILL.md landing in the kernel's own .claude/skills/ instead of output/{domain}/).",
                "  (legitimate exception: set KERNEL_SANDBOX_ALLOW=1)",
            ])

    sys.exit(0)


if __name__ == '__main__':
    main()
