"""Problem 7: The 10001st Prime

https://projecteuler.net/problem=7

Goal: Find the Nth prime number.

Constraints: 1 <= N <= 10001

e.g.: N = 6
      primes = {2,3,5,7,11,13,...}
      6th prime = 13
"""
from math import sqrt, floor


def is_prime(n):
    if n < 2:
        return False
    elif n < 4:
        return True
    elif n % 2 == 0:
        return False
    elif n < 9:
        return True
    elif n % 3 == 0:
        return False
    else:
        step = 5
        while step <= floor(sqrt(n)):
            if n % step == 0 or n % (step + 2) == 0:
                return False
            step += 6
        return True


def nth_prime(n):
    if n == 1:
        return 2
    count, number = n - 1, 1
    while count > 0:
        number += 2
        if is_prime(number):
            count -= 1
    return number
