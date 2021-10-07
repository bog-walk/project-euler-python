""" Problem 25: N-digit Fibonacci Number

https://projecteuler.net/problem=25

Goal: Find the first term in the Fibonacci sequence to have N digits.

Constraints: 2 <= N <= 5000

e.g.: N = 3
      Fibonacci sequence = {0,1,1,2,3,5,8,13,21,34,55,89,144}
      first term with 3 digits = F(12)
"""


def n_digit_fib_terms(max_digits):
    """
    Returns list of the first Fibonacci terms to have (index + 2) digits.
    """
    term = 7
    f_n = 13
    terms = [0] * (max_digits - 1)
    terms[0] = term
    f_n_minus1 = 8
    digits = 3
    while digits <= max_digits:
        term += 1
        f_n_minus2, f_n_minus1 = f_n_minus1, f_n
        f_n = f_n_minus1 + f_n_minus2
        if len(str(f_n)) == digits:
            terms[digits - 2] = term
            digits += 1
    return terms
