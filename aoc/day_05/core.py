"""
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

    def __init__(self, in_: Iterable[int]):
        self.stdin = deque(in_)
        self.stdout = deque()

    def write(self, data: int) -> NoReturn:
        logging.debug(f"Writing to stdout {data}")
        self.stdout.append(data)

    def read(self) -> int:
        return self.stdin.popleft()


def part_1(puzzle_input: Tuple[Number] = p1) -> Number:
    """
    """
    # Put 1 to stdin
    io = QueuedIO([1,])

    c = Computer(list(p1), io=io)
    c.run_program()
    # The computer memory has no significance here, return last stdout
    return io.stdout.pop()


def part_2(puzzle_input: Tuple[Number] = p1) -> Number:
    """
    """
    # Put 5 to stdin
    io = QueuedIO([5,])

    c = Computer(list(p1), io=io)
    c.run_program()
    # The computer memory has no significance here, return last stdout
    return io.stdout.pop()


if __name__ == "__main__":
    print(part_1())
    print(part_2())
