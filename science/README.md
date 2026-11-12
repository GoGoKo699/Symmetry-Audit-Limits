# Scientific route

The story is an inference problem. A relative parity-sector phase rules out a symmetric two-local generator, but symmetry of the final operation does not establish symmetry of its trajectory. Small hidden excursions can accumulate the phase. A repeatable prefix audit measures the excursions, and its cost is constrained by the same control geometry.

| Read in this order | What it establishes |
| --- | --- |
| [Model and task](model.md) | The closed three-qubit device, known strength, observable phase, allowed tests and meaning of a certificate. |
| [Phase and leakage](phase-leakage.md) | Principal-block determinant identity, uniform ceilings, a universal temporal-mean bound and sharp fixed-phase asymptotic. |
| [Exact controls and sampled paths](constructions.md) | An attaining latitude path, its bandwidth cost, and exact symmetry restoration between observation times. |
| [Finite-confidence protocol](audit-protocol.md) | Finite endpoint data, a finite stopping mesh, confidence allocation and matching ordinary-shot lower bound. |
| [Resources and interpretation](resources.md) | Every unknown prefix, endpoint reference, trusted operation, timing bit and boundary of the observation model. |

The mean-leakage lower bound applies to arbitrary intrasector nuisance dynamics. The exact upper construction uses the particular endpoint $`e^{-i\theta ZZZ}`$. These quantifiers differ. The sharp coefficient holds at fixed positive phase as $`JT`$ grows; the finite confidence test uses nonasymptotic bounds.

The [related-work account](../references/related-work.md) credits the exact symmetry/locality obstruction and holonomic mechanisms. The [finite checks](../verification/README.md) verify selected matrix and numerical consequences, while the universal arguments remain in the pages above.
