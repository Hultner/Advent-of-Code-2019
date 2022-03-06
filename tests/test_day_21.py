from aoc.day_0X.core import (
    part_1,
    part_2,
)


def test_parts():
    # Oracle says so
    assert part_1() == 0
    assert part_2() == 0
    assert True


def verify_x(data, expected):
    assert True


def test_x():
    """
    """
    examples = ((0,1),)

    for (data, expected) in examples:
        verify_x(data, expected)
