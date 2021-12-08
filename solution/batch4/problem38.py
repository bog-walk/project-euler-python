""" Problem 38: Pandigital Multiples

https://projecteuler.net/problem=38

Goal: Find all multipliers M below N that provide a K-pandigital
concatenated product when used with a multiplicand starting
with 1 onwards.

Constraints: 100 <= N <= 1e5 and K in {8, 9} and 1 < M

Pandigital Number: An N-digit number that uses all digits
from 1 to N exactly once, e.g. N = 5 -> 15234.

e.g.: N = 100, K = 8
      multipliers = {18, 78}, since:
      18 * (1, 2, 3, 4) -> 18|36|54|72
      78 * (1, 2, 3) -> 78|156|234
"""


def find_pandigital_multipliers(n, k):
    """
    Since a 9-digit pandigital number is the limit, the multiplier will
    never be larger than 4 digits (as a 5-digit number times 2 would give
    another 5-digit number).
    """
    multipliers = []
    limit = min(n, 10000)
    for num in range(9000, limit):
        concat = ""
        i = 1
        while len(concat) < k:
            product = str(num * i)
            if any(ch == "0" or ch > str(k) or ch in concat for ch in product):
                break
            if len(product) != len(set(product)):
                break
            concat += product
            i += 1
        if len(concat) == k:
            multipliers.append(num)
    return multipliers
