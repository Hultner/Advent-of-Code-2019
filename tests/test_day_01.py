from aoc.day_01.core import (
    part_1,
    part_2,
    launch_fuel_required,
    launch_fuel_for_fuel,
)


def verify_fuel(mass, fuel):
    assert fuel == launch_fuel_required(mass)


def verify_fuel_for_fuel(mass, fuel):
    assert fuel == launch_fuel_for_fuel(mass)


def test_fuel():
    """
     - For a mass of 12, divide by 3 and round down to get 4, then subtract 2
       to get 2.
     - For a mass of 14, dividing by 3 and rounding down still yields 4, so the
       fuel required is also 2.
     - For a mass of 1969, the fuel required is 654.
     - For a mass of 100756, the fuel required is 33583.
    """
    examples = (
        (12, 2),
        (14, 2),
        (1969, 654),
        (100756, 33583),
    )

    for (mass, fuel) in examples:
        verify_fuel(mass, fuel)


def test_fuel_for_fuel():
    examples = (
        (12, 2),
        (14, 2),
        (1969, 966),
        (100756, 50346),
    )

    for (mass, fuel) in examples:
        verify_fuel_for_fuel(mass, fuel)
