""" Problem 25: N-digit Fibonacci Number

https://projecteuler.net/problem=25

Goal: Find the first term in the Fibonacci sequence to have N digits.

Constraints: 2 <= N <= 5000

e.g.: N = 3
      Fibonacci sequence = {0,1,1,2,3,5,8,13,21,34,55,89,144}
      first term with 3 digits = F(12)
"""
from math import ceil, log10

phi = (1 + 5 ** 0.5) / 2


def n_digit_fib_terms_brute(max_digits: int) -> list[int]:
    """ Iterative solution that checks all Fibonacci numbers.

    Original solution compared digit lengths by converting f_n to a string. This
    has been replaced by calling log10(f_n) and comparing it to the required
    digits minus 1, with significant performance improvement.

    SPEED (WORST for low N)
        7.7e4ns for N = 10
    SPEED (WORSE for high N)
        25.72ms for N = 5000

    :returns: List of the first Fibonacci terms to have (index + 2) digits.
    """

    term = 7
    f_n = 13
    terms = [0]*(max_digits - 1)
    terms[0] = term
    f_n_minus1 = 8
    digits = 3
    while digits <= max_digits:
        term += 1
        f_n_minus2, f_n_minus1 = f_n_minus1, f_n
        f_n = f_n_minus1 + f_n_minus2
        if int(log10(f_n)) == digits - 1:
            terms[digits - 2] = term
            digits += 1
    return terms


def nth_fib_golden(n: int) -> int:
    """ Finds the nth Fibonacci number using Binet's formula.

    The Golden Ratio, Phi, provides an alternative to iteration, based on
    the closed-form formula:

    Fn = (Phi^n - Psi^n) / sqrt(5), with

    Phi = (1 + sqrt(5)) / 2 ~= 1.61803... and
    Psi = -Phi^-1

    Rounding, using the nearest integer function, reduces the formula to:

    Fn = [Phi^n / sqrt(5)]`, where n >= 0

    Truncation, using the floor function, would result instead in:

    Fn = floor(Phi^n / sqrt(5)) + 0.5, where n >= 0
    """

    return round(phi ** n / 5 ** 0.5)


def n_digit_fib_term_golden_brute(n: int) -> int:
    """ Iterative solution uses the Golden Ratio to check all Fibonacci numbers.

    Original solution compared digit lengths by converting f_n to a string. This
    has been replaced by calling log10(f_n) and comparing it to the required
    digits minus 1, with significant performance improvement.

    SPEED (BETTER for low N)
        6.0e4ns for N = 10
    SPEED (IMPOSSIBLE for N > 300)
        Significantly slower execution due to the exponential need to calculate
        larger Phi^N and resulting OverflowError

    :returns: First Fibonacci term to have N digits.
    """

    term = 7
    f_n = 13
    # pattern shows the amount of digits increases every 4th-5th term
    step = 4
    while log10(f_n) < n - 1:
        term += step
        f_n = nth_fib_golden(term)
        while log10(f_n) < n - 1:
            term += 1
            f_n = nth_fib_golden(term)
    return term


def n_digit_fib_term_golden_formula(n: int) -> int:
    """ O(n) solution based on the inversion of closed-form Binet's formula.

    Phi^t / sqrt(5) > 10^(n-1)

    Phi^t > 10^(n-1) * sqrt(5)

    log(Phi)t > log(10)(n - 1) + log(5)/2

    t > (1(n - 1) + log(5)/2) / log(Phi)

    t = ceil(n - 1 + log(5)/2) / log(Phi)

    SPEED (BEST for low N)
        1.1e4ns for N = 10
    SPEED (BEST for high N)
        1.8e4ns for N = 5000

    :returns: First Fibonacci term to have N digits.
    """

    return ceil((n - 1 + log10(5) / 2) / log10(phi))
