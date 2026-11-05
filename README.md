# antinode-research

Research papers, registered reports, and design documents from Antinode Labs
(`bmrtech-oss`). This repository documents work on system design, knowledge
graphs, and software architecture.

## Repository map

| Path | Purpose |
| --- | --- |
| `001-aidlc-business-rule-extraction/` | First paper and design record |
| `templates/paper-template/` | Reusable paper and report outline |
| `templates/adr-template/` | Starting point for architecture decision records |
| `shared/` | Principles, terminology, writing guidance, and bibliography |

Papers use a zero-padded numeric prefix and kebab-case directory names. Use
Mermaid for diagrams and keep each paper's decisions and supporting artifacts
with that paper. Shared material belongs in `shared/`.

## Research principles

- **Simplicity:** prefer simple, understandable systems over unnecessary
  complexity, following Rich Hickey's emphasis on simplicity.
- **Composability:** build systems from small parts with clear interfaces, in
  the spirit of Unix.
- **Signal over noise:** make important ideas, evidence, and decisions easy to
  find; this is Antinode Labs' editorial principle.

Read [the shared principles](shared/principles.md) and
[contribution guide](CONTRIBUTING.md) before proposing work.

## Current work

[From Noise to Knowing](002-from-noise-to-knowing/README.md) is a book on turning
information into knowledge. Read it online at
<https://bmrtech-oss.github.io/antinode-research/>.

[Design Decisions for a Business Rule Extraction Platform](001-aidlc-business-rule-extraction/README.md)
is a registered report, version 3.0. It records the research plan and the
platform's architectural decisions; it does not claim that proposed evaluations
have already been conducted.

## License and citation

Unless otherwise noted, repository content is available under the MIT License.
See [LICENSE](LICENSE) and [CITATION.cff](CITATION.cff).
