""" Problem 38: Pandigital Multiples

https://projecteuler.net/problem=38

Goal: Find all multipliers M below N that provide a K-pandigital concatenated
product when used with a multiplicand starting with 1 onwards.

Constraints: 100 <= N <= 1e5 and K in [8, 9] and 1 < M

e.g.: N = 100, K = 8
      multipliers = {18, 78}, since:
      18 * (1, 2, 3, 4) -> 18|36|54|72
      78 * (1, 2, 3) -> 78|156|234
"""
from util.strings.reusable import is_pandigital


def find_pandigital_multipliers(n: int, k: int) -> list[int]:
    """
    Since a 9-digit pandigital number is the limit, the multiplier will never be
    larger than 4 digits (as a 5-digit number times 2 would produce another 5-digit
    number).

    N.B. The logic behind the inner loop break could all be replaced by the
    is_pandigital() helper function used in the PE implementation at the bottom.
    """

    multipliers = []
    limit = min(n, 9876)
    for num in range(2, limit):
        concat = ""
        i = 1
        while len(concat) < k:
            product = str(num * i)
            # ensure result only 1 to k pandigital
            if any(ch == "0" or ch > str(k) or ch in concat for ch in product):
                break
            # avoid products that contain duplicate digits
            if len(product) != len(set(product)):
                break
            concat += product
            i += 1
        if len(concat) == k:
            multipliers.append(num)
    return multipliers


def largest_9_pandigital() -> str:
    """
    Project Euler specific implementation that finds the largest 1 to 9 pandigital
    number that can be formed as a concatenated product.

    Solution is based on the following:

    -   Since the multiplier must at minimum be multiplied by both 1 & 2, it cannot
        be larger than 4 digits to ensure product is only 9 digits.

    -   The default largest would be M = 9 * (1, 2, 3, 4, 5) = 918_273_645, so M must
        begin with the digit 9.

    -   The 2-digit minimum (M = 91) would result in either an 8-/11-digit product
        once multiplied by 3 and 4. The 3-digit minimum (M = 912) would result in
        either a 7-/11-digit product once multiplied by 2 and 3.

    -   So M must be a 4-digit number multiplied by 2 to get a 9-digit product and
        at minimum will be 9182 (1st 4 digits of default) and at max 9876.

    -   Multiplying 9xxx by 2 will at minimum result in 18xxx, always generating a
        new digit 1, so M cannot itself contain the digit 1, setting the new minimum
        to 9234.

    -   Lastly, multiplying [98xx, 95xx, -1] by 2 will at minimum result in
    19xxx,
        always generating another digit 9, so M's 2nd digit must be < 5, setting the
        new maximum to 9487.
    """

    largest = ""
    for m in range(9487, 9234, -1):
        largest = str(m) + str(m * 2)
        if is_pandigital(largest, 9):
            break
    return largest
