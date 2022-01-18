""" Problem 35: Circular Primes

https://projecteuler.net/problem=35

Goal: Find the sum of all circular primes less than N, with rotations allowed to
exceed N, & the rotations themselves allowed as duplicates if below N.

Constraints: 10 <= N <= 1e6

Circular Prime: All rotations of the number's digits are themselves prime.
e.g. 197 -> {197, 719, 971}.

e.g.: N = 100
      circular primes = {2,3,5,7,11,13,17,31,37,71,73,79,97}
      sum = 446
"""
from util.maths.reusable import prime_numbers, is_prime
from util.search.reusable import binary_search


def get_rotations(num: str) -> {int, ...}:
    r = len(num)
    rotations = set(int(num[-i:] + num[:r - i]) for i in range(1, r))
    return {int(num)}.union(rotations)


def get_circular_primes(n: int) -> list[int]:
    """
    Solution is optimised by filtering out primes with any even digits as an even
    digit means at least 1 rotation will be even and therefore not prime. The
    primes list is also searched using a binary search algorithm.
    """

    primes = [2] + [
        p for p in prime_numbers(n - 1) if not set(str(p)).intersection("02468")
    ]
    if n == 10:
        return primes
    circular_primes = []
    for prime in primes:
        if prime < 10:
            circular_primes.append(prime)
            continue
        p_rotated = get_rotations(str(prime))
        # avoid duplicates & non-primes
        if any(
                r in circular_primes or
                r < n and not binary_search(r, primes) or
                not is_prime(r)
                for r in p_rotated
        ):
            continue
        # using append would insert a list object, not destructured list elements
        circular_primes += [r for r in p_rotated if r < n]
    return circular_primes


def sum_circular_primes(n: int) -> int:
    return sum(get_circular_primes(n))
