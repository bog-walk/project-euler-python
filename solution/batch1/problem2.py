""" Problem 2: Even Fibonacci Numbers

https://projecteuler.net/problem=2

Goal: Find the sum of all even numbers in the Fibonacci sequence
less than N.

Constraints: 10 <= N <= 4e16

e.g.: N = 44
      even fibonacci < N = {2, 8, 34}
      sum = 44
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


def even_fibonacci_formula(n):
    """
    Uses the formula: Fib(n) = 4 * Fib(n-3) + Fib(n-6), to
    accumulate every 3rd fibonacci number starting with 2.

    Could be refactored to output all evens under N.
    """
    sum_of_evens = 10  # 10 <= N <= 4e16
    prev_even_2, prev_even_1 = 2, 8  # Fib(3), Fib(6)
    while True:
        current_even = 4 * prev_even_1 + prev_even_2
        if current_even >= n:
            break
        sum_of_evens += current_even
        prev_even_2, prev_even_1 = prev_even_1, current_even
    return sum_of_evens
