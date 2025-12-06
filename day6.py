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
        return list(map(list, zip(*(_.split() for _ in nums))))
    elif part == 2:
        nums = list(map(list, zip(*nums)))
        nums_grp = []
        grp = []
        finished = False
        for i, n in enumerate(nums):
            try:
                grp.append(int("".join(n)))
            except ValueError as e:
                finished = True
            if finished or i == len(nums) - 1:
                nums_grp.append(grp)
                grp = []
                finished = False
        return nums_grp
    else:
        raise ValueError(f"Unknown part '{part}'.")


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
