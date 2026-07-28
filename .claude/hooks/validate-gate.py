"""IOM gate hook — the ONE generic hard gate for verdict registers.

Given a verdict register, this checks it against the universal register schema + the scope contract
the register DECLARES. Structural and consistency checks only; semantic judgment stays with the LLM
(the soft gate). It is generic across every scope because it reads the contract as data, never
hardcodes one. Add contracts to the library; this hook gates them all, unchanged.

  python validate-gate.py <register.json>      exit 0 = conforms, 1 = blocked

No external dependencies (no jsonschema): the register shape is small and fixed, so the checks are
inline. Paths in the register are repo-relative and resolve from this hook's location.
"""
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]        # .claude/hooks/ -> .claude/ -> repo root
VERDICTS = {"confirmed", "refuted", "unresolved", "unsupported", "not-applicable"}
NEED_EVIDENCE = {"confirmed", "refuted", "unsupported"}   # a checked verdict must show its work
MUST_FLAG = {"refuted", "unresolved", "unsupported"}      # findings must be flagged


def _load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def gate(register_path):
    """Return a list of blocking findings (empty = the register conforms)."""
    reg = _load(register_path)
    f = []

    for key in ("artifact", "scope", "contract", "units", "gate"):
        if key not in reg:
            f.append(f"register missing required field '{key}'")
    if f:
        return f                                        # can't check further without the shape

    # Per-unit structural rules (the universal "show your work" + "flag findings").
    for u in reg["units"]:
        uid = u.get("id", "?")
        v = u.get("verdict")
        if v not in VERDICTS:
            f.append(f"unit {uid}: verdict '{v}' not one of {sorted(VERDICTS)}")
        if v in NEED_EVIDENCE and not (u.get("authority") and u.get("evidence")):
            f.append(f"unit {uid}: verdict '{v}' requires authority + evidence")
        if v in MUST_FLAG and not u.get("flagged"):
            f.append(f"unit {uid}: verdict '{v}' must be flagged")

    # Per-scope hard rules the hook can mechanically re-check from the contract (the tag vocabulary).
    contract_path = REPO_ROOT / reg["contract"]
    if contract_path.exists():
        contract = _load(contract_path)
        vocab = (contract.get("unit") or {}).get("tag_vocabulary")
        tag_is_hard = any(r.get("id") == "tagged" and r.get("gate") == "hard"
                          for r in contract.get("rules", []))
        if vocab and tag_is_hard:
            for u in reg["units"]:
                if u.get("tag") and u["tag"] not in vocab:
                    f.append(f"unit {u.get('id','?')}: tag '{u['tag']}' not in {reg['scope']} vocabulary")
    else:
        f.append(f"declared contract not found: {reg['contract']}")

    # Gate-consistency: the reported verdict must match the flagged units.
    flagged = sum(1 for u in reg["units"] if u.get("flagged"))
    g = reg.get("gate", {})
    if g.get("findings") != flagged:
        f.append(f"gate.findings {g.get('findings')} != actual flagged count {flagged}")
    if (g.get("verdict") == "pass") != (flagged == 0):
        f.append(f"gate.verdict '{g.get('verdict')}' inconsistent with {flagged} flagged unit(s)")

    return f


def main(register_path):
    findings = gate(register_path)
    if findings:
        sys.stderr.write("GATE BLOCK: register does not conform to its contract\n")
        for finding in findings:
            sys.stderr.write(f"  - {finding}\n")
        return 1
    sys.stdout.write(f"GATE PASS: {register_path} conforms to its contract\n")
    return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.stderr.write("usage: python validate-gate.py <register.json>\n")
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
