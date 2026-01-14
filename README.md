# Causal Debugging via Transition Invariants

This repository is a research lab notebook exploring causal debugging, invariant violations, and failure prevention in concurrent backend systems.

## Research Claim

Recurring production failures persist because debugging practice focuses on *meaning invariants* (symptom constraints) instead of *transition invariants* (state-transition safety constraints) that prevent fault-producing execution paths.

## Causal Model

Error (human reasoning mistake) → Bug (latent system fault) → Failure (observable incorrect behavior)

## Objective

To develop a causal debugging methodology that shifts debugging from failure suppression to invariant-level fault prevention.

## Structure

- `/notes` — theory, models, and literature notes  
- `/experiments` — simulations and empirical validation  
- `/paper` — research documents and briefs
