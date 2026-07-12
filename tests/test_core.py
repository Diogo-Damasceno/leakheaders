from header_leak import core

def test_scan_match():
    pat, label = core.PATTERNS[0]
    assert core.scan(pat) == label

def test_scan_nomatch():
    assert core.scan("normal line without pattern") is None

def test_analyze_counts():
    line = core.PATTERNS[0][0]
    c, h = core.analyze([line, line, "ok"])
    assert c[core.PATTERNS[0][1]] == 2
    assert len(h) == 2
