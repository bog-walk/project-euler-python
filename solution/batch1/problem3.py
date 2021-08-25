""" Problem 3: Largest Prime Factor

https://projecteuler.net/problem=3

Goal: Find the largest prime factor of N.

Constraints: 10 <= N <= 1e12

Fundamental Theorem of Arithmetic: There will only ever be a
unique set of prime factors for any number.

e.g.: N = 10
      prime factors = {2, 5}
      largest = 5
"""
import math


def largest_prime_factor(n):
    """
    Returns largest prime factor of n.

    Only tests factor 2, then every odd factor up to sqrt(n)
    as 2 is the only even prime number. sqrt(n) is the last checked as
    there can be at most 1 prime factor greater than sqrt(n) if n is
    not a prime.
    """
    largest = 2
    factors = [2]
    factors.extend(range(3, int(math.sqrt(n)) + 1, 2))
    for factor in factors:
        while n % factor == 0:
            largest = factor
            n /= factor
    if n > 2:
        largest = max(int(n), largest)
    return largest


def largest_prime_factor_recursive(n, f=2):
    factors = [2]
    factors.extend(range(3, int(math.sqrt(n)) + 1, 2))
    for factor in factors:
        if n % factor == 0:
            f = factor
            return largest_prime_factor_recursive(n / factor, f)
    if n > 2:
        f = max(f, int(n))
    return f
