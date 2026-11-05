"""Generate README.md, mkdocs.yml and prev/next footers from the book's file order.

Re-run after adding, renaming, merging or removing chapters:

    python 002-from-noise-to-knowing/tools/build_book.py
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
START, END = "<!-- book-nav:start -->", "<!-- book-nav:end -->"

PARTS = [
    ("part-1-the-problem", "Part I"),
    ("part-2-the-foundations", "Part II"),
    ("part-3-the-process", "Part III"),
    ("part-4-the-obstacles", "Part IV"),
    ("part-5-the-tools", "Part V"),
    ("part-6-mastery", "Part VI"),
]
FRONT = [
    "00-cover-page.md",
    "00-opening-thoughts.md",
    "00-table-of-contents.md",
    "00-evidence-note.md",
    "00-calibration-model.md",
]
EXTRAS = [
    ("00-front-matter/00-blog-post.md", None),
    ("00-front-matter/00-blog-diagram.md", None),
    ("00-front-matter/00-rating-notes.md", None),
]
TITLE_OVERRIDES = {"00-front-matter/00-cover-page.md": "Cover"}


def read(path):
    with open(path, encoding="utf-8", newline="") as f:
        return f.read()


def title_of(rel):
    if rel in TITLE_OVERRIDES:
        return TITLE_OVERRIDES[rel]
    for line in read(ROOT / rel).splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return Path(rel).stem


def part_files(folder):
    files = sorted(p.name for p in (ROOT / folder).glob("*.md"))
    divider = [f for f in files if "divider" in f]
    return [f"{folder}/{f}" for f in divider + [f for f in files if f not in divider]]


def build_structure():
    front = [f"00-front-matter/{f}" for f in FRONT]
    parts = [(label, part_files(folder)) for folder, label in PARTS]
    back = sorted(p.relative_to(ROOT).as_posix() for p in (ROOT / "back-matter").glob("*.md"))
    return front, parts, back


def rel_link(src, dst):
    up = len(Path(src).parts) - 1
    return "../" * up + dst


def short_title(rel):
    return title_of(rel).split(":")[0].split(" — ")[0]


def footer(order, i):
    src = order[i]
    bits = []
    if i > 0:
        bits.append(f"[← {short_title(order[i - 1])}]({rel_link(src, order[i - 1])})")
    bits.append(f"[Contents]({rel_link(src, 'README.md')})")
    if i < len(order) - 1:
        bits.append(f"[{short_title(order[i + 1])} →]({rel_link(src, order[i + 1])})")
    return f"{START}\n\n---\n\n" + " | ".join(bits) + f"\n\n{END}\n"


def apply_footers(order):
    pattern = re.compile(rf"\n*{re.escape(START)}.*?{re.escape(END)}\n?", re.S)
    for i, rel in enumerate(order):
        path = ROOT / rel
        text = pattern.sub("", read(path)).rstrip() + "\n\n"
        path.write_text(text + footer(order, i), encoding="utf-8", newline="")


SITE_URL = "https://bmrtech-oss.github.io/antinode-research/"


def write_readme(front, parts, back):
    out = [
        "# From Noise to Knowing",
        "",
        "*The Discipline of Turning Information into Knowledge* — Pramod Rathod",
        "",
        "Start reading with the [cover](00-front-matter/00-cover-page.md) or "
        "[opening thoughts](00-front-matter/00-opening-thoughts.md). "
        "Each page links to the previous and next page.",
        "",
        f"**Read it online:** [{SITE_URL}]({SITE_URL})",
        "",
        "## Front Matter",
        "",
    ]
    out += [f"- [{title_of(f)}]({f})" for f in front]
    for _, files in parts:
        out += ["", f"## {title_of(files[0])}", ""]
        out += [f"- [{title_of(f)}]({f})" for f in files[1:]]
    out += ["", "## Back Matter", ""]
    out += [f"- [{title_of(f)}]({f})" for f in back]
    out += ["", "## Extras", ""]
    out += [f"- [{name or title_of(f)}]({f})" for f, name in EXTRAS]
    (ROOT / "README.md").write_text("\n".join(out) + "\n", encoding="utf-8", newline="")


def write_mkdocs(front, parts, back):
    def item(f, name=None):
        label = (name or title_of(f)).replace('"', "'")
        return f'      - "{label}": {f}'

    lines = [
        "site_name: From Noise to Knowing",
        "site_description: The Discipline of Turning Information into Knowledge",
        "site_author: Pramod Rathod",
        "repo_url: https://github.com/bmrtech-oss/antinode-research",
        "edit_uri: edit/main/002-from-noise-to-knowing/",
        "docs_dir: .",
        "site_dir: ../_site",
        "exclude_docs: |",
        "  tools/",
        "  editorial/",
        "hooks:",
        "  - tools/mkdocs_hooks.py",
        "extra_css:",
        "  - assets/book.css",
        "extra_javascript:",
        "  - assets/book-theme.js",
        "theme:",
        "  name: material",
        "  custom_dir: tools/overrides",
        "  font: false",
        "  features:",
        "    - navigation.footer",
        "    - navigation.top",
        "    - navigation.sections",
        "    - search.highlight",
        "    - content.action.edit",
        "  palette:",
        "    scheme: slate",
        "markdown_extensions:",
        "  - admonition",
        "  - toc: {permalink: true}",
        "  - pymdownx.superfences:",
        "      custom_fences:",
        "        - name: mermaid",
        "          class: mermaid",
        "          format: !!python/name:pymdownx.superfences.fence_code_format",
        "nav:",
        "  - Home: README.md",
        "  - Front Matter:",
    ]
    lines += [item(f) for f in front]
    for _, files in parts:
        lines.append(f'  - "{title_of(files[0])}":')
        lines += [item(f) for f in files]
    lines.append("  - Back Matter:")
    lines += [item(f) for f in back]
    lines.append("  - Extras:")
    lines += [item(f, name) for f, name in EXTRAS]
    (ROOT / "mkdocs.yml").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="")


def write_toc(front, parts, back):
    toc_rel = "00-front-matter/00-table-of-contents.md"
    path = ROOT / toc_rel
    text = read(path).replace("\r\n", "\n")

    def link(f, label):
        return f"[{label}]({rel_link(toc_rel, f)})"

    def region(name, body):
        nonlocal text
        pat = re.compile(rf"(<!-- toc:{name}:start -->\n).*?(<!-- toc:{name}:end -->)", re.S)
        text = pat.sub(lambda m: m.group(1) + body + "\n" + m.group(2), text)

    region("front", "\n".join(f"- {link(f, title_of(f))}" for f in front))
    for (folder, _), (_, files) in zip(PARTS, parts):
        rows = ["| Ch. | Title |", "|-----|-------|"]
        for f in files[1:]:
            m = re.match(r"(\d+)-", Path(f).name)
            if not m:
                continue
            num = int(m.group(1))
            name = title_of(f).split(": ", 1)[-1]
            rows.append(f"| {num} | {link(f, name)} |")
        region(folder, "\n".join(rows))
    region("back", "\n".join(f"- {link(f, title_of(f))}" for f in back))

    chapters = {int(re.match(r"(\d+)-", Path(f).name).group(1)): f
                for _, files in parts for f in files[1:]}

    def chapter_cell(m):
        num = int(m.group(1) or m.group(2))
        return f"| {link(chapters[num], f'Ch. {num}')} |" if num in chapters else m.group(0)

    text = re.sub(r"\| (?:\[Ch\. (\d+)\]\([^)]*\)|Ch\. (\d+)) \|$", chapter_cell, text, flags=re.M)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


def main():
    front, parts, back = build_structure()
    order = front + [f for _, files in parts for f in files] + back
    write_toc(front, parts, back)
    apply_footers(order)
    write_readme(front, parts, back)
    write_mkdocs(front, parts, back)
    print(f"{len(order)} pages in reading order")


if __name__ == "__main__":
    main()
