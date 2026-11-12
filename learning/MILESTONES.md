# Thirty milestones from controlled dynamics to a symmetry audit

This is a common understanding map of the project. Its single educational anchor is Domenico D’Alessandro, *Introduction to Quantum Control and Dynamics*, **second edition**. The [source bridge](DALLESSANDRO_BRIDGE.md) identifies the edition, reading route, notation, and steps supplied by this project. Section numbers below refer to that edition; they are reading pointers, not claims that the book contains this project's new bounds.

The map has **12 background milestones and 18 narrative milestones**. The background first joins the local objects—states, generators, parity blocks, and individual measurements—into a complete inference model. The narrative then joins the phase identity, hidden excursions, attaining paths, endpoint confidence, sampling, and resource accounting into one finite audit. The larger narrative allocation reflects the main difficulty: a correct phase invariant must be converted into an observation procedure with a hard budget and an honest access boundary.

The linked scientific statements and proofs are authoritative. This map does not cover every calculation or supply a personal assessment protocol. In particular, the sampling-confidence and finite-resolution arguments are proved in the project; they are not attributed to the control textbook.

## Background and preliminaries

### M01 — Identify the evolving device

- **Central question:** What does it mean to describe the experiment as a closed three-qubit process?
- **Understanding target:** Distinguish the three evolving device qubits from isolated measurement references, and explain why an unobserved mediator changes the tested Hamiltonian model.
- **Dependencies and story role:** Entry point. It establishes which physical degrees of freedom every later locality statement concerns.
- **Conceptual connection:** A finite-dimensional state-space model is also an inference commitment; tracing out an extra system can change what counts as a direct interaction.
- **Sources:** Anchor §§1.1, 1.1.3–1.1.4; [model: tested dynamics](../science/model.md#tested-dynamics) and [physical inference](../science/model.md#what-is-inferred-physically).

### M02 — Charge the complete generator

- **Central question:** What makes a Hamiltonian two-local, and what does its strength bound charge?
- **Understanding target:** Read Pauli support as the number of qubits acted on nontrivially. Distinguish a norm bound on the complete simultaneous Hamiltonian from separate bounds on its listed terms.
- **Dependencies and story role:** Builds on M01 by specifying the alternative that the audit will exclude.
- **Conceptual connection:** Tensor-product support describes locality, while operator norm controls physical evolution speed; neither substitutes for the other.
- **Sources:** Anchor §§1.1.3, 2.4.2, 7.1.2; [model: tested dynamics](../science/model.md#tested-dynamics).

### M03 — Separate a generator from its endpoint

- **Central question:** Why does knowing the final unitary not identify the Hamiltonian that produced it?
- **Understanding target:** Explain time ordering and the possibility that different driven Hamiltonians have the same endpoint. Recognize that a symmetric final unitary need not have followed a symmetric trajectory.
- **Dependencies and story role:** Uses M01–M02 to move from an instantaneous interaction description to an entire controlled evolution.
- **Conceptual connection:** The evolution operator is the observable result of integrating a generator; inversion of that map requires additional information.
- **Sources:** Anchor §§1.3.1, 2.5.2; [model: the phase signal and its assumption](../science/model.md#a-phase-signal-and-the-assumption-behind-it).

### M04 — Resolve the two parity sectors

- **Central question:** How does three-qubit parity divide the device into useful subspaces?
- **Understanding target:** Interpret $`\Pi=Z_1Z_2Z_3`$ and $`P_\pm=(I\pm\Pi)/2`$, identify the four basis states in each sector, and distinguish sector preservation from preservation of every basis state.
- **Dependencies and story role:** Adds a concrete symmetry to the dynamics of M03.
- **Conceptual connection:** Symmetry decomposes a control problem into blocks, but a block may still contain nontrivial unknown dynamics.
- **Sources:** Anchor §§4.3, 4.3.3; [model: observables](../science/model.md#observables).

### M05 — Distinguish worst-input and averaged leakage

- **Central question:** Which parity-transfer quantity is measured by simple basis preparations?
- **Understanding target:** Separate $`q^2=\Vert C\Vert ^2`$ from $`\ell=\mathrm{tr}(C^\dagger C)/4`$. Explain $`\ell\leq q^2\leq4\ell`$ and why uniformly preparing the four positive-parity basis inputs measures $`\ell`$.
- **Dependencies and story role:** Uses M04 to turn off-diagonal blocks into probabilities and to identify the accessible quantity needed later.
- **Conceptual connection:** The largest singular value describes an optimized input; a Frobenius norm describes a basis average without locating that input.
- **Sources:** Anchor §§1.2.2–1.2.3, 2.5.3; [phase–leakage model](../science/phase-leakage.md#model-and-observable-phase) and [audit access](../science/audit-protocol.md#device-and-access-contract).

### M06 — Read a relative determinant phase

- **Central question:** Why can determinants reveal a phase that survives arbitrary dynamics within each sector?
- **Understanding target:** Explain how a block determinant aggregates its eigenphases and how its derivative is tied to a trace. Show why equal sector dimensions cancel a common global phase in the determinant ratio.
- **Dependencies and story role:** Combines M03–M04 into the endpoint observable that motivates the audit.
- **Conceptual connection:** A scalar observable can retain a generator trace while discarding much of the detailed intrasector evolution.
- **Sources:** Anchor §§3.1.1–3.1.2, 4.3; [audit: endpoint datum](../science/audit-protocol.md#the-endpoint-datum).

### M07 — Keep phase winding visible

- **Central question:** Why is the observed phase a distance on a circle rather than an unrestricted accumulated angle?
- **Understanding target:** Interpret $`\vartheta\in[0,\pi/8]`$ as a shortest determinant-phase distance. Explain why $`e^{-i\theta\Pi}`$ has distance $`\theta`$ on the stated branch, while the obstruction vanishes at $`\theta=\pi/4`$.
- **Dependencies and story role:** Qualifies the observable from M06 before any bound uses its magnitude.
- **Conceptual connection:** A continuous phase lift is useful inside a proof; the experimentally identified endpoint remains periodic.
- **Sources:** Anchor §§3.1.1, 6.1.2; [model: observables](../science/model.md#observables) and [phase model](../science/phase-leakage.md#model-and-observable-phase).

### M08 — Understand two-local synthesis

- **Central question:** How can two-local controls create an endpoint associated with a three-body Pauli operator?
- **Understanding target:** Use a commutator or Pauli-product example to distinguish the locality of available generators from the Lie algebra they generate. Explain why endpoint reachability alone supplies no direct interaction witness.
- **Dependencies and story role:** Uses M02–M03 and prepares the concrete loophole in exact endpoint symmetry.
- **Conceptual connection:** Lie closure enlarges reachable dynamics; an additional trajectory condition is needed to recover the phase obstruction.
- **Sources:** Anchor §§3.1–3.2 and Appendix E; [construction: two-local Pauli algebra](../science/constructions.md#a-pauli-algebra-made-from-two-local-controls).

### M09 — Use a moving frame without granting a new control

- **Central question:** Can a three-body term appearing in a factorization be treated as an available physical Hamiltonian?
- **Understanding target:** Distinguish a calculation frame or Euler factor from the actual generator obtained by differentiating the full propagator. Identify the cancellation needed for a physically two-local path.
- **Dependencies and story role:** Extends M08 from reachability algebra to exact constructive calculations.
- **Conceptual connection:** A change of representation can expose an effective phase while the laboratory Hamiltonian remains in the allowed control span.
- **Sources:** Anchor §§1.3.2, 6.1.2; [construction: latitude path](../science/constructions.md#a-latitude-path-with-an-exact-endpoint).

### M10 — Turn strength into temporal regularity

- **Central question:** What can a norm bound say about dynamics between observed times?
- **Understanding target:** Explain $`\Vert U(t)-U(s)\Vert \leq J|t-s|`$ and the resulting Lipschitz bounds for $`q`$ and $`\sqrt\ell`$. Recognize $`L=JT`$ as a dimensionless action budget.
- **Dependencies and story role:** Combines M02–M05 into the regularity tool needed for hidden-trajectory reasoning.
- **Conceptual connection:** Bounded strength limits how quickly leakage can rise, even when pulse switching and bandwidth are unrestricted.
- **Sources:** Anchor §§7.1, 7.4.1; [temporal-mean proof](../science/phase-leakage.md#a-true-temporal-mean-without-a-ceiling) and [grid guarantee](../science/constructions.md#what-a-deterministic-observation-grid-guarantees).

### M11 — Specify an observation rather than an intervention

- **Central question:** What data result from stopping independent fresh runs at selected times?
- **Understanding target:** Distinguish repeated prefix experiments from measurements inserted into one trajectory. Relate a parity-change probability to ordinary binary-shot statistics and explain why repeatability and private stopping choices matter.
- **Dependencies and story role:** Adds the operational observation model to M05 and M10.
- **Conceptual connection:** Sampling a trajectory is an access capability, and statistical confidence concerns repeated observations of that capability. The needed concentration bounds are supplied locally.
- **Sources:** Anchor §§1.2.2–1.2.3, 2.5.3; [audit contract](../science/audit-protocol.md#device-and-access-contract) and [finite audit decision](../science/audit-protocol.md#finite-timing-and-the-audit-decision).

### M12 — Assemble the inference problem

- **Central question:** Which additional observations could turn a phase signal into a justified interaction certificate?
- **Understanding target:** Connect the closed device, two-local null model, circular endpoint phase, repeatable prefixes, strength bound, and retained leakage bit. Distinguish this audit from unrestricted Hamiltonian reconstruction.
- **Dependencies and story role:** Integrates M01–M11 into the complete framework needed for the narrative phase.
- **Conceptual connection:** Observability and indistinguishability depend on both dynamics and allowed outputs; a theorem about one output class need not govern a richer experiment.
- **Sources:** Anchor §§5.2, 5.2.1; [certificate and observation class](../science/model.md#certificate-and-observation-class) and [physical inference](../science/model.md#what-is-inferred-physically).

## Narrative and innovation

### M13 — Recover the exact-symmetry invariant

- **Central question:** What does exact parity preservation forbid for two-local generators?
- **Understanding target:** Explain why $`\mathrm{tr}(\Pi H)=0`$ for every two-local Hamiltonian and why this fixes the relative determinant phase along an exactly symmetric path. Allow arbitrary symmetric two-local nuisance dynamics.
- **Dependencies and story role:** Begins the narrative from M04 and M06 with the inherited invariant whose assumption will be audited.
- **Conceptual connection:** Local Pauli support becomes a trace constraint, and symmetry transports that constraint directly to an endpoint phase.
- **Sources:** Anchor §§3.1, 4.3; [phase–leakage identity, Lemma 1](../science/phase-leakage.md#the-phase-leakage-identity) and [endpoint datum](../science/audit-protocol.md#the-endpoint-datum).

### M14 — Locate the phase accumulated by an excursion

- **Central question:** Which term changes the determinant phase when the path temporarily mixes parity sectors?
- **Understanding target:** Track the off-block correction in the determinant derivative, the inverse-block bound when $`q<1`$, and the Frobenius estimate involving $`\sqrt\ell`$. Explain why intermediate singularity cannot simply be ignored.
- **Dependencies and story role:** Uses M05–M07 and M13 to replace exact conservation by a quantitative identity.
- **Conceptual connection:** A phase obstruction becomes a speed bound once its only uncancelled derivative term is tied to measurable transfer.
- **Sources:** Anchor §§2.5.2, 3.1; [phase–leakage identity, Lemma 1](../science/phase-leakage.md#the-phase-leakage-identity).

### M15 — Read the uniform-leakage speed bound

- **Central question:** How slowly must a forbidden phase be synthesized when every instantaneous excursion is small?
- **Understanding target:** Interpret the lower bound $`T\geq\theta\sqrt{1-\epsilon}/(J\sqrt\epsilon)`$ under a worst-input ceiling. Distinguish it from a uniform basis-averaged ceiling and from a true temporal mean.
- **Dependencies and story role:** Integrates the identity from M14 over a nonsingular path.
- **Conceptual connection:** Reducing excursion probability suppresses the rate of a phase generated indirectly by allowed controls; this does not restrict a native three-body generator in the same way.
- **Sources:** Anchor §§7.1.2, 7.4.1; [uniform bounds, Theorem 2](../science/phase-leakage.md#uniform-leakage-bounds).

### M16 — Handle a large or singular excursion

- **Central question:** What remains provable when no small-leakage ceiling is assumed?
- **Understanding target:** Use the strength-limited rise and fall of $`q`$ to explain the minimum area of a triangular excursion. Separate this argument from determinant differentiation, which may fail at singular intermediate blocks.
- **Dependencies and story role:** Uses M10 and M14 to cover the paths omitted by the uniform-ceiling argument.
- **Conceptual connection:** A large excursion may obstruct one analytic coordinate, yet its finite duration already makes it statistically visible.
- **Sources:** Anchor §§7.1, 7.4.1; [temporal-mean proof, Theorem 3](../science/phase-leakage.md#a-true-temporal-mean-without-a-ceiling).

### M17 — Obtain a universal average-leakage floor

- **Central question:** How do the small- and large-excursion routes combine into a bound on an ordinary time average?
- **Understanding target:** Explain why every two-local implementation of a parity-preserving endpoint obeys $`\bar\ell\geq\theta^2/(8L^2)`$. Identify the $`1/32`$ extension for invertible endpoint blocks without exact endpoint parity return.
- **Dependencies and story role:** Joins M14–M16 into the universal lower bound required by sampling.
- **Conceptual connection:** A case split removes an unobserved trajectory ceiling and leaves a directly observable mean probability.
- **Sources:** Anchor §§2.5.3, 7.4.1; [Theorem 3](../science/phase-leakage.md#a-true-temporal-mean-without-a-ceiling) and [general-endpoint proposition](../science/audit-protocol.md#a-leakage-lower-bound-without-exact-endpoint-return).

### M18 — Fix the asymptotic question before sharpening it

- **Central question:** What does the leading coefficient one actually claim?
- **Understanding target:** Follow the shrinking-threshold converse showing $`\liminf L^2\bar\ell\geq\theta^2`$ at fixed positive $`\theta`$. Explain why it supplies neither a uniform small-$`\theta`$ theorem nor attainment for every endpoint with that phase.
- **Dependencies and story role:** Refines M17 while keeping the limit order and target family explicit.
- **Conceptual connection:** A sharp asymptotic result combines a universal converse with a separately specified attaining family.
- **Sources:** Anchor §§7.1.2, 7.4.1; [sharp mean law, Theorem 4](../science/phase-leakage.md#a-true-temporal-mean-without-a-ceiling).

### M19 — Build the effective two-level algebra

- **Central question:** Why do $`X_1Z_2`$ and $`Y_1Z_3`$ suffice for an exact three-qubit construction?
- **Understanding target:** Verify their Pauli relations with $`\Pi`$, understand the multiplicity-four two-level representation, and explain why the actual Hamiltonian remains two-local.
- **Dependencies and story role:** Uses M08–M09 to construct the family needed to complement M18.
- **Conceptual connection:** A small control algebra can act identically across several sectors without turning its calculated third generator into a free physical control.
- **Sources:** Anchor §§3.1.2, 6.1; [two-local Pauli algebra](../science/constructions.md#a-pauli-algebra-made-from-two-local-controls).

### M20 — Close a latitude path exactly

- **Central question:** How can a path accumulate a phase while holding leakage fixed and return with no endpoint transfer?
- **Understanding target:** Connect the initial ramp, fixed-latitude dwell, and final ramp to an exact endpoint $`e^{-i\theta\Pi}`$. Track the cancellation of the forbidden diagonal generator and the complete norm bound.
- **Dependencies and story role:** Turns the algebra of M19 into an explicit attaining evolution.
- **Conceptual connection:** The phase is earned by controlled motion through other sectors; a factorized three-body phase is a description of that motion, not an available interaction.
- **Sources:** Anchor §§1.3.2, 6.1.2, 6.1.4; [latitude construction, Proposition 1](../science/constructions.md#a-latitude-path-with-an-exact-endpoint).

### M21 — Match the mean law and count bandwidth

- **Central question:** Which resource is optimized by the latitude construction, and which remains unrestricted?
- **Understanding target:** Relate the small solution of $`L=\theta\cot\alpha_0+2\alpha_0`$ to $`\bar\ell=\theta^2/L^2+O_\theta(L^{-4})`$. Keep the diverging dwell frequency visible and restrict attainment to the stated witness targets.
- **Dependencies and story role:** Joins the converse of M18 to the construction of M20.
- **Conceptual connection:** Matching strength–duration performance is compatible with a growing bandwidth requirement; optimality under one resource contract does not imply optimality under another.
- **Sources:** Anchor §§7.1.2, 7.4.1; [mean attainment](../science/constructions.md#uniform-ceilings-and-a-true-temporal-mean) and [latitude bandwidth](../science/constructions.md#a-latitude-path-with-an-exact-endpoint).

### M22 — Bound what can happen between scheduled checks

- **Central question:** How much false phase can fit between deterministic observations of small leakage?
- **Understanding target:** Build the triangular leakage envelope within each time cell and understand the role of $`\sum_jh_j^2`$. Distinguish a bound on worst-input amplitude from a bound on averaged probability.
- **Dependencies and story role:** Applies M10 and M15 to an observation schedule rather than an assumed continuous ceiling.
- **Conceptual connection:** Temporal resolution converts finite samples into a continuous-path bound only through a trusted strength constraint.
- **Sources:** Anchor §§2.5.3, 7.4.1; [deterministic-grid guarantee](../science/constructions.md#what-a-deterministic-observation-grid-guarantees).

### M23 — Expose an exactly sampled spoof

- **Central question:** Can every scheduled check show exact symmetry while the total phase is nonzero?
- **Understanding target:** Explain the driven SU(2) cycle that returns to parity at each grid point and accumulates a tunable phase of order $`J^2Th`$. Respect circular phase winding and the small-cell regime of the matched resolution law.
- **Dependencies and story role:** Uses M19–M22 to show why the grid bound represents a real loophole.
- **Conceptual connection:** Perfect sampled symmetry is a statement about selected endpoints, not about the Hamiltonian between them.
- **Sources:** Anchor §§1.3.2, 6.1.4; [exact sampled spoof, Proposition 2](../science/constructions.md#exact-spoofing-between-perfect-samples) and [matched resolution](../science/constructions.md#matched-grid-resolution-order).

### M24 — Sample the mean instead of certifying every instant

- **Central question:** Why do random fresh-run parity tests detect an excursion that a known schedule can miss?
- **Understanding target:** Connect a uniform time and a uniform positive-parity basis input to the event probability $`\bar\ell`$. Explain why the waveform must be repeatable and independent of the privately chosen stopping time.
- **Dependencies and story role:** Joins the accessible probability of M05, observation model of M11, and universal mean floor of M17.
- **Conceptual connection:** Random observation design converts a trajectory-wide lower bound into an ordinary binary event without reconstructing the path.
- **Sources:** Anchor §§1.2.3, 2.5.3, 5.2.1; [audit contract](../science/audit-protocol.md#device-and-access-contract) and [finite audit decision](../science/audit-protocol.md#finite-timing-and-the-audit-decision). Sampling probabilities and confidence bounds are derived locally.

### M25 — Establish the endpoint phase with finite precision

- **Central question:** How can a phase confidence bound replace an exactly supplied endpoint matrix?
- **Understanding target:** Follow the route from ordinary six-qubit Choi tomography to a matrix radius, block conditioning, and a lower phase bound $`\theta_0`$. Explain why unresolved blocks return inconclusive and why the unitary device model is still an assumption.
- **Dependencies and story role:** Uses M06–M07 and M11 to supply the independent endpoint datum required by M24.
- **Conceptual connection:** Matrix perturbation control turns finite measurement uncertainty into a circular-phase uncertainty; it does not certify an arbitrary channel is unitary.
- **Sources:** Anchor §§1.1.4, 5.1; [finite endpoint measurements](../science/audit-protocol.md#finite-endpoint-measurements) and [endpoint resource cost](../science/resources.md#endpoint-phase-cost). The confidence and perturbation bounds are proved in the project.

### M26 — Declare a resolution floor before seeing data

- **Central question:** Why is a merely positive estimated phase insufficient for a uniform resource guarantee?
- **Understanding target:** Explain the predeclared $`g\in(0,\pi/32]`$, the rule to return inconclusive when $`\theta_0<g`$, and the resulting unconditional shot and timing-bin caps. Identify the completeness promise $`\theta\geq4g`$ with resolved endpoint conditioning.
- **Dependencies and story role:** Combines M25 with the sampling cost in M24 to make the protocol's budget valid on every data record.
- **Conceptual connection:** A statistical confidence event controls correctness; a declared resolution floor independently controls resource use, including rare bad estimates.
- **Sources:** Anchor §§2.5.3, 7.1.2; [finite endpoint measurements](../science/audit-protocol.md#finite-endpoint-measurements), [hard audit caps](../science/audit-protocol.md#finite-timing-and-the-audit-decision), and [resources](../science/resources.md#leakage-audit-cost-and-physical-time). This floor argument is locally supplied.

### M27 — Make random stopping finitely addressable

- **Central question:** What timing resolution preserves the random audit's signal?
- **Understanding target:** Use the root-mean-square Lipschitz estimate to compare continuous uniform time with uniformly sampled bin midpoints. Explain $`K=O(1+L^2/g)`$, logarithmic index storage, and the modification for a trusted bounded stopping error.
- **Dependencies and story role:** Uses M10, M24, and M26 to remove an implicit exact-real-time input from the procedure.
- **Conceptual connection:** Rounding a stopping time perturbs an amplitude before it perturbs the averaged event probability; this preserves the audit order with a controlled mesh.
- **Sources:** Anchor §§2.5.2–2.5.3, 7.1.2; [finite timing proof](../science/audit-protocol.md#finite-timing-and-the-audit-decision) and [timing resources](../science/resources.md#leakage-audit-cost-and-physical-time).

### M28 — Combine confidence and complete resource costs

- **Central question:** What exactly does an all-no-transition record certify, with what risk and cost?
- **Understanding target:** Combine independent endpoint and audit failure budgets, distinguish one-sided certification from identifying the Hamiltonian, and charge endpoint calls plus every audit prefix. Explain expected prefix duration $`T/2`$ and the unconditional bounds using $`N_{\max}`$.
- **Dependencies and story role:** Integrates M24–M27 into the complete finite-confidence upper-bound procedure.
- **Conceptual connection:** Statistical confidence, hard run caps, physical duration, timing, and trusted known operations are separate parts of one operational claim.
- **Sources:** Anchor §§1.2.3, 2.5.3, 7.1.2; [finite audit decision](../science/audit-protocol.md#finite-timing-and-the-audit-decision) and [resource accounting](../science/resources.md#leakage-audit-cost-and-physical-time). The union bound and shot law are locally proved.

### M29 — Match the shot law in its actual observation class

- **Central question:** Why can adaptive choices of parity-only stopping tests not remove the inverse-square shot cost?
- **Understanding target:** Compare honest and two-local paths with the same endpoint, bound the probability of their common all-no-event transcript, and recover $`\Omega((L/\theta)^2\log(1/\delta))`$. Keep the fixed-$`\theta`$, $`g\asymp\theta`$ regime and the leakage-only access restriction explicit.
- **Dependencies and story role:** Combines the hard path of M20–M21 with the inference and budget of M26–M28.
- **Conceptual connection:** Identical endpoint observations and uniformly rare intermediate events establish a statistical lower bound without claiming that all quantum verification strategies are equally limited.
- **Sources:** Anchor §§5.2, 5.2.1; [matching leakage-only lower bound](../science/audit-protocol.md#matching-lower-bound-for-leakage-only-ordinary-shots) and [meaning of the lower bound](../science/resources.md#what-the-matching-lower-bound-means). The transcript argument is proved locally.

### M30 — State the complete scientific conclusion

- **Central question:** Which inference survives after every model, limit, observation, and cost is kept explicit?
- **Understanding target:** Explain how a resolved phase and a bounded leakage audit exclude all stated two-local explanations. Separate the inherited exact invariant from the new quantitative audit frontier, and retain the closed-device, repeatability, strength, bandwidth, timing, and trusted-readout qualifications.
- **Dependencies and story role:** Integrates M13–M29 into the project's full local-to-global narrative.
- **Conceptual connection:** A useful certificate is stronger than an endpoint symmetry check and narrower than microscopic identification. Hidden mediators, unknown SPAM, open dynamics, richer coherent observations, and different limit orders require different claims.
- **Sources:** Anchor §§5.2.1, 7.1.2; [physical inference](../science/model.md#what-is-inferred-physically), [scope and attribution](../science/phase-leakage.md#scope-and-attribution), and [resource boundaries](../science/resources.md#deterministic-inspections-and-experimental-noise).
