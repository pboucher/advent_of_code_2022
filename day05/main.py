"""
https://adventofcode.com/2022/day/5
"""


class Stack:
    """
    Describes a stack of crates
    """

    def __init__(self):
        self._crates = []
        self.crate_count = 0

    def add_crate(self, crate: str):
        """
        Add a crate to the stack
        """
        if len(self._crates) == self.crate_count:
            self._crates.append(crate)
        else:
            self._crates[self.crate_count] = crate
        self.crate_count += 1

    def pop_crate(self) -> str:
        """
        Remove a crate from the stack
        """
        if self.crate_count == 0:
            raise IndexError("No crates on stack")
        self.crate_count -= 1
        return self._crates[self.crate_count]

    def top_crate(self) -> str:
        """
        Return the crate on top of the stack
        """
        if self.crate_count == 0:
            raise IndexError("No crates on stack")
        return self._crates[self.crate_count - 1]

    def __str__(self):
        return f"Stack({self.crate_count} - {self._crates})"

    def __repr__(self):
        return str(self)


class Ship:
    """
    Describes the ship with stacks of crates
    """

    def __init__(self, hold_state: str):
        data = hold_state.splitlines()
        stack_count = len(data[-1].split())

        self.hold = [Stack() for _ in range(stack_count)]

        for line in data[-2::-1]:
            for col in range(stack_count):
                crate = line[col * 4 + 1]
                if crate != " ":
                    self.hold[col].add_crate(crate)

    def process_operations(self, operations: str, mode: str = "A"):
        """
        Mutates the ship according to the operations
        """
        for line in operations.splitlines():
            _, count, _, from_stack, _, to_stack = line.split()

            if mode == "A":
                # Problem A
                for _ in range(int(count)):
                    self.hold[int(to_stack) - 1].add_crate(
                        self.hold[int(from_stack) - 1].pop_crate()
                    )
            elif mode == "B":
                # Problem B
                pile = []
                for _ in range(int(count)):
                    pile.insert(0, self.hold[int(from_stack) - 1].pop_crate())
                for crate in pile:
                    self.hold[int(to_stack) - 1].add_crate(crate)
            else:
                raise ValueError(f"Unknown mode: {mode}")

    def top_crates(self):
        """
        Returns the top crates of all stacks
        """
        return "".join([stack.top_crate() for stack in self.hold])

    def __str__(self):
        return f"Ship({self.hold})"

    def __repr__(self):
        return str(self)


def process_data(filename: str, mode: str) -> str:
    """
    Advent of Code 2022 - Day 05
    """
    data = open(filename, encoding="ascii").read()
    hold_state, operations = data.split("\n\n")

    ship = Ship(hold_state)
    ship.process_operations(operations, mode)

    return ship.top_crates()


def test():
    """
    Test the code
    """
    assert process_data("example_data.txt", "A"), "CMZ"
    assert process_data("example_data.txt", "B"), "MCD"


if __name__ == "__main__":
    test()
    print(process_data("input_data.txt", "A"))
    print(process_data("input_data.txt", "B"))
