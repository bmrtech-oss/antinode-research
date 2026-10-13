# Style guide

## Writing

- Use clear, direct language and define domain-specific terms on first use.
- Separate observations, assumptions, proposals, and results.
- State research questions and evaluation criteria before reporting outcomes.
- Describe limitations and alternative explanations.
- Use headings and lists to aid navigation, not to fragment every paragraph.

## Structure and naming

- Name paper directories with a zero-padded numeric prefix and kebab-case slug.
- Use kebab-case for filenames and ADR identifiers.
- Keep paper-specific decisions, diagrams, and artifacts in that paper's
  directory; place genuinely shared material in `shared/`.
- Link related work with repository-relative Markdown links.

## Diagrams and references

- Use Mermaid source (`.mmd`) for diagrams so they remain text-based and
  reviewable.
- Label diagram edges and keep node names consistent with the glossary.
- Cite sources in the text and add complete BibTeX entries to
  `shared/references.bib`.
- Include access dates for mutable online resources.

## Changes over time

- Record accepted architectural decisions in ADRs.
- Supersede rather than silently rewrite accepted decisions.
- Add a dated entry to the paper's changelog for material revisions.
