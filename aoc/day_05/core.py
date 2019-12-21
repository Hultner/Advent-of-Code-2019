"""
TODO: Day 5 desc
"""
from collections import deque
from numbers import Number
from typing import Tuple, Iterable, List, NoReturn, Dict, Deque
import logging

from aoc.day_05.seed import p1
from aoc.intcode import Computer, StdIO


class QueuedIO(StdIO):
    "Create fake STDOUT/STDIN using deques"

    stdin: Deque
    stdout: Deque

    def __init__(self, in_: Iterable[int]) -> NoReturn:
        self.stdin = deque(in_)
        self.stdout = deque()

    def write(self, data: int) -> NoReturn:
        logging.debug(f"Writing to stdout {data}")
        self.stdout.append(data)

    def read(self) -> int:
        return self.stdin.popleft()


def run_io_program(program: Iterable[int], stdin: Iterable[int]) -> int:
    """
    Returns the last value printed to stdout when running program with `stdin`
    """
    io = QueuedIO(stdin)
    Computer(list(program), io=io).run_program()
    return io.stdout.pop()


def part_1(puzzle_input: Tuple[Number] = p1) -> Number:
    """
    TODO: Day 5 pt1 desc
    """
    # Put 1 to stdin
    return run_io_program(p1, (1,))


def part_2(puzzle_input: Tuple[Number] = p1) -> Number:
    """
    TODO: Day 5 pt2 desc
    """
    # Put 5 to stdin
    return run_io_program(p1, (5,))


if __name__ == "__main__":
    print(part_1())
    print(part_2())
