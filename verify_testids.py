"""Verify all page data-testids exist in Orderly templates."""
import re
import os
import sys

TEMPLATES_DIR = "D:/my_ai_projects/project_test_repos/hmsa-qa-platform/harness/orderly/templates"
PAGES_DIR = "D:/my_ai_projects/project_test_repos/hmsa-qa-platform/framework/_reference/pages"

template_testids = set()
for fname in os.listdir(TEMPLATES_DIR):
    if fname.endswith(".html"):
        with open(os.path.join(TEMPLATES_DIR, fname)) as f:
            content = f.read()
        for m in re.finditer(r"data-testid=['\"]([^'\"{}]+)['\"]", content):
            template_testids.add(m.group(1))

page_testids = set()
for fname in os.listdir(PAGES_DIR):
    if fname.endswith(".py") and fname != "__init__.py":
        with open(os.path.join(PAGES_DIR, fname)) as f:
            content = f.read()
        for m in re.finditer(r"data-testid='([^']+)'", content):
            val = m.group(1)
            if "{" not in val:
                page_testids.add(val)
        for m in re.finditer(r"data-testid\^='([^']+)'", content):
            page_testids.add(m.group(1) + "*")

print("Template testids:", sorted(template_testids))
print()
print("Page testids:", sorted(page_testids))
print()

missing = set()
for tid in page_testids:
    if tid.endswith("*"):
        prefix = tid[:-1]
        found = any(t.startswith(prefix) for t in template_testids)
        if not found:
            missing.add(tid)
    else:
        if tid not in template_testids:
            missing.add(tid)

if missing:
    print("MISSING from templates:", sorted(missing))
    sys.exit(1)
else:
    print("PAG-03 PASS: All page testids exist in templates")
