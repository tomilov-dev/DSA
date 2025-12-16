"""
Поиск кратчайшего пути в неориентированном графе через BFS
"""

from collections import deque


def shortest_path_direct(graph: list[list[int]], x: int, y: int) -> int:
    n = len(graph)
    MAX = n * n

    color = [0] * n
    distance = [MAX] * n

    color[x] = 1
    distance[x] = 0
    q = deque([x])
    while q:
        v = q.popleft()
        for u, conn in enumerate(graph[v]):
            if conn == 1 and color[u] == 0:
                color[u] = 1
                distance[u] = 1 + distance[v]
                q.append(u)
        color[v] = 2
    return distance[y] if distance[y] != MAX else -1
