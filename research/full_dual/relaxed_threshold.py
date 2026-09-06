"""Relaxed-threshold finite dual certificates and endpoint lemma."""

from __future__ import annotations

from fractions import Fraction

from full_dual import finite_certificate


def relaxed_certificate(v: tuple[int, ...], epsilon: Fraction):
    q = len(v) + 1
    delta = Fraction(1, q) - epsilon
    if not 0 < epsilon < Fraction(1, q):
        raise ValueError("epsilon must lie strictly between 0 and 1/q")
    return finite_certificate(v, delta)


def endpoint_lemma_statement():
    return (
        "If for every epsilon>0 there exists t_epsilon with "
        "min_i ||t_epsilon*v_i|| >= 1/q-epsilon, compactness of R/Z "
        "gives a convergent subsequence and a limit t with "
        "min_i ||t*v_i|| >= 1/q."
    )
