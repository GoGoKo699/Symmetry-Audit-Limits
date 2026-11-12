# Learn the symmetry audit

A three-qubit device can finish with exactly the phase expected from a three-body interaction even when every Hamiltonian term used to drive it acts on at most two qubits. The missing evidence is what happened between the start and the endpoint. This project determines how much parity transfer such an explanation must produce, and how many ordinary measurements can reveal it.

The single educational anchor is **Domenico D’Alessandro, *Introduction to Quantum Control and Dynamics*, second edition**, DOI [10.1201/9781003051268](https://doi.org/10.1201/9781003051268). The publisher catalog dates this edition to 2021; its frontmatter states publication and copyright 2022. These identify the same second edition, with hardcover ISBN 9780367507909.

Start with the [D’Alessandro bridge](DALLESSANDRO_BRIDGE.md). It gives a targeted source route, translates the control notation, and works through one complete three-qubit example from its endpoint phase to a finite-confidence audit and its costs. The book supplies the control foundation. The symmetry-phase identities, leakage frontier, statistical audit and resource bounds are developed or attributed in the project’s scientific account.

## One connected route

| Step | What becomes clear | Read |
| --- | --- | --- |
| Describe the device | A Hamiltonian controls a propagator; the chosen input and measurement determine its observed output. | [Bridge: source route](DALLESSANDRO_BRIDGE.md#targeted-reading-route), then [model](../science/model.md) |
| Separate a sector from a subsystem | Parity gives two four-dimensional subspaces of the same three-qubit system. | [Bridge: notation](DALLESSANDRO_BRIDGE.md#notation-and-assumptions) |
| Follow the missing motion | Endpoint symmetry leaves room for intermediate parity transfer. | [Phase and leakage](../science/phase-leakage.md), then [exact constructions](../science/constructions.md) |
| Turn motion into evidence | Random stopping converts the temporal mean into a directly sampled probability. | [Finite-confidence audit](../science/audit-protocol.md) |
| Price the conclusion | Endpoint resolution, a fixed phase floor, timing precision and repeated prefixes all consume resources. | [Resources and boundaries](../science/resources.md) |
| Assemble the whole argument | Thirty understanding targets connect the background to the result and its limits. | [M01–M30](MILESTONES.md) |

The milestone map is common scientific material, with twelve background milestones followed by eighteen narrative milestones. Its dependency order carries the reader from states, measurements and controls to the phase-leakage theorem, the matching construction and the restricted audit optimum. Each milestone points to the source foundation and the authoritative project statements.

For a direct proof route, use the [scientific overview](../science/README.md). For attribution, see [related work](../references/related-work.md); for reproducible finite checks, see [verification](../verification/README.md). Those checks support the formulas and examples at their stated scope. The all-controls conclusions rely on the written proofs.
