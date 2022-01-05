""" Problem 46: Goldbach's Other Conjecture

https://projecteuler.net/problem=46

Goal: Return the number of ways an odd composite number, N, can be
represented as proposed by Goldbach's Conjecture, detailed below.

Constraints: 9 <= N < 5e5

Goldbach's False Conjecture: Every odd composite number can be
written as the sum of a prime and twice a square. Proven to be FALSE.
e.g. 9 = 7 + 2 * 1^2
     15 = 7 + 2 * 2^2 or 13 + 2 * 1^2
     21 = 3 + 2 * 3^2 or 13 + 2 * 2^2 or 19 + 2 * 1^2
     25 = 7 + 2 * 3^2 or 17 + 2 * 2^2 or 23 + 2 * 1^2
     27 = 19 + 2 * 2^2
     33 = 31 + 2 * 1^2

e.g.: N = 9
      result = 1
      N = 15
      result = 2
"""
from math import sqrt, floor
from util.maths.reusable import is_prime, prime_numbers


def is_goldbach_2(composite, prime):
    rep = sqrt((composite - prime) / 2)
    return rep == floor(rep)


def goldbach_repr(n):
    """
    :param n: An odd composite number (no in-built check
    for primality).
    """
    primes = prime_numbers(n)[1:]
    count = 0
    for prime in primes:
        if is_goldbach_2(n, prime):
            count += 1
    return count


def smallest_failing_num():
    """
    Project Euler specific implementation that returns the smallest odd
    composite that cannot be written, as proposed, as the sum of a prime
    and twice a square.
    """
    primes = prime_numbers(10000)[1:]
    composite = 33  # starting point as provided in example
    while True:
        composite += 2
        if is_prime(composite):
            continue
        for prime in primes:
            if prime > composite:
                return composite
            if is_goldbach_2(composite, prime):
                break
    return -1
