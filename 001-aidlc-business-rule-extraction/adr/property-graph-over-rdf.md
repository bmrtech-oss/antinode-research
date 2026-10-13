# Use a property graph as the primary rule and provenance store

- **Status:** Accepted for the proposed design
- **Date:** 2026-10-13
- **Decision owners:** Antinode Labs
- **Supersedes / superseded by:** None

## Context

Rules, source passages, taxonomy concepts, and review events have many
traceability relationships. The initial use case emphasizes traversing those
relationships during investigation and review.

## Decision

Use a property graph as the primary persistence and traversal model for the
proposed platform.

## Alternatives considered

- **RDF as the primary model:** Offers standards-based semantic
  interoperability, but the initial design does not require a shared,
  externally governed ontology.
- **Relational tables only:** Familiar and structured, but multi-hop
  provenance traversal would require more explicit join modeling.

## Consequences

The graph makes connected evidence and history straightforward to navigate.
The choice may reduce interoperability with RDF-oriented tools; export or
mapping can be evaluated if interoperability becomes a demonstrated need. The
decision does not preclude RDF exchange formats.
