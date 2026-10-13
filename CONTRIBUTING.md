# Contributing

Contributions to research papers, registered reports, architecture decisions,
and shared guidance are welcome.

## Before submitting

1. Read the [research principles](shared/principles.md) and
   [style guide](shared/style-guide.md).
2. Search existing papers, terminology, and ADRs to avoid duplicating work.
3. For a new paper, create a numbered kebab-case directory (for example,
   `002-short-descriptive-name/`) and start from
   [`templates/paper-template/`](templates/paper-template/).
4. For an architectural choice, add an ADR from
   [`templates/adr-template/`](templates/adr-template/). Keep decisions
   immutable: supersede an accepted ADR with a new one instead of rewriting its
   history.

## Research and review

Distinguish planned work from completed work. State research questions,
methods, assumptions, and limitations explicitly; do not present proposals as
results. Cite external claims in text and add bibliographic records to
`shared/references.bib` when appropriate. Keep diagrams in Mermaid format and
store source files beside the document they explain.

Submit focused changes with descriptive commit or pull request messages. The
GitLab pipeline validates Markdown, Mermaid diagrams, required repository
structure, and links. Resolve validation failures or explain any intentional
exceptions in the proposal.
