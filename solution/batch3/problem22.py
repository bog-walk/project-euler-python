""" Problem 22: Names Scores

https://projecteuler.net/problem=22

Goal: Given an unsorted list of N names, first sort alphabetically,
then, given 1 of the names, multiply the sum of the value of all its
characters by its position in the alphabetical list.

Constraints: 1 <= N <= 5200, len(NAME) < 12

e.g.: Input = [ALEX, LUIS, JAMES, BRIAN, PAMELA]
      Sorted = [ALEX, BRIAN, JAMES, LUIS, PAMELA]
      Name = PAMELA = 16 + 1 + 13 + 5 + 12 + 1 = 48
      Position = 5th
      Result = 5 * 48 = 240
"""


def name_score(index, name):
    # Unicode decimal value of 'A' is 65, but should be adjusted to 1
    return (index + 1) * sum(ord(c) - 64 for c in name)


def sum_of_name_scores(names: list[str]):
    sorted_names = sorted(names)
    return sum(name_score(i, name) for i, name in enumerate(sorted_names))
