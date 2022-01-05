""" Problem 27: Quadratic Primes

https://projecteuler.net/problem=27

Goal: Find coefficients a & b for the quadratic expression that produces
the maximum number of primes for consecutive values of n = 0..N.

Constraints: 42 <= N <= 2000

Quadratic Formula: n^2 + a*n + b, where |a| < N & |b| <= N.

Euler's Quadratic formula -> n^2 + n + 41, produces 40 primes
for the consecutive values of n = 0..39.
The formula -> n^2 - 79n + 1601, produces 80 primes for the
consecutive values of n = 0..79.

e.g.: N = 42
      formula -> n^2 - n + 41, produces 42 primes
      result = -1 41
"""
from util.maths.reusable import prime_numbers_og, is_prime


def quad_prime_coeff(max_n) -> tuple[int, int, int]:
    """
    Brute force of all a, b combinations optimised based on the following:
    - For n = 0, formula -> 0^2 + 0 + b = b, which means that
    b must be a prime number itself.
    - For n = 1, formula -> 1^2 + a + b, so with b being prime:
        - if b = 2, then a must be even for result to be an odd prime;
        - if b > 2, then a must be odd for result to be an odd prime.
    :return [tuple] -> (a, b, count_of_primes)
    """
    best_a, best_b, max_count = 0, 0, 0
    primes = prime_numbers_og(max_n)
    lowest_a = -max_n - 2 if max_n % 2 else -max_n - 1
    # a will only be even if b == 2, so loop through odd values only
    for a in range(lowest_a, max_n + 1, 2):
        for b in primes:
            n = 0
            adjusted_a = a if b != 2 else a - 1
            while is_prime(n * n + adjusted_a * n + b):
                n += 1
            if n > max_count:
                best_a, best_b, max_count = a, b, n + 1
    return best_a, best_b, max_count
