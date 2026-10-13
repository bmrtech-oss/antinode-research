# Research principles

These principles guide both the systems we study and how we communicate their
design.

## Simplicity

Prefer things that are easy to understand, change, and reason about. Following
Rich Hickey's distinction, simplicity is the absence of interleaved concerns,
not merely a small count of components. Choose the smallest design that meets
the stated requirements, and make unavoidable complexity explicit.

## Composability

Prefer small components with clear responsibilities and interfaces that can be
combined. This follows the Unix tradition of tools that do one thing well and
work together through stable boundaries. Preserve the ability to replace,
inspect, and test parts independently.

## Signal over noise

Make evidence, assumptions, trade-offs, and decisions prominent. Remove
repetition that does not add meaning, but retain enough context to make claims
auditable. This is Antinode Labs' editorial principle: maximize useful signal
for each unit of complexity.

## Applying the principles

When principles conflict, state the trade-off and rationale in the paper or
ADR. These principles are guides for transparent decisions, not claims that
one architecture is universally best.
