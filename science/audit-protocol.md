# A finite-confidence audit of a forbidden parity phase

The audit combines an endpoint phase measurement with independent tests of parity leakage at random stopping times. Its conclusion is narrow and operational: under the stated closed-system and strength assumptions, the observed evolution has no explanation by a Hamiltonian containing only one- and two-qubit terms. The audit does not reconstruct the Hamiltonian or identify a particular microscopic three-body coupling.

All norms without a subscript are operator norms, and units have $`\hbar=1`$.

## Device and access contract

The device consists of exactly three evolving qubits. In each fresh run it implements the same unknown absolutely continuous propagator

```math
\dot U(t)=-iH(t)U(t),\qquad U(0)=I,\qquad 0\leq t\leq T.
```

The Hamiltonian can depend arbitrarily on time, but a trusted bound $`\|H(t)\|\leq J`$ holds almost everywhere. A purely scalar Hamiltonian can be removed by a common phase convention; none of the measured quantities depends on that convention. The alternative to be excluded allows every such time-dependent Hamiltonian whose Pauli expansion has support on at most two qubits. It includes arbitrary single-qubit fields, all pairs, and arbitrary driving frequency. There is no bandwidth assumption.

Preparation, parity measurement, reference isolation during endpoint tomography, and the advertised timing accuracy are trusted. Each run starts afresh; an unmodelled environment or controller that retains quantum information between runs is outside this three-qubit unitary model. The stopping time is selected privately after the repeatable waveform has been fixed. The device cannot change that waveform in response to the chosen stopping time. Preparing an input or stopping one run does not alter subsequent runs.

Let

```math
\Pi=Z_1Z_2Z_3,\qquad P_\pm=\frac{I\pm\Pi}{2},\qquad a=JT.
```

Both parity sectors have dimension four. Write the blocks of $`U(t)`$ as

```math
U(t)=\begin{pmatrix} A(t)&B(t)\\C(t)&D(t)\end{pmatrix},
\qquad C(t)=P_-U(t)P_+.
```

Define the worst-input leakage amplitude and the uniformly averaged leakage probability by

```math
q(t)=\|C(t)\|,\qquad
\ell(t)=\frac{1}{4}\mathrm{Tr}[C(t)^\dagger C(t)],\qquad
\bar\ell=\frac{1}{T}\int_0^T\ell(t)\,dt.
```

The trace is over the positive-parity input sector. In one audit shot, prepare one of $`|000\rangle,|011\rangle,|101\rangle,|110\rangle`$ uniformly, evolve to the selected stopping time, and measure parity. The probability of a negative-parity result at time $`t`$ is exactly $`\ell(t)`$. No operator-norm tomography is required for this leakage test.

## The endpoint datum

When $`A(T)`$ and $`D(T)`$ are invertible, define

```math
\vartheta(U)=\frac{1}{8}\mathrm{dist}\!\left(
\arg\det A(T)-\arg\det D(T),\,2\pi\mathbb Z\right)
\in[0,\pi/8].
```

Here $`\mathrm{dist}`$ denotes the shortest angular distance. Multiplying $`U`$ by a global phase multiplies both determinants by the same fourth power, so $`\vartheta`$ is experimentally meaningful. The definition does not require an exact parity-preserving endpoint.

A parity-preserving endpoint may have arbitrary intrasector unitaries. In particular, if

```math
H(t)=H_{2,\mathrm{sym}}(t)+g(t)\Pi,
\qquad [H_{2,\mathrm{sym}}(t),\Pi]=0,
```

where $`H_{2,\mathrm{sym}}`$ is any one- and two-qubit Hamiltonian, then

```math
\arg\det A(T)-\arg\det D(T)
=-8\int_0^Tg(t)\,dt\pmod{2\pi}.
```

Thus unknown symmetric nuisance dynamics need not be reconstructed. This exact determinant-phase identity is inherited from the [symmetry-and-locality framework](https://doi.org/10.1038/s41567-021-01464-0) and the [symmetry-protected interaction witness](https://arxiv.org/html/2408.10475v1); the issue addressed here is how to audit the symmetry assumption with finite data.

## A leakage lower bound without exact endpoint return

**Proposition.** Suppose $`H(t)`$ is at most two-local, $`\|H(t)\|\leq J`$, and the endpoint blocks are invertible. Set $`\theta=\vartheta(U)>0`$. Then

```math
\boxed{\quad \bar\ell\geq\frac{\theta^2}{32(JT)^2}.\quad}
```

The constant is a convenient uniform bound, not the sharp finite-action constant. If the endpoint preserves parity exactly, the same argument improves $`32`$ to $`8`$. In either case the sharp fixed-$`\theta`$, large-$`JT`$ leading coefficient is one.

**Proof.** At every time where $`q<1`$, unitarity gives

```math
\sigma_{\min}(A),\sigma_{\min}(D)\geq\sqrt{1-q^2},
\qquad \|B\|_{\mathrm F}=\|C\|_{\mathrm F}.
```

Consequently the continuously unwrapped phase

```math
\Phi(t)=\arg\det A(t)-\arg\det D(t),\qquad \Phi(0)=0,
```

is well defined on any interval with $`q<1`$. Differentiating the two determinants yields

```math
\dot\Phi=-\mathrm{Tr}H_{++}+\mathrm{Tr}H_{--}
-\mathrm{Re}\mathrm{Tr}(A^{-1}H_{+-}C)
+\mathrm{Re}\mathrm{Tr}(D^{-1}H_{-+}B).
```

For a two-local Hamiltonian, $`\mathrm{Tr}(\Pi H)=0`$, so the first two terms cancel. Frobenius Cauchy–Schwarz, $`\|H_{+-}\|_{\mathrm F}\leq2J`$, and $`\|C\|_{\mathrm F}=2\sqrt\ell`$ give

```math
|\dot\Phi(t)|\leq\frac{8J\sqrt{\ell(t)}}{\sqrt{1-q(t)^2}}.
```

If $`q(t)<1/2`$ throughout, the endpoint phase has shortest distance $`8\theta`$ from zero, and therefore

```math
8\theta\leq\frac{16J}{\sqrt3}\int_0^T\sqrt{\ell(t)}\,dt,
\qquad
\bar\ell\geq\frac{3\theta^2}{4a^2}.
```

If $`q`$ reaches $`1/2`$, use $`q(0)=0`$ and the $`J`$-Lipschitz property of $`q`$, which follows from $`\|\dot U\|\leq J`$. The fastest possible initial rise to any peak $`r`$ has

```math
\int_0^Tq(t)^2\,dt\geq\frac{r^3}{3J}.
```

Because $`\ell\geq q^2/4`$, a peak of $`1/2`$ implies $`\bar\ell\geq1/(96a)`$ and $`a\geq1/2`$. As $`3\theta^2\leq3(\pi/8)^2<1/2\leq a`$, this is at least $`\theta^2/(32a^2)`$. This case does not use a determinant phase at intermediate singular blocks. The two cases prove the proposition. If $`q(T)=0`$, the fall from the peak doubles the triangular area, giving the stated constant $`8`$. □

For completeness, the leading coefficient one follows by choosing the peak threshold $`r=a^{-1/4}`$. Below that threshold the determinant argument gives $`\bar\ell\geq(1-r^2)\theta^2/a^2`$. Above it the one-sided triangular estimate gives $`\bar\ell\geq r^3/(12a)=a^{-7/4}/12`$, which is larger than $`\theta^2/a^2`$ for fixed $`\theta`$ and sufficiently large $`a`$. The exact construction below supplies the matching upper bound.

## Finite endpoint measurements

Before acquiring any data, declare a phase-resolution floor $`g\in(0,\pi/32]`$, endpoint measurement resolution, and failure budgets $`\delta_E,\delta_A`$. The endpoint procedure returns a certified lower bound $`\theta_0\leq\vartheta(U)`$, rather than assuming an exactly known target. A failed conditioning check or a value $`\theta_0<g`$ returns **inconclusive**. The fixed floor prevents an arbitrarily small positive random estimate from causing an unbounded audit budget.

Here is an explicit, deliberately unoptimized implementation with ordinary independent shots. Prepare three Bell pairs between the device and three isolated reference qubits, apply $`U(T)`$ to the device halves, and perform Pauli tomography on the six-qubit Choi state

```math
\rho_U=|u\rangle\langle u|,\qquad
|u\rangle=\frac{1}{\sqrt8}\mathrm{vec}U(T).
```

There are $`D=64`$ Choi dimensions and $`m=D^2-1=4095`$ nonidentity Pauli observables. Measure each observable on $`M`$ freshly prepared copies, giving estimates $`\widehat r_P`$. With endpoint failure probability $`\delta_E`$, Hoeffding's inequality and a union bound imply

```math
M\geq\frac{2}{s^2}\log\frac{2m}{\delta_E}
\quad\Longrightarrow\quad
\max_P|\widehat r_P-r_P|\leq s
```

with probability at least $`1-\delta_E`$. The Hermitian linear-inversion estimate

```math
\widehat\rho=\frac{1}{D}\left(I+\sum_{P\ne I}\widehat r_PP\right)
```

satisfies $`\|\widehat\rho-\rho_U\|\leq\|\widehat\rho-\rho_U\|_{\mathrm F}\leq e`$, with $`e=8s`$. Choose $`e<1/2`$. Let $`|v\rangle`$ be a normalized top eigenvector of $`\widehat\rho`$, and reshape it as $`V=\sqrt8\mathrm{mat}v`$. Then, for some unobservable common phase $`\varphi`$,

```math
\|V-e^{i\varphi}U(T)\|\leq
\|V-e^{i\varphi}U(T)\|_{\mathrm F}
\leq t,\qquad t=\frac{4e}{1-e}.
```

To see the last bound, the top eigenvalue is at least $`1-e`$. Projecting its eigenvector equation orthogonally to $`u`$ gives $`\sin\angle(u,v)\leq e/(1-e)`$. The phase-aligned vector distance is at most $`\sqrt2`$ times this sine; reshaping multiplies that distance by $`\sqrt8`$.

Set $`\widehat A=P_+VP_+`$ and $`\widehat D=P_-VP_-`$. Compute

```math
\sigma=\min\{\sigma_{\min}(\widehat A),\sigma_{\min}(\widehat D)\},
\qquad
\widehat\theta=\frac18\mathrm{dist}\!\left(
\arg\det\widehat A-\arg\det\widehat D,2\pi\mathbb Z\right).
```

Include the predeclared numerical matrix and singular-value margins in $`t`$, using a certified lower bound for $`\sigma`$; budget these margins so that $`\sigma\geq\sigma_0-t`$ on the completeness class below. Let $`b_{\mathrm{num}}`$ bound the numerical error in $`\widehat\theta`$. If $`\sigma\leq t`$, return inconclusive. Otherwise both true blocks are invertible, and a valid lower confidence bound is

```math
\boxed{\quad
\theta_0=\max\left\{0,\widehat\theta-\arcsin(t/\sigma)-b_{\mathrm{num}}\right\}.
\quad}
```

Indeed, every eigenvalue of $`\widehat A^{-1}e^{i\varphi}A`$ lies within distance $`t/\sigma<1`$ of one, so the difference of its determinant phase has a representative of magnitude at most $`4\arcsin(t/\sigma)`$. The same holds for $`D`$; the common phase cancels. Shortest angular distance is Lipschitz, giving the displayed bound. Numerical matrix and phase errors are known margins, not statistical observations. Certified interval arithmetic is one way to supply them.

This procedure assumes the advertised unitary three-qubit model; it is not a test that an arbitrary noisy channel is unitary. For a declared conditioning-resolution target $`\sigma_0\in(0,1]`$, choose the total matrix radius and numerical phase radius before collecting data so that

```math
t\leq\sigma_0\sin(g)/4,\qquad b_{\mathrm{num}}\leq g/2.
```

Soundness does not assume that the actual endpoint obeys this target. Completeness holds on the class whose true blocks have minimum singular value at least $`\sigma_0`$ and true phase $`\theta\geq4g`$. On the endpoint confidence event, $`\sigma\geq\sigma_0-t\geq3\sigma_0/4`$. Hence $`\arcsin(t/\sigma)\leq\arcsin(\sin(g)/3)\leq g/3`$, and the total angular radius $`b=\arcsin(t/\sigma)+b_{\mathrm{num}}`$ is at most $`g`$. Since $`|\widehat\theta-\theta|\leq b`$, the bound satisfies $`\theta_0\geq\theta-2g\geq2g`$ and passes the fixed floor. Allocating fixed fractions of $`t`$ to statistical and numerical matrix error gives an ordinary endpoint shot count $`O(\sigma_0^{-2}g^{-2}\log(1/\delta_E))`$ at fixed dimension. No postselection on a Choi outcome is used.

## Finite timing and the audit decision

Use fresh audit data, independent of the endpoint data. If $`\theta_0<g`$, return inconclusive without executing an audit run. Otherwise choose $`K`$ equal stopping bins of width $`h=T/K`$, with midpoint stopping times

```math
t_j=(j+1/2)h,\qquad j=0,\ldots,K-1.
```

In every shot select $`j`$ uniformly and privately. A finite sufficient choice is

```math
K=\left\lceil\frac{\sqrt{32}\,(JT)^2}{\theta_0}\right\rceil.
```

To account for this discrete timing, couple a continuous uniform time $`t`$ to its bin midpoint $`t_j`$. The matrix-valued function $`C(t)/2`$ is $`J`$-Lipschitz in Frobenius norm. Minkowski's inequality therefore gives

```math
\sqrt{p_K}\geq\left(\sqrt{\bar\ell}-Jh/2\right)_+,
\qquad
p_K=\frac1K\sum_{j=0}^{K-1}\ell(t_j).
```

On the endpoint confidence event, every two-local alternative then has

```math
p_K\geq\frac{\theta_0^2}{128(JT)^2}.
```

Choose the hard audit shot budget

```math
N=\left\lceil128\left(\frac{JT}{\theta_0}\right)^2
\log\frac1{\delta_A}\right\rceil.
```

If all $`N`$ parity outcomes remain positive, report the certificate. If any leakage event occurs, do not issue it. A leakage event does not prove the device is two-local; it only prevents this one-sided certificate.

For every two-local alternative, the probability of issuing a false certificate is at most

```math
\delta_E+\delta_A.
```

The endpoint event fails with probability at most $`\delta_E`$. Conditional on its success and the resulting $`\theta_0,K,N`$, the independent audit has no-event probability at most $`(1-p_K)^N\leq\delta_A`$. This remains valid when those parameters are selected from the endpoint data. Setting $`\delta_E=\delta_A=\delta/2`$ gives total error at most $`\delta`$.

The procedure also has an unconditional hard budget, including on endpoint-confidence failures. Every executed branch has $`\theta_0\geq g`$, so

```math
K\leq K_{\max}=\left\lceil\frac{\sqrt{32}\,a^2}{g}\right\rceil,
\qquad
N\leq N_{\max}=\left\lceil128(a/g)^2\log(1/\delta_A)\right\rceil.
```

With the fixed endpoint budget $`N_E=4095M`$, at most $`N_E+N_{\max}`$ unknown-evolution runs are used for every data record. For nominal midpoint timing the unconditional expected unknown evolution time is at most $`N_ET+N_{\max}T/2`$; the hard worst-case time is at most $`(N_E+N_{\max})T`$. These bounds do not condition on a successful endpoint estimate.

Every genuinely parity-preserving path has zero audit leakage, including arbitrary symmetric nuisance dynamics. Under the completeness promise $`\theta\geq4g`$ and the endpoint conditioning target above, it passes with probability at least $`1-\delta_E`$. Fixed preparation or readout error rates are not incorporated into this ideal trusted-measurement theorem. Adding an unknown background would change both the test and its resource law.

With ideal continuous uniform stopping, the constants $`128`$ and the stopping-bin requirement can be replaced by $`32`$ and no mesh requirement. The discrete version makes the needed timing resolution explicit. The number of timing or random-index bits is $`O(\log K)`$, not $`K`$ stored controls.

If a trusted deterministic stopping error $`r_t`$ is present, so the actual stop differs from its selected midpoint by at most $`r_t`$, replace $`Jh/2`$ by $`J(h/2+r_t)`$ in the preceding argument. The same signal bound follows whenever $`h/2+r_t\leq\theta_0/(2\sqrt{32}J^2T)`$. For example, selecting $`K=\lceil2\sqrt{32}a^2/\theta_0\rceil`$ and taking $`r_t\leq h/2`$ suffices, with unconditional cap $`\lceil2\sqrt{32}a^2/g\rceil`$. The exact expected prefix time $`T/2`$ then becomes a nominal value, with actual expectation within $`r_t`$ of it. This is a trusted timing-error bound, not a theorem about an unknown clock or an adaptively changing waveform.

## Matching lower bound for leakage-only ordinary shots

The lower bound concerns precisely the audit class above: each run starts with an input supported in a definite parity sector, the device is stopped at a chosen time, and the retained device datum is whether parity changed. Stopping times and definite-parity inputs may be chosen adaptively from earlier outcomes and any endpoint data. Arbitrary endpoint measurements are allowed in addition, but coherent superpositions of run histories, coherent inverse access, and phase-sensitive intermediate observations are outside this class.

For fixed $`0<\theta\leq\pi/8`$ and sufficiently large $`a=JT`$, consider the honest path generated by $`H_3=(\theta/T)\Pi`$. It has endpoint $`e^{-i\theta\Pi}`$ and no leakage at any time. The following two-local path has the same endpoint and leakage at most $`4\theta^2/a^2`$ at every time.

Let $`A_0=X_1Z_2`$, $`B_0=Y_1Z_3`$, so $`A_0B_0=i\Pi`$. Parameterize

```math
U=e^{-i\varphi\Pi}e^{-i\alpha A_0}e^{-i\psi\Pi}.
```

Its physical Hamiltonian is

```math
\begin{aligned}
H={}&(\dot\varphi+\dot\psi\cos2\alpha)\Pi\\
&+\dot\alpha(A_0\cos2\varphi+B_0\sin2\varphi)\\
&-\dot\psi\sin2\alpha(B_0\cos2\varphi-A_0\sin2\varphi).
\end{aligned}
```

Ramp $`\alpha`$ from zero to $`\alpha_0`$ at rate $`J`$, initially holding $`\varphi=\psi=0`$. On a plateau fix $`\alpha=\alpha_0`$ and choose

```math
\dot\psi=J/\sin2\alpha_0,\qquad
\dot\varphi=-J\cot2\alpha_0.
```

The coefficient of $`\Pi`$ vanishes, $`H`$ lies in the two-local span of $`A_0,B_0`$, and $`\|H\|=J`$. Moreover, $`(\varphi+\psi)'=J\tan\alpha_0`$. After accumulating phase $`\theta`$, hold $`\varphi,\psi`$ fixed and ramp $`\alpha`$ back to zero at rate $`J`$. The exact duration and endpoint are

```math
JT=\theta\cot\alpha_0+2\alpha_0,
\qquad U(T)=e^{-i\theta\Pi}.
```

For $`a\geq4\sqrt\theta`$, this equation has a small root $`\alpha_0\leq2\theta/a`$. Throughout the path, for every definite-parity input,

```math
\Pr(\text{parity changes at }t)=\sin^2\alpha(t)
\leq4\theta^2/a^2.
```

The no-event evolution within either sector is a scalar phase, so it supplies no further datum to a leakage-only audit. Endpoint observations are exactly identical for the honest and spoof paths. After at most $`N`$ audit runs, even with adaptive choices, the all-no-event transcript under the spoof has probability at least $`(1-p_{\max})^N`$, with $`p_{\max}=4\theta^2/a^2`$. A test accepting the honest path with probability at least $`1-\delta`$ therefore falsely accepts the spoof with probability at least

```math
(1-\delta)(1-p_{\max})^N.
```

For $`0<\delta\leq1/4`$, demanding this also be at most $`\delta`$ requires

```math
N=\Omega\!\left((JT/\theta)^2\log(1/\delta)\right).
```

Together with the upper bound, this proves the matching shot order for the stated leakage-only audit class. It is not a lower bound for unrestricted verification or Hamiltonian learning. Intermediate phase-sensitive access may reveal information that this class intentionally does not collect.

For a resolved fixed phase, take a declared floor comparable to that phase, for example $`g=\theta/4`$. The unconditional upper cap and this fixed-$`\theta`$ lower bound then have the same order. The matched statement is about a declared resolution class, not a worst-case expectation inferred from an unrestricted random positive $`\theta_0`$.

The same construction has exact mean leakage

```math
\bar\ell=
\frac{(a-2\alpha_0)\sin^2\alpha_0+\alpha_0-\tfrac12\sin2\alpha_0}{a}
=\frac{\theta^2}{a^2}+O(a^{-4})
```

at fixed $`\theta`$. This also proves sharpness of the large-action average-leakage coefficient.

## Why a fixed inspection grid is a different task

Suppose a deterministic grid, including endpoints, has maximum spacing $`h`$, and its observations establish $`q(t_j)\leq\eta`$. Lipschitz continuity gives $`q(t)\leq\eta+Jh/2`$ everywhere. When this is below one, the determinant bound permits a two-local false phase no larger than

```math
\theta\leq JT\frac{\eta+Jh/2}{\sqrt{1-(\eta+Jh/2)^2}}.
```

Zero leakage at every inspected time alone does not eliminate a false phase. On an equally spaced grid, exact two-local SU(2) cycles can return to parity at every grid point while accumulating, per period,

```math
\Delta=\pi\left[1-\sqrt{1-(Jh/\pi)^2}\right]
=\frac{J^2h^2}{2\pi}+O(J^4h^4).
```

Over $`T/h`$ cycles the false phase is $`\Theta(J^2Th)`$. Thus resolving a fixed nonzero phase by deterministic zero-leakage inspections requires $`h`$ of order $`\theta/(J^2T)`$ or smaller, up to constants in the small-$`Jh`$ regime. These statements concern possible dynamics, not an assertion that a finite experiment has established exactly zero probability. The random audit instead pools leakage events over independently selected stopping times and has a matched finite-confidence shot bound.

See [resources](resources.md) for the complete accounting and the distinction between charged shots, physical evolution time, timing resolution, and unoptimized trusted operations.
