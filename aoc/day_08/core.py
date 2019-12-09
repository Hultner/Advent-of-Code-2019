"""
--- Day 8: Space Image Format ---

The Elves' spirits are lifted when they realize you have an opportunity to
reboot one of their Mars rovers, and so they are curious if you would spend a
brief sojourn on Mars. You land your ship near the rover.

When you reach the rover, you discover that it's already in the process of
rebooting! It's just waiting for someone to enter a BIOS password. The Elf
responsible for the rover takes a picture of the password (your puzzle input)
and sends it to you via the Digital Sending Network.

Unfortunately, images sent via the Digital Sending Network aren't encoded with
any normal encoding; instead, they're encoded in a special Space Image Format.
None of the Elves seem to remember why this is the case. They send you the
instructions to decode it.
"""
import logging
from numbers import Number
from typing import Tuple, Iterable, List, NoReturn, Dict
from dataclasses import dataclass, field

from more_itertools import ilen
from toolz import pipe, curry

from aoc.day_08.seed import p1

WIDTH = 25
HEIGHT = 6

# We need a curried version of min
min = curry(min)


render_map = {
    1: "█",
    0: " ",
    2: "",
}


def parse(data: str) -> Iterable[int]:
    """Returns a list of digits form string `data`"""
    # List instead of generator since we wil slice it later
    return [int(x) for x in data]


@curry
def vector_to_matrix(vec: List[int], x: int = WIDTH, y: int = HEIGHT):
    """Returns a `x` by `y` matrix of reshaped `vec` data"""
    return (vec[i : i + (x * y)] for i in range(0, len(vec), x * y))


def compose(layers):
    """Returns composed pixels from layer stack"""
    return (
        next(value for value in layer if value != 2)
        for layer in zip(*layers)
    )


def __render_row(pixels: List[int]) -> str:
    """Returns a List of ints as rendered string"""
    return "".join(render_map.get(pixel) for pixel in pixels)


def render(layers: List[List[int]]):
    """Returns a string rendered version of int matrix"""
    return "\n".join(
        __render_row(pixels) for pixels in layers
    )


@curry
def count(value, vector):
    """
    Returns number of instaces of `value` in `vector`
    """
    return sum(1 for num in vector if num == value)


def part_1(puzzle_input: Tuple[Number] = p1) -> Number:
    """
    Images are sent as a series of digits that each represent the color of a
    single pixel. The digits fill each row of the image left-to-right, then
    move downward to the next row, filling rows top-to-bottom until every pixel
    of the image is filled.

    Each image actually consists of a series of identically-sized layers that
    are filled in this way. So, the first digit corresponds to the top-left
    pixel of the first layer, the second digit corresponds to the pixel to the
    right of that on the same layer, and so on until the last digit, which
    corresponds to the bottom-right pixel of the last layer.

    For example, given an image 3 pixels wide and 2 pixels tall, the image data
    123456789012 corresponds to the following image layers:

    Layer 1: 123
             456

    Layer 2: 789
             012

    The image you received is 25 pixels wide and 6 pixels tall.

    To make sure the image wasn't corrupted during transmission, the Elves
    would like you to find the layer that contains the fewest 0 digits. On that
    layer, what is the number of 1 digits multiplied by the number of 2 digits?
    """
    return pipe(
        p1,
        parse,
        vector_to_matrix,
        min(key=count(0)),
        # Not my most idomatic python code
        lambda v: count(1, v) * count(2, v),
    )


def part_2(puzzle_input: Tuple[Number] = p1) -> Number:
    """
    --- Part Two ---

    Now you're ready to decode the image. The image is rendered by stacking the
    layers and aligning the pixels with the same positions in each layer. The
    digits indicate the color of the corresponding pixel: 0 is black, 1 is
    white, and 2 is transparent.

    The layers are rendered with the first layer in front and the last layer in
    back. So, if a given position has a transparent pixel in the first and
    second layers, a black pixel in the third layer, and a white pixel in the
    fourth layer, the final image would have a black pixel at that position.

    For example, given an image 2 pixels wide and 2 pixels tall, the image data
    0222112222120000 corresponds to the following image layers:

    Layer 1: 02
             22

    Layer 2: 11
             22

    Layer 3: 22
             12

    Layer 4: 00
             00

    Then, the full image can be found by determining the top visible pixel in
    each position:

     - The top-left pixel is black because the top layer is 0.
     - The top-right pixel is white because the top layer is 2 (transparent),
       but the second layer is 1.
     - The bottom-left pixel is white because the top two layers are 2, but the
       third layer is 1.
     - The bottom-right pixel is black because the only visible pixel in that
       position is 0 (from layer 4).

    So, the final image looks like this:

    01
    10

    What message is produced after decoding your image?
    """
    return pipe(
        p1,
        parse,
        vector_to_matrix,
        compose,
        list,
        vector_to_matrix(y=1),
        render,
    )


if __name__ == "__main__":
    from pprint import pprint

    print(part_1())
    print(part_2())
