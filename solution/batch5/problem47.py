""" Problem 47: Distinct Primes Factors

https://projecteuler.net/problem=47

Goal: Find the 1st integers (must be <= N) of K consecutive integers, that have
exactly K distinct prime factors.

Constraints: 20 <= N <= 2e6, 2 <= K <= 4

Distinct Prime Factors: The 1st 2 consecutive integers to have 2 distinct prime
factors are: :math:`14 \\gets 2 \\times 7, 15 \\gets 3 \\times 5`.
The 1st 3 consecutive integers to have 3 distinct prime factors are:
:math:`644 \\gets 2^2 \\times 7,
645 \\gets 3 \\times 5 \\times 43,
646 \\gets 2 \\times 17 \\times 19`.

e.g.: N = 20, K = 2
      result = {14, 20}
      N = 644, K = 3
      result = {644}
"""
from util.maths.reusable import prime_factors, is_prime


def count_prime_factors(n: int) -> list[int]:
    """ Modified prime_factors() helper method.

    :returns: List of amount of distinct prime factors for every N, where N = index.
    """

    count = [0]*(n + 1)
    for i in range(2, n + 1):
        if count[i] == 0:
            for j in range(i, n + 1, i):
                count[j] += 1
    return count


def consecutive_distinct_primes(n: int, k: int) -> list[int]:
    """
    Solution could be integrated with the above helper function by looping only
    once through the range(n + k) and performing both functions' tasks in an 'if'
    block, branched based on whether the list element == k.
    """

    first_consecutive = []
    # extend k-above limit to account for k-consecutive runs
    factor_counts = count_prime_factors(n + k)
    count = 0
    for composite in range(14, n + k):
        if factor_counts[composite] != k:
            count = 0
            continue
        count += 1
        if count >= k:
            first_consecutive.append(composite - k + 1)
    return first_consecutive


def first_4_distinct_primes() -> int:
    """
    Project Euler specific implementation that returns the 1st integer of the 1st
    4 consecutive numbers that have 4 distinct prime factors.

    The minimum representation with 4 distinct prime factors is:

    :math:`2 \\times 3 \\times 5 \\times 7 = 210`.
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
