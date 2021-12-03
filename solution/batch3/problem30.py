""" Problem 30: Digit Fifth Powers

https://projecteuler.net/problem=30

Goal: Calculate the sum of all numbers that can be written
as the sum of the Nth power of their digits.

Constraints: 3 <= N <= 6

e.g.: N = 4
      1634 = 1^4 + 6^4 + 3^4 + 4^4
      8208 = 8^4 + 2^4 + 0^4 + 8^4
      9474 = 9^4 + 4^4 + 7^4 + 4^4
      sum = 1634 + 8208 + 9474 = 19316
"""
from itertools import product


def digit_nth_powers_brute(n):
    """
    SPEED (BEST): 2.8226s for N = 6 
    """
    nums = []
    start = max(100, pow(10, n - 2))
    end = min(999999, pow(9, n) * n)
    for num in range(start, end):
        digits = num
        sum_of_powers = 0
        while digits:
            sum_of_powers += pow(digits % 10, n)
            if sum_of_powers > num:
                break  # only breaks while loop
            digits //= 10
        if sum_of_powers == num:
            nums.append(num)
    return nums


def digit_nth_powers_builtin(n):
    """
    Considers all combinations of digits (0-9 with replacement) for numbers
    of different lengths, using built-in functions.

    SPEED: 4.7851s for N = 6
    """
    nums = []
    min_digits = max(3, n - 2)
    max_digits = min(6, n + 1)
    for length in range(min_digits, max_digits + 1):
        for digits in product(range(10), repeat=length):
            combo_sum = sum((digit ** n for digit in digits))
            if str(combo_sum) == "".join(map(str, digits)):
                nums.append(combo_sum)
    return nums
