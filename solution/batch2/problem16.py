""" Problem 16: Power Digit Sum

https://projecteuler.net/problem=16

Goal: Calculate the sum of the digits of the number 2^N.

Constraints: 1 <= N <= 1e4

e.g.: N = 9
      2^9 = 512
      sum = 5+1+2 = 8
"""


def exp_digit_sum_iterative(n: int) -> int:
    """
    SPEED (WORSE): 6.62s for N = 1e4.
    """

    total = 0
    num = pow(2, n)
    # equivalent to while num != 0
    while num:
        total, num = total + num % 10, num // 10
    return total


def exp_digit_sum_builtin(n: int) -> int:
    """
    SPEED (BETTER): 6.5e5ns for N = 1e4.
    """

    return sum(map(int, str(pow(2, n))))
