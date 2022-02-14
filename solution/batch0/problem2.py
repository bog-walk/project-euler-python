""" Problem 2: Even Fibonacci Numbers

https://projecteuler.net/problem=2

Goal: Find the sum of all even numbers in the Fibonacci sequence less than N.

Constraints: 10 <= N <= 4e16

e.g.: N = 44
      even fibonacci < N = {2, 8, 34}
      sum = 44
"""


def sum_even_fibs_brute(n: int) -> int:
    """
    Sums every 3rd term in the sequence starting with 2, based on the observed
    pattern that every 3rd Fibonacci number after 2 is even. This occurs because
    the sequence begins with 2 odd numbers, the sum of which must be even, then
    the sum of an odd and even number, twice, will produce 2 odd numbers, etc...

    SPEED (WORSE)
        1.2e4s for N = 4e16
    """

    sum_of_evens, odd2, odd1, even = 0, 1, 1, 2
    while even < n:
        sum_of_evens += even
        odd2 = odd1 + even
        odd1 = odd2 + even
        even = odd2 + odd1
    return sum_of_evens


def sum_even_fibs_formula(n: int) -> int:
    """
    Sums every 3rd term in the sequence starting with 2, using the formula:

    Fib(n) = 4Fib(n - 3) + Fib(n - 6)

    SPEED (BETTER)
        7600ns for N = 4e16
    """

    prev_even_2, prev_even_1 = 2, 8  # Fib(3), Fib(6)
    sum_of_evens = 10
    while True:
        current_even = 4 * prev_even_1 + prev_even_2
        if current_even >= n:
            break
        sum_of_evens += current_even
        prev_even_2, prev_even_1 = prev_even_1, current_even
    return sum_of_evens
