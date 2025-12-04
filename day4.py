from typing import Literal


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


def use_forklift(grid: list[list[str]], replace: bool = False) -> int:
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    total = 0
    while True:
        counter = 0
        new_grid = grid
        for i, _ in enumerate(grid):
            for j, cell in enumerate(_):
                current_cell = grid[i][j]
                x_len, y_len = len(grid), len(_)
                if cell == "@":
                    neighbour_roll_counter = 0
                    for x, y in directions:
                        adj_x, adj_y = i + x, j + y
                        if 0 <= adj_x < x_len and 0 <= adj_y < y_len:
                            neighbour_roll_counter += (grid[adj_x][adj_y] in "@")
                    if neighbour_roll_counter < 4:
                        current_cell = "."
                        counter += 1
                new_grid[i][j] = current_cell
        total += counter
        grid = new_grid
        if counter == 0 or not replace:
            break
    return total


if __name__ == "__main__":
    print(f"part1: {use_forklift(get_data("./cache/day4.txt"))}")
    print(f"part2: {use_forklift(get_data("./cache/day4.txt"), True)}")