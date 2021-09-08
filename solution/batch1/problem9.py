""" Problem 9: Special Pythagorean Triplet

https://projecteuler.net/problem=9

Goal: If there exists any Pythagorean triplet for which a + b + c = N,
find the maximum product among all such triplets, otherwise return -1.

Constraints: 1 <= N <= 3000

Pythagorean Triplet: a set of 3 natural numbers, such that
a < b < c && a^2 + b^2 = c^2.

e.g.: N = 12
      triplets = {{3,4,5}}; as 3 + 4 + 5 == 12
      product = 3*4*5 = 60
"""
from math import prod


def pythagorean_triplets(n: int) -> tuple:
    pass


def max_triplets_product(n):
    triplets = pythagorean_triplets(n)
    if triplets is None:
        return -1
    else:
        return max(prod(triplet) for triplet in triplets)
