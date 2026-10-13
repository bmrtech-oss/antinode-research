# Separate deterministic and ambiguity-oriented processing paths

- **Status:** Accepted for the proposed design
- **Date:** 2026-10-13
- **Decision owners:** Antinode Labs
- **Supersedes / superseded by:** None

## Context

Some candidate rules can be evaluated with explicit deterministic checks;
others require interpretation or domain judgment. Treating both cases as
equally certain obscures uncertainty.

## Decision

Use a System 1 path for deterministic checks and a System 2 path to surface
ambiguity, exceptions, and candidates requiring review. Both paths retain
evidence links and feed a human review process. The names denote workflow roles
only.

## Alternatives considered

- **One undifferentiated pipeline:** Simpler to describe, but hides where
  judgment and uncertainty enter.
- **Fully autonomous reasoning:** Not appropriate for the proposed scope or
  evidence requirements.

## Consequences

Review effort can be focused on ambiguous candidates, while deterministic
checks remain inspectable. Path assignment and confidence must not be mistaken
for correctness; the evaluation must test both and report reviewer burden.
