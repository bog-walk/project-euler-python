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


def largest_pandigital_prime_to_exist():
    """
    Project Euler specific implementation that returns the largest
    n-digit pandigital prime that exists. This solution checks primality of all
    pandigital permutations backwards starting from 9 digits.

    Note that there are only 538 pandigital primes & that they are all either
    4-/7-digit pandigitals, as explained in next function.
    """
    digits = [str(d) for d in range(1, 10)]
    while True:
        perms = sorted(list(map("".join, permutations(digits))), reverse=True)
        for perm in perms:
            if is_prime(int(perm)):
                return int(perm)
        digits = digits[:-1]
        if len(digits) == 4:
            return 4231


def largest_pandigital_prime(n):
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
    if n < 1423:
        return -1
    digits = [str(d) for d in range(1, 8)]
    while True:
        perms = sorted(list(map("".join, permutations(digits))), reverse=True)
        for perm in perms:
            n_perm = int(perm)
            if n_perm > n:
                continue
            if is_prime(n_perm):
                return n_perm
        digits = digits[:-3]


if __name__ == '__main__':
    for p in list(map("".join, permutations(['1', '2', '3', '4']))):
        if is_prime(int(p)):
            print(p)

