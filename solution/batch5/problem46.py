""" Problem 46: Goldbach's Other Conjecture

https://projecteuler.net/problem=46

Goal: Return the number of ways an odd composite number, N, can be
represented as proposed by Goldbach's Conjecture, detailed below.

Constraints: 9 <= N < 5e5

Goldbach's Proposed Conjecture: Every odd composite number can be written as
the sum of a prime and twice a square. Proven to be FALSE.
e.g. 9 = 7 + 2 * 1^2
     15 = 7 + 2 * 2^2 or 13 + 2 * 1^2
     21 = 3 + 2 * 3^2
     25 = 7 + 2 * 3^2
     27 = 19 + 2 * 2^2
     33 = 31 + 2 * 1^2

e.g.: N = 9
      result = 1
      N = 15
      result = 2
"""


def smallest_failing_num():
    """
    Project Euler specific implementation that returns the smallest odd
    composite that cannot be written, as proposed, as the sum of a prime and
    twice a square.
    """
    return -1
