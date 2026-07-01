#!/usr/bin/env python3
"""AI writing tell detector. Scans text for patterns common in AI-generated prose."""

import json
import re
import sys


# --- Detection categories ---

EM_DASH = re.compile(r"\u2014")

HEDGE_WORDS = re.compile(
    r"\b(?:"
    r"arguably|notably|it'?s worth noting|it'?s important to|in conclusion|"
    r"overall|essentially|fundamentally|leveraging|utilizing|facilitate|"
    r"comprehensive|robust|cutting-edge|innovative|game-changing|"
    r"transformative|seamless|streamlined|holistic"
    r")\b",
    re.IGNORECASE,
)

FORMULAIC_STARTERS = re.compile(
    r"(?:^|\.\s+)(?:"
    r"In today'?s|When it comes to|It goes without saying|At the end of the day"
    r")",
    re.IGNORECASE,
)

AI_VERBS = re.compile(
    r"\b(?:delve|dive into|deep dive|unpack|unlock)\b",
    re.IGNORECASE,
)

EXCLAMATION = re.compile(r"!")

EMOJI = re.compile(
    r"[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF"
    r"\U0001F1E0-\U0001F1FF\U00002702-\U000027B0\U0001F900-\U0001F9FF"
    r"\U0001FA00-\U0001FA6F\U0001FA70-\U0001FAFF\U00002600-\U000026FF]"
)

TRIPLE_ADJECTIVE = re.compile(
    r"\b(\w+),\s+(\w+),\s+and\s+(\w+)\b",
    re.IGNORECASE,
)

COLON_LIST = re.compile(
    r":\s*(?:first|1\))[^.]*(?:second|2\))[^.]*(?:third|3\))",
    re.IGNORECASE,
)

# Passive voice: be-verb + past participle (approximation)
BE_VERB = r"(?:is|are|was|were|be|been|being)"
PAST_PARTICIPLE = r"(?:\w+ed|\w+en|\w+t)"
PASSIVE = re.compile(
    rf"\b{BE_VERB}\s+{PAST_PARTICIPLE}\b",
    re.IGNORECASE,
)

PARALLEL_STRUCTURE = re.compile(
    r"(?:^|\.\s+)(\w+ing\b.*?,\s+\w+ing\b.*?,\s+(?:and\s+)?\w+ing\b)",
    re.IGNORECASE,
)

# Sentence splitter (rough)
SENTENCE_SPLIT = re.compile(r"[.!?]+\s+")


SUGGESTIONS = {
    "em_dash": "Replace em dash with comma, semicolon, or period",
    "hedge_word": "Remove filler word or rephrase directly",
    "formulaic_starter": "Rewrite opening with specific detail",
    "ai_verb": "Use a concrete verb instead",
    "exclamation": "Remove exclamation mark in professional prose",
    "emoji": "Remove emoji from professional document",
    "triple_adjective": "Pick the one adjective that matters most",
    "colon_list": "Restructure as paragraph or use varied transitions",
    "passive_voice_high": "Rewrite in active voice where possible",
    "parallel_structure": "Vary sentence structure",
}


def detect(text: str) -> list[dict]:
    """Run all detectors on text. Returns list of findings."""
    findings = []
    lines = text.splitlines()

    for line_num, line in enumerate(lines, start=1):
        # Em dashes
        for m in EM_DASH.finditer(line):
            findings.append({
                "line_number": line_num,
                "text": line.strip(),
                "category": "em_dash",
                "suggestion": SUGGESTIONS["em_dash"],
            })

        # Hedge words
        for m in HEDGE_WORDS.finditer(line):
            findings.append({
                "line_number": line_num,
                "text": m.group(),
                "category": "hedge_word",
                "suggestion": SUGGESTIONS["hedge_word"],
            })

        # Formulaic starters
        for m in FORMULAIC_STARTERS.finditer(line):
            findings.append({
                "line_number": line_num,
                "text": m.group().strip(". "),
                "category": "formulaic_starter",
                "suggestion": SUGGESTIONS["formulaic_starter"],
            })

        # AI verbs
        for m in AI_VERBS.finditer(line):
            findings.append({
                "line_number": line_num,
                "text": m.group(),
                "category": "ai_verb",
                "suggestion": SUGGESTIONS["ai_verb"],
            })

        # Exclamation marks
        for m in EXCLAMATION.finditer(line):
            findings.append({
                "line_number": line_num,
                "text": line.strip(),
                "category": "exclamation",
                "suggestion": SUGGESTIONS["exclamation"],
            })

        # Emoji
        for m in EMOJI.finditer(line):
            findings.append({
                "line_number": line_num,
                "text": m.group(),
                "category": "emoji",
                "suggestion": SUGGESTIONS["emoji"],
            })

        # Triple adjective stacking
        for m in TRIPLE_ADJECTIVE.finditer(line):
            findings.append({
                "line_number": line_num,
                "text": m.group(),
                "category": "triple_adjective",
                "suggestion": SUGGESTIONS["triple_adjective"],
            })

        # Colon-list patterns
        for m in COLON_LIST.finditer(line):
            findings.append({
                "line_number": line_num,
                "text": m.group(),
                "category": "colon_list",
                "suggestion": SUGGESTIONS["colon_list"],
            })

        # Parallel structure
        for m in PARALLEL_STRUCTURE.finditer(line):
            findings.append({
                "line_number": line_num,
                "text": m.group(),
                "category": "parallel_structure",
                "suggestion": SUGGESTIONS["parallel_structure"],
            })

    # Passive voice (document-level: flag if >20% of sentences)
    full_text = " ".join(lines)
    sentences = [s.strip() for s in SENTENCE_SPLIT.split(full_text) if s.strip()]
    if sentences:
        passive_count = sum(1 for s in sentences if PASSIVE.search(s))
        ratio = passive_count / len(sentences)
        if ratio > 0.20:
            findings.append({
                "line_number": 0,
                "text": f"{passive_count}/{len(sentences)} sentences ({ratio:.0%}) use passive voice",
                "category": "passive_voice_high",
                "suggestion": SUGGESTIONS["passive_voice_high"],
            })

    return findings


def main():
    if len(sys.argv) < 2:
        print("Usage: python detect.py <file-path>", file=sys.stderr)
        sys.exit(2)

    file_path = sys.argv[1]
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    findings = detect(text)

    report = {
        "file": file_path,
        "total_findings": len(findings),
        "findings": findings,
    }

    print(json.dumps(report, indent=2))
    sys.exit(1 if findings else 0)


if __name__ == "__main__":
    main()
