""" Problem 17: Number to Words

https://projecteuler.net/problem=17

Goal #1: Print the given number N as capitalised words (with/without "And").

Goal #2: Count the total number of letters used when the first N positive numbers
are converted to words, with "And" used in compliance with British usage.

Constraints: 0 <= N <= 1e12

e.g.: Goal #1 -> N = 243
      output = "Two Hundred And Forty Three"
      Goal #2 -> N = 5 -> {"One", "Two", "Three", "Four", "Five"}
      output = 19
"""

space = " "
space_and = " And "
# tuples chosen for storage as immutable & ordered collections
under_twenty = (
    "", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
    "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen",
    "Seventeen", "Eighteen", "Nineteen"
)
tens = (
    "", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy",
    "Eighty", "Ninety"
)
powers_of_ten = "", "Thousand", "Million", "Billion", "Trillion"


def number_under_hundred(n: int) -> str:
    if n < 20:
        return under_twenty[n]
    else:
        second_word = under_twenty[n % 10]
        return f"{tens[n // 10]}" \
               f"{space + second_word if len(second_word) else second_word}"


def number_under_thousand(n: int, include_and: bool) -> str:
    if n < 100:
        return number_under_hundred(n)
    else:
        second_part = number_under_hundred(n % 100)
        extra_part = space_and if include_and else space
        return f"{under_twenty[n // 100]} Hundred" \
               f"{extra_part + second_part if len(second_part) else second_part}"


def number_written(n: int, include_and: bool = True) -> str:
    if n == 0:
        return "Zero"
    words = ""
    power = 0
    while n:
        mod_thousand = n % 1000
        if mod_thousand:
            power_part = space + powers_of_ten[power] if power else ""
            words = f"{number_under_thousand(mod_thousand, include_and)}" \
                    f"{power_part}{space + words if len(words) else words}"
        n //= 1000
        power += 1
    return words


def count_first_N_positives(n: int) -> int:
    """
    Project Euler specific implementation that sums the amount of letters
    (excludes whitespace & punctuations) in the written forms of the first N
    positive numbers.
    """

    return sum(
        map(
            lambda string: sum(ch.isalpha() for ch in string),
            map(number_written, range(1, n + 1))
        )
    )
