# Related work and attribution

This project tests two-local explanations of a closed, repeatable three-qubit evolution with an independently justified operator-norm bound. Its primary sharp family has a parity-preserving endpoint with a nonzero relative parity-sector determinant phase. The finite-confidence audit also permits invertible endpoint parity blocks without exact parity return. The question is how much intermediate parity transfer is unavoidable, and how many fresh-run parity measurements are needed to detect it. A constraint on the whole trajectory is different from endpoint symmetry or a bound on the symmetry-breaking part of the instantaneous Hamiltonian.

The determinant invariant, the use of symmetry to diagnose interaction order, geometric phase generation, and low-population cyclic controls are established ingredients. The contribution claimed here is the stated mean-transfer frontier and its matched statistical consequence within the specified parity-only observation model. No general priority claim for symmetry-based speed limits or holonomic synthesis is intended.

## Exact symmetry and locality

### Marvian: determinant constraints

[Marvian, *Nature Physics* **18**, 283–289 (2022)](https://doi.org/10.1038/s41567-021-01464-0), in the inspected [arXiv:2003.05524v3](https://arxiv.org/abs/2003.05524v3), establishes additional restrictions from symmetry and locality. Supplementary Note 4, Eqs. (D3)–(D6), expresses sector determinants through the time integrals of sector traces. The general-group formulation supplies the invariant used here. For three qubits, every two-local Hamiltonian has zero trace against `Z1 Z2 Z3`; exact parity preservation throughout the evolution therefore fixes the relative sector determinant.

The [Abelian-symmetry theory, *Physical Review Research* **6**, 043292 (2024)](https://doi.org/10.1103/PhysRevResearch.6.043292), inspected as [arXiv:2302.12466v3](https://arxiv.org/abs/2302.12466v3), explicitly includes bit-parity symmetry. Section IV D treats even cyclic groups; Section V and Corollary 6 describe determinant-one control within parity sectors. Thus neither the exact parity obstruction nor independent special-unitary control inside its sectors is new here. The present model allows symmetry-breaking intermediate dynamics and constrains the resulting observable transfer instead.

### Zhukas and collaborators: interaction spectroscopy

[Zhukas, Wang, Katz, Monroe, and Marvian, arXiv:2408.10475v1 (2024)](https://arxiv.org/abs/2408.10475v1), Eqs. (2)–(4), define and measure an efficient three-body phase under instantaneous Hamiltonian U(1) symmetry. At three qubits their phase agrees, up to orientation convention, with the parity-sector determinant phase. Their Methods also develop alternative sector-phase measurements and an experimental error analysis.

This is a direct precedent for the observable and its physical motivation. The present audit addresses the extra question of certifying the trajectory assumption from finitely many repeatable prefix experiments. It does not correct or invalidate that experiment: a deliberately compiled many-body unitary is different from a claim that every pulse in its compilation has the corresponding many-body interaction or exact symmetry.

## Geometric phases and control speed

### Isoholonomic inequalities

[Sönnerborn, *Physical Review A* **109**, 062433 (2024)](https://doi.org/10.1103/PhysRevA.109.062433), inspected as [arXiv:2404.05844v2](https://arxiv.org/abs/2404.05844v2), gives a lower bound on the length of a cyclic subspace path in terms of its gate holonomy, followed by an execution-time bound from its speed. Equations (1)–(5) and Section VI include tightness. The spectral expression is the sum of the eigenphase factors `|theta_j|(2 pi - |theta_j|)` under a square root.

[Sönnerborn, *Physical Review A* **111**, 052430 (2025)](https://doi.org/10.1103/PhysRevA.111.052430), inspected as [arXiv:2412.12013v2](https://arxiv.org/abs/2412.12013v2), gives explicit tight implementations when sufficient codimension is available; Eqs. (7)–(12) state the bound and its speed consequence. Related pure-state bounds appear in [Hörnedal and Sönnerborn, *Physica Scripta* **98**, 105108 (2023)](https://doi.org/10.1088/1402-4896/acf8a2). The later [arXiv:2506.10215v4](https://arxiv.org/abs/2506.10215v4) extends the isoholonomic framework to cyclic isospectral and isodegenerate mixed states.

These results are a substantive antecedent, not merely a keyword neighbor. After removing parity-diagonal evolution, the inverse interaction-picture propagator restricted to one initial sector gives a horizontal frame. A leakage-free time cell is consequently a holonomy loop. The quadratic small-cell phase and the resulting temporal-grid aliasing order can therefore be understood through established isoholonomic geometry. This project does not claim that order as a new geometric principle. The quantity optimized in the principal result is instead transfer from a fixed initial parity sector, averaged over physical stopping time, with a matched observation cost.

### Symmetry-based speed limits

[Wiedmann and Burgarth, *Journal of Physics A* **59**, 065301 (2026)](https://doi.org/10.1088/1751-8121/ae3f68), was inspected through the available [arXiv:2506.10069v1](https://arxiv.org/abs/2506.10069v1), particularly Eq. (7), Lemma 1, and Theorem 8. Their argument bounds target time by distance to an unreachable set divided by the size of a Hamiltonian perturbation restoring a control symmetry; quadratic symmetries provide computable bounds. Publication metadata were checked separately; equality of every preprint and journal equation was not checked.

The present hypothesis permits an instantaneous off-diagonal Hamiltonian as large as the full strength budget. Small propagator leakage does not imply a small instantaneous symmetry-breaking perturbation. Moreover, the target itself commutes with parity, so a direct endpoint commutator with parity is zero. Their results establish the general connection between symmetry and speed, but the stated theorem does not directly give the mean-transfer or parity-audit frontier used here.

## Low-population implementations

[Liu, Yan, Zhang, Yung, Su, and Shan, *Physical Review Research* **5**, 013059 (2023)](https://doi.org/10.1103/PhysRevResearch.5.013059), Section IV and Eqs. (7)–(9), studies the integrated intermediate-state population in reverse-engineered holonomic controls. Small excursions and repeated cyclic evolution reduce occupation while accumulating a gate phase. The published article, whose author list differs from the earlier arXiv preprint, is the source cited here.

This establishes the physical mechanism behind using many small excursions. It does not supply an arbitrary-two-local-control converse or the minimax cost of a parity-only statistical test. The construction here embeds an SU(2) control algebra in two-body Pauli interactions and accounts for its full operator norm. Arbitrary waveform bandwidth remains an explicit assumption; no bounded-bandwidth optimum is claimed.

## A neighboring quantum-workspace result

The public [Quantum Borrowed Ancilla Cost account](https://github.com/GoGoKo699/Quantum-Borrowed-Ancilla-Cost/tree/2b1e332c2fb7b394a31ed5808faa121535038a5e) studies CCZ under exactly excitation-conserving one- and two-qubit gates, with arbitrary borrowed qubits returned jointly with the data. Its [deterministic proof](https://github.com/GoGoKo699/Quantum-Borrowed-Ancilla-Cost/blob/2b1e332c2fb7b394a31ed5808faa121535038a5e/science/deterministic_bound.md) derives a sharp accuracy-versus-width law from a charge-sector determinant character. Circuit time is unrestricted there. It is a scientific neighbor sharing the determinant machinery, rather than the same optimization: here the system has no unobserved helper and transient symmetry breaking is allowed and measured.

## What the comparison supports

The inspected sources already justify the exact obstruction, the many-body-phase observable, the geometric route to hidden excursions, and the possibility of low-occupation implementations. Those ingredients are credited rather than counted as separate discoveries. The additional account here connects a universal mean-transfer lower bound, an attaining asymptotic construction, and a matching number of ordinary fresh-run parity shots. The shot lower bound is confined to parity-definite preparation and parity-only intermediate measurement; it is not an impossibility theorem for coherent process identification or phase-sensitive probes.

The closed-system assumption, trusted norm bound, repeatable waveform, stopping-time access, preparation/readout model, endpoint verification and confidence allocation are load-bearing. Hidden mediators and additional noise define other models. The comparison is based on the named primary statements and proof passages, checked on 12 November 2026; it is not an exhaustive priority certificate. Bibliographic records are in [references.bib](references.bib).
