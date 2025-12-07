from typing import Literal
from sys import argv


def get_data(io: str, mode: Literal["file", "text"]="file") -> tuple[list[str], int]:
    match mode.lower():
        case "file":
            with open(io, mode="r", encoding="utf8") as fl:
                raw_data = fl.read()
        case "text":
            raw_data = io
        case _:
            raise ValueError(f"Unknown mode '{mode}'.")
    grid = [_ for _ in raw_data.split("\n") if 0 < len(_)]
    start = [i for i, val in enumerate(grid[0]) if val == "S"][0]
    return grid, start


def solve(grid: list[str], start: int) -> tuple[int, int]:
    split_count = 0
    timelines = [{start: 1}]
    curr_timeline = 0
    while curr_timeline < len(grid) - 1:
        timeline = {}
        for key in timelines[curr_timeline].keys():
            next_timeline = grid[curr_timeline + 1][key]
            if next_timeline == ".":
                timeline.setdefault(key, 0)
                timeline[key] += timelines[curr_timeline][key]
            else:
                split_count += 1
                timeline.setdefault(key - 1, 0)
                timeline[key - 1] += timelines[curr_timeline][key]
                timeline.setdefault(key + 1, 0)
                timeline[key + 1] += timelines[curr_timeline][key]
        timelines.append(timeline)
        curr_timeline += 1
    timeline_count = sum(val for val in timelines[-1].values())
    return split_count, timeline_count


if __name__ == "__main__":
    for part, solution in enumerate(solve(*get_data(*argv[1:])), 1):
        print(f"part {part}: {solution}")
