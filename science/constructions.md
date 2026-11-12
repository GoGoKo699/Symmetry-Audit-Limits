# Exact low-leakage paths and symmetry between observation times

This file supplies matching paths for the three-qubit bounds in [phase-leakage.md](phase-leakage.md). Every physical generator below acts on at most two qubits. No auxiliary system is introduced. The construction charges Hamiltonian norm and elapsed time; its control bandwidth is unrestricted.

## A Pauli algebra made from two-local controls

Set

$$
A_0=X_1Z_2,\qquad B_0=Y_1Z_3,\qquad C_0=Z_1Z_2Z_3=\Pi.
$$

These operators satisfy

$$
A_0^2=B_0^2=C_0^2=I,
\qquad A_0B_0=iC_0,
$$

and the cyclic Pauli relations. They form a Pauli representation with multiplicity four, with $C_0$ distinguishing the two parity sectors. A Hamiltonian

$$
H(t)=h_x(t)A_0+h_y(t)B_0
$$

is two local and has norm $\sqrt{h_x(t)^2+h_y(t)^2}$. Thus its coefficients may be derived in a single two-dimensional block and then used identically in all four blocks.

## A latitude path with an exact endpoint

**Proposition 1.** For $J>0$, $0<\epsilon<1$, and $\theta>0$, there is an exact two-local implementation of $W_\theta=e^{-i\theta\Pi}$ with

$$
q(t)^2=\ell(t)\le\epsilon,
\qquad
JT=\theta\sqrt{\frac{1-\epsilon}{\epsilon}}
+2\arcsin\sqrt\epsilon.
$$

For $0<\theta\le\pi/8$ this matches the uniform-leakage lower bound up to the additive ramp action $2\arcsin\sqrt\epsilon$.

**Construction.** Write $s=\sqrt\epsilon$, $r=\sqrt{1-\epsilon}$, and $\alpha_0=\arcsin s$. In each Pauli block use

$$
U=
\begin{pmatrix}
a&b\\-b^*&a^*
\end{pmatrix},
\qquad
a=\cos\alpha\,e^{-i\phi},\quad
b=-i\sin\alpha\,e^{-i\psi}.
$$

This form makes both leakage quantities equal to $\sin^2\alpha$.

First increase $\alpha$ from $0$ to $\alpha_0$ at rate $J$, keeping $\phi=\psi=0$. The generator is $JA_0$ and the ramp lasts $\alpha_0/J$.

Next keep $\alpha=\alpha_0$ and choose

$$
\dot\phi=J\frac{s}{r},\qquad
\dot\psi=-J\frac{r}{s}.
$$

Writing $\chi=\phi+\psi$, direct differentiation gives

$$
H(t)=J\bigl[\sin\chi(t)A_0-\cos\chi(t)B_0\bigr].
$$

Its diagonal Pauli coefficient vanishes because

$$
r^2\dot\phi+s^2\dot\psi=0,
$$

and its norm is exactly $J$. Hold this latitude for

$$
\tau=\frac{\theta r}{Js},
$$

so that $\phi$ increases from $0$ to $\theta$.

Finally keep $\phi,\psi$ at their endpoint values and decrease $\alpha$ from $\alpha_0$ to $0$ at rate $J$. The generator is the constant two-local operator

$$
H=-J\bigl[\cos\chi_{\rm end}A_0+
\sin\chi_{\rm end}B_0\bigr].
$$

It lasts $\alpha_0/J$. At the endpoint $b=0$ and $a=e^{-i\theta}$, hence the complete operation is exactly $e^{-i\theta C_0}$. Adding the three durations proves the formula. $\square$

The dwell drive rotates at angular frequency

$$
|\dot\chi|
=J\frac{|1-2\epsilon|}{\sqrt{\epsilon(1-\epsilon)}}.
$$

It diverges as $J/\sqrt\epsilon$ when $\epsilon\to0$. The construction therefore establishes a norm-bounded optimum with unrestricted temporal bandwidth. It does not establish the same optimum under a fixed bandwidth or slew-rate constraint.

## Uniform ceilings and a true temporal mean

For fixed $0<\theta\le\pi/8$, Proposition 1 and the converse imply

$$
\lim_{\epsilon\to0}
\frac{J\sqrt\epsilon}{\theta}
T_{\rm worst}(\theta,\epsilon)=1,
$$

where $T_{\rm worst}$ is the minimum duration under $q^2\le\epsilon$. The same limit holds when only the uniform basis-averaged ceiling $\ell\le\epsilon$ is imposed. The lower bound then has $\sqrt{1-4\epsilon}$ in place of $\sqrt{1-\epsilon}$, which has the same limit.

For the temporal-mean problem, prescribe a large action $L=JT$. Choose the small positive solution of

$$
L=\theta\cot\alpha_0+2\alpha_0.
$$

Such a solution exists for all sufficiently large $L$, because the right side diverges at $\alpha_0=0$ and decreases there. At fixed $\theta$,

$$
\alpha_0=\frac{\theta}{L}+O_\theta(L^{-3}).
$$

The two ramps have total leakage integral

$$
\frac2J\int_0^{\alpha_0}\sin^2u\,du
=\frac1J\left(\alpha_0-\frac12\sin2\alpha_0\right),
$$

while the dwell contributes $\theta\sin\alpha_0\cos\alpha_0/J$. Thus the exact temporal mean is

$$
\overline\ell
=\frac{
\theta\sin\alpha_0\cos\alpha_0+
\alpha_0-\tfrac12\sin2\alpha_0}{L}
=\frac{\theta^2}{L^2}+O_\theta(L^{-4}).
$$

This proves the upper asymptotic bound in Theorem 4 of [phase-leakage.md](phase-leakage.md). Together with that theorem it identifies the sharp leading constant for the witness family $W_\theta$.

## What a deterministic observation grid guarantees

Intermediate observations mean independent repetitions of the same repeatable process, stopped at selected times. They are not invasive measurements inserted into one evolving trajectory.

Let

$$
0=t_0<t_1<\cdots<t_M=T,
\qquad h_j=t_{j+1}-t_j,\quad h_{\max}=\max_jh_j.
$$

Suppose an audit bounds $q(t_j)\le\eta$ at every grid point. The $J$-Lipschitz property gives, inside interval $j$,

$$
q(t)\le\eta+J\min\{t-t_j,t_{j+1}-t\}.
$$

Set $q_{\max}=\eta+Jh_{\max}/2$. If $q_{\max}<1$, Lemma 1 gives the following bound on the determinant phase of a parity-preserving endpoint $W$:

$$
\vartheta(W)\le
\frac{JT\eta+\tfrac14J^2\sum_jh_j^2}
{\sqrt{1-q_{\max}^2}}.
$$

Indeed, the area under the triangular envelope is

$$
\int_{t_j}^{t_{j+1}}q(t)\,dt
\le\eta h_j+\frac{Jh_j^2}{4}.
$$

For a uniform grid of spacing $h$ with exact sampled symmetry, this becomes

$$
\vartheta(W)\le
\frac{J^2Th}{4\sqrt{1-(Jh/2)^2}}.
$$

The phase of an approximately implemented target is treated by replacing $\vartheta(W)$ with $\vartheta_{\rm eff}$ as defined in [phase-leakage.md](phase-leakage.md).

A basis-averaged grid certificate is also possible. The function $\sqrt{\ell(t)}$ is $J$-Lipschitz. One proof differentiates $\ell=\|C\|_F^2/4$ and uses $|\dot\ell|\le2J\sqrt\ell$; the zero points follow by continuity. If $\ell(t_j)\le\eta^2$ and $\eta+Jh_{\max}/2<1/2$, the same numerator is valid with denominator

$$
\sqrt{1-4(\eta+Jh_{\max}/2)^2}.
$$

Here the square root of a probability, rather than the probability itself, enters the grid resolution.

## Exact spoofing between perfect samples

**Proposition 2.** Let $0<Jh\le\pi$. On an interval of length $h$, define

$$
\omega=2\sqrt{(\pi/h)^2-J^2},
\qquad
H(t)=J[A_0\cos\omega t+B_0\sin\omega t].
$$

The exact propagator is

$$
U(t)=e^{-i\omega tC_0/2}
e^{-it(JA_0-\omega C_0/2)}.
$$

At the end of the interval,

$$
U(h)=e^{if(Jh)C_0},\qquad
f(x)=\pi-\sqrt{\pi^2-x^2},
$$

and the maximal intermediate leakage is $(Jh/\pi)^2$.

**Proof.** Differentiation verifies the propagator. Since $A_0$ and $C_0$ anticommute, the second exponential has angular speed

$$
\Omega=\sqrt{J^2+\omega^2/4}=\pi/h.
$$

At $t=h$ it is $-I$, yielding the stated endpoint. The transition amplitude inside this exponential has modulus $(J/\Omega)|\sin\Omega t|$; the first exponential is parity diagonal. Hence the maximal squared transition amplitude is $(J/\Omega)^2=(Jh/\pi)^2$. $\square$

Restart this waveform in each cell of a uniform grid. At every grid point the cumulative unitary is a diagonal function of $\Pi$, so it preserves not only parity but also total excitation number exactly. Nevertheless it accumulates the three-body phase

$$
\Theta=Mf(Jh),\qquad M=T/h.
$$

For $Jh\to0$,

$$
\Theta=
\frac{J^2Th}{2\pi}+O(J^4Th^3).
$$

Reversing the drive orientation reverses the sign. Replacing $J$ by a drive amplitude $a\le J$ continuously tunes the total phase through every value between zero and $Mf(Jh)$. Thus a desired phase in that interval can be spoofed exactly; no approximation of the endpoint is needed.

The measurable determinant phase is periodic. To identify it with an unwrapped target $\theta$, choose the tuned phase in $0<\theta\le\pi/8$. Large accumulated phases must not be counted as proportionally large observable signals after they wind around the phase circle.

## Matched grid-resolution order

In the small-cell regime, the upper envelope and the exact spoof have the same order $J^2Th$. For a fixed meaningful phase tolerance $0<\theta_{\rm tol}\le\pi/8$, uniform deterministic parity samples therefore require spacing of order

$$
h\asymp\frac{\theta_{\rm tol}}{J^2T},
\qquad
M\asymp\frac{J^2T^2}{\theta_{\rm tol}},
$$

up to constants, to exclude an adversarial two-local false phase using this audit criterion. The sufficiency is the triangular-envelope bound; necessity is the exactly sampled spoof with a tunable amplitude. This comparison assumes that the indicated number of cells is large enough for $Jh$ to be small. It is an observation-resolution statement, not the number of statistical repetitions required to estimate each sample probability.

Endpoint symmetry alone supplies no such guarantee. The sample times, trusted parity preparation/readout, independent norm bound, repeatability of the waveform, absence of auxiliary systems, and allowed temporal bandwidth are all part of the operational model.

The constructions use familiar Pauli control and geometric phase accumulation. Their role here is to saturate a specified leakage or observation constraint. They do not establish optimal attainment for an arbitrary parity-preserving target, nor a fixed-bandwidth implementation theorem.
