""" Problem 1: Multiples of 3 or 5

https://projecteuler.net/problem=1

Goal: Find the sum of all natural numbers less than N that are multiples of
either of the provided factors K1 or K2.

Constraints: 1 <= N <= 1e9, 1 <= K <= N

e.g.: N = 10, K1 = 3, K2 = 5
      multiples of K1 || K2 < N = {3, 5, 6, 9}
      sum = 23
"""
from util.maths.reusable import lcm


def sum_of_multiples_brute(n: int, k_1: int, k_2: int) -> int:
    """ Throws MemoryError for upper test constraints > 1e7. """
    min_m = min(k_1, k_2)
    return sum([m for m in range(min_m, n) if (m % k_1 == 0 or m % k_2 == 0)])


def sum_arith_progress(max_term: int, delta: int) -> int:
    """ Calculates the sum of an arithmetic progression sequence.

    Based on the formula:
    n-1_Sigma_k=0 (a + k * d) = (n / 2) * (2 * a + (n - 1) * d), where
    a is the 1st term, d is the delta, and n is the amount of terms to add.
    a and d are the same in this case, so the formula becomes:
    n-1_Sigma_k=0 (a + k * d) = (n / 2) * (n + 1) * d.

    Conversion of very large floats to integers in this formula lead to large
    rounding losses, so division by 2 & int cast is replaced with a single bitwise
    right shift, as x >> 1 == x // 2^1.
    """
    n = max_term // delta
    return n * (n + 1) * delta >> 1


def sum_of_multiples(n: int, k_1: int, k_2: int) -> int:
    """
    Calculates the sum of multiples of both factors minus the sum of duplicates
    found via the least common multiple of the given factors.
    """
    n -= 1  # N not inclusive
    if k_1 == k_2:
        return sum_arith_progress(n, k_1)
    duplicate_sum = sum_arith_progress(n, lcm(k_1, k_2))
    return sum_arith_progress(n, k_1) + sum_arith_progress(n, k_2) - duplicate_sum
