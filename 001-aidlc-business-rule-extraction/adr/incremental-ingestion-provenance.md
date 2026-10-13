# Preserve provenance during incremental ingestion

- **Status:** Accepted for the proposed design
- **Date:** 2026-10-13
- **Decision owners:** Antinode Labs
- **Supersedes / superseded by:** None

## Context

Source documents may change between ingestion runs. Reprocessing everything
can waste resources, while overwriting old versions can make extracted rules
impossible to audit.

## Decision

Track source versions and content identity, process changed material
incrementally, and retain links from each candidate to its source version and
transformation history.

## Alternatives considered

- **Full replacement on every run:** Easier to implement initially, but loses
  efficient change handling and may erase useful lineage.
- **In-place updates without version history:** Reduces storage but prevents
  reliable reconstruction of prior outputs.

## Consequences

Reviewers can inspect what changed and why an output was produced. Version and
deduplication policies require explicit definition, and provenance retention
adds storage and implementation work. Evaluation must verify both changed and
unchanged inputs.
