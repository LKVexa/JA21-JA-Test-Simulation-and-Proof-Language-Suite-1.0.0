# JA21 JA Test, Simulation, and Proof Student Workbook

Preserve exact record IDs, source hashes, expected diagnostics, seeds, clocks, resource profiles, proof identities, and evidence scope.

## Chapter 1: Verification as a Language Suite

- State the invariant: every published result remains linked to source, oracle, environment, and receipt.
- Describe the failure: treating tests as disposable scripts with no provenance.
- Record the selected source SHA-256.
- Draw source → AST → judgment → R12 → executor/proof checker → MCRT.
- Produce accepted and rejected variants.
- Identify native tests and the certification boundary.

## Chapter 2: Program Anatomy, Modules, and Execution Policy

- State the invariant: every verification unit executes in a named module under explicit network and unknown-code rules.
- Describe the failure: implicit host authority or unlabeled execution context.
- Record the selected source SHA-256.
- Draw source → AST → judgment → R12 → executor/proof checker → MCRT.
- Produce accepted and rejected variants.
- Identify native tests and the certification boundary.

## Chapter 3: Fixtures, Generators, and Reproducible Inputs

- State the invariant: the same seed, constraints, and profile reproduce the same case stream.
- Describe the failure: hidden randomness and mutable shared fixtures.
- Record the selected source SHA-256.
- Draw source → AST → judgment → R12 → executor/proof checker → MCRT.
- Produce accepted and rejected variants.
- Identify native tests and the certification boundary.

## Chapter 4: Assertions, Matchers, and Typed Oracles

- State the invariant: an oracle has a declared type, comparison rule, tolerance, and failure explanation.
- Describe the failure: boolean-only checks that erase units, tolerances, or mismatch detail.
- Record the selected source SHA-256.
- Draw source → AST → judgment → R12 → executor/proof checker → MCRT.
- Produce accepted and rejected variants.
- Identify native tests and the certification boundary.

## Chapter 5: Unit, Parameterized, Integration, and Behavior Tests

- State the invariant: each test names its subject, dependencies, oracle, and isolation contract.
- Describe the failure: integration behavior disguised as a unit test or duplicate oracles.
- Record the selected source SHA-256.
- Draw source → AST → judgment → R12 → executor/proof checker → MCRT.
- Produce accepted and rejected variants.
- Identify native tests and the certification boundary.

## Chapter 6: Scenarios, Events, and Virtual Time

- State the invariant: event order and time advancement are explicit, deterministic, and replayable.
- Describe the failure: wall-clock dependence and ambiguous simultaneous events.
- Record the selected source SHA-256.
- Draw source → AST → judgment → R12 → executor/proof checker → MCRT.
- Produce accepted and rejected variants.
- Identify native tests and the certification boundary.

## Chapter 7: UI and Agent-Environment Simulation

- State the invariant: inputs, observations, actions, and environment transitions are typed and auditable.
- Describe the failure: unmodeled focus, hidden environment state, or unrestricted agent actions.
- Record the selected source SHA-256.
- Draw source → AST → judgment → R12 → executor/proof checker → MCRT.
- Produce accepted and rejected variants.
- Identify native tests and the certification boundary.

## Chapter 8: Network and Distributed Failure Simulation

- State the invariant: every injected fault has a declared time, scope, duration, and expected recovery condition.
- Describe the failure: random fault injection without replay identity or safety bounds.
- Record the selected source SHA-256.
- Draw source → AST → judgment → R12 → executor/proof checker → MCRT.
- Produce accepted and rejected variants.
- Identify native tests and the certification boundary.

## Chapter 9: Property Tests and Deterministic Generators

- State the invariant: generator domain, seed, precondition, property, and failure witness remain linked.
- Describe the failure: vacuous properties or generators that never reach boundary states.
- Record the selected source SHA-256.
- Draw source → AST → judgment → R12 → executor/proof checker → MCRT.
- Produce accepted and rejected variants.
- Identify native tests and the certification boundary.

## Chapter 10: Fuzzing, Shrinking, and Counterexamples

- State the invariant: a minimized counterexample preserves the original failure predicate and provenance.
- Describe the failure: shrinking that changes the failure or loses the original seed.
- Record the selected source SHA-256.
- Draw source → AST → judgment → R12 → executor/proof checker → MCRT.
- Produce accepted and rejected variants.
- Identify native tests and the certification boundary.

## Chapter 11: Invariants and Model Assertions

- State the invariant: invariants are evaluated at declared transitions and model boundaries.
- Describe the failure: checking only the final state or mixing assumptions with conclusions.
- Record the selected source SHA-256.
- Draw source → AST → judgment → R12 → executor/proof checker → MCRT.
- Produce accepted and rejected variants.
- Identify native tests and the certification boundary.

## Chapter 12: Theorems, Lemmas, and Proof Obligations

- State the invariant: theorem identity, assumptions, obligations, dependencies, and conclusion are explicit.
- Describe the failure: accepting a theorem because tests passed or because a dependency is unnamed.
- Record the selected source SHA-256.
- Draw source → AST → judgment → R12 → executor/proof checker → MCRT.
- Produce accepted and rejected variants.
- Identify native tests and the certification boundary.

## Chapter 13: Proof Terms and Checkable Evidence

- State the invariant: proof normalization preserves theorem identity, dependencies, and evidence hashes.
- Describe the failure: opaque “proved” flags or proof-term optimization that changes meaning.
- Record the selected source SHA-256.
- Draw source → AST → judgment → R12 → executor/proof checker → MCRT.
- Produce accepted and rejected variants.
- Identify native tests and the certification boundary.

## Chapter 14: Temporal Properties and Model Checking

- State the invariant: time semantics, transition relation, bound, and fairness assumptions are declared.
- Describe the failure: claiming liveness from finite examples without a model or bound.
- Record the selected source SHA-256.
- Draw source → AST → judgment → R12 → executor/proof checker → MCRT.
- Produce accepted and rejected variants.
- Identify native tests and the certification boundary.

## Chapter 15: Resource Limits and Benchmarks

- State the invariant: workload, warmup, repetitions, limits, host profile, and statistics are recorded.
- Describe the failure: unbounded benchmarks or performance claims without environment identity.
- Record the selected source SHA-256.
- Draw source → AST → judgment → R12 → executor/proof checker → MCRT.
- Produce accepted and rejected variants.
- Identify native tests and the certification boundary.

## Chapter 16: Source, AST, Runtime, and R12 Coverage

- State the invariant: coverage names the layer, target set, exclusions, and adequacy threshold.
- Describe the failure: using line coverage as proof of semantic or runtime completeness.
- Record the selected source SHA-256.
- Draw source → AST → judgment → R12 → executor/proof checker → MCRT.
- Produce accepted and rejected variants.
- Identify native tests and the certification boundary.

## Chapter 17: Typed Verification AST and Semantic Judgments

- State the invariant: types, effects, capabilities, seeds, clocks, obligations, and resource profiles survive lowering.
- Describe the failure: generic nodes that erase verification semantics.
- Record the selected source SHA-256.
- Draw source → AST → judgment → R12 → executor/proof checker → MCRT.
- Produce accepted and rejected variants.
- Identify native tests and the certification boundary.

## Chapter 18: Compiler Diagnostics and Negative Cases

- State the invariant: unsafe or ill-formed verification programs fail at the earliest responsible stage.
- Describe the failure: late runtime failure, unstable diagnostics, or silently weakened assertions.
- Record the selected source SHA-256.
- Draw source → AST → judgment → R12 → executor/proof checker → MCRT.
- Produce accepted and rejected variants.
- Identify native tests and the certification boundary.

## Chapter 19: Deterministic Verification Runtime and Replay

- State the invariant: identical source, seed, clock, faults, resources, and runtime profile reproduce the same result.
- Describe the failure: hidden wall time, nondeterministic ordering, or stale caches.
- Record the selected source SHA-256.
- Draw source → AST → judgment → R12 → executor/proof checker → MCRT.
- Produce accepted and rejected variants.
- Identify native tests and the certification boundary.

## Chapter 20: Optimization Without Verification Drift

- State the invariant: optimization preserves test oracles, counterexamples, theorem identity, failure schedule, and receipt.
- Describe the failure: deduplication or caching that erases a distinct obligation or failure.
- Record the selected source SHA-256.
- Draw source → AST → judgment → R12 → executor/proof checker → MCRT.
- Produce accepted and rejected variants.
- Identify native tests and the certification boundary.

## Chapter 21: R12, MCRT, Certification, and Smithson 8S

- State the invariant: modeled and native evidence remain distinct and limitations remain explicit.
- Describe the failure: promoting projected, simulated, or modeled outcomes into unsupported physical or production claims.
- Record the selected source SHA-256.
- Draw source → AST → judgment → R12 → executor/proof checker → MCRT.
- Produce accepted and rejected variants.
- Identify native tests and the certification boundary.

## Chapter 22: Standalone Test, Simulation, and Proof Toolchain Capstone

- State the invariant: the release is deterministic, air-gap-safe, independently auditable, and honest about evidence.
- Describe the failure: shipping a pass/fail dashboard without source, seeds, proofs, faults, resources, or receipts.
- Record the selected source SHA-256.
- Draw source → AST → judgment → R12 → executor/proof checker → MCRT.
- Produce accepted and rejected variants.
- Identify native tests and the certification boundary.
