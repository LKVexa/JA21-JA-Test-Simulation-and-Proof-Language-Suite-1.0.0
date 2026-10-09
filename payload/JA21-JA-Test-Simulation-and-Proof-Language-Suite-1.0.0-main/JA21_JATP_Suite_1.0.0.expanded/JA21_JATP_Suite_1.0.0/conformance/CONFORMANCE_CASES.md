# Conformance Cases

A conforming implementation should publish reproducible cases for:

1. A deterministic unit test with exact matcher output.
2. A parameterized test with stable case ordering.
3. A property test with fixed seed and minimal counterexample.
4. A fuzz target whose shrink trace preserves the failure predicate.
5. A virtual-time scenario with simultaneous-event ordering.
6. A network partition and recovery expectation.
7. A distributed failure with bounded resource use.
8. A theorem with lemma dependencies and checkable proof term.
9. A temporal safety property with counterexample trace.
10. Source, AST, runtime, and R12 coverage reports.
11. A benchmark with environment and statistics.
12. Deterministic replay yielding an identical MCRT identity.
13. Rejection of undeclared network or unknown-code execution.
14. Recovery from interrupted verification without losing the original witness.
