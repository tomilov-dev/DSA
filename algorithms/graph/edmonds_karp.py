from collections import deque
from collections import defaultdict


def edmonds_karp(
    graph: list[list[tuple[int, int]]],
    source: int,
    sink: int,
) -> float:
    def bfs(parent: list[int]):
        visited = [False] * n
        queue = deque()
        queue.append(source)
        visited[source] = True
        parent[source] = -1

        while queue:
            u = queue.popleft()
            for v, capacity in graph[u]:
                if not visited[v] and capacity - flow[u][v] > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
                    if v == sink:
                        return True
        return False

    # Нужно добавить обратные рёбра с capacity=0, если их нет,
    # Иначе DFS не увидит резидуальные обратные пути
    n = len(graph)
    for u in range(n):
        for v, cap in list(graph[u]):
            if not any(w == u for w, _ in graph[v]):
                graph[v].append((u, 0))

    flow = defaultdict(lambda: defaultdict(int))
    max_flow = 0
    parent = [-1] * n
    while bfs(parent):
        path_flow = float("inf")
        s = sink
        while s != source:
            for v, cap in graph[parent[s]]:
                if v == s:
                    path_flow = min(path_flow, cap - flow[parent[s]][s])
                    break
            s = parent[s]

        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            flow[u][v] += path_flow
            flow[v][u] -= path_flow
            v = u

    return max_flow


if __name__ == "__main__":
    graph = [
        [(1, 16), (2, 13)],
        [(2, 10), (3, 12)],
        [(1, 4), (4, 14)],
        [(2, 9), (5, 20)],
        [(3, 7), (5, 4)],
        [],
    ]
    print("Максимальный поток:", edmonds_karp(graph, 0, 5))
