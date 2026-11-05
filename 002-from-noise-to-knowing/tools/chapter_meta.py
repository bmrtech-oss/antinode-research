"""Add the Level flag and Key Terms box to every chapter, and reflection questions to selected chapters.

Idempotent: each block lives between HTML-comment markers and is replaced on every run.
Key Terms come from Appendix A: a term belongs to the first chapter named in its "See:" line.

Run from the repository root:  python 002-from-noise-to-knowing/tools/chapter_meta.py
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GLOSSARY = "back-matter/98-appendix-a-glossary.md"

BEGINNER = {1, 2, 3, 4, 5, 6, 15, 20}
BOTH = set(range(7, 15))
ADVANCED = {16, 17, 18, 19, 21, 22, 23, 24, 25, 26, 27}

META_START, META_END = "<!-- chapter-meta:start -->", "<!-- chapter-meta:end -->"
REFL_START, REFL_END = "<!-- reflection:start -->", "<!-- reflection:end -->"

QUESTIONS = {
    8: [
        "List the last five sources you added to something you read regularly: a feed, a newsletter, a channel, a saved-search alert. For each, write the question it helps you answer. How many serve none?",
        "Recall a recent decision where you had more candidates than you could examine. What was your stopping rule, and did it choose by relevance or by the order in which things arrived?",
        "Find one place in your work that maximizes recall: an alert, a search, a dashboard. Describe a version that selects instead. What would you lose, and would you miss it?",
        "Pick one source you trust highly. Apart from familiarity, what evidence do you have that it deserves the trust?",
    ],
    11: [
        "Take a test, review, or evaluation your team relies on. Who wrote it, and what did they believe when they wrote it? Name a result that would have surprised them. If you cannot, it may be a mirror.",
        "Choose a metric you report. Describe a way it could improve while the thing it is meant to measure gets worse.",
        "Recall a time you changed your mind because of evidence. Who designed the test that produced it? If you cannot remember one, what does that suggest?",
        "Think of the last time a check came back confirming exactly what you expected. What would a skeptical colleague have asked you to look at before you believed it?",
    ],
    14: [
        "Recall a belief you held longer than the evidence justified. What was the first signal you ignored, and what did it look like at the time?",
        "In your work, who is allowed to tell you that you are wrong, and how long does it take for the message to reach you? Sketch the path.",
        "Choose a system, process, or document you own that has not been reviewed since it was launched. What would drift look like, and what would you notice first?",
        "Think of an error from the last year that was fixed as a bug. Restate it as evidence about your model of the situation. What does it say?",
    ],
    15: [
        "Recall the last time someone handed you a pile of material and expected you to come back understanding it. Which parts of the instinctive summary did you produce? What would the one-page artifact have said instead?",
        "Write the purpose sentence for a question you have right now. A good one lets you reject half of what you could read. If yours rejects nothing, it is not yet a purpose.",
        "The briefing in the worked example includes \"what I do not know\" and \"what would change my mind.\" Which of your recent reports or summaries included either? What would adding them have changed for the reader?",
        "Which stage took most of your time on your last piece of analysis, and which took least? Is that the proportion the question needed?",
    ],
    17: [
        "Take a document you wrote or approved: a proposal, a design, a report. Strip the clothing from its three most persuasive paragraphs and restate each argument in plain language. Which survive?",
        "Which fallacy do you commit most often under time pressure? Find one instance from the past month.",
        "Where in your work does a technical term, such as an accuracy figure, a benchmark, or a best practice, do the job an argument should be doing?",
        "Take an AI-generated answer you used recently. Which claim in it would you have challenged if a colleague had made it?",
    ],
    18: [
        "Think of the last important decision you took part in. Trace the order in which evidence was presented. Who spoke first, and would a different order have changed the outcome?",
        "Recall a time you paid the courage tax, or chose not to. What did it cost? What would have made the price lower?",
        "What counts as evidence on your team? When a senior person's recollection and an incident report disagree, which wins? Write down the rule that is actually followed, not the one that is stated.",
        "Name one thing you could do this month to lower the cost of dissent for someone who works beside you or reports to you.",
    ],
    19: [
        "Run an unscaffolded test on one topic in your field. Without tools, write what you know and the three questions you would ask next. Where did you find yourself reaching for something that was not there?",
        "List the tools you rely on every day. For each, decide whether it extends a capacity you have or substitutes for one you no longer exercise.",
        "Which scaffold would hurt most if it disappeared tomorrow? Is it backed up, documented, and understood well enough that you could rebuild it?",
        "Find a scaffold you use that could pay down its own debt, that is, one that could be changed to build capacity as well as extend it. What would the change be?",
    ],
    22: [
        "Pick an AI output you used in the last month. Where did it sit on the trust calibration matrix, and did you verify it in proportion?",
        "Find one place in that output where a gap might have been filled with something confident: a name, a number, a citation, a standard. Check three such items.",
        "What do you do differently with a junior colleague's draft than with an AI draft? Where is the difference unjustified in either direction?",
        "Write a one-sentence instruction that asks an AI to say what it is unsure of. Try it on a real question and compare the result with your usual prompt.",
    ],
    23: [
        "Think of a model, metric, or analysis in your work that was validated on data from the same source or period it was built on. Where could temporal leakage be hiding, and how would you split the data to find out?",
        "Which of the three temptations are you most exposed to at the moment? What evidence would tell you?",
        "Choose a number you report as a result. What decision does it drive, and is the thing measured the thing that matters?",
        "Is there a model you use that predicts but does not tell you what to do? Write the question it does not answer.",
    ],
    25: [
        "Describe a decision where you reduced a conflict of values to a single number. What was left out of the calculation?",
        "For a decision you face now, list the values at stake and mark which are commensurable. How will you weigh the rest, and who should be in the room when you do?",
        "Take the last decision that went badly. Separate the judgment from the outcome. Was it a good decision with a bad result, or the other way round?",
        "Whose judgment do you trust most? What is your evidence for it other than their confidence?",
    ],
    26: [
        "Which of your beliefs do you hold more firmly than you could justify? Who benefits from your holding it that way?",
        "Think of someone whose judgment you admire. What do they do, in observable terms, that shows they hold beliefs at different firmness for different stakes?",
        "Where do the stakes of your decisions escape you? Name someone who pays when you are wrong and is not you.",
        "Of the six practices for cultivating wisdom, which have you neglected? What is the cheapest version you could start this week?",
    ],
    27: [
        "Look back over the last year. Which days looked wasted but fed something later? Can you trace one thread from the day to the result?",
        "What does your calendar protect for reading and thinking without producing? What would you have to give up to protect more?",
        "Of the seven virtues in this chapter, which do you avoid most in practice? Describe a recent situation where it was called for.",
        "If you kept a log for ten years, what would you want it to show? What will you start recording this week?",
    ],
}


def slug(name):
    s = re.sub(r"[^\w\s-]", "", name.lower()).strip()
    return re.sub(r"[-\s]+", "-", s)


def glossary_terms():
    text = (ROOT / GLOSSARY).read_text(encoding="utf-8").replace("\r\n", "\n")
    by_chapter = {}
    for block in re.split(r"\n### ", text)[1:]:
        name = block.split("\n", 1)[0].strip()
        see = re.search(r"\*\*See:\*\*\s*(.*)", block)
        nums = re.findall(r"Chapters? (\d+)", see.group(1)) if see else []
        if nums:
            by_chapter.setdefault(int(nums[0]), []).append(name)
    return by_chapter


def level(n):
    return "Beginner" if n in BEGINNER else "Both" if n in BOTH else "Advanced"


def meta_block(n, terms):
    links = " · ".join(f"[{t}](../back-matter/98-appendix-a-glossary.md#{slug(t)})" for t in sorted(terms))
    return (
        f"{META_START}\n\n"
        f"**Level:** {level(n)}\n\n"
        f"> **Key Terms:** {links}. Definitions are in [Appendix A](../back-matter/98-appendix-a-glossary.md).\n\n"
        f"{META_END}\n\n"
    )


def reflection_block(n):
    items = "\n".join(f"{i}. {q}" for i, q in enumerate(QUESTIONS[n], 1))
    return (
        f"{REFL_START}\n\n"
        f"## Reflection Questions\n\n"
        f"Each takes between ten and thirty minutes and asks you to look at your own work.\n\n"
        f"{items}\n\n"
        f"{REFL_END}\n\n"
    )


def strip_block(text, start, end):
    return re.sub(re.escape(start) + r".*?" + re.escape(end) + r"\n*", "", text, flags=re.S)


def process(path, n, terms):
    raw = path.read_text(encoding="utf-8")
    nl = "\r\n" if "\r\n" in raw else "\n"
    t = raw.replace("\r\n", "\n")
    t = strip_block(t, META_START, META_END)
    t = strip_block(t, REFL_START, REFL_END)
    head, rest = t.split("\n", 1)
    t = head + "\n\n" + meta_block(n, terms) + rest.lstrip("\n")
    if n in QUESTIONS:
        i = t.index("## Chapter Summary")
        j = t.index("\n---\n", i)
        t = t[:j].rstrip("\n") + "\n\n" + reflection_block(n).rstrip("\n") + "\n" + t[j:]
    path.write_text(t.replace("\n", nl), encoding="utf-8", newline="")


def main():
    terms = glossary_terms()
    for path in sorted(ROOT.glob("part-*/[0-9][0-9]-*.md")):
        n = int(path.name[:2])
        process(path, n, terms.get(n, []))
    print("chapters processed; reflection questions in", sorted(QUESTIONS))


if __name__ == "__main__":
    main()
