"""
--- Day 4: Secure Container ---
"""
import logging
from dataclasses import dataclass, field
from itertools import groupby
from numbers import Number
from typing import Tuple, Iterable, List, NoReturn, Dict
from aoc.day_04.seed import p1


def rle(data: str) -> Tuple[str, int]:
    """Returns run-lenght-encoding Tuples for string"""
    # A memory efficient (lazy) and pythonic solution using generators
    return ((x, sum(1 for _ in y)) for x, y in groupby(data))


def verify_password(password: str) -> bool:
    """
    Verify if password are  compliant with these requirments

     - It is a six-digit number.
     - The value is within the range given in your puzzle input.
     - Two adjacent digits are the same (like 22 in 122345).
     - Going from left to right, the digits never decrease; they only ever
       increase or stay the same (like 111123 or 135679).

    Args:
        password: Password to test
    Returns: True if pasword is compliant
    """
    try:
        return all(
            (
                # It is a six-digit number.
                len(str(int(password))) == 6,
                # The value is within the range given in your puzzle input.
                # Two adjacent digits are the same (like 22 in 122345).
                any(ln >= 2 for (char, ln) in rle(password)),
                # Going from left to right, the digits never decrease; they
                # only ever rncrease or stay the same (like 111123 or 135679).
                all(x <= y for (x, y) in zip(password, password[1:])),
            )
        )
    except (ValueError, IndexError):
        # Not number, not multi char string
        return False


def verify_password_p2(password: str) -> bool:
    """
    See: ```verify_password()```, with the additional validation that at least
    one character with exactly RLE 2
    """
    return all(
        (verify_password(password), any(ln == 2 for (char, ln) in rle(password)),)
    )


def part_1(puzzle_input: Tuple[Number] = p1) -> Number:
    """
    You arrive at the Venus fuel depot only to discover it's protected by a
    password. The Elves had written the password on a sticky note, but someone
    threw it out.

    However, they do remember a few key facts about the password:

      - It is a six-digit number.
      - The value is within the range given in your puzzle input.
      - Two adjacent digits are the same (like 22 in 122345).
      - Going from left to right, the digits never decrease; they only ever
        increase or stay the same
        (like 111123 or 135679).

    Other than the range rule, the following are true:

      - 111111 meets these criteria (double 11, never decreases).
      - 223450 does not meet these criteria (decreasing pair of digits 50).
      - 123789 does not meet these criteria (no double).

    How many different passwords within the range given in your puzzle input
    meet these criteria?
    """
    return len([1 for x in range(p1[0], p1[1] + 1) if verify_password(str(x))])


def part_2(puzzle_input: Tuple[Number] = p1) -> Number:
    """

    --- Part Two ---

    An Elf just remembered one more important detail: the two adjacent matching
    digits are not part of a larger group of matching digits.

    Given this additional criterion, but still ignoring the range rule, the
    following are now true:

     - 112233 meets these criteria because the digits never decrease and all
       repeated digits are exactly two digits long.
     - 123444 no longer meets the criteria (the repeated 44 is part of a larger
       group of 444).
     - 111122 meets the criteria (even though 1 is repeated more than twice, it
       still contains a double 22).

    How many different passwords within the range given in your puzzle input
    meet all of the criteria?
    """
    return len([1 for x in range(p1[0], p1[1] + 1) if verify_password_p2(str(x))])
