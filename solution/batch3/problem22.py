""" Problem 22: Names Scores

https://projecteuler.net/problem=22

Goal: Given an unsorted list of N names, first sort alphabetically, then, given
1 of the names, multiply the sum of the value of all its characters by its
position in the alphabetical list.

Constraints: 1 <= N <= 5200, len(NAME) < 12

e.g.: input = [ALEX, LUIS, JAMES, BRIAN, PAMELA]
      sorted = [ALEX, BRIAN, JAMES, LUIS, PAMELA]
      name = PAMELA = 16 + 1 + 13 + 5 + 12 + 1 = 48
      position = 5th
      result = 5 * 48 = 240
"""


def name_score(position: int, name: str) -> int:
    """ Helper function returns a score for a name as detailed above.

    Zero-indexed position is found using -> sorted_list.index("name").
    Input is assumed to consist of names in ALL_CAPS, but this can be ensured by
    including name.upper() in the solution.
    """

    # unicode decimal value of 'A' is 65, but is normalised to represent value 1
    return (position + 1) * sum(map(lambda c: ord(c) - 64, name))


def sum_of_name_scores(names: list[str]) -> int:
    """
    Project Euler specific implementation that requires all the name scores of
    a 5000+ list to be summed.
    """

    sorted_names = sorted(names)
    return sum(name_score(i, name) for i, name in enumerate(sorted_names))
