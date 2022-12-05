"""
https://adventofcode.com/2022/day/3
"""

import typing


def main(filename: str) -> typing.Iterable[int]:
    """
    Advent of Code 2022 - Day 3
    """
    score_a = 0
    score_b = 0
    group_rucksacks = [set()] * 3
    with open(filename, encoding="ascii") as handle:
        for index, line in enumerate(handle):
            items = list(line.strip())
            midpoint = len(items) // 2
            intersection = set(items[:midpoint]) & set(items[midpoint:])
            assert len(intersection) == 1
            score_a += letter_to_priority(intersection.pop())

            group_index = index % 3
            group_rucksacks[group_index] = set(items)
            if group_index == 2:
                intersection = set.intersection(*group_rucksacks)
                assert len(intersection) == 1
                score_b += letter_to_priority(intersection.pop())

    return score_a, score_b


def letter_to_priority(letter: str) -> int:
    """
    Convert a letter to a priority

    As learned from a friend, this could use string.ascii_letters with a find()
    call + 1.
    """
    if len(letter) != 1:
        raise ValueError("letter must be a single character")

    number = ord(letter)
    if number < 91:
        return number - 38
    return number - 96


def tests():
    """
    Run tests
    """
    assert letter_to_priority("A") == 27
    assert letter_to_priority("Z") == 52
    assert letter_to_priority("a") == 1
    assert letter_to_priority("z") == 26


if __name__ == "__main__":
    tests()
    print(main("input_data.txt"))
