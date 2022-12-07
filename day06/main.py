"""
https://adventofcode.com/2022/day/5
"""

import typing


def main(filename: str, marker_func: typing.Callable) -> list[int]:
    """
    Main function
    """
    markers = []
    with open(filename, encoding="ascii") as handle:
        for line in handle.readlines():
            line = line.strip()
            marker = marker_func(line)
            markers.append(marker)
    return markers


def get_message_marker(data: str) -> int:
    """
    Get the message marker.
    """
    return get_marker(data, 14)


def get_packet_marker(data: str) -> int:
    """
    Get the packet marker.
    """
    return get_marker(data, 4)


def get_marker(data: str, length: int) -> int:
    """
    Get the marker.

    This is the index of character after the first character that is not a
    repeat of any of the X length previous characters.
    """
    for index in range(length, len(data)):
        if len({*data[index - length : index]}) == length:
            return index
    return -1


def test():
    """
    Test the main function
    """
    assert main("example_data.txt", get_packet_marker) == [7, 5, 6, 10, 11]
    assert main("example_data.txt", get_message_marker) == [19, 23, 23, 29, 26]


if __name__ == "__main__":
    test()
    print(main("input_data.txt", get_packet_marker))
    print(main("input_data.txt", get_message_marker))
