# Chapter 21: Context Engineering for Humans and Machines

---

I once made a retrieval system worse by giving it better evidence.

The system was answering questions about a product API. The retrieval was already good—we were hitting the right documents about ninety percent of the time. The answers were still mediocre. The model had the right evidence and produced the wrong conclusions.

My fix was to retrieve more. I widened the candidate pool, added a second retriever, and passed the top fifteen documents to the model instead of the top five. I assumed that more evidence would produce better answers. The evidence was good. The answers should improve.

They got worse.

Not because the extra documents were irrelevant—they were all relevant. Because the *ordering* changed. The most important document—the one that contained the exception to the general rule, the one that actually answered the question—was now buried at position twelve. By the time the model reached it, it had already committed to a narrative built from the first five documents, all of which described the general case.

The model did not lack evidence. It lacked the evidence *at the right moment*, in the right place, in the right form. The context was not a bucket. It was a sequence. And the sequence mattered.

I had been thinking of context as a container to fill. I needed to think of it as a design surface.

This chapter is about that shift. It is about context engineering—the discipline of selecting, structuring, and delivering information to a consumer, human or machine, in a way that maximizes understanding and minimizes cognitive load.

---

## Context Is Not a Container

The most common mistake in context engineering is treating context as a container. You have a context window (or a working memory, or a meeting agenda), and your job is to fill it with information. More information means more context. More context means better answers.

This is wrong in both directions.

For a machine, the context window is a **sequence** with position-dependent attention. Evidence at the beginning and end is weighted differently than evidence in the middle. The ordering is a design variable, not a storage decision.

For a human, working memory is a **bottleneck** with fragile attention and finite capacity. More information means more load, and more load means degraded processing. The capacity is a constraint, not a target.

```
   CONTEXT AS CONTAINER VS. CONTEXT AS DESIGN SURFACE

   CONTAINER MENTALITY             DESIGN SURFACE MENTALITY
   ┌──────────────────────┐        ┌──────────────────────┐
   │                      │        │                      │
   │  Fill it up.         │        │  Design it.          │
   │                      │        │                      │
   │  More = better.      │        │  Better = better.    │
   │                      │        │                      │
   │  Order doesn't       │        │  Order is a design   │
   │  matter.             │        │  variable.           │
   │                      │        │                      │
   │  One consumer.       │        │  Different consumers │
   │                      │        │  need different      │
   │                      │        │  designs.            │
   │                      │        │                      │
   │  Success = coverage. │        │  Success = behavior. │
   │                      │        │                      │
   └──────────────────────┘        └──────────────────────┘
```

The shift from container to design surface is the central move of context engineering. Once you make it, the questions change. You stop asking "do I have enough information?" and start asking "is this information structured to produce the behavior I want, from the consumer I'm designing for, at the moment it's needed?"

---

## Why Context Determines Behavior

The reason context engineering matters is simple: **context determines behavior**.

For a human, context shapes what you notice, what you interpret, and what you decide. The same facts, presented in a different frame, produce a different judgment. This is one of the most robust findings in cognitive psychology, and it applies to everything from medical diagnosis to hiring decisions to investment choices.

For a machine, the dependence is even more acute. A language model has no persistent memory, no grounded understanding of the world, no stable identity. It has only the context it is given. The context is the model's entire world. Change the context, and you change the model's behavior.

```
   THE SAME INFORMATION, DIFFERENT CONTEXTS

   CONTEXT A                        CONTEXT B
   ┌──────────────────────┐        ┌──────────────────────┐
   │                      │        │                      │
   │  "This treatment    │        │  "This treatment     │
   │   has a 30% success │        │   has a 70% failure  │
   │   rate."             │        │   rate."             │
   │                      │        │                      │
   └──────────────────────┘        └──────────────────────┘
              │                              │
              ▼                              ▼
   ┌──────────────────────┐        ┌──────────────────────┐
   │  Judged as more      │        │  Judged as less      │
   │  favorable.          │        │  favorable.          │
   │  (Same underlying    │        │  (Same underlying    │
   │   probability.)      │        │   probability.)      │
   └──────────────────────┘        └──────────────────────┘

   The information is identical.
   The context is not.
   The behavior differs.
```

This is why context engineering matters. It is the lever that controls performance. If you want better outputs, you need better context. If you want more reliable knowledge, you need more carefully designed information environments.

---

## What Context Engineering Is

**Context engineering** is the discipline of designing the information environment in which a cognitive system—human or machine—operates.

It is broader than prompt engineering. Prompt engineering is the craft of writing instructions for a language model. Context engineering includes the instructions, but also the retrieval, the structure, the ordering, the tools, the memory, the interaction, and the governance.

It is broader than information architecture. Information architecture is the design of information spaces—websites, databases, documents. Context engineering is the design of **cognitive environments**—the conditions under which thinking happens.

It is broader than user experience design. UX design is about making interfaces usable. Context engineering is about making **cognition effective**—structuring information so that it can be understood, integrated, and acted upon.

```
 ┌───────────────────────────────────────────────────────┐
 │              WHAT CONTEXT ENGINEERING IS              │
 ├───────────────────────────────────────────────────────┤
 │  It is:                                               │
 │    • Designing the information environment            │
 │    • Selecting and structuring information            │
 │    • Ordering it for the consumer                     │
 │    • Framing tasks and goals                          │
 │    • Managing memory and tools                        │
 │    • Grounding claims in evidence                     │
 │                                                       │
 │  It is not:                                           │
 │    • Just prompt engineering                          │
 │    • Just information architecture                    │
 │    • Just UX design                                   │
 │    • A one-time activity                              │
 │    • A synonym for "more context"                     │
 └───────────────────────────────────────────────────────┘
```

The goal of context engineering is to **maximize understanding and minimize cognitive load**. It is to give the cognitive system—human or machine—the information it needs, in the form it needs, in the order it needs it, at the time it needs it, so that it can perform at its best.

---

## The Seven Layers of Context

Context is not a single thing. It has seven layers, each of which must be designed.

```
 ┌───────────────────────────────────────────────────────────────┐
 │                                                               │
 │   ┌───────────────────────────────────────────────────────┐   │
 │   │                   GOVERNANCE                          │   │
 │   │  ┌─────────────────────────────────────────────────┐  │   │
 │   │  │                 INTERACTION                     │  │   │
 │   │  │  ┌───────────────────────────────────────────┐  │  │   │
 │   │  │  │               EXECUTION                   │  │  │   │
 │   │  │  │  ┌─────────────────────────────────────┐  │  │  │   │
 │   │  │  │  │              MEMORY                 │  │  │  │   │
 │   │  │  │  │  ┌───────────────────────────────┐  │  │  │  │   │
 │   │  │  │  │  │            TOOL               │  │  │  │  │   │
 │   │  │  │  │  │  ┌─────────────────────────┐  │  │  │  │  │   │
 │   │  │  │  │  │  │       RETRIEVAL         │  │  │  │  │  │   │
 │   │  │  │  │  │  │  ┌───────────────────┐  │  │  │  │  │  │   │
 │   │  │  │  │  │  │  │    INSTRUCTION    │  │  │  │  │  │  │   │
 │   │  │  │  │  │  │  └───────────────────┘  │  │  │  │  │  │   │
 │   │  │  │  │  │  └─────────────────────────┘  │  │  │  │  │   │
 │   │  │  │  │  └───────────────────────────────┘  │  │  │  │   │
 │   │  │  │  └─────────────────────────────────────┘  │  │  │   │
 │   │  │  └───────────────────────────────────────────┘  │  │   │
 │   │  └─────────────────────────────────────────────────┘  │   │
 │   └───────────────────────────────────────────────────────┘   │
 │                                                               │
 └───────────────────────────────────────────────────────────────┘
```

**Instruction context** is the task, goal, or question. It frames everything else.

**Retrieval context** is the information selected and provided. It is the raw material.

**Tool context** is the capabilities available—APIs, search, computation, code execution.

**Memory context** is the history of prior interactions. It is the continuity.

**Execution context** is the constraints—token limits, time limits, safety rules, temperature.

**Interaction context** is the social and communicative environment—who is involved, what is expected.

**Governance context** is the norms, rules, and accountability structures.

The layers are nested. Every layer matters. A failure at any layer can derail the whole system.

```
   THE SEVEN LAYERS FOR HUMANS AND MACHINES

   ┌─────────────┬──────────────────────┬──────────────────────┐
   │  LAYER      │  HUMAN EQUIVALENT    │  MACHINE EQUIVALENT  │
   ├─────────────┼──────────────────────┼──────────────────────┤
   │ INSTRUCTION │  The question        │  The prompt          │
   │ RETRIEVAL   │  The evidence        │  The retrieved docs  │
   │ TOOL        │  Calculator, search  │  Function calls, API │
   │ MEMORY      │  Experience, notes   │  Conversation history│
   │ EXECUTION   │  Deadline, budget    │  Token limit, temp   │
   │ INTERACTION │  Meeting, audience   │  Chat interface      │
   │ GOVERNANCE  │  Ethics, policy      │  Safety guidelines   │
   └─────────────┴──────────────────────┴──────────────────────┘
```

The layers are the same for both consumers. The content is different. The discipline is the same.

---

## The Signal-to-Noise Ratio Within the Window

We discussed signal and noise in Chapter 4. Here we apply it to the context window itself.

A context window is not homogeneous. Within it, some information is signal—it bears on the question, it is accurate, it changes the answer. Some is noise—it is irrelevant, misleading, or redundant. The ratio between them determines the quality of the output.

```
   SIGNAL AND NOISE WITHIN THE CONTEXT WINDOW

   HIGH SIGNAL CONTEXT              LOW SIGNAL CONTEXT
   ┌──────────────────────┐        ┌──────────────────────┐
   │                      │        │                      │
   │  ████████████████    │        │  ░░░░░░░░░░░░░░░░    │
   │  ████████████████    │        │  ░░░░░█░░░░░░░░░░    │
   │  ████████████████    │        │  ░░░░░░░░░░░█░░░░    │
   │                      │        │  ░░░░░░░░░░░░░░░░    │
   │                      │        │  ░░░░░░░░░░░░░░░░    │
   └──────────────────────┘        └──────────────────────┘
                                              ▲
                                              │
                                     The signal is
                                     in there somewhere.

   The model receives clean        The model receives noise
   evidence and produces           and produces a plausible
   a grounded answer.              answer built from noise.
```

This is what I got wrong with my retrieval system. The fifteen documents were all relevant. But their signal-to-noise ratio *within the context* was low, because most of the content was background, caveats, and examples that did not bear on the specific question. The model had to do its own filtering, and it did not always do it well.

The fix was to **structure the retrieval**, not just rank it. I added a pre-processing step that extracted the key claim from each document, the evidence for it, and the conditions under which it applied. The model received fifteen documents' worth of claims and evidence instead of fifteen documents' worth of text. The signal-to-noise ratio improved. The answers improved.

For a human, the same principle applies. A briefing memo with three pages of background and one paragraph of recommendation has a lower signal-to-noise ratio than a memo with the recommendation first, the evidence second, and the background in an appendix. The information is the same. The design is different. The behavior differs.

---

## The Ordering Problem

Here is the thing that most context engineering advice misses: **ordering is a design variable.**

For a machine, the ordering of the context window affects attention. Evidence at the beginning and end is weighted differently from evidence in the middle. This is a well-documented property of transformer models. If you put the most important evidence at position twelve, the model may not use it as effectively as if you put it at position one.

For a human, the ordering affects primacy and recency. The first things you read set the frame. The last things you read are what you remember. The middle is where things get lost. This is why the executive summary exists, and why it is not a formality.

```
   ORDERING EFFECTS

   POSITION     MACHINE ATTENTION       HUMAN RECALL
   ─────────────────────────────────────────────────
   First        High                   High (primacy)
   Middle       Lower                  Low
   Last         High                   High (recency)

   ┌─────────────────────────────────────────────────────┐
   │                                                     │
   │   ATTENTION/RECALL                                  │
   │                                                     │
   │   ████                                              │
   │   ████                                              │
   │   ████                                              │
   │   ████                                              │
   │   ███                                               │
   │   ██                                                │
   │   ██                                                │
   │   ███                                               │
   │   ████                                              │
   │   ████                                              │
   │   ████                                              │
   │   └──────────────────────────────────────────────►  │
   │    1    2    3    4    5    6    7    8    9   10   │
   │                                                     │
   │   The curve is not flat. The middle is a valley.    │
   │                                                     │
   └─────────────────────────────────────────────────────┘
```

The implication is that **the most important evidence should be at the boundaries, not buried in the middle.** For machines, put critical evidence first and last, and summarize the rest. For humans, use the same principle: lead with the conclusion, support it with evidence, close with the implication.

This is the fix I made to my retrieval system. I did not just reduce the number of documents. I **re-ordered** them. The most critical evidence went first. The second-most critical went last. The middle was supporting context, examples, and caveats. The answers improved immediately.

```
   BEFORE AND AFTER REORDERING

   BEFORE                           AFTER
   ┌──────────────────────┐        ┌──────────────────────┐
   │ 1. Background        │        │ 1. Key evidence      │
   │ 2. Background        │        │ 2. Supporting        │
   │ 3. Example           │        │ 3. Caveat            │
   │ 4. Background        │        │ 4. Supporting        │
   │ 5. Caveat            │        │ 5. Example           │
   │ 6. Supporting        │        │ 6. Key claim         │
   │ 7. Background        │        │ 7. Key exception     │
   │ 8. Example           │        │                      │
   │ 9. Background        │        │                      │
   │ 10. Key evidence     │        │                      │
   │ 11. Key claim        │        │                      │
   │ 12. Key exception    │        │                      │
   │ 13. Background       │        │                      │
   │ 14. Supporting       │        │                      │
   │ 15. Caveat           │        │                      │
   └──────────────────────┘        └──────────────────────┘

   The critical evidence           The critical evidence
   is at position 10-12.           is at position 1, 6, 7.
   It gets lost.                   It gets used.
```

This is a small insight, but it is the difference between a system that works and a system that doesn't. And it applies as much to a briefing for a CEO as to a prompt for a model.

---

## The Grounding Problem

For machines, there is a layer of context engineering that does not have a human equivalent: **grounding**.

A language model has no direct access to the world. It has access to text about the world. When it answers a question, it is generating text that is statistically plausible given the context, not text that is necessarily true. This is why hallucination is a structural property of language models, not a bug.

Grounding is the work of connecting the model's output to something external—retrieved documents, a knowledge base, a verifiable source. The model does not know whether it is right. Grounding is how we check.

```
 ┌───────────────────────────────────────────────────────┐
 │              THE GROUNDING PROBLEM                    │
 ├───────────────────────────────────────────────────────┤
 │                                                       │
 │   Model alone:                                        │
 │     "The capital of France is Lyon."                  │
 │     (Confident, fluent, false.)                       │
 │                                                       │
 │   Model + retrieval:                                  │
 │     "According to [source], the capital of France     │
 │      is Paris."                                       │
 │     (Grounded, verifiable, checkable.)                │
 │                                                       │
 └───────────────────────────────────────────────────────┘
```

The grounding problem has no human equivalent because humans have direct access to the world. But there is an analogy: humans can also generate confident, fluent, false claims, especially when they are reasoning from memory rather than evidence. The cure is the same—grounding in evidence, verifiable sources, and the discipline of testing.

Context engineering for machines must include grounding. Context engineering for humans can include it too—by making evidence explicit, by citing sources, by separating claims from support.

---

## Context Engineering for Humans

How do you engineer context for humans? The principles are different from those for machines, because humans have different capacities and limitations.

### Principle 1: Reduce Cognitive Load

The first principle is **reduce cognitive load**. The human working memory is limited. Context engineering for humans must minimize the amount of information that must be held in mind at once.

```
 ┌───────────────────────────────────────────────────────┐
 │              REDUCE COGNITIVE LOAD                    │
 ├───────────────────────────────────────────────────────┤
 │  • CHUNKING: group information into units             │
 │  • STRUCTURING: organize into hierarchies             │
 │  • SIGNALING: highlight what matters                  │
 │  • OFFLOADING: externalize into notes and tools       │
 └───────────────────────────────────────────────────────┘
```

### Principle 2: Support Predictive Processing

The second principle is **support predictive processing**. The human brain is a prediction engine. It works best when it can generate expectations and check them against reality.

```
 ┌───────────────────────────────────────────────────────┐
 │              SUPPORT PREDICTIVE PROCESSING            │
 ├───────────────────────────────────────────────────────┤
 │  • PROVIDE CONTEXT: background for expectations       │
 │  • USE FAMILIAR STRUCTURES: match mental models       │
 │  • PROVIDE FEEDBACK: confirm or correct predictions   │
 └───────────────────────────────────────────────────────┘
```

### Principle 3: Match the Mode of Representation

The third principle is **match the mode of representation**. Different kinds of information are best represented in different ways.

```
 ┌───────────────────────────────────────────────────────┐
 │              MATCH THE MODE OF REPRESENTATION         │
 ├───────────────────────────────────────────────────────┤
 │  TEXT      →  sequential, logical information         │
 │  DIAGRAMS  →  structural, spatial information         │
 │  TABLES    →  comparative information                 │
 │  CHARTS    →  quantitative information                │
 │  NARRATIVES→  causal, temporal information            │
 └───────────────────────────────────────────────────────┘
```

### Principle 4: Design for Attention

The fourth principle is **design for attention**. Human attention is limited and fragile. Context engineering for humans must protect attention and direct it to what matters.

```
 ┌───────────────────────────────────────────────────────┐
 │              DESIGN FOR ATTENTION                     │
 ├───────────────────────────────────────────────────────┤
 │  • MINIMIZE DISTRACTIONS                              │
 │  • USE VISUAL HIERARCHY                               │
 │  • CREATE FOCUS                                       │
 │  • RESPECT COGNITIVE RHYTHMS                          │
 └───────────────────────────────────────────────────────┘
```

### Principle 5: Order for Primacy and Recency

The fifth principle is **order for primacy and recency**. Put the most important information first and last. Put supporting information in the middle.

```
 ┌───────────────────────────────────────────────────────┐
 │              ORDER FOR PRIMACY AND RECENCY            │
 ├───────────────────────────────────────────────────────┤
 │                                                       │
 │  FIRST:   Conclusion, recommendation, key claim       │
 │  MIDDLE:  Supporting evidence, examples, caveats      │
 │  LAST:    Implication, next step, exception           │
 │                                                       │
 │  The middle is where things get lost. Don't bury      │
 │  the critical evidence there.                         │
 │                                                       │
 └───────────────────────────────────────────────────────┘
```

---

## Context Engineering for Machines

How do you engineer context for machines? The principles are different, because machines have different capabilities and limitations.

### Principle 1: Be Explicit

The first principle is **be explicit**. Machines do not infer context the way humans do. Everything they need must be stated.

```
 ┌───────────────────────────────────────────────────────┐
 │              BE EXPLICIT                              │
 ├───────────────────────────────────────────────────────┤
 │  • STATE THE TASK CLEARLY                             │
 │  • SPECIFY THE FORMAT                                 │
 │  • PROVIDE EXAMPLES                                   │
 │  • DEFINE CONSTRAINTS                                 │
 └───────────────────────────────────────────────────────┘
```

### Principle 2: Manage the Context Window

The second principle is **manage the context window**. Machines have a limited window—a maximum amount of text they can process at once. Context engineering for machines must fit within this window.

```
 ┌───────────────────────────────────────────────────────┐
 │              MANAGE THE CONTEXT WINDOW                │
 ├───────────────────────────────────────────────────────┤
 │  • PRIORITIZE INFORMATION                             │
 │  • COMPRESS INFORMATION                               │
 │  • REMOVE REDUNDANCY                                  │
 │  • USE RETRIEVAL                                      │
 │  • ORDER FOR ATTENTION                                │
 └───────────────────────────────────────────────────────┘
```

### Principle 3: Provide Structure

The third principle is **provide structure**. Machines work better with structured information than with unstructured text.

```
 ┌───────────────────────────────────────────────────────┐
 │              PROVIDE STRUCTURE                        │
 ├───────────────────────────────────────────────────────┤
 │  • USE DELIMITERS                                     │
 │  • USE HEADERS                                        │
 │  • USE LISTS                                          │
 │  • USE SCHEMAS                                        │
 └───────────────────────────────────────────────────────┘
```

### Principle 4: Ground the Model

The fourth principle is **ground the model**. Machines can hallucinate. Context engineering for machines must ground the model in reliable information.

```
 ┌───────────────────────────────────────────────────────┐
 │              GROUND THE MODEL                         │
 ├───────────────────────────────────────────────────────┤
 │  • PROVIDE SOURCES                                    │
 │  • REQUIRE CITATIONS                                  │
 │  • VERIFY OUTPUTS                                     │
 │  • USE RETRIEVAL-AUGMENTED GENERATION                 │
 └───────────────────────────────────────────────────────┘
```

### Principle 5: Order for Attention

The fifth principle is **order for attention**. The context window has position-dependent attention. Put critical evidence at the beginning and end. Put supporting material in the middle.

```
 ┌───────────────────────────────────────────────────────┐
 │              ORDER FOR ATTENTION                      │
 ├───────────────────────────────────────────────────────┤
 │                                                       │
 │  FIRST:   Task instruction, key evidence              │
 │  MIDDLE:  Supporting documents, examples, caveats     │
 │  LAST:    Critical exception, final instruction       │
 │                                                       │
 │  The middle of the window is an attention valley.     │
 │  Do not bury the critical evidence there.             │
 │                                                       │
 └───────────────────────────────────────────────────────┘
```

---

## The Two Consumers, Side by Side

The principles for humans and machines are different, but they share a common logic. Both require selection, structure, ordering, grounding, and attention design. The content differs. The discipline is the same.

```
 ┌──────────────────┬─────────────────────┬─────────────────────┐
 │  DESIGN CHOICE   │  HUMAN CONSUMER     │  MACHINE CONSUMER   │
 ├──────────────────┼─────────────────────┼─────────────────────┤
 │  SELECTION       │  Relevance to the   │  Retrieval ranking  │
 │                  │  decision           │  + metadata         │
 ├──────────────────┼─────────────────────┼─────────────────────┤
 │  STRUCTURE       │  Headings, chunks,  │  Delimiters, schemas│
 │                  │  visual hierarchy   │  sections           │
 ├──────────────────┼─────────────────────┼─────────────────────┤
 │  ORDERING        │  Conclusion first,  │  Key evidence first │
 │                  │  evidence middle,   │  and last, support  │
 │                  │  implication last   │  in middle          │
 ├──────────────────┼─────────────────────┼─────────────────────┤
 │  GROUNDING       │  Cited sources,     │  Retrieved docs,    │
 │                  │  verifiable claims  │  citations          │
 ├──────────────────┼─────────────────────┼─────────────────────┤
 │  ATTENTION       │  Visual hierarchy,  │  Position-aware     │
 │                  │  minimal load       │  ordering           │
 ├──────────────────┼─────────────────────┼─────────────────────┤
 │  FEEDBACK        │  Questions, checks, │  Verification,      │
 │                  │  iteration          │  evaluation         │
 └──────────────────┴─────────────────────┴─────────────────────┘
```

The table is not a checklist. It is a reminder that context engineering is a **design problem**—and that the design choices depend on the consumer.

---

## A Worked Example: The Decision Memo

Let me return to the executive briefing that went wrong.

A manager needs to decide whether to approve a new product launch. The context engineer—the person preparing the information—designs a decision memo.

```
 ┌───────────────────────────────────────────────────────┐
 │              DECISION MEMO CONTEXT                    │
 ├───────────────────────────────────────────────────────┤
 │  INSTRUCTION:  "Should we launch Product X in Q3?"    │
 │  RETRIEVAL:    market research, financials,           │
 │                competitors, customer feedback         │
 │  TOOL:         budget, team, timeline                 │
 │  MEMORY:       prior launches, lessons learned        │
 │  EXECUTION:    deadline, budget limit, regulations    │
 │  INTERACTION:  executive summary, options,            │
 │                recommendation                         │
 │  GOVERNANCE:   values, risk tolerance, legal          │
 └───────────────────────────────────────────────────────┘
```

The memo is structured to support the decision:

```
 ┌───────────────────────────────────────────────────────┐
 │              THE DECISION MEMO                        │
 ├───────────────────────────────────────────────────────┤
 │                                                       │
 │  1. RECOMMENDATION (first)                            │
 │     "Launch in Q3 with a phased rollout."             │
 │                                                       │
 │  2. KEY EVIDENCE (early)                              │
 │     • Market demand                                   │
 │     • Competitive position                            │
 │     • Financial projection                            │
 │                                                       │
 │  3. RISKS AND CAVEATS (middle)                        │
 │     • Integration risk                                │
 │     • Staffing constraints                            │
 │     • Regulatory uncertainty                          │
 │                                                       │
 │  4. ALTERNATIVES (middle)                             │
 │     • Delay to Q4                                     │
 │     • Launch without phased rollout                   │
 │                                                       │
 │  5. IMPLICATION (last)                                │
 │     "If we wait, competitor X launches first."        │
 │                                                       │
 └───────────────────────────────────────────────────────┘
```

The recommendation is first. The evidence is early. The caveats and alternatives are in the middle. The implication is last.

This structure is not cosmetic. It is designed for primacy and recency. It is designed to reduce cognitive load by leading with the conclusion. It is designed to support the reader's predictive processing by giving them the frame before the details.

The same principle applies to the machine. If the task is a question-answering task, the critical evidence goes first. If the task is a summarization task, the document goes first and the instruction goes last.

---

## AI-Specific Risks

We have discussed context engineering for humans and machines. Now let us examine the risks that are specific to AI.

```
 ┌───────────────────────────────────────────────────────┐
 │              AI-SPECIFIC CONTEXT RISKS                │
 ├───────────────────────────────────────────────────────┤
 │  CONTEXT POISONING  →  wrong or misleading info       │
 │                        in the context                 │
 │  CONTEXT DISTRACTION→  too much irrelevant info       │
 │                        in the context                 │
 │  CONTEXT CONFUSION  →  conflicting info in the        │
 │                        context                        │
 │  ATTENTION DILUTION →  critical info buried in the    │
 │                        middle                         │
 │  GROUNDING FAILURE  →  model generates without        │
 │                        evidence                       │
 └───────────────────────────────────────────────────────┘
```

**Context poisoning.** The retrieved documents contain false or misleading information. The model faithfully reproduces it. The fix is provenance and source quality, not better prompting.

**Context distraction.** The context window is filled with irrelevant information. The model's attention is spread across noise. The fix is selection and pruning.

**Context confusion.** The context contains conflicting information. The model generates a synthesis that is internally consistent and factually wrong. The fix is contradiction resolution and ordering.

**Attention dilution.** The critical evidence is buried in the middle of the context. The model's attention has degraded by the time it reaches it. The fix is reordering.

**Grounding failure.** The model generates an answer that is not supported by the evidence. The fix is requiring citations and verifying outputs.

These risks are not hypothetical. They are the failure modes I have seen most often in production systems. And they are all context engineering problems, not model problems.

---

## A Return to the Retrieval System

I did not fix my retrieval system by adding more evidence. I fixed it by designing the context.

I reordered the documents so the critical evidence was first and last. I extracted key claims and evidence from each document instead of passing raw text. I added a pre-processing step that removed redundant background. I required the model to cite the evidence it used. I tested the system on a set of questions it had never seen.

The scores improved. Not dramatically—from mediocre to good, not from good to excellent. But the improvement was real, and it came from context engineering, not from a better model.

The lesson is the same for human and machine consumers. Context is not a container. It is a design surface. The information is the material. The structure, the ordering, the grounding, and the framing are the design. And the design determines the behavior.

This is the lesson of Chapter 21. The quality of the output depends not just on the capabilities of the system, but on the context in which those capabilities are applied. The knowledge engineer designs the context deliberately—for humans and machines—to maximize understanding and minimize cognitive load.

---

## Chapter Summary

- **Context engineering** is the discipline of designing the information environment in which a cognitive system—human or machine—operates. It is broader than prompt engineering, information architecture, or UX design.
- Context determines behavior. For humans, context shapes perception, interpretation, memory, and decision-making. For machines, context is the only input—it determines behavior.
- The **seven layers of context** are: **instruction, retrieval, tool, memory, execution, interaction, and governance**.
- The layers are nested. Every layer matters. A failure at any layer can derail the whole system.
- **Signal-to-noise ratio within the context window** matters as much as signal-to-noise ratio in selection.
- **Ordering is a design variable.** Evidence at the beginning and end is weighted differently from evidence in the middle. The most important evidence should not be buried.
- **Grounding** is the work of connecting the model's output to something external. It has no exact human equivalent but is essential for machines.
- **Context engineering for humans** includes reducing cognitive load, supporting predictive processing, matching the mode of representation, designing for attention, and ordering for primacy and recency.
- **Context engineering for machines** includes being explicit, managing the context window, providing structure, grounding the model, and ordering for attention.
- **AI-specific risks** include context poisoning, context distraction, context confusion, attention dilution, and grounding failure.
- The lesson of the **retrieval system** is that context is not a container. It is a design surface. The information is the material. The structure, ordering, and grounding are the design.

---

**Next Chapter:** *AI as a Knowledge Partner — Using Large Language Models in the Pipeline* — a detailed examination of how to use AI tools as partners in the knowledge pipeline, including their capabilities, their limitations, and the strategies for working with them effectively.

---

<!-- book-nav:start -->

---

[← Chapter 20](../part-5-the-tools/20-personal-knowledge-management.md) | [Contents](../README.md) | [Chapter 22 →](../part-5-the-tools/22-ai-as-a-knowledge-partner.md)

<!-- book-nav:end -->
