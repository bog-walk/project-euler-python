""" Problem 97: Large Non-Mersenne Prime

https://projecteuler.net/problem=97

Goal: Return the last 12 digits of a very large number of the form A * (B^C) + D.
If this amount is less than 1e12, return the output padded with leading zeroes.

Constraints: 1 <= A, B, C, D <= 1e9

Mersenne Prime: A prime number that is 1 less than a power of 2, of the form
M_n = (2^n) - 1. For this number to be prime, n must also be prime. The 1st few
Mersenne primes are 3, 7, 31, 127, 8191 corresponding to n = 2, 3, 5, 7, 13. The
1st known prime to exceed 1e6 digits is a Mersenne prime of the form
(2^6_972_593) - 1, which contains exactly 2_098_960 digits.

e.g.: A = 2, B = 3, C = 4, D = 5
      2 * (3^4) + 5 = 167
      output = "000000000167"
"""

modulo = 1_000_000_000_000


def tail_of_very_large_num_opt(a: int, b: int, c: int, d: int) -> str:
    """ Solution optimised by using built-in pow(base, exp, mod).

    SPEED (BETTER)
            2.0e+04ns for PE problem.
    """

    power = pow(b, c, modulo)
    result = a * power + d
    return str(result % modulo).rjust(12, '0')


def tail_of_very_large_num(a: int, b: int, c: int, d: int) -> str:
    """
    Solution is similar to Problem 13's RTL manual addition, except that there is
    no need to iterate more than 12 times since only the last 12 digits are required.

    SPEED (WORSE)
            109.25s for PE problem.
    """

    power = str(pow(b, c))[-12:].rjust(12, '0')
    extra = str(d).rjust(12, '0')
    tail = [0] * 12
    carry_over = 0
    for i in range(11, -1, -1):
        total = a * int(power[i]) + int(extra[i]) + carry_over
        tail[i] = total % 10
        carry_over = total // 10

    return "".join(map(str, tail))


def tail_sum_of_very_large_nums(inputs: list[list[str]]) -> str:
    """
    HackerRank specific implementation that requires the last 12 digits of the sum
    of multiple very large numbers resulting from expressions of the form
    a * b^c + d.
    """

    total = 0

    for i in inputs:
        a, b, c, d = map(int, i)
        power = pow(b, c, modulo)
        total += (a * power + d) % modulo
        # could perform a third modulo here but this significantly
        # reduces performance

    return str(total % modulo).rjust(12, '0')


def tail_of_non_mersenne_prime(use_manual: bool = False) -> str:
    """
    Project Euler specific implementation that requires the last 10 digits of the
    massive non-Mersenne prime of the form 28433 * (2^7_830_457) + 1,
    which contains 2_357_207 digits.
    """

    a, b, c, d = 28433, 2, 7_830_457, 1
    if use_manual:
        return tail_of_very_large_num(a, b, c, d)[-10:]
    else:
        return tail_of_very_large_num_opt(a, b, c, d)[-10:]
