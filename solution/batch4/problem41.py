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
from util.maths.reusable import is_prime_mr, prime_numbers
from util.strings.reusable import is_pandigital


def largest_pandigital_prime_brute() -> int:
    """
    Project Euler specific implementation that returns the largest n-digit
    pandigital prime that exists. This solution checks primality of all pandigital
    permutations backwards starting from 9 digits.

    Note that there are only 538 pandigital primes & that they are all either
    4-/7-digit pandigitals, as explained in following function below.
    """

    magnitudes = [pow(10, d - 1) for d in range(1, 10)]
    n, digits = 987_654_321, 9
    limit = magnitudes[digits - 1]
    while True:
        if is_pandigital(str(n), digits) and is_prime_mr(n):
            return n
        n -= 2
        if n < limit:
            digits -= 1
            limit = magnitudes[digits - 1]


def all_pandigital_primes_builtin() -> list[int]:
    """
    Solution optimised based on the following:

    -   The smallest pandigital prime is 4-digits -> 1423.

    -   Found using the brute force backwards search in the function above, the
        largest pandigital prime is 7-digits -> 7_652_413.

    -   The above 2 proven bounds confirm that only 4- & 7-digit pandigitals can
        be prime numbers as all primes greater than 3 are of the form 6*p(+/- 1) & so
        cannot be multiples of 3. If the sum of a pandigital's digits is a multiple
        of 3, then that number will be a multiple of 3 & thereby not a prime. Only
        4- & 7-digit pandigitals have sums that are not divisible by 3.

    SPEED (BETTER)
        68.37ms to generate all pandigital primes

    :returns: List of all pandigital primes sorted in descending order.
    """

    pandigital_primes = []
    # create reversed list to find larger permutations first
    digits = [str(d) for d in range(7, 0, -1)]
    for _ in range(2):
        # permutations() returns a sorted list of tuples
        for perm in map("".join, permutations(digits)):
            n_perm = int(perm)
            if is_prime_mr(n_perm):
                pandigital_primes.append(n_perm)
        digits = digits[3:]
    return pandigital_primes


def all_pandigital_primes() -> list[int]:
    """
    Alternative to the above solution that, instead of using itertools.permutations(),
    generates and filters prime numbers (using helper Sieve) under the optimised
    limits if they are also pandigital.

    SPEED (WORSE)
        2.81s to generate all pandigital primes

    :returns: List of all pandigital primes sorted in descending order.
    """

    return [
        p
        for p in prime_numbers(7654321)[::-1]
        if p > pow(10, 6) and is_pandigital(str(p), 7) or
        4321 >= p > 1000 and is_pandigital(str(p), 4)
    ]


def largest_pandigital_prime(n: int) -> int:
    if n < 1423:
        return -1
    else:
        return min(all_pandigital_primes_builtin(), key=lambda p: p > n)
