import heapq


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        adj: list[list[tuple[int, int]]] = [[] for _ in range(n)]
        for time in times:
            adj[time[0] - 1].append((time[1] - 1, time[2]))

        MAX = 10**10
        distance = [MAX] * n
        distance[k - 1] = 0

        heap = [(0, k - 1)]
        while len(heap) > 0:
            curDist, v = heapq.heappop(heap)
            if curDist > distance[v]:
                continue
            for u, w in adj[v]:
                if distance[u] > distance[v] + w:
                    distance[u] = distance[v] + w
                    heapq.heappush(heap, (distance[v], u))

        max_dist = max(distance)
        return -1 if max_dist == MAX else max_dist
