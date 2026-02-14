from collections import defaultdict


def ford_fulkerson(
    graph: list[list[tuple[int, int]]],
    source: int,
    sink: int,
) -> float:
    def dfs(u: int, min_capacity: float, visited: list[bool]) -> float:
        if u == sink:
            return min_capacity
        visited[u] = True
        for v, capacity in graph[u]:
            if not visited[v] and capacity - flow[u][v] > 0:
                residual = capacity - flow[u][v]
                if residual > 0:
                    path_flow = dfs(v, min(min_capacity, residual), visited)
                    if path_flow > 0:
                        flow[u][v] += path_flow  # type: ignore
                        flow[v][u] -= path_flow  # type: ignore
                        return path_flow
        return 0

    # Нужно добавить обратные рёбра с capacity=0, если их нет,
    # Иначе DFS не увидит резидуальные обратные пути
    n = len(graph)
    for u in range(n):
        for v, cap in list(graph[u]):
            if not any(w == u for w, _ in graph[v]):
                graph[v].append((u, 0))

    flow = defaultdict(lambda: defaultdict(int))
    max_flow = 0
    while True:
        visited = [False] * n
        path_flow = dfs(source, float("inf"), visited)
        if path_flow == 0:
            break
        max_flow += path_flow
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
    print("Максимальный поток:", ford_fulkerson(graph, 0, 5))
