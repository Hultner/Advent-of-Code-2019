from typing import NoReturn
from aoc.day_01 import core as day_01


def main() -> NoReturn:
    puzzles: Tuple = ((day_01.part_1(), day_01.part_2()),)

    for (day, parts) in enumerate(puzzles, start=1):
        print(f"Day {day}:")
        for (part, result) in enumerate(parts, start=1):
            print(f"\tPart {part}: {result}")

    return None


if __name__ == "__main__":
    main()
