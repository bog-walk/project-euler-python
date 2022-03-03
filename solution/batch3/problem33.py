""" Problem 33: Digit Cancelling Fractions

https://projecteuler.net/problem=33

Goal: Find every non-trivial fraction where the numerator is less than the
denominator (both have N-digits) and the value of the reduced fraction (by
cancelling K digits from num. & denom.) is equal to the original fraction.

Constraints: 2 <= N <= 4 & 1 <= K <= N-1

Non-Trivial Fraction: Satisfies goal's conditions, e.g. 49/98 = 4/8.

Trivial Fraction: Fractions with trailing zeroes in both numerator and denominator
that allow cancellation, e.g. 30/50 = 3/5.

 e.g.: N = 2, K = 1
       non-trivials = {16 / 64, 19 / 95, 26 / 65, 49 / 98}
       reduced-equivalents = {1 / 4, 1 / 5, 2 / 5, 4 / 8}
"""
from itertools import combinations, product
from math import gcd, prod


def is_reduced_equivalent(
        digits: int, numerator: int, denominator: int, to_cancel: int
) -> bool:
    """
    Naive method checks if a reduced fraction is equivalent to its original fraction.
    """

    n_mod = pow(10, to_cancel)
    d_mod = pow(10, digits - to_cancel)
    if numerator % n_mod == denominator // d_mod:
        og_fraction = numerator / denominator
        reduced = (numerator // n_mod) / (denominator % d_mod)
        return og_fraction == reduced
    return False


def find_non_trivials_brute(n: int, k: int) -> list[(int, int)]:
    """
    Brute iteration through all numerators and denominators with the expected amount
    of digits, & following constraints specified in problem above.

    SPEED (WORSE for PE problem)
        27.44s for N = 4, K = 1

    :returns: List of tuples of (numerator, denominator) sorted by numerator.
    """

    non_trivials = []
    min_numerator = pow(10, n - 1) + 1
    max_denominator = pow(10, n)
    for numerator in range(min_numerator, max_denominator // 2):
        for denominator in range(numerator + 1, max_denominator):
            if denominator % 10 == 0:
                continue
            if is_reduced_equivalent(n, numerator, denominator, k):
                non_trivials.append((numerator, denominator))
    return non_trivials


def find_non_trivials(n: int, k: int) -> list[(int, int)]:
    """
    Solution limits loops by pre-cancelling possible digits, rather than checking
    each iteration to see if cancelled digits match. This pre-reduces all
    numerators & denominators, which reduces iteration by power of 10.

    Loop nesting is based on numerator < denominator & cancelled < max_cancelled.
    This order of solutions is based on the combination equation:

    (n10^k + c) / (c10^k + d) = n / d

    which reduces to:

    n(10^k - 1)(c - d) = c(d - n)

    SPEED (BETTER for PE problem)
        1.08s for N = 4, K = 1

    :returns: List of tuples of (numerator, denominator) sorted by numerator.
    """

    non_trivials = []
    cancelled_min = pow(10, k - 1)
    cancelled_max = pow(10, k)
    reduced_min = pow(10, n - k - 1)
    reduced_max = pow(10, n - k)
    for cancelled in range(cancelled_min, cancelled_max):
        for d_2 in range(reduced_min + 1, reduced_max):
            for n_2 in range(reduced_min, d_2):
                numerator = n_2 * cancelled_max + cancelled
                denominator = cancelled * reduced_max + d_2
                if n_2 * denominator == numerator * d_2:
                    non_trivials.append((numerator, denominator))
    return sorted(non_trivials)


def product_of_non_trivials() -> int:
    """
    Project Euler specific implementation that requires all non-trivial fractions
    that have 2 digits (pre-cancellation of 1 digit) to be found.

    :returns: The denominator of the product of the fractions given in their
        lowest common terms.
    """

    non_trivials = find_non_trivials(2, 1)
    numerators, denominators = map(list, zip(*non_trivials))
    n_prod, d_prod = prod(numerators), prod(denominators)
    return d_prod // gcd(n_prod, d_prod)


def get_cancelled_combos(num: str, combo: tuple[str]) -> {int, ...}:
    """
    Finds all combinations for digits cancelled from a number based on the indices
    of the digits to be cancelled. Ensures no combinations have duplicate digits
    or duplicate integer outputs.

    :returns: Set of {post-cancellation integers}.
    """

    # e.g. num = "9919" with cancel_combo = ('9','9')
    # indices = [[0,1,3], [0,1,3]]
    indices = [[i for i, d in enumerate(num) if d == ch] for ch in combo]
    perms = set()
    # all_combos = {0,1}, {0,3}, {1,0}, {1, 3}...; {0,0}...etc reduced to {0}
    all_combos = map(set, product(*indices))
    # remove combos that have been reduced due to duplicate indices
    combos_filtered = list(filter(lambda s: len(s) == len(combo), all_combos))
    for c in combos_filtered:
        # e.g. {0,1,2,3} - {0,1} = {2,3}
        post_cancel = set(range(len(num))) - c
        # above identical to "9919" becoming 19 post-cancellation
        perms.add(int("".join([num[i] for i in post_cancel])))
    # perms = {19, 91}, as set removes any duplicates
    return perms


def sum_of_non_trivials_brute(n: int, k: int) -> (int, int):
    """
    HackerRank specific implementation that includes extra restrictions that
    are not clearly specified on the problem page:

    -   The digits cancelled from the numerator and denominator can be in any
        order.
            e.g. 1306/6530 == 10/50 and 6483/8644 == 3/5.

    -   Zeroes should not be cancelled, but leading zeroes are allowed as they
        will be read as if removed.
            e.g. 4808/8414 == 08/14 == 8/14 and 490/980 == 40/80.

    -   Pre-cancelled fractions must only be counted once, even if the cancelled
        digits can be removed in different ways with the same output.
            e.g. 1616/6464 == 161/644 == 116/464.

    SPEED (WORSE for HR problem)
        1606.35s for N = 4, K = 1

    :returns: Tuple of (sum of numerators, sum of denominators).
    """

    n_sum, d_sum = 0, 0
    min_numerator = pow(10, n - 1) + 2
    max_denominator = pow(10, n)
    for numerator in range(min_numerator, max_denominator - 1):
        n_s = str(numerator)
        cancel_combos = set(combinations([ch for ch in n_s if ch != '0'], k))
        for denominator in range(numerator + 1, max_denominator):
            og_fraction = numerator / denominator
            for combo in cancel_combos:
                n_post = get_cancelled_combos(n_s, combo)
                d_post = get_cancelled_combos(str(denominator), combo)
                if len(d_post) == 0:
                    # denominator did not contain all digits to cancel
                    continue
                for n_2 in n_post:
                    if n_2 == 0:
                        continue
                    for d_2 in d_post:
                        # avoid division by zero error
                        if d_2 == 0:
                            continue
                        if og_fraction == n_2 / d_2:
                            n_sum += numerator
                            d_sum += denominator
                            break
                    else:
                        continue
                    # avoid duplicating numerator with this denominator
                    break
                else:
                    continue
                break
    return n_sum, d_sum


def sum_of_non_trivials_gcd(n: int, k: int) -> (int, int):
    """
    HackerRank specific implementation with extra restrictions, as detailed
    in the above brute force solution.

    This solution has been optimised by only looping through possible numerators
    & the cancellation combos they allow. Rather than loop through denominators,
    gcd() is used to assess reductive equivalence based on the following:

    n_og / d_og = n_r / d_r, and

    n_r = n_og / gcd(n_og, d_og)

    d_r = d_og / gcd(n_og, d_og)

    SPEED (BETTER for HR problem)
        1.86s for N = 4, K = 1

    :returns: Tuple of (sum of numerators, sum of denominators).
    """

    n_sum, d_sum = 0, 0
    min_numerator = pow(10, n - 1)
    max_denominator = pow(10, n)
    max_reduced = pow(10, n - k)
    for numerator in range(min_numerator, max_denominator - 1):
        n_s = str(numerator)
        cancel_combos = set(combinations([ch for ch in n_s if ch != '0'], k))
        # avoid denominator duplicates with same numerator
        denominators_used = []
        for combo in cancel_combos:
            # get all integers possible post-cancellation of k digits
            n_post = get_cancelled_combos(n_s, combo)
            for n_2 in n_post:
                if n_2 == 0:
                    continue
                d = numerator
                i = 1
                while True:
                    i += 1
                    g = gcd(d, n_2)
                    d, n_2 = (d // g) * i, (n_2 // g) * i
                    if d <= numerator:
                        continue
                    if n_2 >= max_reduced or d >= max_denominator:
                        break
                    d_post = get_cancelled_combos(str(d), combo)
                    # denominator did not contain all digits to cancel
                    if len(d_post) == 0:
                        continue
                    for d_2 in d_post:
                        if n_2 == d_2 and d not in denominators_used:
                            n_sum += numerator
                            d_sum += d
                            denominators_used.append(d)
    return n_sum, d_sum
