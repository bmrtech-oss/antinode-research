"""Check every relative Markdown link and #anchor in the book, and every 'Chapter N' reference.

Run from the repository root:  python 002-from-noise-to-knowing/tools/check_links.py
Exits non-zero if anything is broken.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LINK = re.compile(r"(?<!\!)\[[^\]]*\]\(([^)\s]+)\)")
HEADING = re.compile(r"^#{1,6}\s+(.*?)\s*#*\s*$", re.M)


def slug(h):
    h = re.sub(r"[`*_]", "", h)
    s = re.sub(r"[^\w\s-]", "", h.lower()).strip()
    return re.sub(r"[-\s]+", "-", s)


def anchors(path, cache={}):
    if path not in cache:
        text = path.read_text(encoding="utf-8")
        text = re.sub(r"```.*?```", "", text, flags=re.S)
        seen, out = {}, set()
        for h in HEADING.findall(text):
            s = slug(h)
            n = seen.get(s, 0)
            seen[s] = n + 1
            out.add(s if n == 0 else f"{s}-{n}")
        cache[path] = out
    return cache[path]


def main():
    files = sorted(ROOT.rglob("*.md"))
    chapters = {int(p.name[:2]) for p in ROOT.glob("part-*/[0-9][0-9]-*.md")}
    bad = []
    count = 0
    for f in files:
        text = f.read_text(encoding="utf-8")
        body = re.sub(r"```.*?```", "", text, flags=re.S)
        for target in LINK.findall(body):
            if re.match(r"[a-z]+:", target) or target.startswith("#") and False:
                continue
            count += 1
            path, _, frag = target.partition("#")
            dest = f if not path else (f.parent / path).resolve()
            if not dest.exists():
                bad.append(f"{f.relative_to(ROOT)}: missing file {target}")
            elif frag and dest.suffix == ".md" and frag not in anchors(dest):
                bad.append(f"{f.relative_to(ROOT)}: missing anchor {target}")
        for m in re.finditer(r"\bChapters? (\d+)(?:\s*(?:and|,|–|-)\s*(\d+))?", body):
            for g in m.groups():
                if g and int(g) not in chapters and not (f.name.startswith("98-") and int(g) == 0):
                    bad.append(f"{f.relative_to(ROOT)}: reference to nonexistent chapter {g}")
    print(f"{len(files)} files, {count} links checked, {len(bad)} problems")
    for b in sorted(set(bad)):
        print("  ", b)
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
