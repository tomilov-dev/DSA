import heapq


def prim(
    adj: list[list[tuple[int, int]]],
) -> tuple[list[tuple[int, int, int]], int]:
    n = len(adj)
    visited = [False] * n
    mst: list[tuple[int, int, int]] = []
    total_weight = 0

    visited[0] = True
    heap: list[tuple[int, int, int]] = []
    for w, v in adj[0]:
        heapq.heappush(heap, (w, 0, v))

    while heap and len(mst) < n - 1:
        w, u, v = heapq.heappop(heap)
        if visited[v]:
            continue
        visited[v] = True
        mst.append((u, v, w))
        total_weight += w
        for next_w, next_v in adj[v]:
            if not visited[next_v]:
                heapq.heappush(heap, (next_w, v, next_v))

    return mst, total_weight
