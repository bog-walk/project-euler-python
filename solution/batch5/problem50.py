""" Problem 50: Consecutive Prime Sum

https://projecteuler.net/problem=50

Goal: Return the smallest prime <= N that can be represented
as the sum of the longest consecutive prime sequence.

Constraints: 2 <= N <= 1e12

e.g.: N = 100
      sum = 41 -> 2 + 3 + 5 + 7 + 11 + 13
      length = 6
"""
from util.reusable import prime_numbers, is_prime


def consecutive_prime_sum(n) -> tuple[int, int]:
    limit = min(n, 1_000_000)
    primes = prime_numbers(limit)
    prime, longest = 2, 1
    for i in range(min(len(primes), 4)):
        total = primes[i]
        length = 1
        for j in range(i + 1, len(primes)):
            total += primes[j]
            length += 1
            if total > n:
                break
            if total < limit and total in primes or is_prime(total):
                if length > longest:
                    prime, longest = total, length
    return prime, longest
