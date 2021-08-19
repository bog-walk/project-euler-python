""" Problem 1: Multiples of 3 or 5

https://projecteuler.net/problem=1

Goal: Find the sum of all natural numbers less than N that are multiples of either of
the provided factors K1 or K2.

Constraints: 1 <= N <= 1e9, 1 <= K <= N.

e.g.: Sum of all multiples of 3 or 5 below 10 (i.e. 3, 5, 6, 9) = 23.
"""
from math import gcd


def sum_of_multiples_brute(n, k1, k2):
    min_m = min(k1, k2)
    return sum([m for m in range(min_m, n) if (m % k1 == 0 or m % k2 == 0)])


def sum_arith_progress(n, diff):
    """
    Formula returns sum of arithmetic progression series based on number of terms.
    """
    terms = int(n / diff)
    return terms * (terms + 1) * diff / 2


def sum_of_multiples(n, k1, k2):
    """ FINAL SOLUTION
    Return sum of multiples of both factors minus any duplicates found via lcm.
    """
    n -= 1  # N not inclusive
    if k1 == k2:
        return sum_arith_progress(n, k1)
    lcm = int((k1 * k2) // gcd(k1, k2))
    return (sum_arith_progress(n, k1) +
            sum_arith_progress(n, k2) -
            sum_arith_progress(n, lcm))
