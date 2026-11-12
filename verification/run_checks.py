#!/usr/bin/env python3
"""Finite numerical diagnostics for the symmetry-audit account.

The universal statements are proved in science/. These checks reconstruct their
load-bearing matrix identities, controls, and finite-confidence constants on
specified finite examples. They do not prove a universal bound or priority.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path

import numpy as np
import scipy
from scipy.integrate import quad, solve_ivp
from scipy.linalg import expm
from scipy.optimize import brentq


I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)
PAULI = (I2, X, Y, Z)
I8 = np.eye(8, dtype=complex)


def tensor(items):
    out = np.ones((1, 1), dtype=complex)
    for item in items:
        out = np.kron(out, item)
    return out


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def opnorm(matrix):
    return float(np.linalg.norm(matrix, 2))


def number(value):
    """Stable, compact JSON precision; assertions use unrounded values."""
    return float(f"{float(value):.12g}")


A0 = tensor((X, Z, I2))
B0 = tensor((Y, I2, Z))
PI = tensor((Z, Z, Z))
PLUS = np.flatnonzero(np.diag(PI).real > 0)
MINUS = np.flatnonzero(np.diag(PI).real < 0)
BASIS3 = [
    (labels, tensor(PAULI[label] for label in labels))
    for labels in itertools.product(range(4), repeat=3)
]
LOCAL = [matrix for labels, matrix in BASIS3 if 0 < sum(x != 0 for x in labels) <= 2]


def block(matrix, rows, columns):
    return matrix[np.ix_(rows, columns)]


def leakage(unitary):
    c = block(unitary, MINUS, PLUS)
    return opnorm(c) ** 2, float(np.linalg.norm(c, "fro") ** 2 / 4)


def phase_angle(matrix):
    a = block(matrix, PLUS, PLUS)
    d = block(matrix, MINUS, MINUS)
    sign_a, _ = np.linalg.slogdet(a)
    sign_d, _ = np.linalg.slogdet(d)
    require(abs(sign_a) > 0 and abs(sign_d) > 0, "singular phase block")
    return float(np.angle(sign_a / sign_d))


def circular_difference(left, right):
    return float(np.angle(np.exp(1j * (left - right))))


def phase_distance(matrix):
    return abs(phase_angle(matrix)) / 8


def rotation(pauli, angle):
    return math.cos(angle) * I8 - 1j * math.sin(angle) * pauli


def euler(alpha, phi, psi):
    return rotation(PI, phi) @ rotation(A0, alpha) @ rotation(PI, psi)


def euler_generator(alpha, phi, psi, alpha_dot, phi_dot, psi_dot):
    rz1, rx, rz2 = rotation(PI, phi), rotation(A0, alpha), rotation(PI, psi)
    unitary = rz1 @ rx @ rz2
    derivative = (
        (-1j * phi_dot * PI) @ unitary
        + rz1 @ (-1j * alpha_dot * A0) @ rx @ rz2
        + rz1 @ rx @ (-1j * psi_dot * PI) @ rz2
    )
    return unitary, 1j * derivative @ unitary.conj().T


def check_algebra():
    pauli_error = max(
        opnorm(A0 @ A0 - I8), opnorm(B0 @ B0 - I8),
        opnorm(PI @ PI - I8), opnorm(A0 @ B0 - 1j * PI),
    )
    trace_error = max(abs(np.trace(PI @ local)) for local in LOCAL)
    require(pauli_error < 1e-13 and trace_error < 1e-13, "Pauli/locality algebra")
    require(len(LOCAL) == 36, "three-qubit one- and two-local basis size")
    return {
        "local_nonidentity_basis_size": len(LOCAL),
        "pauli_identity_error": number(pauli_error),
        "max_two_local_parity_trace": number(trace_error),
    }


def latitude_parameters(theta, epsilon, strength=1.0):
    alpha = math.asin(math.sqrt(epsilon))
    psi_dot = strength / math.sin(2 * alpha)
    phi_dot = -strength / math.tan(2 * alpha)
    dwell = theta / (strength * math.tan(alpha))
    return alpha, phi_dot, psi_dot, dwell


def check_latitudes():
    theta, strength = 0.2, 1.0
    cases = []
    max_weight_error = 0.0
    for epsilon in (0.1, 0.01, 0.001, 0.0001):
        alpha, phi_dot, psi_dot, dwell = latitude_parameters(theta, epsilon, strength)
        phi_end, psi_end = phi_dot * dwell, psi_dot * dwell
        endpoint = euler(0.0, phi_end, psi_end)
        endpoint_error = opnorm(endpoint - rotation(PI, theta))
        max_p = max(leakage(euler(alpha, phi_dot * t, psi_dot * t))[0]
                    for t in np.linspace(0, dwell, 31))
        generator_errors, norm_errors, forbidden = [], [], []
        samples = [
            (0.41 * alpha, 0.0, 0.0, strength, 0.0, 0.0),
            (alpha, 0.37 * phi_end, 0.37 * psi_end, 0.0, phi_dot, psi_dot),
            (0.63 * alpha, phi_end, psi_end, -strength, 0.0, 0.0),
        ]
        for values in samples:
            unitary, hamiltonian = euler_generator(*values)
            coeff_a = np.trace(A0 @ hamiltonian) / 8
            coeff_b = np.trace(B0 @ hamiltonian) / 8
            generator_errors.append(opnorm(hamiltonian - coeff_a * A0 - coeff_b * B0))
            norm_errors.append(abs(opnorm(hamiltonian) - strength))
            forbidden.append(abs(np.trace(PI @ hamiltonian) / 8))
            weight_error = math.sqrt(sum(
                abs(np.trace(pauli @ hamiltonian) / 8) ** 2
                for labels, pauli in BASIS3 if sum(x != 0 for x in labels) > 2
            ))
            max_weight_error = max(max_weight_error, weight_error)
            require(opnorm(unitary.conj().T @ unitary - I8) < 1e-11, "Euler unitarity")
        duration = dwell + 2 * alpha / strength
        lower = theta * math.sqrt(1 - epsilon) / (strength * math.sqrt(epsilon))
        require(endpoint_error < 1e-9, "latitude exact endpoint")
        require(abs(max_p - epsilon) < 1e-10, "latitude maximum leakage")
        require(max(generator_errors + norm_errors + forbidden) < 1e-8,
                "differentiated latitude generator")
        require(abs(duration - lower - 2 * alpha / strength) < 1e-11,
                "latitude lower/upper duration relation")
        # Matrix-valued leakage, integrated separately on both ramps and dwell.
        integral = 2 * quad(lambda u: leakage(euler(u, 0.0, 0.0))[1], 0, alpha,
                            epsabs=1e-13)[0] / strength
        integral += quad(
            lambda t: leakage(euler(alpha, phi_dot * t, psi_dot * t))[1],
            0, dwell, epsabs=1e-12,
        )[0]
        analytic_integral = (
            theta * math.sin(alpha) * math.cos(alpha)
            + alpha - 0.5 * math.sin(2 * alpha)
        ) / strength
        require(abs(integral - analytic_integral) < 1e-10, "latitude leakage integral")
        cases.append({
            "epsilon": epsilon, "endpoint_error": number(endpoint_error),
            "max_leakage": number(max_p),
            "generator_span_error": number(max(generator_errors)),
            "generator_norm_error": number(max(norm_errors)),
            "forbidden_coefficient": number(max(forbidden)),
            "quadrature_error": number(abs(integral - analytic_integral)),
            "duration": number(duration),
            "scaled_duration": number(strength * math.sqrt(epsilon) * duration / theta),
        })
    # Independently integrate the physical Hamiltonian for one complete path.
    alpha, phi_dot, psi_dot, dwell = latitude_parameters(theta, 0.01, strength)
    phi_end, psi_end = phi_dot * dwell, psi_dot * dwell
    unitary = I8.copy()
    stages = [
        (alpha / strength, lambda t: strength * A0),
        (dwell, lambda t: euler_generator(alpha, phi_dot * t, psi_dot * t,
                                          0.0, phi_dot, psi_dot)[1]),
        (alpha / strength, lambda t: euler_generator(alpha - strength * t,
                                                     phi_end, psi_end,
                                                     -strength, 0.0, 0.0)[1]),
    ]
    for duration, hamiltonian in stages:
        solution = solve_ivp(
            lambda t, y: (-1j * hamiltonian(t) @ y.reshape(8, 8)).ravel(),
            (0, duration), unitary.ravel(), rtol=1e-10, atol=1e-12,
        )
        require(solution.success, "physical Hamiltonian ODE integration")
        unitary = solution.y[:, -1].reshape(8, 8)
    ode_error = opnorm(unitary - rotation(PI, theta))
    require(ode_error < 2e-9, "ODE latitude endpoint")
    require(max_weight_error < 1e-8, "no weight-three physical Hamiltonian coefficient")
    return {"theta": theta, "strength": strength, "cases": cases,
            "max_weight_above_two": number(max_weight_error),
            "independent_ode_endpoint_error": number(ode_error)}


def check_temporal_means():
    theta = 0.2
    cases = []
    for action in (5.0, 10.0, 30.0, 100.0):
        alpha = brentq(lambda x: theta / math.tan(x) + 2 * x - action, 1e-10, 0.3)
        dwell_action = theta / math.tan(alpha)
        integrated = 2 * quad(lambda x: math.sin(x) ** 2, 0, alpha, epsabs=1e-14)[0]
        integrated += dwell_action * math.sin(alpha) ** 2
        formula = theta * math.sin(alpha) * math.cos(alpha) + alpha - 0.5 * math.sin(2 * alpha)
        mean = formula / action
        ratio = action * action * mean / (theta * theta)
        require(abs(action - dwell_action - 2 * alpha) < 1e-8, "fixed-action small root")
        require(abs(integrated - formula) < 1e-12, "temporal mean exact formula")
        require(mean >= theta * theta / (8 * action * action), "finite mean bound example")
        cases.append({"action": action, "alpha": number(alpha), "mean_leakage": number(mean),
                      "scaled_mean": number(ratio),
                      "quadrature_error": number(abs(integrated - formula))})
    require(all(cases[i + 1]["scaled_mean"] < cases[i]["scaled_mean"]
                for i in range(len(cases) - 1)), "fixed-theta asymptotic approach")
    require(abs(cases[-1]["scaled_mean"] - 1) < 1e-4, "large-action coefficient example")
    return {"theta_fixed": theta, "cases": cases}


def check_cycles():
    strength = 1.0
    cases = []
    for spacing in (0.1, 0.3, 1.0):
        omega = 2 * math.sqrt((math.pi / spacing) ** 2 - strength ** 2)
        cycle = lambda t: rotation(PI, omega * t / 2) @ expm(
            -1j * t * (strength * A0 - omega * PI / 2)
        )
        # Rationalized expression avoids subtractive cancellation for short cells.
        phase = (strength * spacing) ** 2 / (
            math.pi + math.sqrt(math.pi ** 2 - (strength * spacing) ** 2)
        )
        endpoint = cycle(spacing)
        endpoint_error = opnorm(endpoint - rotation(PI, -phase))
        peak = leakage(cycle(spacing / 2))[0]
        expected_peak = (strength * spacing / math.pi) ** 2
        require(endpoint_error < 1e-11, "cycle endpoint")
        require(abs(peak - expected_peak) < 1e-11, "cycle intermediate leakage")
        require(leakage(endpoint)[0] < 1e-20, "cycle exact sampled return")
        # Several windings: compare the matrix datum to the circular phase,
        # never to an unrestricted unwrapped angle.
        cells = 100
        total = np.linalg.matrix_power(endpoint, cells)
        expected_distance = abs(float(np.angle(np.exp(1j * 8 * cells * phase)))) / 8
        require(abs(phase_distance(total) - expected_distance) < 1e-10,
                "cycle phase winding convention")
        cases.append({"spacing": spacing, "phase_per_cell": number(phase),
                      "endpoint_error": number(endpoint_error),
                      "peak_leakage": number(peak),
                      "phase_over_J2_h2": number(phase / (strength * spacing) ** 2),
                      "cells_for_winding_check": cells,
                      "circular_phase_distance": number(phase_distance(total))})
    require(abs(phase_distance(rotation(PI, math.pi / 4))) < 1e-14,
            "special phase has zero determinant obstruction")
    return {"cases": cases, "zero_obstruction_theta": number(math.pi / 4)}


def random_local_hamiltonian(rng):
    matrix = sum(coefficient * pauli for coefficient, pauli in
                 zip(rng.normal(size=len(LOCAL)), LOCAL))
    return matrix / opnorm(matrix)


def check_phase_derivatives():
    rng = np.random.default_rng(7491)
    identity_errors, difference_errors, worst_ratios, mean_ratios = [], [], [], []
    for _ in range(64):
        unitary = I8.copy()
        for _ in range(8):
            unitary = expm(-1j * rng.uniform(0.02, 0.16) * random_local_hamiltonian(rng)) @ unitary
        hamiltonian = random_local_hamiltonian(rng)
        derivative = -1j * hamiltonian @ unitary
        a, d = block(unitary, PLUS, PLUS), block(unitary, MINUS, MINUS)
        c = block(unitary, MINUS, PLUS)
        da, dd = block(derivative, PLUS, PLUS), block(derivative, MINUS, MINUS)
        direct = float(np.imag(np.trace(np.linalg.solve(a, da))
                               - np.trace(np.linalg.solve(d, dd))))
        ca_inverse = np.linalg.solve(a.T, c.T).T
        identity = -2 * float(np.real(np.trace(block(hamiltonian, PLUS, MINUS) @ ca_inverse)))
        p, mean = leakage(unitary)
        require(p < 0.95, "random example block conditioning")
        worst_bound = 8 * math.sqrt(p / (1 - p))
        mean_bound = 8 * math.sqrt(mean / (1 - p))
        step = 1e-6
        forward = expm(-1j * step * hamiltonian) @ unitary
        backward = expm(1j * step * hamiltonian) @ unitary
        finite_difference = circular_difference(phase_angle(forward), phase_angle(backward)) / (2 * step)
        identity_errors.append(abs(direct - identity))
        difference_errors.append(abs(direct - finite_difference))
        worst_ratios.append(abs(direct) / worst_bound)
        mean_ratios.append(abs(direct) / mean_bound)
        require(abs(direct - identity) < 1e-11, "principal-block phase identity")
        require(abs(direct - finite_difference) < 2e-8, "finite-difference phase derivative")
        require(abs(direct) <= mean_bound + 1e-12, "Frobenius leakage derivative bound")
        require(abs(direct) <= worst_bound + 1e-12, "worst-input leakage derivative bound")
    return {"seed": 7491, "cases": 64,
            "max_identity_error": number(max(identity_errors)),
            "max_finite_difference_error": number(max(difference_errors)),
            "max_worst_bound_ratio": number(max(worst_ratios)),
            "max_frobenius_bound_ratio": number(max(mean_ratios))}


def endpoint_certificate(matrix, radius):
    a, d = block(matrix, PLUS, PLUS), block(matrix, MINUS, MINUS)
    sigma = min(float(np.linalg.svd(a, compute_uv=False)[-1]),
                float(np.linalg.svd(d, compute_uv=False)[-1]))
    if sigma <= radius:
        return {"inconclusive": True, "sigma": sigma}
    estimate = phase_distance(matrix)
    lower = max(0.0, estimate - math.asin(radius / sigma))
    return {"inconclusive": False, "sigma": sigma,
            "estimate": estimate, "lower": lower}


def check_endpoint_and_confidence():
    theta, tolerance = 0.2, 0.001
    # Nontrivial within-parity nuisance dynamics with zero parity trace.
    nuisance = 0.23 * tensor((Z, I2, I2)) + 0.17 * tensor((X, X, I2))
    unitary = expm(-1j * nuisance) @ rotation(PI, theta)
    true_phase = phase_distance(unitary)
    choi_vector = unitary.reshape(-1, order="F") / math.sqrt(8)
    rho = np.outer(choi_vector, choi_vector.conj())
    exact_sum = np.zeros((64, 64), dtype=complex)
    perturbed_sum = np.zeros((64, 64), dtype=complex)
    rng = np.random.default_rng(520430)
    observables = 0
    max_expectation_error = 0.0
    for labels in itertools.product(range(4), repeat=6):
        pauli = tensor(PAULI[label] for label in labels)
        expectation = float(np.real(np.vdot(choi_vector, pauli @ choi_vector)))
        perturbation = 0.0 if not any(labels) else float(rng.uniform(-tolerance, tolerance))
        exact_sum += expectation * pauli
        perturbed_sum += (expectation + perturbation) * pauli
        if any(labels):
            observables += 1
            max_expectation_error = max(max_expectation_error, abs(perturbation))
    exact_rho, estimate_rho = exact_sum / 64, perturbed_sum / 64
    exact_error = opnorm(exact_rho - rho)
    actual_frobenius = float(np.linalg.norm(estimate_rho - rho, "fro"))
    state_radius = 8 * tolerance
    require(observables == 4095, "six-qubit Pauli setting count")
    require(exact_error < 1e-12, "complete Choi Pauli reconstruction")
    require(actual_frobenius <= state_radius + 1e-12, "linear-inversion confidence radius")
    _, vectors = np.linalg.eigh(estimate_rho)
    reconstructed = math.sqrt(8) * vectors[:, -1].reshape(8, 8, order="F")
    phase = float(np.angle(np.vdot(unitary.ravel(), reconstructed.ravel())))
    matrix_error = opnorm(reconstructed - np.exp(1j * phase) * unitary)
    matrix_radius = 4 * state_radius / (1 - state_radius)
    require(matrix_error <= matrix_radius + 1e-12, "top-eigenvector matrix radius")
    certificate = endpoint_certificate(reconstructed, matrix_radius)
    require(not certificate["inconclusive"], "well-conditioned endpoint certificate")
    require(0 < certificate["lower"] <= true_phase + 1e-12, "endpoint phase lower bound")
    singular_endpoint = rotation(A0, math.pi / 2)
    require(endpoint_certificate(singular_endpoint, matrix_radius)["inconclusive"],
            "singular endpoint must return inconclusive")
    # This is a numerical evaluation of analytic budgets, not sampled data.
    strength, duration = 1.0, 10.0
    delta_endpoint, delta_audit = 0.025, 0.025
    theta0 = certificate["lower"]
    action = strength * duration
    bins = math.ceil(math.sqrt(32) * action ** 2 / theta0)
    spacing = duration / bins
    continuous_root_floor = theta0 / (math.sqrt(32) * action)
    midpoint_root_floor = continuous_root_floor - strength * spacing / 2
    probability_floor = theta0 ** 2 / (128 * action ** 2)
    audit_shots = math.ceil(128 * (action / theta0) ** 2 * math.log(1 / delta_audit))
    resolution_floor = 0.05
    require(theta0 >= resolution_floor, "resolved example must pass its declared floor")
    audit_cap = math.ceil(128 * (action / resolution_floor) ** 2
                          * math.log(1 / delta_audit))
    bins_cap = math.ceil(math.sqrt(32) * action ** 2 / resolution_floor)
    require(audit_shots <= audit_cap and bins <= bins_cap,
            "unconditional resolution-floor resource caps")
    weak_signal = endpoint_certificate(rotation(PI, resolution_floor / 2), matrix_radius)
    require(weak_signal.get("lower", 0) < resolution_floor,
            "well-conditioned but unresolved phase must not start an audit")
    endpoint_per_setting = math.ceil(2 / tolerance ** 2
                                     * math.log(2 * observables / delta_endpoint))
    endpoint_shots = observables * endpoint_per_setting
    require(midpoint_root_floor ** 2 >= probability_floor - 1e-18,
            "discrete-timing contamination constant")
    log_false_accept = audit_shots * math.log1p(-probability_floor)
    require(log_false_accept <= math.log(delta_audit) + 1e-12,
            "finite no-event false-acceptance constant")
    require(endpoint_per_setting >= 2 / tolerance ** 2
            * math.log(2 * observables / delta_endpoint), "Hoeffding endpoint budget")
    return {
        "endpoint": {
            "perturbation_seed": 520430,
            "pauli_observables": observables,
            "expectation_tolerance": tolerance,
            "max_deterministic_expectation_perturbation": number(max_expectation_error),
            "exact_reconstruction_error": number(exact_error),
            "actual_state_frobenius_error": number(actual_frobenius),
            "state_radius": number(state_radius),
            "actual_phase_aligned_matrix_error": number(matrix_error),
            "matrix_radius": number(matrix_radius),
            "estimated_block_min_singular_value": number(certificate["sigma"]),
            "true_phase_distance": number(true_phase),
            "estimated_phase_distance": number(certificate["estimate"]),
            "phase_lower_bound": number(theta0),
            "singular_endpoint_inconclusive": True,
            "sub_resolution_phase_inconclusive": True,
        },
        "calculated_resource_example": {
            "simulated_shots": 0,
            "strength": strength, "duration": duration,
            "delta_endpoint": delta_endpoint, "delta_audit": delta_audit,
            "declared_resolution_floor": resolution_floor,
            "hard_audit_cap_all_endpoint_outcomes": audit_cap,
            "hard_stopping_bin_cap_all_endpoint_outcomes": bins_cap,
            "stopping_bins": bins, "stopping_spacing": number(spacing),
            "audit_probability_floor": number(probability_floor),
            "audit_shots": audit_shots,
            "no_event_probability_upper_bound": number(math.exp(log_false_accept)),
            "endpoint_shots_per_setting": endpoint_per_setting,
            "endpoint_shots": endpoint_shots,
            "expected_unknown_audit_time": number(audit_shots * duration / 2),
            "unknown_endpoint_time": number(endpoint_shots * duration),
            "false_certificate_probability_upper_bound": delta_endpoint + delta_audit,
        },
    }


def run():
    return {
        "passed": True,
        "scope": "Finite matrix and numerical-budget diagnostics; universal claims require the proofs in science/.",
        "versions": {"numpy": np.__version__, "scipy": scipy.__version__},
        "algebra": check_algebra(),
        "latitudes": check_latitudes(),
        "temporal_means": check_temporal_means(),
        "grid_cycles": check_cycles(),
        "phase_derivatives": check_phase_derivatives(),
        "endpoint_and_confidence": check_endpoint_and_confidence(),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="also write the JSON report to this path")
    arguments = parser.parse_args()
    try:
        report = run()
        status = 0
    except (AssertionError, ValueError, np.linalg.LinAlgError) as error:
        report = {"passed": False, "error": str(error)}
        status = 1
    rendered = json.dumps(report, indent=2, sort_keys=True, allow_nan=False) + "\n"
    if arguments.output:
        arguments.output.parent.mkdir(parents=True, exist_ok=True)
        arguments.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    raise SystemExit(status)


if __name__ == "__main__":
    main()
