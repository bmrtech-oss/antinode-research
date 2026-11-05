# Chapter 2: Information Is Not Knowledge

<!-- chapter-meta:start -->

**Level:** Beginner

> **Key Terms:** [Data](../back-matter/98-appendix-a-glossary.md#data) · [Epistemology](../back-matter/98-appendix-a-glossary.md#epistemology) · [Information](../back-matter/98-appendix-a-glossary.md#information) · [Knowledge](../back-matter/98-appendix-a-glossary.md#knowledge). Definitions are in [Appendix A](../back-matter/98-appendix-a-glossary.md).

<!-- chapter-meta:end -->

---

Last year I watched a retrieval system do something I still think about.

A user asked it a question about a database schema. The system retrieved three documents, ranked them by relevance, and passed them to a language model. The model produced a fluent, confident answer. The user thanked it and moved on.

The answer was wrong. Not because the retrieval was bad, and not because the model was bad, but because the model had been given *information* and had been asked for *knowledge*, and it had no way to tell the difference.

The documents contained the facts. The facts were accurate. The answer used the facts. And still the answer was wrong—because the model had assembled the facts into a model that did not correspond to how the system actually worked. It had information. It did not have knowledge.

That gap—between having the facts and understanding the thing—is the subject of this chapter. It is the most important distinction in this book, and it is the one most often blurred.

---

## Two Words We Use Interchangeably

We say "I have information about X" and "I have knowledge about X" as if they meant the same thing. We talk about "information workers" and "knowledge workers" as synonyms. We describe the internet as a repository of knowledge when it is, more accurately, a repository of information.

This confusion is not harmless. It leads to a fundamental misunderstanding of what is scarce and what is abundant, what is cheap and what is expensive, what can be stored and what must be built. It leads people to believe that because they have access to information, they therefore possess knowledge. And that belief is false.

It is also the belief that underlies most of the failures I see in AI systems. A model is given information and expected to produce knowledge. Sometimes it does. Often it produces something that *looks* like knowledge—fluent, structured, confident—but is actually a plausible-sounding assembly of information that does not correspond to reality.

To build systems that do better—and to become people who do better—we need to be precise about the difference.

---

## What Information Is

**Information is data that has been organized, structured, or contextualized so that it carries meaning.**

Raw data is not information. The string `3.14159` is data. If I tell you those digits represent the ratio of a circle's circumference to its diameter, the data becomes information. It now has meaning. It can be understood, communicated, and used.

Information has several characteristics that distinguish it from knowledge:

**It is external.** Information exists outside the mind. It can be stored in books, transmitted over networks, encoded in bits. It is, in principle, independent of any particular knower. The information that water boils at 100°C at sea level exists whether or not anyone knows it.

**It is transferable.** Because it is external, information can be moved from place to place, from person to person, from medium to medium. It can be copied, duplicated, and distributed at near-zero cost.

**It is propositional.** Information typically takes the form of propositions—statements that can be true or false. "The cat is on the mat." "The boiling point of water is 100°C." Information is the kind of thing that can be asserted, denied, recorded, and verified.

**It is cumulative.** Information can be added to. You can have more or less of it. It can be collected, aggregated, and stored.

**It is passive.** Information does not do anything by itself. It does not act, decide, or apply itself. A book on a shelf contains information, but the book does not read itself.

```
   THE PROPERTIES OF INFORMATION

   ┌────────────────────────────────────────────────────┐
   │  EXTERNAL      │  exists outside the mind          │
   │  TRANSFERABLE  │  can be copied and moved          │
   │  PROPOSITIONAL │  takes the form of true/false     │
   │                │  statements                        │
   │  CUMULATIVE    │  can be added to, stored,         │
   │                │  aggregated                        │
   │  PASSIVE       │  does not act or apply itself     │
   └────────────────────────────────────────────────────┘
```

These characteristics are what make information so valuable and so cheap. It can be stored, transmitted, and replicated at almost no cost. It can be organized and searched. It can be aggregated and analyzed. And because it is external, it can be shared among unlimited numbers of people without being diminished.

But these same characteristics are what make information *insufficient* for knowledge. Information is external; knowledge is internal. Information is transferable; knowledge must be constructed. Information is propositional; knowledge is model-based. Information is cumulative; knowledge is integrative. Information is passive; knowledge is active.

---

## What Knowledge Is

If information is external, structured data with meaning, then **knowledge is the internal, integrated, actionable model of reality that a mind constructs from information.**

This definition has several components, and each of them matters.

### Knowledge Is Internal

Knowledge exists in minds, not in books or databases. This is not a trivial point. It means that knowledge cannot be transferred directly from one mind to another. It can only be **reconstructed**.

When I read a book, I do not receive the author's knowledge. I receive information—words, sentences, propositions—and I use that information to build my own knowledge. The knowledge I build may be similar to the author's, but it is not identical. It is my construction, shaped by my prior knowledge, my experiences, my questions, and my purposes.

This is why teaching is so difficult. A teacher cannot pour knowledge into a student's head. The teacher can only provide information—explanations, examples, problems, feedback—and hope that the student constructs the right kind of knowledge. The student must do the work of construction.

### Knowledge Is Integrated

Information is fragmented. It arrives in pieces—a fact here, a statistic there, an observation somewhere else. Knowledge is what happens when those pieces are integrated into a coherent whole. It is the **network of connections** among pieces of information, not the pieces themselves.

```
   INFORMATION                 KNOWLEDGE
   (fragmented)                (integrated)

   ●       ●                   ●───────●───────●
       ●       ●               │ ╲     │     ╱ │
   ●       ●                   │   ╲   │   ╱   │
       ●       ●               ●───────●───────●
   ●       ●                   │   ╱   │   ╲   │
       ●       ●               │ ╱     │     ╲ │
   ●       ●                   ●───────●───────●

   Facts scattered             Facts woven into
   without connection          a model with
                               connections
```

A person who has memorized a thousand isolated facts has more information than a person who understands a single principle deeply. But the person with the principle has more knowledge, because knowledge is about connections, not accumulation.

### Knowledge Is Actionable

Information tells you **that** something is the case. Knowledge tells you **what to do about it**.

John Snow's information told him that people were dying of cholera in Soho. His knowledge told him that the Broad Street pump was the source and that removing the handle would stop the epidemic. The information was a description. The knowledge was a **capacity for action**.

This does not mean that all knowledge must be immediately practical. Theoretical knowledge—the knowledge of how the universe works, of mathematical truths, of historical patterns—is valuable even when it has no immediate application. But even theoretical knowledge is actionable in a broader sense: it shapes how we see the world, what questions we ask, and what possibilities we consider.

### Knowledge Is Model-Based

The deepest difference between information and knowledge is that knowledge takes the form of **models**. A model is a simplified representation of some aspect of reality that captures the relationships, mechanisms, or patterns that matter for a particular purpose.

Knowledge is model-based because reality is too complex to be known in full. We cannot hold all the details of the world in our minds. So we build simplified representations that capture what matters and ignore what does not. These models allow us to predict, explain, and act.

```
   INFORMATION                  KNOWLEDGE
   (propositional)              (model-based)

   "Water boils at 100°C"       ┌──────────────────────┐
                                │  Pressure            │
                                │     │                │
                                │     ▼                │
                                │  Boiling point       │
                                │     │                │
                                │     ▼                │
                                │  Cooking time        │
                                │     │                │
                                │     ▼                │
                                │  Altitude effects    │
                                └──────────────────────┘

   A single fact                A model of how the
                                variables relate
```

The person who knows *that* water boils at 100°C has a fact. The person who knows *why* and *how it changes with pressure* has a model. The first can recite. The second can predict what happens on a mountain, adapt a recipe, and design a pressure cooker.

### Knowledge Is Provisional

Finally, knowledge is provisional. It is always subject to revision, correction, and improvement. This is not a weakness; it is a feature. The history of science is the history of knowledge being revised—from Newtonian mechanics to relativity, from miasma theory to germ theory. Each revision did not destroy knowledge; it improved it.

```
   INFORMATION                  KNOWLEDGE
   (static)                     (provisional)

   "The sun revolves             "The sun is at the
    around the earth."            center of the solar
                                  system."
                                        │
                                        │ revised when
                                        │ new evidence
                                        ▼
                                  "The solar system
                                   is part of a
                                   galaxy."
                                        │
                                        ▼
                                  "The galaxy is
                                   part of an
                                   expanding
                                   universe."
```

Information can be true or false, and it stays that way. Knowledge is always subject to revision—because the evidence can change, and because the model can always be improved.

---

## The DIKW Hierarchy — and Its Limits

The distinction between information and knowledge is often represented by the **DIKW hierarchy**: Data, Information, Knowledge, Wisdom. It is one of the most widely used frameworks in information science and knowledge management.

```
   THE DIKW HIERARCHY

               ┌───────────┐
               │  WISDOM   │  applied judgment
               └─────▲─────┘
                     │
               ┌─────┴─────┐
               │ KNOWLEDGE │  integrated, actionable models
               └─────▲─────┘
                     │
               ┌─────┴─────┐
               │INFORMATION│  structured data with meaning
               └─────▲─────┘
                     │
               ┌─────┴─────┐
               │   DATA    │  raw, unprocessed symbols
               └───────────┘

   Each level is produced by transforming the level below it.
```

The hierarchy is useful because it captures the intuition that there is a qualitative difference between having data and having wisdom. But it is also **misleading**, in three ways.

**First, it implies a linear progression.** The pyramid suggests that data becomes information, which becomes knowledge, which becomes wisdom—as if each level automatically produces the next. It does not. Most data never becomes information. Most information never becomes knowledge. Most knowledge never becomes wisdom. The transformation requires effort, and most of it is lost.

**Second, it implies that the levels are separate.** In reality, they are intertwined. Knowledge informs what data we collect. Wisdom shapes what knowledge we pursue. The hierarchy is not a ladder; it is a spiral, with each level feeding back into the others.

**Third, it hides the knower.** The hierarchy describes levels of *content*—data, information, knowledge, wisdom—without acknowledging that all of them require a mind to exist. Data is only data relative to a mind that interprets it. Information is only information relative to a mind that understands it. Knowledge is only knowledge relative to a mind that constructs it. Wisdom is only wisdom relative to a mind that lives it.

```
   THE DIKW HIERARCHY, REVISED

   DATA ◄──────────── KNOWLEDGE ◄──────────── WISDOM
     │                    │                     │
     │ informs            │ informs             │ informs
     ▼                    ▼                     ▼
   INFORMATION ◄─────── EXPERIENCE ◄────────── ACTION
     │                    │                     │
     └────────────────────┴─────────────────────┘
                    (the knower)

   The levels are not a ladder. They are a loop,
   and the knower is at the center.
```

For our purposes, the most important distinction is between **information** and **knowledge**. Information is the raw material. Knowledge is the product. The transformation between them is the subject of this book.

---

## The Tacit Dimension

There is another crucial distinction between information and knowledge: the existence of **tacit knowledge**.

The term was coined by the philosopher Michael Polanyi in his 1966 book *The Tacit Dimension*. It refers to knowledge that cannot be fully articulated in words or transmitted through information. Polanyi's famous dictum is: **"We can know more than we can tell."**

Consider the knowledge of how to ride a bicycle. You can read a thousand pages of information about bicycles, balance, and physics, and still not know how to ride one. The knowledge of riding is tacit—it is embodied in the skill, the coordination, the feel of the bike. It can be learned, but it cannot be fully transmitted through information. It must be acquired through practice.

```
   THE EXPLICIT–TACIT SPECTRUM

   EXPLICIT ◄──────────────────────────────► TACIT
   (can be written)                (must be practiced)

   Formula    Recipe    Diagnostic    Bike     Intuition
                       heuristics     balance  /judgment
     │          │           │           │          │
     ▼          ▼           ▼           ▼          ▼
   Easy to   Easy to    Partly       Hard to    Very hard
   transmit  transmit   transmittable transmit   to transmit
```

Tacit knowledge is pervasive. It is the knowledge of how to recognize a face, how to speak a language, how to play a musical instrument, how to diagnose a disease, how to judge a legal case, how to lead a team. It is the knowledge that experts have but cannot fully explain.

The existence of tacit knowledge has profound implications for the information age. It means that the most valuable knowledge in any domain is often the **least transferable**. It cannot be captured in a database, written in a manual, or transmitted over a network. It must be acquired through experience, practice, and apprenticeship.

This is why the dream of uploading all human knowledge to a computer is fundamentally misguided. Much of what we know cannot be represented as information. It is embodied, situated, and practical.

For AI systems, this is a hard limit. A language model can be trained on every explicit statement ever written and still not know how to ride a bike, because the knowledge of riding is not in the text. It is in the practice. The same is true for many of the things we most want AI to do—judge, care, decide, create—they depend on tacit knowledge that cannot be extracted from data.

---

## Why the Confusion Matters

We have spent this chapter distinguishing information from knowledge. Why does it matter?

It matters because the confusion between the two is the root of many of our contemporary problems—and of many of the failures I see in AI systems.

### In AI Systems

The most common failure mode of language models is that they are given **information** and asked to produce **knowledge**.

A retrieval-augmented system retrieves documents and passes them to a model. The documents contain facts. The facts are accurate. But the model has no way to know whether the facts are *sufficient*—whether they actually support the answer it is about to produce. It assembles the facts into a plausible model, and sometimes the model is wrong.

```
   THE AI FAILURE MODE

   Information ──► Model ──► Plausible Answer
                     ▲              │
                     │              │
              (no grounding         │
               in reality)          │
                                    ▼
                              Confident Wrongness

   The model has information. It does not have knowledge.
   It has no way to tell the difference.
```

This is why retrieval-augmented generation (RAG) helps, but does not solve the problem. RAG grounds the model in information. It does not ground it in knowledge. The model can still assemble accurate facts into an inaccurate model—and present that model with perfect confidence.

### In Education

When we confuse information with knowledge, we design educational systems that emphasize the transmission of information rather than the construction of knowledge. We test students on their ability to recall facts rather than their ability to integrate, apply, and evaluate. We produce graduates who are informed but not knowledgeable.

### In Decision-Making

When we confuse information with knowledge, we make decisions based on the latest data rather than on a deep understanding of the situation. We react to headlines rather than analyzing trends. We confuse the availability of information with the possession of knowledge, and we act with confidence that is not warranted.

### In Society

When we confuse information with knowledge, we create a public sphere that is saturated with information but impoverished in knowledge. We have more news than ever, but less understanding. We have more data than ever, but less wisdom. We have more communication than ever, but less agreement.

---

## The Economics of the Distinction

The difference between information and knowledge has profound economic implications—and these implications explain a lot about the world we live in.

**Information is abundant and cheap.** It can be copied and distributed at near-zero cost. This is why the internet has been so disruptive to industries built on the control of information—publishing, music, journalism, education.

**Knowledge is scarce and expensive.** It requires time, effort, attention, and often collaboration. It requires validation, integration, and application. It requires the construction of models and the testing of models against reality.

```
   THE ECONOMICS OF INFORMATION AND KNOWLEDGE

   INFORMATION                    KNOWLEDGE
   ┌──────────────────────┐      ┌──────────────────────┐
   │  Cost to copy: ~0    │      │  Cost to build: high │
   │  Abundance: infinite │      │  Abundance: scarce   │
   │  Transfer: instant   │      │  Transfer: slow      │
   │  Value: decaying     │      │  Value: enduring     │
   └──────────────────────┘      └──────────────────────┘

   This is why the most valuable companies are not the
   ones that control the most information. They are the
   ones that have built the most valuable knowledge.
```

This is why experts are valuable. They possess knowledge that is difficult to acquire and expensive to replace. This is why education is valuable. It is the process by which knowledge is transmitted from one generation to the next—not as information, but as practice, apprenticeship, and discipline.

It is also why the AI industry is so volatile. The companies that win are not the ones with the most data. They are the ones that can convert data into models that actually work—that can build knowledge from information.

---

## A Return to the Retrieval System

The retrieval system I described at the start of this chapter did not fail because it lacked information. It failed because it confused information with knowledge.

The documents were accurate. The facts were correct. But the model assembled them into a picture that did not correspond to how the system worked—and it had no way to know.

I think about that failure often. It is a reminder that the distinction between information and knowledge is not academic. It is operational. It is the difference between a system that can recite and a system that can understand. It is the difference between a person who is informed and a person who knows.

And it is the reason this book exists. Because the pipeline—the process of converting information into knowledge—is not automatic. It requires discipline, method, and practice. And it is the most important skill of our age.

---

## Chapter Summary

- **Information** is external, structured data that carries meaning. It is transferable, propositional, cumulative, and passive.
- **Knowledge** is the internal, integrated, actionable model of reality that a mind constructs from information. It is constructed, validated, integrated, contextual, and provisional.
- The **DIKW hierarchy** (Data, Information, Knowledge, Wisdom) captures the progression from raw material to applied judgment—but it is misleading because it implies a linear progression and hides the role of the knower.
- **Tacit knowledge**—knowledge that cannot be fully articulated—is a crucial dimension of knowledge that is often overlooked. It cannot be captured in a database; it must be acquired through practice.
- The confusion between information and knowledge has consequences for **AI systems, education, decision-making, and society**.
- The **economics** of information and knowledge are different. Information is cheap and abundant; knowledge is expensive and scarce.
- The transformation from information to knowledge is a **disciplined process**, not an automatic one. It is the subject of this book.

---

**Next Chapter:** *The Knowledge Gap* — why the gap between information and knowledge is widening, what it costs us, and what it would take to close it.

---

<!-- book-nav:start -->

---

[← Chapter 1](../part-1-the-problem/01-the-information-deluge.md) | [Contents](../README.md) | [Chapter 3 →](../part-1-the-problem/03-the-knowledge-gap.md)

<!-- book-nav:end -->
