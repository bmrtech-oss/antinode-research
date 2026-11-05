"""Generate Appendix F (Index) from the glossary, the named formulations, and names and topics found in the text.

Run from the repository root:  python 002-from-noise-to-knowing/tools/build_index.py
Glossary terms point to their Appendix A definition and to the chapters named in the glossary's "See:" line.
Formulations, people and topics point to every chapter whose text contains them.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GLOSSARY = ROOT / "back-matter/98-appendix-a-glossary.md"
OUT = ROOT / "back-matter/98-appendix-f-index.md"

FORMULATIONS = [
    ("Recall is not selection", r"recall is not selection"),
    ("The test that cannot fail is a mirror", r"test that cannot fail|cannot fail is a mirror"),
    ("The fallacy in technical clothing", r"technical clothing"),
    ("Strip the clothing", r"strip the clothing|strip(ping)? (away )?the clothing"),
    ("The courage tax", r"courage tax"),
    ("Scaffold debt", r"scaffold debt"),
    ("The unscaffolded test", r"unscaffolded test"),
    ("Extension vs. substitution", r"extension (vs\.?|versus|or) substitution|extension from substitution|extends? .{0,40}or substitut"),
    ("Confident gap-filling", r"confident gap-filling"),
    ("The junior colleague metaphor", r"junior colleague"),
    ("The trust calibration matrix", r"trust calibration matrix"),
    ("Temporal leakage", r"temporal leakage"),
    ("The validation gap", r"validation gap"),
    ("The three temptations", r"three temptations"),
    ("The compression insight", r"compression insight"),
    ("Commensurable vs. incommensurable values", r"incommensurable"),
    ("The confidence–stakes calibration", r"confidence.{1,3}stakes calibration"),
    ("The wasted-day insight", r"wasted-day insight|wasted day"),
    ("The seven-stage pipeline", r"seven-stage|seven stages"),
]

PEOPLE_AND_TOPICS = [
    "Kahneman", "Tversky", "Polanyi", "Popper", "Ericsson", "Klein", "Clark", "Chalmers",
    "Shannon", "Herbert Simon", "Vannevar Bush", "Luhmann", "Feynman", "Ebbinghaus", "Bayes", "Gettier",
    "Plato", "Aristotle", "Socrates", "Descartes", "Hume", "Kant", "Newton", "Einstein", "Darwin",
    "Dunning", "Tetlock", "Goodhart", "Friston", "Kuhn", "Baddeley", "Cowan", "Tononi",
    "Hickey", "Hayek", "Turing", "Wittgenstein", "Peirce", "Locke", "Hegel", "Nietzsche", "Pascal",
    "Gigerenzer", "Taleb", "Tolstoy", "Dewey", "Merton", "Hofstadter",
    "Memex", "Dunning–Kruger", "Dunning-Kruger", "Occam", "Gladwell",
    "Large language model", "Retrieval-augmented generation", "Embedding", "Hallucination",
     "Context window", "Chunking", "Overfitting", "Cross-validation", "Correlation",
    "Causation", "Randomized", "Confidence interval", "Calibration", "Paradigm",
    "Serendipity", "Scientific method", "Peer review", "Wikipedia", 
    "Postmortem", "Code review", "Benchmark", 
    "Sleep", "Dopamine", "Hippocampus", "Prefrontal", "Neuron", "Synapse",
    "Dark matter", "Photograph", "Telescope", "Microscope",
]


def slug(name):
    s = re.sub(r"[^\w\s-]", "", name.lower()).strip()
    return re.sub(r"[-\s]+", "-", s)


def chapters():
    return {int(p.name[:2]): p for p in sorted(ROOT.glob("part-*/[0-9][0-9]-*.md"))}


def link(n, ch):
    return f"[{n}](../{ch[n].relative_to(ROOT).as_posix()})"


def body(p):
    t = p.read_text(encoding="utf-8")
    t = re.sub(r"<!-- chapter-meta:start -->.*?<!-- chapter-meta:end -->", "", t, flags=re.S)
    t = re.sub(r"<!-- book-nav:start -->.*?<!-- book-nav:end -->", "", t, flags=re.S)
    return t


def found_in(pattern, texts):
    rx = re.compile(pattern, re.I)
    return [n for n, t in texts.items() if rx.search(t)]


def glossary_entries():
    text = GLOSSARY.read_text(encoding="utf-8").replace("\r\n", "\n")
    out = []
    for block in re.split(r"\n### ", text)[1:]:
        name = block.split("\n", 1)[0].strip()
        see = re.search(r"\*\*See:\*\*\s*(.*)", block)
        nums = sorted({int(n) for n in re.findall(r"Chapters? (\d+)", see.group(1))}) if see else []
        extra = sorted({int(n) for m in re.findall(r"Chapters? ([\d, and]+)", see.group(1)) for n in re.findall(r"\d+", m)}) if see else []
        out.append((name, sorted(set(nums) | set(extra))))
    return out


def main():
    ch = chapters()
    texts = {n: body(p) for n, p in ch.items()}
    entries = {}

    for name, nums in glossary_entries():
        refs = ", ".join(link(n, ch) for n in nums if n in ch)
        gl = f"[definition](98-appendix-a-glossary.md#{slug(name)})"
        entries[name] = f"{gl}" + (f" · Ch {refs}" if refs else "")

    for name, pat in FORMULATIONS:
        nums = found_in(pat, texts)
        if nums and name not in entries:
            entries[name] = "Ch " + ", ".join(link(n, ch) for n in nums)

    for name in PEOPLE_AND_TOPICS:
        if name in entries:
            continue
        nums = found_in(r"\b" + re.escape(name), texts)
        if nums:
            entries[name] = "Ch " + ", ".join(link(n, ch) for n in nums[:8])

    lines = [
        "# Appendix F: Index",
        "",
        "Glossary terms link to their definition in [Appendix A](98-appendix-a-glossary.md) and to the chapters "
        "where the glossary introduces them. The book's named formulations, the people it draws on, and recurring "
        "topics link to the chapters where they appear.",
        "",
        f"*{len(entries)} entries.*",
        "",
    ]
    letter = None
    for name in sorted(entries, key=lambda s: re.sub(r"^(the|a)\s+", "", s, flags=re.I).lower()):
        key = re.sub(r"^(the|a)\s+", "", name, flags=re.I)[0].upper()
        if key != letter:
            letter = key
            lines += ["", f"## {letter}", ""]
        lines.append(f"- **{name}**: {entries[name]}")
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="")
    print(len(entries), "index entries")


if __name__ == "__main__":
    main()
