import heapq


class Solution:
    def minimumCost(
        self,
        start: list[int],
        target: list[int],
        specialRoads: list[list[int]],
    ) -> int:
        def key(args: list[int]) -> tuple[int, int]:
            return (args[0], args[1])

        MAX = 10**10
        points: set[tuple[int, int]] = set()
        points.add(key(start))
        points.add(key(target))
        for x1, y1, x2, y2, _ in specialRoads:
            points.add((x1, y1))
            points.add((x2, y2))

        dist = {p: MAX for p in points}
        dist[key(start)] = 0

        heap = [(0, key(start))]
        while heap:
            cost, point = heapq.heappop(heap)
            for p in points:
                if p == point:
                    continue

                dst = cost + abs(point[0] - p[0]) + abs(point[1] - p[1])
                if dst < dist[p]:
                    dist[p] = dst
                    heapq.heappush(heap, (dst, p))

            for x1, y1, x2, y2, c in specialRoads:
                if point == (x1, y1):
                    dst = cost + c
                    p = (x2, y2)
                    if dst < dist[p]:
                        dist[p] = dst
                        heapq.heappush(heap, (dst, p))

        return dist[key(target)]
