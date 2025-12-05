from typing import Literal
from sys import argv


TEST = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

def get_data(io: str, mode: Literal["file", "text"] = "file") -> tuple[list[tuple[int, ...]], list[int]]:
    match mode.lower():
        case "file":
            with open(io, mode="r", encoding="utf8") as fl:
                raw_data = fl.read()
        case "text":
            raw_data = io
        case _:
            raise ValueError(f"Unknown mode '{mode}'.")

    ranges, ids = raw_data.split("\n\n")
    ranges = [tuple(map(int, _.split("-"))) for _ in ranges.splitlines()]
    ids = list(map(int, ids.splitlines()))
    return ranges, ids


def get_fresh_ids(ranges: list[tuple[int, ...]], ids: list[int]) -> list[int]:
    fresh_ids = []
    for id in ids:
        for start, end in ranges:
            if start <= id <= end:
                fresh_ids.append(id)
                break
    return fresh_ids


def get_overlapping_ranges(ranges: list[tuple[int, ...]]) -> list[tuple[int, ...]]:
    ranges = sorted(ranges, key=lambda x: x[0])
    to_visit = [True for _ in range(len(ranges))]
    merged = []
    for i in range(len(ranges)):
        if to_visit[i]:
            to_visit[i] = False
            cs, ce = ranges[i]
            for j in range(i + 1, len(ranges)):
                ns, ne = ranges[j]
                if cs <= ns <= ce or ns <= cs <= ne:
                    to_visit[j] = False
                    cs, ce = min(cs, ns), max(ce, ne)
            merged.append((cs, ce))
    return merged

if __name__ == "__main__":
    ranges, ids = get_data(*argv[1:])
    fresh = get_fresh_ids(ranges, ids)
    print(f"Part 1: {len(fresh)}")
    print(f"Part 2: {sum([e + 1 - s for s, e in get_overlapping_ranges(ranges)])}")