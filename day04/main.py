"""
https://adventofcode.com/2022/day/4
"""

import typing


def main(filename: str) -> typing.Iterable[int]:
    """
    Advent of Code 2022 - Day 4
    """
    count_a = 0
    count_b = 0
    with open(filename, encoding="ascii") as handle:
        for line in handle:
            pair1, pair2 = line.strip().split(",")
            pair1_low, pair1_high = [int(x) for x in pair1.split("-")]
            pair2_low, pair2_high = [int(x) for x in pair2.split("-")]
            if (pair1_low >= pair2_low and pair1_high <= pair2_high) or (
                pair2_low >= pair1_low and pair2_high <= pair1_high
            ):
                count_a += 1
            if (pair1_low <= pair2_high and pair1_high >= pair2_low) or (
                pair2_low <= pair1_high and pair2_high >= pair1_low
            ):
                count_b += 1
    return count_a, count_b


def test():
    """
    Test the code
    """
    assert main("example_data.txt") == (2, 4)


if __name__ == "__main__":
    test()
    print(main("input_data.txt"))
