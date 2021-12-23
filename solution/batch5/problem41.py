""" Problem 41: Pandigital Prime

https://projecteuler.net/problem=41

Goal: Find the largest pandigital prime <= N or return -1 if none exists.

Constraints: 10 <= N < 1e10

e.g.: N = 100
      return -1, as no 2-digit pandigital primes exist; however,
      N = 10_000
      return 4231, as the smallest pandigital prime.
"""
from itertools import permutations
from util.reusable import is_prime


def largest_pandigital_prime_brute():
    """
    Project Euler specific implementation that returns the largest
    n-digit pandigital prime that exists. This solution checks primality of all
    pandigital permutations backwards starting from 9 digits.

    Note that there are only 538 pandigital primes & that they are all either
    4-/7-digit pandigitals, as explained in next function.
    """
    digits = [str(d) for d in range(1, 10)]
    while True:
        # Could sort in reverse, but permutations already returns sorted list
        perms = list(map("".join, permutations(digits)))
        # Traverse backwards through already sorted list to get largest first
        for i in range(len(perms) - 1, -1, -1):
            perm = int(perms[i])
            if is_prime(perm):
                return perm
        digits = digits[:-1]


def all_pandigital_primes():
    """
    Solution optimised based on the following:

    - The smallest pandigital prime is 4-digits -> 1423.

    - Found using the brute backwards search through permutations in the function
    above, the largest pandigital prime is 7-digits -> 7652413.

    - The above 2 proven bounds confirms that only 4- & 7-digit pandigitals can
    be prime numbers as all primes greater than 3 are of the form 6*p(+/- 1) & so
    cannot be multiples of 3. If the sum of a pandigital's digits is a multiple
    of 3, then that number will be a multiple of 3 & thereby not a prime. Only
    4- & 7-digit pandigitals have sums that are not divisible by 3 (10 & 28 respectively).
    """
    pandigital_primes = []
    digits = [str(d) for d in range(1, 8)]
    for _ in range(2):
        perms = list(map("".join, permutations(digits)))
        for i in range(len(perms) - 1, -1, -1):
            n_perm = int(perms[i])
            if is_prime(n_perm):
                pandigital_primes.append(n_perm)
        digits = digits[:-3]
    return pandigital_primes


def largest_pandigital_prime_improved(n):
    """
    Consider increasing efficiency by pulling generation of all pandigital
    primes out into a global variable (if multiple test cases needed).
    """
    if n < 1423:
        return -1
    else:
        for prime in all_pandigital_primes():
            if prime <= n:
                return prime
