"""
https://adventofcode.com/2022/day/7
"""

from __future__ import annotations
import typing


class Directory:
    """
    Represents a directory on our filesystem. Basically a linked list of
    directories with each containing files.
    """

    def __init__(self, name: str, parent_directory: typing.Optional[Directory] = None):
        self.name = name
        self._files: typing.Dict[str, int] = {}
        self._subdirectories: typing.List[Directory] = []
        self._parent_directory: typing.Optional[Directory] = None
        self._size = None
        if parent_directory:
            self.set_parent_directory(parent_directory)

    def set_parent_directory(self, parent_directory: Directory) -> None:
        """
        Set the parent directory of this directory
        """
        if self._parent_directory == parent_directory:
            return
        self._parent_directory = parent_directory
        parent_directory.add_subdirectory(self)

    def add_subdirectory(self, subdirectory: Directory) -> None:
        """
        Add a subdirectory to this directory
        """
        if subdirectory in self._subdirectories:
            return
        self._subdirectories.append(subdirectory)
        subdirectory.set_parent_directory(self)
        self._size = None

    def add_file(self, filename: str, size: int) -> None:
        """
        Add a file to this directory
        """
        self._files[filename] = size
        self._size = None

    def get_size(self) -> int:
        """
        Get the size of this directory
        """
        if self._size is not None:
            return self._size

        self._size = sum(self._files.values()) + sum(
            subdirectory.get_size() for subdirectory in self.subdirectories()
        )
        return self._size

    def subdirectories(self) -> typing.Iterator[Directory]:
        """
        Iterate over all subdirectories
        """
        yield from self._subdirectories

    def subdirectories_recursively(self) -> typing.Iterator[Directory]:
        """
        Iterate over all subdirectories recursively
        """
        for subdirectory in self.subdirectories():
            yield subdirectory
            yield from subdirectory.subdirectories_recursively()

    def __repr__(self) -> str:
        return f"Directory({self.name}, {self._files}, {self._subdirectories})"


def parse_data(filename: str) -> Directory:
    """
    Parse data
    """
    current_path = []
    with open(filename, encoding="ascii") as handle:
        for line in handle:
            line = line.strip()
            tokens = line.split()
            if tokens[1] == "cd":
                if tokens[2] == "..":
                    current_path.pop()
                    continue
                directory = Directory(
                    tokens[2], current_path[-1] if current_path else None
                )
                current_path.append(directory)
            elif tokens[1] == "ls":
                continue
            elif tokens[0] == "dir":
                continue
            elif (size := tokens[0]).isdigit():
                current_path[-1].add_file(tokens[1], int(size))

    return current_path[0]


def main(
    filename: str, max_dir_size: int, file_system_size: int, free_space_needed: int
) -> typing.Tuple[int, int]:
    """
    Main function
    """
    directory = parse_data(filename)
    space_to_make = free_space_needed - (file_system_size - directory.get_size())

    directory_sizes = sorted(
        [directory.get_size()]
        + [d.get_size() for d in directory.subdirectories_recursively()]
    )

    return (
        sum([size for size in directory_sizes if size <= max_dir_size]),
        [size for size in directory_sizes if size >= space_to_make][0],
    )


def test():
    """
    Test function
    """
    assert main("example_data.txt", 100000, 70000000, 30000000) == (95437, 24933642)


if __name__ == "__main__":
    test()
    print(main("input_data.txt", 100000, 70000000, 30000000))
