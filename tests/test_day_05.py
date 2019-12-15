from aoc.day_05.core import (
    part_1,
    part_2,
)


def test_parts():
    # Oracle says so
    assert part_1() == 12896948
    assert part_2() == 7704130


def verify_x(data, expected):
    assert True


def test_x():
    """
    """
    examples = ((0,1),)

    for (data, expected) in examples:
        verify_x(data, expected)


    """
    I've been running tests in repl-mode, need to formalize this

    # Part 2
    # For example, here are several programs that take one input, compare it to
    # the value 8, and then produce one output:
     - 3,9,8,9,10,9,4,9,99,-1,8 - Using position mode, consider whether the
       input is equal to 8; output 1 (if it is) or 0 (if it is not).
     - 3,9,7,9,10,9,4,9,99,-1,8 - Using position mode, consider whether the
       input is less than 8; output 1 (if it is) or 0 (if it is not).
     - 3,3,1108,-1,8,3,4,3,99 - Using immediate mode, consider whether the
       input is equal to 8; output 1 (if it is) or 0 (if it is not).
     - 3,3,1107,-1,8,3,4,3,99 - Using immediate mode, consider whether the
       input is less than 8; output 1 (if it is) or 0 (if it is not).

    # With a custom stack for stdin/out testing would be easy, these could easily
    # be written as property based test with hypothesis (easy to prove)

    # Here are some jump tests that take an input, then output 0 if the input
    # was zero or 1 if the input was non-zero:
     - 3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9 (using position mode)
     - 3,3,1105,-1,9,1101,0,0,12,4,12,99,1 (using immediate mode)


    # Here's a larger example:
    3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
    1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
    999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99

    # The above example program uses an input instruction to ask for a single
    # number. The program will then output 999 if the input value is below 8,
    # output 1000 if the input value is equal to 8, or output 1001 if the input
    # value is greater than 8.
    """

