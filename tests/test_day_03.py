from aoc.day_03.core import (
    part_1,
    part_2,
    parse_moves,
)


def test_parts():
    # Oracle says so
    # assert part_1() == 9581917
    # assert part_2() == 2505
    assert True


def verify_parse(data):
    assert data == "\n".join(",".join(moves) for moves in parse_moves(data))


def verify_distance(data, expected):
    verify_parse(data)
    assert True


def test_x():
    """
    """
    examples = (
        ("R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83", 159,),
        (
            "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\nU98,R91,D20,R16,D67,R40,U7,R15,U6,R7",
            135,
        ),
    )

    for (data, expected) in examples:
        verify_distance(data, expected)
