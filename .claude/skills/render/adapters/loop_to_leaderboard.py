"""loop_to_leaderboard.py — Adapter: a venture loop's decide/output -> leaderboard items.json.

The glue that used to be done by hand. Takes whatever a loop emits (a list of items /
wedges, each with a name, a plain description, a recommendation, a fit level, and a merit
or rank signal) and returns the exact data model that templates/leaderboard/generate.py
consumes.

Baked-in rules (callers never re-apply them):
  - Plain vocabulary: internal jargon is translated/stripped from every shown string.
  - Rank on MERIT only. Fit never changes the order — it is a displayed tag.
  - No em dashes in any produced string.

Public: to_items(loop_output, title, lead) -> dict
"""
import re

# recommendation label -> (display label, tone).  tone: c=green b=amber e=red
_REC = {
    "build": ("Build", "c"),
    "test first": ("Test first", "b"),
    "test-first": ("Test first", "b"),
    "testfirst": ("Test first", "b"),
    "test": ("Test first", "b"),
    "go-if": ("Test first", "b"),
    "go if": ("Test first", "b"),
    "dont build": ("Don't build", "e"),
    "don't build": ("Don't build", "e"),
    "do not build": ("Don't build", "e"),
    "kill": ("Don't build", "e"),
    "skip": ("Don't build", "e"),
}

# fit level -> (display tag, tone).  tone: a=blue(new) b=amber(partly) c=green(strength)
_FIT = {
    "high": ("Your strength", "c"),
    "your strength": ("Your strength", "c"),
    "strength": ("Your strength", "c"),
    "partly": ("Partly yours", "b"),
    "partly yours": ("Partly yours", "b"),
    "cond": ("Partly yours", "b"),
    "conditional": ("Partly yours", "b"),
    "medium": ("Partly yours", "b"),
    "low": ("New for you", "a"),
    "new": ("New for you", "a"),
    "new for you": ("New for you", "a"),
    "none": ("New for you", "a"),
}

# jargon -> plain english. applied case-insensitively to every shown string.
_PLAIN = [
    (r"payer[- ]swap", "sell to a different buyer"),
    (r"\bwedges?\b", "ideas"),
    (r"\bassay\b", "check"),
    (r"\bgo[- ]if\b", "worth a test"),
    (r"\bkill(ed)?\b", "skip"),
    (r"\bhunters?\b", "finders"),
    (r"\btranspose\b", "move to another market"),
    (r"\bmerit\b", "opportunity strength"),
    (r"\bfit[- ]to[- ]me\b", "how close to your world"),
]


def _slug(name):
    s = re.sub(r"[^a-z0-9]+", "-", str(name).lower()).strip("-")
    return s or "item"


def _plain(text):
    """Translate jargon out and remove em dashes from a shown string."""
    s = str(text)
    for pat, repl in _PLAIN:
        s = re.sub(pat, repl, s, flags=re.IGNORECASE)
    # no em dashes: em dash, en dash, and the ' -- ' surrogate all become a comma or space
    s = s.replace("—", ", ").replace("–", "-").replace(" -- ", ", ")
    return re.sub(r"\s+", " ", s).strip()


def _norm_rec(value):
    key = str(value or "").strip().lower()
    return _REC.get(key, ("Test first", "b"))


def _norm_fit(value):
    key = str(value or "").strip().lower()
    return _FIT.get(key, ("New for you", "a"))


def _merit(item, fallback):
    """Higher = better. Accept merit/score/rank_signal; fall back to input order."""
    for k in ("merit", "score", "rank_signal", "strength"):
        if k in item and item[k] is not None:
            try:
                return float(item[k])
            except (TypeError, ValueError):
                pass
    return fallback


def to_items(loop_output, title, lead):
    """Convert a loop output dict into the leaderboard items.json data model.

    loop_output: {"items": [ {name, desc/description, rec/recommendation, fit, merit?} ]}
                 (a bare list is also accepted)
    Returns: {title, lead, recLegend, legend, items:[...]} — rank on merit, fit as a tag.
    """
    raw = loop_output.get("items", loop_output) if isinstance(loop_output, dict) else loop_output
    raw = list(raw or [])

    # rank on merit only (fit is ignored for ordering). Stable: higher merit first,
    # ties keep input order (negative index as tiebreak).
    scored = []
    for i, it in enumerate(raw):
        it = it or {}
        scored.append((_merit(it, len(raw) - i), -i, it))
    scored.sort(key=lambda t: (t[0], t[1]), reverse=True)

    items = []
    for rank, (_, _, it) in enumerate(scored, start=1):
        name = _plain(it.get("name", it.get("title", "")))
        desc = _plain(it.get("desc", it.get("description", "")))
        rec_label, rec_tone = _norm_rec(it.get("rec", it.get("recommendation")))
        tag_label, tag_tone = _norm_fit(it.get("fit", it.get("tag")))
        items.append({
            "id": it.get("id") or _slug(name),
            "rank": str(rank),
            "name": name,
            "desc": desc,
            "rec": {"label": rec_label, "tone": rec_tone},
            "tag": {"label": tag_label, "tone": tag_tone},
        })

    return {
        "title": _plain(title),
        "lead": _plain(lead),
        "recLegend": [
            {"label": "Build", "tone": "c"},
            {"label": "Test first", "tone": "b"},
            {"label": "Don't build", "tone": "e"},
        ],
        "legend": {
            "label": "How close to your world:",
            "tags": [
                {"label": "New for you", "tone": "a"},
                {"label": "Partly yours", "tone": "b"},
                {"label": "Your strength", "tone": "c"},
            ],
        },
        "items": items,
    }
