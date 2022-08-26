""" Problem 86: Cuboid Route

https://projecteuler.net/problem=86

Goal: Find the number of distinct cuboids (ignoring rotations) that can be formed
(with integer dimensions and shortest route with integer length) up to a maximum
size of MxMxM.

Constraints: A <= M && B <= M && C <= M
             1 <= M <= 4e5

This is based on the premise that a spider can sit on the bottom corner of a
cuboid room of size 6x5x3, with a fly perched on the opposite ceiling corner. By
travelling in the shortest straight line, the spider can reach the fly on a path
of distance 10.

Considering all cuboid rooms that do not exceed M = 100, the amount that have a
shortest path with integer dimensions is 2060.

e.g.: M = 99
      count = 1975
"""
from itertools import accumulate
from util.maths.reusable import pythagorean_triplet


def count_cuboids(a: int, b: int) -> int:
    """
    Returns a count of distinct cuboid combinations based on the assumption that
    a is the longest side and b is a summation of the 2 other sides.

            e.g. Pythagorean triplet (6, 8, 10) produces 2 sets of combinations:
                 {(6, 2, 6), (6, 3, 5), (6, 4, 4)} when a=6 and b=8 &
                 {(8, 1, 5), (8, 2, 4), (8, 3, 3)} when a=8 and b=6
    """

    return b // 2 if a >= b else a - (b - 1) // 2


def count_distinct_cuboids(max_m: int) -> int:
    """
    The cuboid room can be visualised by flattening it to 2D, showing that the 3
    shortest path candidates are formed by the hypotenuses of either a 6x8
    right-angled triangle or a 9x5 right-angled triangle. Only the 6x8 triangle
    has an integer hypotenuse (10), which is a Pythagorean triplet.

    Solution uses a similar approach to the previously determined solutions for
    finding perimeters of right-angled triangles (Batch 3 - Problem 39,
    Batch 7 - Problem 75).

    The amount of distinct cuboids is checked and counted twice to account for
    different combinations, e.g. Pythagorean triplet (6, 8, 10) produces different
    sets of cuboids depending on whether the longest side is 6 or 8.

    Given that the triplet's a (= m^2 - n^2) must be <= max_m, setting the outer
    loop limit to reflect the lowest value of a (so as not to miss any
    combinations) works fine but produces very slow speeds as M increases. When M
    = 1e4, it took 17.27s to iterate through the 3 loops, whereas it took the quick
    draw solution 10.20s to generate all counts accurately up to 4e5.
    """

    cuboids = 0
    m = 2
    while m <= (max_m + 1) // 2:
        for n in range(1, m):
            d = 0
            try:
                while True:
                    d += 1
                    a, b, _ = pythagorean_triplet(m, n, d)
                    if a > max_m and b > max_m:
                        break
                    if b // 2 <= a <= max_m:
                        cuboids += count_cuboids(a, b)
                    if a // 2 <= b <= max_m:
                        cuboids += count_cuboids(b, a)
            except ValueError:
                # primitive triplet must have m XOR n as even &
                # m and n co-prime (gcd == 1)
                continue
        m += 1

    return cuboids


def cuboid_counts_quick_draw() -> [int]:
    """
    Stores the cumulative sum of all distinct cuboid counts for quick access.

    Note that brute force shows highest m = 1414 for M = 4e5, so max of 1e6 chosen
    to ensure no combinations are missed.

    Note that the list of single counts is identical to sequence A143714.
    @see <a href=">https://oeis.org/A143714">Sequence A143714</a>

    :returns: List of possible cuboid combinations for every index = M.
    """

    max_m = 1_000_000
    single_counts = [0]*(max_m + 1)
    m = 2

    while m * m // 2 <= max_m:
        for n in range(1, m):
            d = 0
            try:
                while True:
                    d += 1
                    a, b, _ = pythagorean_triplet(m, n, d)
                    if a > max_m and b > max_m:
                        break
                    if b // 2 <= a <= max_m:
                        single_counts[a] += count_cuboids(a, b)
                    if a // 2 <= b <= max_m:
                        single_counts[b] += count_cuboids(b, a)
            except ValueError:
                # primitive triplet must have m XOR n as even &
                # m and n co-prime (gcd == 1)
                continue
        m += 1

    return list(accumulate(single_counts))


def get_least_m(count: int) -> int:
    """
    Project Euler specific implementation that requires the least value of M such
    that the count of distinct cuboid rooms first exceeds count.
    """

    cumulative_count = cuboid_counts_quick_draw()
    return max(
        range(len(cumulative_count)),
        key=lambda i: cumulative_count[i] > count
    )
