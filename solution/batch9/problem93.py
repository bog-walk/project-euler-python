""" Problem 93: Arithmetic Expressions

https://projecteuler.net/problem=93

Goal: Distinct positive integer outcomes can be achieved from expressions created
using a set of M distinct digits, each used exactly once with any of the operators
+, -, *, /, as well as parentheses. Find the largest possible integer N, such that
[1, N] is expressible. If 1 is not even a possible outcome, return 0.

Constraints: 1 <= M <= 5

e.g.: M = 2 -> {2, 8}
      outcomes = {8/2, 8-2, 2+8, 2*8} = {4, 6, 10, 16}
      output = 0

      M = 2 -> {1, 2}
      outcomes = {1+2, 2-1, 1*2 or 2/1} = {3, 1, 2}
      output = 3
"""
from fractions import Fraction
from itertools import combinations


def highest_streak(digits: list[int]) -> int:
    """
    Recursive solution repeatedly reduces the number of digits in the set by
    evaluating all possible expressions between different combinations of 2 digits
    in the set. The digits are treated as Fractions to avoid any floating-point
    issues.

    Note that non-commutative operations have to be performed twice to account for
    the alternative ordered combinations.

    N.B. Cache size was initially calculated using the product of the M largest
    digits:
            listOf(5, 6, 7, 8, 9).takeLast(m).reduce { acc, d -> acc * d })

    Exhaustive search showed that this was excessive as, while these maximum
    values are achievable, the longest streaks barely make it a fraction of the way:
            1 digit -> 1
            2 digits -> 3
            3 digits -> 10
            4 digits -> 51
            5 digits -> 192

    :param digits: List of unique digits sorted in ascending order.
    """

    max_cache = 200
    expressed = [False]*max_cache  # value 1 at index 0

    def evaluate_expression(nums: list[Fraction]):
        if len(nums) == 1:
            final_num, final_denom = nums[0].as_integer_ratio()
            if final_denom == 1 and final_num in range(1, max_cache + 1):
                expressed[final_num - 1] = True
        else:
            for i in range(len(nums)-1):
                for j in range(i+1, len(nums)):
                    new_nums = nums.copy()
                    y = new_nums.pop(j)
                    x = new_nums.pop(i)
                    # commutative operators
                    new_nums.append(x + y)
                    evaluate_expression(new_nums)
                    new_nums[-1] = x * y
                    evaluate_expression(new_nums)
                    # non-commutative operators
                    new_nums[-1] = x - y
                    evaluate_expression(new_nums)
                    new_nums[-1] = y - x
                    evaluate_expression(new_nums)
                    if y != Fraction():
                        new_nums[-1] = x / y
                        evaluate_expression(new_nums)
                    if x != Fraction():
                        new_nums[-1] = y / x
                        evaluate_expression(new_nums)

    evaluate_expression(list(map(Fraction, digits)))
    # index of first false means end of streak comes at previous index
    return expressed.index(False)


def longest_streak_set(m: int = 4) -> str:
    """
    Project Euler specific implementation that returns a String representation of
    the set of digits that can express the longest streak of positive integers.

    Note that, including the digit 0 would have resulted in 210 4-digit
    combinations instead of 126. It was left out because exhaustive search showed
    that [1, 2] was the longest streak achievable by a 4-digit set that includes 0.
    """

    highest, longest_streak = 0, ""
    for digit_combo in combinations(range(1, 10), m):
        combo_high = highest_streak(list(digit_combo))
        if combo_high > highest:
            highest, longest_streak = combo_high, "".join(map(str, digit_combo))
    return longest_streak
