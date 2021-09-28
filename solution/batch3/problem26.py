""" Problem 26: Reciprocal Cycles

https://projecteuler.net/problem=26

Goal: Find the value of the smallest d less than N for which
1/d contains the longest recurring cycle in its decimal fraction part.

Constraints: 4 <= N <= 1e4

e.g.: N = 10
      1/2 = 0.5
      1/3 = 0.(3) -> 1-digit recurring cycle
      1/4 = 0.25
      1/5 = 0.2
      1/6 = 0.1(6) -> 1-digit recurring cycle
      1/7 = 0.(142857) -> 6-digit recurring cycle
      1/8 = 0.125
      1/9 = 0.(1) -> 1-digit recurring cycle
      result = 7
"""
from util.reusable import prime_numbers


def longest_repetend_denominator_primes(n):
    primes = [x for x in prime_numbers(n - 1) if x not in [2, 3, 5]]
    d = 3
    longest_k = 1
    for p in primes:
        for k in range(1, p):
            if (pow(10, k) - 1) % p == 0:
                if k > longest_k:
                    longest_k = k
                    d = p
                break
    return d


def longest_repetend_denominator(n):
    """
    Significantly faster than above solution.
    """
    longest_k = 0
    d = n
    upper_n = n - 1 if n % 2 == 0 else n - 2
    lower_n = upper_n // 2 - 1
    for i in range(upper_n, lower_n, -2):
        if longest_k >= i:
            break
        remainders = [0]*i
        remainder = 1
        position = 0
        while remainders[remainder] == 0 and remainder != 0:
            remainders[remainder] = position
            remainder = (remainder * 10) % i
            position += 1
        if position - remainders[remainder] >= longest_k:
            longest_k = position - remainders[remainder]
            d = i
    return d


if __name__ == '__main__':
    print(longest_repetend_denominator(15))
