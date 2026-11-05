# Part IV — The Obstacles

---

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║                                                                              ║
║   ┌──────────────────────────────────────────────────────────────────────┐   ║
║   │                                                                      │   ║
║   │                     THE PIPELINE, IDEAL                              │   ║
║   │                                                                      │   ║
║   │   ┌────────┐   ┌────────────┐   ┌──────────┐   ┌────────┐            │   ║
║   │   │ SELECT │──►│ PRE-PROCESS│──►│ GENERATE │──►│  TEST  │            │   ║
║   │   └────────┘   └────────────┘   └──────────┘   └────────┘            │   ║
║   │        ▲                                              │              │   ║
║   │        │                                              ▼              │   ║
║   │   ┌────────┐   ┌────────────┐   ┌────────────────────────┐           │   ║
║   │   │ CORRECT│◄──│   RETAIN   │◄──│       INTEGRATE        │           │   ║
║   │   └────────┘   └────────────┘   └────────────────────────┘           │   ║
║   │        │                                                             │   ║
║   │        └──────────────────────────► back to SELECT                   │   ║
║   │                                                                      │   ║
║   └──────────────────────────────────────────────────────────────────────┘   ║
║                                                                              ║
║                                                                              ║
║                                    ▼                                         ║
║                                                                              ║
║                                                                              ║
║   ┌──────────────────────────────────────────────────────────────────────┐   ║
║   │                                                                      │   ║
║   │                     THE SAME PIPELINE, REAL                          │   ║
║   │                                                                      │   ║
║   │        ╲╲╲╲╲╲         ╲╲╲╲╲╲          ╲╲╲╲╲╲         ╲╲╲╲╲╲          │   ║
║   │   ┌────────┐   ┌────────────┐   ┌──────────┐   ┌────────┐            │   ║
║   │   │ SELECT │──►│ PRE-PROCESS│──►│ GENERATE │──►│  TEST  │            │   ║
║   │   └────────┘   └────────────┘   └──────────┘   └────────┘            │   ║
║   │        ▲           ╲╲╲╲╲╲            ╲╲╲╲╲╲           │              │   ║
║   │        │                                              ▼              │   ║
║   │   ┌────────┐   ┌────────────┐   ┌────────────────────────┐           │   ║
║   │   │ CORRECT│◄──│   RETAIN   │◄──│       INTEGRATE        │           │   ║
║   │   └────────┘   └────────────┘   └────────────────────────┘           │   ║
║   │        │            ╲╲╲╲╲╲              ╲╲╲╲╲╲                       │   ║
║   │        └──────────────────────────► back to SELECT                   │   ║
║   │                                                                      │   ║
║   │        ╲╲╲╲╲╲  =  the forces that push the pipeline off course       │   ║
║   │                                                                      │   ║
║   └──────────────────────────────────────────────────────────────────────┘   ║
║                                                                              ║
║                                                                              ║
║                    T H E   O B S T A C L E S                                 ║
║                                                                              ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

              A GOOD METHOD IS NOT ENOUGH. THE WORLD INTERFERES.
```

---

> *"The first principle is that you must not fool yourself—and you are the easiest person to fool."*
> — Richard Feynman

> *"A wealth of information creates a poverty of attention."*
> — Herbert Simon

---

## The Obstacles, in Four Chapters

Part III described the pipeline as it should work. Part IV describes why it usually doesn't.

A method is not a machine. It runs on minds, in groups, inside institutions, under pressure. And each of those environments introduces forces that push the pipeline off course—forces that are not errors in the method but obstacles in the conditions under which the method operates.

There are three categories of obstacle, and Part IV adds a fourth that is often overlooked.

**Chapter 16 — Cognitive Biases: The Enemies Within.** The mind itself is the first obstacle. Biases do not just distort judgment; they get built into the instruments we use to judge—the tests, the metrics, the tools—where they look objective.

**Chapter 17 — Logical Fallacies: The Enemies Without.** The second obstacle is the structure of arguments. The fallacies that matter most are not the ones in political debate. They are the ones in technical clothing—the design documents, benchmarks, and best-practice appeals that look like engineering but are dressed-up non sequiturs.

**Chapter 18 — Social and Institutional Obstacles: When the Environment Fights Back.** The third obstacle is the room. A correct analysis can be talked out of existence without ever being refuted—drowned by anecdote, social proof, and the courage tax that makes dissent individually irrational and collectively essential.

**Chapter 19 — The Limits of the Individual Mind: Why We Need External Scaffolds.** The fourth obstacle is the boundary of the brain itself. The unaided mind cannot run the pipeline at scale, so we build scaffolds—and scaffolds can either extend the mind or replace it, and you cannot tell which one you have built until you remove it.

By the end of this part, you should understand why the pipeline fails even when every stage is understood. You should also understand that the failures are not random. They are structural. And structural failures can be designed against.

---

```
                    ┌───────────────────────────┐
                    │                           │
                    │   The pipeline is not     │
                    │   the hard part.          │
                    │                           │
                    │   Running it in the       │
                    │   world is.               │
                    │                           │
                    └───────────────────────────┘
```

---

**→ Turn the page. The enemies are about to become visible.**

<!-- book-nav:start -->

---

[← Chapter 15](../part-3-the-process/15-the-pipeline-in-practice.md) | [Contents](../README.md) | [Chapter 16 →](../part-4-the-obstacles/16-cognitive-biases.md)

<!-- book-nav:end -->
