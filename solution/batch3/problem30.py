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
from itertools import combinations_with_replacement


def digit_nth_powers_brute(n):
    nums = []
    start = max(100, pow(10, n - 2))
    end = min(999999, pow(9, n) * n)
    for num in range(start, end):
        digits = num
        sum_of_powers = 0
        while digits > 0:
            sum_of_powers += pow(digits % 10, n)
            if sum_of_powers > num:
                break  # only breaks while loop
            digits //= 10
        if sum_of_powers == num:
            nums.append(num)
    return nums


def digit_nth_powers_combo(n):
    """
    Considers all combinations of digits (0-9 with replacement) for numbers
    of different lengths.
    """
    answer = 0
    min_digits = max(3, n - 2)
    max_digits = min(6, n + 1)
    for length in range(min_digits, max_digits + 1):
        for digits in combinations_with_replacement(range(10), length):
            mapped_value = sum((digit ** n for digit in digits))
            if tuple(sorted(digits_of(mapped_value))) == digits and num_digits(mapped_value) == n:
                answer += mapped_value
    return answer
