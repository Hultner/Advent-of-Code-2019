from aoc.day_04.core import (
    part_1,
    part_2,
    verify_password,
    verify_password_p2,
)


def test_parts():
    # Oracle says so
    assert part_1() == 1929
    assert part_2() == 1306


def verify_pw_test(data, expected):
    assert expected == verify_password(str(data))

def verify_pw_test_2(data, expected):
    assert expected == verify_password_p2(str(data))



def test_passwords():
    """
    """
    examples = (
        (111_111, True),
        (223_450, False),
        (123_789, False),
    )

    examples_2= (
        (111111, False),
        (112233, True),
        (123444, False),
        (111122, True),
    )

    for (data, expected) in examples:
        verify_pw_test(data, expected)

    for (data, expected) in examples_2:
        verify_pw_test_2(data, expected)
