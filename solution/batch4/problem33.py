""" Problem 33: Digit Cancelling Fractions

https://projecteuler.net/problem=33

Goal: Find every non-trivial fraction where the numerator is less than
the denominator (both have N-digits) and the value of the reduced fraction
(by cancelling K digits from num. & denom.) is equal to the original fraction.

Constraints: 2 <= N <= 4 & 1 <= K <= N-1

Non-Trivial Fraction: Satisfies goal's conditions, e.g. 49/98 = 4/8.
Trivial Fraction: Fractions with trailing zeroes in both
numerator and denominator that allow cancellation, e.g. 30/50 = 3/5.

 e.g.: N = 2, K = 1
       non-trivials = {16 / 64, 19 / 95, 26 / 65, 49 / 98}
       reduced-equivalents = {1 / 4, 1 / 5, 2 / 5, 4 / 8}
"""
from math import prod, gcd
from itertools import combinations


def is_reduced_equivalent(digits, numerator, denominator, to_cancel):
    n_mod = 10 ** to_cancel
    d_mod = 10 ** (digits - to_cancel)
    if numerator % n_mod == denominator // d_mod:
        og_fraction = numerator / denominator
        reduced = (numerator // n_mod) / (denominator % d_mod)
        return og_fraction == reduced
    return False


def find_non_trivials_brute(n, k) -> list[list[int]]:
    """
    SPEED: 22.1190s for N = 4, K = 1

    :return List of [numerator, denominator]s.
    """
    non_trivials = []
    # e.g. 2 digits has 11 as lowest numerator
    min_numerator = 10 ** (n - 1) + 1
    # e.g. 2 digits has 99 as lowest denominator (+1 for exclusive PY range)
    max_denominator = 10 ** n
    for numerator in range(min_numerator, max_denominator // 2):
        # Denominator must be greater than numerator
        for denominator in range(numerator + 1, max_denominator):
            # Avoid division by zero error
            if denominator % 10 == 0:
                continue
            if is_reduced_equivalent(n, numerator, denominator, k):
                non_trivials.append([numerator, denominator])
    return non_trivials


def find_non_trivials(n, k) -> list[list[int]]:
    """
    Rather than checking each brute iteration to see if cancelled digits match,
    limit loops by pre-cancelling possible digits, thereby pre-reducing all
    numerators & denominators, which reduces iteration by power of 10.

    Loop nesting is based on numerator < denominator & cancelled < max_cancelled.
    This order of solutions is based on the combination equation:
    ((10^k)*n + c) / ((10^k)*c + d) = n / d; which reduces to,
    ((10^k)-1)*n(c - d) = c*(d - n)

    SPEED (BEST for normal problem): 0.9368s for N = 4, K = 1

    :return List of [numerator, denominator]s.
    """
    non_trivials = []
    cancelled_min = 10 ** (k - 1)
    cancelled_max = 10 ** k
    reduced_min = 10 ** (n - k - 1)
    reduced_max = 10 ** (n - k)
    for cancelled in range(cancelled_min, cancelled_max):
        for denominator in range(reduced_min + 1, reduced_max):
            for numerator in range(reduced_min, denominator):
                num_adjusted = numerator * cancelled_max + cancelled
                denom_adjusted = cancelled * reduced_max + denominator
                if num_adjusted * denominator == numerator * denom_adjusted:
                    non_trivials.append([num_adjusted, denom_adjusted])
    return non_trivials


def product_of_non_trivials():
    """
    Project Euler specific implementation that required all non-trivial
    fractions that have 2 digits (pre-cancellation of 1 digit) to be found.

    :return: The denominator of the product of the fractions
    given in its lowest common terms.
    """
    non_trivials = find_non_trivials(2, 1)
    numerators, denominators = map(list, zip(*non_trivials))
    n_prod, d_prod = prod(numerators), prod(denominators)
    return d_prod // gcd(n_prod, d_prod)


def sum_of_non_trivials_brute(n, k):
    """
    HackerRank specific implementation that includes extra restrictions that
    are not clearly specified on the problem page:
    - The digits cancelled from the numerator and denominator can be in any order.
    e.g. 1306/6530 == 10/50 and 6483/8644 == 3/5.
    - Zeroes should not be cancelled, but leading zeroes are allowed as they will be
    read as if removed.
    e.g. 4808/8414 == 08/14 == 8/14 and 490/980 == 40/80.
    - Pre-cancelled fractions must only be counted once, even if the cancelled
    digits can be removed in different ways with the same output.
    e.g. 1616/6464 == 161/644 == 116/464.

    SPEED: s for N = 4, K = 1

    :return Tuple of (sum of numerators, sum of denominators).
    """
    # non_trivials = []
    n_sum, d_sum = 0, 0
    min_numerator = 10 ** (n - 1) + 2
    max_denominator = 10 ** n
    # max_denominator = 10 ** n // 3
    for numerator in range(min_numerator, max_denominator - 1):
        n_2 = str(numerator)
        cancel_combos = list(combinations([ch for ch in n_2 if ch != '0'], k))
        for denominator in range(numerator + 1, max_denominator):
            og_fraction = numerator / denominator
            for combo in cancel_combos:
                n_r = list(n_2)
                d_r = list(str(denominator))
                compatible = True
                found_non_trivial = False
                for digit in combo:
                    if digit in d_r:
                        n_r.remove(digit)
                        d_r.remove(digit)
                    else:
                        compatible = False
                        break
                if compatible:
                    num = int("".join(n_r))
                    denom = int("".join(d_r))
                    if denom == 0:
                        continue
                    if og_fraction == num / denom:
                        n_sum += numerator
                        d_sum += denominator
                        # non_trivials.append((numerator, denominator))
                        found_non_trivial = True
                if found_non_trivial:
                    break
    return n_sum, d_sum
    # return non_trivials


def sum_of_non_trivials_gcd(n, k):
    """
    HackerRank specific implementation, as above, but optimised through
    the use of gcd.

    SPEED: s for N = 4, K = 1

    :return Tuple of (sum of numerators, sum of denominators).
    """
    # non_trivials = []
    n_sum, d_sum = 0, 0
    min_numerator = 10 ** (n - 1)
    max_denominator = 10 ** n
    # max_denominator = 10 ** n // 3
    max_reduced = 10 ** (n - k)
    for numerator in range(min_numerator, max_denominator - 1):
        n_s = str(numerator)
        cancel_combos = list(combinations([ch for ch in n_s if ch != '0'], k))
        denominators_used = []
        for combo in cancel_combos:
            n_r = list(n_s)
            for c in combo:
                n_r.remove(c)
            n_2 = int("".join(n_r))
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
                d_r = list(str(d))
                for c in combo:
                    try:
                        d_r.remove(c)
                    except ValueError:
                        d_r = []
                        break
                if d_r == list(str(n_2)) and d not in denominators_used:
                    n_sum += numerator
                    d_sum += d
                    # non_trivials.append((numerator, d))
                    denominators_used.append(d)
    return n_sum, d_sum
    # return non_trivials


if __name__ == '__main__':
    brute = sum_of_non_trivials_brute(4, 1)
    gcd = sum_of_non_trivials_gcd(4, 1)
    print(len(brute))
    print(len(gcd))
