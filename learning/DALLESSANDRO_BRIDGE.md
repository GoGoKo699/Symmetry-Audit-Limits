# From quantum control to a symmetry audit

The starting question is concrete: a device produces a phase associated with three qubits acting together. Could an unknown sequence of one- and two-qubit interactions have produced the same endpoint? In general it could. A symmetry constraint on the entire evolution changes the answer, but a finite experiment must justify that constraint. This bridge explains how the project turns that gap into a measurable probability and a resource law.

## The single source and its edition

The educational anchor is **Domenico D’Alessandro, *Introduction to Quantum Control and Dynamics*, second edition**, CRC Press, DOI [10.1201/9781003051268](https://doi.org/10.1201/9781003051268), hardcover ISBN **9780367507909**. The [publisher catalog](https://www.routledge.com/link/link/p/book/9780367507909) uses 2021; the publisher-produced [preview frontmatter](https://api.pageplace.de/preview/DT0400.9781000394993_A40919156/preview-9781000394993_A40919156.pdf) states 2022. This route retains that same second edition. Section numbers and printed page starts below were checked against its contents; detailed project proofs are supplied locally rather than attributed to unread textbook passages.

## Targeted reading route

Read the relevant part alongside the corresponding project explanation. The whole book is not a prerequisite.

| Source pointer | Use in this project | Continue here |
| --- | --- | --- |
| §§1.1.3–1.1.5, pp. 8–13; §1.4.2, p. 34 | Tensor factors versus a direct-sum sector decomposition. | [Model](../science/model.md) |
| §§1.2.2–1.2.3, pp. 20–25; §1.3, p. 27 | Probabilities, repeated preparations and unitary evolution. | [Example below](#worked-example-two-paths-one-endpoint) |
| §§2.4.2 and 2.5.2–2.5.3, pp. 68, 73–74 | Spin controls, the propagator and measured outputs. | [Audit contract](../science/audit-protocol.md#device-and-access-contract) |
| §§3.1–3.2, pp. 82–89; §4.3, p. 131 | Lie-generated reachability and symmetry decomposition. | [Phase-leakage identity](../science/phase-leakage.md#the-phase-leakage-identity) |
| §6.1, p. 169; Appendix E, p. 363 | Two-level control, Euler coordinates and commutators. | [Exact paths](../science/constructions.md) |
| §§5.1–5.2, pp. 151–157 | Tomography and limits of observable information. | [Endpoint measurement](../science/audit-protocol.md#finite-endpoint-measurements) |
| §§7.1 and 7.4.1, pp. 200, 214 | Declaring a control objective and its bounded resources. | [Resource account](../science/resources.md) |

## Notation and assumptions

| Object | Meaning here | Distinction that matters |
| --- | --- | --- |
| $H(t)$ and $U(t)$ | The Hermitian generator and its propagator, with $\dot U=-iHU$ and $\hbar=1$. | A description of the endpoint $U(T)$ does not uniquely describe $H(t)$. |
| $iH$ or $-iH$ in Lie-algebra notation | A skew-Hermitian generator; the sign is conventional when real linear spans are taken. | Physical evolution throughout this account uses $\dot U=-iHU$. |
| Two-local Hamiltonian | A sum of Pauli terms, each acting nontrivially on at most two of the three qubits. | The sum can act on all three qubits. Body order counts each term’s support. |
| $J$ | A bound on the operator norm of the complete Hamiltonian. | Separate norm budgets for individual terms would define a different constraint. |
| $P_+$ and $P_-$ | Projectors onto positive and negative parity. | They select subspaces, not separate physical registers. |
| Reachability and time cost | Whether a target is possible, and the duration required under a resource bound. | A Lie-algebra reachability calculation alone does not determine that duration. |
| $q(t)^2$ and $\ell(t)$ | Worst-input and basis-averaged probabilities of changing parity. | Their square roots are amplitudes; confusing amplitude with probability changes the scaling. |
| $\vartheta(U)$ | One eighth of the shortest relative determinant-phase angle of the two endpoint blocks. | It is invariant under a common global phase; wrapping modulo $2\pi$ is retained. |

The unknown evolution is a closed, repeatable three-qubit unitary process. The endpoint protocol uses three additional isolated reference qubits for trusted measurements; they do not participate in the unknown dynamics. There is no unobserved mediator, retained device memory or device response to the privately selected stopping time. The norm bound, input preparation, readout and timing accuracy are trusted inputs to the theorem.

## Worked example: two paths, one endpoint

Take units with $J=1$, total duration $T=4$, and the target

$$
W=\exp(-i\Pi/4),\qquad \Pi=Z_1Z_2Z_3.
$$

The dimensionless action is $L=JT=4$. Positive parity means an even number of ones in the computational basis, so the four positive-parity inputs are

$$
|000\rangle,\quad |011\rangle,\quad |101\rangle,\quad |110\rangle.
$$

Each is an eigenstate of $\Pi$ with eigenvalue $+1$. The other four basis states have eigenvalue $-1$.

### The endpoint phase is observable, but not sufficient

A genuinely three-body path can use the constant Hamiltonian

$$
H_3=\Pi/16.
$$

Its norm is $1/16\leq J$, its duration is four, and its propagator at the endpoint is $W$. It never changes parity. On the positive sector the endpoint is $e^{-i/4}I_4$, and on the negative sector it is $e^{i/4}I_4$. Hence

$$
\frac{\det W_+}{\det W_-}=e^{-2i},
\qquad \vartheta(W)=\frac{2}{8}=\frac14.
$$

This phase cannot be produced by a two-local Hamiltonian that preserves parity at every time. That exact obstruction is inherited from the symmetry-locality literature. It does not rule out a two-local path that temporarily transfers amplitude between the sectors and returns it before the endpoint.

### A two-local path can return exactly

Choose

$$
A_0=X_1Z_2,\qquad B_0=Y_1Z_3.
$$

Both terms are two local, but $A_0B_0=i\Pi$. Their control algebra therefore contains the direction needed for the target phase. The [exact latitude construction](../science/constructions.md#a-latitude-path-with-an-exact-endpoint) uses only Hamiltonians in their span, with complete norm at most one.

For this example its small parameter $\alpha_0$ solves

$$
\frac14\cot\alpha_0+2\alpha_0=4.
$$

The small root is approximately $0.064493$. A short ramp moves amplitude out of its initial parity sector; a driven plateau accumulates phase; a final ramp returns the amplitude. The endpoint is exactly $W$, while

$$
q(t)^2=\ell(t)\leq\sin^2\alpha_0\simeq0.004154.
$$

Its true temporal mean is approximately $0.004064$. Every endpoint input-output experiment has the same predictions for this path and the three-body path. Intermediate measurements distinguish them. This is an effective three-qubit model statement: no claim is made that a hidden mediator has been excluded by measuring the three qubits alone.

The control phase on the plateau rotates increasingly rapidly as the excursion is reduced. The norm is charged, but temporal bandwidth is unrestricted. The construction is not an optimum under a fixed bandwidth constraint.

### Random stopping turns a mean into a probability

In one fresh audit run, choose one of the four positive-parity basis inputs uniformly, choose a stopping time privately, and measure parity at that time. Conditional on a time $t$, the negative-parity probability is exactly

$$
\ell(t)=\frac14\operatorname{Tr}\left[C(t)^\dagger C(t)\right],
\qquad C(t)=P_-U(t)P_+.
$$

With a continuous uniform stopping time, its event probability is the temporal mean $\bar\ell$. The [universal converse](../science/phase-leakage.md#a-true-temporal-mean-without-a-ceiling) says that every norm-bounded two-local path with this parity-preserving endpoint obeys

$$
\bar\ell\geq\frac{(1/4)^2}{8\cdot4^2}
=\frac1{2048}.
$$

This lower bound permits large excursions and singular intermediate blocks. It does not assume the path resembles the latitude example. The large-action theorem sharpens the leading coefficient at fixed phase; it does not claim that this finite-action lower bound is exact.

### A finite-confidence version also pays for the endpoint

Declare the phase floor $g=1/16$ and total failure budget $\delta=0.05$, split as $\delta_E=\delta_A=0.025$. The floor is fixed before observing data. It makes poorly resolved endpoint data inconclusive instead of allowing an arbitrarily small positive estimate to demand an arbitrarily large audit.

For a fully explicit endpoint method, use the [six-qubit Choi tomography procedure](../science/audit-protocol.md#finite-endpoint-measurements). One permissible statistical tolerance is $s=1/4000$. Its state-matrix radius is $e=8s=0.002$, and its statistical propagator radius is $4e/(1-e)<0.008017$. Budget numerical matrix and singular-value errors inside a total radius $t=0.01$, and phase arithmetic error at most $0.001$. For the target’s true block singular values equal to one, a certified lower estimate $\sigma\geq0.99$ then gives total angular radius at most

$$
\arcsin(0.01/0.99)+0.001<0.011102.
$$

On the endpoint confidence event, this resolves more than enough phase to retain the conservative lower confidence bound $\theta_0=1/8$. Using only that much resolved phase keeps the arithmetic simple; a larger valid bound saves audit shots. A failed conditioning check or an endpoint lower bound below $g$ returns inconclusive.

Now use $K=725$ equally spaced stopping bins, selecting one midpoint uniformly in each independent audit run. This follows the sufficient finite-timing choice

$$
K=\left\lceil\frac{\sqrt{32}L^2}{\theta_0}\right\rceil.
$$

The bin width is $4/725$. Under exact midpoint timing, every two-local alternative consistent with the endpoint confidence bound has mean sampled event probability at least $1/131072$. Consequently

$$
N_A=\left\lceil128(L/\theta_0)^2\ln40\right\rceil
=483509
$$

audit shots suffice. If all outcomes preserve parity, issue the certificate; if a parity change occurs, this procedure does not issue it. A change does not itself identify the Hamiltonian. For every admitted two-local alternative, the probability of issuing a false certificate is at most $0.025+0.025=0.05$.

The constant three-body path has no audit events. The two-local latitude path has the same endpoint but a nonzero event probability. The theorem controls every admitted two-local path, not only this convenient example.

### The resource bill

| Part | Unknown-evolution runs | Unknown-evolution time in these units | Other charged requirements |
| --- | --- | --- | --- |
| Explicit endpoint procedure | $N_E=4095\lceil32000000\ln327600\rceil$, about $1.66\times10^{12}$ | $4N_E$ | Fresh three-Bell-pair preparation and six-qubit Pauli readout in each run; fixed-dimensional numerical certification. |
| Audit on the resolved branch above | $483509$ | Nominal mean $N_AT/2=967018$; hard bound below $4N_A$ | Fresh basis preparation, parity readout, private bin selection and stopping resolution in every run. |
| Audit cap over every endpoint-data record | At most $1934036$ | Nominal mean at most twice that cap | The cap follows from the predeclared floor; inconclusive branches execute no audit shots. |

The endpoint count is a deliberately conservative ordinary-shot construction, not an optimal tomography estimate or a practical implementation claim. Its large constant must remain visible. Total expected nominal unknown-evolution time is at most $4N_E+2N_{\max}$, and the hard bound is $4(N_E+N_{\max})$. Known preparation, reset and readout durations must be added. The exact midpoint example also assumes trusted stopping accuracy; [resources](../science/resources.md#leakage-audit-cost-and-physical-time) gives a finite timing-error budget and its larger mesh.

No controlled unknown prefix, inverse unknown evolution, amplitude amplification or coherent storage across audit runs is used. For fixed resolved phase and large $JT$, the number of ordinary leakage-only shots has the matching order $(JT/\theta)^2\log(1/\delta)$. That lower bound does not cover intermediate phase-sensitive probes or unrestricted coherent process identification.

## The steps supplied by this project

The book’s control language explains how to formulate a generator, reachable set, output and resource constraint. The project supplies the connection needed for this task:

1. The [model](../science/model.md) specifies the closed system, observables and trusted information.
2. The [phase-leakage identity and converse](../science/phase-leakage.md) connect a forbidden endpoint phase to unavoidable intermediate transfer, including a true temporal mean without a pointwise ceiling.
3. The [construction](../science/constructions.md) gives exact endpoints and shows the asymptotic mean-transfer coefficient is attainable.
4. The [audit](../science/audit-protocol.md) turns that mean into a finite-data certificate, with endpoint confidence, discrete stopping times and a fixed phase floor.
5. The [resource account](../science/resources.md) prices repeated prefixes and states the restricted observation class for which the shot order matches.

The determinant and geometric foundations have their own [primary attribution](../references/related-work.md). They are not presented as results proved in the selected textbook. The [thirty-milestone map](MILESTONES.md) follows these connections from local objects to the complete argument; the [scientific overview](../science/README.md) gives the direct proof route.
