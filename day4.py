from itertools import permutations

TEST = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

directions = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1)
]

with open("./cache/day4.txt", mode="r", encoding="utf8") as fl:
    raw_data = fl.read()

data = [[cell for cell in _] for _ in TEST.split()]


counter = 0
for i, _ in enumerate(data):
    for j, cell in enumerate(_):
        if cell == "@":
            roll_counter = 0
            for x, y in directions:
                adj_x, adj_y = i + x, j + y
                if 0 <= adj_x < len(data) and 0 <= adj_y < len(_):
                    roll_counter += (data[adj_x][adj_y] in "@x")
            if roll_counter < 4:
                data[i][j] = "x"
                counter += 1
print(counter)
print("\n".join(["".join(_) for _ in data]))

with open("./cache/day4.txt", mode="r", encoding="utf8") as fl:
    raw_data = fl.read()

data = [[cell for cell in _] for _ in raw_data.split()]

total = 0
while True:
    counter = 0
    new_grid = data
    for i, _ in enumerate(data):
        for j, cell in enumerate(_):
            repl = data[i][j]
            if cell == "@":
                roll_counter = 0
                for x, y in directions:
                    adj_x, adj_y = i + x, j + y
                    if 0 <= adj_x < len(data) and 0 <= adj_y < len(_):
                        roll_counter += (data[adj_x][adj_y] in "@")
                if roll_counter < 4:
                    repl = "."
                    counter += 1
            new_grid[i][j] = repl
    total += counter
    data = new_grid
    print(counter)
    if counter == 0:
        break

print(total)