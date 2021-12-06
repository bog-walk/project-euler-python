""" Problem 35: Circular Primes

https://projecteuler.net/problem=35

Goal: Find the sum of all circular primes less than N, with rotations allowed
to exceed N & the rotation themselves allowed as duplicates if below N.

Constraints: 10 <= N <= 1e6

Circular Prime: All rotations of the number's digits are themselves prime.
e.g. 197 -> {197, 719, 971}.

e.g.: N = 100
      circular primes = {2,3,5,7,11,13,17,31,37,71,73,79,97}
      sum = 446
"""
from util.reusable import prime_numbers, is_prime


def get_rotations(num):
    rotations = {num}
    rotation = str(num)
    # number of possible rotations minus original already listed
    r = len(rotation) - 1
    for _ in range(r):
        rotation = rotation[r:] + rotation[:r]
        rotations.add(int(rotation))
    return rotations


def get_circular_primes(n) -> list[int]:
    """
    Solution optimised by first getting all primes less than N then filtering
    out primes with even digits as primes (other than 2) must be odd & an even
    digit means at least 1 rotation will be even.
    """
    primes = prime_numbers(n - 1)
    if n == 10:
        return primes
    rotations = primes[:4]
    for prime in primes[4:]:
        if any(d in "02468" for d in str(prime)):
            continue
        p_rotated = get_rotations(prime)
        if any(r in rotations for r in p_rotated):
            continue
        if any(r < n and r not in primes or not is_prime(r) for r in p_rotated):
            continue
        # using append would insert a list object, not destructured list elements
        rotations += [r for r in p_rotated if r < n]
    return rotations


def sum_circular_primes(n) -> int:
    """
    Increase this solution's efficiency by only using Sieve of Eratosthenes once
    to calculate all primes less than the upper constraint.
    """
    return sum(get_circular_primes(n))
