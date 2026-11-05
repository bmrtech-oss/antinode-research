# Chapter 4: The Raw Material — Information, Signals, and Noise

<!-- chapter-meta:start -->

**Level:** Beginner

> **Key Terms:** [Context](../back-matter/98-appendix-a-glossary.md#context) · [Fact](../back-matter/98-appendix-a-glossary.md#fact) · [Noise](../back-matter/98-appendix-a-glossary.md#noise) · [Signal](../back-matter/98-appendix-a-glossary.md#signal). Definitions are in [Appendix A](../back-matter/98-appendix-a-glossary.md).

<!-- chapter-meta:end -->

---

The first time I built a retrieval system for a customer, I made a mistake that took me a year to understand.

I had built the system to find the most relevant documents. I measured relevance carefully—semantic similarity, BM25, hybrid ranking. I tuned the parameters. I got the retrieval quality up to a number I was proud of.

And the answers were still wrong.

Not all of them. But often enough to matter. The system would retrieve the right documents and produce the wrong answer. I spent months convinced the problem was in the ranking. It was not. The problem was that I had confused **retrieval** with **understanding**. I had built a system that could find the right information. I had not built a system that could tell the difference between signal and noise within that information.

The documents were relevant. Within each document, most of the content was noise—context that did not matter, caveats that did not apply, examples that were close but not quite right. The retrieval system passed all of it to the model. The model, unable to distinguish signal from noise, assembled an answer from whatever was nearest to hand.

This is the problem of the raw material. Information is not a clean substance. It is a mixture of signal and noise, and the ratio is usually much worse than it looks. Before you can convert information into knowledge, you must understand what you are actually working with.

---

## The Three Layers, Revisited

We have already distinguished data, information, and knowledge. It is worth restating them here because the distinction is the foundation of everything that follows—and because most people collapse the first two without realizing it.

**Data** is raw, unprocessed, and meaningless in itself. It is a number, a character, a reading from a sensor. Data has no inherent meaning.

**Information** is data that has been organized, structured, or contextualized so that it carries meaning. It answers questions. It reduces uncertainty.

**Knowledge** is the internal, integrated, actionable model that a mind constructs from information.

```
   THE THREE LAYERS

   ┌──────────────────────────────────────────────────────┐
   │                      KNOWLEDGE                       │
   │         internal, integrated, actionable models      │
   └──────────────────────────▲───────────────────────────┘
                              │
                          constructed from
                              │
   ┌──────────────────────────┴───────────────────────────┐
   │                     INFORMATION                      │
   │         structured data with meaning                 │
   └──────────────────────────▲───────────────────────────┘
                              │
                          organized from
                              │
   ┌──────────────────────────┴───────────────────────────┐
   │                        DATA                          │
   │         raw, unprocessed, meaningless                │
   └──────────────────────────────────────────────────────┘
```

Most conversations about information stop at this diagram. They treat the movement from data to information as a solved problem—just add structure, just add context, just clean the data. What they miss is that even after data becomes information, it is still mostly noise. The signal-to-noise ratio does not improve automatically. It has to be engineered.

---

## Shannon's Ghost

In 1948, Claude Shannon published a paper that quietly reshaped the modern world. It was called "A Mathematical Theory of Communication," and it appeared in the *Bell System Technical Journal*. Shannon was not a philosopher. He was not interested in meaning, truth, or knowledge. He was an engineer at Bell Labs, and his problem was practical: how do you transmit a message reliably over a noisy channel?

To solve this problem, Shannon did something radical. He **stripped information of meaning entirely**. For Shannon, information was not about what a message said. It was about **uncertainty reduction**. A message carries information to the extent that it resolves uncertainty about what was sent.

This was a profound move. It made modern telecommunications, data compression, and digital computing possible. It gave us the bit. It gave us the network. It gave us the internet.

But it also created a conceptual trap that we are still struggling to escape.

```
   WHAT SHANNON MEASURED                WHAT SHANNON ABSTRACTED AWAY
   ┌────────────────────────┐           ┌────────────────────────┐
   │                        │           │                        │
   │    INFORMATION         │           │       MEANING          │
   │    (quantity)          │           │       (quality)        │
   │                        │           │                        │
   │    Measured in bits    │           │    Cannot be measured  │
   │    Transferable        │           │    Must be constructed │
   │    Reducible to        │           │    Depends on context  │
   │    probability         │           │    and knower          │
   │                        │           │                        │
   └────────────────────────┘           └────────────────────────┘

   Shannon gave us the tools to move information around
   at the speed of light. He did not give us the tools
   to understand it.
```

By treating information as a quantity independent of meaning, Shannon made it possible to transmit information without understanding it. This is exactly what the modern internet does. It moves bits at enormous speed with almost no understanding of what those bits mean. The understanding—the conversion from information to knowledge—is left to the receiver.

This is why the information age has produced so much transmission and so little comprehension. We optimized the channel. We forgot the receiver.

---

## The Anatomy of Information

Not all information is created equal. To build knowledge, we need to understand the different types of information we encounter, because each type has different strengths, weaknesses, and requirements for validation.

### Facts

A **fact** is a claim about the world that is (or is presented as) true and verifiable. Facts are the most basic unit of information.

But facts are not as simple as they look. A fact has three components:

```
   THE ANATOMY OF A FACT

   ┌─────────────────────────────────────────────────────┐
   │                                                     │
   │   "The unemployment rate was 3.5 percent in         │
   │    July 2023."                                      │
   │                                                     │
   │   ┌─────────────┐   ┌──────────────┐   ┌──────────┐│
   │   │  CLAIM      │   │  MEASUREMENT │   │ CONTEXT  ││
   │   │             │   │              │   │          ││
   │   │ unemployment│   │ 3.5 percent  │   │ U.S.,    ││
   │   │ rate        │   │              │   │ July 2023││
   │   └─────────────┘   └──────────────┘   └──────────┘│
   │                                                     │
   │   Remove any one component and the fact becomes     │
   │   meaningless or misleading.                        │
   │                                                     │
   └─────────────────────────────────────────────────────┘
```

The danger with facts is **decontextualization**. A fact stripped of its context can be misleading or meaningless. "The unemployment rate is 3.5 percent" is a fact. But is it good or bad? Compared to what? Measured how? For whom? Without context, the fact is inert.

### Observations

An **observation** is a record of something that was perceived—by a human or an instrument. Observations are the raw material of science.

Observations are more reliable than mere claims because they are grounded in something that happened. But they are not infallible. Instruments can be miscalibrated. Observers can be biased. Measurements can be noisy.

The danger with observations is **selection bias**. We notice what we are looking for. We record what fits our expectations. An observation is always an observation *of something*, from a particular perspective, with a particular instrument. It is not the world itself; it is a trace of the world.

### Claims

A **claim** is an assertion that something is true. Claims are the most common form of information we encounter. They are what people say, write, post, and publish.

Claims are not the same as facts. A fact is a claim that has been verified. A claim is a proposition that has been asserted but not necessarily verified. The difference is crucial. Most of the information we encounter is claims, not facts. And most claims are not verified.

The danger with claims is **unreliability**. Claims can be true, false, partially true, misleading, or meaningless. They can be made in good faith or bad. They can be supported by evidence or not. The confidence of the claimant is not evidence of the truth of the claim.

### Models

A **model** is a simplified representation of some aspect of reality. Models are not claims about specific facts; they are frameworks for understanding how things work.

Models are more powerful than facts or claims because they are **generative**. They allow you to predict, explain, and understand. A good model can account for many facts, explain many observations, and generate new hypotheses.

The danger with models is **overconfidence**. Models are not reality; they are simplified representations of reality. When we forget this—when we treat our models as if they were the world itself—we become dogmatic, rigid, and blind to evidence that does not fit.

### Opinions

An **opinion** is a judgment or belief that is not necessarily based on evidence. Opinions are expressions of preference, values, or perspective.

Opinions are not information in the same sense as facts or observations. They are not claims about the world that can be verified or falsified. They are expressions of subjective experience or value.

The danger with opinions is **confusion with facts**. When opinions are presented as facts, or when we treat our own opinions as if they were objective truths, we confuse the map with the territory.

```
   THE FIVE TYPES OF INFORMATION

   ┌──────────────┬──────────────────────┬─────────────────────┐
   │  TYPE        │  CHARACTERISTIC      │  PRIMARY DANGER     │
   ├──────────────┼──────────────────────┼─────────────────────┤
   │  FACT        │  Verifiable claim    │  Decontextualization│
   │  OBSERVATION │  Perceived record    │  Selection bias     │
   │  CLAIM       │  Unverified          │  Unreliability      │
   │              │  assertion           │                     │
   │  MODEL       │  Generative          │  Overconfidence     │
   │              │  representation      │                     │
   │  OPINION     │  Subjective          │  Confusion with     │
   │              │  judgment            │  facts              │
   └──────────────┴──────────────────────┴─────────────────────┘
```

The knowledge engineer must know which type of information they are dealing with, because each type requires a different approach to validation.

---

## Signal and Noise

We have been talking about information as if it were a homogeneous substance. But in reality, information comes mixed with noise.

**Signal** is the part of the information that is meaningful, relevant, and useful. **Noise** is the part that is meaningless, irrelevant, or distracting.

The distinction between signal and noise is not absolute. It depends on your purpose. A piece of information that is signal for one person may be noise for another.

But the distinction is real. And in the modern information environment, the ratio of noise to signal is very high.

### The Sources of Noise

Noise comes from many sources.

**Irrelevance.** Most information is not relevant to your question. The news is full of stories that have nothing to do with your life. Social media is full of posts that do not matter to you. Email is full of messages that do not require your attention. The volume of irrelevant information is vast.

**Inaccuracy.** Much information is simply wrong. Claims are made without evidence. Statistics are misreported. Studies are misrepresented. Rumors are repeated as facts.

**Ambiguity.** Much information is unclear. It can be interpreted in multiple ways. It lacks context, definition, or precision.

**Manipulation.** Some information is deliberately designed to mislead. Propaganda, disinformation, advertising, and political spin are all forms of information that are intended to produce a false belief or a desired behavior.

**Overload.** Even accurate, relevant information can become noise if there is too much of it. When you are presented with more information than you can process, the excess becomes noise—not because it is meaningless, but because it cannot be integrated. It clogs the system.

```
   THE FIVE SOURCES OF NOISE

   ┌─────────────┬────────────────────────────────────────┐
   │ IRRELEVANCE │  Not about your question               │
   ├─────────────┼────────────────────────────────────────┤
   │ INACCURACY  │  Simply wrong                          │
   ├─────────────┼────────────────────────────────────────┤
   │ AMBIGUITY   │  Unclear, multiple interpretations     │
   ├─────────────┼────────────────────────────────────────┤
   │ MANIPULATION│  Deliberately designed to mislead      │
   ├─────────────┼────────────────────────────────────────┤
   │ OVERLOAD    │  Too much to integrate                 │
   └─────────────┴────────────────────────────────────────┘
```

### The Signal-to-Noise Ratio

The concept of the **signal-to-noise ratio** (SNR) comes from engineering. It is a measure of how much signal there is relative to noise.

In the information age, the SNR is often very low. This is not because there is no signal. It is because there is so much noise.

```
   THE SIGNAL-TO-NOISE RATIO

   HIGH SNR                     LOW SNR
   ┌──────────────────┐         ┌──────────────────┐
   │                  │         │  ░░░░░░░░░░░░░░  │
   │   ████████████   │         │  ░░░█░░░░░░░░░░  │
   │   ████████████   │         │  ░░░░░░░░░░█░░░  │
   │                  │         │  ░░░░░░░░░░░░░░  │
   └──────────────────┘         └──────────────────┘

   Signal is easy to         Signal is buried in
   detect.                   noise. Requires effort
                             to extract.

   The modern information environment is the right
   image, not the left. And most tools are built
   for the left.
```

This is the second thing I learned from my retrieval failure. I had built a system that was good at finding documents. I had not built a system that was good at finding signal *within* documents. The SNR inside the retrieved content was low, and the system had no mechanism to improve it.

Improving the SNR requires both **increasing the signal** (finding better sources, asking better questions, focusing on what matters) and **decreasing the noise** (filtering, ignoring, and discarding what is irrelevant or unreliable).

---

## The Art of Ignoring

The ability to ignore is underrated. In a world of information abundance, the person who succeeds is not the one who consumes the most information. It is the one who can **selectively ignore** the information that does not matter.

This is not laziness. It is discipline. It requires knowing what you are looking for, what your purpose is, and what is relevant to that purpose. It requires the confidence to say, "This is not for me," and the wisdom to recognize when something is.

```
   THE FOUR DIMENSIONS OF IGNORING

   ┌─────────────────────┬──────────────────────────────────┐
   │  IGNORE SOURCES     │  Filter by quality               │
   ├─────────────────────┼──────────────────────────────────┤
   │  IGNORE TOPICS      │  Define your domain              │
   ├─────────────────────┼──────────────────────────────────┤
   │  IGNORE DISTRACTIONS│  Design your environment         │
   ├─────────────────────┼──────────────────────────────────┤
   │  IGNORE NOISE       │  Extract signal from signal      │
   └─────────────────────┴──────────────────────────────────┘
```

**Ignoring sources.** Not all sources are equally valuable. Some are reliable, some are not. Some are relevant, some are not. Some are worth your time, some are not. Learning to ignore low-quality sources is a skill.

**Ignoring topics.** You cannot know everything. You cannot follow every development in every field. You must choose what to attend to and what to let go. This is not ignorance; it is focus.

**Ignoring distractions.** The modern world is full of distractions—notifications, alerts, messages, feeds. These are designed to capture your attention. Learning to ignore them is essential for deep work.

**Ignoring noise within signal.** Even good sources contain noise. A useful article may contain irrelevant details. A valuable conversation may contain small talk. Learning to extract the signal from the noise is a skill.

The art of ignoring is not the same as close-mindedness. It is not about refusing to consider new ideas or challenging evidence. It is about **selecting** what to attend to, based on relevance, quality, and purpose.

---

## Context: The Multiplier

We have said that information is data with meaning, and that meaning depends on context. This is one of the most important ideas in this book. **Context is what turns data into information, and information into knowledge.**

Consider the number `100`. As data, it is meaningless. As information, it could be "100 degrees Fahrenheit" (a temperature), "100 dollars" (a price), "100 years" (a duration), "100 percent" (a proportion), or "100 people" (a count). The context tells you which.

Now consider the statement "The temperature is 100 degrees." This is information. But is it knowledge? Not yet. To turn it into knowledge, you need more context. Where is the temperature being measured? What is the normal range for that location and time of year? What are the implications for health, agriculture, or energy use?

Context has several dimensions:

```
   THE FIVE DIMENSIONS OF CONTEXT

   ┌──────────────┬──────────────────────────────────────┐
   │  SEMANTIC    │  What do the words mean?             │
   ├──────────────┼──────────────────────────────────────┤
   │  SITUATIONAL │  What is the situation?              │
   ├──────────────┼──────────────────────────────────────┤
   │  HISTORICAL  │  What has happened before?           │
   ├──────────────┼──────────────────────────────────────┤
   │  CAUSAL      │  What caused this? What will it cause│
   ├──────────────┼──────────────────────────────────────┤
   │  PURPOSIVE   │  What is the information for?        │
   └──────────────┴──────────────────────────────────────┘
```

The loss of context is one of the greatest dangers of the information age. Information is often stripped of its context—decontextualized, fragmented, and presented in isolation. A statistic without its source, a quote without its surrounding text, a study without its limitations—these are forms of information that can mislead as much as they inform.

To build knowledge, you must **restore context**. You must ask: Where does this information come from? What is the situation? What is the background? What are the causes and effects? What is the purpose?

This is why the retrieval system I built failed. It retrieved documents, but it did not retrieve context. It passed the model a pile of facts with no way to tell which facts mattered, which were relevant, and which were noise. The model did not fail because it was bad. It failed because the raw material it was given was raw.

---

## Provenance and Source Quality

One of the most important aspects of context is **provenance**—the origin of the information. Where did it come from? Who produced it? Why? How?

Provenance matters because the quality of information depends on the quality of its source. A claim from a reliable source is more credible than a claim from an unreliable source.

But provenance is not a simple matter of "trustworthy" vs. "untrustworthy." It is a spectrum. And it requires judgment.

```
   THE SIX DIMENSIONS OF SOURCE QUALITY

   ┌──────────────┬──────────────────────────────────────┐
   │  EXPERTISE   │  Does the source have relevant        │
   │              │  knowledge and training?              │
   ├──────────────┼──────────────────────────────────────┤
   │  TRACK RECORD│  Has the source been reliable in      │
   │              │  the past?                            │
   ├──────────────┼──────────────────────────────────────┤
   │  INCENTIVES  │  What does the source gain from       │
   │              │  being believed?                      │
   ├──────────────┼──────────────────────────────────────┤
   │  EVIDENCE    │  Does the source provide verifiable   │
   │              │  evidence?                            │
   ├──────────────┼──────────────────────────────────────┤
   │  TRANSPARENCY│  Is the source open about its methods │
   │              │  and limitations?                     │
   ├──────────────┼──────────────────────────────────────┤
   │  INDEPENDENCE│  Is the source free from conflicts    │
   │              │  of interest?                         │
   └──────────────┴──────────────────────────────────────┘
```

When I rebuilt the retrieval system, I added a provenance layer. Every document had to carry metadata about its source, its date, and its confidence level. The system did not just retrieve documents; it retrieved documents with a context that told the model how much to trust them.

The quality of the answers improved dramatically. Not because the model was better. Because the raw material was cleaner.

---

## The Problem of Misinformation

The information age has made it easier than ever to produce and distribute misinformation. This is not a new problem—false information has always existed—but the scale and speed of modern misinformation are unprecedented.

Misinformation comes in several forms, and each requires a different response.

```
   THE MISINFORMATION LANDSCAPE

   ┌──────────────────┬─────────────────────────────────┐
   │  MISINFORMATION  │  False or inaccurate info,      │
   │                  │  regardless of intent           │
   ├──────────────────┼─────────────────────────────────┤
   │  DISINFORMATION  │  False info deliberately spread │
   │                  │  to deceive                     │
   ├──────────────────┼─────────────────────────────────┤
   │  MALINFORMATION  │  True info used to harm         │
   ├──────────────────┼─────────────────────────────────┤
   │  PROPAGANDA      │  Info spread to promote a       │
   │                  │  political cause or viewpoint   │
   └──────────────────┴─────────────────────────────────┘
```

The problem of misinformation is not just that people believe false things. It is that misinformation **erodes trust**. When people cannot tell what is true, they may stop trusting anything. They retreat to tribes, where they trust their own sources and distrust everyone else's.

Combating misinformation requires more than fact-checking. It requires **information literacy**—the ability to evaluate sources, assess evidence, and recognize manipulation. It requires **institutional trust**—reliable institutions that can serve as arbiters of truth. And it requires **cognitive discipline**—the willingness to question your own beliefs and to seek out disconfirming evidence.

For AI systems, misinformation is an acute problem. A language model trained on a corpus that contains misinformation will reproduce it. It has no way to distinguish true from false unless it is grounded in something external—a retrieval system, a knowledge base, a human verifier. The raw material it learns from is not clean, and cleaning it is the hardest problem in the field.

---

## A Return to the Retrieval System

The retrieval system I built failed because it confused retrieval with understanding. It could find information, but it could not tell the difference between signal and noise within that information.

The fix was not a better model. The fix was a better understanding of the raw material. I had to teach the system to:
- **Clean** the information (remove duplicate, low-quality, or stale documents).
- **Structure** the information (break documents into sections, extract key claims, attach metadata).
- **Contextualize** the information (record the source, the date, the confidence).
- **Connect** the information to the query (rank by relevance, not just similarity).

In other words, I had to pre-process the raw material. I had to do the work that Chapter 9 is about.

This is the lesson of Chapter 4. The raw material is not given. It is not clean. It is not obvious what is signal and what is noise. You must do the work of cleaning, structuring, contextualizing, and connecting. You must do the work of improving the signal-to-noise ratio. And you must do it before you try to convert the information into knowledge.

Shannon gave us the tools to move information around at the speed of light. He did not give us the tools to understand it. That work is ours.

---

## Chapter Summary

- **Data** is raw, unprocessed, and meaningless. **Information** is data organized and contextualized. **Knowledge** is the internal, integrated, actionable model that a mind constructs from information.
- **Shannon's information theory** made information measurable by abstracting away meaning. This made modern communication possible. It also created a trap: we now optimize transmission and forget comprehension.
- Information comes in five types: **facts** (verifiable), **observations** (perceived), **claims** (asserted), **models** (generative), and **opinions** (subjective). Each type has different strengths, weaknesses, and requirements for validation.
- **Signal** is meaningful, relevant, and useful. **Noise** is meaningless, irrelevant, or distracting. The signal-to-noise ratio is very low in the modern environment.
- Noise comes from **irrelevance, inaccuracy, ambiguity, manipulation, and overload**.
- The **art of ignoring** is essential: ignore sources, topics, distractions, and noise within signal.
- **Context** is what turns data into information and information into knowledge. Its dimensions are semantic, situational, historical, causal, and purposive.
- **Provenance** matters: source quality depends on expertise, track record, incentives, evidence, transparency, and independence.
- **Misinformation** comes in several forms: misinformation, disinformation, malinformation, and propaganda. Combating it requires information literacy, institutional trust, and cognitive discipline.
- The raw material is not clean. Improving the signal-to-noise ratio is the work of pre-processing—and it must be done before conversion to knowledge.

---

**Next Chapter:** *The Target — What Knowledge Actually Is* — a deeper examination of knowledge as a predictive model, the distinction between explicit and tacit knowledge, and the four tests by which knowledge can be evaluated.

---

<!-- book-nav:start -->

---

[← Part II](../part-2-the-foundations/part-2-divider.md) | [Contents](../README.md) | [Chapter 5 →](../part-2-the-foundations/05-the-target.md)

<!-- book-nav:end -->
