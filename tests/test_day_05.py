from typing import Iterable, Callable, NoReturn

import pytest
from hypothesis import given
import hypothesis.strategies as st
from aoc.day_05.core import part_1, part_2, run_io_program

MAX_SIGNED_8BIT = 0b_1111_1111 // 2  # 127
MIN_SIGNED_8BIT = -0b_1111_1111 // 2  # -128

# Part 2
# For example, here are several programs that take one input, compare it to
# the value 8, and then produce one output:
test_programs = (
    (
        (3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8),
        lambda x: 1 if x == 8 else 0,
        (
            "Using position mode, consider whether the input is equal to 8;"
            "output 1 (if it is) or 0 (if it is not)."
        ),
    ),
    (
        (3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8),
        lambda x: 1 if x < 8 else 0,
        (
            "Using position mode, consider whether the input is less than 8;"
            "output 1 (if it is) or 0 (if it is not)."
        ),
    ),
    (
        (3, 3, 1108, -1, 8, 3, 4, 3, 99),
        lambda x: 1 if x == 8 else 0,
        (
            "Using immediate mode, consider whether the input is equal to 8;"
            "output 1 (if it is) or 0 (if it is not)."
        ),
    ),
    (
        (3, 3, 1107, -1, 8, 3, 4, 3, 99),
        lambda x: 1 if x < 8 else 0,
        (
            "Using immediate mode, consider whether the"
            "input is less than 8; output 1 (if it is) or 0 (if it is not)."
        ),
    ),
    (
        (3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9),
        lambda x: 0 if x == 0 else 1,
        (
            "Here are some jump tests that take an input, then output 0 if the input"
            "was zero or 1 if the input was non-zero: (using position mode)"
        ),
    ),
    (
        (3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1),
        lambda x: 0 if x == 0 else 1,
        (
            "Here are some jump tests that take an input, then output 0 if the input"
            "was zero or 1 if the input was non-zero: (using immediate mode)"
        ),
    ),
    (
        # Here's a larger example:
        (
            # fmt: off
            3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
            1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
            999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99,
            # fmt: on
        ),
        lambda x: 999 if x < 8 else 1000 if x == 8 else 1001,
        (
            "The above example program uses an input instruction to ask for a single"
            "number. The program will then output 999 if the input value is below 8,"
            "output 1000 if the input value is equal to 8, or output 1001 if the input"
            "value is greater than 8."
        ),
    ),
)


def test_parts():
    # Oracle says so
    assert part_1() == 12896948
    assert part_2() == 7704130


# Hypothesis generate stdin
@given(stdin=st.integers(min_value=MIN_SIGNED_8BIT, max_value=MAX_SIGNED_8BIT))
@pytest.mark.parametrize("data,expected,msg", test_programs)
def test_io_program(
    data: Iterable[int], expected: Callable[[int], int], stdin: int, msg: str
) -> NoReturn:
    assert run_io_program(data, (stdin,)) == expected(stdin), msg

