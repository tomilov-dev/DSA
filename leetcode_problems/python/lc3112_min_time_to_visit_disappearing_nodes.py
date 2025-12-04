import heapq
from collections import defaultdict


class Solution:
    def minimumTime(
        self,
        n: int,
        edges: list[list[int]],
        disappear: list[int],
    ) -> list[int]:
        def dij(init: int):
            MAX = 10**10
            distance = [MAX] * n
            distance[0] = 0

            heap = [(0, init)]
            while heap:
                curDist, v = heapq.heappop(heap)
                if curDist > distance[v]:
                    continue
                for u, weight in adj[v].items():
                    nextDist = distance[v] + weight
                    if nextDist >= disappear[u]:
                        continue
                    if distance[u] > nextDist:
                        distance[u] = nextDist
                        heapq.heappush(heap, (distance[u], u))
            return distance

        adj = defaultdict(dict)
        for u, v, w in edges:
            if v not in adj[u] or adj[u][v] > w:
                adj[u][v] = w
            if u not in adj[v] or adj[v][u] > w:
                adj[v][u] = w

        dist = dij(0)
        return [dist[i] if dist[i] < disappear[i] else -1 for i in range(n)]
