# Chapter 11: Testing — Comparing Candidate Models Against Evidence

<!-- chapter-meta:start -->

**Level:** Both

> **Key Terms:** [Base Rate](../back-matter/98-appendix-a-glossary.md#base-rate) · [Bayesian Reasoning](../back-matter/98-appendix-a-glossary.md#bayesian-reasoning) · [Bias (Statistical)](../back-matter/98-appendix-a-glossary.md#bias-statistical) · [Confirmation Bias](../back-matter/98-appendix-a-glossary.md#confirmation-bias) · [Disconfirmation](../back-matter/98-appendix-a-glossary.md#disconfirmation) · [Evidence](../back-matter/98-appendix-a-glossary.md#evidence) · [Falsification](../back-matter/98-appendix-a-glossary.md#falsification) · [Hindsight Bias](../back-matter/98-appendix-a-glossary.md#hindsight-bias) · [Regression to the Mean](../back-matter/98-appendix-a-glossary.md#regression-to-the-mean) · [Reliability](../back-matter/98-appendix-a-glossary.md#reliability) · [Testing](../back-matter/98-appendix-a-glossary.md#testing) · [Theory](../back-matter/98-appendix-a-glossary.md#theory) · [Validity](../back-matter/98-appendix-a-glossary.md#validity). Definitions are in [Appendix A](../back-matter/98-appendix-a-glossary.md).

<!-- chapter-meta:end -->

---

I once shipped a retrieval system that passed every test I gave it.

The evaluation suite was comprehensive. It had three hundred query-document pairs. It had relevance judgments from two annotators. It had metrics for precision, recall, and nDCG. The system scored 0.89 on nDCG@10. I was proud of it.

It failed in production within a week.

The failure was not subtle. Users were getting answers that were confidently wrong. The system retrieved documents that were relevant to the query but irrelevant to the answer. It had learned to match surface patterns—keywords, phrases, entities—and it had no idea whether the documents it retrieved actually supported the answer it was generating.

I went back to the evaluation suite. The scores were still 0.89. The suite was passing. The system was failing.

It took me another week to understand why. The evaluation suite and the retrieval index shared the same documents. The test queries had been written against the index. The relevance judgments had been made with the index in mind. The system was not being tested on whether it could retrieve the right documents. It was being tested on whether it could retrieve the documents that the annotators *remembered* from the index.

It was not a test of retrieval. It was a test of memorization. And it was passing.

This chapter is about that failure, and about the discipline that prevents it.

---

## Why Testing Is the Heart of the Pipeline

We have said that generation produces candidates and testing discriminates among them. But testing is more than a filter. It is the **engine of correction**—the process by which models are refined, revised, and replaced.

Without testing, the pipeline is speculation. With testing, it is knowledge.

```
 ┌───────────────────────────────────────────────────────┐
 │              WHAT TESTING SEPARATES                   │
 ├───────────────────────────────────────────────────────┤
 │  BELIEF          →  KNOWLEDGE                         │
 │  (held to be     │   (tested and survived)            │
 │   true)          │                                    │
 │                                                       │
 │  HYPOTHESIS      →  THEORY                            │
 │  (candidate      │   (extensively tested and          │
 │   explanation)   │    survived)                       │
 │                                                       │
 │  OPINION         →  EVIDENCE-BASED JUDGMENT           │
 │  (may or may    │   (exposed to evidence and          │
 │   not be based  │    corrected by it)                 │
 │   on evidence)  │                                     │
 └───────────────────────────────────────────────────────┘
```

<!-- diagram-alt -->*Diagram description: A diagram of what testing separates: beliefs become knowledge when tested and sustained, hypotheses become theories through extensive testing, and opinions become evidence-based judgments when exposed to and corrected by evidence.*


Testing is also the stage that most people skip. They form a belief, and then they look for evidence that confirms it. They avoid evidence that challenges it. They treat their beliefs as conclusions rather than as hypotheses.

The knowledge engineer does the opposite. They seek out disconfirming evidence. They try to falsify their models. They take seriously the possibility that they are wrong.

And they design tests that can actually fail.

That last part is what I got wrong. My evaluation suite could not fail. It was contaminated. The system was being tested on data it had already seen. The scores were high because the test was easy. The test was easy because I had built it wrong.

---

## The Logic of Testing: Prediction, Observation, Error

At its core, testing is a simple loop: **predict, observe, compare**.

```
 ┌─────────────────┐
 │      MODEL      │
 │  (your beliefs  │
 │  about the world│
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

<!-- diagram-alt -->*Diagram description: A downward flow from a model of the world to a prediction, then to an observation, which produces prediction error that updates the model in a feedback loop.*


This loop is the same one we encountered in the brain's predictive processing (Clark, Surfing Uncertainty: Prediction, Action, and the Embodied Mind, 2016; see Appendix D) and in the generation-testing cycle. It is the fundamental logic of knowledge acquisition.

The loop is simple, but executing it well is hard. The difficulty is not in understanding the logic; it is in **avoiding the traps** that make testing unreliable.

The first trap is a test that cannot fail. My evaluation suite was that trap. The queries were written against the index. The judgments were made with the index in mind. The test could only confirm what the annotators already believed. It could not surprise them.

The second trap is a test that measures the wrong thing. My suite measured whether the system could retrieve documents that the annotators remembered. It did not measure whether the system could retrieve documents that supported the answer. The metric was real. It was just measuring a fragment of the target.

```
   TWO WAYS A TEST CAN BE BROKEN

   TEST THAT CANNOT FAIL          TEST THAT MEASURES
                                   THE WRONG THING
   ┌──────────────────────┐        ┌──────────────────────┐
   │                      │        │                      │
   │  Query → System →    │        │  Metric: nDCG@10     │
   │  Known document →    │        │  Target: answer      │
   │  Score: high         │        │  quality             │
   │                      │        │                      │
   │  The test confirms   │        │  The metric is       │
   │  what it already     │        │  correlated with     │
   │  knows.              │        │  the target, but     │
   │                      │        │  not the target      │
   │                      │        │  itself.             │
   └──────────────────────┘        └──────────────────────┘
```

<!-- diagram-alt -->*Diagram description: Two columns compare a test that cannot fail, where a known document earns a high score and merely confirms prior knowledge, with a test using nDCG@10 as a proxy for answer quality even though it measures a correlated target rather than answer quality itself.*


The knowledge engineer must design tests that avoid both traps. The test must be capable of failing, and it must measure the thing that matters.

---

## Forms of Testing

Testing takes many forms. Each has its own strengths and weaknesses.

### Prediction

The most basic form of testing is **prediction**. You use your model to generate a prediction about what will happen or what is the case, and then you check whether the prediction is accurate.

The key to prediction as a test is **specificity**. A prediction that is vague ("something will happen") is not a test. A prediction that is specific ("this will happen at this time in this place with this magnitude") is a test.

```
 ┌───────────────────────────────────────────────────────┐
 │              SPECIFICITY OF PREDICTION                │
 ├───────────────────────────────────────────────────────┤
 │  VAGUE:    "The system will probably improve."        │
 │            (Not testable)                             │
 │                                                       │
 │  SPECIFIC: "Latency will drop below 200ms for         │
 │             90% of requests within two weeks."        │
 │            (Testable)                                 │
 └───────────────────────────────────────────────────────┘
```

<!-- diagram-alt -->*Diagram description: A diagram contrasts a vague, untestable prediction that a system will probably improve with a specific, testable prediction that latency will fall below 200 milliseconds for 90 percent of requests within two weeks.*


### Observation

The second form is **observation**. You compare your model against observations—data, experience, or experiment. If the model explains the observations, it is supported. If it does not, it is challenged.

Observation is more passive than prediction. You do not generate an expectation; you simply look at what is there. But observation is still a test.

For my retrieval system, the observation was the production failure. Users were getting wrong answers. The model (that nDCG@10 was a good measure of quality) was challenged. The observation did not fit the model.

### Experimentation

The third form is **experimentation**. You intervene in the world—you change something—and observe the result. Experimentation is among the most powerful forms of testing because it allows you to establish **causation**, not just correlation.

```
 ┌───────────────────────────────────────────────────────┐
 │              THE CONTROLLED COMPARISON                │
 ├───────────────────────────────────────────────────────┤
 │                                                       │
 │   ┌─────────────┐          ┌─────────────┐            │
 │   │  TREATMENT  │          │   CONTROL   │            │
 │   │    GROUP    │          │    GROUP    │            │
 │   └──────┬──────┘          └──────┬──────┘            │
 │          │                        │                   │
 │          ▼                        ▼                   │
 │   ┌─────────────┐          ┌─────────────┐            │
 │   │ INTERVENTION│          │    NO       │            │
 │   │             │          │ INTERVENTION│            │
 │   └──────┬──────┘          └──────┬──────┘            │
 │          │                        │                   │
 │          ▼                        ▼                   │
 │   ┌─────────────┐          ┌─────────────┐            │
 │   │  OUTCOME    │          │   OUTCOME   │            │
 │   └─────────────┘          └─────────────┘            │
 │                                                       │
 │   Difference in outcome → effect of intervention      │
 └───────────────────────────────────────────────────────┘
```

<!-- diagram-alt -->*Diagram description: A flow compares a treatment group receiving an intervention with a control group receiving none; their outcomes are compared, and the difference represents the intervention's effect.*


The controlled comparison is often called the gold standard. It involves treatment and control groups, random assignment, blinding, and measurement.

### Falsification

The fourth form is **falsification**. You subject your model to a test that could prove it wrong.

The logic of falsification is asymmetric. No amount of confirming evidence can prove a model true, but a single piece of disconfirming evidence can prove it false.

```
 ┌───────────────────────────────────────────────────────┐
 │              THE LOGIC OF FALSIFICATION               │
 ├───────────────────────────────────────────────────────┤
 │                                                       │
 │   Confirming evidence:     does not prove the model   │
 │   Disconfirming evidence:  can disprove the model     │
 │                                                       │
 │   The knowledge engineer seeks disconfirming          │
 │   evidence, not confirming evidence.                  │
 │                                                       │
 └───────────────────────────────────────────────────────┘
```

<!-- diagram-alt -->*Diagram description: A diagram of falsification contrasts confirming evidence, which does not prove a model, with disconfirming evidence, which can disprove it; the knowledge engineer is urged to seek the latter.*


For my retrieval system, the disconfirming evidence was the production failure. The model was wrong. The test that had confirmed it was contaminated. The disconfirming evidence—the actual failures—was the signal I needed. I had not been looking for it. I had been looking at the nDCG score.

### Comparison of Rival Hypotheses

The fifth form is **comparison of rival hypotheses**. When multiple models can explain the same evidence, you must find evidence that discriminates between them.

The test is a **crucial experiment**—one whose outcome is predicted differently by two rival hypotheses.

```
   THE CRUCIAL EXPERIMENT

   Hypothesis A predicts:  X
   Hypothesis B predicts:  Y

   Observation:            X

   → A is supported
   → B is challenged

   The experiment is "crucial" because it discriminates
   between the two hypotheses.
```

<!-- diagram-alt -->*Diagram description: A diagram of a crucial experiment: hypothesis A predicts X and hypothesis B predicts Y, while the observed X supports A and challenges B, distinguishing the rival explanations.*


In practice, crucial experiments are rare. Most of the time, rival hypotheses make overlapping predictions. But when a crucial experiment is possible, it is the most powerful form of testing.

---

## The Bayesian Stance

The logic of testing is often described in **Bayesian** terms. Bayes' theorem provides a formal framework for updating beliefs in light of evidence.

The core idea is simple: your belief in a hypothesis should be proportional to the evidence. When new evidence arrives, you update your belief. If the evidence is more likely under one hypothesis than another, you shift your belief toward the hypothesis that better predicts the evidence.

```
 ┌───────────────────────────────────────────────────────┐
 │                  THE BAYESIAN STANCE                  │
 ├───────────────────────────────────────────────────────┤
 │  Prior belief + New evidence → Updated belief         │
 │                                                       │
 │  • Strong priors → smaller updates                    │
 │  • Weak priors → larger updates                       │
 │  • Strong evidence → larger updates                   │
 │  • Weak evidence → smaller updates                    │
 │  • Certainty is impossible; calibration is the goal   │
 └───────────────────────────────────────────────────────┘
```

<!-- diagram-alt -->*Diagram description: A diagram of the Bayesian stance: prior belief combines with new evidence to produce updated belief; strong priors lead to smaller updates, strong evidence to larger ones, and calibration replaces certainty as the goal.*


The Bayesian stance is a corrective to two common errors: **overconfidence** (believing too strongly) and **underconfidence** (believing too weakly). The knowledge engineer calibrates their confidence to the evidence.

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

<!-- diagram-alt -->*Diagram description: A graph shows confidence rising in steps as evidence accumulates over time, while remaining below absolute certainty.*


For my retrieval system, the Bayesian update should have been: the nDCG score gave me high prior confidence in the system. The production failures were strong disconfirming evidence. The correct update was a large downward revision. I did not make it, because I was not looking at the production failures as evidence. I was looking at them as bugs to fix, not as tests of the model.

---

## The Problem of Confirmation Bias

The greatest obstacle to good testing is **confirmation bias**—the tendency to seek out, interpret, and remember information in ways that confirm our existing beliefs.

Confirmation bias operates at every stage of information processing.

```
 ┌───────────────────────────────────────────────────────┐
 │                 CONFIRMATION BIAS                     │
 ├───────────────────────────────────────────────────────┤
 │  SELECTION:   We seek sources that agree with us      │
 │  INTERPRETATION: We see what we expect to see         │
 │  MEMORY:      We recall confirming evidence more      │
 │               readily than disconfirming evidence     │
 └───────────────────────────────────────────────────────┘
```

<!-- diagram-alt -->*Diagram description: A diagram of confirmation bias identifies three stages: selection favors sources that agree, interpretation sees what is expected, and memory more readily recalls confirming than disconfirming evidence.*


My evaluation suite was a monument to confirmation bias. I had built a test that confirmed what I already believed—that the system was good. I had selected the queries. I had selected the relevance judgments. I had selected the metric. Every choice was shaped by my prior belief, and the test reflected that belief back to me.

The knowledge engineer combats confirmation bias through deliberate strategies.

### Strategy 1: Seek Disconfirming Evidence

Actively look for evidence that could prove you wrong. Read sources that disagree with you. Ask people who hold different views.

This is what I should have done. I should have written test queries that were not in the index. I should have asked annotators who had never seen the index to judge relevance. I should have looked for evidence that the system was failing, not just evidence that it was succeeding.

### Strategy 2: Consider Alternative Hypotheses

Force yourself to generate alternative explanations for the same evidence.

For my system, the alternative hypothesis was: *the system is retrieving documents that match the query but do not support the answer.* That hypothesis was generated by the production failures. If I had considered it earlier, I would have built a different test.

### Strategy 3: Test Your Predictions

Do not just look for evidence that supports your model. Make specific predictions and test them.

I had not made specific predictions. I had built a test that produced a score, and I had interpreted the score as evidence that the system was good. I had not predicted what the system would do on unseen queries. I had not tested whether the score would generalize.

### Strategy 4: Keep a Record

Write down your predictions and your reasons for holding your beliefs. Later, when the evidence arrives, compare your predictions with what actually happened.

I had not kept a record. I had built the suite, run it, and moved on. I had no record of what I expected the system to do in production. I had only the score.

```
 ┌───────────────────────────────────────────────────────┐
 │              COMBATING CONFIRMATION BIAS              │
 ├───────────────────────────────────────────────────────┤
 │  1. SEEK DISCONFIRMING EVIDENCE                       │
 │  2. CONSIDER ALTERNATIVE HYPOTHESES                   │
 │  3. TEST YOUR PREDICTIONS                             │
 │  4. KEEP A RECORD                                     │
 └───────────────────────────────────────────────────────┘
```

<!-- diagram-alt -->*Diagram description: A diagram lists four ways to combat confirmation bias in order: seek disconfirming evidence, consider alternatives, test predictions, and keep a record.*


---

## The Discipline of Falsification

Falsification is the most demanding form of testing. It requires you to seek out evidence that could prove you wrong.

The knowledge engineer cultivates the **discipline of falsification**. They treat their models as hypotheses, not conclusions. They actively look for the observations that would refute them.

### The Falsification Checklist

```
 ┌───────────────────────────────────────────────────────┐
 │              THE FALSIFICATION CHECKLIST              │
 ├───────────────────────────────────────────────────────┤
 │  1. What would prove this wrong?                      │
 │  2. What evidence would be inconsistent?              │
 │  3. Have I sought out that evidence?                  │
 │  4. Have I interpreted the evidence fairly?           │
 │  5. Am I willing to change my mind?                   │
 └───────────────────────────────────────────────────────┘
```

<!-- diagram-alt -->*Diagram description: A diagram of the falsification checklist asks what could prove a belief wrong, what evidence would conflict with it, whether that evidence was sought and interpreted fairly, and whether the person is willing to change their mind.*


If you cannot answer question 1, your model is not falsifiable. It is a belief.

If you have not sought out the evidence in question 3, you have not tested. You have confirmed.

If your answer to question 5 is no, you are not testing. You are defending.

For my retrieval system, the answers would have been:
1. What would prove this wrong? Production failures.
2. What evidence would be inconsistent? Users getting wrong answers.
3. Have I sought out that evidence? No. I had not looked at production.
4. Have I interpreted the evidence fairly? I had not looked at it at all.
5. Am I willing to change my mind? Apparently not, until the failures were undeniable.

The checklist is a diagnostic. It would have caught my failure before it shipped.

---

## Common Pitfalls in Testing

Testing is hard, and it is easy to do badly. Here are the five pitfalls I have encountered most often—including in my own work.

```
 ┌───────────────────────────────────────────────────────┐
 │              COMMON PITFALLS IN TESTING               │
 ├───────────────────────────────────────────────────────┤
 │  CONTAMINATED TEST SET →  test data has been seen     │
 │                          by the system                │
 │  OVERFITTING           →  memorize noise, not signal  │
 │  HINDSIGHT BIAS        →  "I knew it all along"       │
 │  SMALL SAMPLES         →  chance masquerading as      │
 │                          pattern                      │
 │  CORRELATION ≠ CAUSATION →  confounded relationships  │
 └───────────────────────────────────────────────────────┘
```

<!-- diagram-alt -->*Diagram description: A diagram lists common testing pitfalls and their effects: contaminated data has been seen before, overfitting memorizes noise, hindsight bias claims prior knowledge, small samples make chance look patterned, and correlation can be mistaken for causation.*


**Contaminated test set.** The test data has been seen by the system—either directly, through training, or indirectly, through the annotators. The system is being tested on memorization, not generalization.

**Overfitting.** The model fits the training data too closely, capturing noise as if it were signal. It performs well on the test set but poorly on new data.

**Hindsight bias.** The tendency to believe, after an outcome is known, that you predicted it all along.

**Small samples.** A pattern that appears in a small sample may be due to chance.

**Correlation ≠ causation.** Two variables can be correlated because one causes the other, because the other causes the one, because both are caused by a third variable, or because of chance.

For my retrieval system, the first pitfall—contaminated test set—was the fatal one. The test queries had been written against the index. The annotators had seen the index. The system was tested on data it had already seen.

```
   CONTAMINATION

   ┌─────────────────────────────────────────────────────┐
   │                                                     │
   │   INDEX ──────────────────────────────┐             │
   │     │                                 │             │
   │     │                                 ▼             │
   │     │                         ┌──────────────┐      │
   │     │                         │  TEST QUERIES│      │
   │     │                         │  (written    │      │
   │     │                         │   against    │      │
   │     │                         │   the index) │      │
   │     │                         └──────┬───────┘      │
   │     │                                │              │
   │     ▼                                ▼              │
   │   ┌─────────────────────────────────────────┐       │
   │   │           EVALUATION SUITE              │       │
   │   │                                         │       │
   │   │   Tests memorization, not retrieval.    │       │
   │   │                                         │       │
   │   └─────────────────────────────────────────┘       │
   │                                                     │
   └─────────────────────────────────────────────────────┘
```

<!-- diagram-alt -->*Diagram description: A diagram of test contamination shows an index used to write test queries, which then enter an evaluation suite; because the test material has been seen, the suite measures memorization rather than retrieval.*


The fix was to build a test set that was independent of the index. Queries written by people who had never seen the index. Documents that had not been used to build the index. A test that could not be passed by memorization.

The scores dropped. From 0.89 to 0.62. The system looked worse. But the scores were now measuring something that mattered. And the system that scored 0.62 was the one that actually worked in production.

---

## Testing in the Age of AI

AI has changed the landscape of testing. Machine learning models can be tested on massive datasets, with sophisticated methods for avoiding overfitting and selection bias.

But AI testing has its own pitfalls.

```
 ┌───────────────────────────────────────────────────────┐
 │                AI TESTING PITFALLS                    │
 ├───────────────────────────────────────────────────────┤
 │  WRONG METRICS   →  optimizing for the benchmark,     │
 │                     not the real world                │
 │  BIASED DATA     →  learning and concealing bias      │
 │  OPAQUE MODELS   →  can't test the mechanism,         │
 │                     only the output                   │
 │  BENCHMARK       →  training on the test set          │
 │  CONTAMINATION                                        │
 └───────────────────────────────────────────────────────┘
```

<!-- diagram-alt -->*Diagram description: A diagram lists AI testing pitfalls: wrong metrics encourage benchmark optimization over real-world performance, biased data can teach and conceal bias, opaque models expose only outputs, and benchmark contamination occurs when the test set is used for training.*


**Wrong metrics.** A model that performs well on a benchmark may perform poorly in the real world. The choice of metric is a value judgment, not a technical one.

**Biased data.** If the training data are biased, the model will learn the bias. It will perform well on the biased data and poorly on the unbiased data.

**Opaque models.** Many AI models are "black boxes." It is difficult to understand why they make the predictions they do. This makes it hard to test the mechanism, not just the output.

**Benchmark contamination.** Language models are trained on vast corpora that often include the benchmarks they are later evaluated on. The test scores are inflated. The models are being tested on data they have already seen.

For my retrieval system, the last one was the problem. The documents in the index were the documents in the test set. The system was being tested on data it had already seen.

The fix was to build a test set that was independent of the training data. It was smaller, noisier, and less convenient. It was also the only test that mattered.

---

## A Return to the Evaluation Suite

I rebuilt the evaluation suite three times.

The first version was contaminated. It scored 0.89 and meant nothing.

The second version was independent. It scored 0.62 and meant something.

The third version added a mechanism for continuous evaluation. It ran on production traffic, with a small sample of queries reviewed by human annotators every week. It was not a fixed test. It was a living test.

The system that shipped was not the one that scored 0.89. It was the one that scored 0.62 and was continuously evaluated against reality. It was less impressive on paper. It was more reliable in practice.

This is the lesson of Chapter 11. Testing is not about producing a score. It is about producing evidence. The score is a proxy. The evidence is the thing. And the evidence must be capable of showing you that you are wrong.

The evaluation suite that cannot fail is not a test. It is a mirror. It shows you what you already believe.

---

## Chapter Summary

- **Testing** is the fourth stage of the knowledge pipeline. It is the process of comparing candidate models against evidence.
- Testing separates **belief from knowledge, hypothesis from theory, opinion from evidence-based judgment**.
- The logic of testing is the **prediction-observation-error** loop.
- Forms of testing include **prediction, observation, experimentation, falsification, and comparison of rival hypotheses**.
- The **Bayesian stance** holds that beliefs are probabilities that are updated proportionally to evidence.
- **Confirmation bias** is the greatest obstacle to good testing. Strategies to combat it include seeking disconfirming evidence, considering alternative hypotheses, testing predictions, and keeping a record.
- **Falsification** is the most demanding form of testing. The falsification checklist includes: What would prove this wrong? What evidence would be inconsistent? Have I sought it out? Have I interpreted it fairly? Am I willing to change my mind?
- Common pitfalls include **contaminated test sets, overfitting, hindsight bias, small samples, and confusing correlation with causation**.
- **AI testing** has its own pitfalls: wrong metrics, biased data, opaque models, and benchmark contamination.
- The lesson of the **evaluation suite** is that a test that cannot fail is not a test. It is a mirror. The test must be independent, capable of failing, and continuously evaluated against reality.

<!-- reflection:start -->

## Reflection Questions

Each takes between ten and thirty minutes and asks you to look at your own work.

1. Take a test, review, or evaluation your team relies on. Who wrote it, and what did they believe when they wrote it? Name a result that would have surprised them. If you cannot, it may be a mirror.
2. Choose a metric you report. Describe a way it could improve while the thing it is meant to measure gets worse.
3. Recall a time you changed your mind because of evidence. Who designed the test that produced it? If you cannot remember one, what does that suggest?
4. Think of the last time a check came back confirming exactly what you expected. What would a skeptical colleague have asked you to look at before you believed it?

<!-- reflection:end -->

---

**Next Chapter:** *Integration — Building a Coherent Knowledge Base* — a detailed examination of the fifth stage of the pipeline, including coherence, consilience, hierarchy, and the resolution of contradictions.

---

<!-- book-nav:start -->

---

[← Chapter 10](../part-3-the-process/10-generation.md) | [Contents](../README.md) | [Chapter 12 →](../part-3-the-process/12-integration.md)

<!-- book-nav:end -->
