from functools import cache, lru_cache
from typing import Literal
from sys import argv
import re


TEST = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""


def get_data(io: str, mode: Literal["file", "text"]="file") -> list[str]:
    match mode.lower():
        case "file":
            with open(io, mode="r", encoding="utf8") as fl:
                raw_data = fl.read()
        case "text":
            raw_data = io
        case _:
            raise ValueError(f"Unknown mode '{mode}'.")
    return [_ for _ in raw_data.split("\n") if 0 < len(_)]


def part1(grid: list[str]) -> int:
    counter = 0
    for i in range(1, len(grid)):
        repl = [c for c in grid[i]]
        for j in range(len(grid[0])):
            parent = grid[i - 1][j]
            current = grid[i][j]
            if parent in "S|":
                if current in "|.":
                    repl[j] = "|"
                else:
                    repl[j - 1], repl[j + 1] = "|", "|"
                    counter += 1
        grid[i] = "".join(repl)
    return counter


def solve(grid: list[str], start: int) -> tuple[int, int]:
    hier = [{start: 1}]
    curr_gen = 0
    split_count = 0
    while curr_gen < len(grid) - 1:
        next_gen = curr_gen + 1
        n = {}
        for key in hier[curr_gen].keys():
            successor = grid[next_gen][key]
            if successor == ".":
                n.setdefault(key, 0)
                n[key] += hier[curr_gen][key]
            else:
                split_count += 1
                n.setdefault(key - 1, 0)
                n[key - 1] += hier[curr_gen][key]
                n.setdefault(key + 1, 0)
                n[key + 1] += hier[curr_gen][key]
        hier.append(n)
        curr_gen += 1
    route_count = sum(val for val in hier[-1].values())
    return split_count, route_count


if __name__ == "__main__":
    grid = get_data(argv[1:])
    start = [i for i, val in enumerate(grid[0]) if val == "S"][0]
    for i, val in enumerate(solve(grid, start), 1):
        print(f"part {i}: {val}")
