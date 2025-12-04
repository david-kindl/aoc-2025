from typing import Literal
import argparse


def get_data(io: str, mode: Literal["file", "text"] = "file") -> list[list[str]]:
    match mode.lower():
        case "file":
            with open("./cache/day4.txt", mode="r", encoding="utf8") as fl:
                raw_data = fl.read()
        case "text":
            raw_data = io
        case _:
            raise ValueError(f"Unknown mode '{mode}'.")
    return [[cell for cell in _] for _ in raw_data.split()]


def count_adjacent(grid: list[list[str]], x: int, y: int) -> int:
    adjacent = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    rows, cols = len(grid), len(grid[0])
    return sum(
        0 <= x + dx < rows
        and 0 <= y + dy < cols
        and grid[x + dx][y + dy] == "@"
        for dx, dy in adjacent
    )

def update_grid(grid: list[list[str]]) -> tuple[list[list[str]], int]:
    rows, cols = len(grid), len(grid[0])
    new_grid = [row.copy() for row in grid]
    counter = 0
    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == "@":
                if count_adjacent(grid, x, y) < 4:
                    new_grid[x][y] = "."
                    counter += 1
    return new_grid, counter


def use_forklift(grid: list[list[str]], replace: bool = False) -> int:
    total = 0
    while True:
        grid, changed = update_grid(grid)
        total += changed
        if changed == 0 or not replace:
            break
    return total


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Process grid from file or text input."
    )
    parser.add_argument(
        "input",
        nargs="?",
        default="./cache/day4.txt",
        help="Path to input file or (if mode=text) input text"
    )
    parser.add_argument(
        "--mode",
        choices=["file", "text"],
        default="file",
        help="Data read mode: 'file' for reading from file, 'text' for reading direct input text"
    )
    args = parser.parse_args()
    grid = get_data(args.input, mode=args.mode)
    print(f"part1: {use_forklift(grid)}")
    print(f"part2: {use_forklift(grid, True)}")
