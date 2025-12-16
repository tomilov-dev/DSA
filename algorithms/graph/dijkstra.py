import heapq


def dijkstra(graph: list[list[tuple[int, int]]], init: int) -> list[int]:
    n = len(graph)
    MAX = 10**10
    distance = [MAX] * n
    distance[init] = 0

    heap = [(0, init)]
    while heap:
        curDist, v = heapq.heappop(heap)
        if curDist > distance[v]:
            continue
        for u, weight in graph[v]:
            if distance[u] > distance[v] + weight:
                distance[u] = distance[v] + weight
                heapq.heappush(heap, (distance[u], u))
    return distance
