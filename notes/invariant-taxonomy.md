# Invariant Taxonomy

## Meaning Invariants
Constraints on observed system state (e.g., count ≥ 0).  
They detect invalid states but do not prevent fault-producing transitions.

## Transition Invariants
Constraints on allowable state transitions.  
They prevent execution paths that can lead to invalid states.

## Example

Meaning Invariant:
- active_users ≥ 0

Transition Invariant:
- active_users updates must be atomic with respect to execution context
