""" Problem 2: Even Fibonacci Numbers

https://projecteuler.net/problem=2

Goal: Find the sum of all even numbers in the Fibonacci sequence
less than N.

Constraints: 10 <= N <= 4e16.

e.g.: N = 44;
      even fibonacci < N = {2, 8, 34};
      sum = 44.
"""


def even_fibonacci_step(n):
    """
    Return sum of evens by stepping forward 3 times in the sequence.

    After 2, every 3rd Fibonacci number will be even.
    """
    sum_of_evens, odd2, odd1, even = 0, 1, 1, 2
    while even < n:
        sum_of_evens += even
        odd2 = odd1 + even
        odd1 = odd2 + even
        even = odd2 + odd1
    return sum_of_evens
