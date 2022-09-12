""" Problem 89: Roman Numerals

https://projecteuler.net/problem=89

Goal: Given a string of Roman number symbols, output a valid (or more efficient)
Roman number that represents it, by following the rules below.

Constraints: 1 <= length of input string <= 1000

Roman Numerals: {I: 1, V: 5, X: 10, L: 50, C: 100, D: 500, M: 1000}

Roman numbers are written in descending order of symbols to be added, with the
appearance of a symbol with lesser value before another symbol implying
subtraction. This is why 14 is written as XIV, not IVX.

Notably, M is the only symbol that can appear more than 3 times in a row. This is
why 9 is written as IX and not VIII. Also, V, L, and D will not appear more than
once.

Subtraction Rules:
     - I can only be subtracted from V and X.
     - X can only be subtracted from L and C.
     - C can only be subtracted from D and M.
     - V, L, D, and M cannot be subtracted from another symbol.
     - Only one I, X, and C can be used as the leading numeral in part of a
     subtractive pair.
e.g. 999 is written as CMXCIX, not IM.

e.g.: input = "IIIII"
      output = "V"
      input = "VVVVVVVVV"
      output = "XLV"
"""

roman_symbols = {
    "M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, "L": 50, "XL": 40,
    "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1
}


def parse_input(string: str) -> int:
    """
    Creates an integer from a string representation of a Roman Number by iterating
    through every character and looking forward to see if the appropriate value
    must be added or subtracted.

    This could be solved in the opposite way that Int.toRomanNumber() works,
    by iterating through an alternative map sorted from the lowest value to
    highest (but with subtractive pairs first). Every symbol could be removed from
    the original string & resulting lengths compared to create an incrementing
    numerical value.
    """

    value = 0
    last_i = len(string) - 1

    for i, ch in enumerate(string):
        current_symbol = roman_symbols.get(ch, 0)
        if i == last_i:
            value += current_symbol
        else:
            next_symbol = roman_symbols.get(string[i+1], 0)
            if next_symbol <= current_symbol:
                value += current_symbol
            else:
                value -= current_symbol

    return value


def to_roman_number(n: int) -> str:
    """
    Creates a Roman Number by repeatedly dividing out all mapped symbols from the
    original  number.
    """

    roman_numeral = []

    for symbol, value in roman_symbols.items():
        if n == 0 or symbol == "I":
            break
        roman_numeral.append(symbol * (n // value))
        n %= value
    roman_numeral.append("I" * n)

    return "".join(roman_numeral)


def get_roman_number(string: str) -> str:
    return to_roman_number(parse_input(string))


def roman_chars_saved(inputs: [str]) -> int:
    """
    Project Euler specific implementation that returns the number of characters
    saved by writing all 1000 input strings in their more efficient minimal form.

    Note that test resource input strings are not guaranteed to have symbols in
    descending value order.
    """

    # string length difference should never be a negative value
    return sum(len(string) - len(get_roman_number(string)) for string in inputs)
