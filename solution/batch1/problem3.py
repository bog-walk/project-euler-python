""" Problem 3: Largest Prime Factor

https://projecteuler.net/problem=3

Goal: Find the largest prime factor of N.

Constraints: 10 <= N <= 1e12

Fundamental Theorem of Arithmetic: There will only ever be a unique set of prime
factors for any number.

e.g.: N = 10
      prime factors = {2, 5}
      largest = 5
"""
from math import isqrt
from util.maths.reusable import prime_factors


def largest_prime_factor(n: int) -> int:
    """
    Uses prime decomposition via the Sieve of Eratosthenes algorithm to return
    the largest prime factor.

    SPEED (EQUAL for n with small factors)
        5.44s for N = 1e12 over 100 iterations
    SPEED (WORSE for n with large factors)
        4.50s for N = 600_851_475_143 over 100 iterations
    """

    factors = prime_factors(n)
    return max(factors.keys())


def largest_prime_factor_recursive(n: int, f: int = 2) -> int:
    """
    Original solution used a floored square root to get an integer value. This
    was replaced with math.isqrt(), introduced in Py 3.8.

    SPEED (EQUAL for n with small factors)
        5.65s for N = 1e12 over 100 iterations
    SPEED (BETTER for n with large factors)
        1.32s for N = 600_851_475_143 over 100 iterations
    """

    factors = [2]
    factors.extend(range(3, isqrt(n) + 1, 2))
    for factor in factors:
        if n % factor == 0:
            return largest_prime_factor_recursive(n // factor, factor)
    if n > 2:
        f = max(f, int(n))
    return f
