# JA21 JA Test, Simulation, and Proof Language Textbook
## Verification Engineering, Deterministic Simulation, Formal Proof, and Evidence

**Edition:** 1.0.0  
**Suite:** JA21 JA Test, Simulation, and Proof Language Suite  
**Extension:** `.jap`  
**Evidence status:** corpus-modeled unless a separate native report is supplied.

## Preface

This textbook turns the uploaded JA Test, Simulation, and Proof Language corpus into a coherent course of study. It treats fixtures, assertions, property tests, fuzzing, shrinking, simulations, failure injection, theorems, proof obligations, proof terms, temporal properties, coverage, benchmarks, replay, and certification as one typed verification language. The 10,000-record corpus is the technical reference; the 1,000-program pack is the laboratory library; this book supplies the conceptual sequence and review discipline.

The five analytical roles are used throughout. **SOPHIA** examines semantic and systemic coherence. **CHARLOTTE** examines verification information architecture and diagnostic clarity. **LANDON** examines compiler, simulation, proof-checking, runtime, coverage, benchmark, sandbox, and replay feasibility. **Professor** examines pedagogy, counterexamples, and proof obligations. **Podium** examines publication, release integrity, limitations, and certification readiness.

## Contents

1. Verification as a Language Suite
2. Program Anatomy, Modules, and Execution Policy
3. Fixtures, Generators, and Reproducible Inputs
4. Assertions, Matchers, and Typed Oracles
5. Unit, Parameterized, Integration, and Behavior Tests
6. Scenarios, Events, and Virtual Time
7. UI and Agent-Environment Simulation
8. Network and Distributed Failure Simulation
9. Property Tests and Deterministic Generators
10. Fuzzing, Shrinking, and Counterexamples
11. Invariants and Model Assertions
12. Theorems, Lemmas, and Proof Obligations
13. Proof Terms and Checkable Evidence
14. Temporal Properties and Model Checking
15. Resource Limits and Benchmarks
16. Source, AST, Runtime, and R12 Coverage
17. Typed Verification AST and Semantic Judgments
18. Compiler Diagnostics and Negative Cases
19. Deterministic Verification Runtime and Replay
20. Optimization Without Verification Drift
21. R12, MCRT, Certification, and Smithson 8S
22. Standalone Test, Simulation, and Proof Toolchain Capstone

# Chapter 1: Verification as a Language Suite

## Learning objectives

- Explain tests, simulations, and proofs as one evidence-bearing language across source, semantics, AST, R12, runtime, and MCRT layers.
- State and test the invariant that every published result remains linked to source, oracle, environment, and receipt.
- Construct a positive case and a minimal counterexample involving treating tests as disposable scripts with no provenance.
- Separate modeled corpus evidence from native compiler, simulator, proof-checker, and runtime evidence.

## Technical foundation

This chapter treats **tests, simulations, and proofs as one evidence-bearing language** as a compiled language concern. In JA Test, Simulation, and Proof, a verification declaration is more than executable source: it is a stable claim connected to input construction, an oracle or proposition, typed semantics, a verification AST, an R12 execution or proof plan, a modeled runtime outcome, and an MCRT receipt. That chain makes a result reviewable before execution and reproducible after publication.

The central invariant is that **every published result remains linked to source, oracle, environment, and receipt**. The compiler must preserve this invariant during parsing, name resolution, type and effect analysis, proof-obligation generation, canonicalization, lowering, and optimization. The runtime must preserve it while scheduling tests, advancing virtual time, injecting failures, checking proofs, collecting coverage, measuring resources, shrinking counterexamples, and emitting receipts.

The principal counterexample is **treating tests as disposable scripts with no provenance**. Negative, boundary, security, determinism, recovery, and certification records are therefore essential. They define where the language must stop, which diagnostic should be stable, what evidence must remain unresolved, and which counterexample must survive minimization. Verification quality is measured as much by reliable rejection and honest uncertainty as by successful passes.

Implementation proceeds in explicit passes: parse stable source nodes; resolve fixtures, generators, tests, simulations, theorems, and dependencies; infer types, effects, capabilities, clocks, seeds, and resources; generate proof and replay obligations; lower accepted programs to R12; execute only inside the declared sandbox and virtual environment; preserve failures and counterexamples; and emit an MCRT verification receipt. Optimization is permitted only when this complete behavior remains equivalent.

## Representative corpus program

**Record:** `JATP-00311`  
**Feature:** `integration_test`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `87bf0ac8a69e15856a913ac3e9950adaa360b0ad60c923b43b86ad1d640f8fdd`

```jap
ja source 0.3
module corpus.ja_proof.example_00311
use Proof
policy no_network

fixture FixtureJATP_00311 {
    input 22
    expected 44
}
unit test FixtureCheckJATP_00311 {
    let fixture_result = FixtureJATP_00311.input * 2
    assert fixture_result == FixtureJATP_00311.expected
}
property PropertyJATP_00311 for_all x: Count where x <= 22 {
    let result = x * 2
    invariant result >= x
}
simulation FailureJATP_00311 {
    virtual_time 22s
    inject network.partition at 2s
    expect service.recovers within 5s
}
benchmark BenchJATP_00311 limit cpu 22ms memory 10MB
assert proof.complete == true
emit mcrt "PropertyJATP_00311.proof.mcrt"
```

## Evidence trace

- Semantic identity: `sem-11f2f7073bfff2ce85fa`
- Judgment: `Environment; Policy; {proof.check} ⊢ node-bec30434184e39e12a66 : VerificationBundle ! {state.read} ⇒ validated`
- AST node: `node-bec30434184e39e12a66` (`VerificationDecl`)
- Declared / inferred type: `VerificationBundle` / `VerificationBundle`
- Effects: `state.read`
- Capabilities: `proof.check`
- Semantic operator: `shrink`
- Policy decision: `allow`
- R12 record: `r12-da83c1aa4f9fdefe2e6d`
- MCRT record: `mcrt-885755f0efee07d4f026`
- Determinism class: `R3-Deterministic`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA reviews semantic coherence and whether the declared oracle or proposition actually expresses the intended claim. CHARLOTTE reviews the legibility of fixtures, scenarios, failure schedules, proof dependencies, diagnostics, and evidence navigation. LANDON reviews parser, compiler, scheduler, simulator, proof checker, coverage engine, benchmark harness, sandbox, and replay feasibility. Professor requires a stated invariant, minimal counterexample, and defensible test oracle. Podium requires checksums, provenance, limitations, release integrity, and a certification decision tied to exact artifacts.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Confirm the fixture or generator domain and oracle are explicit.
- Record seeds, virtual clock rules, injected failures, and resource limits.
- Preserve proof obligations, theorem dependencies, and counterexamples.
- Name the measured coverage layer and benchmark environment.
- Verify network and unknown-code execution are explicitly governed.
- Verify optimization preserves results, diagnostics, traces, and receipts.

## Laboratory

**Task:** Assemble a minimal verification suite and evidence map.

1. Copy the representative program into a separate laboratory module.
2. Write the invariant and evidence boundary before changing the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, diagnostic, R12 change, runtime result, and MCRT outcome.
5. Run structural validation; label remaining results modeled unless a native toolchain is used.
6. Submit source, seeds or proof inputs, expected results, evidence map, replay data, limitations, and certification decision.

## Review questions

1. What exact claim does this program verify?
2. Which identity or hash must change when the oracle, seed, failure schedule, or proof changes?
3. At what stage should the primary unsafe or invalid case be rejected?
4. Which optimization is safe, and which would erase verification meaning?
5. What native test would promote the modeled outcome into execution evidence?

# Chapter 2: Program Anatomy, Modules, and Execution Policy

## Learning objectives

- Explain headers, modules, Proof imports, policies, and emissions across source, semantics, AST, R12, runtime, and MCRT layers.
- State and test the invariant that every verification unit executes in a named module under explicit network and unknown-code rules.
- Construct a positive case and a minimal counterexample involving implicit host authority or unlabeled execution context.
- Separate modeled corpus evidence from native compiler, simulator, proof-checker, and runtime evidence.

## Technical foundation

This chapter treats **headers, modules, Proof imports, policies, and emissions** as a compiled language concern. In JA Test, Simulation, and Proof, a verification declaration is more than executable source: it is a stable claim connected to input construction, an oracle or proposition, typed semantics, a verification AST, an R12 execution or proof plan, a modeled runtime outcome, and an MCRT receipt. That chain makes a result reviewable before execution and reproducible after publication.

The central invariant is that **every verification unit executes in a named module under explicit network and unknown-code rules**. The compiler must preserve this invariant during parsing, name resolution, type and effect analysis, proof-obligation generation, canonicalization, lowering, and optimization. The runtime must preserve it while scheduling tests, advancing virtual time, injecting failures, checking proofs, collecting coverage, measuring resources, shrinking counterexamples, and emitting receipts.

The principal counterexample is **implicit host authority or unlabeled execution context**. Negative, boundary, security, determinism, recovery, and certification records are therefore essential. They define where the language must stop, which diagnostic should be stable, what evidence must remain unresolved, and which counterexample must survive minimization. Verification quality is measured as much by reliable rejection and honest uncertainty as by successful passes.

Implementation proceeds in explicit passes: parse stable source nodes; resolve fixtures, generators, tests, simulations, theorems, and dependencies; infer types, effects, capabilities, clocks, seeds, and resources; generate proof and replay obligations; lower accepted programs to R12; execute only inside the declared sandbox and virtual environment; preserve failures and counterexamples; and emit an MCRT verification receipt. Optimization is permitted only when this complete behavior remains equivalent.

## Representative corpus program

**Record:** `JATP-00028`  
**Feature:** `fixture`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `a1f10451f8e331f9958f803964c8e686681e3499e0abd8690e2051af8bf05819`

```jap
ja source 0.3
module corpus.ja_proof.example_00028
use Proof
policy no_network

fixture FixtureJATP_00028 {
    input 30
    expected 870
}
unit test FixtureCheckJATP_00028 {
    let fixture_result = FixtureJATP_00028.input * 29
    assert fixture_result == FixtureJATP_00028.expected
}
property PropertyJATP_00028 for_all x: Count where x <= 30 {
    let result = x * 29
    invariant result >= x
}
simulation FailureJATP_00028 {
    virtual_time 30s
    inject network.partition at 29s
    expect service.recovers within 32s
}
benchmark BenchJATP_00028 limit cpu 30ms memory 37MB
assert proof.complete == true
emit mcrt "PropertyJATP_00028.proof.mcrt"
```

## Evidence trace

- Semantic identity: `sem-8ee1802ea369796a81b7`
- Judgment: `Environment; Policy; {benchmark.run:bounded} ⊢ node-f490890f263dec480140 : VerificationBundle ! {state.write} ⇒ validated`
- AST node: `node-f490890f263dec480140` (`VerificationDecl`)
- Declared / inferred type: `VerificationBundle` / `VerificationBundle`
- Effects: `state.write`
- Capabilities: `benchmark.run:bounded`
- Semantic operator: `generate`
- Policy decision: `allow`
- R12 record: `r12-cb4c2c5934fa5f97e717`
- MCRT record: `mcrt-e79fdf0b4776b79298d6`
- Determinism class: `R3-Deterministic`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA reviews semantic coherence and whether the declared oracle or proposition actually expresses the intended claim. CHARLOTTE reviews the legibility of fixtures, scenarios, failure schedules, proof dependencies, diagnostics, and evidence navigation. LANDON reviews parser, compiler, scheduler, simulator, proof checker, coverage engine, benchmark harness, sandbox, and replay feasibility. Professor requires a stated invariant, minimal counterexample, and defensible test oracle. Podium requires checksums, provenance, limitations, release integrity, and a certification decision tied to exact artifacts.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Confirm the fixture or generator domain and oracle are explicit.
- Record seeds, virtual clock rules, injected failures, and resource limits.
- Preserve proof obligations, theorem dependencies, and counterexamples.
- Name the measured coverage layer and benchmark environment.
- Verify network and unknown-code execution are explicitly governed.
- Verify optimization preserves results, diagnostics, traces, and receipts.

## Laboratory

**Task:** Compare a valid module with an undeclared-authority variant.

1. Copy the representative program into a separate laboratory module.
2. Write the invariant and evidence boundary before changing the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, diagnostic, R12 change, runtime result, and MCRT outcome.
5. Run structural validation; label remaining results modeled unless a native toolchain is used.
6. Submit source, seeds or proof inputs, expected results, evidence map, replay data, limitations, and certification decision.

## Review questions

1. What exact claim does this program verify?
2. Which identity or hash must change when the oracle, seed, failure schedule, or proof changes?
3. At what stage should the primary unsafe or invalid case be rejected?
4. Which optimization is safe, and which would erase verification meaning?
5. What native test would promote the modeled outcome into execution evidence?

# Chapter 3: Fixtures, Generators, and Reproducible Inputs

## Learning objectives

- Explain reusable inputs and deterministic generated values across source, semantics, AST, R12, runtime, and MCRT layers.
- State and test the invariant that the same seed, constraints, and profile reproduce the same case stream.
- Construct a positive case and a minimal counterexample involving hidden randomness and mutable shared fixtures.
- Separate modeled corpus evidence from native compiler, simulator, proof-checker, and runtime evidence.

## Technical foundation

This chapter treats **reusable inputs and deterministic generated values** as a compiled language concern. In JA Test, Simulation, and Proof, a verification declaration is more than executable source: it is a stable claim connected to input construction, an oracle or proposition, typed semantics, a verification AST, an R12 execution or proof plan, a modeled runtime outcome, and an MCRT receipt. That chain makes a result reviewable before execution and reproducible after publication.

The central invariant is that **the same seed, constraints, and profile reproduce the same case stream**. The compiler must preserve this invariant during parsing, name resolution, type and effect analysis, proof-obligation generation, canonicalization, lowering, and optimization. The runtime must preserve it while scheduling tests, advancing virtual time, injecting failures, checking proofs, collecting coverage, measuring resources, shrinking counterexamples, and emitting receipts.

The principal counterexample is **hidden randomness and mutable shared fixtures**. Negative, boundary, security, determinism, recovery, and certification records are therefore essential. They define where the language must stop, which diagnostic should be stable, what evidence must remain unresolved, and which counterexample must survive minimization. Verification quality is measured as much by reliable rejection and honest uncertainty as by successful passes.

Implementation proceeds in explicit passes: parse stable source nodes; resolve fixtures, generators, tests, simulations, theorems, and dependencies; infer types, effects, capabilities, clocks, seeds, and resources; generate proof and replay obligations; lower accepted programs to R12; execute only inside the declared sandbox and virtual environment; preserve failures and counterexamples; and emit an MCRT verification receipt. Optimization is permitted only when this complete behavior remains equivalent.

## Representative corpus program

**Record:** `JATP-00161`  
**Feature:** `generator`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `ee4cfafd7be5ef5669c4e4325609e5ba025f46f862d6cec871c007c9b6ac65c1`

```jap
ja source 0.3
module corpus.ja_proof.example_00161
use Proof
policy no_network

fixture FixtureJATP_00161 {
    input 66
    expected 462
}
unit test FixtureCheckJATP_00161 {
    let fixture_result = FixtureJATP_00161.input * 7
    assert fixture_result == FixtureJATP_00161.expected
}
property PropertyJATP_00161 for_all x: Count where x <= 66 {
    let result = x * 7
    invariant result >= x
}
simulation FailureJATP_00161 {
    virtual_time 66s
    inject network.partition at 7s
    expect service.recovers within 10s
}
benchmark BenchJATP_00161 limit cpu 66ms memory 15MB
assert proof.complete == true
emit mcrt "PropertyJATP_00161.proof.mcrt"
```

## Evidence trace

- Semantic identity: `sem-1183184efb2d0b41442a`
- Judgment: `Environment; Policy; {proof.check} ⊢ node-bda18d45e099e5749685 : VerificationBundle ! {state.read} ⇒ validated`
- AST node: `node-bda18d45e099e5749685` (`VerificationDecl`)
- Declared / inferred type: `VerificationBundle` / `VerificationBundle`
- Effects: `state.read`
- Capabilities: `proof.check`
- Semantic operator: `shrink`
- Policy decision: `allow`
- R12 record: `r12-ccb772145291ba49c38f`
- MCRT record: `mcrt-9d211e6923cf1cbf0607`
- Determinism class: `R3-Deterministic`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA reviews semantic coherence and whether the declared oracle or proposition actually expresses the intended claim. CHARLOTTE reviews the legibility of fixtures, scenarios, failure schedules, proof dependencies, diagnostics, and evidence navigation. LANDON reviews parser, compiler, scheduler, simulator, proof checker, coverage engine, benchmark harness, sandbox, and replay feasibility. Professor requires a stated invariant, minimal counterexample, and defensible test oracle. Podium requires checksums, provenance, limitations, release integrity, and a certification decision tied to exact artifacts.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Confirm the fixture or generator domain and oracle are explicit.
- Record seeds, virtual clock rules, injected failures, and resource limits.
- Preserve proof obligations, theorem dependencies, and counterexamples.
- Name the measured coverage layer and benchmark environment.
- Verify network and unknown-code execution are explicitly governed.
- Verify optimization preserves results, diagnostics, traces, and receipts.

## Laboratory

**Task:** Build a fixture and generator with replay evidence.

1. Copy the representative program into a separate laboratory module.
2. Write the invariant and evidence boundary before changing the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, diagnostic, R12 change, runtime result, and MCRT outcome.
5. Run structural validation; label remaining results modeled unless a native toolchain is used.
6. Submit source, seeds or proof inputs, expected results, evidence map, replay data, limitations, and certification decision.

## Review questions

1. What exact claim does this program verify?
2. Which identity or hash must change when the oracle, seed, failure schedule, or proof changes?
3. At what stage should the primary unsafe or invalid case be rejected?
4. Which optimization is safe, and which would erase verification meaning?
5. What native test would promote the modeled outcome into execution evidence?

# Chapter 4: Assertions, Matchers, and Typed Oracles

## Learning objectives

- Explain precise expected behavior and diagnostics across source, semantics, AST, R12, runtime, and MCRT layers.
- State and test the invariant that an oracle has a declared type, comparison rule, tolerance, and failure explanation.
- Construct a positive case and a minimal counterexample involving boolean-only checks that erase units, tolerances, or mismatch detail.
- Separate modeled corpus evidence from native compiler, simulator, proof-checker, and runtime evidence.

## Technical foundation

This chapter treats **precise expected behavior and diagnostics** as a compiled language concern. In JA Test, Simulation, and Proof, a verification declaration is more than executable source: it is a stable claim connected to input construction, an oracle or proposition, typed semantics, a verification AST, an R12 execution or proof plan, a modeled runtime outcome, and an MCRT receipt. That chain makes a result reviewable before execution and reproducible after publication.

The central invariant is that **an oracle has a declared type, comparison rule, tolerance, and failure explanation**. The compiler must preserve this invariant during parsing, name resolution, type and effect analysis, proof-obligation generation, canonicalization, lowering, and optimization. The runtime must preserve it while scheduling tests, advancing virtual time, injecting failures, checking proofs, collecting coverage, measuring resources, shrinking counterexamples, and emitting receipts.

The principal counterexample is **boolean-only checks that erase units, tolerances, or mismatch detail**. Negative, boundary, security, determinism, recovery, and certification records are therefore essential. They define where the language must stop, which diagnostic should be stable, what evidence must remain unresolved, and which counterexample must survive minimization. Verification quality is measured as much by reliable rejection and honest uncertainty as by successful passes.

Implementation proceeds in explicit passes: parse stable source nodes; resolve fixtures, generators, tests, simulations, theorems, and dependencies; infer types, effects, capabilities, clocks, seeds, and resources; generate proof and replay obligations; lower accepted programs to R12; execute only inside the declared sandbox and virtual environment; preserve failures and counterexamples; and emit an MCRT verification receipt. Optimization is permitted only when this complete behavior remains equivalent.

## Representative corpus program

**Record:** `JATP-00261`  
**Feature:** `matcher`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `d7b81b933443fa71b4c57b4a2fc6fd862781d9919400cd502f33deb72a52c38b`

```jap
ja source 0.3
module corpus.ja_proof.example_00261
use Proof
policy no_network

fixture FixtureJATP_00261 {
    input 69
    expected 966
}
unit test FixtureCheckJATP_00261 {
    let fixture_result = FixtureJATP_00261.input * 14
    assert fixture_result == FixtureJATP_00261.expected
}
property PropertyJATP_00261 for_all x: Count where x <= 69 {
    let result = x * 14
    invariant result >= x
}
simulation FailureJATP_00261 {
    virtual_time 69s
    inject network.partition at 14s
    expect service.recovers within 17s
}
benchmark BenchJATP_00261 limit cpu 69ms memory 22MB
assert proof.complete == true
emit mcrt "PropertyJATP_00261.proof.mcrt"
```

## Evidence trace

- Semantic identity: `sem-fcc4926e4763ff6a4de9`
- Judgment: `Environment; Policy; {fuzz.run:isolated} ⊢ node-5538c57b2c06896612e9 : VerificationBundle ! {process.spawn} ⇒ validated`
- AST node: `node-5538c57b2c06896612e9` (`VerificationDecl`)
- Declared / inferred type: `VerificationBundle` / `VerificationBundle`
- Effects: `process.spawn`
- Capabilities: `fuzz.run:isolated`
- Semantic operator: `shrink`
- Policy decision: `allow`
- R12 record: `r12-2e59e51c491dbd1fc07b`
- MCRT record: `mcrt-c93146f48d27f83e0247`
- Determinism class: `R3-Deterministic`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA reviews semantic coherence and whether the declared oracle or proposition actually expresses the intended claim. CHARLOTTE reviews the legibility of fixtures, scenarios, failure schedules, proof dependencies, diagnostics, and evidence navigation. LANDON reviews parser, compiler, scheduler, simulator, proof checker, coverage engine, benchmark harness, sandbox, and replay feasibility. Professor requires a stated invariant, minimal counterexample, and defensible test oracle. Podium requires checksums, provenance, limitations, release integrity, and a certification decision tied to exact artifacts.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Confirm the fixture or generator domain and oracle are explicit.
- Record seeds, virtual clock rules, injected failures, and resource limits.
- Preserve proof obligations, theorem dependencies, and counterexamples.
- Name the measured coverage layer and benchmark environment.
- Verify network and unknown-code execution are explicitly governed.
- Verify optimization preserves results, diagnostics, traces, and receipts.

## Laboratory

**Task:** Design typed matchers and a minimal failing witness.

1. Copy the representative program into a separate laboratory module.
2. Write the invariant and evidence boundary before changing the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, diagnostic, R12 change, runtime result, and MCRT outcome.
5. Run structural validation; label remaining results modeled unless a native toolchain is used.
6. Submit source, seeds or proof inputs, expected results, evidence map, replay data, limitations, and certification decision.

## Review questions

1. What exact claim does this program verify?
2. Which identity or hash must change when the oracle, seed, failure schedule, or proof changes?
3. At what stage should the primary unsafe or invalid case be rejected?
4. Which optimization is safe, and which would erase verification meaning?
5. What native test would promote the modeled outcome into execution evidence?

# Chapter 5: Unit, Parameterized, Integration, and Behavior Tests

## Learning objectives

- Explain layered testing scopes and responsibility boundaries across source, semantics, AST, R12, runtime, and MCRT layers.
- State and test the invariant that each test names its subject, dependencies, oracle, and isolation contract.
- Construct a positive case and a minimal counterexample involving integration behavior disguised as a unit test or duplicate oracles.
- Separate modeled corpus evidence from native compiler, simulator, proof-checker, and runtime evidence.

## Technical foundation

This chapter treats **layered testing scopes and responsibility boundaries** as a compiled language concern. In JA Test, Simulation, and Proof, a verification declaration is more than executable source: it is a stable claim connected to input construction, an oracle or proposition, typed semantics, a verification AST, an R12 execution or proof plan, a modeled runtime outcome, and an MCRT receipt. That chain makes a result reviewable before execution and reproducible after publication.

The central invariant is that **each test names its subject, dependencies, oracle, and isolation contract**. The compiler must preserve this invariant during parsing, name resolution, type and effect analysis, proof-obligation generation, canonicalization, lowering, and optimization. The runtime must preserve it while scheduling tests, advancing virtual time, injecting failures, checking proofs, collecting coverage, measuring resources, shrinking counterexamples, and emitting receipts.

The principal counterexample is **integration behavior disguised as a unit test or duplicate oracles**. Negative, boundary, security, determinism, recovery, and certification records are therefore essential. They define where the language must stop, which diagnostic should be stable, what evidence must remain unresolved, and which counterexample must survive minimization. Verification quality is measured as much by reliable rejection and honest uncertainty as by successful passes.

Implementation proceeds in explicit passes: parse stable source nodes; resolve fixtures, generators, tests, simulations, theorems, and dependencies; infer types, effects, capabilities, clocks, seeds, and resources; generate proof and replay obligations; lower accepted programs to R12; execute only inside the declared sandbox and virtual environment; preserve failures and counterexamples; and emit an MCRT verification receipt. Optimization is permitted only when this complete behavior remains equivalent.

## Representative corpus program

**Record:** `JATP-00032`  
**Feature:** `unit_test`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `7a2060d6c04d8abec4d3b27ec584dd69e01bce35c6f3dd29032fc51cfea1c20b`

```jap
ja source 0.3
module corpus.ja_proof.example_00032
use Proof
policy no_network

fixture FixtureJATP_00032 {
    input 34
    expected 68
}
unit test FixtureCheckJATP_00032 {
    let fixture_result = FixtureJATP_00032.input * 2
    assert fixture_result == FixtureJATP_00032.expected
}
property PropertyJATP_00032 for_all x: Count where x <= 34 {
    let result = x * 2
    invariant result >= x
}
simulation FailureJATP_00032 {
    virtual_time 34s
    inject network.partition at 2s
    expect service.recovers within 5s
}
benchmark BenchJATP_00032 limit cpu 34ms memory 10MB
assert proof.complete == true
emit mcrt "PropertyJATP_00032.proof.mcrt"
```

## Evidence trace

- Semantic identity: `sem-efbd5ebe3207a424adce`
- Judgment: `Environment; Policy; {ledger.append} ⊢ node-4000e6746b06f8503eba : VerificationBundle ! {device.cpu} ⇒ validated`
- AST node: `node-4000e6746b06f8503eba` (`VerificationDecl`)
- Declared / inferred type: `VerificationBundle` / `VerificationBundle`
- Effects: `device.cpu`
- Capabilities: `ledger.append`
- Semantic operator: `test_declare`
- Policy decision: `allow`
- R12 record: `r12-f59bce94c5d619c69ef6`
- MCRT record: `mcrt-cd6552d8207a7ea26c2f`
- Determinism class: `R3-Deterministic`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA reviews semantic coherence and whether the declared oracle or proposition actually expresses the intended claim. CHARLOTTE reviews the legibility of fixtures, scenarios, failure schedules, proof dependencies, diagnostics, and evidence navigation. LANDON reviews parser, compiler, scheduler, simulator, proof checker, coverage engine, benchmark harness, sandbox, and replay feasibility. Professor requires a stated invariant, minimal counterexample, and defensible test oracle. Podium requires checksums, provenance, limitations, release integrity, and a certification decision tied to exact artifacts.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Confirm the fixture or generator domain and oracle are explicit.
- Record seeds, virtual clock rules, injected failures, and resource limits.
- Preserve proof obligations, theorem dependencies, and counterexamples.
- Name the measured coverage layer and benchmark environment.
- Verify network and unknown-code execution are explicitly governed.
- Verify optimization preserves results, diagnostics, traces, and receipts.

## Laboratory

**Task:** Refactor one behavior into four correctly scoped tests.

1. Copy the representative program into a separate laboratory module.
2. Write the invariant and evidence boundary before changing the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, diagnostic, R12 change, runtime result, and MCRT outcome.
5. Run structural validation; label remaining results modeled unless a native toolchain is used.
6. Submit source, seeds or proof inputs, expected results, evidence map, replay data, limitations, and certification decision.

## Review questions

1. What exact claim does this program verify?
2. Which identity or hash must change when the oracle, seed, failure schedule, or proof changes?
3. At what stage should the primary unsafe or invalid case be rejected?
4. Which optimization is safe, and which would erase verification meaning?
5. What native test would promote the modeled outcome into execution evidence?

# Chapter 6: Scenarios, Events, and Virtual Time

## Learning objectives

- Explain ordered situations, event schedules, and controlled clocks across source, semantics, AST, R12, runtime, and MCRT layers.
- State and test the invariant that event order and time advancement are explicit, deterministic, and replayable.
- Construct a positive case and a minimal counterexample involving wall-clock dependence and ambiguous simultaneous events.
- Separate modeled corpus evidence from native compiler, simulator, proof-checker, and runtime evidence.

## Technical foundation

This chapter treats **ordered situations, event schedules, and controlled clocks** as a compiled language concern. In JA Test, Simulation, and Proof, a verification declaration is more than executable source: it is a stable claim connected to input construction, an oracle or proposition, typed semantics, a verification AST, an R12 execution or proof plan, a modeled runtime outcome, and an MCRT receipt. That chain makes a result reviewable before execution and reproducible after publication.

The central invariant is that **event order and time advancement are explicit, deterministic, and replayable**. The compiler must preserve this invariant during parsing, name resolution, type and effect analysis, proof-obligation generation, canonicalization, lowering, and optimization. The runtime must preserve it while scheduling tests, advancing virtual time, injecting failures, checking proofs, collecting coverage, measuring resources, shrinking counterexamples, and emitting receipts.

The principal counterexample is **wall-clock dependence and ambiguous simultaneous events**. Negative, boundary, security, determinism, recovery, and certification records are therefore essential. They define where the language must stop, which diagnostic should be stable, what evidence must remain unresolved, and which counterexample must survive minimization. Verification quality is measured as much by reliable rejection and honest uncertainty as by successful passes.

Implementation proceeds in explicit passes: parse stable source nodes; resolve fixtures, generators, tests, simulations, theorems, and dependencies; infer types, effects, capabilities, clocks, seeds, and resources; generate proof and replay obligations; lower accepted programs to R12; execute only inside the declared sandbox and virtual environment; preserve failures and counterexamples; and emit an MCRT verification receipt. Optimization is permitted only when this complete behavior remains equivalent.

## Representative corpus program

**Record:** `JATP-00006`  
**Feature:** `scenario_test`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `222ab4c688c1dfc442dd8bf77c8fdaf0d0bb47fc3f3a36816831115e256422d3`

```jap
ja source 0.3
module corpus.ja_proof.example_00006
use Proof
policy no_network

fixture FixtureJATP_00006 {
    input 8
    expected 56
}
unit test FixtureCheckJATP_00006 {
    let fixture_result = FixtureJATP_00006.input * 7
    assert fixture_result == FixtureJATP_00006.expected
}
property PropertyJATP_00006 for_all x: Count where x <= 8 {
    let result = x * 7
    invariant result >= x
}
simulation FailureJATP_00006 {
    virtual_time 8s
    inject network.partition at 7s
    expect service.recovers within 10s
}
benchmark BenchJATP_00006 limit cpu 8ms memory 15MB
assert proof.complete == true
emit mcrt "PropertyJATP_00006.proof.mcrt"
```

## Evidence trace

- Semantic identity: `sem-f21db79e35ff84bd2f5e`
- Judgment: `Environment; Policy; {simulation.execute} ⊢ node-ead0b1ac2ba2d0e672b0 : VerificationBundle ! {pure} ⇒ validated`
- AST node: `node-ead0b1ac2ba2d0e672b0` (`VerificationDecl`)
- Declared / inferred type: `VerificationBundle` / `VerificationBundle`
- Effects: `pure`
- Capabilities: `simulation.execute`
- Semantic operator: `benchmark`
- Policy decision: `allow`
- R12 record: `r12-f78ab2a22e265737c3a5`
- MCRT record: `mcrt-95440397fb4ab61b8eb7`
- Determinism class: `R3-Deterministic`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA reviews semantic coherence and whether the declared oracle or proposition actually expresses the intended claim. CHARLOTTE reviews the legibility of fixtures, scenarios, failure schedules, proof dependencies, diagnostics, and evidence navigation. LANDON reviews parser, compiler, scheduler, simulator, proof checker, coverage engine, benchmark harness, sandbox, and replay feasibility. Professor requires a stated invariant, minimal counterexample, and defensible test oracle. Podium requires checksums, provenance, limitations, release integrity, and a certification decision tied to exact artifacts.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Confirm the fixture or generator domain and oracle are explicit.
- Record seeds, virtual clock rules, injected failures, and resource limits.
- Preserve proof obligations, theorem dependencies, and counterexamples.
- Name the measured coverage layer and benchmark environment.
- Verify network and unknown-code execution are explicitly governed.
- Verify optimization preserves results, diagnostics, traces, and receipts.

## Laboratory

**Task:** Construct a scenario with a virtual event timeline.

1. Copy the representative program into a separate laboratory module.
2. Write the invariant and evidence boundary before changing the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, diagnostic, R12 change, runtime result, and MCRT outcome.
5. Run structural validation; label remaining results modeled unless a native toolchain is used.
6. Submit source, seeds or proof inputs, expected results, evidence map, replay data, limitations, and certification decision.

## Review questions

1. What exact claim does this program verify?
2. Which identity or hash must change when the oracle, seed, failure schedule, or proof changes?
3. At what stage should the primary unsafe or invalid case be rejected?
4. Which optimization is safe, and which would erase verification meaning?
5. What native test would promote the modeled outcome into execution evidence?

# Chapter 7: UI and Agent-Environment Simulation

## Learning objectives

- Explain interaction state, focus, agent observations, and governed actions across source, semantics, AST, R12, runtime, and MCRT layers.
- State and test the invariant that inputs, observations, actions, and environment transitions are typed and auditable.
- Construct a positive case and a minimal counterexample involving unmodeled focus, hidden environment state, or unrestricted agent actions.
- Separate modeled corpus evidence from native compiler, simulator, proof-checker, and runtime evidence.

## Technical foundation

This chapter treats **interaction state, focus, agent observations, and governed actions** as a compiled language concern. In JA Test, Simulation, and Proof, a verification declaration is more than executable source: it is a stable claim connected to input construction, an oracle or proposition, typed semantics, a verification AST, an R12 execution or proof plan, a modeled runtime outcome, and an MCRT receipt. That chain makes a result reviewable before execution and reproducible after publication.

The central invariant is that **inputs, observations, actions, and environment transitions are typed and auditable**. The compiler must preserve this invariant during parsing, name resolution, type and effect analysis, proof-obligation generation, canonicalization, lowering, and optimization. The runtime must preserve it while scheduling tests, advancing virtual time, injecting failures, checking proofs, collecting coverage, measuring resources, shrinking counterexamples, and emitting receipts.

The principal counterexample is **unmodeled focus, hidden environment state, or unrestricted agent actions**. Negative, boundary, security, determinism, recovery, and certification records are therefore essential. They define where the language must stop, which diagnostic should be stable, what evidence must remain unresolved, and which counterexample must survive minimization. Verification quality is measured as much by reliable rejection and honest uncertainty as by successful passes.

Implementation proceeds in explicit passes: parse stable source nodes; resolve fixtures, generators, tests, simulations, theorems, and dependencies; infer types, effects, capabilities, clocks, seeds, and resources; generate proof and replay obligations; lower accepted programs to R12; execute only inside the declared sandbox and virtual environment; preserve failures and counterexamples; and emit an MCRT verification receipt. Optimization is permitted only when this complete behavior remains equivalent.

## Representative corpus program

**Record:** `JATP-00231`  
**Feature:** `ui_interaction_simulation`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `4956c8426f53d063df596379a561a0d8f01f8d549417675a1cc69669f93d09c1`

```jap
ja source 0.3
module corpus.ja_proof.example_00231
use Proof
policy no_network

fixture FixtureJATP_00231 {
    input 39
    expected 585
}
unit test FixtureCheckJATP_00231 {
    let fixture_result = FixtureJATP_00231.input * 15
    assert fixture_result == FixtureJATP_00231.expected
}
property PropertyJATP_00231 for_all x: Count where x <= 39 {
    let result = x * 15
    invariant result >= x
}
simulation FailureJATP_00231 {
    virtual_time 39s
    inject network.partition at 15s
    expect service.recovers within 18s
}
benchmark BenchJATP_00231 limit cpu 39ms memory 23MB
assert proof.complete == true
emit mcrt "PropertyJATP_00231.proof.mcrt"
```

## Evidence trace

- Semantic identity: `sem-d87c019cbd66df317caa`
- Judgment: `Environment; Policy; {fuzz.run:isolated} ⊢ node-4a89169c7b80e98d8f28 : VerificationBundle ! {process.spawn} ⇒ validated`
- AST node: `node-4a89169c7b80e98d8f28` (`VerificationDecl`)
- Declared / inferred type: `VerificationBundle` / `VerificationBundle`
- Effects: `process.spawn`
- Capabilities: `fuzz.run:isolated`
- Semantic operator: `shrink`
- Policy decision: `allow`
- R12 record: `r12-8b06db83a9043b73daec`
- MCRT record: `mcrt-6ec8e46f6ac6ebae1efc`
- Determinism class: `R3-Deterministic`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA reviews semantic coherence and whether the declared oracle or proposition actually expresses the intended claim. CHARLOTTE reviews the legibility of fixtures, scenarios, failure schedules, proof dependencies, diagnostics, and evidence navigation. LANDON reviews parser, compiler, scheduler, simulator, proof checker, coverage engine, benchmark harness, sandbox, and replay feasibility. Professor requires a stated invariant, minimal counterexample, and defensible test oracle. Podium requires checksums, provenance, limitations, release integrity, and a certification decision tied to exact artifacts.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Confirm the fixture or generator domain and oracle are explicit.
- Record seeds, virtual clock rules, injected failures, and resource limits.
- Preserve proof obligations, theorem dependencies, and counterexamples.
- Name the measured coverage layer and benchmark environment.
- Verify network and unknown-code execution are explicitly governed.
- Verify optimization preserves results, diagnostics, traces, and receipts.

## Laboratory

**Task:** Simulate a bounded interface and agent workflow.

1. Copy the representative program into a separate laboratory module.
2. Write the invariant and evidence boundary before changing the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, diagnostic, R12 change, runtime result, and MCRT outcome.
5. Run structural validation; label remaining results modeled unless a native toolchain is used.
6. Submit source, seeds or proof inputs, expected results, evidence map, replay data, limitations, and certification decision.

## Review questions

1. What exact claim does this program verify?
2. Which identity or hash must change when the oracle, seed, failure schedule, or proof changes?
3. At what stage should the primary unsafe or invalid case be rejected?
4. Which optimization is safe, and which would erase verification meaning?
5. What native test would promote the modeled outcome into execution evidence?

# Chapter 8: Network and Distributed Failure Simulation

## Learning objectives

- Explain partitions, loss, delay, node failure, and recovery across source, semantics, AST, R12, runtime, and MCRT layers.
- State and test the invariant that every injected fault has a declared time, scope, duration, and expected recovery condition.
- Construct a positive case and a minimal counterexample involving random fault injection without replay identity or safety bounds.
- Separate modeled corpus evidence from native compiler, simulator, proof-checker, and runtime evidence.

## Technical foundation

This chapter treats **partitions, loss, delay, node failure, and recovery** as a compiled language concern. In JA Test, Simulation, and Proof, a verification declaration is more than executable source: it is a stable claim connected to input construction, an oracle or proposition, typed semantics, a verification AST, an R12 execution or proof plan, a modeled runtime outcome, and an MCRT receipt. That chain makes a result reviewable before execution and reproducible after publication.

The central invariant is that **every injected fault has a declared time, scope, duration, and expected recovery condition**. The compiler must preserve this invariant during parsing, name resolution, type and effect analysis, proof-obligation generation, canonicalization, lowering, and optimization. The runtime must preserve it while scheduling tests, advancing virtual time, injecting failures, checking proofs, collecting coverage, measuring resources, shrinking counterexamples, and emitting receipts.

The principal counterexample is **random fault injection without replay identity or safety bounds**. Negative, boundary, security, determinism, recovery, and certification records are therefore essential. They define where the language must stop, which diagnostic should be stable, what evidence must remain unresolved, and which counterexample must survive minimization. Verification quality is measured as much by reliable rejection and honest uncertainty as by successful passes.

Implementation proceeds in explicit passes: parse stable source nodes; resolve fixtures, generators, tests, simulations, theorems, and dependencies; infer types, effects, capabilities, clocks, seeds, and resources; generate proof and replay obligations; lower accepted programs to R12; execute only inside the declared sandbox and virtual environment; preserve failures and counterexamples; and emit an MCRT verification receipt. Optimization is permitted only when this complete behavior remains equivalent.

## Representative corpus program

**Record:** `JATP-00002`  
**Feature:** `network_failure_simulation`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `b89fa58b7b5340b5cd3c3cc234c93642bf8075c19c796499bd3aa427fa1f9181`

```jap
ja source 0.3
module corpus.ja_proof.example_00002
use Proof
policy explicit_network

fixture FixtureJATP_00002 {
    input 4
    expected 12
}
unit test FixtureCheckJATP_00002 {
    let fixture_result = FixtureJATP_00002.input * 3
    assert fixture_result == FixtureJATP_00002.expected
}
property PropertyJATP_00002 for_all x: Count where x <= 4 {
    let result = x * 3
    invariant result >= x
}
simulation FailureJATP_00002 {
    virtual_time 4s
    inject network.partition at 3s
    expect service.recovers within 6s
}
benchmark BenchJATP_00002 limit cpu 4ms memory 11MB
assert proof.complete == true
emit mcrt "PropertyJATP_00002.proof.mcrt"
```

## Evidence trace

- Semantic identity: `sem-ca303ec52dda6c3b2ec2`
- Judgment: `Environment; Policy; {ledger.append} ⊢ node-8efca8b3c6eed84630f9 : VerificationBundle ! {device.cpu} ⇒ validated`
- AST node: `node-8efca8b3c6eed84630f9` (`VerificationDecl`)
- Declared / inferred type: `VerificationBundle` / `VerificationBundle`
- Effects: `device.cpu`
- Capabilities: `ledger.append`
- Semantic operator: `test_declare`
- Policy decision: `allow`
- R12 record: `r12-66cc64c90273f381f888`
- MCRT record: `mcrt-a49fccb7f9d4b5dad48e`
- Determinism class: `R3-Deterministic`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA reviews semantic coherence and whether the declared oracle or proposition actually expresses the intended claim. CHARLOTTE reviews the legibility of fixtures, scenarios, failure schedules, proof dependencies, diagnostics, and evidence navigation. LANDON reviews parser, compiler, scheduler, simulator, proof checker, coverage engine, benchmark harness, sandbox, and replay feasibility. Professor requires a stated invariant, minimal counterexample, and defensible test oracle. Podium requires checksums, provenance, limitations, release integrity, and a certification decision tied to exact artifacts.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Confirm the fixture or generator domain and oracle are explicit.
- Record seeds, virtual clock rules, injected failures, and resource limits.
- Preserve proof obligations, theorem dependencies, and counterexamples.
- Name the measured coverage layer and benchmark environment.
- Verify network and unknown-code execution are explicitly governed.
- Verify optimization preserves results, diagnostics, traces, and receipts.

## Laboratory

**Task:** Build partition and node-failure scenarios with recovery oracles.

1. Copy the representative program into a separate laboratory module.
2. Write the invariant and evidence boundary before changing the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, diagnostic, R12 change, runtime result, and MCRT outcome.
5. Run structural validation; label remaining results modeled unless a native toolchain is used.
6. Submit source, seeds or proof inputs, expected results, evidence map, replay data, limitations, and certification decision.

## Review questions

1. What exact claim does this program verify?
2. Which identity or hash must change when the oracle, seed, failure schedule, or proof changes?
3. At what stage should the primary unsafe or invalid case be rejected?
4. Which optimization is safe, and which would erase verification meaning?
5. What native test would promote the modeled outcome into execution evidence?

# Chapter 9: Property Tests and Deterministic Generators

## Learning objectives

- Explain quantified invariants over generated spaces across source, semantics, AST, R12, runtime, and MCRT layers.
- State and test the invariant that generator domain, seed, precondition, property, and failure witness remain linked.
- Construct a positive case and a minimal counterexample involving vacuous properties or generators that never reach boundary states.
- Separate modeled corpus evidence from native compiler, simulator, proof-checker, and runtime evidence.

## Technical foundation

This chapter treats **quantified invariants over generated spaces** as a compiled language concern. In JA Test, Simulation, and Proof, a verification declaration is more than executable source: it is a stable claim connected to input construction, an oracle or proposition, typed semantics, a verification AST, an R12 execution or proof plan, a modeled runtime outcome, and an MCRT receipt. That chain makes a result reviewable before execution and reproducible after publication.

The central invariant is that **generator domain, seed, precondition, property, and failure witness remain linked**. The compiler must preserve this invariant during parsing, name resolution, type and effect analysis, proof-obligation generation, canonicalization, lowering, and optimization. The runtime must preserve it while scheduling tests, advancing virtual time, injecting failures, checking proofs, collecting coverage, measuring resources, shrinking counterexamples, and emitting receipts.

The principal counterexample is **vacuous properties or generators that never reach boundary states**. Negative, boundary, security, determinism, recovery, and certification records are therefore essential. They define where the language must stop, which diagnostic should be stable, what evidence must remain unresolved, and which counterexample must survive minimization. Verification quality is measured as much by reliable rejection and honest uncertainty as by successful passes.

Implementation proceeds in explicit passes: parse stable source nodes; resolve fixtures, generators, tests, simulations, theorems, and dependencies; infer types, effects, capabilities, clocks, seeds, and resources; generate proof and replay obligations; lower accepted programs to R12; execute only inside the declared sandbox and virtual environment; preserve failures and counterexamples; and emit an MCRT verification receipt. Optimization is permitted only when this complete behavior remains equivalent.

## Representative corpus program

**Record:** `JATP-00010`  
**Feature:** `property_test`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `c1a708224cb3ab8cfed25a28e25818c13a8e236b67309dc3cfddf9a8c240b779`

```jap
ja source 0.3
module corpus.ja_proof.example_00010
use Proof
policy no_network

fixture FixtureJATP_00010 {
    input 12
    expected 132
}
unit test FixtureCheckJATP_00010 {
    let fixture_result = FixtureJATP_00010.input * 11
    assert fixture_result == FixtureJATP_00010.expected
}
property PropertyJATP_00010 for_all x: Count where x <= 12 {
    let result = x * 11
    invariant result >= x
}
simulation FailureJATP_00010 {
    virtual_time 12s
    inject network.partition at 11s
    expect service.recovers within 14s
}
benchmark BenchJATP_00010 limit cpu 12ms memory 19MB
assert proof.complete == true
emit mcrt "PropertyJATP_00010.proof.mcrt"
```

## Evidence trace

- Semantic identity: `sem-e79f53a3e95ea508d5b2`
- Judgment: `Environment; Policy; {benchmark.run:bounded} ⊢ node-8d4665baba8d15af7629 : VerificationBundle ! {state.write} ⇒ validated`
- AST node: `node-8d4665baba8d15af7629` (`VerificationDecl`)
- Declared / inferred type: `VerificationBundle` / `VerificationBundle`
- Effects: `state.write`
- Capabilities: `benchmark.run:bounded`
- Semantic operator: `check_invariant`
- Policy decision: `allow`
- R12 record: `r12-47a259d996eed19ccf50`
- MCRT record: `mcrt-d12b8f66e3d6a0a6f05d`
- Determinism class: `R3-Deterministic`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA reviews semantic coherence and whether the declared oracle or proposition actually expresses the intended claim. CHARLOTTE reviews the legibility of fixtures, scenarios, failure schedules, proof dependencies, diagnostics, and evidence navigation. LANDON reviews parser, compiler, scheduler, simulator, proof checker, coverage engine, benchmark harness, sandbox, and replay feasibility. Professor requires a stated invariant, minimal counterexample, and defensible test oracle. Podium requires checksums, provenance, limitations, release integrity, and a certification decision tied to exact artifacts.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Confirm the fixture or generator domain and oracle are explicit.
- Record seeds, virtual clock rules, injected failures, and resource limits.
- Preserve proof obligations, theorem dependencies, and counterexamples.
- Name the measured coverage layer and benchmark environment.
- Verify network and unknown-code execution are explicitly governed.
- Verify optimization preserves results, diagnostics, traces, and receipts.

## Laboratory

**Task:** Design a property test with domain-coverage evidence.

1. Copy the representative program into a separate laboratory module.
2. Write the invariant and evidence boundary before changing the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, diagnostic, R12 change, runtime result, and MCRT outcome.
5. Run structural validation; label remaining results modeled unless a native toolchain is used.
6. Submit source, seeds or proof inputs, expected results, evidence map, replay data, limitations, and certification decision.

## Review questions

1. What exact claim does this program verify?
2. Which identity or hash must change when the oracle, seed, failure schedule, or proof changes?
3. At what stage should the primary unsafe or invalid case be rejected?
4. Which optimization is safe, and which would erase verification meaning?
5. What native test would promote the modeled outcome into execution evidence?

# Chapter 10: Fuzzing, Shrinking, and Counterexamples

## Learning objectives

- Explain broad input exploration and minimal reproducible failures across source, semantics, AST, R12, runtime, and MCRT layers.
- State and test the invariant that a minimized counterexample preserves the original failure predicate and provenance.
- Construct a positive case and a minimal counterexample involving shrinking that changes the failure or loses the original seed.
- Separate modeled corpus evidence from native compiler, simulator, proof-checker, and runtime evidence.

## Technical foundation

This chapter treats **broad input exploration and minimal reproducible failures** as a compiled language concern. In JA Test, Simulation, and Proof, a verification declaration is more than executable source: it is a stable claim connected to input construction, an oracle or proposition, typed semantics, a verification AST, an R12 execution or proof plan, a modeled runtime outcome, and an MCRT receipt. That chain makes a result reviewable before execution and reproducible after publication.

The central invariant is that **a minimized counterexample preserves the original failure predicate and provenance**. The compiler must preserve this invariant during parsing, name resolution, type and effect analysis, proof-obligation generation, canonicalization, lowering, and optimization. The runtime must preserve it while scheduling tests, advancing virtual time, injecting failures, checking proofs, collecting coverage, measuring resources, shrinking counterexamples, and emitting receipts.

The principal counterexample is **shrinking that changes the failure or loses the original seed**. Negative, boundary, security, determinism, recovery, and certification records are therefore essential. They define where the language must stop, which diagnostic should be stable, what evidence must remain unresolved, and which counterexample must survive minimization. Verification quality is measured as much by reliable rejection and honest uncertainty as by successful passes.

Implementation proceeds in explicit passes: parse stable source nodes; resolve fixtures, generators, tests, simulations, theorems, and dependencies; infer types, effects, capabilities, clocks, seeds, and resources; generate proof and replay obligations; lower accepted programs to R12; execute only inside the declared sandbox and virtual environment; preserve failures and counterexamples; and emit an MCRT verification receipt. Optimization is permitted only when this complete behavior remains equivalent.

## Representative corpus program

**Record:** `JATP-00271`  
**Feature:** `fuzz_target`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `e65124fab48ae0e261977add2bf16bad9e33a1279f56df56516c7122785ca0a5`

```jap
ja source 0.3
module corpus.ja_proof.example_00271
use Proof
policy no_network

fixture FixtureJATP_00271 {
    input 79
    expected 1896
}
unit test FixtureCheckJATP_00271 {
    let fixture_result = FixtureJATP_00271.input * 24
    assert fixture_result == FixtureJATP_00271.expected
}
property PropertyJATP_00271 for_all x: Count where x <= 79 {
    let result = x * 24
    invariant result >= x
}
simulation FailureJATP_00271 {
    virtual_time 79s
    inject network.partition at 24s
    expect service.recovers within 27s
}
benchmark BenchJATP_00271 limit cpu 79ms memory 32MB
assert proof.complete == true
emit mcrt "PropertyJATP_00271.proof.mcrt"
```

## Evidence trace

- Semantic identity: `sem-a9bc944a0d2b45c77d93`
- Judgment: `Environment; Policy; {test.execute} ⊢ node-b214e4bceb19e8ab8ddc : VerificationBundle ! {ledger.append} ⇒ validated`
- AST node: `node-b214e4bceb19e8ab8ddc` (`VerificationDecl`)
- Declared / inferred type: `VerificationBundle` / `VerificationBundle`
- Effects: `ledger.append`
- Capabilities: `test.execute`
- Semantic operator: `shrink`
- Policy decision: `allow`
- R12 record: `r12-7c56d79ee222b6c978f1`
- MCRT record: `mcrt-b51479465dd72d01ba09`
- Determinism class: `R3-Deterministic`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA reviews semantic coherence and whether the declared oracle or proposition actually expresses the intended claim. CHARLOTTE reviews the legibility of fixtures, scenarios, failure schedules, proof dependencies, diagnostics, and evidence navigation. LANDON reviews parser, compiler, scheduler, simulator, proof checker, coverage engine, benchmark harness, sandbox, and replay feasibility. Professor requires a stated invariant, minimal counterexample, and defensible test oracle. Podium requires checksums, provenance, limitations, release integrity, and a certification decision tied to exact artifacts.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Confirm the fixture or generator domain and oracle are explicit.
- Record seeds, virtual clock rules, injected failures, and resource limits.
- Preserve proof obligations, theorem dependencies, and counterexamples.
- Name the measured coverage layer and benchmark environment.
- Verify network and unknown-code execution are explicitly governed.
- Verify optimization preserves results, diagnostics, traces, and receipts.

## Laboratory

**Task:** Fuzz a bounded parser target and preserve the minimal witness.

1. Copy the representative program into a separate laboratory module.
2. Write the invariant and evidence boundary before changing the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, diagnostic, R12 change, runtime result, and MCRT outcome.
5. Run structural validation; label remaining results modeled unless a native toolchain is used.
6. Submit source, seeds or proof inputs, expected results, evidence map, replay data, limitations, and certification decision.

## Review questions

1. What exact claim does this program verify?
2. Which identity or hash must change when the oracle, seed, failure schedule, or proof changes?
3. At what stage should the primary unsafe or invalid case be rejected?
4. Which optimization is safe, and which would erase verification meaning?
5. What native test would promote the modeled outcome into execution evidence?

# Chapter 11: Invariants and Model Assertions

## Learning objectives

- Explain state-space claims and executable model constraints across source, semantics, AST, R12, runtime, and MCRT layers.
- State and test the invariant that invariants are evaluated at declared transitions and model boundaries.
- Construct a positive case and a minimal counterexample involving checking only the final state or mixing assumptions with conclusions.
- Separate modeled corpus evidence from native compiler, simulator, proof-checker, and runtime evidence.

## Technical foundation

This chapter treats **state-space claims and executable model constraints** as a compiled language concern. In JA Test, Simulation, and Proof, a verification declaration is more than executable source: it is a stable claim connected to input construction, an oracle or proposition, typed semantics, a verification AST, an R12 execution or proof plan, a modeled runtime outcome, and an MCRT receipt. That chain makes a result reviewable before execution and reproducible after publication.

The central invariant is that **invariants are evaluated at declared transitions and model boundaries**. The compiler must preserve this invariant during parsing, name resolution, type and effect analysis, proof-obligation generation, canonicalization, lowering, and optimization. The runtime must preserve it while scheduling tests, advancing virtual time, injecting failures, checking proofs, collecting coverage, measuring resources, shrinking counterexamples, and emitting receipts.

The principal counterexample is **checking only the final state or mixing assumptions with conclusions**. Negative, boundary, security, determinism, recovery, and certification records are therefore essential. They define where the language must stop, which diagnostic should be stable, what evidence must remain unresolved, and which counterexample must survive minimization. Verification quality is measured as much by reliable rejection and honest uncertainty as by successful passes.

Implementation proceeds in explicit passes: parse stable source nodes; resolve fixtures, generators, tests, simulations, theorems, and dependencies; infer types, effects, capabilities, clocks, seeds, and resources; generate proof and replay obligations; lower accepted programs to R12; execute only inside the declared sandbox and virtual environment; preserve failures and counterexamples; and emit an MCRT verification receipt. Optimization is permitted only when this complete behavior remains equivalent.

## Representative corpus program

**Record:** `JATP-00181`  
**Feature:** `invariant`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `d242a61ace81861672b48ca8c0e67e082516f1643750415d68119fd2a0d6ece0`

```jap
ja source 0.3
module corpus.ja_proof.example_00181
use Proof
policy no_network

fixture FixtureJATP_00181 {
    input 86
    expected 2322
}
unit test FixtureCheckJATP_00181 {
    let fixture_result = FixtureJATP_00181.input * 27
    assert fixture_result == FixtureJATP_00181.expected
}
property PropertyJATP_00181 for_all x: Count where x <= 86 {
    let result = x * 27
    invariant result >= x
}
simulation FailureJATP_00181 {
    virtual_time 86s
    inject network.partition at 27s
    expect service.recovers within 30s
}
benchmark BenchJATP_00181 limit cpu 86ms memory 35MB
assert proof.complete == true
emit mcrt "PropertyJATP_00181.proof.mcrt"
```

## Evidence trace

- Semantic identity: `sem-dbea3d1584192dec2fa0`
- Judgment: `Environment; Policy; {test.execute} ⊢ node-671bfc9651b5f87b6c37 : VerificationBundle ! {ledger.append} ⇒ validated`
- AST node: `node-671bfc9651b5f87b6c37` (`VerificationDecl`)
- Declared / inferred type: `VerificationBundle` / `VerificationBundle`
- Effects: `ledger.append`
- Capabilities: `test.execute`
- Semantic operator: `shrink`
- Policy decision: `allow`
- R12 record: `r12-4081d15de531dc35be99`
- MCRT record: `mcrt-3c6863a4586c64726c35`
- Determinism class: `R3-Deterministic`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA reviews semantic coherence and whether the declared oracle or proposition actually expresses the intended claim. CHARLOTTE reviews the legibility of fixtures, scenarios, failure schedules, proof dependencies, diagnostics, and evidence navigation. LANDON reviews parser, compiler, scheduler, simulator, proof checker, coverage engine, benchmark harness, sandbox, and replay feasibility. Professor requires a stated invariant, minimal counterexample, and defensible test oracle. Podium requires checksums, provenance, limitations, release integrity, and a certification decision tied to exact artifacts.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Confirm the fixture or generator domain and oracle are explicit.
- Record seeds, virtual clock rules, injected failures, and resource limits.
- Preserve proof obligations, theorem dependencies, and counterexamples.
- Name the measured coverage layer and benchmark environment.
- Verify network and unknown-code execution are explicitly governed.
- Verify optimization preserves results, diagnostics, traces, and receipts.

## Laboratory

**Task:** State and test a transition invariant.

1. Copy the representative program into a separate laboratory module.
2. Write the invariant and evidence boundary before changing the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, diagnostic, R12 change, runtime result, and MCRT outcome.
5. Run structural validation; label remaining results modeled unless a native toolchain is used.
6. Submit source, seeds or proof inputs, expected results, evidence map, replay data, limitations, and certification decision.

## Review questions

1. What exact claim does this program verify?
2. Which identity or hash must change when the oracle, seed, failure schedule, or proof changes?
3. At what stage should the primary unsafe or invalid case be rejected?
4. Which optimization is safe, and which would erase verification meaning?
5. What native test would promote the modeled outcome into execution evidence?

# Chapter 12: Theorems, Lemmas, and Proof Obligations

## Learning objectives

- Explain formal propositions and reusable proof structure across source, semantics, AST, R12, runtime, and MCRT layers.
- State and test the invariant that theorem identity, assumptions, obligations, dependencies, and conclusion are explicit.
- Construct a positive case and a minimal counterexample involving accepting a theorem because tests passed or because a dependency is unnamed.
- Separate modeled corpus evidence from native compiler, simulator, proof-checker, and runtime evidence.

## Technical foundation

This chapter treats **formal propositions and reusable proof structure** as a compiled language concern. In JA Test, Simulation, and Proof, a verification declaration is more than executable source: it is a stable claim connected to input construction, an oracle or proposition, typed semantics, a verification AST, an R12 execution or proof plan, a modeled runtime outcome, and an MCRT receipt. That chain makes a result reviewable before execution and reproducible after publication.

The central invariant is that **theorem identity, assumptions, obligations, dependencies, and conclusion are explicit**. The compiler must preserve this invariant during parsing, name resolution, type and effect analysis, proof-obligation generation, canonicalization, lowering, and optimization. The runtime must preserve it while scheduling tests, advancing virtual time, injecting failures, checking proofs, collecting coverage, measuring resources, shrinking counterexamples, and emitting receipts.

The principal counterexample is **accepting a theorem because tests passed or because a dependency is unnamed**. Negative, boundary, security, determinism, recovery, and certification records are therefore essential. They define where the language must stop, which diagnostic should be stable, what evidence must remain unresolved, and which counterexample must survive minimization. Verification quality is measured as much by reliable rejection and honest uncertainty as by successful passes.

Implementation proceeds in explicit passes: parse stable source nodes; resolve fixtures, generators, tests, simulations, theorems, and dependencies; infer types, effects, capabilities, clocks, seeds, and resources; generate proof and replay obligations; lower accepted programs to R12; execute only inside the declared sandbox and virtual environment; preserve failures and counterexamples; and emit an MCRT verification receipt. Optimization is permitted only when this complete behavior remains equivalent.

## Representative corpus program

**Record:** `JATP-00291`  
**Feature:** `theorem`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `e6b0b1392c6b4f2ea2633386d696568e469332c7a7c1f8f1d0fed11b22198c36`

```jap
ja source 0.3
module corpus.ja_proof.example_00291
use Proof
policy no_network

fixture FixtureJATP_00291 {
    input 2
    expected 26
}
unit test FixtureCheckJATP_00291 {
    let fixture_result = FixtureJATP_00291.input * 13
    assert fixture_result == FixtureJATP_00291.expected
}
property PropertyJATP_00291 for_all x: Count where x <= 2 {
    let result = x * 13
    invariant result >= x
}
simulation FailureJATP_00291 {
    virtual_time 2s
    inject network.partition at 13s
    expect service.recovers within 16s
}
benchmark BenchJATP_00291 limit cpu 2ms memory 21MB
assert proof.complete == true
emit mcrt "PropertyJATP_00291.proof.mcrt"
```

## Evidence trace

- Semantic identity: `sem-cca055c5383280cfe865`
- Judgment: `Environment; Policy; {fuzz.run:isolated} ⊢ node-d1f80b43768d28089884 : VerificationBundle ! {process.spawn} ⇒ validated`
- AST node: `node-d1f80b43768d28089884` (`VerificationDecl`)
- Declared / inferred type: `VerificationBundle` / `VerificationBundle`
- Effects: `process.spawn`
- Capabilities: `fuzz.run:isolated`
- Semantic operator: `shrink`
- Policy decision: `allow`
- R12 record: `r12-756c058eea50da5612af`
- MCRT record: `mcrt-5fa718a9a949b22696cb`
- Determinism class: `R3-Deterministic`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA reviews semantic coherence and whether the declared oracle or proposition actually expresses the intended claim. CHARLOTTE reviews the legibility of fixtures, scenarios, failure schedules, proof dependencies, diagnostics, and evidence navigation. LANDON reviews parser, compiler, scheduler, simulator, proof checker, coverage engine, benchmark harness, sandbox, and replay feasibility. Professor requires a stated invariant, minimal counterexample, and defensible test oracle. Podium requires checksums, provenance, limitations, release integrity, and a certification decision tied to exact artifacts.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Confirm the fixture or generator domain and oracle are explicit.
- Record seeds, virtual clock rules, injected failures, and resource limits.
- Preserve proof obligations, theorem dependencies, and counterexamples.
- Name the measured coverage layer and benchmark environment.
- Verify network and unknown-code execution are explicitly governed.
- Verify optimization preserves results, diagnostics, traces, and receipts.

## Laboratory

**Task:** Construct a theorem with a supporting lemma and obligations.

1. Copy the representative program into a separate laboratory module.
2. Write the invariant and evidence boundary before changing the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, diagnostic, R12 change, runtime result, and MCRT outcome.
5. Run structural validation; label remaining results modeled unless a native toolchain is used.
6. Submit source, seeds or proof inputs, expected results, evidence map, replay data, limitations, and certification decision.

## Review questions

1. What exact claim does this program verify?
2. Which identity or hash must change when the oracle, seed, failure schedule, or proof changes?
3. At what stage should the primary unsafe or invalid case be rejected?
4. Which optimization is safe, and which would erase verification meaning?
5. What native test would promote the modeled outcome into execution evidence?

# Chapter 13: Proof Terms and Checkable Evidence

## Learning objectives

- Explain proof objects, normalization, and independent checking across source, semantics, AST, R12, runtime, and MCRT layers.
- State and test the invariant that proof normalization preserves theorem identity, dependencies, and evidence hashes.
- Construct a positive case and a minimal counterexample involving opaque “proved” flags or proof-term optimization that changes meaning.
- Separate modeled corpus evidence from native compiler, simulator, proof-checker, and runtime evidence.

## Technical foundation

This chapter treats **proof objects, normalization, and independent checking** as a compiled language concern. In JA Test, Simulation, and Proof, a verification declaration is more than executable source: it is a stable claim connected to input construction, an oracle or proposition, typed semantics, a verification AST, an R12 execution or proof plan, a modeled runtime outcome, and an MCRT receipt. That chain makes a result reviewable before execution and reproducible after publication.

The central invariant is that **proof normalization preserves theorem identity, dependencies, and evidence hashes**. The compiler must preserve this invariant during parsing, name resolution, type and effect analysis, proof-obligation generation, canonicalization, lowering, and optimization. The runtime must preserve it while scheduling tests, advancing virtual time, injecting failures, checking proofs, collecting coverage, measuring resources, shrinking counterexamples, and emitting receipts.

The principal counterexample is **opaque “proved” flags or proof-term optimization that changes meaning**. Negative, boundary, security, determinism, recovery, and certification records are therefore essential. They define where the language must stop, which diagnostic should be stable, what evidence must remain unresolved, and which counterexample must survive minimization. Verification quality is measured as much by reliable rejection and honest uncertainty as by successful passes.

Implementation proceeds in explicit passes: parse stable source nodes; resolve fixtures, generators, tests, simulations, theorems, and dependencies; infer types, effects, capabilities, clocks, seeds, and resources; generate proof and replay obligations; lower accepted programs to R12; execute only inside the declared sandbox and virtual environment; preserve failures and counterexamples; and emit an MCRT verification receipt. Optimization is permitted only when this complete behavior remains equivalent.

## Representative corpus program

**Record:** `JATP-00241`  
**Feature:** `proof_term`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `c1345ae302f8c70cae824a616cb450a24e940b99b34ac09f6a5fb02538f154b0`

```jap
ja source 0.3
module corpus.ja_proof.example_00241
use Proof
policy no_network

fixture FixtureJATP_00241 {
    input 49
    expected 1225
}
unit test FixtureCheckJATP_00241 {
    let fixture_result = FixtureJATP_00241.input * 25
    assert fixture_result == FixtureJATP_00241.expected
}
property PropertyJATP_00241 for_all x: Count where x <= 49 {
    let result = x * 25
    invariant result >= x
}
simulation FailureJATP_00241 {
    virtual_time 49s
    inject network.partition at 25s
    expect service.recovers within 28s
}
benchmark BenchJATP_00241 limit cpu 49ms memory 33MB
assert proof.complete == true
emit mcrt "PropertyJATP_00241.proof.mcrt"
```

## Evidence trace

- Semantic identity: `sem-e2c8b2944a0c8b9af98d`
- Judgment: `Environment; Policy; {test.execute} ⊢ node-3d7efaede188cfa4d768 : VerificationBundle ! {ledger.append} ⇒ validated`
- AST node: `node-3d7efaede188cfa4d768` (`VerificationDecl`)
- Declared / inferred type: `VerificationBundle` / `VerificationBundle`
- Effects: `ledger.append`
- Capabilities: `test.execute`
- Semantic operator: `shrink`
- Policy decision: `allow`
- R12 record: `r12-0fca8d7ef6526a5f63b0`
- MCRT record: `mcrt-530d6ace72473909bdd9`
- Determinism class: `R3-Deterministic`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA reviews semantic coherence and whether the declared oracle or proposition actually expresses the intended claim. CHARLOTTE reviews the legibility of fixtures, scenarios, failure schedules, proof dependencies, diagnostics, and evidence navigation. LANDON reviews parser, compiler, scheduler, simulator, proof checker, coverage engine, benchmark harness, sandbox, and replay feasibility. Professor requires a stated invariant, minimal counterexample, and defensible test oracle. Podium requires checksums, provenance, limitations, release integrity, and a certification decision tied to exact artifacts.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Confirm the fixture or generator domain and oracle are explicit.
- Record seeds, virtual clock rules, injected failures, and resource limits.
- Preserve proof obligations, theorem dependencies, and counterexamples.
- Name the measured coverage layer and benchmark environment.
- Verify network and unknown-code execution are explicitly governed.
- Verify optimization preserves results, diagnostics, traces, and receipts.

## Laboratory

**Task:** Produce and validate a compact proof term.

1. Copy the representative program into a separate laboratory module.
2. Write the invariant and evidence boundary before changing the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, diagnostic, R12 change, runtime result, and MCRT outcome.
5. Run structural validation; label remaining results modeled unless a native toolchain is used.
6. Submit source, seeds or proof inputs, expected results, evidence map, replay data, limitations, and certification decision.

## Review questions

1. What exact claim does this program verify?
2. Which identity or hash must change when the oracle, seed, failure schedule, or proof changes?
3. At what stage should the primary unsafe or invalid case be rejected?
4. Which optimization is safe, and which would erase verification meaning?
5. What native test would promote the modeled outcome into execution evidence?

# Chapter 14: Temporal Properties and Model Checking

## Learning objectives

- Explain safety, liveness, bounded progress, and counterexample traces across source, semantics, AST, R12, runtime, and MCRT layers.
- State and test the invariant that time semantics, transition relation, bound, and fairness assumptions are declared.
- Construct a positive case and a minimal counterexample involving claiming liveness from finite examples without a model or bound.
- Separate modeled corpus evidence from native compiler, simulator, proof-checker, and runtime evidence.

## Technical foundation

This chapter treats **safety, liveness, bounded progress, and counterexample traces** as a compiled language concern. In JA Test, Simulation, and Proof, a verification declaration is more than executable source: it is a stable claim connected to input construction, an oracle or proposition, typed semantics, a verification AST, an R12 execution or proof plan, a modeled runtime outcome, and an MCRT receipt. That chain makes a result reviewable before execution and reproducible after publication.

The central invariant is that **time semantics, transition relation, bound, and fairness assumptions are declared**. The compiler must preserve this invariant during parsing, name resolution, type and effect analysis, proof-obligation generation, canonicalization, lowering, and optimization. The runtime must preserve it while scheduling tests, advancing virtual time, injecting failures, checking proofs, collecting coverage, measuring resources, shrinking counterexamples, and emitting receipts.

The principal counterexample is **claiming liveness from finite examples without a model or bound**. Negative, boundary, security, determinism, recovery, and certification records are therefore essential. They define where the language must stop, which diagnostic should be stable, what evidence must remain unresolved, and which counterexample must survive minimization. Verification quality is measured as much by reliable rejection and honest uncertainty as by successful passes.

Implementation proceeds in explicit passes: parse stable source nodes; resolve fixtures, generators, tests, simulations, theorems, and dependencies; infer types, effects, capabilities, clocks, seeds, and resources; generate proof and replay obligations; lower accepted programs to R12; execute only inside the declared sandbox and virtual environment; preserve failures and counterexamples; and emit an MCRT verification receipt. Optimization is permitted only when this complete behavior remains equivalent.

## Representative corpus program

**Record:** `JATP-00012`  
**Feature:** `temporal_property`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `03861c26a742571fb6c873a3ce3ff4993783db01c3e5dfd25cbca6c07a5f880a`

```jap
ja source 0.3
module corpus.ja_proof.example_00012
use Proof
policy no_network

fixture FixtureJATP_00012 {
    input 14
    expected 182
}
unit test FixtureCheckJATP_00012 {
    let fixture_result = FixtureJATP_00012.input * 13
    assert fixture_result == FixtureJATP_00012.expected
}
property PropertyJATP_00012 for_all x: Count where x <= 14 {
    let result = x * 13
    invariant result >= x
}
simulation FailureJATP_00012 {
    virtual_time 14s
    inject network.partition at 13s
    expect service.recovers within 16s
}
benchmark BenchJATP_00012 limit cpu 14ms memory 21MB
assert proof.complete == true
emit mcrt "PropertyJATP_00012.proof.mcrt"
```

## Evidence trace

- Semantic identity: `sem-5f999342987287c55b8f`
- Judgment: `Environment; Policy; {simulation.execute} ⊢ node-e531e1c792576387ec90 : VerificationBundle ! {pure} ⇒ validated`
- AST node: `node-e531e1c792576387ec90` (`VerificationDecl`)
- Declared / inferred type: `VerificationBundle` / `VerificationBundle`
- Effects: `pure`
- Capabilities: `simulation.execute`
- Semantic operator: `test_declare`
- Policy decision: `allow`
- R12 record: `r12-a8b26fddb8bd7067ca98`
- MCRT record: `mcrt-6e703ba4254188d829cf`
- Determinism class: `R3-Deterministic`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA reviews semantic coherence and whether the declared oracle or proposition actually expresses the intended claim. CHARLOTTE reviews the legibility of fixtures, scenarios, failure schedules, proof dependencies, diagnostics, and evidence navigation. LANDON reviews parser, compiler, scheduler, simulator, proof checker, coverage engine, benchmark harness, sandbox, and replay feasibility. Professor requires a stated invariant, minimal counterexample, and defensible test oracle. Podium requires checksums, provenance, limitations, release integrity, and a certification decision tied to exact artifacts.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Confirm the fixture or generator domain and oracle are explicit.
- Record seeds, virtual clock rules, injected failures, and resource limits.
- Preserve proof obligations, theorem dependencies, and counterexamples.
- Name the measured coverage layer and benchmark environment.
- Verify network and unknown-code execution are explicitly governed.
- Verify optimization preserves results, diagnostics, traces, and receipts.

## Laboratory

**Task:** Specify a temporal property and counterexample trace.

1. Copy the representative program into a separate laboratory module.
2. Write the invariant and evidence boundary before changing the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, diagnostic, R12 change, runtime result, and MCRT outcome.
5. Run structural validation; label remaining results modeled unless a native toolchain is used.
6. Submit source, seeds or proof inputs, expected results, evidence map, replay data, limitations, and certification decision.

## Review questions

1. What exact claim does this program verify?
2. Which identity or hash must change when the oracle, seed, failure schedule, or proof changes?
3. At what stage should the primary unsafe or invalid case be rejected?
4. Which optimization is safe, and which would erase verification meaning?
5. What native test would promote the modeled outcome into execution evidence?

# Chapter 15: Resource Limits and Benchmarks

## Learning objectives

- Explain repeatable measurement under explicit resource envelopes across source, semantics, AST, R12, runtime, and MCRT layers.
- State and test the invariant that workload, warmup, repetitions, limits, host profile, and statistics are recorded.
- Construct a positive case and a minimal counterexample involving unbounded benchmarks or performance claims without environment identity.
- Separate modeled corpus evidence from native compiler, simulator, proof-checker, and runtime evidence.

## Technical foundation

This chapter treats **repeatable measurement under explicit resource envelopes** as a compiled language concern. In JA Test, Simulation, and Proof, a verification declaration is more than executable source: it is a stable claim connected to input construction, an oracle or proposition, typed semantics, a verification AST, an R12 execution or proof plan, a modeled runtime outcome, and an MCRT receipt. That chain makes a result reviewable before execution and reproducible after publication.

The central invariant is that **workload, warmup, repetitions, limits, host profile, and statistics are recorded**. The compiler must preserve this invariant during parsing, name resolution, type and effect analysis, proof-obligation generation, canonicalization, lowering, and optimization. The runtime must preserve it while scheduling tests, advancing virtual time, injecting failures, checking proofs, collecting coverage, measuring resources, shrinking counterexamples, and emitting receipts.

The principal counterexample is **unbounded benchmarks or performance claims without environment identity**. Negative, boundary, security, determinism, recovery, and certification records are therefore essential. They define where the language must stop, which diagnostic should be stable, what evidence must remain unresolved, and which counterexample must survive minimization. Verification quality is measured as much by reliable rejection and honest uncertainty as by successful passes.

Implementation proceeds in explicit passes: parse stable source nodes; resolve fixtures, generators, tests, simulations, theorems, and dependencies; infer types, effects, capabilities, clocks, seeds, and resources; generate proof and replay obligations; lower accepted programs to R12; execute only inside the declared sandbox and virtual environment; preserve failures and counterexamples; and emit an MCRT verification receipt. Optimization is permitted only when this complete behavior remains equivalent.

## Representative corpus program

**Record:** `JATP-00191`  
**Feature:** `benchmark`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `56f5ac2ac4f7a2f032ac41f3cf1e643409059ba030dc4823eb84d2336532f290`

```jap
ja source 0.3
module corpus.ja_proof.example_00191
use Proof
policy no_network

fixture FixtureJATP_00191 {
    input 96
    expected 576
}
unit test FixtureCheckJATP_00191 {
    let fixture_result = FixtureJATP_00191.input * 6
    assert fixture_result == FixtureJATP_00191.expected
}
property PropertyJATP_00191 for_all x: Count where x <= 96 {
    let result = x * 6
    invariant result >= x
}
simulation FailureJATP_00191 {
    virtual_time 96s
    inject network.partition at 6s
    expect service.recovers within 9s
}
benchmark BenchJATP_00191 limit cpu 96ms memory 14MB
assert proof.complete == true
emit mcrt "PropertyJATP_00191.proof.mcrt"
```

## Evidence trace

- Semantic identity: `sem-1ab77329f7cb93bcfb90`
- Judgment: `Environment; Policy; {proof.check} ⊢ node-f975dc4f4532f3451769 : VerificationBundle ! {state.read} ⇒ validated`
- AST node: `node-f975dc4f4532f3451769` (`VerificationDecl`)
- Declared / inferred type: `VerificationBundle` / `VerificationBundle`
- Effects: `state.read`
- Capabilities: `proof.check`
- Semantic operator: `shrink`
- Policy decision: `allow`
- R12 record: `r12-2a32910255849ee19e9b`
- MCRT record: `mcrt-64e2d4a4a582dd1b8a52`
- Determinism class: `R3-Deterministic`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA reviews semantic coherence and whether the declared oracle or proposition actually expresses the intended claim. CHARLOTTE reviews the legibility of fixtures, scenarios, failure schedules, proof dependencies, diagnostics, and evidence navigation. LANDON reviews parser, compiler, scheduler, simulator, proof checker, coverage engine, benchmark harness, sandbox, and replay feasibility. Professor requires a stated invariant, minimal counterexample, and defensible test oracle. Podium requires checksums, provenance, limitations, release integrity, and a certification decision tied to exact artifacts.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Confirm the fixture or generator domain and oracle are explicit.
- Record seeds, virtual clock rules, injected failures, and resource limits.
- Preserve proof obligations, theorem dependencies, and counterexamples.
- Name the measured coverage layer and benchmark environment.
- Verify network and unknown-code execution are explicitly governed.
- Verify optimization preserves results, diagnostics, traces, and receipts.

## Laboratory

**Task:** Design a bounded benchmark and resource-failure test.

1. Copy the representative program into a separate laboratory module.
2. Write the invariant and evidence boundary before changing the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, diagnostic, R12 change, runtime result, and MCRT outcome.
5. Run structural validation; label remaining results modeled unless a native toolchain is used.
6. Submit source, seeds or proof inputs, expected results, evidence map, replay data, limitations, and certification decision.

## Review questions

1. What exact claim does this program verify?
2. Which identity or hash must change when the oracle, seed, failure schedule, or proof changes?
3. At what stage should the primary unsafe or invalid case be rejected?
4. Which optimization is safe, and which would erase verification meaning?
5. What native test would promote the modeled outcome into execution evidence?

# Chapter 16: Source, AST, Runtime, and R12 Coverage

## Learning objectives

- Explain layer-specific coverage and meaningful adequacy across source, semantics, AST, R12, runtime, and MCRT layers.
- State and test the invariant that coverage names the layer, target set, exclusions, and adequacy threshold.
- Construct a positive case and a minimal counterexample involving using line coverage as proof of semantic or runtime completeness.
- Separate modeled corpus evidence from native compiler, simulator, proof-checker, and runtime evidence.

## Technical foundation

This chapter treats **layer-specific coverage and meaningful adequacy** as a compiled language concern. In JA Test, Simulation, and Proof, a verification declaration is more than executable source: it is a stable claim connected to input construction, an oracle or proposition, typed semantics, a verification AST, an R12 execution or proof plan, a modeled runtime outcome, and an MCRT receipt. That chain makes a result reviewable before execution and reproducible after publication.

The central invariant is that **coverage names the layer, target set, exclusions, and adequacy threshold**. The compiler must preserve this invariant during parsing, name resolution, type and effect analysis, proof-obligation generation, canonicalization, lowering, and optimization. The runtime must preserve it while scheduling tests, advancing virtual time, injecting failures, checking proofs, collecting coverage, measuring resources, shrinking counterexamples, and emitting receipts.

The principal counterexample is **using line coverage as proof of semantic or runtime completeness**. Negative, boundary, security, determinism, recovery, and certification records are therefore essential. They define where the language must stop, which diagnostic should be stable, what evidence must remain unresolved, and which counterexample must survive minimization. Verification quality is measured as much by reliable rejection and honest uncertainty as by successful passes.

Implementation proceeds in explicit passes: parse stable source nodes; resolve fixtures, generators, tests, simulations, theorems, and dependencies; infer types, effects, capabilities, clocks, seeds, and resources; generate proof and replay obligations; lower accepted programs to R12; execute only inside the declared sandbox and virtual environment; preserve failures and counterexamples; and emit an MCRT verification receipt. Optimization is permitted only when this complete behavior remains equivalent.

## Representative corpus program

**Record:** `JATP-00251`  
**Feature:** `r12_coverage`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `d3ca1a48c6f6c8299ae645daf6ccb7e3c12716ffbf5c2a541f37f8d45fd554f0`

```jap
ja source 0.3
module corpus.ja_proof.example_00251
use Proof
policy no_network

fixture FixtureJATP_00251 {
    input 59
    expected 236
}
unit test FixtureCheckJATP_00251 {
    let fixture_result = FixtureJATP_00251.input * 4
    assert fixture_result == FixtureJATP_00251.expected
}
property PropertyJATP_00251 for_all x: Count where x <= 59 {
    let result = x * 4
    invariant result >= x
}
simulation FailureJATP_00251 {
    virtual_time 59s
    inject network.partition at 4s
    expect service.recovers within 7s
}
benchmark BenchJATP_00251 limit cpu 59ms memory 12MB
assert proof.complete == true
emit mcrt "PropertyJATP_00251.proof.mcrt"
```

## Evidence trace

- Semantic identity: `sem-b5adea0cde1b471ce921`
- Judgment: `Environment; Policy; {proof.check} ⊢ node-96fa33364167bcd1396b : VerificationBundle ! {state.read} ⇒ validated`
- AST node: `node-96fa33364167bcd1396b` (`VerificationDecl`)
- Declared / inferred type: `VerificationBundle` / `VerificationBundle`
- Effects: `state.read`
- Capabilities: `proof.check`
- Semantic operator: `shrink`
- Policy decision: `allow`
- R12 record: `r12-442408679ec74333b96c`
- MCRT record: `mcrt-a854389ee653a88817e8`
- Determinism class: `R3-Deterministic`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA reviews semantic coherence and whether the declared oracle or proposition actually expresses the intended claim. CHARLOTTE reviews the legibility of fixtures, scenarios, failure schedules, proof dependencies, diagnostics, and evidence navigation. LANDON reviews parser, compiler, scheduler, simulator, proof checker, coverage engine, benchmark harness, sandbox, and replay feasibility. Professor requires a stated invariant, minimal counterexample, and defensible test oracle. Podium requires checksums, provenance, limitations, release integrity, and a certification decision tied to exact artifacts.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Confirm the fixture or generator domain and oracle are explicit.
- Record seeds, virtual clock rules, injected failures, and resource limits.
- Preserve proof obligations, theorem dependencies, and counterexamples.
- Name the measured coverage layer and benchmark environment.
- Verify network and unknown-code execution are explicitly governed.
- Verify optimization preserves results, diagnostics, traces, and receipts.

## Laboratory

**Task:** Create a four-layer coverage report.

1. Copy the representative program into a separate laboratory module.
2. Write the invariant and evidence boundary before changing the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, diagnostic, R12 change, runtime result, and MCRT outcome.
5. Run structural validation; label remaining results modeled unless a native toolchain is used.
6. Submit source, seeds or proof inputs, expected results, evidence map, replay data, limitations, and certification decision.

## Review questions

1. What exact claim does this program verify?
2. Which identity or hash must change when the oracle, seed, failure schedule, or proof changes?
3. At what stage should the primary unsafe or invalid case be rejected?
4. Which optimization is safe, and which would erase verification meaning?
5. What native test would promote the modeled outcome into execution evidence?

# Chapter 17: Typed Verification AST and Semantic Judgments

## Learning objectives

- Explain compiler representation of tests, simulations, proofs, and evidence across source, semantics, AST, R12, runtime, and MCRT layers.
- State and test the invariant that types, effects, capabilities, seeds, clocks, obligations, and resource profiles survive lowering.
- Construct a positive case and a minimal counterexample involving generic nodes that erase verification semantics.
- Separate modeled corpus evidence from native compiler, simulator, proof-checker, and runtime evidence.

## Technical foundation

This chapter treats **compiler representation of tests, simulations, proofs, and evidence** as a compiled language concern. In JA Test, Simulation, and Proof, a verification declaration is more than executable source: it is a stable claim connected to input construction, an oracle or proposition, typed semantics, a verification AST, an R12 execution or proof plan, a modeled runtime outcome, and an MCRT receipt. That chain makes a result reviewable before execution and reproducible after publication.

The central invariant is that **types, effects, capabilities, seeds, clocks, obligations, and resource profiles survive lowering**. The compiler must preserve this invariant during parsing, name resolution, type and effect analysis, proof-obligation generation, canonicalization, lowering, and optimization. The runtime must preserve it while scheduling tests, advancing virtual time, injecting failures, checking proofs, collecting coverage, measuring resources, shrinking counterexamples, and emitting receipts.

The principal counterexample is **generic nodes that erase verification semantics**. Negative, boundary, security, determinism, recovery, and certification records are therefore essential. They define where the language must stop, which diagnostic should be stable, what evidence must remain unresolved, and which counterexample must survive minimization. Verification quality is measured as much by reliable rejection and honest uncertainty as by successful passes.

Implementation proceeds in explicit passes: parse stable source nodes; resolve fixtures, generators, tests, simulations, theorems, and dependencies; infer types, effects, capabilities, clocks, seeds, and resources; generate proof and replay obligations; lower accepted programs to R12; execute only inside the declared sandbox and virtual environment; preserve failures and counterexamples; and emit an MCRT verification receipt. Optimization is permitted only when this complete behavior remains equivalent.

## Representative corpus program

**Record:** `JATP-00004`  
**Feature:** `ast_coverage`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `af254cb658041996792bace21b2a669a81eba78b74b904364ed356919faf3161`

```jap
ja source 0.3
module corpus.ja_proof.example_00004
use Proof
policy no_network

fixture FixtureJATP_00004 {
    input 6
    expected 30
}
unit test FixtureCheckJATP_00004 {
    let fixture_result = FixtureJATP_00004.input * 5
    assert fixture_result == FixtureJATP_00004.expected
}
property PropertyJATP_00004 for_all x: Count where x <= 6 {
    let result = x * 5
    invariant result >= x
}
simulation FailureJATP_00004 {
    virtual_time 6s
    inject network.partition at 5s
    expect service.recovers within 8s
}
benchmark BenchJATP_00004 limit cpu 6ms memory 13MB
assert proof.complete == true
emit mcrt "PropertyJATP_00004.proof.mcrt"
```

## Evidence trace

- Semantic identity: `sem-f2957267290f054cf162`
- Judgment: `Environment; Policy; {benchmark.run:bounded} ⊢ node-0f883d4abac86431bb82 : VerificationBundle ! {state.write} ⇒ validated`
- AST node: `node-0f883d4abac86431bb82` (`VerificationDecl`)
- Declared / inferred type: `VerificationBundle` / `VerificationBundle`
- Effects: `state.write`
- Capabilities: `benchmark.run:bounded`
- Semantic operator: `fuzz`
- Policy decision: `allow`
- R12 record: `r12-496231b3ece66d4c05ec`
- MCRT record: `mcrt-0b267dd1f19db33e6ad0`
- Determinism class: `R3-Deterministic`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA reviews semantic coherence and whether the declared oracle or proposition actually expresses the intended claim. CHARLOTTE reviews the legibility of fixtures, scenarios, failure schedules, proof dependencies, diagnostics, and evidence navigation. LANDON reviews parser, compiler, scheduler, simulator, proof checker, coverage engine, benchmark harness, sandbox, and replay feasibility. Professor requires a stated invariant, minimal counterexample, and defensible test oracle. Podium requires checksums, provenance, limitations, release integrity, and a certification decision tied to exact artifacts.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Confirm the fixture or generator domain and oracle are explicit.
- Record seeds, virtual clock rules, injected failures, and resource limits.
- Preserve proof obligations, theorem dependencies, and counterexamples.
- Name the measured coverage layer and benchmark environment.
- Verify network and unknown-code execution are explicitly governed.
- Verify optimization preserves results, diagnostics, traces, and receipts.

## Laboratory

**Task:** Map a source program into typed verification nodes.

1. Copy the representative program into a separate laboratory module.
2. Write the invariant and evidence boundary before changing the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, diagnostic, R12 change, runtime result, and MCRT outcome.
5. Run structural validation; label remaining results modeled unless a native toolchain is used.
6. Submit source, seeds or proof inputs, expected results, evidence map, replay data, limitations, and certification decision.

## Review questions

1. What exact claim does this program verify?
2. Which identity or hash must change when the oracle, seed, failure schedule, or proof changes?
3. At what stage should the primary unsafe or invalid case be rejected?
4. Which optimization is safe, and which would erase verification meaning?
5. What native test would promote the modeled outcome into execution evidence?

# Chapter 18: Compiler Diagnostics and Negative Cases

## Learning objectives

- Explain stable rejection, repair guidance, and counterexample preservation across source, semantics, AST, R12, runtime, and MCRT layers.
- State and test the invariant that unsafe or ill-formed verification programs fail at the earliest responsible stage.
- Construct a positive case and a minimal counterexample involving late runtime failure, unstable diagnostics, or silently weakened assertions.
- Separate modeled corpus evidence from native compiler, simulator, proof-checker, and runtime evidence.

## Technical foundation

This chapter treats **stable rejection, repair guidance, and counterexample preservation** as a compiled language concern. In JA Test, Simulation, and Proof, a verification declaration is more than executable source: it is a stable claim connected to input construction, an oracle or proposition, typed semantics, a verification AST, an R12 execution or proof plan, a modeled runtime outcome, and an MCRT receipt. That chain makes a result reviewable before execution and reproducible after publication.

The central invariant is that **unsafe or ill-formed verification programs fail at the earliest responsible stage**. The compiler must preserve this invariant during parsing, name resolution, type and effect analysis, proof-obligation generation, canonicalization, lowering, and optimization. The runtime must preserve it while scheduling tests, advancing virtual time, injecting failures, checking proofs, collecting coverage, measuring resources, shrinking counterexamples, and emitting receipts.

The principal counterexample is **late runtime failure, unstable diagnostics, or silently weakened assertions**. Negative, boundary, security, determinism, recovery, and certification records are therefore essential. They define where the language must stop, which diagnostic should be stable, what evidence must remain unresolved, and which counterexample must survive minimization. Verification quality is measured as much by reliable rejection and honest uncertainty as by successful passes.

Implementation proceeds in explicit passes: parse stable source nodes; resolve fixtures, generators, tests, simulations, theorems, and dependencies; infer types, effects, capabilities, clocks, seeds, and resources; generate proof and replay obligations; lower accepted programs to R12; execute only inside the declared sandbox and virtual environment; preserve failures and counterexamples; and emit an MCRT verification receipt. Optimization is permitted only when this complete behavior remains equivalent.

## Representative corpus program

**Record:** `JATP-00014`  
**Feature:** `assertion`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `5e92693577ac76bfbc0c27c2246a7a8439592ae22f62f1e245bb4c40ef5f1e42`

```jap
ja source 0.3
module corpus.ja_proof.example_00014
use Proof
policy no_network

fixture FixtureJATP_00014 {
    input 16
    expected 240
}
unit test FixtureCheckJATP_00014 {
    let fixture_result = FixtureJATP_00014.input * 15
    assert fixture_result == FixtureJATP_00014.expected
}
property PropertyJATP_00014 for_all x: Count where x <= 16 {
    let result = x * 15
    invariant result >= x
}
simulation FailureJATP_00014 {
    virtual_time 16s
    inject network.partition at 15s
    expect service.recovers within 18s
}
benchmark BenchJATP_00014 limit cpu 16ms memory 23MB
assert proof.complete == true
emit mcrt "PropertyJATP_00014.proof.mcrt"
```

## Evidence trace

- Semantic identity: `sem-0b9ede60ce55df76766c`
- Judgment: `Environment; Policy; {ledger.append} ⊢ node-00db298184a155a35667 : VerificationBundle ! {device.cpu} ⇒ validated`
- AST node: `node-00db298184a155a35667` (`VerificationDecl`)
- Declared / inferred type: `VerificationBundle` / `VerificationBundle`
- Effects: `device.cpu`
- Capabilities: `ledger.append`
- Semantic operator: `fuzz`
- Policy decision: `allow`
- R12 record: `r12-e9d49c9373a8b248b981`
- MCRT record: `mcrt-b731d19fa04ec67491e8`
- Determinism class: `R3-Deterministic`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA reviews semantic coherence and whether the declared oracle or proposition actually expresses the intended claim. CHARLOTTE reviews the legibility of fixtures, scenarios, failure schedules, proof dependencies, diagnostics, and evidence navigation. LANDON reviews parser, compiler, scheduler, simulator, proof checker, coverage engine, benchmark harness, sandbox, and replay feasibility. Professor requires a stated invariant, minimal counterexample, and defensible test oracle. Podium requires checksums, provenance, limitations, release integrity, and a certification decision tied to exact artifacts.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Confirm the fixture or generator domain and oracle are explicit.
- Record seeds, virtual clock rules, injected failures, and resource limits.
- Preserve proof obligations, theorem dependencies, and counterexamples.
- Name the measured coverage layer and benchmark environment.
- Verify network and unknown-code execution are explicitly governed.
- Verify optimization preserves results, diagnostics, traces, and receipts.

## Laboratory

**Task:** Classify and minimize five negative cases.

1. Copy the representative program into a separate laboratory module.
2. Write the invariant and evidence boundary before changing the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, diagnostic, R12 change, runtime result, and MCRT outcome.
5. Run structural validation; label remaining results modeled unless a native toolchain is used.
6. Submit source, seeds or proof inputs, expected results, evidence map, replay data, limitations, and certification decision.

## Review questions

1. What exact claim does this program verify?
2. Which identity or hash must change when the oracle, seed, failure schedule, or proof changes?
3. At what stage should the primary unsafe or invalid case be rejected?
4. Which optimization is safe, and which would erase verification meaning?
5. What native test would promote the modeled outcome into execution evidence?

# Chapter 19: Deterministic Verification Runtime and Replay

## Learning objectives

- Explain scheduling, sandboxes, proof checking, and reproducible receipts across source, semantics, AST, R12, runtime, and MCRT layers.
- State and test the invariant that identical source, seed, clock, faults, resources, and runtime profile reproduce the same result.
- Construct a positive case and a minimal counterexample involving hidden wall time, nondeterministic ordering, or stale caches.
- Separate modeled corpus evidence from native compiler, simulator, proof-checker, and runtime evidence.

## Technical foundation

This chapter treats **scheduling, sandboxes, proof checking, and reproducible receipts** as a compiled language concern. In JA Test, Simulation, and Proof, a verification declaration is more than executable source: it is a stable claim connected to input construction, an oracle or proposition, typed semantics, a verification AST, an R12 execution or proof plan, a modeled runtime outcome, and an MCRT receipt. That chain makes a result reviewable before execution and reproducible after publication.

The central invariant is that **identical source, seed, clock, faults, resources, and runtime profile reproduce the same result**. The compiler must preserve this invariant during parsing, name resolution, type and effect analysis, proof-obligation generation, canonicalization, lowering, and optimization. The runtime must preserve it while scheduling tests, advancing virtual time, injecting failures, checking proofs, collecting coverage, measuring resources, shrinking counterexamples, and emitting receipts.

The principal counterexample is **hidden wall time, nondeterministic ordering, or stale caches**. Negative, boundary, security, determinism, recovery, and certification records are therefore essential. They define where the language must stop, which diagnostic should be stable, what evidence must remain unresolved, and which counterexample must survive minimization. Verification quality is measured as much by reliable rejection and honest uncertainty as by successful passes.

Implementation proceeds in explicit passes: parse stable source nodes; resolve fixtures, generators, tests, simulations, theorems, and dependencies; infer types, effects, capabilities, clocks, seeds, and resources; generate proof and replay obligations; lower accepted programs to R12; execute only inside the declared sandbox and virtual environment; preserve failures and counterexamples; and emit an MCRT verification receipt. Optimization is permitted only when this complete behavior remains equivalent.

## Representative corpus program

**Record:** `JATP-00018`  
**Feature:** `runtime_coverage`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `41939396170d83dd61667d202e04ac96d794ea75133276888a0d981d1fd0bf13`

```jap
ja source 0.3
module corpus.ja_proof.example_00018
use Proof
policy no_network

fixture FixtureJATP_00018 {
    input 20
    expected 380
}
unit test FixtureCheckJATP_00018 {
    let fixture_result = FixtureJATP_00018.input * 19
    assert fixture_result == FixtureJATP_00018.expected
}
property PropertyJATP_00018 for_all x: Count where x <= 20 {
    let result = x * 19
    invariant result >= x
}
simulation FailureJATP_00018 {
    virtual_time 20s
    inject network.partition at 19s
    expect service.recovers within 22s
}
benchmark BenchJATP_00018 limit cpu 20ms memory 27MB
assert proof.complete == true
emit mcrt "PropertyJATP_00018.proof.mcrt"
```

## Evidence trace

- Semantic identity: `sem-908fdf3edd3131676665`
- Judgment: `Environment; Policy; {simulation.execute} ⊢ node-f1e8b6a9d608deeca6a4 : VerificationBundle ! {pure} ⇒ validated`
- AST node: `node-f1e8b6a9d608deeca6a4` (`VerificationDecl`)
- Declared / inferred type: `VerificationBundle` / `VerificationBundle`
- Effects: `pure`
- Capabilities: `simulation.execute`
- Semantic operator: `generate`
- Policy decision: `allow`
- R12 record: `r12-d46cc2135a5891182281`
- MCRT record: `mcrt-39387a77f4d636f302c6`
- Determinism class: `R3-Deterministic`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA reviews semantic coherence and whether the declared oracle or proposition actually expresses the intended claim. CHARLOTTE reviews the legibility of fixtures, scenarios, failure schedules, proof dependencies, diagnostics, and evidence navigation. LANDON reviews parser, compiler, scheduler, simulator, proof checker, coverage engine, benchmark harness, sandbox, and replay feasibility. Professor requires a stated invariant, minimal counterexample, and defensible test oracle. Podium requires checksums, provenance, limitations, release integrity, and a certification decision tied to exact artifacts.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Confirm the fixture or generator domain and oracle are explicit.
- Record seeds, virtual clock rules, injected failures, and resource limits.
- Preserve proof obligations, theorem dependencies, and counterexamples.
- Name the measured coverage layer and benchmark environment.
- Verify network and unknown-code execution are explicitly governed.
- Verify optimization preserves results, diagnostics, traces, and receipts.

## Laboratory

**Task:** Build a replayable verification transaction.

1. Copy the representative program into a separate laboratory module.
2. Write the invariant and evidence boundary before changing the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, diagnostic, R12 change, runtime result, and MCRT outcome.
5. Run structural validation; label remaining results modeled unless a native toolchain is used.
6. Submit source, seeds or proof inputs, expected results, evidence map, replay data, limitations, and certification decision.

## Review questions

1. What exact claim does this program verify?
2. Which identity or hash must change when the oracle, seed, failure schedule, or proof changes?
3. At what stage should the primary unsafe or invalid case be rejected?
4. Which optimization is safe, and which would erase verification meaning?
5. What native test would promote the modeled outcome into execution evidence?

# Chapter 20: Optimization Without Verification Drift

## Learning objectives

- Explain safe canonicalization, caching, scheduling, and proof normalization across source, semantics, AST, R12, runtime, and MCRT layers.
- State and test the invariant that optimization preserves test oracles, counterexamples, theorem identity, failure schedule, and receipt.
- Construct a positive case and a minimal counterexample involving deduplication or caching that erases a distinct obligation or failure.
- Separate modeled corpus evidence from native compiler, simulator, proof-checker, and runtime evidence.

## Technical foundation

This chapter treats **safe canonicalization, caching, scheduling, and proof normalization** as a compiled language concern. In JA Test, Simulation, and Proof, a verification declaration is more than executable source: it is a stable claim connected to input construction, an oracle or proposition, typed semantics, a verification AST, an R12 execution or proof plan, a modeled runtime outcome, and an MCRT receipt. That chain makes a result reviewable before execution and reproducible after publication.

The central invariant is that **optimization preserves test oracles, counterexamples, theorem identity, failure schedule, and receipt**. The compiler must preserve this invariant during parsing, name resolution, type and effect analysis, proof-obligation generation, canonicalization, lowering, and optimization. The runtime must preserve it while scheduling tests, advancing virtual time, injecting failures, checking proofs, collecting coverage, measuring resources, shrinking counterexamples, and emitting receipts.

The principal counterexample is **deduplication or caching that erases a distinct obligation or failure**. Negative, boundary, security, determinism, recovery, and certification records are therefore essential. They define where the language must stop, which diagnostic should be stable, what evidence must remain unresolved, and which counterexample must survive minimization. Verification quality is measured as much by reliable rejection and honest uncertainty as by successful passes.

Implementation proceeds in explicit passes: parse stable source nodes; resolve fixtures, generators, tests, simulations, theorems, and dependencies; infer types, effects, capabilities, clocks, seeds, and resources; generate proof and replay obligations; lower accepted programs to R12; execute only inside the declared sandbox and virtual environment; preserve failures and counterexamples; and emit an MCRT verification receipt. Optimization is permitted only when this complete behavior remains equivalent.

## Representative corpus program

**Record:** `JATP-00024`  
**Feature:** `shrinker`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `69c7a7474fc802dedf5ed463e4d98e661ecb3202fe74aa3321f51cba0b3e0ac6`

```jap
ja source 0.3
module corpus.ja_proof.example_00024
use Proof
policy no_network

fixture FixtureJATP_00024 {
    input 26
    expected 650
}
unit test FixtureCheckJATP_00024 {
    let fixture_result = FixtureJATP_00024.input * 25
    assert fixture_result == FixtureJATP_00024.expected
}
property PropertyJATP_00024 for_all x: Count where x <= 26 {
    let result = x * 25
    invariant result >= x
}
simulation FailureJATP_00024 {
    virtual_time 26s
    inject network.partition at 25s
    expect service.recovers within 28s
}
benchmark BenchJATP_00024 limit cpu 26ms memory 33MB
assert proof.complete == true
emit mcrt "PropertyJATP_00024.proof.mcrt"
```

## Evidence trace

- Semantic identity: `sem-e25a72af98ced3d925f1`
- Judgment: `Environment; Policy; {simulation.execute} ⊢ node-b051a8b53685b36d1963 : VerificationBundle ! {pure} ⇒ validated`
- AST node: `node-b051a8b53685b36d1963` (`VerificationDecl`)
- Declared / inferred type: `VerificationBundle` / `VerificationBundle`
- Effects: `pure`
- Capabilities: `simulation.execute`
- Semantic operator: `fuzz`
- Policy decision: `allow`
- R12 record: `r12-fef0638a165ce89e9487`
- MCRT record: `mcrt-48e406ab24429bae0b49`
- Determinism class: `R3-Deterministic`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA reviews semantic coherence and whether the declared oracle or proposition actually expresses the intended claim. CHARLOTTE reviews the legibility of fixtures, scenarios, failure schedules, proof dependencies, diagnostics, and evidence navigation. LANDON reviews parser, compiler, scheduler, simulator, proof checker, coverage engine, benchmark harness, sandbox, and replay feasibility. Professor requires a stated invariant, minimal counterexample, and defensible test oracle. Podium requires checksums, provenance, limitations, release integrity, and a certification decision tied to exact artifacts.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Confirm the fixture or generator domain and oracle are explicit.
- Record seeds, virtual clock rules, injected failures, and resource limits.
- Preserve proof obligations, theorem dependencies, and counterexamples.
- Name the measured coverage layer and benchmark environment.
- Verify network and unknown-code execution are explicitly governed.
- Verify optimization preserves results, diagnostics, traces, and receipts.

## Laboratory

**Task:** Write equivalence and invalidation tests for an optimization.

1. Copy the representative program into a separate laboratory module.
2. Write the invariant and evidence boundary before changing the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, diagnostic, R12 change, runtime result, and MCRT outcome.
5. Run structural validation; label remaining results modeled unless a native toolchain is used.
6. Submit source, seeds or proof inputs, expected results, evidence map, replay data, limitations, and certification decision.

## Review questions

1. What exact claim does this program verify?
2. Which identity or hash must change when the oracle, seed, failure schedule, or proof changes?
3. At what stage should the primary unsafe or invalid case be rejected?
4. Which optimization is safe, and which would erase verification meaning?
5. What native test would promote the modeled outcome into execution evidence?

# Chapter 21: R12, MCRT, Certification, and Smithson 8S

## Learning objectives

- Explain provenance, uncertainty, relation classification, and evidence scope across source, semantics, AST, R12, runtime, and MCRT layers.
- State and test the invariant that modeled and native evidence remain distinct and limitations remain explicit.
- Construct a positive case and a minimal counterexample involving promoting projected, simulated, or modeled outcomes into unsupported physical or production claims.
- Separate modeled corpus evidence from native compiler, simulator, proof-checker, and runtime evidence.

## Technical foundation

This chapter treats **provenance, uncertainty, relation classification, and evidence scope** as a compiled language concern. In JA Test, Simulation, and Proof, a verification declaration is more than executable source: it is a stable claim connected to input construction, an oracle or proposition, typed semantics, a verification AST, an R12 execution or proof plan, a modeled runtime outcome, and an MCRT receipt. That chain makes a result reviewable before execution and reproducible after publication.

The central invariant is that **modeled and native evidence remain distinct and limitations remain explicit**. The compiler must preserve this invariant during parsing, name resolution, type and effect analysis, proof-obligation generation, canonicalization, lowering, and optimization. The runtime must preserve it while scheduling tests, advancing virtual time, injecting failures, checking proofs, collecting coverage, measuring resources, shrinking counterexamples, and emitting receipts.

The principal counterexample is **promoting projected, simulated, or modeled outcomes into unsupported physical or production claims**. Negative, boundary, security, determinism, recovery, and certification records are therefore essential. They define where the language must stop, which diagnostic should be stable, what evidence must remain unresolved, and which counterexample must survive minimization. Verification quality is measured as much by reliable rejection and honest uncertainty as by successful passes.

Implementation proceeds in explicit passes: parse stable source nodes; resolve fixtures, generators, tests, simulations, theorems, and dependencies; infer types, effects, capabilities, clocks, seeds, and resources; generate proof and replay obligations; lower accepted programs to R12; execute only inside the declared sandbox and virtual environment; preserve failures and counterexamples; and emit an MCRT verification receipt. Optimization is permitted only when this complete behavior remains equivalent.

## Representative corpus program

**Record:** `JATP-00030`  
**Feature:** `model_assertion`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `3ed90e20f6c911dbff6d198f7dd96910ea84a73a1d93cafb0b28079ccc5c3307`

```jap
ja source 0.3
module corpus.ja_proof.example_00030
use Proof
policy no_network

fixture FixtureJATP_00030 {
    input 32
    expected 992
}
unit test FixtureCheckJATP_00030 {
    let fixture_result = FixtureJATP_00030.input * 31
    assert fixture_result == FixtureJATP_00030.expected
}
property PropertyJATP_00030 for_all x: Count where x <= 32 {
    let result = x * 31
    invariant result >= x
}
simulation FailureJATP_00030 {
    virtual_time 32s
    inject network.partition at 31s
    expect service.recovers within 34s
}
benchmark BenchJATP_00030 limit cpu 32ms memory 39MB
assert proof.complete == true
emit mcrt "PropertyJATP_00030.proof.mcrt"
```

## Evidence trace

- Semantic identity: `sem-5ec8374b2248908b0098`
- Judgment: `Environment; Policy; {simulation.execute} ⊢ node-e4cb274ab7408fe329e1 : VerificationBundle ! {pure} ⇒ validated`
- AST node: `node-e4cb274ab7408fe329e1` (`VerificationDecl`)
- Declared / inferred type: `VerificationBundle` / `VerificationBundle`
- Effects: `pure`
- Capabilities: `simulation.execute`
- Semantic operator: `check_invariant`
- Policy decision: `allow`
- R12 record: `r12-5906c6559e278fefd22a`
- MCRT record: `mcrt-4dffc867e10db9f66ee2`
- Determinism class: `R3-Deterministic`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA reviews semantic coherence and whether the declared oracle or proposition actually expresses the intended claim. CHARLOTTE reviews the legibility of fixtures, scenarios, failure schedules, proof dependencies, diagnostics, and evidence navigation. LANDON reviews parser, compiler, scheduler, simulator, proof checker, coverage engine, benchmark harness, sandbox, and replay feasibility. Professor requires a stated invariant, minimal counterexample, and defensible test oracle. Podium requires checksums, provenance, limitations, release integrity, and a certification decision tied to exact artifacts.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Confirm the fixture or generator domain and oracle are explicit.
- Record seeds, virtual clock rules, injected failures, and resource limits.
- Preserve proof obligations, theorem dependencies, and counterexamples.
- Name the measured coverage layer and benchmark environment.
- Verify network and unknown-code execution are explicitly governed.
- Verify optimization preserves results, diagnostics, traces, and receipts.

## Laboratory

**Task:** Construct a certification packet with limitations and replay requirements.

1. Copy the representative program into a separate laboratory module.
2. Write the invariant and evidence boundary before changing the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, diagnostic, R12 change, runtime result, and MCRT outcome.
5. Run structural validation; label remaining results modeled unless a native toolchain is used.
6. Submit source, seeds or proof inputs, expected results, evidence map, replay data, limitations, and certification decision.

## Review questions

1. What exact claim does this program verify?
2. Which identity or hash must change when the oracle, seed, failure schedule, or proof changes?
3. At what stage should the primary unsafe or invalid case be rejected?
4. Which optimization is safe, and which would erase verification meaning?
5. What native test would promote the modeled outcome into execution evidence?

# Chapter 22: Standalone Test, Simulation, and Proof Toolchain Capstone

## Learning objectives

- Explain integrated authoring, compilation, simulation, proof, coverage, benchmark, replay, and publication across source, semantics, AST, R12, runtime, and MCRT layers.
- State and test the invariant that the release is deterministic, air-gap-safe, independently auditable, and honest about evidence.
- Construct a positive case and a minimal counterexample involving shipping a pass/fail dashboard without source, seeds, proofs, faults, resources, or receipts.
- Separate modeled corpus evidence from native compiler, simulator, proof-checker, and runtime evidence.

## Technical foundation

This chapter treats **integrated authoring, compilation, simulation, proof, coverage, benchmark, replay, and publication** as a compiled language concern. In JA Test, Simulation, and Proof, a verification declaration is more than executable source: it is a stable claim connected to input construction, an oracle or proposition, typed semantics, a verification AST, an R12 execution or proof plan, a modeled runtime outcome, and an MCRT receipt. That chain makes a result reviewable before execution and reproducible after publication.

The central invariant is that **the release is deterministic, air-gap-safe, independently auditable, and honest about evidence**. The compiler must preserve this invariant during parsing, name resolution, type and effect analysis, proof-obligation generation, canonicalization, lowering, and optimization. The runtime must preserve it while scheduling tests, advancing virtual time, injecting failures, checking proofs, collecting coverage, measuring resources, shrinking counterexamples, and emitting receipts.

The principal counterexample is **shipping a pass/fail dashboard without source, seeds, proofs, faults, resources, or receipts**. Negative, boundary, security, determinism, recovery, and certification records are therefore essential. They define where the language must stop, which diagnostic should be stable, what evidence must remain unresolved, and which counterexample must survive minimization. Verification quality is measured as much by reliable rejection and honest uncertainty as by successful passes.

Implementation proceeds in explicit passes: parse stable source nodes; resolve fixtures, generators, tests, simulations, theorems, and dependencies; infer types, effects, capabilities, clocks, seeds, and resources; generate proof and replay obligations; lower accepted programs to R12; execute only inside the declared sandbox and virtual environment; preserve failures and counterexamples; and emit an MCRT verification receipt. Optimization is permitted only when this complete behavior remains equivalent.

## Representative corpus program

**Record:** `JATP-00311`  
**Feature:** `integration_test`  
**Level:** `beginner`  
**Validation class:** `positive`  
**Source SHA-256:** `87bf0ac8a69e15856a913ac3e9950adaa360b0ad60c923b43b86ad1d640f8fdd`

```jap
ja source 0.3
module corpus.ja_proof.example_00311
use Proof
policy no_network

fixture FixtureJATP_00311 {
    input 22
    expected 44
}
unit test FixtureCheckJATP_00311 {
    let fixture_result = FixtureJATP_00311.input * 2
    assert fixture_result == FixtureJATP_00311.expected
}
property PropertyJATP_00311 for_all x: Count where x <= 22 {
    let result = x * 2
    invariant result >= x
}
simulation FailureJATP_00311 {
    virtual_time 22s
    inject network.partition at 2s
    expect service.recovers within 5s
}
benchmark BenchJATP_00311 limit cpu 22ms memory 10MB
assert proof.complete == true
emit mcrt "PropertyJATP_00311.proof.mcrt"
```

## Evidence trace

- Semantic identity: `sem-11f2f7073bfff2ce85fa`
- Judgment: `Environment; Policy; {proof.check} ⊢ node-bec30434184e39e12a66 : VerificationBundle ! {state.read} ⇒ validated`
- AST node: `node-bec30434184e39e12a66` (`VerificationDecl`)
- Declared / inferred type: `VerificationBundle` / `VerificationBundle`
- Effects: `state.read`
- Capabilities: `proof.check`
- Semantic operator: `shrink`
- Policy decision: `allow`
- R12 record: `r12-da83c1aa4f9fdefe2e6d`
- MCRT record: `mcrt-885755f0efee07d4f026`
- Determinism class: `R3-Deterministic`
- Expected validation: `pass`
- Diagnostic: `none`
- Evidence scope: modeled, not native execution

## Five-lens review

SOPHIA reviews semantic coherence and whether the declared oracle or proposition actually expresses the intended claim. CHARLOTTE reviews the legibility of fixtures, scenarios, failure schedules, proof dependencies, diagnostics, and evidence navigation. LANDON reviews parser, compiler, scheduler, simulator, proof checker, coverage engine, benchmark harness, sandbox, and replay feasibility. Professor requires a stated invariant, minimal counterexample, and defensible test oracle. Podium requires checksums, provenance, limitations, release integrity, and a certification decision tied to exact artifacts.

## Engineering checklist

- Confirm stable source, AST, R12, and MCRT identities.
- Confirm the fixture or generator domain and oracle are explicit.
- Record seeds, virtual clock rules, injected failures, and resource limits.
- Preserve proof obligations, theorem dependencies, and counterexamples.
- Name the measured coverage layer and benchmark environment.
- Verify network and unknown-code execution are explicitly governed.
- Verify optimization preserves results, diagnostics, traces, and receipts.

## Laboratory

**Task:** Build and certify a small offline verification toolchain.

1. Copy the representative program into a separate laboratory module.
2. Write the invariant and evidence boundary before changing the source.
3. Produce one accepted variant and one minimal rejected variant.
4. Predict the semantic judgment, diagnostic, R12 change, runtime result, and MCRT outcome.
5. Run structural validation; label remaining results modeled unless a native toolchain is used.
6. Submit source, seeds or proof inputs, expected results, evidence map, replay data, limitations, and certification decision.

## Review questions

1. What exact claim does this program verify?
2. Which identity or hash must change when the oracle, seed, failure schedule, or proof changes?
3. At what stage should the primary unsafe or invalid case be rejected?
4. Which optimization is safe, and which would erase verification meaning?
5. What native test would promote the modeled outcome into execution evidence?

# Appendix A: Evidence Vocabulary

- **Modeled evidence:** expected behavior supplied by the corpus.
- **Structural validation:** counts, hashes, declarations, catalogs, and package integrity.
- **Native compiler evidence:** observed parse, semantic, diagnostic, and lowering results.
- **Native simulation/proof evidence:** observed schedules, injected failures, proof checks, traces, counterexamples, coverage, and benchmarks.
- **Native runtime evidence:** observed execution, sandbox, recovery, replay, and receipt results.
- **Certification evidence:** signed decision identifying exact artifacts, tools, tests, limitations, and authority.

# Appendix B: Capstone Evidence Packet

1. Source and module identities
2. Fixture, generator, oracle, and property definitions
3. Scenario, virtual-time, event, and failure schedules
4. Theorem, lemma, obligation, and proof-term graph
5. Typed AST and semantic judgments
6. R12 verification plan
7. Sandbox, resource, and benchmark profiles
8. Coverage plan and results by layer
9. Counterexamples and shrink traces
10. Deterministic replay inputs and results
11. MCRT receipts
12. Structural and native test reports
13. Limitations and certification decision
