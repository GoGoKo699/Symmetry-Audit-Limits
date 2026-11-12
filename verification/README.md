# Verification

The analytical claims are proved in [phase-leakage.md](../science/phase-leakage.md), [constructions.md](../science/constructions.md), and [audit-protocol.md](../science/audit-protocol.md). The accompanying numerical suite checks specified finite examples and implementation-sensitive constants. It does not establish universal correctness, literature priority, or an experimental result.

From the repository root, with Python 3.10 or later:

```bash
python -m pip install -r verification/requirements.txt
python verification/run_checks.py --output verification/results.json
```

The script prints JSON, returns a nonzero exit status on a failed check, and writes a report only when `--output` is supplied. Seeds and parameters are fixed; the report contains no timestamp or timing benchmark. Numerical versions are retained because last-bit floating-point results can vary across supported environments. [results.json](results.json) records the actual included run.

The checks have the following scope:

| Check | What is compared |
| --- | --- |
| Three-qubit control algebra | Full $`8\times8`$ Pauli identities, the 36 nonidentity one- and two-local basis elements, and their vanishing trace against parity. |
| Exact latitude controls | Hamiltonians reconstructed by differentiating the Euler propagator, their complete Pauli support, norm, forbidden coefficient, endpoint unitary, and maximum leakage. One complete path is also integrated independently as a Schrödinger ODE. |
| Temporal mean | Leakage integrated from the matrix propagator versus the closed expression, followed by fixed-phase large-action examples approaching the leading coefficient one. This is a finite check of the formula and limiting trend. |
| Grid spoof | Exact rotating-drive propagators, intermediate leakage, return at the cell endpoint, and the circular determinant phase after multiple windings. |
| Phase derivative | Fixed-seed, time-dependent two-local examples: the derivative obtained from principal blocks, the simplified trace identity, a central finite difference, and both operator-norm and Frobenius leakage bounds. These examples do not sample all allowed controls. |
| Endpoint inference | Complete six-qubit Choi Pauli reconstruction, deterministic expectation perturbations within a known radius, the top-eigenvector matrix radius, the resulting phase lower bound, and the inconclusive response for singular blocks. No tomography shots are simulated. |
| Finite-confidence budgets | An explicit numerical endpoint/audit example checks the Hoeffding allocation, stopping-bin correction, exponential no-event guarantee, predeclared resolution-floor caps and inconclusive weak-signal branch. The potentially large shot budgets are calculated directly; the suite does not execute or simulate those shots. |

The deterministic perturbations in the endpoint check are test inputs, not statistically observed errors. Statistical coverage comes from the analytical tail bounds in the protocol. The example keeps the deliberately unoptimized 4095-setting endpoint cost visible rather than hiding it behind the fixed-dimension asymptotic notation.

All comparisons use ordinary double-precision linear algebra with explicit tolerances. This suite is not interval arithmetic and does not itself provide certified numerical margins for laboratory data. A real endpoint certificate must include its numerical matrix and phase errors in the confidence radius, as the protocol requires.

## Hosted mathematics

The read-only `Hosted mathematics` pull-request workflow checks out the exact proposed commit, visits every tracked Markdown page on GitHub at widths 1440 and 760, and compares its rendered MathML with the source expressions. It retains actual HTML, screenshots and a source-bound report as a temporary Actions artifact. A person must still inspect the screenshots and compare the prose, tables and navigation with the source.

The generic collectors in `hosted_math/` use Playwright 1.56.1 and MathJax 3.2.1. They do not authenticate, change GitHub settings, or establish the scientific claims. Run the collector locally with `--root`, `--repository`, `--revision` (a full commit SHA) and `--output` (a new evidence directory); use `probe_hosted_math.cjs` with exactly one `--page` for an early diagnostic. The artifact is a reproducible check, not permanent preservation.
