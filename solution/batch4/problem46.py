""" Problem 46: Goldbach's Other Conjecture

https://projecteuler.net/problem=46

Goal: Return the number of ways an odd composite number, N, can be represented as
proposed by Goldbach's Conjecture, detailed below.

Constraints: 9 <= N < 5e5

Goldbach's False Conjecture: Every odd composite number can be written as the sum
of a prime and twice a square. Proven to be FALSE.
e.g.: :math:`9 = 7 + 2 \\times 1^2`
      :math:`15 = 7 + 2 \\times 2^2 || 13 + 2 \\times 1^2`
      :math:`21 = 3 + 2 \\times 3^2 || 13 + 2 \\times 2^2 || 19 + 2 \\times 1^2`
      :math:`25 = 7 + 2 \\times 3^2 || 17 + 2 \\times 2^2 || 23 + 2 \\times 1^2`
      :math:`27 = 19 + 2 \\times 2^2`
      :math:`33 = 31 + 2 \\times 1^2`

e.g.: N = 9
      result = 1
      N = 15
      result = 2
"""
from math import floor, sqrt
from util.maths.reusable import is_prime, prime_numbers


def is_goldbach_2(composite: int, prime: int) -> bool:
    rep = sqrt((composite - prime) / 2)
    return rep == floor(rep)


def goldbach_repr(n: int) -> int:
    """
    :param n: An odd composite number (no in-built check to ensure it is not prime).
    :returns: Count of primes that return True (== 1) from is_goldbach_2() with
        the provided n.
    """

    return sum(is_goldbach_2(n, prime) for prime in prime_numbers(n)[1:])


def smallest_failing_num() -> int:
    """
    Project Euler specific implementation that returns the smallest odd composite
    that cannot be written, as proposed, as the sum of a prime and twice a square.

    The found value can be confirmed by using it as an argument in the HackerRank
    problem solution above, as seen in the test cases.
    """

    limit = 5000  # starting limit guessed with contingency block later down
    primes = prime_numbers(limit)[1:]
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
        else:
            # if reached, means not enough primes for current composite
            limit += 5000
            primes = prime_numbers(limit)[1:]
            composite -= 2
    return -1
