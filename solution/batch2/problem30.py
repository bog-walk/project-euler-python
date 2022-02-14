""" Problem 30: Digit Fifth Powers

https://projecteuler.net/problem=30

Goal: Calculate the sum of all numbers that can be written as the sum of the Nth
power of their digits.

Constraints: 3 <= N <= 6

e.g.: N = 4
      1634 = 1^4 + 6^4 + 3^4 + 4^4
      8208 = 8^4 + 2^4 + 0^4 + 8^4
      9474 = 9^4 + 4^4 + 7^4 + 4^4
      sum = 1634 + 8208 + 9474 = 19316
"""
from itertools import combinations_with_replacement


def digit_nth_powers_brute(n: int) -> list[int]:
    """
    SPEED (WORSE)
        1.10s for N = 6
    """

    nums = []
    powers = [pow(i, n) for i in range(10)]
    start = max(100, pow(10, n - 2))
    end = min(999_999, pow(9, n) * n)
    for num in range(start, end):
        digits = num
        sum_of_powers = 0
        while digits:
            sum_of_powers += powers[digits % 10]
            if sum_of_powers > num:
                break
            digits //= 10
        if sum_of_powers == num:
            nums.append(num)
    return nums


def digit_nth_powers_builtin(n: int) -> list[int]:
    """
    Considers all combinations of digits (0-9 with replacement) for max number of
    digits that allow valid candidates, using built-in
    combinations_with_replacement().

    This function returns all possible subsets, allowing element repetitions, but
    not allowing arrangements that are identical except for order. This will produce
    significantly fewer subsets than the built-in Cartesian product(), which does
    not differ between, e.g., 122 and 212. It is redundant to check both these
    numbers as both would return the same combo_sum (due to commutative addition).

    Instead, if the generated combo_sum itself produces an identical combo_sum,
    then it is a valid number to include in the sum.

    SPEED (BETTER)
        16.66ms for N = 6
    """

    nums = []
    powers = [pow(i, n) for i in range(10)]
    max_digits = n if n < 5 else 6
    for digits in combinations_with_replacement(range(10), max_digits):
        combo_sum = sum(powers[digit] for digit in digits)
        combo_sum_2 = sum(powers[int(digit)] for digit in str(combo_sum))
        if combo_sum == combo_sum_2 and combo_sum > 9:
            nums.append(combo_sum)
    return sorted(nums)
