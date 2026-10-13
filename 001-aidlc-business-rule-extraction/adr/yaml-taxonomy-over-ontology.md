# Use a versioned YAML taxonomy rather than requiring an ontology

- **Status:** Accepted for the proposed design
- **Date:** 2026-10-13
- **Decision owners:** Antinode Labs
- **Supersedes / superseded by:** None

## Context

The initial scope needs stable, reviewable categories for classifying
candidate rules. There is no established requirement for formal reasoning over
a domain ontology.

## Decision

Represent the initial controlled vocabulary as a versioned YAML taxonomy with
explicit identifiers, labels, and relationships.

## Alternatives considered

- **Formal ontology from the outset:** Adds expressive semantics but requires
  governance and modeling effort not justified by current requirements.
- **Unconstrained labels:** Low initial overhead, but weakens consistency and
  analysis across documents.

## Consequences

The taxonomy is easy to review and version alongside the paper. It must be
validated and governed as it evolves. If formal inference or interoperability
becomes necessary, a mapping to an ontology can be evaluated without treating
the current taxonomy as one.
