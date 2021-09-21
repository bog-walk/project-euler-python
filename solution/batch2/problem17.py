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

# tuples chosen for storage as immutable & ordered collections
__space = " "
__space_and = " And "
__under_twenty = (
    "", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
    "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen",
    "Seventeen", "Eighteen", "Nineteen"
)
__twenty_up = (
    "", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
)
__powers_of_ten = ("", "Thousand", "Million", "Billion", "Trillion")


def __number_under_hundred(n):
    if n < 20:
        return __under_twenty[n]
    else:
        second_word: str = __under_twenty[n % 10]
        return f"{__twenty_up[n // 10]}" \
               f"{second_word if not len(second_word) else __space + second_word}"


def __number_under_thousand(n, include_and):
    if n < 100:
        return __number_under_hundred(n)
    else:
        second_part: str = __number_under_hundred(n % 100)
        extra_part = __space_and if include_and else __space
        return f"{__under_twenty[n // 100]} Hundred" \
               f"{second_part if not len(second_part) else extra_part + second_part}"


def number_written(n, include_and: bool = True) -> str:
    if n == 0:
        return "Zero"
    words = ""
    power = 0
    while n:
        mod_thousand = n % 1000
        if mod_thousand:
            power_part = __space + __powers_of_ten[power] if power else ""
            words = f"{__number_under_thousand(mod_thousand, include_and)}" \
                    f"{power_part}{words if not len(words) else __space + words}"
        n //= 1000
        power += 1
    return words


def count_letters(words: str) -> int:
    """
    Counts number of letters in a string, excluding whitespace & hyphens.
    """
    return sum(ch.isalpha() for ch in words)


def count_first_N_positives(n):
    return sum(list(map(count_letters, list(map(number_written, range(1, n + 1))))))
