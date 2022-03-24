""" Problem 77: Prime Summations

https://projecteuler.net/problem=77

Goal: Count the number of ways that N can be written as the sum of 1 or more primes.

Constraints: 2 <= N <= 1000

EXTRA

e.g.: N = 5
      count = 2 -> {5, 3+2}
      N = 10
      count = 5 -> {7+3, 5+5, 5+3+2, 3+3+2+2, 2+2+2+2+2}
"""
from util.maths.reusable import prime_numbers


def all_prime_sum_combos(n: int) -> list[int]:
    """
    Solution is identical to the bottom-up approach that found the number of ways
    a total could be achieved, either using coins of different values (Batch 3 -
    Problem 31) or using combinations of lesser value positive integers (Batch 7 -
    Problem 76).

    :returns: List of prime partitions (mod 1e9 + 7) of all N <= limit, with
        index == N.
    """

    prime_combos_by_sum = [1] + [0]*n
    primes = prime_numbers(n)
    for prime in primes:
        for i in range(prime, n + 1):
            prime_combos_by_sum[i] += prime_combos_by_sum[i-prime]
    return prime_combos_by_sum


def first_prime_sum_combo() -> int:
    """
    Project Euler specific implementation that requests the first integer that
    can be written as the sum of primes in over 5000 different ways.
    """

    limit = 0
    while True:
        limit += 50
        all_counts = all_prime_sum_combos(limit)
        for i, count in enumerate(all_counts):
            if count > 5000:
                return i
