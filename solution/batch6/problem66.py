""" Problem 66: Diophantine Equation

https://projecteuler.net/problem=66

Goal: Given a quadratic Diophantine equation of the form, x^2 - Dy^2 = 1, find
the value of D <= N in minimal solutions of x for which the largest value of x is
obtained. There are no solutions in positive integers when D is square.

Constraints: 7 <= N <= 1e4

Pell-Fermat Equation: Any Diophantine equation of the form x^2 - ny^2 = 1,
where n is a given positive non-square integer. As long as n is not a perfect
square, this equation has infinitely many distinct integer solutions that can be
used to approximate sqrt(n) by rational numbers of the form x/y.

e.g.: N = 7
      D = 2 -> 3^2 - 2 * 2^2 = 1
      D = 3 -> 2^2 - 3 * 1^2 = 1
      D = 5 -> 9^2 - 5 * 4^2 = 1
      D = 6 -> 5^2 - 6 * 2^2 = 1
      D = 7 -> 8^2 - 7 * 3^2 = 1
      largest x = 9 when D = 5
"""
from math import modf, sqrt


def largest_diophantine_x(n: int) -> int:
    """
    Solution is similar to that in Problem 64, which solves continuous fractions
    based on the formulae below:

    n_k = d_{k-1} * a_{k-1} - n_{k-1}

    d_k = floor((x - (n_k)^2)/d_{k-1})

    a_k = floor((a_0 + n_k)/d_k)

    The fundamental solution is found by performing this continued fraction
    expansion, then applying the recursive relation to the successive convergents
    using the formulae:

    h_n = a_n * h_{n-1} + h_{n-2}

    k_n = a_n * k_{n-1} + k_{n-2}

    with h_n representing numerators & k_n representing denominators.

    When h_n & k_n satisfy the Pell equation, this pair becomes the fundamental
    solution (x_1, y_1) for the value D, with h_n = x_1 and k_n = y_1.
    """

    max_d, max_x = 2, 3  # smallest fundamental D = 2
    for d in range(3, n + 1):
        fractional, root = modf(sqrt(d))
        if fractional == 0.0:  # skip perfect squares
            continue
        a_0 = int(root)
        a, numerator, denominator = (a_0, 0, 1)
        # represents [h_n_minus_2, h_n_minus_1, a * h_n_minus_1 + h_n_minus_2]
        h_n = [0, 1, a_0]
        # represents [k_n_minus_2, k_n_minus_1, a * k_n_minus_1 + k_n_minus_2]
        k_n = [1, 0, 1]
        while True:
            numerator = denominator * a - numerator
            denominator = (d - numerator * numerator) // denominator
            a = (a_0 + numerator) // denominator
            h_n[0], h_n[1] = h_n[1], h_n[2]
            h_n[2] = a * h_n[1] + h_n[0]
            k_n[0], k_n[1] = k_n[1], k_n[2]
            k_n[2] = a * k_n[1] + k_n[0]
            if h_n[2] * h_n[2] - d * k_n[2] * k_n[2] == 1:
                break
        if h_n[2] > max_x:
            max_d, max_x = d, h_n[2]
    return max_d
