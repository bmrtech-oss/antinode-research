# Chapter 9: Pre-processing — Cleaning, Structuring, and Contextualizing

---

The worst bug I ever shipped was a chunking bug.

I was building a retrieval system over a corpus of technical documentation. The documents were Markdown files—headers, code blocks, tables, prose. I wrote a chunker that split them into fixed-size pieces of about five hundred tokens each, with a small overlap to preserve continuity. It was the obvious thing to do. It was in every tutorial.

The system retrieved chunks that were relevant. The model produced answers that were wrong.

It took me weeks to find the problem. The chunks were cutting through the middle of code examples. A chunk would end mid-function, with the closing braces in the next chunk. A table would be split so that the column headers lived in one chunk and the data in another. A warning box—"Do not use this in production"—would be separated from the code it warned about, so the retriever would surface the code without the warning.

The documents were fine. The model was fine. The retrieval was fine. The **pre-processing** was broken.

I had optimized for token count. I had not asked what a chunk *was*. A chunk is not a fixed-size window. A chunk is a unit of meaning. And I had destroyed the meaning by treating it as a string.

This chapter is about that mistake, and about the discipline that prevents it.

---

## Why Pre-processing Is the Stage Everyone Skips

Selection is the gatekeeper. Generation is the forge. Testing is the crucible. These stages get attention because they feel consequential.

Pre-processing feels like chores. Cleaning. Formatting. Adding metadata. Splitting documents. Nobody writes blog posts about chunking. Nobody gets excited about deduplication.

And yet, in my experience, **most pipeline failures are pre-processing failures.** Not because the later stages are easy, but because the later stages cannot recover from bad inputs. A model cannot reason its way out of a context window filled with fragmented, decontextualized, noisy text. A human cannot build a model from data that has been mislabeled, misaligned, or stripped of its frame.

Pre-processing is the stage that determines whether the rest of the pipeline has anything worth working with.

```
   WHERE PIPELINE FAILURES ORIGINATE

   ┌─────────────────────────────────────────────────────┐
   │                                                     │
   │   SELECT       ████                                 │
   │   PRE-PROCESS  ████████████████████████             │
   │   GENERATE     ███████                              │
   │   TEST         ██████████                           │
   │   INTEGRATE    ██████                               │
   │   RETAIN       ████                                 │
   │   CORRECT      ████                                 │
   │                                                     │
   │   (Rough distribution of failures in my own         │
   │    experience building retrieval systems.)          │
   │                                                     │
   └─────────────────────────────────────────────────────┘
```

The bar chart is not a scientific finding. It is a confession. For years I looked for the problem in the model, in the prompt, in the retrieval ranking. It was almost always upstream of all of those—in the raw material I had handed to the system without preparing it.

---

## The Four Tasks

Pre-processing has four tasks. Each takes the output of the previous task and prepares it for the next.

```
 ┌────────┐   ┌───────────┐   ┌───────────────┐   ┌─────────┐
 │ CLEAN  │──►│ STRUCTURE │──►│ CONTEXTUALIZE │──►│ CONNECT │
 └────────┘   └───────────┘   └───────────────┘   └─────────┘
```

They are not strictly sequential. You will loop back. But the order is a useful default: clean first, because structuring dirty data is wasted effort; structure before contextualizing, because context attaches to structure; connect last, because connection requires knowing what you are connecting.

---

## Cleaning

Cleaning is the work of removing errors, inconsistencies, ambiguities, omissions, and biases from the information.

It is the least glamorous task in the pipeline and the one with the highest return on investment.

```
 ┌───────────────────────────────────────────────────────┐
 │                   FIVE TYPES OF ERROR                 │
 ├───────────────────────────────────────────────────────┤
 │  FACTUAL       →  false claims                        │
 │  INCONSISTENT  →  contradictory claims                │
 │  AMBIGUOUS     →  multiple interpretations            │
 │  OMISSION      →  missing information                 │
 │  BIAS          →  systematic distortion               │
 └───────────────────────────────────────────────────────┘
```

Each type requires a different cleaning strategy:

```
 ┌───────────────────────────────────────────────────────┐
 │                 CLEANING STRATEGIES                   │
 ├───────────────────────────────────────────────────────┤
 │  CROSS-CHECK       →  compare with other sources      │
 │  SOURCE VERIFY     →  check the original              │
 │  DEFINITION CHECK  →  resolve ambiguity               │
 │  GAP ANALYSIS      →  identify what is missing        │
 │  BIAS DETECTION    →  look for systematic distortion  │
 └───────────────────────────────────────────────────────┘
```

In a retrieval system, cleaning takes a specific form. It means:

- **Deduplicating.** The same content appears in multiple documents, often in slightly different forms. Retrieving all of them wastes context.
- **Removing boilerplate.** Navigation elements, footers, cookie banners, "related articles" sections. These are pure noise.
- **Fixing encoding.** Mojibake, broken Unicode, HTML entities that were never decoded.
- **Normalizing formatting.** Consistent date formats, consistent units, consistent capitalization of proper nouns.
- **Flagging staleness.** A document from 2019 about a library that has since been rewritten is not just outdated; it is actively misleading.

The last one matters more than people realize. In my chunking disaster, half the retrieved documents were from an older version of the documentation. They described an API that no longer existed. The model, unable to tell old from new, mixed the two together into an answer that was internally consistent and completely wrong.

After that, I added a `version` field to every document's metadata and filtered the corpus to the current version before retrieval. The answer quality jumped. I had not changed the model. I had cleaned the data.

---

## Structuring

Structuring is the work of organizing information into a form that can be used.

Raw information is often unstructured. It arrives as a stream of text, a jumble of numbers, a collection of disconnected facts. Structuring is the work of imposing order on this chaos.

```
 ┌───────────────────────────────────────────────────────┐
 │                 FORMS OF STRUCTURE                    │
 ├───────────────────────────────────────────────────────┤
 │  CATEGORY   →  group by shared characteristics        │
 │  HIERARCHY  →  organize by levels                     │
 │  SEQUENCE   →  organize by time or process            │
 │  MATRIX     →  organize by dimensions                 │
 │  NETWORK    →  organize by connections                │
 └───────────────────────────────────────────────────────┘
```

The choice of structure depends on the purpose. A hierarchy is good for understanding a topic. A sequence is good for understanding a process. A matrix is good for comparing options. A network is good for understanding a system.

For the chunking problem, the right structure was a **hierarchy** that respected the document's own organization:

```
   NAIVE CHUNKING                    STRUCTURE-AWARE CHUNKING

   ┌──────────────┐                  ┌──────────────────────┐
   │ ...text...   │                  │ # Section Header     │
   │ ...code...   │                  │                      │
   │ ...text...   │                  │ Parent: Chapter 3    │
   │ ...code mid- │                  │ Children: none       │
   │ function...  │                  │                      │
   └──────────────┘                  │ ┌──────────────────┐ │
   ┌──────────────┐                  │ │ ...text...       │ │
   │ ...closing   │                  │ │ ...code...       │ │
   │ braces...    │                  │ │ ...text...       │ │
   │ ...text...   │                  │ └──────────────────┘ │
   └──────────────┘                  │                      │
                                     │ Every chunk carries  │
   Chunks cut through                │ its structural       │
   meaning.                          │ context.             │
                                     └──────────────────────┘
```

The fix was to chunk on **semantic boundaries**—headers, paragraphs, code blocks, table boundaries—rather than on token count. Each chunk carried metadata about its parent section, its siblings, and its place in the document. When the chunk was retrieved, the model received not just the text but the structure.

This is what structuring means in practice. It is not a formatting exercise. It is the work of preserving the relationships that give information meaning.

---

## Contextualizing

Contextualizing is the work of restoring the context that gives information meaning.

We discussed context in Chapter 4. Here we treat it as a pre-processing task.

```
 ┌───────────────────────────────────────────────────────┐
 │                 DIMENSIONS OF CONTEXT                 │
 ├───────────────────────────────────────────────────────┤
 │  SEMANTIC    →  what do the words mean?               │
 │  SITUATIONAL →  what is the situation?                │
 │  HISTORICAL  →  what is the background?               │
 │  CAUSAL      →  what caused it? what will it cause?   │
 │  PURPOSIVE   →  what is it for?                       │
 └───────────────────────────────────────────────────────┘
```

When information is decontextualized, it becomes ambiguous or misleading. A statistic without its source is a rumor. A quote without its surrounding text is a distortion. A study without its limitations is an overclaim.

In retrieval systems, contextualizing takes a specific form. Every retrieved chunk should carry:

- **Source.** Where did it come from? Who wrote it?
- **Date.** When was it written? Is it still current?
- **Version.** Which version of the system does it describe?
- **Scope.** What does it apply to? What does it not apply to?
- **Confidence.** How reliable is it? Is it official documentation, a blog post, a forum answer?

```
   THE CONTEXT ENVELOPE

   ┌─────────────────────────────────────────────────────┐
   │  source: docs.example.com/api/v2                    │
   │  date: 2024-03-15                                   │
   │  version: 2.4                                       │
   │  scope: production API                              │
   │  confidence: official documentation                 │
   ├─────────────────────────────────────────────────────┤
   │                                                     │
   │  ...the actual content of the chunk...              │
   │                                                     │
   └─────────────────────────────────────────────────────┘

   The model receives the content AND its context.
   It can weigh, compare, and cite appropriately.
```

This is what "contextualizing" means for a retrieval system. It is not enough to retrieve the right text. You must retrieve the text with the context that tells the model how to interpret it.

---

## Connecting

Connecting is the work of linking new information to what you already know.

Connection is the beginning of integration. It is the process of situating new information in the network of existing knowledge—identifying related concepts, comparing with previous evidence, and recognizing patterns and relationships.

```
 ┌───────────────────────────────────────────────────────┐
 │                  FORMS OF CONNECTION                  │
 ├───────────────────────────────────────────────────────┤
 │  SIMILARITY   →  how is it like what I know?          │
 │  DIFFERENCE   →  how is it different?                 │
 │  CAUSATION    →  what caused it? what does it cause?  │
 │  CONTRADICTION→  does it conflict with what I know?   │
 │  IMPLICATION  →  what follows from it?                │
 └───────────────────────────────────────────────────────┘
```

In retrieval systems, connecting takes a specific form. It means retrieving not just the chunk that matches the query, but the chunks that are **related** to it—parent sections, sibling chunks, cross-references, related documents.

```
   FLAT RETRIEVAL                    CONNECTED RETRIEVAL

   Query ──► [chunk]                 Query ──► [chunk]
                                                  │
                                                  ├──► parent section
                                                  ├──► sibling chunks
                                                  ├──► cross-references
                                                  └──► related documents

   Model receives one               Model receives the chunk
   chunk in isolation.              and its neighborhood.
```

This is what connecting means in practice. It is the work of ensuring that the model—or the human—receives not just the piece of information, but the piece in its network.

In my chunking disaster, the fix was not just structure-aware chunks. It was **graph-aware retrieval**. When a chunk was retrieved, the system also retrieved its neighbors—the chunks immediately before and after, the parent section, and any chunks that explicitly referenced it. The model received a small, coherent subgraph of the documentation instead of a scattered set of fragments.

The answer quality improved again. The model was not smarter. It had been given the connections it needed to reason.

---

## The Pre-processing Workflow

The four tasks form a workflow. It is iterative, not linear.

```
 ┌───────────────────────────────────────────────────────────────┐
 │                                                               │
 │   ┌────────┐   ┌───────────┐   ┌───────────────┐              │
 │   │ CLEAN  │──►│ STRUCTURE │──►│ CONTEXTUALIZE │              │
 │   └────────┘   └───────────┘   └───────────────┘              │
 │       ▲                                    │                  │
 │       │                                    ▼                  │
 │       │                           ┌────────────────┐          │
 │       │                           │    CONNECT     │          │
 │       │                           └────────────────┘          │
 │       │                                    │                  │
 │       └────────────────────────────────────┘                  │
 │                    (iterative loops)                          │
 │                                                               │
 └───────────────────────────────────────────────────────────────┘
```

The workflow can be summarized as four questions:

```
 ┌───────────────────────────────────────────────────────┐
 │            PRE-PROCESSING QUESTIONS                   │
 ├───────────────────────────────────────────────────────┤
 │  CLEAN:          Is it accurate, consistent,          │
 │                  complete, unbiased?                  │
 │  STRUCTURE:      How should it be organized?          │
 │  CONTEXTUALIZE:  What is the context?                 │
 │  CONNECT:        How does it relate to what I know?   │
 └───────────────────────────────────────────────────────┘
```

Ask them habitually. Ask them of every document, every dataset, every chunk. They will become automatic.

---

## Common Pitfalls

Pre-processing is hard, and it is easy to do badly. Here are the five pitfalls I have encountered most often—including in my own work.

```
 ┌───────────────────────────────────────────────────────┐
 │              COMMON PRE-PROCESSING PITFALLS           │
 ├───────────────────────────────────────────────────────┤
 │  SKIPPING CLEANING    →  accept errors                │
 │  OVER-STRUCTURING     →  impose false order           │
 │  DECONTEXTUALIZING    →  ignore meaning               │
 │  UNDER-CONNECTING     →  fragment knowledge           │
 │  CONFUSING STAGES     →  never move forward           │
 └───────────────────────────────────────────────────────┘
```

**Skipping cleaning.** The most common pitfall. Accepting information at face value without checking for errors, inconsistencies, or biases.

**Over-structuring.** The opposite pitfall. Imposing a rigid structure on information that does not fit. Over-structuring can obscure important details and create false patterns.

**Decontextualizing.** Treating information as if it were context-free. This is the path to misunderstanding.

**Under-connecting.** Failing to connect new information to existing knowledge. Information that is not connected is quickly forgotten and rarely used.

**Confusing stages.** Spending so much time on pre-processing that you never move to generation and testing. Pre-processing is preparation. It is not the destination.

The knowledge engineer avoids these pitfalls by being deliberate. They clean, structure, contextualize, and connect—but they do not overdo any of them. They know when to stop and move on.

---

## Pre-processing and the Brain

We have described pre-processing as a deliberate, conscious process. But it is worth noting that the brain does something similar automatically.

```
 ┌──────────────────────┬───────────────────────┐
 │   BRAIN PROCESS      │   PRE-PROCESSING STEP │
 ├──────────────────────┼───────────────────────┤
 │   Sensory filtering  │   Cleaning            │
 │   Categorization     │   Structuring         │
 │   Memory/association │   Contextualizing     │
 │   Neural networks    │   Connecting          │
 └──────────────────────┴───────────────────────┘
```

The brain **cleans** information through sensory filtering—ignoring irrelevant stimuli, correcting for noise, and filling in gaps. It **structures** information through categorization and schemas. It **contextualizes** information through memory and association. It **connects** information through neural networks.

The deliberate process of pre-processing is a **formalization** of what the brain does automatically. It is what happens when you take the brain's implicit processes and make them explicit, systematic, and controllable.

This is why pre-processing works. It is not an arbitrary set of steps. It is a mirror of the brain's own methods, refined and extended.

---

## Pre-processing in the Age of AI

The modern knowledge engineer does not pre-process alone. They have tools—including AI—that can help.

Large language models can assist with pre-processing in several ways. They can summarize long documents. They can clean text and resolve inconsistencies. They can structure information into categories, outlines, or tables. They can extract metadata. They can identify related concepts.

But AI is not a substitute for the knowledge engineer's judgment. AI can make errors—it can hallucinate metadata, misinterpret context, and miss important connections. The knowledge engineer uses AI as a **tool**, not as an oracle.

```
 ┌───────────────────────────────────────────────────────┐
 │              AI-ASSISTED PRE-PROCESSING               │
 ├───────────────────────────────────────────────────────┤
 │  WHAT AI CAN DO:                                      │
 │    • Summarize long documents                         │
 │    • Clean text and correct errors                    │
 │    • Structure information into categories            │
 │    • Extract metadata and tags                        │
 │    • Identify related concepts and connections        │
 │                                                       │
 │  WHAT AI CANNOT DO:                                   │
 │    • Judge whether information is true                │
 │    • Understand the purpose of the inquiry            │
 │    • Make the final decision about relevance          │
 │    • Take responsibility for the knowledge            │
 └───────────────────────────────────────────────────────┘
```

In my own work, I now use AI to do the first pass of pre-processing—summarizing, tagging, extracting structure—and then I review the output manually. The AI saves me perhaps 70% of the time. The remaining 30% is where the quality lives, and it requires human judgment.

---

## A Return to the Chunker

I rewrote the chunker three times.

The first version split on token count. It was fast and wrong.

The second version split on semantic boundaries—headers, paragraphs, code blocks—and attached structural metadata to each chunk. It was slower and better.

The third version added graph-aware retrieval. It was slower still, and it was the version we shipped.

The final system was not elegant. It was not the kind of thing you write a paper about. It was a series of unglamorous fixes to the pre-processing layer, each one removing a source of noise or restoring a piece of context. The model never changed. The retrieval ranking never changed. The pre-processing changed, and the answers changed with it.

This is the lesson of Chapter 9. Pre-processing is the stage that determines whether the rest of the pipeline has anything worth working with. It is not glamorous. It is not fast. It is the work that turns raw material into something that can become knowledge.

The chunker is not the hero of the story. But it is the reason the story has a happy ending.

---

## Chapter Summary

- **Pre-processing** is the second stage of the knowledge pipeline. It is the work of turning raw, messy, decontextualized information into something that can be understood, tested, and integrated.
- Pre-processing has four tasks: **cleaning, structuring, contextualizing, and connecting**.
- **Cleaning** is removing errors, inconsistencies, ambiguities, omissions, and biases. Strategies include cross-checking, source verification, definition checking, gap analysis, and bias detection.
- **Structuring** is organizing information into a usable form. Forms include categories, hierarchies, sequences, matrices, and networks. The choice of structure depends on the purpose.
- **Contextualizing** is restoring the context that gives information meaning. Dimensions include semantic, situational, historical, causal, and purposive.
- **Connecting** is linking new information to existing knowledge. Forms include similarity, difference, causation, contradiction, and implication.
- The pre-processing workflow is **iterative**, not linear.
- Common pitfalls include skipping cleaning, over-structuring, decontextualizing, under-connecting, and confusing pre-processing with processing.
- Pre-processing **mirrors the brain's own processes**—sensory filtering, categorization, memory/association, and neural networks.
- **AI can assist** with pre-processing, but it cannot replace human judgment.
- The lesson of the **chunker** is that most pipeline failures are pre-processing failures, and that fixing the raw material is often more valuable than improving the model.

---

**Next Chapter:** *Generation — Forming Candidate Models, Concepts, and Hypotheses* — a detailed examination of the third stage of the pipeline, including concept formation, hypothesis generation, analogy, and synthesis.

---

<!-- book-nav:start -->

---

[← Chapter 8](../part-3-the-process/08-selection.md) | [Contents](../README.md) | [Chapter 10 →](../part-3-the-process/10-generation.md)

<!-- book-nav:end -->
