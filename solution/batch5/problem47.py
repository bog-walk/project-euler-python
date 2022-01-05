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
from util.maths.reusable import prime_factors


def count_prime_factors(n):
    """
    Modified prime_factor utility method that instead counts number
    of distinct prime factors for each n <= N.

    :return: Each ith element represents the number of prime factors
    for the number i.
    """
    factors = [0]*(n + 1)
    for i in range(2, n + 1):
        if factors[i] == 0:
            for j in range(i, n + 1, i):
                factors[j] += 1
    return factors


def consecutive_distinct_primes(n, k):
    first_consecutive = []
    # Extend k-above limit to account for k-consecutive runs
    factors = count_prime_factors(n + k)
    count = 0
    for composite in range(14, n + k):
        if factors[composite] != k:
            count = 0
            continue
        count += 1
        if count >= k:
            first_consecutive.append(composite - k + 1)
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
        if len(prime_factors(composite)) != 4:
            continue
        valid = True
        for i in range(1, 4):
            adjacent = composite + i
            if len(prime_factors(adjacent)) != 4:
                valid = False
                break
        if valid:
            break
    return composite
