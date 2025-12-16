MAX = 10**10  ## Определение случая, когда между вершинами нет ребра


def floyd_warshall(graph: list[list[int]]) -> list[list[int]]:
    n = len(graph)
    dist = [row[:] for row in graph]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] < MAX and dist[k][j] < MAX:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist
