# The inference task

## A phase signal and the assumption behind it

For three qubits define parity $\Pi=Z_1Z_2Z_3$. If a Hamiltonian commutes with parity throughout an evolution, its propagator separates into two four-dimensional blocks. Their relative determinant phase measures an integrated trace of the Hamiltonian against $\Pi$. Every one- or two-qubit Pauli term has zero such trace. Consequently a nonzero phase excludes a two-local explanation under exact trajectory symmetry.

This determinant observation and its interaction-spectroscopy motivation are inherited. The question here is how to replace an exact, continuously imposed symmetry assumption by finite observations of a repeatable process.

Endpoint symmetry is insufficient. A two-local control can leave a parity sector, accumulate a phase, and return exactly. This can happen in every interval between predetermined observations. The audit must therefore account for both how much transfer is hidden and how observations sample time.

## Tested dynamics

The device Hilbert space is exactly $(\mathbb C^2)^{\otimes3}$. Each run implements the same propagator on $[0,T]$, beginning at identity. There are no additional evolving levels, ancillary systems, measurements, resets, retained quantum controller or unknown environment in the tested process. An observer's isolated references used for endpoint measurements do not interact with it.

The known strength assumption is a uniform operator-norm bound $\|H(t)\|\le J$ almost everywhere, in a common scalar-phase convention. A scalar term does not affect any measured phase difference or transition probability. The bound concerns the complete Hamiltonian, including all simultaneous controls; the decomposition into local terms does not supply separate budgets. Units have $\hbar=1$.

The null model contains every such Hamiltonian whose Pauli expansion has weight at most two, with arbitrary real time-dependent coefficients. All pairs and single-qubit fields are admitted. There is no limit on pulse count or driving bandwidth. This makes the converse robust to driven two-local synthesis, while the matching construction's required bandwidth remains a resource qualification.

The allowed process must be fixed independently of a run's privately chosen stopping time. Prefix experiments reproduce the same earlier trajectory. Stopping an experiment freezes its evolution for trusted readout and supplies no advance information to the device. These are access assumptions, not conclusions of endpoint tomography.

## Observables

Write $P_\pm=(I\pm\Pi)/2$ and

$$
U(t)=\begin{pmatrix}A(t)&B(t)\\C(t)&D(t)\end{pmatrix}.
$$

The principal quantities are:

| Symbol | Meaning |
| --- | --- |
| $q(t)=\|C(t)\|=\|B(t)\|$ | Largest parity-transition amplitude over a definite-parity input. |
| $\ell(t)=\operatorname{tr}(C^\dagger C)/4$ | Transition probability from a uniformly chosen positive-parity computational-basis input; equal to averaging over all eight basis inputs. |
| $\bar\ell=T^{-1}\int_0^T\ell(t)dt$ | Space-and-time averaged physical transition probability. |
| $L=JT$ | Dimensionless strength–duration budget. |
| $\vartheta(U)=\operatorname{dist}(\arg\det A-\arg\det D,2\pi\mathbb Z)/8$ | Endpoint phase distance, defined when both blocks are invertible and invariant under a common phase. |
| $\theta_0$ | A lower confidence bound on the endpoint phase distance, derived from independent endpoint data. |

The phase is circular and lies in $[0,\pi/8]$. It is not an unbounded accumulated phase. For $e^{-i\theta\Pi}$ with $0<\theta\le\pi/8$ the distance equals $\theta$; at $\theta=\pi/4$ the determinant obstruction vanishes. Arbitrary unitaries within either endpoint parity sector are allowed by the lower bounds.

## Certificate and observation class

The finite procedure declares a minimum phase resolution and measurement budget before acquiring data, then estimates the endpoint phase with a confidence radius. It returns inconclusive when the signal falls below that resolution or block conditioning is unresolved. Otherwise it uses fresh runs stopped at privately randomized times, prepares a definite-parity basis state, and retains the parity-change bit. If all prescribed tests have no transition, it issues a certificate excluding every member of the two-local null model at the stated false-certification probability. The fixed resolution makes its resource cap unconditional, including on rare endpoint-estimation failures.

A detected transition does not prove two-locality and is not a failed scientific theorem. It means that this one-sided certificate is not issued. A parity-preserving trajectory with a resolved nonzero endpoint phase passes the trusted-measurement audit, even in the presence of unknown symmetric nuisance dynamics.

The matched lower bound permits adaptively chosen stopping times and definite-parity inputs, plus arbitrary endpoint measurements. It concerns ordinary fresh-run parity-only intermediate data. Intermediate phase measurements, coherent device histories, controlled unknown evolution and inverse access are richer models and are not subject to that shot lower bound.

## What is inferred physically

Within the stated closed three-qubit unitary model, rejecting all bounded-norm two-local explanations establishes the need for a higher-body Hamiltonian component. It does not identify its microscopic origin or certify the absence of an unobserved mediator. Under exact trajectory symmetry and the narrower form $H=H_{2,\mathrm{sym}}+g(t)\Pi$, the inherited phase identity additionally measures $\int g(t)dt$ modulo its phase period. The finite audit alone should not be promoted to unique Hamiltonian reconstruction.

Trusted preparation/readout, reference isolation, a known strength bound, waveform repeatability and stopping accuracy are material assumptions. Unknown SPAM backgrounds or nonunitary dynamics require a different statistical account. [Resources](resources.md) records the cost of the accesses used here.
