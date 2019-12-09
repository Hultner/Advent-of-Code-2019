from aoc.day_08.core import part_1, part_2, parse
from aoc.day_08.seed import p1

PART_2_ANSWER: str = """
█  █ ███  █  █ ████ ███  
█  █ █  █ █  █ █    █  █ 
█  █ ███  █  █ ███  █  █ 
█  █ █  █ █  █ █    ███  
█  █ █  █ █  █ █    █    
 ██  ███   ██  █    █    
"""


def test_parts():
    # Oracle says so
    assert part_1() == 1677
    assert part_2() == PART_2_ANSWER.strip("\n")
    assert True


def test_parse():
    assert p1 == "".join(str(x) for x in parse(p1))


def verify_x(data, expected):
    assert True


def test_x():
    """
    """
    examples = ((0, 1),)

    for (data, expected) in examples:
        verify_x(data, expected)
