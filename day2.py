import re
import math


TEST = ("11-22,95-115,998-1012,1188511880-1188511890,"
        "222220-222224,1698522-1698528,446443-446449,"
        "38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124")


def get_data(io: str) -> list[list[int]]:
    try:
        with open(io, mode="r", encoding="utf8") as fl:
            raw_data = fl.read()
    except FileNotFoundError:
        raw_data = io
    return [list(map(int, pair.split("-"))) for pair in raw_data.split(",")]


def get_invalid_ids(data: list[list[int]]) -> tuple[int, int]:
    ids1 = 0
    ids2 = 0
    pattern1 = r"^(\d+)\1$"
    pattern2 = r"^(\d+)\1+$"
    for lb, ub in data:
        for i in range(lb, ub + 1):
            currval = str(i)
            ids1 += i if re.match(pattern1, currval) else 0
            ids2 += i if re.match(pattern2, currval) else 0
    return ids1, ids2


if __name__ == "__main__":
    print(get_invalid_ids(get_data(TEST)))
    print(get_invalid_ids(get_data("./cache/day2.txt")))