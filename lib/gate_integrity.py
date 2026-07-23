"""Gate-integrity helpers for the Isagawa Kernel runner (backlog 273).

Composes with 276's completion-truth oracle (observability.py) — that module
detects claimed-vs-evidence divergence across a batch's completed_tasks;
this module classifies a SINGLE gate/L3 task's own evidence artifact as
live/simulated/empty, so a simulated or empty gate is a structurally
detectable DEFECT (reaffirms lessons #39 the-orchestrator-re-runs-every-gate
and #49 0-byte-log-gate-skip) rather than a self-reported pass.
"""

import pathlib
import re

from observability import _artifact_evidence

_SIMULATION_MARKERS = (
    'would run', 'would execute', 'would have run', 'as if it ran',
    'as if executed', 'simulate', 'simulated', 'simulation',
    'hypothetical', 'hypothetically', 'pretend', 'mock run',
    'not actually run', 'not actually executed', 'never ran',
    'never executed',
)


def _looks_simulated(text):
    lowered = text.lower()
    return any(marker in lowered for marker in _SIMULATION_MARKERS)


def classify_gate_evidence(log_path, artifact_paths=None):
    """Classify a GATE/L3 task's evidence as 'live', 'simulated', or 'empty'.

    log_path: path to the task's iteration/evidence log — the recorded
        command + captured output the task offers as its pass proof.
    artifact_paths: optional additional artifact path(s) (file/dir) that
        would corroborate live execution independent of the log text.

    Order matters: a simulation narrative in the log wins even if some
    artifact happens to exist (the 247 L3 shape — a simulated dependent
    swarm run, not a live one). Only once no simulation language is found
    does an empty log + no artifact fall through to 'empty' (the 208
    UT-04 0-byte-log shape). Everything else with real non-empty content
    is 'live'.
    """
    log = pathlib.Path(log_path)
    text = log.read_text(encoding='utf-8', errors='replace') if log.is_file() else ''

    if _looks_simulated(text):
        return 'simulated'

    has_artifact = _artifact_evidence(artifact_paths) if artifact_paths else False
    if not text.strip() and not has_artifact:
        return 'empty'

    return 'live'


def is_defect(verdict):
    """A gate's evidence is a DEFECT finding unless the verdict is 'live'."""
    return verdict != 'live'


_DB_URL_RE = re.compile(r'DATABASE_URL\s*[=:]\s*["\']?([^"\'\s]+)')
_ENV_DRIVEN_RE = re.compile(r'os\.environ|os\.getenv|\$\{|%[A-Z_]+%|\$[A-Z_]+\b')
_SQLITE_PATH_RE = re.compile(r'sqlite(?:\+\w+)?:///+(.*)$')
_ABSOLUTE_PATH_RE = re.compile(r'^([A-Za-z]:[\\/]|/)')
_IMPORT_RE = re.compile(r'^\s*(import|from)\s+\S', re.MULTILINE)


def lint_fixture_portability(file_path):
    """Scan a test task/fixture file for portability violations (lesson #47).

    Flags (1) a DATABASE_URL whose value is a relative/cwd-dependent sqlite
    path rather than absolute or env-driven (the 222 relative-URL class),
    and (2) a file that imports package roots but never declares an
    explicit PYTHONPATH (the 213 collection-failure class). Read-only —
    reports violations, never modifies the file. 223's already-portable
    pattern (absolute DATABASE_URL, explicit PYTHONPATH) is the PASS
    standard and produces no violations.

    Returns a list of {file, line, kind, message} violation dicts — empty
    means the fixture is portable.
    """
    path = pathlib.Path(file_path)
    text = path.read_text(encoding='utf-8', errors='replace') if path.is_file() else ''
    violations = []

    for lineno, line in enumerate(text.splitlines(), start=1):
        match = _DB_URL_RE.search(line)
        if not match or _ENV_DRIVEN_RE.search(line):
            continue
        value = match.group(1)
        sqlite_match = _SQLITE_PATH_RE.search(value)
        if sqlite_match and not _ABSOLUTE_PATH_RE.match(sqlite_match.group(1)):
            violations.append({
                'file': str(path), 'line': lineno, 'kind': 'relative_database_url',
                'message': (f'DATABASE_URL uses a relative/cwd-dependent path: '
                            f'{value!r} (lesson #47 — use absolute or env-driven)'),
            })

    if _IMPORT_RE.search(text) and 'pythonpath' not in text.lower():
        violations.append({
            'file': str(path), 'line': None, 'kind': 'missing_pythonpath',
            'message': ('Test imports package roots but declares no explicit '
                        'PYTHONPATH (lesson #47 / 213 collection-failure class)'),
        })

    return violations


def is_portable(file_path):
    """True if lint_fixture_portability finds zero violations."""
    return not lint_fixture_portability(file_path)


_STYLE_BLOCK_RE = re.compile(r'<style\b[^>]*>.*?</style>', re.IGNORECASE | re.DOTALL)
_SCRIPT_BLOCK_RE = re.compile(r'<script\b[^>]*>.*?</script>', re.IGNORECASE | re.DOTALL)
_INLINE_STYLE_ATTR_RE = re.compile(r'\sstyle\s*=\s*(".*?"|\'.*?\')', re.IGNORECASE | re.DOTALL)


def strip_markup_then_grep(html_or_source, pattern, context_chars=60):
    """Strip <style>/<script> blocks + inline style="..." attributes, THEN
    grep, THEN return matches with surrounding context for human/automated
    adjudication.

    Eliminates the CSS `max-width:100%` false-positive class (pipelines
    255/256/258) that fired when an absolute-claims grep matched raw HTML
    source without stripping markup first — the fix is structural (strip
    markup before matching), not a smarter regex. `pattern` is a regex
    string (matched case-insensitively) or a pre-compiled pattern. All
    HTML/source semantics gates should call this instead of a raw grep.

    Returns a list of {match, start, end, context} dicts; offsets are
    relative to the STRIPPED text, not the original input.
    """
    stripped = _STYLE_BLOCK_RE.sub(' ', html_or_source)
    stripped = _SCRIPT_BLOCK_RE.sub(' ', stripped)
    stripped = _INLINE_STYLE_ATTR_RE.sub(' ', stripped)

    compiled = pattern if hasattr(pattern, 'search') else re.compile(pattern, re.IGNORECASE)

    matches = []
    for m in compiled.finditer(stripped):
        start = max(0, m.start() - context_chars)
        end = min(len(stripped), m.end() + context_chars)
        matches.append({
            'match': m.group(0),
            'start': m.start(),
            'end': m.end(),
            'context': stripped[start:end].strip(),
        })
    return matches


_ABSOLUTE_CLAIMS_RE = re.compile(
    r'100%\s*(accurate|guaranteed|correct|safe|reliable)|guaranteed|unbypassable|zero[\s-]?drift',
    re.IGNORECASE,
)


def check_absolute_claims(html_or_source):
    """Retrofit of the portfolio absolute-claims gate onto strip_markup_then_grep.

    Flags checklist-banned absolute claims (100%/guaranteed/unbypassable/zero
    drift) in real body content while ignoring CSS declarations like
    `max-width:100%` that live inside <style> blocks or style="..." attrs.
    """
    return strip_markup_then_grep(html_or_source, _ABSOLUTE_CLAIMS_RE)


def _main():
    import argparse
    import json

    parser = argparse.ArgumentParser(description='Gate-integrity helpers (backlog 273)')
    sub = parser.add_subparsers(dest='cmd', required=True)

    classify = sub.add_parser('classify', help='GI-01 gate-evidence classifier')
    classify.add_argument('--log', required=True, help='path to the gate task evidence log')
    classify.add_argument('--artifacts', nargs='*', default=[], help='additional artifact path(s)')

    lint = sub.add_parser('lint', help='GI-02 fixture-portability linter')
    lint.add_argument('--fixture', required=True, help='path to the test task/fixture file')

    claims = sub.add_parser('absolute-claims', help='GI-03 portfolio absolute-claims gate')
    claims.add_argument('--file', required=True, help='path to the HTML/source file to check')

    args = parser.parse_args()

    if args.cmd == 'classify':
        verdict = classify_gate_evidence(args.log, artifact_paths=args.artifacts)
        result = {'log': args.log, 'verdict': verdict, 'defect': is_defect(verdict)}
        print(json.dumps(result, indent=2))
        if result['defect']:
            raise SystemExit(1)
    elif args.cmd == 'lint':
        violations = lint_fixture_portability(args.fixture)
        print(json.dumps({'fixture': args.fixture, 'violations': violations}, indent=2))
        if violations:
            raise SystemExit(1)
    elif args.cmd == 'absolute-claims':
        source = pathlib.Path(args.file).read_text(encoding='utf-8', errors='replace')
        matches = check_absolute_claims(source)
        print(json.dumps({'file': args.file, 'matches': matches}, indent=2))
        if matches:
            raise SystemExit(1)


if __name__ == '__main__':
    _main()
