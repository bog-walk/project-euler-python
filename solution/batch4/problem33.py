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

    SPEED: 0.9368s for N = 4, K = 1

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


def sum_of_non_trivials(n, k) -> tuple[int, int]:
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

    :return Tuple of (sum of numerators, sum of denominators).
    """
    n_sum, d_sum = 0, 0
    min_numerator = 10 ** (n - 1) + 2
    max_denominator = 10 ** n
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
                        found_non_trivial = True
                if found_non_trivial:
                    break
    return n_sum, d_sum


def sum_of_non_trivials_new(n, k) -> tuple[int, int]:
    """
    See comments extended in HR.
    """
    n_sum, d_sum = 0, 0
    min_numerator = 10 ** (n - 1) + 2
    max_denominator = 10 ** n
    for numerator in range(min_numerator, max_denominator - 1):
        n_s = str(numerator)
        cancel_combos = list(combinations([ch for ch in n_s if ch != '0'], k))
        for combo in cancel_combos:
            n_2 = int("".join(combo))
            g = gcd(numerator, n_2)
            
    return n_sum, d_sum


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


results = [
    (106, 265), (112, 616), (116, 464), (119, 595), (121, 220), (130, 325), (132, 231),
    (132, 330), (133, 532), (133, 931), (134, 335), (134, 536), (134, 737), (134, 938),
    (136, 238), (136, 340), (138, 345), (139, 695), (143, 242), (143, 341), (143, 440),
    (146, 365), (149, 298), (149, 596), (149, 894), (154, 253), (154, 352), (154, 451),
    (154, 550), (156, 858), (159, 795), (160, 640), (161, 644), (162, 648), (163, 652),
    (164, 656), (165, 264), (165, 363), (165, 462), (165, 561), (165, 660), (166, 664),
    (167, 668), (168, 672), (169, 676), (176, 275), (176, 374), (176, 473), (176, 572),
    (176, 671), (176, 770), (178, 979), (179, 895), (183, 732), (186, 465), (187, 286),
    (187, 385), (187, 484), (187, 583), (187, 682), (187, 781), (187, 880), (190, 950),
    (191, 955), (192, 960), (193, 965), (194, 291), (194, 970), (195, 390), (195, 975),
    (196, 294), (196, 392), (196, 490), (196, 980), (197, 394), (197, 591), (197, 985),
    (198, 297), (198, 396), (198, 495), (198, 594), (198, 693), (198, 792), (198, 891),
    (198, 990), (199, 398), (199, 597), (199, 796), (199, 995), (216, 864), (217, 775),
    (224, 728), (226, 565), (231, 330), (233, 932), (234, 936), (238, 340), (242, 341),
    (242, 440), (249, 498), (249, 996), (253, 352), (253, 451), (253, 550), (260, 650),
    (262, 655), (264, 363), (264, 462), (264, 561), (264, 660), (266, 665), (268, 469),
    (268, 670), (270, 756), (275, 374), (275, 473), (275, 572), (275, 671), (275, 770),
    (286, 385), (286, 484), (286, 583), (286, 682), (286, 781), (286, 880), (291, 970),
    (294, 392), (294, 490), (294, 980), (295, 590), (296, 592), (297, 396), (297, 495),
    (297, 594), (297, 693), (297, 792), (297, 891), (297, 990), (298, 596), (298, 894),
    (299, 598), (299, 897), (305, 854), (306, 765), (332, 830), (334, 835), (335, 536),
    (335, 737), (335, 938), (341, 440), (346, 865), (349, 698), (352, 451), (352, 550),
    (363, 462), (363, 561), (363, 660), (374, 473), (374, 572), (374, 671), (374, 770),
    (385, 484), (385, 583), (385, 682), (385, 781), (385, 880), (386, 965), (390, 975),
    (392, 490), (392, 980), (394, 591), (394, 985), (395, 790), (396, 495), (396, 594),
    (396, 693), (396, 792), (396, 891), (396, 990), (397, 794), (398, 597), (398, 796),
    (398, 995), (399, 798), (427, 976), (449, 898), (451, 550), (462, 561), (462, 660),
    (469, 670), (473, 572), (473, 671), (473, 770), (484, 583), (484, 682), (484, 781),
    (484, 880), (490, 980), (491, 982), (492, 984), (493, 986), (494, 988), (495, 594),
    (495, 693), (495, 792), (495, 891), (495, 990), (496, 992), (497, 994), (498, 996),
    (499, 998), (532, 931), (536, 737), (536, 938), (561, 660), (572, 671), (572, 770),
    (583, 682), (583, 781), (583, 880), (591, 985), (594, 693), (594, 792), (594, 891),
    (594, 990), (596, 894), (597, 796), (597, 995), (598, 897), (671, 770), (682, 781),
    (682, 880), (693, 792), (693, 891), (693, 990), (737, 938), (781, 880), (792, 891),
    (792, 990), (796, 995), (891, 990)]
