# Start with a single-tenant deployment

- **Status:** Accepted for the proposed design
- **Date:** 2026-10-13
- **Decision owners:** Antinode Labs
- **Supersedes / superseded by:** None

## Context

The first research iteration targets a bounded organizational context. No
cross-organization service or tenant-isolation requirement has been
established.

## Decision

Design and evaluate a single-tenant deployment boundary first.

## Alternatives considered

- **Multi-tenant service:** Could share operational infrastructure, but
  introduces isolation, identity, and data-governance complexity before it is
  needed.
- **Per-user deployment:** Narrows sharing further and does not match the
  initial organization-level review workflow.

## Consequences

The design has fewer isolation concerns and a simpler initial operational
model. It is not ready to serve multiple organizations; tenancy boundaries,
authorization, and migration would require a separate design before expansion.
