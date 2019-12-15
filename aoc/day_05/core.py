"""
"""
from numbers import Number
from typing import Tuple, Iterable, List, NoReturn, Dict
from aoc.day_05.seed import p1
from aoc.intcode import Computer


# TODO:
#  - Create fake STDOUT/STDIN using deques

def part_1(puzzle_input: Tuple[Number] = p1) -> Number:
    """
    """
    # Put 1 to stdin
    c = Computer(list(p1))
    c.run_program()
    # The read has no significance here, return stdout
    return c.read()


def part_2(puzzle_input: Tuple[Number] = p1) -> Number:
    """
    """
    # Put 5 to stdin
    c = Computer(list(p1))
    c.run_program()
    # The read has no significance here, return stdout
    return c.read()


if __name__ == "__main__":
    print(part_1())
    print(part_2())
