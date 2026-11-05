# The Confidence–Stakes Calibration

---

The pipeline tells you how to get to a belief. It does not tell you how firmly to hold the belief once you have it. This model does.

I did not set out to write it. It surfaced slowly, from the failures in these chapters: a retrieval system I trusted too much, a migration I analyzed too narrowly, a design document I verified too lightly because it read well. In each case the work was not the problem. The firmness was. I held a belief at one setting when the situation called for another.

## The model

Every belief you act on has three properties, and the discipline is to keep them matched.

1. **The stakes.** What does it cost if I am wrong, and who pays?
2. **The confidence I require before acting.** The higher the stakes, the more evidence I need before I commit.
3. **The review I owe the belief.** The higher the stakes, the more often I look again. When being wrong is cheap, I revise when convenient.

```
   THE CONFIDENCE–STAKES CALIBRATION

   ┌──────────────┬────────────────────┬────────────────────┐
   │              │  LOW STAKES        │  HIGH STAKES       │
   ├──────────────┼────────────────────┼────────────────────┤
   │  CONFIDENCE  │  Loose.            │  Firm enough       │
   │  REQUIRED    │  Experiment.       │  to commit.        │
   ├──────────────┼────────────────────┼────────────────────┤
   │  REVIEW      │  When convenient.  │  Frequent.         │
   ├──────────────┼────────────────────┼────────────────────┤
   │  IF WRONG    │  Revise cheaply.   │  Correct early,    │
   │              │                    │  before it spreads.│
   └──────────────┴────────────────────┴────────────────────┘

   Firm enough to act. Loose enough to correct.
```

<!-- diagram-alt -->*Diagram description: A confidence and stakes calibration table compares low- and high-stakes decisions across required confidence, review frequency, and the response to error. Low stakes allow experimentation and cheap revision, while high stakes call for firmer commitment, frequent review, and early correction.*


## Two ways to fail

The dogmatist holds everything firmly, including the things that should be held loosely, and so cannot correct. The skeptic holds nothing firmly, including the things that should be held firmly, and so cannot act. Wisdom is not a midpoint between them. It is the habit of asking, for each belief, what the stakes are, and setting the firmness accordingly.

## Where it appears in the book

- **Chapter 22** applies it to AI output: the trust calibration matrix is this model with verification cost added.
- **Chapter 25** applies it to decisions, where the stakes include values that cannot be added together.
- **Chapter 26** gives the full treatment.
- **Chapter 27** shows what holding beliefs this way looks like over ten years.

If the pipeline is the method, this is the dial. I would like the book to be remembered for both.

<!-- book-nav:start -->

---

[← A Note on Evidence](../00-front-matter/00-evidence-note.md) | [Contents](../README.md) | [Part I →](../part-1-the-problem/part-1-divider.md)

<!-- book-nav:end -->
