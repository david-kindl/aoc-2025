import itertools
from typing import Literal
from operator import mul
from functools import reduce
from itertools import product
from sys import argv


def get_data(io: str, mode: Literal["file", "text"]="file") -> tuple[list[str], list[str]]:
    match mode.lower():
        case "file":
            with open(io, mode="r", encoding="utf8") as fl:
                raw_data = fl.read()
        case "text":
            raw_data = io
        case _:
            raise ValueError(f"Unknown mode '{mode}'.")
    raw_data = [_ for _ in raw_data.split("\n") if 0 < len(_)]
    return raw_data[:-1], raw_data[-1].split()


def stdize(part: int, nums: list[str]):
    if part == 1:
        nums = list(map(list, zip(*(_.split() for _ in nums))))
    elif part == 2:
        nums = list(map(list, zip(*nums)))
        tmp = []
        curr = []
        for n in nums:
            try:
                curr.append(int("".join(n)))
            except ValueError as e:
                tmp.append(curr)
                curr = []
        tmp.append(curr)
        nums = tmp
    else:
        raise ValueError(f"Unknown part '{part}'.")

    return nums


def solve(part: int, nums: list[str], signs: list[str]) -> int:
    nums = stdize(part, nums)
    total = 0
    for i, s in enumerate(signs):
        curr = map(int, nums[i])
        if s == "+":
            total += sum(curr)
        elif s == "*":
            total += reduce(mul, curr)
    return total


if __name__ == '__main__':
    nums, signs = get_data(*argv[1:])
    print(f"part1: {solve(1, nums, signs)}")
    print(f"part2: {solve(2, nums, signs)}")