# Design Decisions for a Business Rule Extraction Platform

**Document type:** Registered Report  
**Version:** 3.0  
**Date:** 2026-10-13  
**Status:** Proposed architecture and pre-specified evaluation plan  
**Authors:** Antinode Labs

## Abstract

Organizations often encode business rules across policies, technical
documentation, and operational records. Extracting those rules requires more
than text generation: each candidate must be traceable to evidence, represented
consistently, and reviewable by a domain expert. This registered report
proposes an architecture for a business rule extraction platform and specifies
how its utility should be evaluated. The design combines a property graph for
rules and provenance, a versioned YAML taxonomy, schema-validated ingestion,
and distinct deterministic and human-reviewed reasoning paths. The report
records eight consequential design decisions and a phased evaluation plan.
Results are not reported here; all evaluation criteria are specified before
measurement.

## 1. Introduction

Business rules shape eligibility, obligations, exceptions, and operational
decisions. In many settings they are distributed across documents and change
over time. Manual extraction can be slow and inconsistent, while automated
extraction without evidence links can be difficult to audit or safely adopt.

This report asks how to design an extraction platform that supports
traceability, incremental updates, and review without imposing unnecessary
operational complexity. The proposed system treats extracted rules as
evidence-backed, versioned assertions rather than unqualified generated text.

The architecture follows simplicity, composability, and signal over noise
([shared principles](../../shared/principles.md)). It is a design proposal: no
performance, accuracy, or user-study result is asserted in this document.

## 2. Research questions

- **RQ1:** Can a provenance-aware representation support reliable tracing from
  extracted business rules to their source passages and transformations?
- **RQ2:** Does separating deterministic rule processing from an
  ambiguity-oriented review path make decisions easier to inspect and validate?
- **RQ3:** Which operational trade-offs arise from a single-tenant,
  incrementally updated platform compared with the requirements it is intended
  to satisfy?

## 3. Scope and assumptions

The proposed platform ingests a bounded set of policy and business documents,
identifies candidate rules, associates them with a controlled taxonomy, and
allows a reviewer to inspect evidence and provenance. The first research
iteration targets one organization and one deployment boundary.

The design assumes source documents can be assigned stable identifiers and
that an authorized domain reviewer can adjudicate uncertain candidates. It
does not assume that a model-generated candidate is a valid rule until
reviewed according to the applicable workflow.

Out of scope for this report are autonomous enforcement of extracted rules,
unbounded web crawling, cross-organization data sharing, and claims of
production readiness.

## 4. Proposed architecture

The architecture separates source ingestion, extraction, rule representation,
and review. A property graph links source documents, passages, rule candidates,
taxonomy concepts, and review events. The graph is the traceability model, not
a claim that every document must be converted to graph form. A versioned YAML
taxonomy supplies controlled categories without requiring an ontology as a
prerequisite.

Each ingestion is validated against explicit schemas before processing.
Content-addressed source versions and transformation records enable incremental
reprocessing while preserving lineage. A deterministic System 1 path handles
well-formed, explicitly specified rules; a System 2 path flags ambiguity,
exceptions, and low-confidence candidates for assisted review. These labels
describe workflow roles in this design, not psychological or model guarantees.

The system's boundaries and data flow are shown in
[`architecture.mmd`](../diagrams/architecture.mmd). The planned extraction and
review sequence is shown in [`review-flow.mmd`](../diagrams/review-flow.mmd).
Eight records in [`../adr/`](../adr/) explain the principal choices.

## 5. Methods and materials

### 5.1 Study design

The proposed evaluation uses a curated corpus of representative business
documents, reviewed against a manually adjudicated reference set. Corpus
selection, inclusion criteria, and any necessary redaction must be documented
before the evaluation begins. No confidential or personal data should be
included in public artifacts.

### 5.2 Procedures

1. Record document identifiers, versions, formats, and inclusion decisions.
2. Establish a reference set of rule statements, evidence spans, and taxonomy
   labels through independent review and adjudication.
3. Run the proposed ingestion and extraction workflow on the frozen corpus.
4. Have reviewers assess candidates without treating system output as ground
   truth.
5. Preserve configuration, schema, taxonomy, and transformation versions with
   every run.

### 5.3 Comparison

Where feasible, compare the proposed workflow with a documented manual
baseline using the same corpus and reference criteria. Report deviations from
the protocol and do not select comparisons after observing favorable outcomes.

## 6. Analysis plan

The evaluation should report rule-level precision and recall against the
adjudicated reference set, evidence-span coverage, taxonomy agreement, and
review effort. Report counts and uncertainty alongside aggregate values.
Disagreements in the reference set must be described rather than silently
discarded.

For provenance, sample extracted candidates and verify whether a reviewer can
follow links to the source version, supporting passage, processing step, and
review event. For incremental ingestion, compare changed and unchanged source
versions and verify that unchanged content is not needlessly treated as new
evidence. Record runtime and resource observations as descriptive measures,
not as a general performance guarantee.

Before evaluation, the research team must publish concrete acceptance
thresholds appropriate to the corpus and use case. Since no corpus, baseline,
or stakeholder-approved thresholds have been established in this proposal,
numeric thresholds remain an explicitly unresolved preregistration item and
must be specified before outcome collection.

## 7. Evaluation criteria

The study will be considered informative if it can determine:

- whether candidate rules can be traced to source evidence and processing
  history;
- how extraction quality varies by rule type and source characteristics;
- whether the two review paths expose ambiguity in a way domain reviewers can
  act on;
- what review burden and operational costs accompany the design; and
- which proposed components are necessary, insufficient, or disproportionate
  for the stated scope.

Evaluation results, including negative or inconclusive findings, should be
reported with protocol deviations and limitations.

## 8. Risks, limitations, and ethics

The reference set may be incomplete or reflect reviewer interpretation. Results
from a bounded corpus may not generalize to other domains, languages, or
document types. A graph representation and taxonomy may add maintenance
overhead; the study should assess whether the traceability benefits justify
that cost.

Documents may contain sensitive business information or personal data. Obtain
authorization, minimize collected data, redact public examples, and define
retention and access controls before ingestion. The platform must not be used
for consequential automated decisions on the basis of unreviewed extractions.

## 9. Expected contributions

The expected outputs are an inspectable architecture, a documented set of
trade-offs, and an evaluation protocol that can be tested against a suitable
corpus. These are planned contributions, not findings.

## 10. Decision register

| Decision | Record |
| --- | --- |
| Use a property graph rather than RDF as the primary rule/provenance store | [ADR 001](../adr/property-graph-over-rdf.md) |
| Use a YAML taxonomy rather than requiring an ontology | [ADR 002](../adr/yaml-taxonomy-over-ontology.md) |
| Start with a single-tenant deployment | [ADR 003](../adr/single-tenant-over-multi-tenant.md) |
| Validate schemas with CUE and Pkl | [ADR 004](../adr/cue-pkl-schema-validation.md) |
| Separate deterministic System 1 and review-oriented System 2 paths | [ADR 005](../adr/system-1-system-2-model.md) |
| Preserve incremental-ingestion provenance | [ADR 006](../adr/incremental-ingestion-provenance.md) |
| Keep a hybrid repository structure | [ADR 007](../adr/hybrid-repo-structure.md) |
| Deliver in phases with hard gates | [ADR 008](../adr/phased-delivery-hard-gates.md) |

## References

See [`../../shared/references.bib`](../../shared/references.bib). The design
principles draw on Hickey's discussion of simplicity and Unix composability;
the registered-report format follows the rationale for specifying methods
before results are known.
