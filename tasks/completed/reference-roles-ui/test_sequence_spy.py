"""Sequence-spy behavioral proof — L2: real Role code, recording stubs."""

import sys
import importlib.util
from types import ModuleType

FRAMEWORK = "D:/my_ai_projects/project_test_repos/hmsa-qa-platform/framework"
sys.path.insert(0, FRAMEWORK)

from resources.utilities.trace import trace

for pkg in ["_reference", "_reference.tasks", "_reference.roles"]:
    if pkg not in sys.modules:
        p = ModuleType(pkg)
        p.__path__ = []
        sys.modules[pkg] = p

ct_mod = ModuleType("_reference.tasks.common_tasks")
ct_mod.CommonTasks = type("CommonTasks", (), {})
sys.modules["_reference.tasks.common_tasks"] = ct_mod

owt_mod = ModuleType("_reference.tasks.order_workup_tasks")
owt_mod.OrderWorkupTasks = type("OrderWorkupTasks", (), {})
sys.modules["_reference.tasks.order_workup_tasks"] = owt_mod


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


clerk_mod = _load("_reference.roles.order_clerk",
                   f"{FRAMEWORK}/_reference/roles/order_clerk.py")
manager_mod = _load("_reference.roles.order_manager",
                     f"{FRAMEWORK}/_reference/roles/order_manager.py")

OrderClerk = clerk_mod.OrderClerk
OrderManager = manager_mod.OrderManager


class RecordingStub:
    """Records (module, method, args) into a shared journal list."""

    def __init__(self, module_name, journal):
        self._module = module_name
        self._journal = journal

    def __getattr__(self, name):
        if name.startswith("_"):
            raise AttributeError(name)
        mod = self._module
        jrnl = self._journal
        def recorder(*args):
            jrnl.append((mod, name, args))
        return recorder


failures = []


def check(label, actual, expected):
    if actual != expected:
        failures.append(f"{label}: got {actual!r}, expected {expected!r}")
    else:
        print(f"  [PASS] {label}")


print("ROL-05 Sequence-Spy Behavioral Proof — L2")
print("=" * 50)

# --- OrderClerk.work_order_status_change ---
print("\n=== OrderClerk.work_order_status_change ===")
journal = []
stub_common = RecordingStub("common", journal)
stub_workup = RecordingStub("workup", journal)
clerk = OrderClerk(stub_common, stub_workup,
                   {"username": "clerk", "password": "clerk123"})

result = clerk.work_order_status_change("3", "PROCESSING")

check("total calls", len(journal), 3)
if len(journal) >= 1:
    check("call 1: common.login", (journal[0][0], journal[0][1]),
          ("common", "login"))
    check("call 1: identity flows", journal[0][2], ("clerk", "clerk123"))
if len(journal) >= 2:
    check("call 2: workup.open_order", (journal[1][0], journal[1][1]),
          ("workup", "open_order"))
    check("call 2: args", journal[1][2], ("3",))
if len(journal) >= 3:
    check("call 3: workup.change_status", (journal[2][0], journal[2][1]),
          ("workup", "change_status"))
    check("call 3: args", journal[2][2], ("PROCESSING",))
check("returns None", result, None)
check("no extra calls", len(journal), 3)

# --- OrderManager.cancel_order ---
print("\n=== OrderManager.cancel_order ===")
journal2 = []
stub_common2 = RecordingStub("common", journal2)
stub_workup2 = RecordingStub("workup", journal2)
manager = OrderManager(stub_common2, stub_workup2,
                       {"username": "manager", "password": "manager123"})

result2 = manager.cancel_order("3")

check("total calls", len(journal2), 3)
if len(journal2) >= 1:
    check("call 1: common.login", (journal2[0][0], journal2[0][1]),
          ("common", "login"))
    check("call 1: identity flows", journal2[0][2],
          ("manager", "manager123"))
if len(journal2) >= 2:
    check("call 2: workup.open_order", (journal2[1][0], journal2[1][1]),
          ("workup", "open_order"))
    check("call 2: args", journal2[1][2], ("3",))
if len(journal2) >= 3:
    check("call 3: workup.change_status", (journal2[2][0], journal2[2][1]),
          ("workup", "change_status"))
    check("call 3: args", journal2[2][2], ("CANCELLED",))
check("returns None", result2, None)
check("no extra calls", len(journal2), 3)

# --- Summary ---
print("\n" + "=" * 50)
if failures:
    print(f"FAILED — {len(failures)} assertion(s):")
    for f in failures:
        print(f"  ✗ {f}")
    sys.exit(1)
else:
    print("PASSED — all sequence assertions verified")
    sys.exit(0)
