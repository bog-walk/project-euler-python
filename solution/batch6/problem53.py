""" Problem 53: Combinatoric Selections 

https://projecteuler.net/problem=53

Goal: Count the values of n_C_r, for 1 <= n <= N, that are
greater than K. Values do not have to be distinct.

Constraints: 2 <= N <= 1000, 1 <= K <= 1e18

Combinatorics: n_C_r = n! / (r! * (n - r)!), where r <= n.
There are 10 combinations when 3 digits are chosen from 5 digits.
It is not until n = 23 that the amount of combinations first
exceeds 1e6, namely 23_C_10 = 1_144_066.

e.g.: N = 23, K = 1e6
      answer = 4
"""
from math import factorial


factorials = [factorial(i) for i in range(1001)]


def get_combinatorics(n, r):
    return factorials[n] // (factorials[r] * factorials[n - r])


def count_large_combinatorics(n, k):
    count = 0
    while n > 0:
        for r in range(1, n):
            if get_combinatorics(n, r) > k:
                count += 1
        n -= 1
    return count


if __name__ == '__main__':
    print(count_large_combinatorics(23, 1_000_000))
