""" Problem 44: Pentagon Numbers

https://projecteuler.net/problem=44

Goal: For a given K, find all P_n, where n < N, such that
P_n - P_(n-K) || P_n + P_(n-K) is also pentagonal.

Constraints: 1 <= K <= 9999 & K+1 <= N <= 1e6

Pentagonal Number: The sequence is generated by ->
P_n = n(3n - 1) / 2 -> 1, 5, 12, 22, 35, 51, 70, 92, 117, 145,...

e.g. P_7 = 70 is special in that, if K = 2:
     P_7 - P_5 = 35 = P_5; and, if K = 3:
     P_7 + P_4 = 92 = P_8

e.g.: N = 10, K = 2
      output = {70}
"""
from util.maths.reusable import is_pentagonal_number


def pentagon_numbers_HR(n: int, k: int) -> {int, ...}:
    p_n_s = [(n + 1) * (3 * (n + 1) - 1) // 2 for n in range(n - 1)]
    valid_p_n = set()
    for i in range(k, n - 1):
        p_n = p_n_s[i]
        p_n_minus_k = p_n_s[i - k]
        if (is_pentagonal_number(p_n - p_n_minus_k) is not None
                or is_pentagonal_number(p_n + p_n_minus_k) is not None):
            valid_p_n.add(p_n)
    return valid_p_n


def pentagon_numbers_PE() -> int:
    """
    Project Euler specific implementation that returns the smallest difference,
    |P_x - P_y|, for a pair of pentagonal numbers whose sum and difference
     are both pentagonal.

    Surprisingly, the first eligible pair found has the smallest difference:

    P_x = 7_042_750, where x = 2167, and

    P_y = 1_560_090, where y = 1020.
    """

    p_n_s = [(n + 1) * (3 * (n + 1) - 1) // 2 for n in range(10_000)]
    delta = None
    for x in range(2, 10_000):
        p_x = p_n_s[x]
        for y in range(x - 1, 0, -1):
            p_y = p_n_s[y]
            minus = p_x - p_y
            if (is_pentagonal_number(minus) is None
                    or is_pentagonal_number(p_x + p_y) is None):
                continue
            if delta is None or minus < delta:
                delta = minus
    return delta
