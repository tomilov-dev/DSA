import heapq


class SolutionMaxHeap:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        maxheap = []
        for i in range(m):
            for j in range(n):
                heapq.heappush(maxheap, -matrix[i][j])
                if len(maxheap) > k:
                    print(heapq.heappop(maxheap))
        return -heapq.heappop(maxheap)
