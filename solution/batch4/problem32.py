""" Problem 32: Pandigital Products

https://projecteuler.net/problem=32

Goal: Find the sum of all products whose identity expression
can be written as an N-pandigital number.

Constraints: 4 <= N <= 9

Pandigital Number: An N-digit number that uses all digits
from 1 to N exactly once, e.g. N = 5 -> 15234.

Identity expression: 39(multiplicand) * 186(multiplier) = 7254(product).
Therefore, 7254 is a product of a pandigital identity expression.

e.g.: N = 4
      identities = {3 * 4 = 12}
      sum = 12
"""
from itertools import permutations


def get_valid_product(n, permutation):
    # neither multiplicand nor multiplier can have more digits than product
    prod_d = 2 if n < 7 else 3 if n == 7 else 4
    # if multiplicand has 1 digit, it would be found at [:1]
    a = 1
    while True:
        multiplicand = int("".join(permutation[:a]))
        # find start index of product based on multiplicand & product digits
        p_i = a + min(prod_d, n - prod_d - a)
        multiplier = int("".join(permutation[a:p_i]))
        product = int("".join(permutation[p_i:]))
        if multiplicand * multiplier == product:
            return product
        if n < 7 or a == 2:
            return 0
        # higher N means multiplicand can also have 2 digits
        a += 1


def sum_pandigital_products(n):
    digits = [str(d) for d in range(1, n + 1)]
    # set() to ensure no duplicate permutation results
    return sum(
        {get_valid_product(n, perm) for perm in permutations(digits)}
    )
