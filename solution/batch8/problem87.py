""" Problem 87: Prime Power Triples

https://projecteuler.net/problem=87

Goal: Count how many numbers <= N can be expressed as the sum of a prime square,
prime cube, and prime fourth power.

Constraints: 1 <= N <= 1e7

e.g.: N = 50
      28 = 2^2 + 2^3 + 2^4
      33 = 3^2 + 2^3 + 2^4
      49 = 5^2 + 2^3 + 2^4
      47 = 2^2 + 3^3 + 2^4
      count = 4
"""
from math import isqrt
from util.maths.reusable import prime_numbers


def all_prime_power_triple_counts(n: int) -> [int]:
    """
    Stores all cumulative counts for how many numbers <= index N can be expressed
    as a triple prime-powered sum.
    """

    triple = [False]*(n+1)
    primes = prime_numbers(isqrt(n))
    for a in primes:
        total_a = a**2
        for b in primes:
            total_b = total_a + b**3
            if total_b > n:
                break
            for c in primes:
                total_c = total_b + c**4
                if total_c > n:
                    break
                triple[total_c] = True

    count = 0
    all_counts = [0]*(n+1)
    for i, valid in enumerate(triple):
        count += 1 if valid else 0
        all_counts[i] = count

    return all_counts
