"""
https://adventofcode.com/2022/day/1

Some friends have used oneliners like this:
https://github.com/jimmycallin/adventofcode/blob/main/2022/day01/main.py

I have a love hate relationship with oneliners. I don't find them readable for
production code but they are often very efficient. ~20/30% faster in this case.

I guess documenting the oneliner heavily can be a good compromise.
"""
import timeit


def problem_a():
    """
    The highest sum of integer blocks in the file.
    """
    block_total = 0
    largest_block = 0
    with open("input_data.txt", encoding="ascii") as handle:
        for line in handle:
            if line == "\n":
                if block_total > largest_block:
                    largest_block = block_total
                block_total = 0
            else:
                block_total += int(line)

    if block_total > largest_block:
        largest_block = block_total

    return largest_block


def problem_b():
    """
    The sum of the 3 largest blocks of integers in the file.
    """
    data = [0]
    with open("input_data.txt", encoding="ascii") as handle:
        for line in handle:
            if line == "\n":
                data.append(0)
            else:
                data[-1] += int(line)
    return sum(sorted(data)[-3:])


if __name__ == "__main__":
    print("Problem A:", problem_a())
    print(timeit.timeit(problem_a, number=100))

    print("Problem B:", problem_b())
    print(timeit.timeit(problem_b, number=100))
