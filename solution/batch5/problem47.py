""" Problem 47: Distinct Primes Factors

https://projecteuler.net/problem=47

Goal: Find the 1st integers (must be <= N) of K consecutive integers,
that have exactly K distinct prime factors.

Constraints: 20 <= N <= 2e6, 2 <= K <= 4

Distinct Prime Factors: The 1st 2 consecutive integers to have 2 distinct
prime factors are: 14 -> 2 * 7, 15 -> 3 * 5.
The 1st 3 consecutive integers to have 3 distinct prime factors are:
644 -> 2^2 * 7, 645 -> 3 * 5 * 43, 646 -> 2 * 17 * 19.

e.g.: N = 20, K = 2
      result = {14, 20}
      N = 644, K = 3
      result = {644}
"""
from util.reusable import prime_factors, is_prime


def consecutive_distinct_primes(n, k):
    first_consecutive = []
    for composite in range(14, n + 1):
        if is_prime(composite) or len(prime_factors(composite)) != k:
            continue
        valid = True
        for i in range(1, k):
            adjacent = composite + i
            if is_prime(adjacent) or len(prime_factors(adjacent)) != k:
                valid = False
                break
        if valid:
            first_consecutive.append(composite)
    return first_consecutive


def first_4_distinct_primes():
    """
    Project Euler specific implementation that returns the 1st integer
    of the 1st 4 consecutive numbers that have 4 distinct prime factors.
    The minimum representation with 4 distinct prime factors is:
    2 * 3 * 5 * 7 = 210.
    """
    composite = 210
    while True:
        composite += 1
        if is_prime(composite) or len(prime_factors(composite)) != 4:
            continue
        valid = True
        for i in range(1, 4):
            adjacent = composite + i
            if is_prime(adjacent) or len(prime_factors(adjacent)) != 4:
                valid = False
                break
        if valid:
            break
    return composite
