"""Problem 7: The 10001st Prime

https://projecteuler.net/problem=7

Goal: Find the Nth prime number.

Constraints: 1 <= N <= 10_001

e.g.: N = 6
      primes = {2,3,5,7,11,13,...}
      6th prime = 13
"""
from util.maths.reusable import is_prime


def nth_prime(n: int) -> int:
    """
    After the number 2, every prime number is odd, so this solution iterates over
    all odd numbers & checks for primality using an optimised helper function,
    until the nth prime is found.
    """
    if n == 1:
        return 2
    count, number = n - 1, 1
    while count > 0:
        number += 2
        if is_prime(number):
            count -= 1
    return number
