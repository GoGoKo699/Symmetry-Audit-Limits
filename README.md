# Symmetry Audit Limits

**How much testing is needed before a symmetry-protected phase can certify a three-body interaction?**

Two-body interactions can synthesize a three-body gate by briefly breaking symmetry. Checking symmetry only at the final time, or even at every point of a predetermined observation grid, can miss those excursions. This project gives a quantitative audit for a closed, repeatable three-qubit evolution with a known total Hamiltonian-strength bound.

The measured signal is the relative determinant phase of the two parity blocks. The exact-symmetry interaction witness is inherited from the theory of local symmetric circuits. The result here is a sharp temporal-mean leakage frontier and its matching statistical cost for ordinary parity-only tests.

## Principal results

Let $`L=JT`$, where $`J`$ bounds the operator norm of the complete Hamiltonian and $`T`$ is the evolution duration. Let $`\theta\in(0,\pi/8]`$ be the normalized circular distance of the endpoint parity-block determinant phase. Write $`\bar\ell`$ for the parity-transition probability averaged over a uniformly chosen computational-basis input and stopping time.

| Question | Supported result |
| --- | --- |
| How much leakage must a two-local explanation produce? | Every path with invertible endpoint parity blocks obeys $`\bar\ell\ge\theta^2/(32L^2)`$. For an exactly parity-preserving endpoint, the denominator improves to $`8L^2`$. |
| Is the leading mean-leakage coefficient sharp? | For the target family $`e^{-i\theta ZZZ}`$, $`\inf\bar\ell=(\theta^2+o(1))/L^2`$ as $`L\to\infty`$ at each fixed positive $`\theta`$. |
| Can the witness be audited with finite data? | Endpoint tomography plus privately randomized parity tests excludes every allowed two-local explanation with a specified false-certification probability. |
| What is the audit shot cost? | The matching order is $`\Theta((JT/\theta)^2\log(1/\delta))`$ for ordinary fresh-run, parity-only intermediate tests, at fixed endpoint conditioning and a declared phase-resolution floor comparable to $`\theta`$. |
| Do perfect scheduled symmetry checks suffice? | Exact two-local loops pass every uniform-grid checkpoint while accumulating a false phase of order $`J^2Th`$, where $`h`$ is the spacing. |

The lower bound for audit shots permits adaptively chosen stopping times and arbitrary endpoint data. It does not cover phase-sensitive intermediate probes or coherent queries. The protocol declares a minimum phase resolution before data collection and returns inconclusive below it, ensuring an unconditional hard resource cap. The matching construction attains the mean frontier for the stated target family; attainment for every parity-preserving endpoint is not claimed.

## Read the science

Start with the [scientific route](science/README.md). The [model](science/model.md) defines the tested process, observation class and certificate. The central proofs are the [phase–leakage bounds](science/phase-leakage.md), [matching controls](science/constructions.md), and [finite-confidence audit](science/audit-protocol.md). The [resource account](science/resources.md) charges endpoint tomography, repeated prefixes, trusted operations, timing resolution and classical processing.

For attribution, read the [comparison with primary work](references/related-work.md) and [bibliography](references/references.bib). Exact determinant constraints, symmetry-based interaction spectroscopy, holonomic geometry and low-population controls are established ingredients. The [LLM reading guide](llms.txt) maps specific questions to the authoritative files.

## Learn the project

The single educational anchor is **Domenico D’Alessandro, *Introduction to Quantum Control and Dynamics*, second edition**, identified by [DOI 10.1201/9781003051268](https://doi.org/10.1201/9781003051268). The [learning route](learning/README.md) connects its Hamiltonian-control foundations to this project's question. The [source bridge](learning/DALLESSANDRO_BRIDGE.md) gives verified reading pointers, notation translations, the locally supplied arguments and a complete three-qubit example.

The [30-milestone map](learning/MILESTONES.md) develops the prerequisites before following the phase witness, unavoidable hidden transfer, attaining controls and finite-confidence audit into one account. The map records project understanding targets for any reader; it contains no personal learner history.

## Reproduce the finite checks

```sh
python -m pip install -r verification/requirements.txt
python verification/run_checks.py
```

The [verification account](verification/README.md) explains the matrix identities, exact control constructions, numerical integrations and confidence calculations checked by the script. These diagnostics support the analytical account; they are not a proof of universal optimality or an exhaustive literature-priority check.

## Resources and scope

The physical device contains exactly three evolving qubits. Endpoint tomography additionally uses three isolated reference qubits. The theorem assumes unitary repeatable dynamics, a trusted total norm bound, trusted preparation and parity readout, and stopping times that cannot change the fixed waveform. A hidden mediator, extra level or environment changes the model.

Conditional on the endpoint data and selected fixed budget of $`N_A`$ midpoint audit shots, expected charged unknown-evolution time is $`N_ET+N_AT/2`$, where $`N_E`$ counts endpoint shots. The declared resolution also gives an unconditional hard cap on calls and a bound on expected time across all data branches. Preparation, reset, readout and timing are additional counted operations with platform-dependent durations. The matching controls allow drive bandwidth to grow as leakage shrinks. There is no fixed-bandwidth optimum, noisy-readout theorem, unrestricted quantum-verification lower bound or demonstrated hardware crossover.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

## License

See [LICENSE](LICENSE).
