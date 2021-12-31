""" Problem 13: Large Sum

https://projecteuler.net/problem=13

Goal: Find the first 10 digits of the sum of N 50-digit numbers.

Constraints: 1 <= N <= 1e3

e.g.: N.B. This is a scaled-down example (first 2 digits of N 5-digit numbers)
      N = 3
      34827, 93726, 90165
      sum = 218718
      1st 2 digits = 21
"""


def add_in_reverse(n, digits):
    """
    Simulates manual addition from RTL, as an alternative for simply
    adding the input (given Python's superior handling of larger numbers
    without overflow issues). See test cases for simple addition comparison.
    """
    if n == 1:
        return digits[0][:10]
    output = []
    carry_over = 0
    for i in range(len(digits[0]) - 1, -1, -1):
        total = sum([int(digits[j][i]) for j in range(n)]) + carry_over
        if len(output) >= 10:
            output.pop(0)
        output.append(str(total % 10))
        carry_over = total // 10
    while carry_over > 0:
        if len(output) >= 10:
            output.pop(0)
        output.append(str(carry_over % 10))
        carry_over //= 10
    return "".join(reversed(output))
