""" Problem 25: N-digit Fibonacci Number

https://projecteuler.net/problem=25

Goal: Find the first term in the Fibonacci sequence to have N digits.

Constraints: 2 <= N <= 5000

e.g.: N = 3
      Fibonacci sequence = {0,1,1,2,3,5,8,13,21,34,55,89,144}
      first term with 3 digits = F(12)
"""
from math import ceil, log10


def n_digit_fib_terms(max_digits):
    """
    SPEED (BEST for N<= 10): 0.0287ms for N = 10
    4590ms (compared to <1ms with inverted formula) for N = 5000

    :return [list] of the first Fibonacci terms to have (index + 2) digits.
    """
    term = 7
    f_n = 13
    terms = [0] * (max_digits - 1)
    terms[0] = term
    f_n_minus1 = 8
    digits = 3
    while digits <= max_digits:
        term += 1
        f_n_minus2, f_n_minus1 = f_n_minus1, f_n
        f_n = f_n_minus1 + f_n_minus2
        if len(str(f_n)) == digits:
            terms[digits - 2] = term
            digits += 1
    return terms


def nth_fib_golden(n):
    """
    The golden ratio provides an alternative to iteration & is based on
    the closed-form formula:
    Fn = (Phi^n - Psi^n) / sqrt(5),
    with Phi = (1 + sqrt(5)) / 2 ~= 1.61803... & Psi = -Phi^-1

    Rounding, using the nearest integer function, reduces the formula to:
    Fn = [Phi^n / sqrt(5)], where n >= 0.
    Truncation, using the floor function, would result instead in:
    Fn = [(Phi^n / sqrt(5)) + 0.5], where n >= 0.

    :return the nth Fibonacci sequence number.
    """
    phi = (1 + 5 ** 0.5) / 2
    return round(phi ** n / 5 ** 0.5)


def n_digit_fib_term_using_golden(n):
    """
    Iterative solution uses Golden Ratio to calculate the Fibonacci
    sequence numbers.

    SPEED: 0.0406ms for N = 10
    Significantly slower execution from N > 10, due to exponential
    need to calculate Phi^N.

    :return first Fibonacci term to have N digits.
    """
    term = 7
    f_n = 13
    # Pattern shows the amount of digits increases every 4th-5th term
    step = 4
    while len(str(f_n)) < n:
        term += step
        f_n = nth_fib_golden(term)
        while len(str(f_n)) < n:
            term += 1
            f_n = nth_fib_golden(term)
    return term


def n_digit_fib_term_by_digits_golden(n):
    """
    O(n) solution based on the closed-form golden ratio formula shown
    previously being inverted to calculate log10 of each Fibonacci number,
    thereby returning the term that has the required amount of digits,
    without the need to iterate.

    SPEED: 39.7731ms for N = 10
    (BEST for N > 10) 0.0837ms for N = 5000

    :return first Fibonacci term to have N digits.
    """
    phi = (1 + 5 ** 0.5) / 2
    return int(ceil((n - 1 + log10(5) / 2) / log10(phi)))
