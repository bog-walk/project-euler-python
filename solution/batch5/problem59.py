""" Problem 59: XOR Decryption

https://projecteuler.net/problem=59

Goal: Given encoded ASCII codes for a plain text message that contains common
English characters, decrypt it and find the key (3 characters a-z long) that is
used to encrypt the message.

Constraints: 80 <= N <= 1500

XOR Decryption: A modern encryption method is to take a text file, convert the
    bytes to ASCII, then XOR each byte with a given value, taken from a secret key.
    This same encryption key will decrypt cipher text. An unbreakable encryption has
    a key of the same length as the plain text and the former is made up of random
    bytes. The encryption and its key would also be in separate locations. However,
    a password of shorter-than-message length is more likely used an encryption key,
    repeated cyclically throughout the message.

e.g.: N = 82
      encryption = [32, 66, 50, 20, 11, 0, 42, 66, 33, 19, 13, 20, 47, 66, 37, 14,
      58, 67, 43, 23, 14, 17, 49, 67, 46, 20, 6, 51, 66, 55, 9, 39, 67, 45, 3, 25,
      56, 66, 39, 14, 37, 34, 65, 51, 22, 8, 1, 40, 65, 32, 17, 14, 21, 45, 65,
      36, 12, 57, 66, 41, 20, 15, 19, 50, 66, 44, 23, 7, 49, 65, 54, 11, 36, 66,
      47, 0, 24, 58, 65, 38, 12, 38]
      encryption key = "abc"
"""
import string
from itertools import product
from re import fullmatch

valid_chars = " !\"" + "'()*+,-./" + string.digits + ":;?" + \
              string.ascii_letters + "[]"
valid_code = [ord(ch) for ch in valid_chars]
is_valid_character = [code in valid_code for code in range(123)]
prefix = "^['\"(\\[]?"
suffix = "[,.:;?!'\")\\]]{0,2}$"
words = "([a-zA-Z0-9'(\\-\\+:]*|[0-9]*[./]?[0-9]*)"


def is_valid_word(word: str) -> bool:
    return (
            len(word) != 0 and
            fullmatch(prefix + words + suffix, word) is not None
    )


def decrypt_code(encryption: list[int], key: (str, str, str)) -> list[int]:
    """ Decrypts a list of ASCII codes using a 3-letter key.

    Could be used to also encrypt a list of original ASCII codes.

    Bitwise XOR (^) is used to decrypt/encrypt the codes by returning a new code
    that corresponds to the comparison between 2 equal-sized bit patterns where 1
    is returned if exactly one of the compared bits is 1; otherwise, 0 is returned.

    :returns: List of ASCII codes that have been altered through xor decryption (
        or encryption if used in reverse).
    """

    key_code = [ord(k) for k in key]
    return [code ^ key_code[i % 3] for i, code in enumerate(encryption)]


def get_message(decryption: list[int]) -> str:
    return "".join(chr(code) for code in decryption)


def xor_decryption(encryption: list[int]) -> str:
    """
    Solution optimised by ensuring only valid ASCII codes are returned by the
    decryption of a smaller message, which means fewer full-sized messages will
    undergo regex pattern matching.

    e.g. The PE test case skips 3311 keys that generate invalid ASCII code and
    only uses regex to test the full test message on 7 occasions.
    """

    sample = encryption[:80]
    found_key = None
    # 17576 combinations as not guaranteed that each key character is unique
    for key in product(string.ascii_lowercase, repeat=3):
        sample_code = decrypt_code(sample, key)
        if any(code > 122 or not is_valid_character[code] for code in sample_code):
            continue
        all_code = decrypt_code(encryption, key)
        message = get_message(all_code)
        if all(is_valid_word(word) for word in message.split(" ")):
            found_key = "".join(key)
            break
    return found_key


def sum_of_decrypted_codes(encryption: list[int]) -> int:
    """
    Project Euler specific implementation that decrypts the encoded ASCII codes
    provided in a resource file and returns the sum of the ASCII codes in the
    original plain text message.

    The key to the solution is "exp".
    """

    key = xor_decryption(encryption)
    return sum(decrypt_code(encryption, key))
