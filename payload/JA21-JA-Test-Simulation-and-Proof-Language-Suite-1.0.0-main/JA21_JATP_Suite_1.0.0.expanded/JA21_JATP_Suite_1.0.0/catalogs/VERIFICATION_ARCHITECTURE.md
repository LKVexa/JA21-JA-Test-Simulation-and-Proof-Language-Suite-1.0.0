# JA Test, Simulation, and Proof Architecture

```text
JA source (.jap)
  │
  ├─ fixtures / generators / matchers
  ├─ assertions / properties / invariants
  ├─ scenarios / simulations / failure injection
  ├─ theorems / lemmas / obligations / proof terms
  └─ coverage / benchmarks / resource limits
  │
  ▼
Parser → Resolver → Typed Verification AST
  │                    │
  │                    ├─ effects and capabilities
  │                    ├─ deterministic seed and virtual time
  │                    ├─ proof obligations and theorem identity
  │                    └─ resource and sandbox profile
  ▼
R12 verification plan
  │
  ├─ deterministic test executor
  ├─ simulation scheduler and failure injector
  ├─ property/fuzz engine and shrinker
  ├─ proof checker / model checker
  ├─ coverage and benchmark collectors
  └─ replay and recovery controller
  │
  ▼
MCRT verification receipt
```

## Architectural invariant

A verification result is publishable only when source identity, oracle, seed, virtual time, injected failures, resource profile, proof identity, R12 plan, runtime observations, and MCRT receipt agree. Missing evidence produces an explicit unresolved or rejected result, never a silent pass.
