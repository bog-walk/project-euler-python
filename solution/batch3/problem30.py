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


def digit_nth_powers(n):
    nums = []
    start = pow(10, n - 2)
    end = pow(9, n) * n
    for num in range(start, end):
        digits = num
        total = 0
        while digits != 0:
            total += pow(digits % 10, n)
            if total > num:
                break  # only breaks while loop
            digits //= 10
        if total == num:
            nums.append(num)
    return nums
