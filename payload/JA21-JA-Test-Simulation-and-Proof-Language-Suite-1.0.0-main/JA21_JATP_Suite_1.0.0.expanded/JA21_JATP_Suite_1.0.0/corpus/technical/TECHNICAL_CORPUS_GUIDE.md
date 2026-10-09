# JA21 JA Test, Simulation, and Proof Technical Corpus Guide

## Scope

This corpus contains **10,000 normalized JA Test, Simulation, and Proof Language records**. Every record preserves source, semantic interpretation, typed AST, compiler representation, R12 lowering, modeled verification-runtime evidence, MCRT identity, validation expectation, optimization notes, and Smithson 8S annotations.

## Evidence boundary

The corpus describes expected behavior. It does not prove that a native parser, compiler, simulator, model checker, proof checker, benchmark harness, coverage engine, or verification runtime executed a program. Native evidence must record exact tool identity, command, input hashes, output hashes, resource profile, sandbox policy, seed, virtual clock, replay identifier, and observed result.

## Reading a record

1. Start with `record_id`, `feature`, `level`, and `validation_class`.
2. Verify `source_sha256` before relying on the example.
3. Follow the semantic judgment into the typed AST and R12 record.
4. Compare compiler diagnostics with the modeled runtime result.
5. Inspect the MCRT receipt, determinism class, and evidence limitations.
6. Use the script catalog to locate the curated laboratory copy.

## Publication principles

- Tests are executable specifications, not decorative examples.
- Simulated time and injected failures must be explicit and replayable.
- Property tests require deterministic generators and shrinkers.
- Proof terms, theorems, lemmas, and obligations retain stable identities.
- Coverage metrics name the measured layer: source, AST, runtime, or R12.
- Benchmarks declare resource limits and measurement conditions.
- Counterexamples are preserved as first-class evidence.
- Modeled, structural, native, and certified evidence remain distinct.
