""" Problem 98: Anagramic Squares

https://projecteuler.net/problem=98

Goal: Find all square numbers with N digits that have at least 1 anagram that is
also a square number with N digits. Use this set to either map squares to anagram
strings or to find the largest square with the most anagramic squares in the set.

Constraints: 3 <= N <= 13

e.g.: N = 4
      only 1 set of anagramic squares is of length > 2 -> {1296, 2916, 9216}
      largest = 9216
"""
from math import inf, isqrt
from util.combinatorics.reusable import permutation_id


def find_anagrams(words: list[str]) -> list[tuple[str, str]]:
    """
    Returns all sets of anagrams found in a list of words, sorted in descending
    order by the length of the words.
    """

    permutations: {str, list[str]} = {}
    for word in words:
        if len(word) <= 2:
            continue  # palindromes are not anagrams
        perm_id = "".join(sorted(list(word)))
        permutations[perm_id] = permutations.setdefault(perm_id, [])
        permutations[perm_id].append(word)

    anagrams: list[tuple[str, str]] = []
    for perm_match in permutations.values():
        count = len(perm_match)
        if count == 1:
            continue
        elif count == 2:
            anagrams.append((perm_match[0], perm_match[1]))
        else:
            # only occurs once (size 3) from test resource, but let's be dynamic
            for i in range(count - 1):
                for j in range(i + 1, count):
                    anagrams.append((perm_match[i], perm_match[j]))

    return sorted(anagrams, key=lambda p: len(p[0]), reverse=True)


def get_eligible_squares(digits: int) -> list[list[str]]:
    """
    Returns all squares that have the desired number of digits and that are
    anagrams of other squares (based on their permutation id), with the latter being
    grouped together.

    Note that squares are found and returned in groups already sorted in ascending
    order.
    """

    all_squares: {str, list[str]} = {}

    maximum = pow(10, digits)
    base = isqrt(pow(10, digits - 1))
    square = base * base
    while square < maximum:
        perm_id = "".join(map(str, permutation_id(square)))
        all_squares[perm_id] = all_squares.setdefault(perm_id, [])
        all_squares[perm_id].append(str(square))
        base += 1
        square = base * base

    return list(filter(lambda squares: len(squares) > 1, all_squares.values()))


def find_largest_anagramic_square_by_words(words: list[str]) -> [str, str, int]:
    """
    Project Euler specific implementation that requests the largest square number
    possible from any anagramic square pair found within a large list of words.

    e.g. CARE, when mapped to 1296 (36^2), forms a pair with its anagram RACE,
    which maps to one of the square's own anagrams, 9216 (96^2).

    :returns: Tuple of Anagram word #1, Anagram word #2, the largest mapped square.
    """

    largest = ("", "", 0)

    anagrams = find_anagrams(words)
    num_of_digits = inf
    squares: list[list[str]] = []
    for anagram in anagrams:
        if len(anagram[0]) < num_of_digits:
            num_of_digits = len(anagram[0])
            squares = get_eligible_squares(num_of_digits)
        for square_set in squares:
            for square in square_set:
                # ensure square can be mapped to first word without different chars
                # using the same digit; e.g. CREATION should not map to 11323225
                mapping: {str, str} = {}
                for ch, digit in zip(anagram[0], square):
                    if ch in mapping.keys():
                        if mapping[ch] == digit:
                            continue
                        else:
                            break
                    else:
                        if digit in mapping.values():
                            break
                        else:
                            mapping[ch] = digit
                else:
                    expected = "".join(map(lambda s: mapping[s], anagram[1]))
                    if expected in square_set:
                        larger_square = max(int(square), int(expected))
                        if larger_square > largest[2]:
                            largest = (anagram[0], anagram[1], larger_square)
        # only interested in the largest found from the first set of squares
        # with a result
        if len(largest[0]):
            break

    return largest


def find_largest_anagramic_square_by_digits(n: int) -> int:
    """
    HackerRank specific implementation that only requires that all possible
    anagram squares with n digits be found. From this list of sets, the largest
    square from the largest set must be returned; otherwise, return the largest
    square from all equivalently sized sets.
    """

    squares = get_eligible_squares(n)
    largest_size, largest_square = 0, 0
    for square_set in squares:
        if len(square_set) > largest_size:
            largest_size, largest_square = len(square_set), int(square_set[-1])
            continue
        if len(square_set) == largest_size:
            largest_square = max(largest_square, int(square_set[-1]))

    return largest_square
