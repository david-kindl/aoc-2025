

TEST = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

def get_input(is_test: bool = False) -> list[tuple[str, int]]:
    raw_input = []
    if is_test:
        raw_input = TEST.split("\n")
        print(raw_input)
    else:
        with open("./cache/day1.txt", mode="r", encoding="utf8") as fl:
            raw_input = fl.read().split("\n")
    return [(s[0], int(s[1:])) for s in raw_input]


def rotate(directions: list[tuple[str, int]], loc: int = 50) -> tuple[int, int, int]:
    stops, turns = 0, 0
    for d, clicks in directions:
        t, l = divmod(clicks, 100)
        turns += t
        if d == 'R':
            turns += (100 <= loc + l)
            loc = (loc + l) % 100
        else:
            turns += (loc and loc - l <= 0)
            loc = (loc - l) % 100

        if loc % 100 == 0:
            stops += 1

    return loc, stops, turns


if __name__ == '__main__':
    data = get_input()
    location, stop_count, turn_count = rotate(data)
    print(location, stop_count, turn_count)
