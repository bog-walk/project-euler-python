""" Problem 1: Multiples of 3 or 5

https://projecteuler.net/problem=1

Goal: Find the sum of all natural numbers less than N that are multiples of
either of the provided factors K1 or K2.

Constraints: 1 <= N <= 1e9, 1 <= K < N

e.g.: N = 10, K1 = 3, K2 = 5
      multiples of K1 || K2 < N = {3, 5, 6, 9}
      sum = 23
"""
from math import lcm
from util.maths.reusable import gauss_sum


def sum_of_multiples_brute(n: int, k_1: int, k_2: int) -> int:
    """
    Brute iteration through all numbers < N that checks for selector predicate.

    SPEED (WORSE)
        1.15s for N = 1e7, K1 = 20, K2 = 32

    :raises MemoryError: When upper test constraints > 1e7.
    """

    min_m = min(k_1, k_2)
    return sum([m for m in range(min_m, n) if (m % k_1 == 0 or m % k_2 == 0)])


def sum_arith_progress(max_term: int, delta: int) -> int:
    """ Calculates the sum of an arithmetic progression sequence.

    Solution based on the formula:

    S_n = {n}Sigma{k=1} a + (k - 1)d = n(2a + (n - 1)d)/2,

    where a is the 1st term, d is the delta, and n is the amount of terms to add.

    a and d are the same in this case, so the formula becomes:

    S_n = (n(n + 1)d) / 2

    Note that this is an adapted Gaussian sum (triangular number) formula,
    where n is replaced with the amount of terms that are evenly divisible by d,
    then the original formula is multiplied by d.
    """

    n = max_term // delta
    return gauss_sum(n) * delta


def sum_of_multiples(n: int, k_1: int, k_2: int) -> int:
    """
    Calculates the sum of multiples of both factors minus the sum of duplicates
    found via the least common multiple of the given factors.

    Original solution used manual implementation of lcm(), but this was replaced
    with math.lcm(), introduced in PY 3.9.

    SPEED (BETTER)
        3480ns for N = 1e7, K1 = 20, K2 = 32
    """

    n -= 1  # n not inclusive
    if k_1 == k_2:
        return sum_arith_progress(n, k_1)
    duplicate_sum = sum_arith_progress(n, lcm(k_1, k_2))
    return sum_arith_progress(n, k_1) + sum_arith_progress(n, k_2) - duplicate_sum
