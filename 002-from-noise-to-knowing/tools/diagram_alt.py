"""Extract ASCII diagrams and insert plain-language alt text after each one.

  python 002-from-noise-to-knowing/tools/diagram_alt.py extract OUT_DIR   # dump diagrams to JSON batches
  python 002-from-noise-to-knowing/tools/diagram_alt.py apply             # insert text from diagram_alt.json
  python 002-from-noise-to-knowing/tools/diagram_alt.py check             # report diagrams without alt text

Alt text is keyed by file path plus a hash of the diagram text, stored in diagram_alt.json,
and written after the closing fence as an italic line preceded by an HTML comment marker.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ALT = Path(__file__).with_name("diagram_alt.json")
FENCE = re.compile(r"(```[^\n]*\n)(.*?)(```[ \t]*)(\n|$)", re.S)
DIAGRAM = re.compile(r"[┌└┐┘│─╔╚╗╝║→←↑↓▼▲►◄]|\+-{3}|\|\s{2,}\|")
MARK = "<!-- diagram-alt -->"
OLD = re.compile(r"\n\n" + re.escape(MARK) + r"[^\n]*\n\n")


def key(path, text):
    return f"{path.relative_to(ROOT).as_posix()}::{hashlib.sha1(text.strip().encode('utf-8')).hexdigest()[:10]}"


def read(path):
    raw = path.read_text(encoding="utf-8")
    return raw, ("\r\n" if "\r\n" in raw else "\n"), raw.replace("\r\n", "\n")


def diagrams(path):
    _, _, t = read(path)
    t = OLD.sub("\n", t)
    out = []
    for m in FENCE.finditer(t):
        if DIAGRAM.search(m.group(2)):
            heading = re.findall(r"^#{1,6} .*$", t[: m.start()], re.M)
            out.append((key(path, m.group(2)), m.group(2), heading[-1] if heading else ""))
    return out


def files():
    return sorted(p for p in ROOT.rglob("*.md") if "_site" not in p.parts)


def extract(out_dir):
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    batches = {}
    for p in files():
        for k, text, heading in diagrams(p):
            batches.setdefault(p.parent.name, []).append({"id": k, "section": heading, "diagram": text})
    for name, items in batches.items():
        (out_dir / f"{name}.json").write_text(json.dumps(items, ensure_ascii=False, indent=1), encoding="utf-8")
        print(name, len(items))


def apply():
    alts = json.loads(ALT.read_text(encoding="utf-8"))
    missing = 0
    for p in files():
        raw, nl, t = read(p)
        t = OLD.sub("\n", t)

        def repl(m):
            nonlocal missing
            if not DIAGRAM.search(m.group(2)):
                return m.group(0)
            a = alts.get(key(p, m.group(2)))
            if not a:
                missing += 1
                return m.group(0)
            return f"{m.group(1)}{m.group(2)}{m.group(3)}\n\n{MARK}*Diagram description: {a}*\n\n"

        new = FENCE.sub(repl, t)
        if new != t or OLD.search(raw.replace("\r\n", "\n")):
            p.write_text(new.replace("\n", nl), encoding="utf-8", newline="")
    print("diagrams without alt text:", missing)
    return missing


def check():
    alts = json.loads(ALT.read_text(encoding="utf-8")) if ALT.exists() else {}
    total = miss = 0
    for p in files():
        for k, _, _ in diagrams(p):
            total += 1
            miss += k not in alts
    print(f"{total} diagrams, {miss} without alt text")
    sys.exit(1 if miss else 0)


if __name__ == "__main__":
    {"extract": lambda: extract(sys.argv[2]), "apply": apply, "check": check}[sys.argv[1]]()
