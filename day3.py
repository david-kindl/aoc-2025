from sys import argv
from typing import Literal


def get_data(io: str, mode: Literal["file", "text"] = "file") -> list[str]:
    if mode == "file":
        with open(io, mode="r", encoding="utf8") as fl:
            raw_data = fl.read()
    elif mode == "text":
        raw_data = io
    else:
        raise ValueError(f"Unknown mode '{mode}'.")
    return [line.strip() for line in raw_data.split() if line.strip()]


def get_max_joltage(data: list[str], bank_len: int) -> int:
    banks = []
    for d in data:
        bank = ""
        num_swaps = len(d) - bank_len
        i = 0
        while i < len(d) and len(bank) < bank_len:
            curr = d[i]
            swap = i
            for j in range(i + 1, min(i + num_swaps + 1, len(d))):
                if curr < d[j]:
                    curr = d[j]
                    swap = j
            num_swaps -= swap - i
            i = swap + 1
            bank += curr
        banks.append(int(bank))
    return sum(banks)


if __name__ == "__main__":
    d = get_data(*argv[1:])
    print(f"part 1: {get_max_joltage(d, 2)}")
    print(f"part 2: {get_max_joltage(d, 12)}")
