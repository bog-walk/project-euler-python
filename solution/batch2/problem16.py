""" Problem 16: Power Digit Sum

https://projecteuler.net/problem=16

Goal: Calculate the sum of the digits of the number 2^N.

Constraints: 1 <= N <= 1e4

e.g.: N = 9
      2^9 = 512
      sum = 5+1+2 = 8
"""


def exp_digit_sum_A(n):
    return sum(int(digit) for digit in str(pow(2, n)))


def exp_digit_sum_B(n):
    num = pow(2, n)
    total = 0
    # equivalent to while num != 0
    while num:
        total, num = total + num % 10, num // 10
    return total
