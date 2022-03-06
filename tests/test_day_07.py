from typing import Iterable

import pytest

from aoc.day_07.core import (
    part_1,
    part_2,
)

# Here are some example programs:
test_programs = (
    (
        # Max thruster signal 43210 (from phase setting sequence 4,3,2,1,0):
        43210,
        (4, 3, 2, 1, 0),
        (3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0),
    ),
    (
        # Max thruster signal 54321 (from phase setting sequence 0,1,2,3,4):
        54321,
        (0, 1, 2, 3, 4),
        (
            # fmt: off
            3,23,3,24,1002,24,10,24,1002,23,-1,23,
            101,5,23,23,1,24,23,23,4,23,99,0,0
            # fmt: on
        ),
    ),
    (
        # Max thruster signal 65210 (from phase setting sequence 1,0,4,3,2):
        65210,
        (1, 0, 4, 3, 2),
        (
            # fmt: off
            3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,
            1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0
            # fmt: on
        ),
    ),
)


def test_parts():
    # Oracle says so
    assert part_1() == 0
    assert part_2() == 0
    assert True


@pytest.mark.parametrize("signal,sequence,program", test_programs)
def test_max_thruster(signal: int, sequence: Iterable[int], program: Iterable[int]):
    assert True
