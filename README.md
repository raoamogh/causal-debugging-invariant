# Causal Debugging via Transition Invariants

> **A systems-level investigation into why recurring production failures persist — and how enforcing transition invariants eliminates fault-producing execution paths.**

This repository is a live research lab exploring causal debugging, invariant violations, and failure prevention in concurrent backend systems.

---

## Core Claim

Most recurring production failures persist because debugging practice focuses on **meaning invariants** (symptom constraints on observed state) rather than **transition invariants** (constraints on allowable state transitions).
While meaning invariants *detect* invalid states, transition invariants *prevent* fault-producing execution paths entirely.

---

## Causal Model

**Error → Bug → Failure**

* **Error:** Human reasoning mistake about system behavior
* **Bug:** Latent defect introduced into system design or code
* **Failure:** Observable incorrect runtime behavior

Debugging that targets failures suppresses symptoms.
Debugging that enforces transition invariants eliminates causal fault paths.

---

## Empirical Evidence

| Configuration                 | Failures Observed | Final Counter |
| ----------------------------- | ----------------- | ------------- |
| Without transition invariants | 3610              | 18            |
| With transition invariants    | **0**             | 39            |

This experiment demonstrates that enforcing transition invariants eliminates failure-producing execution paths entirely.

---

## Objective

To develop a causal debugging methodology that shifts debugging practice from symptom suppression to **invariant-level fault prevention**.

---

## Repository Structure

* `/notes` — theory, models, and literature notes
* `/experiments` — simulations and empirical validation
* `/paper` — research documents and briefs
