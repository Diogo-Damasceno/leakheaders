"""Detector de ataques em logs por padroes (blue team)."""
from __future__ import annotations
import re
from collections import Counter

PATTERNS = [('Server:', 'server-leak'), ('X-Powered-By', 'poweredby-leak')]

def scan(line: str) -> str | None:
    for pat, label in PATTERNS:
        if re.search(pat, line):
            return label
    return None

def analyze(lines):
    counts = Counter()
    hits = []
    for ln in lines:
        hit = scan(ln)
        if hit:
            counts[hit] += 1
            hits.append((hit, ln))
    return counts, hits

def main(argv=None):
    import sys
    argv = argv if argv is not None else sys.argv[1:]
    data = sys.stdin.read() if not argv else open(argv[0]).read()
    counts, _ = analyze(data.splitlines())
    for k, v in counts.items():
        print(f"{k}: {v}")
    return 0
