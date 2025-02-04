import heapq


class Solution:
    def lastStoneWeight(
        self,
        stones: list[int],
    ) -> int:
        heap = [-stones[i] for i in range(len(stones))]
        heapq.heapify(heap)

        while heap:
            if len(heap) == 1:
                break

            bg = heapq.heappop(heap)
            sm = heapq.heappop(heap)
            if bg == sm:
                continue
            heapq.heappush(heap, bg - sm)

        return -heap[0] if heap else 0


if __name__ == "__main__":
    stones = [2, 7, 4, 1, 8, 1]
    stones = [1]
    print(Solution().lastStoneWeight(stones))
