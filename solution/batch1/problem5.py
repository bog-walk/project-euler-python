""" Problem 5: Smallest Multiple

https://projecteuler.net/problem=5

Goal: Find the smallest positive number that can be evenly divided by
each number in the range(1, N+1).

Constraints: 1 <= N <= 40

e.g.: N = 3
      {1, 2, 3} evenly divides 6 to give quotient {6, 3, 2}
"""
from util.reusable import least_common_multiple
from functools import reduce


def lcm_of_range(range_max):
    """
    Find the least common multiple of the largest numbers in range, then
    continue to do so iterating backwards through range with 1 of the
    lcm parameters being the previously calculated lcm.
    """
    lcm = range_max
    for i in range(range_max, 0, -1):
        lcm = least_common_multiple(lcm, i)
    return lcm


def lcm_of_range_reduce(range_max):
    return reduce(least_common_multiple, range(range_max, 0, -1))
