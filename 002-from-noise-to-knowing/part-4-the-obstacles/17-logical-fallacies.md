# Chapter 17: Logical Fallacies — The Enemies Without

<!-- chapter-meta:start -->

**Level:** Advanced

> **Key Terms:** [Cherry-Picking](../back-matter/98-appendix-a-glossary.md#cherry-picking) · [Equivocation](../back-matter/98-appendix-a-glossary.md#equivocation) · [Fallacy](../back-matter/98-appendix-a-glossary.md#fallacy) · [Survivorship Bias](../back-matter/98-appendix-a-glossary.md#survivorship-bias). Definitions are in [Appendix A](../back-matter/98-appendix-a-glossary.md).

<!-- chapter-meta:end -->

---

I once approved an architecture decision because the document arguing for it was the most rigorous thing I had read all quarter.

It had numbered premises. It had citations. It had a cost-benefit table. It had a section titled "Risks and Mitigations." It ran to eleven pages, and every page looked like engineering.

The argument, stripped of its clothes, was this:

1. Our current system has performance problems.
2. The proposed system is used by three companies that are larger than us.
3. Therefore, the proposed system will solve our performance problems.

That is a non sequitur. The fact that larger companies use a system does not establish that the system will fix our specific problems. It might. It might not. The document never argued that it would—it argued that *other people had chosen it*, and dressed that up in enough structure that nobody asked the obvious question.

I asked the obvious question two months later, when the migration was half done and the performance problems were unchanged. By then we had spent the budget.

The document was not written by a fool. It was written by a competent engineer who believed the conclusion and constructed an argument to support it. And the fallacy survived review because it was wearing technical clothing. Nobody expects a straw man in a design doc. Nobody looks for a false dilemma in a build-versus-buy analysis. The fallacies we learn to spot in political debate are not the fallacies that cost us money.

This chapter is about those fallacies—the enemies without. Not the distortions inside your mind, but the defects in the structure of arguments, including the ones that look most like engineering.

---

## Why Fallacies Matter for the Pipeline

We have said that cognitive biases are errors in **how we think**. Logical fallacies are errors in **how we argue**—in the structure of reasoning itself.

The distinction matters. A bias is a tendency of the mind. A fallacy is a defect in an argument. You can commit a fallacy without being biased, and be biased without committing a fallacy. But the two are intertwined: biases make us more likely to commit fallacies, and fallacies reinforce biases.

Fallacies affect every stage of the pipeline where reasoning is involved.

```
 ┌───────────────────────────────────────────────────────┐
 │              FALLACIES AFFECT EVERY STAGE             │
 ├───────────────────────────────────────────────────────┤
 │  SELECT       →  appeals to authority or popularity   │
 │  PRE-PROCESS  →  equivocation, ambiguity              │
 │  GENERATE     →  false analogy, hasty generalization  │
 │  TEST         →  post hoc, cum hoc, cherry-picking    │
 │  INTEGRATE    →  circular reasoning, false dilemma    │
 │  RETAIN       →  appeals to tradition                 │
 │  CORRECT      →  appeal to ignorance, ad hominem      │
 └───────────────────────────────────────────────────────┘
```

<!-- diagram-alt -->*Diagram description: A diagram maps logical fallacies to each pipeline stage, from appeals to authority or popularity during SELECT to appeals to ignorance and ad hominem during CORRECT.*


The architecture document failed at the **testing** stage. The argument was never subjected to a test that could distinguish "this system works for us" from "this system is popular." It was accepted because it looked like reasoning, not because it was.

---

## The Anatomy of a Fallacy

A **logical fallacy** is a pattern of reasoning that appears valid but is not. The conclusion may be true, but the argument does not establish it.

```
 ┌───────────────────────────────────────────────────────┐
 │              THE ANATOMY OF A FALLACY                 │
 ├───────────────────────────────────────────────────────┤
 │                                                       │
 │   PREMISE ──────► INFERENCE ──────► CONCLUSION        │
 │      │                │                  │            │
 │      ▼                ▼                  ▼            │
 │   (defect)         (defect)           (defect)        │
 │                                                       │
 │   A fallacy is a defect in any of these components.   │
 │                                                       │
 └───────────────────────────────────────────────────────┘
```

<!-- diagram-alt -->*Diagram description: A diagram shows a fallacy as a possible defect in any link from premise through inference to conclusion, with each component marked as a place where reasoning can fail.*


There are six families of fallacy, each with its own logic and its own countermeasures. We will go through them quickly—the catalog is well known—and then spend the rest of the chapter on the thing the catalog usually misses: **why fallacies in professional reasoning are so much harder to see than fallacies in political argument.**

---

## The Six Families

The six families are fallacies of premise, conclusion, ambiguity, causal reasoning, statistics, and relevance.

### Family 1: Fallacies of Premise

The starting point is broken.

**Begging the question.** Assuming the conclusion in the premise. *"This architecture is correct because it follows best practices, and best practices are whatever this architecture does."*

**False premise.** An argument resting on something untrue. *"All distributed systems need eventual consistency."*

### Family 2: Fallacies of Conclusion

The premises may be fine, but the conclusion does not follow.

**Non sequitur.** The conclusion does not follow at all. *"Company X uses this tool; therefore it will solve our problem."*

**Hasty generalization.** A general conclusion from a small sample. *"We tested it on three workloads and it was faster, so it is faster."*

**False dilemma.** Two options presented when more exist. *"Either we migrate or we fall behind."*

**Straw man.** Misrepresenting a position to attack it. *"The critics want us to keep the old system forever."*

### Family 3: Fallacies of Ambiguity

The words shift meaning.

**Equivocation.** Same word, different senses. *"The system is 'available'—it responds to health checks. What do you mean, users can't log in?"*

**Amphiboly.** Grammatical ambiguity. *"We will review the proposal with the security team."* (Are they reviewing it, or are you reviewing it together?)

### Family 4: Causal Fallacies

The causal reasoning is broken.

**Post hoc.** B followed A, so A caused B. *"We deployed the caching layer and latency improved."* (Or traffic dropped.)

**Cum hoc.** A and B correlate, so one causes the other. *"Teams that use this tool ship faster."* (Or faster teams choose this tool.)

**Ignoring a common cause.** Both are caused by a third factor. *"Services with more logs have more incidents."* (Or high-traffic services generate both more logs and more incidents.)

### Family 5: Statistical Fallacies

The numbers are misused.

**Base rate neglect.** Ignoring the prior probability. *"The classifier is 99% accurate."* (On a dataset where 1% are positive.)

**Survivorship bias.** Only the survivors are studied. *"Every successful startup we studied had a strong culture."* (How many strong-culture startups failed?)

**Regression to the mean.** Extreme values return to normal. *"We intervened during the outage and performance recovered."* (It would have recovered anyway.)

**Cherry-picking.** Selecting only supporting evidence. *"Our benchmark shows a 40% improvement."* (On the one workload where it does.)

### Family 6: Fallacies of Relevance

The appeal is to the wrong thing.

**Ad hominem.** Attacking the person. *"He's never run a team of this size, so his architecture review doesn't count."*

**Appeal to authority.** *"Google does it this way."*

**Appeal to ignorance.** *"No one has proven this approach will fail."*

**Bandwagon.** *"Every serious company is doing it."*

**Appeal to tradition.** *"This is how we've always done it."*

**Tu quoque.** *"You want us to document more, but your team's docs are a mess."*

---

## The Fallacy in Technical Clothing

Here is what the catalog misses.

The fallacies above are taught with political and everyday examples, where they are easy to spot. But the fallacies that actually cost money in engineering organizations look like this:

```
   THE FALLACY IN TECHNICAL CLOTHING

   PLAIN VERSION (easy to spot):
   "Everyone is doing it, so it must be right."

   TECHNICAL VERSION (hard to spot):
   "Industry leaders including [three large companies]
    have adopted this pattern, which suggests it has
    reached the maturity inflection point where the
    risk profile becomes favorable for organizations
    at our scale."

   Same fallacy: appeal to popularity.
   Different clothing: it looks like analysis.
```

The technical clothing does three things:

**It adds structure.** Numbered premises, citations, tables. Structure signals rigor. But structure is not validity—a fallacious argument can be formatted perfectly.

**It adds vocabulary.** Domain terms make an argument sound like reasoning. "Maturity inflection point" is not evidence. It is a phrase that sounds like evidence.

**It adds social cost to objecting.** When an argument is dressed in expertise, questioning it feels like questioning expertise. The reviewer who says "this is a non sequitur" sounds less sophisticated than the author who wrote eleven pages. So the reviewer stays quiet.

This is why the architecture document survived review. Nobody wanted to be the person who said "this is just an appeal to popularity" to a document with a cost-benefit table.

```
   WHY TECHNICAL FALLACIES SURVIVE REVIEW

   ┌───────────────────────────────────────────────┐
   │                                               │
   │   AUTHOR:    structure + vocabulary + length  │
   │                    │                          │
   │                    ▼                          │
   │   REVIEWER:  "It looks rigorous.              │
   │               I don't want to look            │
   │               unsophisticated by asking       │
   │               the obvious question."          │
   │                    │                          │
   │                    ▼                          │
   │   RESULT:    Fallacy approved.                │
   │              Budget spent.                    │
   │              Lesson unlearned.                │
   │                                               │
   └───────────────────────────────────────────────┘
```

<!-- diagram-alt -->*Diagram description: A flow from an author using structure, vocabulary, and length to a reviewer who mistakes the work for rigor and avoids an obvious question, ending with an approved fallacy, spent budget, and unlearned lesson.*


---

## The Professional Fallacy Checklist

For each common professional argument, there is a corresponding fallacy. Here is the working version of the catalog—the one I actually use.

```
 ┌───────────────────────────────────────────────────────┐
 │         PROFESSIONAL FALLACY PATTERNS                 │
 ├───────────────────────────────────────────────────────┤
 │  "Everyone is doing it"                               │
 │     →  Appeal to popularity / bandwagon               │
 │     ASK: Does adoption by others predict success      │
 │          for our specific case?                       │
 │                                                       │
 │  "Google/Amazon/Netflix does it"                      │
 │     →  Appeal to authority                            │
 │     ASK: Do they have our constraints, scale, team,   │
 │          and problem?                                 │
 │                                                       │
 │  "The benchmark shows 40% improvement"                │
 │     →  Cherry-picking, hasty generalization           │
 │     ASK: On what workload? Representative of ours?    │
 │          Who ran it? What was left out?               │
 │                                                       │
 │  "Either we migrate or we fall behind"                │
 │     →  False dilemma                                  │
 │     ASK: What are the third, fourth, fifth options?   │
 │                                                       │
 │  "We deployed X and metrics improved"                 │
 │     →  Post hoc, cum hoc                              │
 │     ASK: What else changed? Was there a control?      │
 │                                                       │
 │  "No one has shown this will fail"                    │
 │     →  Appeal to ignorance                            │
 │     ASK: Who holds the burden of proof?               │
 │                                                       │
 │  "This is industry best practice"                     │
 │     →  Appeal to authority + tradition                │
 │     ASK: What evidence supports the practice in       │
 │          contexts like ours?                          │
 │                                                       │
 │  "The team will adapt quickly"                        │
 │     →  Unwarranted assumption                         │
 │     ASK: What is the evidence? What is the track      │
 │          record of similar adaptations?               │
 └───────────────────────────────────────────────────────┘
```

<!-- diagram-alt -->*Diagram description: A diagram pairs common professional claims with fallacy patterns and probing questions, including appeals to popularity or authority, cherry-picking, false dilemmas, post hoc claims, appeals to ignorance, and unsupported assumptions.*


This table is worth more than the classical catalog. The classical catalog teaches you to spot fallacies in debate. This table teaches you to spot them in a design review.

---

## AI-Generated Fallacies

Here is where it gets harder.

Large language models are trained on human text, which is saturated with fallacies. They learn the patterns—not the validity, the patterns. And because they are optimized for plausibility, they reproduce fallacies fluently.

The result is a new failure mode: **fallacies that are grammatically perfect, syntactically confident, and structurally invalid.**

```
 ┌───────────────────────────────────────────────────────┐
 │              AI-GENERATED FALLACIES                   │
 ├───────────────────────────────────────────────────────┤
 │  • FALSE PREMISES        asserted with confidence     │
 │  • FABRICATED CITATIONS  that look real               │
 │  • NON SEQUITURS         that read as reasoning       │
 │  • FALSE DILEMMAS        presented as the only options│
 │  • APPEALS TO AUTHORITY  citing sources that may not  │
 │                          exist or may not say what is │
 │                          claimed                      │
 │  • CHERRY-PICKING        selecting favorable evidence │
 │  • PLAUSIBLE NONSENSE    fluent, confident, invalid   │
 └───────────────────────────────────────────────────────┘
```

<!-- diagram-alt -->*Diagram description: A diagram lists AI-generated fallacies: false premises, fabricated citations, non sequiturs, false dilemmas, appeals to authority, cherry-picking, and plausible-sounding nonsense.*


The architecture document I approved was written by a human. But the same document, generated by a model, would have been *worse*—not because the model is worse at reasoning, but because it is better at sounding like reasoning. It would have produced the citations. It would have produced the cost-benefit table. It would have produced the "Risks and Mitigations" section. And it would have produced them in seconds, in a tone of complete confidence.

This is the new problem. The classical fallacies required a human to construct them, and humans are bad at constructing them convincingly. Models are excellent at constructing them convincingly. The fallacy has been automated.

```
   THE AUTOMATION OF THE FALLACY

   BEFORE                          AFTER
   ┌──────────────────┐            ┌──────────────────┐
   │  Human writes    │            │  Model writes    │
   │  fallacious      │            │  fallacious      │
   │  argument        │            │  argument        │
   │                  │            │                  │
   │  Slow            │            │  Instant         │
   │  Imperfect       │            │  Flawless prose  │
   │  Detectable     │            │  Confident       │
   │  (rough edges)   │            │  (no rough edges)│
   └──────────────────┘            └──────────────────┘

   The fallacy is the same.
   The detection is harder.
```

<!-- diagram-alt -->*Diagram description: Two columns compare a human and a model producing the same fallacious argument: the model does so instantly in polished, confident prose, making the error harder to detect.*


The knowledge engineer must be more vigilant with AI-generated reasoning than with human reasoning—not because AI is more fallacious, but because its fallacies are more polished.

The countermeasures are specific:

**Formalize the argument.** Ask the model (or yourself) to state the premises and the conclusion explicitly. Strip the clothing. A non sequitur becomes visible when it is written as P1, P2, therefore C.

**Demand the disconfirming case.** Ask: what evidence would make this argument wrong? If the model cannot answer, the argument may not be an argument.

**Verify every citation.** Models fabricate sources. Check that they exist and that they say what is claimed.

**Check the structure, not the fluency.** Fluency is not validity. Read the argument for its logical form, not its rhetorical polish.

**Use a second model to critique the first.** Models are better at finding fallacies in others' arguments than in their own. Adversarial review helps.

---

## The Detection Method

How do you detect a fallacy? The six-step method from Chapter 17's original draft still applies, but it needs one addition for technical and AI-generated reasoning.

```
 ┌───────────────────────────────────────────────────────┐
 │              DETECTING FALLACIES                      │
 ├───────────────────────────────────────────────────────┤
 │  1. IDENTIFY THE CONCLUSION                           │
 │  2. IDENTIFY THE PREMISES                             │
 │  3. CHECK THE LOGIC                                   │
 │  4. CHECK THE TERMS                                   │
 │  5. CHECK THE EVIDENCE                                │
 │  6. CHECK THE RELEVANCE                               │
 │  7. STRIP THE CLOTHING                                │
 └───────────────────────────────────────────────────────┘
```

<!-- diagram-alt -->*Diagram description: A diagram of a seven-step fallacy check: identify the conclusion and premises, check logic, terms, evidence, and relevance, then strip away technical clothing.*


**Step 7 is the addition.** Rewrite the argument in its plainest form. Remove the technical vocabulary. Remove the structure. Remove the citations. What is left?

If the plain version is a fallacy, the technical version is a fallacy. The clothing does not change the structure. It only hides it.

For the architecture document, step 7 would have produced: *"Larger companies use this, so it will work for us."* That is a plain appeal to popularity. It would have taken thirty seconds to spot. It took two months to discover, because nobody stripped the clothing.

---

## A Return to the Architecture Document

I did not fix that migration. We finished it, because the sunk cost was too high to abandon, and we mitigated the performance problems with other changes. The system works now. It did not work because of the argument that approved it. It worked in spite of it.

What I fixed was my review process.

Now, when I review a technical proposal, I do one thing first: I strip it. I write the argument in plain language on a single page—premises, conclusion, nothing else. If the plain version is not convincing, the technical version does not get approved, no matter how many pages it has.

It is a small practice. It takes ten minutes. It has saved me from at least three more non sequiturs dressed as engineering.

The lesson of Chapter 17 is not that fallacies exist. Everyone knows that. The lesson is that **the fallacies that matter are the ones that don't look like fallacies.** They look like design documents. They look like benchmarks. They look like best practices. They look like the confident output of a language model.

The knowledge engineer strips the clothing. They check the structure. They ask the obvious question that nobody wants to ask, because asking it makes them look less sophisticated than the document they are questioning.

It doesn't. It makes them the only person in the room who is actually reading.

---

## Chapter Summary

- **Logical fallacies** are errors in reasoning—patterns of argument that appear valid but are not. They are the enemies without, complementing the cognitive biases that are the enemies within.
- Fallacies affect every stage of the pipeline where reasoning is involved.
- Fallacies fall into six families: **premise** (begging the question, false premise, unwarranted assumption), **conclusion** (non sequitur, hasty generalization, false dilemma, straw man, slippery slope), **ambiguity** (equivocation, amphiboly, accent), **causal** (post hoc, cum hoc, common cause, reverse causation), **statistical** (base rate neglect, survivorship bias, regression to the mean, cherry-picking), and **relevance** (ad hominem, appeal to authority, appeal to emotion, appeal to ignorance, bandwagon, tradition, tu quoque).
- The fallacies that matter most in professional work are **fallacies in technical clothing**—appeals to popularity dressed as maturity analysis, non sequiturs dressed as design documents, cherry-picked benchmarks dressed as evaluation.
- **AI-generated fallacies** are the same fallacies, but more polished and more confident. Models are optimized for plausibility, not validity, and they reproduce the fallacies in their training data fluently.
- The **detection method** includes a seventh step: **strip the clothing.** Rewrite the argument in plain language. If the plain version is a fallacy, the technical version is a fallacy.
- The lesson of the **architecture document** is that the fallacies that cost money don't look like fallacies. They look like engineering. The knowledge engineer strips the clothing and asks the obvious question.

<!-- reflection:start -->

## Reflection Questions

Each takes between ten and thirty minutes and asks you to look at your own work.

1. Take a document you wrote or approved: a proposal, a design, a report. Strip the clothing from its three most persuasive paragraphs and restate each argument in plain language. Which survive?
2. Which fallacy do you commit most often under time pressure? Find one instance from the past month.
3. Where in your work does a technical term, such as an accuracy figure, a benchmark, or a best practice, do the job an argument should be doing?
4. Take an AI-generated answer you used recently. Which claim in it would you have challenged if a colleague had made it?

<!-- reflection:end -->

---

**Next Chapter:** *Social and Institutional Obstacles — When the Environment Fights Back* — a detailed examination of the social and institutional forces that derail the pipeline, including groupthink, information cascades, incentive structures, and the erosion of epistemic authority.

---

<!-- book-nav:start -->

---

[← Chapter 16](../part-4-the-obstacles/16-cognitive-biases.md) | [Contents](../README.md) | [Chapter 18 →](../part-4-the-obstacles/18-social-and-institutional-obstacles.md)

<!-- book-nav:end -->
