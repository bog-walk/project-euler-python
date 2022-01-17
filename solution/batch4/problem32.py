""" Problem 32: Pandigital Products

https://projecteuler.net/problem=32

Goal: Find the sum of all products whose identity expression can be written as
an N-pandigital number.

Constraints: 4 <= N <= 9

Pandigital Number: An N-digit number that uses all digits from 1 to N exactly once,
e.g. N = 5 -> 15234.

Identity expression: 39(multiplicand) * 186(multiplier) = 7254(product).
Therefore, 7254 is a product of a pandigital identity expression.

e.g.: N = 4
      identities = {3 * 4 = 12}
      sum = 12
"""
from itertools import permutations
from util.strings.reusable import is_pandigital


def get_valid_product(n: int, permutation: (str, ...)) -> int:
    """
    :returns: Product of a valid identity expression if found, else 0.
    """

    # neither multiplicand nor multiplier can have more digits than product
    prod_d = 2 if n < 7 else 3 if n == 7 else 4
    # if multiplicand has 1 digit, it would be found at [:1]
    a = 1
    while a < 3:
        multiplicand = int("".join(permutation[:a]))
        # find start index of product based on multiplicand & product digits
        p_i = a + min(prod_d, n - prod_d - a)
        multiplier = int("".join(permutation[a:p_i]))
        product = int("".join(permutation[p_i:]))
        if multiplicand * multiplier == product:
            return product
        # expressions with < 7 digits can only have multiplier be 1 digit
        if n < 7:
            break
        a += 1
    return 0


def sum_pandigital_products(n: int) -> int:
    """
    Solution uses built-in permutations() to assess all arrangements of the
    required digits for a valid identity expression.

    SPEED (WORSE): 1.5490s for N = 9.
    """

    digits = [str(d) for d in range(1, n + 1)]
    # stored as set to ensure no duplicate permutation results
    return sum(
        {get_valid_product(n, perm) for perm in permutations(digits)}
    )


def sum_pandigital_products_brute(n: int) -> int:
    """
    Iterative solution assesses the pandigital quality of all identity expressions
    produced by multiplier, multiplicand combinations within a specified limit.

    SPEED (BETTER): 0.0834s for N = 9.
    """

    # stored as set to ensure no duplicate permutation results
    products = set()
    multiplier_max = 9 if n < 7 else 99
    product_max = pow(10, n // 2)
    for multiplier in range(2, multiplier_max):
        m_str = str(multiplier)
        multiplicand = multiplier + 1
        while True:
            product = multiplier * multiplicand
            if product >= product_max:
                break
            # ensure identity terms do not have duplicate digits
            if not any(d in m_str for d in str(multiplicand)):
                expression = f"{multiplier}{multiplicand}{product}"
                if is_pandigital(expression, n):
                    products.add(product)
            multiplicand += 1
    return sum(products)
