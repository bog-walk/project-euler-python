"""Problem 7: The 10001st Prime

https://projecteuler.net/problem=7

Goal: Find the Nth prime number.

Constraints: 1 <= N <= 10001

e.g.: N = 6
      primes = {2,3,5,7,11,13,...}
      6th prime = 13
"""
from util.maths.reusable import is_prime


def nth_prime(n):
    """
    This function can be modified to return the first N prime numbers,
    by declaring & initiating an array with the value 2, removing the 1st 'if'
    block, & appending new prime values in the 2nd 'if' block.
    """
    if n == 1:
        return 2
    count, number = n - 1, 1
    while count > 0:
        number += 2
        if is_prime(number):
            count -= 1
    return number
