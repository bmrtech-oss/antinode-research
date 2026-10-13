# Keep a hybrid repository structure

- **Status:** Accepted for the proposed design
- **Date:** 2026-10-13
- **Decision owners:** Antinode Labs
- **Supersedes / superseded by:** None

## Context

Research documents benefit from a navigable paper-oriented structure, while
schemas, taxonomies, and evaluation materials need to remain versioned and
usable as artifacts.

## Decision

Keep the paper, diagrams, artifacts, and ADRs together in the paper directory,
and share only cross-paper principles, glossary, style, and bibliography at
repository level. Store structured materials with the paper they support.

## Alternatives considered

- **Documents-only repository:** Simplifies reading but can separate claims
  from the artifacts needed to inspect them.
- **Code-first monorepo:** Can make artifacts prominent but may obscure the
  research narrative and create premature implementation structure.

## Consequences

Readers can navigate from paper claims to supporting materials while shared
guidance avoids duplication. The boundary must be maintained as papers grow;
move material to shared locations only when it is genuinely reused.
