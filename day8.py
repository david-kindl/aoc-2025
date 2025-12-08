from collections import defaultdict, deque
from itertools import combinations
from operator import mul
from functools import reduce
from typing import Literal
from sys import argv


TEST = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""


def get_boxes(io: str, mode: Literal["file", "text"] = "file") -> set[tuple[int, ...]]:
    match mode.lower():
        case "file":
            with open(io, mode="r", encoding="utf8") as fl:
                raw_data = fl.read()
        case "text":
            raw_data = io
        case _:
            raise ValueError(f"Unknown mode '{mode}'.")
    return {tuple(map(int, box.split(","))) for box in raw_data.split("\n")}


def euclidean_distance(p, q) -> int:
    if len(p) == len(q):
        return sum((p[n] - q[n]) ** 2 for n in range(len(p))) ** (1 / 2)
    else:
        raise ValueError(f"Length of {p} and {q} are not equal.")


def get_distance_rank(boxes, n: int) -> dict[int, list[tuple[int, ...]]]:
    distances = {}
    for box1, box2 in combinations(boxes, 2):
        distance = euclidean_distance(box1, box2)
        distances[distance] = sorted([box1, box2])
    return dict(sorted(distances.items())[:n])


def build_graph(boxes: dict[int, list[tuple[int, ...]]]) -> defaultdict[tuple[int, ...], list[tuple[int, ...]]]:
    d = defaultdict(list)
    for distance, pairs in boxes.items():
        cord1, cord2 = pairs
        d[cord1].append(cord2)
        d[cord2].append(cord1)
    return d


def get_circuits(graph: defaultdict[tuple[int, ...], list[tuple[int, ...]]]):
    def bfs():
        visited = set()
        circuits = []

        for node in graph:
            if node not in visited:
                queue = deque([node])
                circuit = set()

                while queue:
                    n = queue.popleft()
                    if n in visited:
                        continue
                    visited.add(n)
                    circuit.add(n)
                    queue.extend(graph[n])
                circuits.append(circuit)
        return circuits

    circuits = bfs()
    return sorted([circuit for circuit in circuits], key=lambda x: len(x), reverse=True)


if __name__ == "__main__":
    junction_boxes = get_boxes(*argv[1:])
    distances = get_distance_rank(junction_boxes, 1000)
    graph = build_graph(distances)
    print(reduce(mul, [len(circuit) for circuit in get_circuits(graph)[:3]]))
