def bellman_ford(
    edges: list[tuple[int, int, int]],
    n: int,
    start: int,
) -> list[int] | None:
    MAX = 10**10
    dist = [MAX] * n
    dist[start] = 0
    for i in range(n):
        for src, tgt, wgt in edges:
            if dist[src] != MAX and dist[tgt] > dist[src] + wgt:
                dist[tgt] = dist[src] + wgt
                if i == n - 1:
                    # Проверка на отрицательный цикл
                    return None
    return dist
