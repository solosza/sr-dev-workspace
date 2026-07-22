#!/usr/bin/env python3
"""JIT rule injector — advisory PreToolUse hook.
Matches tool calls against jit-rule-map.json, injects snippets via additionalContext.
ADVISORY ONLY: exits 0 on every path.
"""
import json
import sys
import os
import re
from fnmatch import fnmatch
from pathlib import Path
from datetime import datetime, timezone


def main():
    try:
        try:
            data = json.load(sys.stdin)
        except (json.JSONDecodeError, ValueError):
            sys.exit(0)

        tool_name = data.get("tool_name", "")
        tool_input = data.get("tool_input", {})

        hook_dir = Path(__file__).parent
        state_dir = hook_dir.parent / "state"

        rule_map_path = hook_dir / "jit-rule-map.json"
        if not rule_map_path.exists():
            sys.exit(0)

        try:
            rule_map = json.loads(rule_map_path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, ValueError):
            sys.exit(0)

        rules = rule_map.get("rules", [])
        if not rules:
            sys.exit(0)

        last_injection_path = state_dir / "jit-last-injection.json"
        last_rule_ids = _load_last_injection(last_injection_path)

        matched = []
        for rule in rules:
            if not _tool_matches(tool_name, rule.get("tool", "")):
                continue
            if not _trigger_matches(rule.get("trigger", {}), tool_input, state_dir):
                continue
            matched.append(rule)

        if not matched:
            _save_last_injection(last_injection_path, None, state_dir)
            sys.exit(0)

        cat_order = {"safety": 0, "quality": 1, "convention": 2, "architecture": 3}
        matched.sort(key=lambda r: (r.get("priority", 5), cat_order.get(r.get("category", ""), 9)))
        matched = matched[:5]

        current_ids = [r["id"] for r in matched]
        if current_ids == last_rule_ids:
            sys.exit(0)

        context = "\n---\n".join(r["snippet"] for r in matched)

        now = datetime.now(timezone.utc).isoformat()
        state_dir.mkdir(parents=True, exist_ok=True)
        event = {"ts": now, "rule_ids": current_ids, "tool": tool_name}
        with open(state_dir / "jit-injections.jsonl", "a", encoding="utf-8") as f:
            f.write(json.dumps(event) + "\n")

        _save_last_injection(last_injection_path, current_ids, state_dir)

        output = {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "allow",
                "additionalContext": context
            }
        }
        sys.stdout.write(json.dumps(output))
        sys.exit(0)

    except Exception:
        sys.exit(0)


def _load_last_injection(path):
    if not path.exists():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8-sig"))
        return data.get("last_rule_ids")
    except (json.JSONDecodeError, ValueError, OSError):
        return None


def _save_last_injection(path, rule_ids, state_dir):
    try:
        state_dir.mkdir(parents=True, exist_ok=True)
        tmp = str(path) + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump({"last_rule_ids": rule_ids, "ts": datetime.now(timezone.utc).isoformat()}, f)
        os.replace(tmp, path)
    except OSError:
        pass


def _tool_matches(tool_name, tool_pattern):
    if tool_pattern == "*":
        return True
    return tool_name in tool_pattern.split("|")


def _trigger_matches(trigger, tool_input, state_dir):
    t = trigger.get("type", "")

    if t == "always":
        return True

    if t == "session_state":
        cond = trigger.get("condition", "")
        if cond == "file_not_read_this_session":
            fp = tool_input.get("file_path", "")
            return bool(fp) and not _file_was_read(fp, state_dir)
        return False

    if t == "path_glob":
        pat = trigger.get("pattern", "")
        fp = tool_input.get("file_path", "")
        if not fp or not pat:
            return False
        norm = fp.replace("\\", "/")
        return fnmatch(norm, pat) or fnmatch(norm.rsplit("/", 1)[-1], pat)

    if t == "content_match":
        pat = trigger.get("pattern", "")
        content = tool_input.get("content", "") or tool_input.get("new_string", "")
        if not content or not pat:
            return False
        return bool(re.search(pat, content, re.IGNORECASE))

    if t == "command_match":
        pat = trigger.get("pattern", "")
        cmd = tool_input.get("command", "")
        if not cmd or not pat:
            return False
        return bool(re.search(pat, cmd))

    return False


def _file_was_read(file_path, state_dir):
    norm = os.path.normpath(file_path).replace("\\", "/").lower()
    log_files = [state_dir / "actions.jsonl"]
    for p in state_dir.glob("agent-*-actions.jsonl"):
        log_files.append(p)
    for log_path in log_files:
        if not log_path.exists():
            continue
        try:
            with open(log_path, "r", encoding="utf-8-sig") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                        if entry.get("tool") == "Read":
                            ep = entry.get("entry", "").replace("\\", "/").lower()
                            if norm in ep or ep in norm:
                                return True
                    except (json.JSONDecodeError, ValueError):
                        continue
        except (OSError, IOError):
            continue
    return False


if __name__ == "__main__":
    main()
