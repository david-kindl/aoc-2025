from collections import defaultdict, deque
from tokenize import group

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


def euclidean_distance(p, q) -> int:
    if len(p) == len(q):
        return sum((p[n] - q[n]) ** 2 for n in range(len(p))) ** (1 / 2)
    else:
        raise ValueError(f"Length of {p} and {q} are not equal.")


def get_connections(boxes: set[tuple[int, ...]]) -> dict[tuple, tuple[tuple, float]]:
    conn = {}
    for box in junction_boxes:
        for other_box in junction_boxes:
            if box != other_box:
                dist = euclidean_distance(box, other_box)
                conn.setdefault(box, (other_box, dist))
                if conn[box][1] > dist:
                    conn[box] = (other_box, dist)
    return conn


def get_graph(conn: dict[tuple, tuple[tuple, float]]) -> defaultdict[tuple[int, ...], set[tuple[int, ...]]]:
    graph = defaultdict(set)
    for a, b in conn.items():
        graph[a].add(b[0])
        graph[b[0]].add(a)
    return graph


def bfs(graph):
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


if __name__ == "__main__":
    junction_boxes = {tuple(map(int, box.split(","))) for box in TEST.split("\n")}
    connections = get_connections(junction_boxes)
    print(sorted([(k, v) for k, v in connections.items()], key=lambda x: x[1][1]))
