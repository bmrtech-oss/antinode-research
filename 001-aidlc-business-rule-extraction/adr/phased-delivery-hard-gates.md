# Deliver in phases with hard gates

- **Status:** Accepted for the proposed design
- **Date:** 2026-10-13
- **Decision owners:** Antinode Labs
- **Supersedes / superseded by:** None

## Context

The proposal includes ingestion, extraction, provenance, and review. Building
all capabilities at once would make it difficult to isolate risks and validate
assumptions.

## Decision

Deliver and evaluate the work in phases, with explicit hard gates before
advancing scope. A gate requires documented evidence against pre-specified
criteria; unmet criteria pause or redirect the next phase.

## Alternatives considered

- **Big-bang delivery:** Delays learning and compounds integration risk.
- **Un-gated continuous expansion:** Enables flexibility but can increase scope
  without confirming the core assumptions.

## Consequences

Phased work supports earlier learning and limits investment in unvalidated
assumptions. Gates add review overhead and require criteria to be specified
before observing results. No phase is considered passed solely because its
implementation is complete.
