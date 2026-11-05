# Chapter 14: Correct — Updating Beliefs and Models in Light of Error

---

For two years, I believed that hybrid retrieval was better than dense retrieval.

I had evidence. When I first built the system, I benchmarked both approaches on our internal evaluation set. Hybrid—combining sparse keyword matching with dense semantic search—scored higher. It retrieved more relevant documents. It handled edge cases better. It was, by every metric I had, the superior approach.

So I built the system on hybrid retrieval. I tuned it. I optimized it. I defended it in design reviews when colleagues suggested alternatives. I had data. The data said hybrid was better.

Two years later, a new engineer joined the team and asked a question that I had never thought to ask: *When was the last time we re-ran the benchmark?*

The answer was: two years ago. When we first built the system.

We re-ran it. Dense retrieval had improved dramatically—new embedding models, better training data, larger context windows. On the current evaluation set, dense retrieval scored higher than hybrid. It was faster, cheaper, and more accurate. The approach I had defended for two years was no longer the best approach.

I had not been wrong when I made the decision. I had been wrong when I stopped questioning it.

This chapter is about that failure—and about the discipline that prevents it.

---

## Why Correction Is the Most Important Stage

We have described six stages of the pipeline: select, pre-process, generate, test, integrate, retain or discard. Each stage is essential. But correction is the stage that makes all the others **work**.

Without correction, the pipeline is a **one-way process**. You select information, process it, generate models, test them, integrate them, retain what survives. But if you never correct—if you never update your models in light of new evidence—the pipeline produces the same output regardless of whether that output is true. It is a machine that runs, but does not learn.

```
 ┌───────────────────────────────────────────────────────────────────────┐
 │                                                                       │
 │                    THE PIPELINE AS A LEARNING SYSTEM                  │
 │                                                                       │
 │   ┌────────┐   ┌────────────┐   ┌──────────┐   ┌────────┐             │
 │   │ SELECT │──►│ PRE-PROCESS│──►│ GENERATE │──►│  TEST  │             │
 │   └────────┘   └────────────┘   └──────────┘   └────────┘             │
 │        ▲                                              │               │
 │        │                                              ▼               │
 │   ┌────────┐   ┌────────────┐   ┌────────────────────────┐            │
 │   │ CORRECT│◄──│   RETAIN   │◄──│       INTEGRATE        │            │
 │   │        │   │  / DISCARD │   │                        │            │
 │   └────────┘   └────────────┘   └────────────────────────┘            │
 │        │                                                              │
 │        └──────────────────────────► back to SELECT                    │
 │                                                                       │
 │   Correction is the feedback loop that makes the pipeline             │
 │   a learning system. Without it, the pipeline is static.              │
 │                                                                       │
 └───────────────────────────────────────────────────────────────────────┘
```

My retrieval system had no correction loop. It had a benchmark that was run once, a decision that was made once, and a belief that was never questioned. The system was not learning. It was repeating.

Correction is also the stage that most directly addresses the **knowledge gap**. The gap exists because information is abundant and knowledge is scarce. The scarcity of knowledge is, in large part, a scarcity of correction—a failure to update models in light of error.

And correction is the stage that most directly addresses the **human condition**. We are all prone to error. We all have beliefs that are false, models that are incomplete, judgments that are biased. The difference between the wise and the foolish is not that the wise make no errors. It is that the wise **correct** their errors. They seek out disconfirming evidence. They revise their beliefs. They learn.

---

## The Three Levels of Correction

Correction operates at three levels. Each level is more powerful than the one below it.

```
 ┌───────────────────────────────────────────────────────┐
 │                THE THREE LEVELS OF CORRECTION         │
 ├───────────────────────────────────────────────────────┤
 │                                                       │
 │   LEVEL 3: PROCESS    →  improve the method           │
 │        ▲                                              │
 │        │                                              │
 │   LEVEL 2: MODELS     →  revise the framework         │
 │        ▲                                              │
 │        │                                              │
 │   LEVEL 1: BELIEFS    →  update specific beliefs      │
 │                                                       │
 └───────────────────────────────────────────────────────┘
```

### Level 1: Correcting Beliefs

The first level is **correcting beliefs**—updating a specific belief in light of new evidence.

This is the most basic form of correction. You believe that a certain approach is better. The evidence shows that it is not. You correct your belief.

```
 ┌───────────────────────────────────────────────────────┐
 │                LEVEL 1: CORRECTING BELIEFS            │
 ├───────────────────────────────────────────────────────┤
 │  New evidence → Update specific belief                │
 │                                                       │
 │  "Hybrid retrieval is better."                        │
 │       ↓                                               │
 │  Evidence: dense retrieval now scores higher.         │
 │       ↓                                               │
 │  "Dense retrieval is better (now)."                   │
 │                                                       │
 │  Limitation: doesn't fix the underlying model.        │
 └───────────────────────────────────────────────────────┘
```

Belief correction is essential, but it is limited. It addresses the specific belief, but it does not address the **model** that produced the belief. If your model of retrieval is wrong—if you believed that hybrid was inherently superior—correcting a specific belief about a specific system will not fix the underlying problem.

### Level 2: Correcting Models

The second level is **correcting models**—revising the underlying framework that produced the beliefs.

This is a deeper form of correction. You do not just update a specific belief; you revise the model that generated the belief. If your model of retrieval is wrong—if you believed that hybrid was always better—you must revise the model itself.

```
 ┌───────────────────────────────────────────────────────┐
 │                LEVEL 2: CORRECTING MODELS             │
 ├───────────────────────────────────────────────────────┤
 │  Repeated errors → Revise underlying model            │
 │                                                       │
 │  Model: "Hybrid is always better than dense."         │
 │       ↓                                               │
 │  Evidence: dense improved, hybrid did not.            │
 │       ↓                                               │
 │  Revised model: "The better approach depends on       │
 │                  the current state of the embedding   │
 │                  models and the data."                │
 │                                                       │
 │  More powerful: addresses the source of the error.    │
 └───────────────────────────────────────────────────────┘
```

Model correction is more powerful than belief correction because it addresses the **source** of the error, not just the symptom. It prevents future errors of the same kind.

My belief that hybrid was better was a symptom. The model that produced it was: *the best approach is the one that scored highest on the benchmark when I first ran it.* That model was wrong. It assumed that benchmarks are timeless. They are not.

### Level 3: Correcting the Process

The third level is **correcting the process**—improving the method by which you acquire knowledge.

This is the deepest form of correction. You do not just revise a model; you revise the **pipeline** that produced the model. If your selection criteria are biased, you revise them. If your testing is insufficient, you strengthen it. If your retention is hoarding, you prune it.

```
 ┌───────────────────────────────────────────────────────┐
 │                LEVEL 3: CORRECTING THE PROCESS        │
 ├───────────────────────────────────────────────────────┤
 │  Systematic errors → Improve the method               │
 │                                                       │
 │  Problem: benchmarks are run once, then forgotten.    │
 │       ↓                                               │
 │  Correction: add a scheduled re-evaluation.           │
 │       ↓                                               │
 │  Improved pipeline: benchmarks are re-run quarterly.  │
 │                                                       │
 │  Most powerful: addresses the system itself.          │
 └───────────────────────────────────────────────────────┘
```

Process correction is the most powerful form of correction because it addresses the **system** that produces knowledge. It makes the entire pipeline more reliable, more accurate, more effective.

My retrieval failure was ultimately a process failure. I had a process that evaluated the system once, at the beginning, and never again. The process had no correction loop. Fixing the belief (dense is better now) was necessary. Fixing the model (approaches change over time) was better. Fixing the process (re-evaluate quarterly) was the real fix.

```
   THE THREE LEVELS IN PRACTICE

   ┌──────────────────────────────────────────────────────┐
   │  LEVEL 1: "Dense retrieval is better now."           │
   │           (fixes the answer)                         │
   ├──────────────────────────────────────────────────────┤
   │  LEVEL 2: "The best approach depends on the current  │
   │           state of the models and data."             │
   │           (fixes the reasoning)                      │
   ├──────────────────────────────────────────────────────┤
   │  LEVEL 3: "We need to re-run benchmarks on a         │
   │           schedule, not just once."                  │
   │           (fixes the system)                         │
   └──────────────────────────────────────────────────────┘

   All three are necessary.
   Level 3 is the one that prevents the next failure.
```

---

## Error as a Signal

Correction is driven by **error**—the discrepancy between expectation and reality. The knowledge engineer does not fear error; they **seek** it, because error is the signal that drives learning.

This is a profound shift in attitude. Most people treat error as a failure—something to be avoided, hidden, or explained away. The knowledge engineer treats error as a **gift**—an opportunity to correct, to improve, to learn.

```
 ┌───────────────────────────────────────────────────────┐
 │                ERROR AS A SIGNAL                      │
 ├───────────────────────────────────────────────────────┤
 │  Most people:                                         │
 │    Error → Failure → Avoid, hide, explain away        │
 │                                                       │
 │  Knowledge engineer:                                  │
 │    Error → Signal → Seek, amplify, learn from         │
 │                                                       │
 │  The attitude toward error is the difference between  │
 │  stagnation and growth.                               │
 └───────────────────────────────────────────────────────┘
```

The neuroscience of error is instructive. As we saw in Chapter 6, the brain encodes **prediction error** through dopamine. When an outcome is better than expected, dopamine neurons fire; when it is worse, they pause. This signal drives learning.

The knowledge engineer **harnesses** this signal. They do not suppress error; they amplify it. They expose their models to tests that could fail. They seek out disconfirming evidence. They welcome criticism. They treat being wrong as an opportunity to become less wrong.

For the retrieval system, the error signal was the production degradation. The system was getting worse, and I was not seeing it. I had no mechanism for detecting the error—no monitoring, no comparison against a baseline, no feedback loop. The error was there. I was not looking for it.

```
   ERROR SIGNALS IN A RETRIEVAL SYSTEM

   ┌─────────────────────────────────────────────────────┐
   │                                                     │
   │   User feedback:    "This answer is wrong."         │
   │   User behavior:    Users reformulate the query     │
   │                     immediately after the answer.   │
   │   Metrics:          Answer quality trending down    │
   │                     over time.                      │
   │   Comparisons:      New approach outperforms the    │
   │                     current one in a re-benchmark.  │
   │                                                     │
   │   All of these are error signals.                   │
   │   The system had none of them.                      │
   │                                                     │
   └─────────────────────────────────────────────────────┘
```

The fix was to add error signals. We added user feedback logging. We added query reformulation tracking. We added periodic re-benchmarking. We added comparison against a baseline. The system went from having no correction loop to having four.

---

## The Bayesian Stance Revisited

We discussed the Bayesian stance in Chapter 11. Here we revisit it as a framework for correction.

In the Bayesian framework, beliefs are **probabilities**—degrees of belief that are updated as evidence arrives. Correction is the process of updating those probabilities in light of new evidence.

```
 ┌───────────────────────────────────────────────────────┐
 │              THE BAYESIAN STANCE REVISITED            │
 ├───────────────────────────────────────────────────────┤
 │  Beliefs are probabilities, not certainties.          │
 │  Correction is proportional to evidence.              │
 │  Correction is continuous.                            │
 │  The goal is calibration, not certainty.              │
 └───────────────────────────────────────────────────────┘
```

The Bayesian stance has several implications for correction:

**Correction is proportional to evidence.** Strong evidence produces large updates; weak evidence produces small updates. The knowledge engineer calibrates their correction to the strength of the evidence.

**Correction is continuous.** Beliefs are always being updated. There is no final state of knowledge—only a continuous process of revision.

**Correction is not certainty.** The goal is not to reach certainty; it is to reach **calibration**—a degree of belief that matches the evidence.

For the retrieval system, the Bayesian update should have been: my prior belief in hybrid retrieval was high (based on the initial benchmark). The production evidence—degradation, user complaints—was strong disconfirming evidence. The correct update was a large downward revision. I did not make it, because I was not looking at the production evidence as evidence. I was looking at it as bugs to fix, not as tests of the model.

---

## The Psychology of Correction

Correction is hard, not just because it requires evidence, but because it requires **psychology**. There are deep psychological barriers to changing one's mind.

```
 ┌─────────────────────────────────────────────────────────┐
 │            PSYCHOLOGICAL BARRIERS TO CORRECTION         │
 ├─────────────────────────────────────────────────────────┤
 │  SUNK COST FALLACY  →  "I've invested too much"         │
 │  CONFIRMATION BIAS  →  "I only see confirming evidence" │
 │  IDENTITY THREAT    →  "This belief is who I am"        │
 │  SOCIAL COST        →  "I'll lose my community"         │
 │  FEAR OF UNCERTAINTY→  "I can't handle not knowing"     │
 └─────────────────────────────────────────────────────────┘
```

**The sunk cost fallacy.** The tendency to continue investing in a belief or a model because of the resources already invested in it. "I've spent years believing this. I can't give it up now." The knowledge engineer recognizes that past investment is irrelevant to present truth.

**Confirmation bias.** The tendency to seek out and interpret information in ways that confirm existing beliefs. We have discussed this in Chapter 11. It is a barrier to correction because it prevents us from seeing the evidence that would require us to change.

**Identity threat.** The tendency to treat beliefs as part of one's identity. "I am a person who believes X." Changing the belief feels like changing the self. The knowledge engineer separates belief from identity.

**Social cost.** The tendency to avoid changing beliefs because of the social consequences. "If I change my mind, I will lose my community." The knowledge engineer recognizes that social approval is not evidence of truth.

**Fear of uncertainty.** The discomfort of not knowing. Changing a belief means entering a state of uncertainty. The knowledge engineer tolerates uncertainty.

For the retrieval system, the barriers were **sunk cost** and **identity threat**. I had invested two years in the hybrid approach. I had defended it in design reviews. Changing my mind meant admitting that I had been wrong—not just about the approach, but about the process by which I had chosen it. That was a threat to my identity as a competent engineer.

The fix was not just technical. It was psychological. I had to separate my identity from my belief. I had to accept that being wrong about the approach did not make me a bad engineer. It made me a human who had not corrected soon enough.

```
   SEPARATING BELIEF FROM IDENTITY

   ┌─────────────────────────────────────────────────────┐
   │                                                     │
   │   "I believed hybrid was better."                   │
   │         │                                           │
   │         ▼                                           │
   │   "That belief was wrong."                          │
   │         │                                           │
   │         ▼                                           │
   │   "I am still competent."                           │
   │         │                                           │
   │         ▼                                           │
   │   "I can correct and improve."                      │
   │                                                     │
   │   The belief is not the self.                       │
   │                                                     │
   └─────────────────────────────────────────────────────┘
```

---

## The Discipline of Error Correction

Correction is not a single act. It is a **discipline**—a set of practices that make correction habitual.

```
 ┌───────────────────────────────────────────────────────┐
 │            PRACTICES FOR ERROR CORRECTION             │
 ├───────────────────────────────────────────────────────┤
 │  1. SEEK DISCONFIRMING EVIDENCE                       │
 │  2. KEEP A PREDICTION JOURNAL                         │
 │  3. CONDUCT PRE-MORTEMS                               │
 │  4. USE RED TEAMS                                     │
 │  5. REVIEW AND REFLECT                                │
 └───────────────────────────────────────────────────────┘
```

### Practice 1: Seek Disconfirming Evidence

Go looking for the evidence that challenges your beliefs rather than waiting for it to find you; Chapter 11 gives the full treatment.

For the retrieval system, the disconfirming evidence was the production data. I should have been looking at it. I should have been asking: is the system getting worse? Is the approach still the best? I should have been seeking the evidence that would tell me I was wrong.

### Practice 2: Keep a Prediction Journal

Write down your predictions—what you expect to happen and why. Later, when the outcome is known, compare your prediction with what actually happened.

The prediction journal is a powerful tool for correction. It prevents hindsight bias—the tendency to believe, after the fact, that you predicted it all along. It provides a record of your accuracy—a way to calibrate your confidence.

For the retrieval system, I had no prediction journal. I had no record of what I expected the system to do. I had only the initial benchmark, and no record of what I expected after that. The absence of a prediction journal meant that I could not see the drift.

### Practice 3: Conduct Pre-Mortems

Before committing to a decision or a model, imagine that it has failed. Ask: What went wrong? What did we miss? What would we do differently?

The pre-mortem, developed by Gary Klein, forces you to consider the ways your model could be wrong—before you commit to it. It surfaces risks and assumptions that might otherwise go unnoticed.

For the retrieval system, a pre-mortem would have surfaced the risk: *the approach might become obsolete as the embedding models improve.* That risk was real. It was not considered. A pre-mortem would have considered it.

### Practice 4: Use Red Teams

A red team is a group whose job is to challenge the assumptions of the main group—to find the flaws, the weaknesses, the blind spots.

Red teams are used in the military, in intelligence, and increasingly in business. The knowledge engineer uses them to test their models. They invite criticism. They reward people who find errors.

For the retrieval system, the new engineer was an informal red team. She asked the question that no one else had asked: *when was the last time we re-ran the benchmark?* That question was the red team's contribution. It found the flaw.

### Practice 5: Review and Reflect

After a project, a decision, or a cycle of the pipeline, take time to review what happened. What went well? What went wrong? What did you learn? What would you do differently?

Review and reflection turn experience into knowledge. Without reflection, experience is just a series of events. With reflection, it becomes a source of correction and improvement.

```
   THE CORRECTION LOOP

   ┌──────────────┐
   │   PREDICT    │
   └──────┬───────┘
          │
          ▼
   ┌──────────────┐
   │   OBSERVE    │
   └──────┬───────┘
          │
          ▼
   ┌──────────────┐
   │   COMPARE    │
   └──────┬───────┘
          │
          ▼
   ┌──────────────┐
   │   CORRECT    │
   └──────┬───────┘
          │
          ▼
   ┌──────────────┐
   │   REFLECT    │
   └──────┬───────┘
          │
          └──────────► PREDICT again

   The loop is not complete until reflection.
   Reflection is what turns correction into learning.
```

---

## Correcting the Process

We have said that the deepest level of correction is **correcting the process**. This is the work of improving the pipeline itself—making it more reliable, more accurate, more effective.

```
 ┌───────────────────────────────────────────────────────┐
 │              CORRECTING THE PROCESS                   │
 ├───────────────────────────────────────────────────────┤
 │  AUDIT SELECTION   →  what am I missing?              │
 │  STRENGTHEN TESTING→  am I seeking disconfirmation?   │
 │  IMPROVE INTEGRATION→  are models connected?          │
 │  REFINE RETENTION  →  is knowledge base focused?      │
 └───────────────────────────────────────────────────────┘
```

**Audit selection.** Are you selecting information that confirms your biases? Are you ignoring sources that might challenge you? The knowledge engineer periodically audits their selection.

**Strengthen testing.** Are you testing your models adequately? Are you seeking disconfirming evidence? The knowledge engineer periodically strengthens their testing.

**Improve integration.** Are you connecting your models to the rest of your knowledge? Are you resolving contradictions? The knowledge engineer periodically reviews their integration.

**Refine retention.** Are you retaining what matters? Are you discarding what does not? The knowledge engineer periodically reviews their retention.

For the retrieval system, the process correction was **scheduled re-evaluation**. We added a quarterly benchmark. We added a monthly review of production metrics. We added a process for comparing current performance against a baseline. The process went from having no correction loop to having a regular one.

```
   PROCESS CORRECTION IN PRACTICE

   ┌─────────────────────────────────────────────────────┐
   │                                                     │
   │   Before:                                           │
   │     Benchmark once → Decide → Never revisit         │
   │                                                     │
   │   After:                                            │
   │     Benchmark quarterly → Review monthly →          │
   │     Compare against baseline → Update decisions     │
   │                                                     │
   │   The process now has a correction loop.            │
   │                                                     │
   └─────────────────────────────────────────────────────┘
```

---

## Correction in the Age of AI

AI has changed the landscape of correction. Large language models can be corrected—they can be fine-tuned, retrained, and updated. They can learn from feedback. They can be improved over time.

But AI correction has its own pitfalls.

```
 ┌───────────────────────────────────────────────────────┐
 │                AI AND CORRECTION                      │
 ├───────────────────────────────────────────────────────┤
 │  WHAT AI CAN DO:                                      │
 │    • Learn from feedback                              │
 │    • Be fine-tuned and retrained                      │
 │    • Improve with more data                           │
 │                                                       │
 │  WHAT AI CANNOT DO:                                   │
 │    • Understand the mechanism of its errors           │
 │    • Correct without introducing new errors           │
 │    • Correct itself without human judgment            │
 └───────────────────────────────────────────────────────┘
```

**AI can be corrected without understanding.** A language model can be fine-tuned to produce more accurate outputs without understanding why the outputs were wrong. This is not correction; it is adjustment. True correction requires understanding the mechanism of the error.

**AI can be corrected in ways that introduce new errors.** Fine-tuning a model on one dataset can degrade its performance on another. Correcting one bias can introduce another.

**AI can be corrected by humans who are themselves uncorrected.** If the humans who are correcting the AI have biases, the AI will inherit those biases.

For the retrieval system, AI was part of the correction loop. We used the model to generate candidate answers, and we used user feedback to correct the model. But the correction was not automatic. It required human judgment—deciding what counted as an error, what should be corrected, and how.

The knowledge engineer uses AI as a **correction tool**, not as an **oracle**. They use it to identify errors, to test hypotheses, to explore alternatives. But they retain the responsibility for the correction. They understand the mechanism. They test the results. They take responsibility for the knowledge.

---

## The Humility of Correction

We have described correction as a discipline—a set of practices and principles. But correction is also a **virtue**. It requires humility.

```
 ┌───────────────────────────────────────────────────────┐
 │                THE HUMILITY OF CORRECTION             │
 ├───────────────────────────────────────────────────────┤
 │  1. ALL KNOWLEDGE IS PROVISIONAL                      │
 │  2. ERROR IS INEVITABLE                               │
 │  3. UNCERTAINTY IS NOT FAILURE                        │
 │  4. LEARNING IS LIFELONG                              │
 └───────────────────────────────────────────────────────┘
```

**All knowledge is provisional.** Every model is subject to revision. Holding on to a model after it has been disproven is not loyalty; it is stubbornness.

**Error is inevitable.** No one is immune to error. The difference between the wise and the foolish is not that the wise make no errors. It is that the wise correct their errors.

**Uncertainty is not failure.** Not knowing is not a failure; it is a condition of knowledge. The knowledge engineer is comfortable with uncertainty, because they know that certainty is impossible.

**Learning is a lifelong process.** There is no final state of knowledge. There is only the continuous process of correction and improvement.

For the retrieval system, humility was the missing ingredient. I had been confident. I had been certain. I had believed that the benchmark was timeless. Humility would have told me: *you might be wrong. You should check. You should re-evaluate.* Humility would have corrected the error two years earlier.

---

## A Return to the Benchmark

We re-ran the benchmark. We switched to dense retrieval. The system got faster, cheaper, and more accurate.

But the more important change was the process. We added a quarterly benchmark. We added a monthly review. We added a prediction journal—we wrote down what we expected the system to do, and we compared it against what it actually did.

The system did not become perfect. It became **correctable**. It became a system that could learn from its errors, rather than a system that repeated them.

I think about that failure often. It taught me something that I have applied to every system I have built since, and to my own thinking. The lesson is simple: **the most dangerous belief is the one you never question.** The most dangerous model is the one you never test. The most dangerous process is the one with no correction loop.

The retrieval system did not fail because it was wrong. It failed because it could not become less wrong.

This is the lesson of Chapter 14. Correction is the stage that makes the pipeline a learning system. It is the stage that closes the gap between information and knowledge. It is the stage that makes knowledge possible.

And it begins with humility—the recognition that you can be wrong, that your models are provisional, that the only way to know is to correct.

---

## Chapter Summary

- **Correction** is the seventh and final stage of the knowledge pipeline. It is the feedback loop that makes the pipeline a learning system.
- Correction operates at three levels: **belief correction** (updating specific beliefs), **model correction** (revising underlying frameworks), and **process correction** (improving the method itself).
- **Error is a signal**, not a failure. The knowledge engineer seeks error because it drives learning.
- The **Bayesian stance** holds that beliefs are probabilities updated in light of evidence. Correction is proportional to evidence and continuous. The goal is calibration, not certainty.
- **Psychological barriers** to correction include the sunk cost fallacy, confirmation bias, identity threat, social cost, and fear of uncertainty.
- The **discipline of error correction** includes five practices: seeking disconfirming evidence, keeping a prediction journal, conducting pre-mortems, using red teams, and reviewing and reflecting.
- **Correcting the process** involves auditing selection, strengthening testing, improving integration, and refining retention.
- **AI can assist** with correction—learning from feedback, being fine-tuned—but it cannot replace human judgment. True correction requires understanding and responsibility.
- **Humility** is the virtue that underlies correction. It is the recognition that you can be wrong, that all knowledge is provisional, that error is inevitable, and that learning is lifelong.
- The lesson of the **retrieval system** is that the most dangerous belief is the one you never question. The system did not fail because it was wrong. It failed because it could not become less wrong.

---

**Next Chapter:** *The Pipeline in Practice — A Guide to Implementation* — the first chapter of Part IV, offering a practical guide to applying the pipeline in everyday life, including exercises, checklists, and case studies.

---

<!-- book-nav:start -->

---

[← Chapter 13](../part-3-the-process/13-retain-or-discard.md) | [Contents](../README.md) | [Chapter 15 →](../part-3-the-process/15-the-pipeline-in-practice.md)

<!-- book-nav:end -->
