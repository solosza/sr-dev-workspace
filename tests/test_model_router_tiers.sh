#!/bin/bash
#
# test_model_router_tiers.sh — Live routing-assertion test for the model router (Gate MR-03)
#
# Feeds representative task shapes through the REAL route_model() function in
# lib/model-router.sh (not a re-implementation) and asserts the resolved tier:
#   (a) BUILD / authoring   -> sonnet   (the 247/001 + 257/001 under-tiering class)
#   (b) copy / scaffold     -> haiku    (unambiguous mechanical)
#   (c) architecture / gate -> opus     (hardest tier)
#   (d) unmatched / ambiguous -> sonnet (no silent cheapest routing)
#   (e) copy THEN adapt (multi-match) -> sonnet (higher tier wins)
# Also asserts the resolved model IDs are unchanged (opus-4-8 / sonnet-5 / haiku-4.5).
#
# Portable: absolute paths derived from this script's location, no `cd`.

set -u

# Resolve repo root from this script's location (tests/ lives under repo root).
ROOT="$(dirname "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")")"
ROUTER="$ROOT/lib/model-router.sh"
CONFIG="$ROOT/lib/model-routing-config.json"

# Expected resolved model IDs (must remain unchanged by keyword-tuning work).
EXPECT_OPUS="claude-opus-4-8"
EXPECT_SONNET="claude-sonnet-5"
EXPECT_HAIKU="claude-haiku-4-5-20251001"

fail=0
pass=0

if [ ! -f "$ROUTER" ]; then echo "FAIL: router not found at $ROUTER"; exit 1; fi
if [ ! -f "$CONFIG" ]; then echo "FAIL: config not found at $CONFIG"; exit 1; fi

# Source the REAL router — use its actual route_model function.
# shellcheck disable=SC1090
source "$ROUTER"

# Native Windows Python (used by the router) can't open MSYS-style paths
# (/d/...). Mirror the router's own normalization for our direct config reads.
CONFIG_PY="$CONFIG"
if command -v cygpath &>/dev/null; then
  CONFIG_PY="$(cygpath -m "$CONFIG")"
fi

WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT

# --- Fixtures: representative task shapes -----------------------------------

cat > "$WORK/build.md" <<'EOF'
# Task 001: Build the Employee Report Module
**Type:** BUILD | **Gates:** X-01
## Action
Write the report generator. Implement the aggregation and author the docstrings.
## Acceptance
Module built; output generates correctly.
EOF

cat > "$WORK/copy.md" <<'EOF'
# Task 002: Scaffold the Directory
**Type:** MECHANICAL
## Action
Copy the reference file into place. Scaffold the empty package folders.
## Acceptance
Files copied; folders present.
EOF

cat > "$WORK/opus.md" <<'EOF'
# Task 003: Verify the System Architecture Gate
**Type:** GATE
## Action
Synthesize the multi-file architecture review and verify the exit gate.
## Acceptance
Architecture verified; gate synthesis complete.
EOF

cat > "$WORK/unmatched.md" <<'EOF'
# Task 004: Handle the Widget Flow
**Type:** MISC
## Action
Adjust the gizmo knob until the sprocket settles. Tune the flange.
## Acceptance
Widget behaves; sprocket calm.
EOF

cat > "$WORK/copy_then_adapt.md" <<'EOF'
# Task 005: Copy Then Adapt the Template
**Type:** BUILD
## Action
Copy the reference template, then write the adapted implementation and update the config.
## Acceptance
Template adapted; new module builds.
EOF

# --- Assertion helper -------------------------------------------------------

assert_tier() {
  local name="$1" file="$2" expected="$3"
  local got
  got="$(route_model "$file" "$CONFIG")"
  if [ "$got" = "$expected" ]; then
    echo "PASS: $name -> $got"
    pass=$((pass + 1))
  else
    echo "FAIL: $name -> got '$got', expected '$expected'"
    fail=$((fail + 1))
  fi
}

echo "=== Routing assertions (live, real route_model) ==="
assert_tier "(a) BUILD/authoring"        "$WORK/build.md"          "$EXPECT_SONNET"
assert_tier "(b) copy/scaffold"          "$WORK/copy.md"           "$EXPECT_HAIKU"
assert_tier "(c) architecture/gate/verify" "$WORK/opus.md"         "$EXPECT_OPUS"
assert_tier "(d) unmatched/ambiguous"    "$WORK/unmatched.md"      "$EXPECT_SONNET"
assert_tier "(e) copy-then-adapt (higher wins)" "$WORK/copy_then_adapt.md" "$EXPECT_SONNET"

# --- Model IDs unchanged ----------------------------------------------------

echo "=== Model IDs unchanged ==="
assert_id() {
  local tier="$1" expected="$2" got
  got="$("${PYTHON_CMD:-python}" -c "import json;print(json.load(open('$CONFIG_PY'))['tiers']['$tier']['model_id'])")"
  if [ "$got" = "$expected" ]; then
    echo "PASS: $tier model_id = $got"
    pass=$((pass + 1))
  else
    echo "FAIL: $tier model_id = '$got', expected '$expected'"
    fail=$((fail + 1))
  fi
}
assert_id "opus"   "$EXPECT_OPUS"
assert_id "sonnet" "$EXPECT_SONNET"
assert_id "haiku"  "$EXPECT_HAIKU"

# --- Summary ----------------------------------------------------------------

echo "=== Summary: $pass passed, $fail failed ==="
if [ "$fail" -ne 0 ]; then exit 1; fi
exit 0
