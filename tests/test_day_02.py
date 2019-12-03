from aoc.day_02.core import (
    part_1,
    part_2,
    Computer,
)


def test_parts():
    # Oracle says so
    assert part_1() == 9581917
    assert part_2() == 2505


def verify_computer(program, mem_out):
    c = Computer(list(program))
    c.run_program()
    assert list(mem_out) == c.memory


def test_computer():
    """
    Here are the initial and final states of a few more small programs:

     - 1,0,0,0,99 becomes 2,0,0,0,99 (1 + 1 = 2).
     - 2,3,0,3,99 becomes 2,3,0,6,99 (3 * 2 = 6).
     - 2,4,4,5,99,0 becomes 2,4,4,5,99,9801 (99 * 99 = 9801).
     - 1,1,1,4,99,5,6,0,99 becomes 30,1,1,4,2,5,6,0,99.

    """
    examples = (
        ((1, 0, 0, 0, 99), (2, 0, 0, 0, 99)),
        ((2, 3, 0, 3, 99), (2, 3, 0, 6, 99)),
        ((2, 4, 4, 5, 99, 0), (2, 4, 4, 5, 99, 9801)),
        ((1, 1, 1, 4, 99, 5, 6, 0, 99), (30, 1, 1, 4, 2, 5, 6, 0, 99)),
    )

    for (program, mem_out) in examples:
        verify_computer(program, mem_out)
