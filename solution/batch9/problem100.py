""" Problem 100: Arranged Probability

https://projecteuler.net/problem=100

Goal: Find the first arrangement (of blue and red discs) to contain > D total
discs, where the probability of taking 2 blue discs is exactly P/Q. Output the
number of blue discs followed by the total amount of discs.

Constraints: 2 <= D <= 1e15, 0 < P < Q <= 1e7

e.g. A box has 21 total discs, of which 15 are blue and 6 are red. The probability
of taking 2 blue discs at random is P(BB) = 15/21 * 14/20 = 1/2. The next
arrangement to also have exactly 50% chance involves a box with 120 total discs, of
which 85 must be blue.

e.g.: D = 2, P/Q = 1/2
      output = 3 4
"""
from math import isqrt, sqrt


def get_next_arrangement(limit: int, p: int, q: int) -> tuple[str, str] | None:
    """
    Solution based on the equation:

            X^2 - X = p * (b^2 - b), where p = probability of picking 2 blue discs

    If a value of X is assumed (& valid), the value of b is found by solving for
    the positive integer solution of the quadratic equation:

            0 = b^2 - b - ((X^2 - X) / p)

    A quadratic solution is solved using the formula:

            (-b +/- sqrt(b^2 - 4ac)) / 2a, with a = 1, b = -1, and c = -(X^2 - X) / p

    Since the value of a and b never change & only the positive integer solution
    is required & c is always negative, the formula becomes:

            (1 + sqrt(4c + 1)) / 2

    This means that 2 requirements are needed for a positive solution to be possible:
        - 4c must be a whole positive integer to be a square number when incremented.
        - the square root must be odd to be divisible by 2 when incremented.

    Brute force of the solutions also brought to light that totalDiscs switched
    between even and odd values, with the first arrangement always having an even
    total, but this is only useful if generating all arrangements. Brute force
    also shows that some fractions (e.g. 1/2, 3/4, 11/12) can be easily found
    using the following:

            given initial values determined using the equations above:
            red_{n+1} = 2 * blue_n + red_n - 1
            blue_{n+1} = blue_n + (pNum + pDenom - 1) * red_{n+1}

    Certain fractions deviate from this norm (e.g. 3/8, 2/5) by toggling between
    2 distinct fractions to use in the multiplication, e.g.:

            given p = 3/8
            red_{n+1} = 2 * blue_n + red_n - 1
            blue_{n+1} = blue_n + (6/5 OR ~189/125) * red_{n+1}
    """

    blue_discs = 0
    max_total = pow(2, 63) - 1
    total_discs = limit + 1

    while total_discs < max_total:
        c, c_rem = divmod(total_discs * (total_discs - 1) * p, q)
        # must have integer value
        if not c_rem:
            base = 4 * c + 1
            root = sqrt(base)
            if root * root == base and root % 2 == 1:
                blue_discs = (int(root) + 1) // 2
                break
        total_discs += 1

    return None if not blue_discs else (str(blue_discs), str(total_discs))


def get_next_half_arrangement(limit: int) -> tuple[str, str]:
    """
    Original PE problem (p = 1/2) results in a known integer sequence of
    blueDiscs based on the solution to X(X-1) = 2b(b-1), such that:

            when p = 1/2 -> b(n) = 6b(n-1) - b(n-2) - 2, with b(0) = 1, b(1) = 3

    Some other fractions can be observed to follow a similar pattern:

            when p = 3/4 -> b(n) = 14b(n-1) - b(n-2) - 6
            when p = 5/7 -> b(n) = 12b(n-1) - b(n-2) - 5

    see here: https://oeis.org/A011900
    """

    if limit <= 3:
        return "3", "4"

    blue_n_minus_2, blue_n_minus_1 = 1, 3

    while True:
        blue_discs = 6 * blue_n_minus_1 - blue_n_minus_2 - 2
        rhs = 2 * blue_discs * (blue_discs - 1)
        root = isqrt(1 + 4 * rhs)
        total_discs = (1 + root) // 2
        blue_n_minus_2, blue_n_minus_1 = blue_n_minus_1, blue_discs
        if total_discs > limit:
            break

    return str(blue_discs), str(total_discs)
