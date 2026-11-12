# Resources and boundaries of the audit

The task is to exclude every norm-bounded two-local explanation of an observed forbidden endpoint parity phase. The [audit protocol](audit-protocol.md) supplies a finite-confidence procedure and a matching lower bound for leakage-only independent shots. This page records what the procedure actually uses.

Let $`a=JT`$ and declare a phase-resolution floor $`g\in(0,\pi/32]`$ before collecting data. Let $`\theta_0`$ be the endpoint lower confidence bound and total false-certification probability be at most $`\delta=\delta_E+\delta_A`$. A branch executes the leakage audit only when $`\theta_0\geq g`$; otherwise it returns inconclusive. This gives a hard global budget even for erroneous or poorly resolved endpoint data. All logarithms in tail bounds are natural.

## Access and trusted resources

| Resource | Required access or accounting |
| --- | --- |
| Unknown device | One repeatable three-qubit unitary waveform $`U(t)`$ on $`0\leq t\leq T`$; no retained hidden quantum state between runs. |
| Strength information | A trusted almost-everywhere bound $`\|H(t)\|\leq J`$ in a common scalar-phase convention. This is an assumption, not inferred from endpoint tomography. |
| Unknown evolution call | A physical evolution prefix from zero to the chosen stopping time; every repeated prefix is charged. |
| Stopping | Private random choice, implemented to the stated mesh accuracy; the fixed waveform cannot adapt to that choice. |
| Audit input and output | Fresh computational-basis positive-parity input and a trusted parity readout; one retained leakage bit per audit run. |
| Endpoint input and output | Three trusted Bell pairs, isolation of the reference halves during evolution, and trusted six-qubit Pauli measurements on independent runs. |
| Known operations | Preparation, resets, measurement rotations, readout, timing, and classical processing are needed in every run. Their counts are explicit below; their device-dependent durations and fidelities are not optimized. |
| Coherent access | No controlled unknown evolution, inverse unknown evolution, QRAM, coherent superposition of run histories, or amplitude amplification is used by the upper bound. The lower bound does not exclude improvements using richer intermediate access. |

The physical evolution has width three during the leakage audit and width six during the explicit endpoint procedure, counting the three isolated reference qubits. There is no growing quantum memory. A noisy or open-system device does not satisfy the theorem merely because its final channel is close to a unitary.

## Endpoint phase cost

An explicit ordinary-shot endpoint method uses $`m=4095`$ Pauli settings on a $`D=64`$ dimensional Choi state. For an expectation tolerance $`s`$, take

```math
M=\left\lceil\frac{2}{s^2}\log\frac{2m}{\delta_E}\right\rceil,
\qquad N_E=mM.
```

There are exactly $`N_E`$ full unknown evolutions of duration $`T`$, so unknown endpoint evolution time is $`N_ET`$. There are also $`N_E`$ fresh three-Bell-pair preparations, resets, and six-qubit Pauli readouts. All these known circuits have constant size at this fixed dimension; this does not make them physically free.

The linear-inversion confidence radius is $`e=8s<1/2`$. Reshaping the top eigenvector gives a statistical endpoint matrix radius $`4e/(1-e)`$; add the declared numerical matrix and singular-value margins to obtain $`t`$. Use a certified lower singular-value estimate $`\sigma`$, budgeting its error in the same total radius. If $`\sigma>t`$, and $`b_{\mathrm{num}}`$ bounds numerical phase error, the phase lower confidence bound is

```math
\theta_0=\left[\widehat\theta-\arcsin(t/\sigma)-b_{\mathrm{num}}\right]_+.
```

If $`\theta_0<g`$ or the conditioning test fails, the audit returns inconclusive at the chosen endpoint resolution. Extra endpoint shots are a possible new run of this same measurement task; they are not silently counted as a successful certificate. Any adaptive repetition of endpoint confidence tests must allocate a summable failure budget or use a valid confidence sequence, rather than reusing $`\delta_E`$ for every attempt. The single-run global cap below does not include an unbounded sequence of such retries.

For a declared endpoint conditioning-resolution target $`\sigma_0\in(0,1]`$, preselect $`t\leq\sigma_0\sin(g)/4`$ and $`b_{\mathrm{num}}\leq g/2`$, including all numerical margins. On the class with true minimum block singular value at least $`\sigma_0`$ and true phase $`\theta\geq4g`$, the endpoint confidence event guarantees $`\sigma\geq3\sigma_0/4`$, total angular radius at most $`g`$, and $`\theta_0\geq\theta-2g\geq2g`$. Thus it passes the fixed floor. Fixed-fraction statistical and numerical error allocations give

```math
N_E=O\!\left(\sigma_0^{-2}g^{-2}\log(1/\delta_E)\right)
```

with a large but fixed dimension-dependent constant for this deliberately simple tomography scheme. Soundness does not assume that the true endpoint obeys the conditioning target; failure to resolve it can instead produce inconclusive. For a parity-preserving endpoint, the completeness target may be $`\sigma_0=1`$. This is an upper bound for the supplied method, not an optimal endpoint-tomography theorem.

Classically, the method accumulates $`4095`$ counters, forms one $`64\times64`$ Hermitian matrix, finds its top eigenvector, and computes singular values and determinants of two $`4\times4`$ matrices. Streaming accumulation costs $`O(N_E)`$ arithmetic operations; the matrix step has fixed dimension and $`O(64^3)`$ arithmetic complexity with standard dense methods. Sufficient arithmetic precision and numerical error margins must be retained when computing the phase certificate. The required bit precision grows logarithmically with the desired matrix and phase tolerances; no infinite-precision endpoint matrix is supplied as input.

## Leakage audit cost and physical time

For the finite timing version, choose

```math
K=\left\lceil\frac{\sqrt{32}\,a^2}{\theta_0}\right\rceil,
\qquad h=T/K,
```

and select one midpoint uniformly per audit run. The hard audit shot budget is

```math
N_A=\left\lceil128(a/\theta_0)^2\log(1/\delta_A)\right\rceil.
```

The finite timing mesh is part of the guarantee. It is sufficient that $`h\leq\theta_0/(\sqrt{32}J^2T)`$; there is no assumption that a finite device samples an exact real number uniformly. Sampling a bin needs $`O(\log K)`$ random bits, using rejection sampling when $`K`$ is not a power of two. The expected number of random-index trials is less than two. Positive-parity basis preparation needs two additional random bits. No table of $`K`$ quantum control programs is needed.

The stated mesh uses the selected midpoint times. If actual stopping has a trusted error at most $`r_t`$, require $`h/2+r_t\leq\theta_0/(2\sqrt{32}J^2T)`$ instead. Doubling $`K`$ and ensuring $`r_t\leq h/2`$ is sufficient. Resolving those times needs $`O(\log(T/r_t))`$ clock-address bits when such a finite clock is used; the physical cost of producing that timing accuracy remains an explicit hardware requirement.

Every selected midpoint has mean $`T/2`$. Conditional on the endpoint data and the resulting fixed budget $`N_A`$, the expected charged unknown evolution time is therefore

```math
\boxed{\quad \mathbb E[T_{\mathrm{unknown,audit}}]=N_AT/2.\quad}
```

The hard worst-case evolution time is less than $`N_AT`$. With bounded stopping error $`r_t`$, the actual expected audit evolution time lies between $`N_A(T/2-r_t)`$ and $`N_A(T/2+r_t)`$, provided all stops remain in $`[0,T]`$; the doubled-mesh choice above guarantees this. This count includes failed audit runs if the prescribed fixed budget is executed; stopping immediately after the first leakage event can only reduce time on paths that fail certification. The honest parity-preserving path always consumes the full no-event budget.

The audit also needs $`N_A`$ fresh preparations/resets and parity readouts, and $`O(N_A\log K)`$ random-bit processing. Streaming memory consists of a counter, a leakage flag, and the timing index: $`O(\log N_A+\log K)`$ bits. The endpoint counters are separate fixed-setting classical storage.

The fixed floor gives unconditional caps on every executed branch, including an endpoint-confidence failure:

```math
K\leq K_{\max}=\left\lceil\frac{\sqrt{32}\,a^2}{g}\right\rceil,
\qquad
N_A\leq N_{\max}=\left\lceil128(a/g)^2\log(1/\delta_A)\right\rceil.
```

For the bounded stopping-error variant, selecting $`K=\lceil2\sqrt{32}a^2/\theta_0\rceil`$ instead gives $`K\leq\lceil2\sqrt{32}a^2/g\rceil`$. The audit run cap remains $`N_{\max}`$.

Set the executed audit count to zero on an inconclusive endpoint branch. Conditional on endpoint data, its nominal expected unknown evolution time is

```math
\mathbb E[T_{\mathrm{unknown,total}}\mid\text{endpoint data}]=N_ET+N_AT/2.
```

Unconditionally, the protocol uses at most $`N_E+N_{\max}`$ unknown-evolution runs, expected nominal unknown evolution time at most $`N_ET+N_{\max}T/2`$, and hard worst-case unknown evolution time at most $`(N_E+N_{\max})T`$. A stopping error $`r_t`$ adds at most $`N_{\max}r_t`$ to the expected-time upper bound. If known preparation, reset, and readout take $`\tau_E`$ per endpoint run and $`\tau_A`$ per audit run, add at most $`N_E\tau_E+N_{\max}\tau_A`$ to laboratory elapsed time, as well as the actual timing/control and classical-processing overhead. No universal numerical duration is assigned to these platform-dependent operations.

For $`a\geq1`$ and fixed endpoint conditioning, the declared resolution class has endpoint-plus-audit run cap $`O(a^2g^{-2}\log(1/\delta))`$. When a resolved phase $`\theta`$ is compared at a declared floor of the same order, such as $`g=\theta/4`$, the large-action leakage-audit shot cost is

```math
\Theta\!\left((JT/\theta)^2\log(1/\delta)\right).
```

Its unconditional expected nominal unknown evolution time is at most of order $`J^2T^3g^{-2}\log(1/\delta)`$, in addition to endpoint measurement time, and has the stated $`\theta`$ scaling when $`g`$ is comparable to $`\theta`$. The matching result concerns this resolved-phase class; an arbitrarily small random positive $`\theta_0`$ supplies no uniform resource law without the fixed floor. Increasing the observation horizon makes the possible two-local micromotion harder to rule out under a fixed integrated phase; it does not supply free repetitions.

## What the matching lower bound means

The lower bound applies to a hard cap on the number of ordinary leakage-audit runs. Within a run, the input has definite parity, the device can be stopped at any chosen time, and the retained datum is the parity-change bit. The choices may be adaptive, and arbitrary independent endpoint data may be supplied. The hard family has exactly the same endpoint unitary for an honest parity-preserving three-body path and a driven two-local spoof, so endpoint data cannot distinguish that pair.

The spoof has parity-change probability at most $`C\theta^2/(JT)^2`$ for every stopping time and every definite-parity input. Before

```math
\Omega\!\left((JT/\theta)^2\log(1/\delta)\right)
```

runs, its all-no-event transcript cannot be reliably separated from the honest transcript. Thus adaptively choosing times does not remove the shot cost in this access class.

The result is not an unrestricted quantum-query lower bound. It does not constrain a verifier that observes intermediate relative phases, retains coherent device histories, implements controlled unknown prefixes or inverses, or uses a different Hamiltonian-identification task. It is also not a lower bound on the optimal total laboratory time across all stopping distributions and all richer measurements.

## Deterministic inspections and experimental noise

The deterministic-grid counterexample is an exact dynamical statement: a two-local drive can restore parity at every scheduled inspection while accumulating a nonzero forbidden phase between inspections. It does not turn a finite collection of zero observed counts into a proof of zero transition probability. Finite-confidence zero-count interpretation is supplied by the random-audit protocol, not by the counterexample.

The theorem assumes trusted ideal input and parity measurement. A calibrated nonzero background can be modelled in a separate statistical task; an unknown background cannot simply be subtracted. At a fixed background rate, the small-signal discrimination cost may differ from the zero-background law. No realistic-SPAM threshold, decoherence theorem, or practical crossover is claimed here.

The certificate rules out the stated bounded-norm two-local model. It does not distinguish a true three-qubit term from an unmodelled mediator, hidden memory, a violated strength bound, or a waveform that changes with the selected stopping time. Those possibilities are excluded by the access contract and must not be relabelled as experimentally certified facts.
