# Validate contracts with CUE and Pkl

- **Status:** Accepted for the proposed design
- **Date:** 2026-10-13
- **Decision owners:** Antinode Labs
- **Supersedes / superseded by:** None

## Context

The platform needs explicit, reviewable contracts for ingestion and
configuration. Invalid inputs should be rejected before extraction, and
contract changes should be auditable.

## Decision

Use CUE and Pkl as schema and configuration validation tools in the proposed
design, applying each where its contract model is appropriate.

## Alternatives considered

- **Ad hoc validation:** Easy to start, but risks inconsistent checks and
  poorly documented constraints.
- **A single format for every contract:** Could reduce tool count, but may not
  fit both data constraints and configuration needs equally well.

## Consequences

Contracts become explicit and validation can run before processing. The team
must document ownership and avoid duplicate, conflicting definitions across
the two tools. The choice should be revisited if prototypes show excessive
overlap or operational cost.
