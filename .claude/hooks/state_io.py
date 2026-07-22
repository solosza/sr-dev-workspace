"""Atomic state file writer with schema validation.

Shared module for all kernel hooks. Ensures state files are written
atomically (temp + os.replace) and validated against minimal schemas.
"""

import json
import os
import tempfile

SCHEMAS = {
    "session_state": {
        "required": {
            "session_started": bool,
            "domain": str,
            "timestamp": str,
            "one_shot": bool,
            "actions_log": list,
            "anchor_token_confirmed": bool,
        },
        "min_keys": 4,
    },
    "workflow": {
        "required": {
            "domain": str,
            "anchored": bool,
            "actions_since_anchor": int,
            "setup_complete": bool,
            "completed_tasks": list,
        },
        "min_keys": 4,
    },
}


def validate(obj, schema_key):
    if schema_key not in SCHEMAS:
        raise ValueError(f"Unknown schema: {schema_key}")

    schema = SCHEMAS[schema_key]

    if not isinstance(obj, dict):
        raise ValueError(f"[{schema_key}] Expected dict, got {type(obj).__name__}")

    if len(obj) < schema["min_keys"]:
        raise ValueError(
            f"[{schema_key}] Near-empty payload rejected: "
            f"{len(obj)} keys, minimum {schema['min_keys']}"
        )

    for key, expected_type in schema["required"].items():
        if key not in obj:
            raise ValueError(f"[{schema_key}] Missing required key: {key}")
        if not isinstance(obj[key], expected_type):
            raise ValueError(
                f"[{schema_key}] Key '{key}': expected {expected_type.__name__}, "
                f"got {type(obj[key]).__name__}"
            )


def read_json(path, schema_key=None):
    """Read a state JSON file, tolerating a UTF-8 BOM (utf-8-sig).

    PowerShell 5.1 writes BOM'd UTF-8 by default; strict utf-8 readers
    crash on such files. Write path stays canonical UTF-8 (no BOM).
    """
    with open(path, "r", encoding="utf-8-sig") as f:
        obj = json.load(f)
    if schema_key is not None:
        validate(obj, schema_key)
    return obj


def atomic_write_json(path, obj, schema_key):
    validate(obj, schema_key)

    target = os.path.abspath(path)
    target_dir = os.path.dirname(target)

    fd, tmp_path = tempfile.mkstemp(dir=target_dir, suffix=".tmp", prefix=".state_")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(obj, f, indent=2, ensure_ascii=False)
            f.write("\n")
        os.replace(tmp_path, target)
    except BaseException:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise


if __name__ == "__main__":
    import sys

    print("=== state_io unit-style checks ===")
    errors = []

    # 1. Valid session_state passes
    valid_session = {
        "session_started": True,
        "domain": "test",
        "timestamp": "2026-01-01T00:00:00Z",
        "one_shot": False,
        "actions_log": [],
        "anchor_token_confirmed": False,
        "extra_key": "allowed",
    }
    try:
        validate(valid_session, "session_state")
        print("PASS: valid session_state accepted")
    except Exception as e:
        errors.append(f"FAIL: valid session_state rejected: {e}")
        print(errors[-1])

    # 2. Valid workflow passes
    valid_workflow = {
        "domain": "test",
        "anchored": True,
        "actions_since_anchor": 0,
        "setup_complete": True,
        "completed_tasks": [],
    }
    try:
        validate(valid_workflow, "workflow")
        print("PASS: valid workflow accepted")
    except Exception as e:
        errors.append(f"FAIL: valid workflow rejected: {e}")
        print(errors[-1])

    # 3. Near-empty dict rejected
    try:
        validate({"domain": "x"}, "session_state")
        errors.append("FAIL: near-empty dict was NOT rejected")
        print(errors[-1])
    except ValueError as e:
        if "Near-empty" in str(e):
            print(f"PASS: near-empty dict rejected: {e}")
        else:
            errors.append(f"FAIL: wrong error for near-empty: {e}")
            print(errors[-1])

    # 4. Missing required key rejected
    bad_session = dict(valid_session)
    del bad_session["domain"]
    try:
        validate(bad_session, "session_state")
        errors.append("FAIL: missing 'domain' was NOT rejected")
        print(errors[-1])
    except ValueError as e:
        if "Missing required key" in str(e):
            print(f"PASS: missing key rejected: {e}")
        else:
            errors.append(f"FAIL: wrong error for missing key: {e}")
            print(errors[-1])

    # 5. Wrong type rejected
    bad_type = dict(valid_session)
    bad_type["session_started"] = "yes"
    try:
        validate(bad_type, "session_state")
        errors.append("FAIL: wrong type was NOT rejected")
        print(errors[-1])
    except ValueError as e:
        if "expected bool" in str(e):
            print(f"PASS: wrong type rejected: {e}")
        else:
            errors.append(f"FAIL: wrong error for wrong type: {e}")
            print(errors[-1])

    # 6. Unknown schema rejected
    try:
        validate({}, "bogus")
        errors.append("FAIL: unknown schema was NOT rejected")
        print(errors[-1])
    except ValueError as e:
        if "Unknown schema" in str(e):
            print(f"PASS: unknown schema rejected: {e}")
        else:
            errors.append(f"FAIL: wrong error for unknown schema: {e}")
            print(errors[-1])

    # 7. Atomic write + read-back
    import tempfile as tf

    test_dir = tf.mkdtemp()
    test_path = os.path.join(test_dir, "test_state.json")
    try:
        atomic_write_json(test_path, valid_session, "session_state")
        with open(test_path, "r", encoding="utf-8") as f:
            roundtrip = json.load(f)
        if roundtrip == valid_session:
            print("PASS: atomic write + read-back matches")
        else:
            errors.append("FAIL: roundtrip mismatch")
            print(errors[-1])
    except Exception as e:
        errors.append(f"FAIL: atomic write error: {e}")
        print(errors[-1])
    finally:
        try:
            os.unlink(test_path)
            os.rmdir(test_dir)
        except OSError:
            pass

    # 8. Atomic write rejects invalid payload (no file written)
    test_path2 = os.path.join(test_dir if os.path.isdir(test_dir) else tf.mkdtemp(), "should_not_exist.json")
    try:
        atomic_write_json(test_path2, {"x": 1}, "session_state")
        errors.append("FAIL: invalid payload was written")
        print(errors[-1])
    except ValueError:
        if not os.path.exists(test_path2):
            print("PASS: invalid payload not written to disk")
        else:
            errors.append("FAIL: invalid payload left a file on disk")
            print(errors[-1])

    # 9. BOM'd file read tolerated (utf-8-sig), write stays BOM-free
    bom_dir = tf.mkdtemp()
    bom_path = os.path.join(bom_dir, "bom_state.json")
    try:
        with open(bom_path, "wb") as f:
            f.write(b"\xef\xbb\xbf" + json.dumps(valid_session).encode("utf-8"))
        bom_read = read_json(bom_path, "session_state")
        if bom_read == valid_session:
            print("PASS: BOM'd state file read via utf-8-sig")
        else:
            errors.append("FAIL: BOM'd read mismatch")
            print(errors[-1])
        atomic_write_json(bom_path, bom_read, "session_state")
        with open(bom_path, "rb") as f:
            if f.read(3) != b"\xef\xbb\xbf":
                print("PASS: rewrite is BOM-free canonical UTF-8")
            else:
                errors.append("FAIL: rewrite contains BOM")
                print(errors[-1])
    except Exception as e:
        errors.append(f"FAIL: BOM tolerance check error: {e}")
        print(errors[-1])
    finally:
        try:
            os.unlink(bom_path)
            os.rmdir(bom_dir)
        except OSError:
            pass

    print(f"\n=== {len(errors)} failures ===")
    sys.exit(1 if errors else 0)
