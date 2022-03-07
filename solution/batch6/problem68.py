""" Problem 68: Magic 5-Gon Ring

https://projecteuler.net/problem=68

Goal: Given N, representing a magic N-gon ring, and S, representing the total to
which each ring's line sums, return all concatenated strings (in lexicographic order)
representing the N sets of solutions.

Constraints: 3 <= N <= 10

Magic 3-Gon Ring (as seen in above link): The ring has 3 external nodes,
each ending a line of 3 nodes (6 nodes total representing digits 1 to 6). The
ring can be completed so the lines reach 4 different totals, [9, 12], so there
are 8 solutions in total:
     9 -> [{4,2,3}, {5,3,1}, {6,1,2}], [{4,3,2}, {6,2,1}, {5,1,3}]
     10 -> [{2,3,5}, {4,5,1}, {6,1,3}], [{2,5,3}, {6,3,1}, {4,1,5}]
     11 -> [{1,4,6}, {3,6,2}, {5,2,4}], [{1,6,4}, {5,4,2}, {3,2,6}]
     12 -> [{1,5,6}, {2,6,4}, {3,4,5}], [{1,6,5}, {3,5,4}, {2,4,6}]
     So the maximum concatenated string for a magic 3-gon is "432621513".

e.g.: N = 3, S = 9
      solutions = ["423531612", "432621513"]
"""
from itertools import permutations


def max_magic_5_gon_solution() -> str:
    """
    Project Euler specific implementation that requests the maximum 16-digit
    string solution from all solutions for a magic 5-gon ring that uses numbers
    1 to 10 in its nodes.

    For the solution to have 16 digits, the number 10 has to be an external node,
    as, if it were placed on the internal ring, it would be used by 2 unique lines
    & would create a 17-digit concatenation. So, at minimum, the line with 10 as
    an external node will sum to 13.

    To create the largest lexicographic concatenation, larger numbers ideally
    should be placed first. Based on the magic 3-gon ring example detailed in the
    problem description, if the largest numbers are external nodes and the
    smallest numbers are ring nodes, the maximum solution occurs at the lowest
    total achieved by the following:

    (sum(external_nodes) + 2 * sum(internal_nodes)) / N

    e.g. (sum([4, 5, 6]) + 2 * sum([1, 2, 3])) / 3 = 9

    The maximum solution indeed occurs when S = 14 with the largest numbers on
    the external nodes, but all totals up to 27 were explored given the speed of
    the recursive solution below.

    N.B. Solutions exist for the following totals: [14, 16, 17, 19].
    """

    solutions: list[list[str]] = []
    for s in range(13, 28):
        solution = magic_ring_solutions_improved(5, s)
        if len(solution):
            solutions.append(solution)
    solutions_sorted = sorted([
        solution
        for pair in solutions
        for solution in pair
        if len(solution) == 16
    ], reverse=True)
    return solutions_sorted[0]


def magic_ring_solutions(n: int, s: int) -> [str, ...]:
    """
    Solution uses recursion to search through all permutations (n * 2 digits
    choose 3) from an increasingly smaller set of remaining digits. Permutations
    are checked to see if they sum to s & if their middle digit matches the last
    digit of the permutation found previously.

    A stack of the remaining digits to use is cached so the search can continue if
    a solution that cannot close the ring is reached. This is done by adding the
    elements of the last permutation back to the stack if the solution becomes
    invalid.

    Rather than searching for a final permutation that completes the ring,
    the expected list is generated based on the remaining digits possible &
    checked to see if it complements the starter list & adds up to s.

    SPEED (WORST)
        310.48ms for N = 7, S = 23
    """

    solutions = []
    all_digits = set(range(1, n * 2 + 1))

    def next_ring_line(solution: list[tuple]):
        if len(all_digits) == 2:
            expected = [
                all_digits.difference({solution[-1][2]}).pop(),
                solution[-1][2],
                solution[0][1]
            ]
            if expected[0] > solution[0][0] and sum(expected) == s:
                concat = "".join([str(d) for line in solution for d in line])
                concat += "".join(map(str, expected))
                solutions.append(concat)
        else:
            for perm in permutations(all_digits, 3):
                if (
                        perm[1] != solution[-1][2] or
                        perm[0] < solution[0][0] or
                        sum(perm) != s
                ):
                    continue
                solution.append(perm)
                all_digits.difference_update(set(perm) - {perm[2]})
                next_ring_line(solution)
        all_digits.update(solution.pop())

    # starter must have the lowest external node, which limits the digits it can have
    starter_max = n * 2 - n + 1
    for starter in permutations(all_digits, 3):
        if starter[0] > starter_max or sum(starter) != s:
            continue
        all_digits.difference_update(set(starter) - {starter[2]})
        next_ring_line([starter])
        all_digits = set(range(1, n * 2 + 1))
    return sorted(solutions)


def magic_ring_solutions_improved(n: int, s: int) -> [str, ...]:
    """
    While still using recursion, the solution is optimised by not generating all
    permutations of 3-digit lines. Instead, nodes on the internal ring alone are
    recursively generated from an increasingly smaller set of available digits and
    the corresponding external node for every pair of ring nodes is calculated.

    SPEED (BETTER)
        88.06ms for N = 7, S = 23
    """

    solutions = []
    all_digits = range(1, n * 2 + 1)
    remaining_digits = set(all_digits)
    ring_nodes = [0] * n
    external_nodes = [0] * n

    def next_ring_node(i: int):
        if i == n - 1:
            external_nodes[i] = s - ring_nodes[i] - ring_nodes[0]
            if (
                    external_nodes[i] in remaining_digits and
                    # first external node must be smallest of all external nodes
                    external_nodes[0] == min(external_nodes)
            ):
                solution = "".join([
                    f"{external_nodes[j]}{ring_nodes[j]}{ring_nodes[(j + 1) % n]}"
                    for j in range(n)
                ])
                solutions.append(solution)
        else:
            for d in all_digits:
                if d not in remaining_digits:
                    continue
                next_external = s - ring_nodes[i] - d
                if next_external == d or next_external not in remaining_digits:
                    continue
                ring_nodes[i + 1] = d
                external_nodes[i] = next_external
                just_used = {d, next_external}
                remaining_digits.difference_update(just_used)
                next_ring_node(i + 1)
                # solution found or not
                # either way backtrack to try a different ring node
                remaining_digits.update(just_used)

    for digit in all_digits:
        ring_nodes[0] = digit
        remaining_digits.remove(digit)
        next_ring_node(0)
        # solution found or not
        # either way backtrack to start ring with a novel node
        remaining_digits = set(all_digits)
    return sorted(solutions)


def magic_ring_solutions_optimised(n: int, s: int) -> [str, ...]:
    """
    This solution is identical to the above improved solution but reduces speed in
    half by taking advantage of the pattern that all solutions present in pairs.

    e.g. when N = 4, S = 12, the 1st solution will be found when the starter
    digit = 2, with:

    ring_nodes = [2, 6, 1 ,3] and external_nodes = [4, 5, 8, 7] -> "426561813732"

    If the 1st 2 elements of ring_nodes are swapped & the rest reversed, and all
    elements of external_nodes, except the static lowest external, are also reversed,
    the lists become:

    ring_nodes = [6, 2, 3, 1] and external_nodes = [4, 7, 8, 5] -> "462723831516"

    This latter solution would have been eventually found when the starter digit = 6.

    Instead, any duplicate searches are eliminated by reversing all solutions when
    found & not allowing starter digits to explore adjacent ring digits that are
    smaller (as these would already have been found by previous iterations). So
    the starter digit 6 would only end up searching through
    ring_nodes = [6, [7, 12], X, X]

    Lastly, neither digit 1 nor digit n need to be assessed as they will be found in
    later or earlier iterations.

    SPEED (BEST - EQUAL)
        40.35ms for N = 7, S = 23
    """

    solutions = []
    all_digits = range(1, n * 2 + 1)
    remaining_digits = set(all_digits)
    ring_nodes = [0]*n
    external_nodes = [0]*n

    def next_ring_node(i: int):
        if i == n - 1:
            external_nodes[i] = s - ring_nodes[i] - ring_nodes[0]
            if (
                    external_nodes[i] in remaining_digits and
                    external_nodes[0] == min(external_nodes)
            ):
                solution1 = ""
                solution2 = ""
                for j in range(n):
                    solution1 += f"{external_nodes[j]}{ring_nodes[j]}" \
                        f"{ring_nodes[(j+1)%n]}"
                    solution2 += f"{external_nodes[(n-j)%n]}" \
                        f"{ring_nodes[(n-j+1)%n]}" \
                        f"{ring_nodes[(n-j)%n]}"
                solutions.extend([solution1, solution2])
        else:
            search = range(ring_nodes[0] + 1, n * 2 + 1) if i == 0 else all_digits
            for d in search:
                if d not in remaining_digits:
                    continue
                next_external = s - ring_nodes[i] - d
                if next_external == d or next_external not in remaining_digits:
                    continue
                ring_nodes[i + 1] = d
                external_nodes[i] = next_external
                just_used = {d, next_external}
                remaining_digits.difference_update(just_used)
                next_ring_node(i + 1)
                remaining_digits.update(just_used)

    for digit in range(2, n * 2):
        ring_nodes[0] = digit
        remaining_digits.remove(digit)
        next_ring_node(0)
        remaining_digits = set(all_digits)
    return sorted(solutions)


def magic_ring_solutions_optimised_alt(n: int, s: int) -> [str, ...]:
    """
    This solution is identical to the above optimised but combine internal &
    external nodes into a single array, so the reversed paired array can be
    generated in parallel, reducing the need to use formatted strings when a
    valid pair is found.

    SPEED (BEST - EQUAL)
        47.23ms for N = 7, S = 23
    """

    solutions = []
    all_digits = range(1, n * 2 + 1)
    remaining_digits = set(all_digits)
    ring_nodes = [0]*(n*3)
    ring_nodes_rev = [0]*(n*3)

    def next_ring_node(i: int):
        if i == (n - 1) * 3:
            last_external = s - ring_nodes[i + 1] - ring_nodes[i + 2]
            ring_nodes[i] = last_external
            if (
                    last_external in remaining_digits and
                    ring_nodes[0] == min(ring_nodes[::3])
            ):
                ring_nodes_rev[-i] = last_external
                solutions.append("".join(map(str, ring_nodes)))
                solutions.append("".join(map(str, ring_nodes_rev)))
        else:
            search = range(ring_nodes[1] + 1, n*2+1) if i == 0 else all_digits
            for d in search:
                if i != 0 and d not in remaining_digits:
                    continue
                next_external = s - ring_nodes[i+1] - d
                if next_external == d or next_external not in remaining_digits:
                    continue
                ring_nodes[i+2] = d
                ring_nodes[i+4] = d
                ring_nodes[i] = next_external
                ring_nodes_rev[-i+1] = d
                ring_nodes_rev[-i-1] = d
                # list[-0] == list[0]
                ring_nodes_rev[-i] = next_external
                just_used = {d, next_external}
                remaining_digits.difference_update(just_used)
                next_ring_node(i + 3)
                remaining_digits.update(just_used)

    for digit in range(2, n * 2):
        ring_nodes[1] = digit
        ring_nodes_rev[2] = digit
        ring_nodes[-1] = digit
        ring_nodes_rev[4] = digit
        remaining_digits.remove(digit)
        next_ring_node(0)
        remaining_digits = set(all_digits)
    return sorted(solutions)
