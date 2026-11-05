# Chapter 5: The Target — What Knowledge Actually Is

<!-- chapter-meta:start -->

**Level:** Beginner

> **Key Terms:** [Belief](../back-matter/98-appendix-a-glossary.md#belief) · [Coherence](../back-matter/98-appendix-a-glossary.md#coherence) · [Explicit Knowledge](../back-matter/98-appendix-a-glossary.md#explicit-knowledge) · [Mental Model](../back-matter/98-appendix-a-glossary.md#mental-model) · [Tacit Knowledge](../back-matter/98-appendix-a-glossary.md#tacit-knowledge) · [Truth](../back-matter/98-appendix-a-glossary.md#truth). Definitions are in [Appendix A](../back-matter/98-appendix-a-glossary.md).

<!-- chapter-meta:end -->

---

When I first started building evaluation suites for AI systems, I thought the hard part would be the models. It was not. The hard part was defining what I was evaluating.

I had a benchmark. The benchmark had questions. The questions had answers. The system either produced the right answer or it did not. I could compute a score.

And then I would look at the score and feel that it was measuring something other than what I cared about.

A system that memorized the benchmark scored well. A system that could reason its way to an answer it had never seen scored badly, because it phrased things differently. A system that produced the correct answer for the wrong reason scored perfectly.

I had built a machine that could measure **matching**. I had not built a machine that could measure **knowing**. And I could not build the second until I could say, precisely, what knowing was.

This chapter is that attempt. Not for a benchmark, but for the book—and for the systems I build, and for the way I try to think.

---

## The Target Shapes the Process

We have defined knowledge as the internal, integrated, actionable model of reality that a mind constructs from information. That definition is a skeleton. It needs flesh.

The reason it matters is simple: **the target shapes the process.**

If you think knowledge is a collection of facts, you will build a process for collecting facts—and you will end up with a very large collection of facts and very little understanding. If you think knowledge is a network of tested models, you will build a process for constructing and testing models—and you will end up with something that can predict, explain, and act.

```
   THE TARGET SHAPES THE PROCESS

   IF YOU THINK KNOWLEDGE IS:       YOU WILL BUILD A PROCESS FOR:

   ┌──────────────────────┐         ┌──────────────────────┐
   │  A collection        │         │  Accumulation        │
   │  of facts            │         │  Memorization        │
   └──────────────────────┘         └──────────────────────┘

   ┌──────────────────────┐         ┌──────────────────────┐
   │  A network of        │         │  Construction        │
   │  tested models       │         │  Testing             │
   └──────────────────────┘         └──────────────────────┘

   The two processes produce very different people,
   and very different systems.
```

The history of education, science, and technology is littered with the wreckage of fact-collection mistaken for knowledge. The student who memorizes the periodic table but cannot predict how two elements will react. The manager who has every metric but cannot diagnose why sales are falling. The pundit who has read every headline but cannot explain a single mechanism.

All of them have information. None of them has knowledge.

So let us be precise about what knowledge is.

---

## Knowledge Is a Predictive Model

The most fundamental thing to understand about knowledge is that it is **predictive**. Knowledge is not a mirror held up to reality; it is a **model** that allows a mind to anticipate what will happen next.

This claim has roots in several traditions. The philosopher of science Karl Popper argued that knowledge grows through conjecture and refutation—we propose models, test their predictions, and discard those that fail. The cognitive scientist Karl Friston has argued that the brain is fundamentally a prediction machine, constantly generating expectations and updating them in light of prediction error. The psychologist Gary Klein, studying how experts make decisions under pressure, found that experts do not compare options; they **recognize** situations, because they have internalized models that let them see what is happening and what to do.

In all of these accounts, the core of knowledge is the same: a model that generates **expectations**, which are then tested against reality.

```
   THE KNOWLEDGE LOOP

        ┌─────────────────┐
        │      MODEL      │
        │  (your beliefs  │
        │  about the world)│
        └────────┬────────┘
                 │ generates
                 ▼
        ┌─────────────────┐
        │   PREDICTION    │
        │ (what you expect│
        │  to happen)     │
        └────────┬────────┘
                 │ compared against
                 ▼
        ┌─────────────────┐
        │   OBSERVATION   │
        │ (what actually  │
        │  happens)       │
        └────────┬────────┘
                 │ produces
                 ▼
        ┌─────────────────┐
        │  PREDICTION     │
        │     ERROR       │
        └────────┬────────┘
                 │ updates
                 └──────────► MODEL
```

This loop is the engine of all knowledge, from navigating by the stars to testing a scientific theory. The model need not be conscious. But it must be predictive: it tells you what to expect, and it is corrected when the expectation fails.

The implication is important. **A "fact" that does not feed into any predictive model is not knowledge.** It is information. It may be true, it may be interesting, it may be worth storing somewhere. But it does not become knowledge until it is integrated into a structure that allows you to anticipate, explain, or act.

```
   THE SAME INFORMATION, TWO DIFFERENT STATES

   INFORMATION (not knowledge):
   "Water boils at 100°C at sea level."

   KNOWLEDGE (model-based):
   ┌─────────────────────────────────────────────┐
   │                                             │
   │   Pressure ───► Boiling point ───► Cooking  │
   │      │                              time    │
   │      │                                       │
   │      └──────► Altitude ───► Food safety     │
   │                                             │
   │   The model lets you predict what happens   │
   │   on a mountain, in a pressure cooker, or   │
   │   at a facility where sterilization matters.│
   │                                             │
   └─────────────────────────────────────────────┘
```

The person who knows *that* water boils at 100°C has a fact. The person who has the model can predict what happens when the pressure changes. The first can recite. The second can act.

---

## The Anatomy of a Knowledge Model

If knowledge is a model, what is a model made of? Models vary enormously in content, but they share a common anatomy.

```
 ┌───────────────────────────────────────────────────────┐
 │                    KNOWLEDGE MODEL                    │
 │                                                       │
 │   ENTITIES        RELATIONS         MECHANISMS        │
 │   (what exists)   (how they are     (why they         │
 │                    connected)        interact)        │
 │                                                       │
 │   CONSTRAINTS                     PRIORS              │
 │   (what cannot happen)            (what is usually    │
 │                                    the case)          │
 └───────────────────────────────────────────────────────┘
```

**Entities** are the things the model is about. In a medical model, entities might be organs, pathogens, cells, and symptoms. In an economic model, entities might be buyers, sellers, prices, and goods. In a model of a software system, entities might be services, queues, databases, and callers.

**Relations** are the connections between entities. "Smoking is associated with lung cancer." "When supply falls and demand holds, price rises." Relations are the skeleton of the model.

**Mechanisms** are the causal processes that explain *why* the relations hold. This is the difference between a model that merely correlates and a model that understands. "Smoking causes lung cancer because carcinogens in smoke damage DNA in lung cells, leading to uncontrolled cell division." The mechanism is what makes the knowledge explanatory rather than merely predictive.

**Constraints** are the boundaries of what is possible. A model of physics includes the constraint that nothing travels faster than light. A model of economics includes the constraint that you cannot consume more than you produce indefinitely. Constraints are what allow a model to rule things out—which is often more valuable than ruling things in.

**Priors** are the background assumptions about what is usually the case. In medicine, a prior might be that common diseases are common. In engineering, a prior might be that most failures are ordinary rather than exotic. Priors are not certainties; they are starting points that get updated as evidence arrives.

A good knowledge model has all five components. A model with entities and relations but no mechanisms is a correlation, not an explanation. A model with mechanisms but no constraints is unbounded and cannot rule anything out. A model with no priors must learn everything from scratch, which is impossible.

```
   WHAT HAPPENS WHEN A COMPONENT IS MISSING

   ┌──────────────┬──────────────────────────────────────┐
   │  MISSING     │  CONSEQUENCE                         │
   ├──────────────┼──────────────────────────────────────┤
   │  MECHANISMS  │  Correlation without explanation.    │
   │              │  Predicts, but cannot generalize.    │
   ├──────────────┼──────────────────────────────────────┤
   │  CONSTRAINTS │  Unbounded model. Cannot rule out    │
   │              │  impossible explanations.            │
   ├──────────────┼──────────────────────────────────────┤
   │  PRIORS      │  Must learn everything from data.    │
   │              │  Fails on small samples.             │
   ├──────────────┼──────────────────────────────────────┤
   │  RELATIONS   │  Just a list of entities. Not a      │
   │              │  model at all.                       │
   └──────────────┴──────────────────────────────────────┘
```

The richness of the model determines the richness of the knowledge.

---

## Three Kinds of Knowing

Philosophers have long distinguished between different kinds of knowledge. The most useful distinction for our purposes is between **knowing that**, **knowing how**, and **knowing why**.

### Knowing That (Declarative Knowledge)

**Knowing that** is propositional knowledge—knowledge of facts, claims, and descriptions. This is the kind of knowledge that can be stated in propositions, written down, and transmitted as information.

Knowing that is the most easily acquired form of knowledge. It can be learned from books, lectures, and conversations. It is also the most easily mistaken for knowledge in general—because it is the kind that can be tested on exams, measured by quizzes, and counted in databases.

But knowing that is only one kind of knowledge, and often the least valuable. A medical student who knows that a certain disease causes a certain symptom is not yet a diagnostician. Declarative knowledge is necessary but not sufficient.

### Knowing How (Procedural Knowledge)

**Knowing how** is the knowledge of how to do something—how to ride a bike, how to perform surgery, how to negotiate a contract, how to debug a distributed system. Knowing how is often **tacit**: it cannot be fully articulated in words.

Knowing how is acquired through practice, feedback, and experience. It cannot be transmitted as information. It must be built through repeated action and correction.

### Knowing Why (Explanatory Knowledge)

**Knowing why** is the knowledge of mechanisms and causes—why things happen the way they do. It is the knowledge that connects knowing that to knowing how.

Knowing why is the most powerful form of knowledge because it is the most **transferable**. A principle that explains why something works can be applied to a thousand situations that share the same underlying mechanism. A fact applies only to the case at hand.

```
 ┌──────────────┬────────────────────┬─────────────────────┐
 │  KNOWING     │  WHAT IT IS        │  HOW IT IS ACQUIRED │
 ├──────────────┼────────────────────┼─────────────────────┤
 │  THAT        │  Facts, claims,    │  Reading, listening,│
 │              │  descriptions      │  memorization       │
 ├──────────────┼────────────────────┼─────────────────────┤
 │  HOW         │  Skills, procedures│  Practice, feedback,│
 │              │  (often tacit)     │  apprenticeship     │
 ├──────────────┼────────────────────┼─────────────────────┤
 │  WHY         │  Mechanisms, causes│  Explanation,       │
 │              │  principles        │  experimentation    │
 └──────────────┴────────────────────┴─────────────────────┘
```

This distinction is why my evaluation suite was measuring the wrong thing. It was measuring **knowing that**—whether the system could produce the right string. It was not measuring **knowing why**—whether the system could explain, generalize, or handle a case it had never seen. The benchmark was real. It was just measuring a fragment of the target.

---

## Explicit and Tacit Knowledge

The distinction between explicit and tacit knowledge, introduced by Michael Polanyi, is one of the most important ideas in the study of knowledge. It cuts across the three kinds of knowing and explains why so much of what experts know cannot be captured in a database.

**Explicit knowledge** is knowledge that can be articulated, codified, and transmitted. It is the knowledge of formulas, recipes, manuals, and textbooks.

**Tacit knowledge** is knowledge that cannot be fully articulated. It is the knowledge of skills, intuitions, judgments, and pattern recognition. It is acquired through experience and practice, and it is often invisible even to the person who possesses it.

Polanyi's dictum—"We can know more than we can tell"—captures the essence. The experienced doctor who "just knows" that something is wrong with a patient, the master craftsperson who can feel when a piece of wood is ready, the senior engineer who can smell a bad design—all of them possess knowledge that cannot be fully reduced to explicit rules.

```
  EXPLICIT ─────────────────────────────────── TACIT
  (can be written)                    (must be practiced)

   Formula    Recipe    Diagnostic    Bike     Intuition
                       heuristics     balance  /judgment
     │          │           │           │          │
     ▼          ▼           ▼           ▼          ▼
  Easy to    Easy to    Partly       Hard to    Very hard
  transmit   transmit   transmittable transmit   to transmit
```

This has profound implications for knowledge engineering. It means that **not all knowledge can be captured in information systems**. The most valuable knowledge in any domain—the judgment of the expert, the skill of the craftsperson, the intuition of the navigator—is often the least codifiable. It can only be cultivated through apprenticeship, practice, and feedback.

For the individual, the implication is equally important. Reading about a skill is not the same as acquiring it. The transformation from explicit to tacit knowledge requires **practice**—repeated action, feedback, and correction.

For AI systems, this is a hard boundary. A model trained on text can learn what has been written about a skill. It cannot learn the skill itself. This is why a language model can write fluently about surgery and cannot perform it. The explicit knowledge is in the corpus. The tacit knowledge is in the hands.

---

## The Four Tests of Knowledge

How do we know whether a model is knowledge or merely a belief? How do we evaluate the quality of what we think we know?

There is no single test, but there are four criteria that, taken together, provide a robust standard.

```
 ┌──────────────────────────────────────────────────────┐
 │                 THE FOUR TESTS                       │
 ├──────────────────────────────────────────────────────┤
 │  1. PREDICTIVE  →  Does it anticipate accurately?    │
 │  2. EXPLANATORY →  Does it explain why?              │
 │  3. COHERENT    →  Does it fit with what else we     │
 │                     know?                            │
 │  4. ACTIONABLE  →  Does it guide effective action?   │
 └──────────────────────────────────────────────────────┘
```

### Test 1: Predictive

**Does the model generate accurate predictions?**

This is the most fundamental test. Knowledge is a predictive model, so the first question is whether the predictions hold up. If you believe that a certain change will improve performance, and it does, your model has predictive power. If it consistently fails, your model is wrong—or at least incomplete.

Prediction is not the same as certainty. A model can be predictive without being perfectly accurate. The question is not whether the model is always right, but whether it is **better than chance**—and better than the alternatives.

### Test 2: Explanatory

**Does the model explain why the predictions hold?**

A model that predicts but cannot explain is a black box. It may be useful, but it is fragile. It cannot be generalized to new situations, because you do not know what makes it work. Explanation—mechanism, causation, principle—is what allows knowledge to transfer.

### Test 3: Coherent

**Is the model consistent with other things you know?**

Knowledge is not a collection of isolated models. It is a network. A new model must fit with the existing network—or, if it does not, it must be powerful enough to force a revision of the network. Coherence is the test of integration.

### Test 4: Actionable

**Does the model guide action effectively?**

Knowledge is for something. The final test is whether the model can guide action—whether it can help you decide what to do, solve a problem, or achieve a goal. A model that is predictive, explanatory, and coherent but cannot be used is incomplete.

Not every piece of knowledge needs to pass all four tests with equal strength. A purely theoretical model may be predictive and explanatory but not immediately actionable. A practical skill may be actionable but not fully explanatory. But the more tests a model passes, the more robust it is.

```
   THE FOUR TESTS APPLIED

   ┌─────────────────────┬───────┬───────┬───────┬───────┐
   │  MODEL              │ PRED  │ EXPL  │ COH   │ ACT   │
   ├─────────────────────┼───────┼───────┼───────┼───────┤
   │  "Ice melts above   │  ✓    │  ✗    │  ✓    │  ✓    │
   │   0°C"              │       │       │       │       │
   ├─────────────────────┼───────┼───────┼───────┼───────┤
   │  "Ice melts because │  ✓    │  ✓    │  ✓    │  ✓    │
   │   heat breaks the   │       │       │       │       │
   │   lattice bonds"    │       │       │       │       │
   └─────────────────────┴───────┴───────┴───────┴───────┘

   The first is information. The second is knowledge.
```

This is what my benchmark could not measure. It could measure prediction—did the system produce the right string. It could not measure explanation, coherence, or actionability. A system that scored perfectly on the benchmark might have failed three of the four tests.

---

## Knowledge, Belief, Opinion, and Information

It is useful to place knowledge in a family of related concepts, to see how it differs from its neighbors.

```
 ┌────────────┬─────────────────────────────────────────────┐
 │ CONCEPT    │ CHARACTERISTIC                              │
 ├────────────┼─────────────────────────────────────────────┤
 │ DATA       │ Raw, unprocessed, meaningless in itself     │
 │ INFORMATION│ Structured data with meaning                │
 │ OPINION    │ Subjective judgment or preference           │
 │ BELIEF     │ Assent to a proposition, with or without    │
 │            │ evidence                                    │
 │ KNOWLEDGE  │ Integrated, tested, actionable model        │
 └────────────┴─────────────────────────────────────────────┘
```

The key distinction is between **belief** and **knowledge**. Belief is assent to a proposition—you believe something when you hold it to be true. Knowledge is belief that has been **justified** and **tested**. Not all beliefs are knowledge; some are false, some are unjustified, some are lucky guesses. Knowledge is belief that has survived the tests.

**Opinion** is different again. An opinion is a judgment or preference that is not necessarily truth-apt. "Chocolate is better than vanilla" is an opinion. But opinions can be informed or uninformed, reasoned or unreasoned.

**Information** is the raw material. Knowledge is the product. Information can be true or false; knowledge is information that has been integrated and tested.

---

## The Provisionality of Knowledge

Perhaps the most important thing to understand about knowledge is that it is **provisional**. Knowledge is not certainty. It is the best model we have, given the evidence available, subject to revision when new evidence arrives.

This is not a weakness. It is a strength. The history of science is the history of knowledge being revised—from Newtonian mechanics to relativity, from miasma theory to germ theory. Each revision did not destroy knowledge; it improved it.

But provisionality has implications for how we should hold our knowledge. We should hold it **firmly enough to act**, but **loosely enough to revise**. Hold your beliefs too firmly, and you become dogmatic—unable to see evidence that contradicts you. Hold them too loosely, and you become paralyzed—unable to act because you are always waiting for more evidence.

```
   KNOWLEDGE AS CALIBRATED CONFIDENCE

   Confidence
       ▲
   1.0 │                                    ●●●
       │                              ●●●
   0.8 │                        ●●●
       │                  ●●●
   0.6 │            ●●●
       │      ●●●
   0.4 │ ●●●
       │
   0.2 │
       │
   0.0 └──────────────────────────────────────────►
         Evidence accumulated over time

   As evidence accumulates, confidence should rise—
   but it should never reach absolute certainty.
```

This is the mature attitude toward knowledge. Not "I know for certain," but "I have good reason to believe, and I will revise if the evidence changes." Not "I don't know anything," but "I know enough to act, and I am open to learning more."

---

## What Knowledge Is Not

It is often clarifying to say what something is *not*.

**Knowledge is not a database.** A database can store information, but it cannot know anything. Knowledge requires a mind—a knower—that constructs, tests, and applies models.

**Knowledge is not a list of facts.** You can memorize a thousand facts and still not understand anything. Knowledge is the integration of facts into models, not the accumulation of facts in isolation.

**Knowledge is not certainty.** Certainty is the absence of doubt. Knowledge is the presence of justified confidence. The person who is certain cannot learn, because they have closed themselves off from evidence.

**Knowledge is not information.** Information is external, transferable, and passive. Knowledge is internal, constructed, and active. The confusion between them is the central error of the information age.

**Knowledge is not just true belief.** A true belief held for the wrong reasons—a lucky guess, a superstition that happens to be correct—is not knowledge. Knowledge requires justification, evidence, and understanding of why the belief is true.

---

## Implications for the Process

We have now described the target in detail. What does this mean for the process of acquiring knowledge?

**First, the process must aim at models, not facts.** It is not enough to collect information. The information must be integrated into structures that can predict, explain, and guide action. This means that the process must include **synthesis**—the construction of models from information.

**Second, the process must include testing.** Knowledge is a predictive model, so the process must include **prediction and verification**. Beliefs must be exposed to reality, and revised when they fail.

**Third, the process must include practice.** Much knowledge is tacit, and tacit knowledge cannot be acquired by reading. It must be acquired by doing. This means that the process must include **application**.

**Fourth, the process must include explanation.** Knowing why is more powerful than knowing that. The process must seek **mechanisms**—not just what happens, but why.

**Fifth, the process must be provisional.** Knowledge is always subject to revision. The process must include **humility**—a willingness to change one's mind when evidence warrants.

The pipeline that we will describe in the chapters that follow is designed to meet these requirements. It is a process for building models that are predictive, explanatory, coherent, and actionable—and for holding them provisionally, subject to revision.

```
   THE TARGET, REDUCED TO ONE SENTENCE

   ┌─────────────────────────────────────────────────────┐
   │                                                     │
   │   Knowledge is a model that predicts, explains,     │
   │   coheres, and guides action—and that is held       │
   │   with the humility to be revised.                  │
   │                                                     │
   │   Anything less is information.                     │
   │   Anything more is wisdom.                          │
   │                                                     │
   └─────────────────────────────────────────────────────┘
```

---

## A Return to the Benchmark

I still use benchmarks. They are useful tools. But I no longer mistake them for the target.

When I build an evaluation suite now, I try to measure all four tests. Not just whether the system produces the right answer, but whether it can explain it, whether it is consistent with what we know, and whether it can help someone act.

The scores are lower. The systems look worse. But the scores are measuring something closer to knowledge—and the systems that score well are the ones I would actually trust.

That is the lesson of this chapter. The target shapes the process. If you want to build knowledge—in a mind, in a system, in an organization—you must first be precise about what you are trying to build. The precision is not pedantry. It is the difference between a benchmark and a knowing.

---

## Chapter Summary

- **Knowledge is a predictive model.** It is not a mirror of reality but a simplified representation that allows a mind to anticipate, explain, and act.
- The **knowledge loop**—model → prediction → observation → error → update—is the engine of all knowledge.
- A knowledge model has an anatomy: **entities, relations, mechanisms, constraints, and priors**. The richness of the model determines the richness of the knowledge.
- There are **three kinds of knowing**: **knowing that** (declarative), **knowing how** (procedural, often tacit), and **knowing why** (explanatory). Full knowledge usually requires all three.
- **Explicit knowledge** can be articulated and transmitted. **Tacit knowledge** cannot; it must be acquired through practice and apprenticeship.
- The **four tests of knowledge** are: **predictive**, **explanatory**, **coherent**, and **actionable**.
- Knowledge differs from **data, information, opinion, and belief**. Knowledge is belief that has been justified and tested.
- Knowledge is **provisional**. It is not certainty but calibrated confidence, subject to revision as evidence accumulates.
- Knowledge is **not** a database, a list of facts, certainty, information, or mere true belief.
- The **implications for the process** are: aim at models, not facts; include testing; include practice; include explanation; and remain provisional.

---

**Next Chapter:** *The Knower — How Brains Build Knowledge* — a journey into the cognitive machinery that makes knowledge possible, from attention and perception to prediction, memory, and the pruning of neural circuits.

---

<!-- book-nav:start -->

---

[← Chapter 4](../part-2-the-foundations/04-the-raw-material.md) | [Contents](../README.md) | [Chapter 6 →](../part-2-the-foundations/06-the-knower.md)

<!-- book-nav:end -->
