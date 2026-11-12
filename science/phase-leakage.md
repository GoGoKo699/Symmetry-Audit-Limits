# A three-body phase requires a detectable symmetry excursion

The exact-symmetry obstruction is inherited from the theory of local symmetric circuits: fewer-body symmetric generators cannot produce every symmetric unitary. Determinant phases make this obstruction observable [1,2]. Here the generator may break symmetry. The question is how much intermediate parity leakage a two-local explanation must then produce.

## Model and observable phase

Work on exactly three qubits, with no additional quantum system, and set $`\hbar=1`$. Define

```math
\Pi=Z_1Z_2Z_3,\qquad P_\pm=\frac{I\pm\Pi}{2}.
```

Both parity sectors have dimension $`d=4`$. Let $`H(t)`$ be a measurable Hermitian Hamiltonian that is a sum of terms supported on at most two qubits. Assume $`\Vert H(t)\Vert \le J`$, where $`J\gt 0`$ bounds the norm of the complete Hamiltonian. Let

```math
\dot U(t)=-iH(t)U(t),\qquad U(0)=I.
```

The controls may be time dependent, and their switching rate and bandwidth are unrestricted. Their norm and elapsed duration are charged. A two-local decomposition does not grant a separate norm budget to each term.

In the parity decomposition write

```math
U(t)=
\begin{pmatrix}A(t)&B(t)\\C(t)&D(t)\end{pmatrix},
\qquad
q(t)=\Vert C(t)\Vert =\Vert B(t)\Vert .
```

Thus $`q(t)^2`$ is the largest parity-transition probability over a parity-definite input. Unitarity gives the equality of the two operator norms. The probability averaged uniformly over the eight computational-basis inputs is

```math
\ell(t)=\frac{\Vert B(t)\Vert _F^2+\Vert C(t)\Vert _F^2}{8}
=\frac{\mathrm{tr}[C(t)^\dagger C(t)]}{4}.
```

It obeys $`\ell(t)\le q(t)^2\le4\ell(t)`$. The average is over ordinary parity-definite preparations; it requires no search for an optimal coherent input.

For a parity-preserving unitary $`W=W_+\oplus W_-`$ define its normalized determinant-phase distance

```math
\vartheta(W)=\frac18\mathrm{dist}\!\left(
\arg\frac{\det W_+}{\det W_-},\;2\pi\mathbb Z\right)
\in[0,\pi/8].
```

Here $`\mathrm{dist}(\phi,2\pi\mathbb Z)`$ denotes the absolute value of the nearest representative modulo $`2\pi`$. Equal sector dimensions make $`\vartheta`$ invariant under a global phase on $`W`$. For the witness targets

```math
W_\theta=e^{-i\theta\Pi},\qquad0\lt \theta\le\pi/8,
```

one has $`\vartheta(W_\theta)=\theta`$. The restriction to the nearest phase branch matters: for example, $`\vartheta(W_{\pi/4})=0`$.

## The phase-leakage identity

**Lemma 1.** Wherever $`q(t)\lt 1`$, the matrices $`A,D`$ are invertible. If $`q(t)\lt 1`$ throughout $`[0,T]`$, the determinant ratio has a unique continuous phase lift $`\Phi(t)`$ with $`\Phi(0)=0`$. On a general nonsingular subinterval a lift exists after choosing its initial branch. Almost everywhere on such an interval,

```math
\dot\Phi(t)=-2\mathrm{Re}\mathrm{tr}
\bigl[H_{+-}(t)C(t)A(t)^{-1}\bigr].
```

Consequently,

```math
|\dot\Phi(t)|\le
8J\frac{q(t)}{\sqrt{1-q(t)^2}},
```

and also

```math
|\dot\Phi(t)|\le
8J\frac{\sqrt{\ell(t)}}{\sqrt{1-q(t)^2}}.
```

**Proof.** Every Pauli string of weight at most two is Hilbert-Schmidt orthogonal to $`\Pi`$. Therefore

```math
\mathrm{tr}(\Pi H)=
\mathrm{tr}H_{++}-\mathrm{tr}H_{--}=0.
```

The block equations give

```math
\frac{d}{dt}\log\det A
=-i\mathrm{tr}H_{++}
-i\mathrm{tr}(H_{+-}CA^{-1}),
```

with the corresponding expression for $`D`$. Unitarity implies

```math
BD^{-1}=-(A^\dagger)^{-1}C^\dagger.
```

The two direct traces cancel in their difference, while the off-diagonal terms combine into the stated real trace. Moreover,

```math
A^\dagger A=I-C^\dagger C,
\qquad \Vert A^{-1}\Vert \le(1-q^2)^{-1/2}.
```

Using $`|\mathrm{tr}X|\le4\Vert X\Vert `$ proves the first bound. For the second use

```math
\Vert H_{+-}\Vert _F\le2J,\qquad
\Vert CA^{-1}\Vert _F\le
\frac{2\sqrt\ell}{\sqrt{1-q^2}},
```

and the Hilbert-Schmidt Cauchy-Schwarz inequality. The equations hold almost everywhere for bounded measurable controls, which suffices after integration. $`\square`$

This identity isolates the relevant distinction. If parity is preserved throughout the path, the phase is constant. Symmetry of the endpoint alone does not force it to be constant.

## Uniform leakage bounds

**Theorem 2.** Suppose $`U(T)=e^{i\chi}W`$ for a parity-preserving $`W`$, and $`q(t)\lt 1`$ throughout. Then

```math
\vartheta(W)\le
J\int_0^T\frac{q(t)}{\sqrt{1-q(t)^2}}\,dt.
```

In particular, a uniform worst-input leakage ceiling $`q(t)^2\le\epsilon\lt 1`$ implies

```math
T\ge
\frac{\vartheta(W)\sqrt{1-\epsilon}}
{J\sqrt\epsilon}.
```

A uniform basis-averaged ceiling $`\ell(t)\le\epsilon\lt 1/4`$ implies

```math
T\ge
\frac{\vartheta(W)\sqrt{1-4\epsilon}}
{J\sqrt\epsilon}.
```

For zero leakage these statements mean that every reachable endpoint has $`\vartheta(W)=0`$.

**Proof.** The endpoint determinant ratio equals that of $`W`$, so every continuous lift satisfies $`|\Phi(T)|\ge8\vartheta(W)`$. Integrate Lemma 1. For the basis-averaged version use $`q^2\le4\ell`$ in the denominator and the Frobenius bound in the numerator. $`\square`$

The same proof permits a time-dependent norm budget $`J(t)`$: insert $`J(t)`$ inside the integral. The constant-$`J`$ corollaries use its uniform upper bound.

## A true temporal mean, without a ceiling

Define the space-and-time averaged leakage and dimensionless action

```math
\overline\ell=\frac1T\int_0^T\ell(t)\,dt,
\qquad L=JT.
```

The next bound does not assume small leakage at every instant. It also allows paths on which $`A`$ or $`D`$ becomes singular.

**Theorem 3.** If $`U(T)=e^{i\chi}W`$ with $`W`$ parity preserving, then

```math
\overline\ell\ge\frac{\vartheta(W)^2}{8L^2}.
```

**Proof.** The function $`q`$ is $`J`$-Lipschitz, because $`\Vert U(t)-U(s)\Vert \le J|t-s|`$. Also $`q(0)=q(T)=0`$.

If $`q(t)\lt 1/2`$ for all $`t`$, Lemma 1 and Cauchy-Schwarz give

```math
8\vartheta(W)
\le\frac{16J}{\sqrt3}\int_0^T\sqrt{\ell(t)}\,dt
\le\frac{16L}{\sqrt3}\sqrt{\overline\ell},
```

so $`\overline\ell\ge3\vartheta(W)^2/(4L^2)`$.

Otherwise $`q`$ reaches $`1/2`$. A Lipschitz path starting and ending at zero must contain the rising and falling sides of a triangular excursion. Hence

```math
\int_0^Tq(t)^2\,dt\ge\frac{1}{12J},
\qquad L\ge1.
```

Since $`\ell\ge q^2/4`$, this gives $`\overline\ell\ge1/(48L)`$. Finally,

```math
6\vartheta(W)^2\le6(\pi/8)^2\lt 1\le L,
```

which implies $`1/(48L)\ge\vartheta(W)^2/(8L^2)`$. Both cases prove the claim. $`\square`$

The constant $`1/8`$ is a convenient finite-action guarantee. The leading asymptotic constant is sharper.

**Theorem 4.** Fix $`0\lt \theta\le\pi/8`$. Among all allowed paths of duration $`T=L/J`$ implementing $`W_\theta`$,

```math
\inf\overline\ell
=\frac{\theta^2+o(1)}{L^2}
\quad\text{as }L\longrightarrow\infty.
```

The lower asymptotic bound applies to every parity-preserving endpoint with determinant-phase distance $`\theta`$. The matching construction is proved for $`W_\theta`$, not for every endpoint with that distance.

**Proof of the lower bound.** Let $`q_*=L^{-1/4}`$. If $`\sup_tq(t)\le q_*`$, the Frobenius inequality in Lemma 1 gives

```math
\overline\ell\ge
(1-q_*^2)\frac{\theta^2}{L^2}.
```

If $`q`$ reaches $`q_*`$, the triangular-excursion argument instead gives

```math
\overline\ell\ge\frac{q_*^3}{6L}
=\frac{L^{-7/4}}6.
```

The latter is asymptotically larger than $`\theta^2/L^2`$ for fixed $`\theta`$. Thus the liminf of $`L^2\overline\ell`$ is at least $`\theta^2`$. The latitude construction in [constructions.md](constructions.md) gives the matching limsup. $`\square`$

The order of limits is fixed: the endpoint phase $`\theta`$ stays positive while $`L`$ grows. No uniform relative-error claim as $`\theta\to0`$ is asserted by this asymptotic statement.

## Approximate endpoints

An approximate endpoint does not have to commute exactly with parity. Compare it to an explicitly specified parity-preserving unitary $`W`$ using phase-optimized operator norm:

```math
\inf_\chi\Vert U(T)-e^{i\chi}W\Vert \le\delta\lt 1.
```

Define

```math
\vartheta_{\rm eff}
=\max\{0,\vartheta(W)-\arcsin\delta\}.
```

Every conclusion of Theorem 2 remains true with $`\vartheta(W)`$ replaced by $`\vartheta_{\rm eff}`$. This includes its integrated inequality when $`q\lt 1`$ throughout, and both uniform-ceiling bounds.

To see the endpoint correction, set $`E_+=e^{-i\chi}AW_+^\dagger`$ and similarly $`E_-=e^{-i\chi}DW_-^\dagger`$. Each satisfies $`\Vert E_\pm-I\Vert \le\delta`$. Every eigenvalue lies in the disk of radius $`\delta`$ about $`1`$, so its argument has absolute value at most $`\arcsin\delta`$. Each rank-four determinant phase changes by at most $`4\arcsin\delta`$; their ratio changes by at most $`8\arcsin\delta`$. Circular triangle inequality and the integrated phase identity give the result.

This is an operator-norm endpoint statement. It does not silently substitute fidelity or diamond distance for $`\delta`$. The exact-endpoint temporal-mean bounds above retain their stated endpoint hypothesis.

## Scope and attribution

The result bounds false determinant phases under a two-local explanation of a defined closed three-qubit process. It is not a lower bound for unrestricted Hamiltonian identification, and parity leakage does not identify every possible higher-body term.

An unobserved mediator changes the model. Couplings of the form $`Z_j\otimes K_j`$ can preserve system parity throughout while mediating a higher-body system phase. A system-only parity audit cannot exclude such an auxiliary explanation. The no-ancilla assumption is therefore part of the scientific claim.

The exact-symmetry invariant and its interpretation as an interaction witness come from [1,2]. Small-excursion geometric control and holonomic speed bounds are established tools [3,4]. The contribution here is their quantitative use in leakage and finite-observation audits; the inverse-square-root leakage scaling alone is not presented as a new geometric mechanism.

1. I. Marvian, *Restrictions on realizable unitary operations imposed by symmetry and locality*, Nature Physics **18**, 283–289 (2022), [arXiv:2003.05524](https://arxiv.org/abs/2003.05524).
2. L. A. Zhukas, Q. Wang, O. Katz, C. Monroe, and I. Marvian, *Observation of the symmetry-protected signature of 3-body interactions*, [arXiv:2408.10475](https://arxiv.org/abs/2408.10475), especially Eqs. (3)–(4).
3. O. Sönnerborn, *Estimate of the time required to perform a nonadiabatic holonomic quantum computation*, Physical Review A **109**, 062433 (2024), [arXiv:2404.05844](https://arxiv.org/abs/2404.05844).
4. O. Sönnerborn, *Isoholonomic inequality and tight implementations of holonomic quantum gates*, Physical Review A **111**, 052430 (2025), [arXiv:2412.12013](https://arxiv.org/abs/2412.12013).
